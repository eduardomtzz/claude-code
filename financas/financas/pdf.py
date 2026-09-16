"""Extracao de texto de PDF, sem dependencias externas.

O ambiente nao tem pypdf nem pdftotext e o indice do pip esta inacessivel, e
uma fatura de cartao e a proxima fonte de dados. Este modulo le o suficiente de
PDF para reconstruir as linhas de texto de cada pagina, que e tudo que um
extrator de fatura precisa.

O que ele cobre:

* objetos indiretos, inclusive dentro de fluxos de objetos (``/ObjStm``), que
  todo PDF moderno usa;
* fluxos comprimidos com ``FlateDecode``, com os preditores PNG;
* o mapa ``/ToUnicode`` de fontes com subconjunto, sem o qual o texto sai como
  sequencia de indices de glifo em vez de letras;
* posicionamento do texto, para remontar as linhas na ordem em que estao na
  pagina em vez de na ordem em que aparecem no fluxo.

O que ele nao cobre: criptografia, PDF linearizado com xref quebrado, texto em
imagem. Uma fatura de banco nao usa nada disso.
"""

from __future__ import annotations

import re
import zlib
from dataclasses import dataclass, field

#: Tolerancia vertical, em pontos, para duas marcas de texto irem para a mesma
#: linha. Sobrescritos e pequenas variacoes de baseline cabem aqui.
TOLERANCIA_LINHA = 2.5

#: Fracao do tamanho da fonte a partir da qual o vao entre dois trechos vira um
#: espaco. Abaixo disso o vao e so o espacamento entre letras da mesma palavra.
FRACAO_DE_ESPACO = 0.28

#: Largura media de um glifo, como fracao do tamanho da fonte. Serve para
#: estimar onde um trecho termina sem ler a tabela de larguras da fonte.
LARGURA_MEDIA = 0.5

_OBJETO = re.compile(rb"(\d+)\s+(\d+)\s+obj\b")
_FLUXO = re.compile(rb"stream\r?\n?", re.MULTILINE)


class ErroDePDF(Exception):
    """O arquivo nao e um PDF legivel por este extrator."""


# --------------------------------------------------------------------------
# Objetos
# --------------------------------------------------------------------------


@dataclass
class Objeto:
    numero: int
    dicionario: bytes           # o dicionario bruto, entre << e >>
    fluxo: bytes | None = None  # o conteudo do stream, ja descomprimido


def _valor(dicionario: bytes, nome: bytes) -> bytes | None:
    """Le o valor cru de uma chave do dicionario, sem interpretar o tipo.

    Feito a mao, e nao por expressao regular, porque o valor pode ser um nome
    (``/FlateDecode``), um dicionario aninhado ou um vetor -- e uma regex que
    para na proxima barra devolve string vazia justamente no caso do nome, que
    e o mais comum.
    """
    chave_bytes = b"/" + nome
    posicao = 0
    while True:
        posicao = dicionario.find(chave_bytes, posicao)
        if posicao == -1:
            return None
        seguinte = dicionario[posicao + len(chave_bytes):posicao + len(chave_bytes) + 1]
        # Evita casar /Type quando a chave procurada e /Typ.
        if seguinte and (seguinte.isalnum() or seguinte == b"#"):
            posicao += len(chave_bytes)
            continue
        break

    i = posicao + len(chave_bytes)
    while i < len(dicionario) and dicionario[i:i + 1].isspace():
        i += 1
    if i >= len(dicionario):
        return None

    if dicionario[i:i + 2] == b"<<":
        return dicionario[i:_fim_do_par(dicionario, i, b"<<", b">>")]
    if dicionario[i:i + 1] == b"[":
        return dicionario[i:_fim_do_par(dicionario, i, b"[", b"]")]
    if dicionario[i:i + 1] == b"/":
        achado = re.match(rb"/[^\s/\[\]<>()]*", dicionario[i:])
        return achado.group(0)
    achado = re.match(rb"[^/<>\[\]]+", dicionario[i:])
    return achado.group(0).strip() if achado else None


def _fim_do_par(dados: bytes, inicio: int, abre: bytes, fecha: bytes) -> int:
    """Indice logo apos o delimitador que fecha o par aberto em ``inicio``."""
    profundidade, i, passo = 0, inicio, len(abre)
    while i < len(dados):
        if dados[i:i + passo] == abre:
            profundidade += 1
            i += passo
            continue
        if dados[i:i + len(fecha)] == fecha:
            profundidade -= 1
            i += len(fecha)
            if profundidade == 0:
                return i
            continue
        i += 1
    return len(dados)


def _inteiro(dicionario: bytes, nome: bytes) -> int | None:
    bruto = _valor(dicionario, nome)
    if not bruto:
        return None
    achado = re.match(rb"(\d+)", bruto)
    return int(achado.group(1)) if achado else None


def _referencias(bruto: bytes) -> list[int]:
    """Numeros dos objetos referenciados por ``12 0 R``."""
    return [int(n) for n in re.findall(rb"(\d+)\s+\d+\s+R\b", bruto)]


def _aplicar_preditor(dados: bytes, parametros: bytes) -> bytes:
    """Desfaz o preditor PNG, usado por fluxos de xref e de objetos."""
    preditor = _inteiro(parametros, b"Predictor") or 1
    if preditor < 10:
        return dados
    colunas = _inteiro(parametros, b"Columns") or 1
    cores = _inteiro(parametros, b"Colors") or 1
    bits = _inteiro(parametros, b"BitsPerComponent") or 8
    amostra = max(1, (cores * bits) // 8)
    largura = colunas * cores * bits // 8

    saida = bytearray()
    anterior = bytearray(largura)
    passo = largura + 1
    for inicio in range(0, len(dados) - largura, passo):
        tipo = dados[inicio]
        linha = bytearray(dados[inicio + 1:inicio + 1 + largura])
        if tipo == 1:
            for i in range(amostra, largura):
                linha[i] = (linha[i] + linha[i - amostra]) & 0xFF
        elif tipo == 2:
            for i in range(largura):
                linha[i] = (linha[i] + anterior[i]) & 0xFF
        elif tipo == 3:
            for i in range(largura):
                esquerda = linha[i - amostra] if i >= amostra else 0
                linha[i] = (linha[i] + ((esquerda + anterior[i]) >> 1)) & 0xFF
        elif tipo == 4:
            for i in range(largura):
                a = linha[i - amostra] if i >= amostra else 0
                b = anterior[i]
                c = anterior[i - amostra] if i >= amostra else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                melhor = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                linha[i] = (linha[i] + melhor) & 0xFF
        saida += linha
        anterior = linha
    return bytes(saida)


def _descomprimir(dicionario: bytes, bruto: bytes) -> bytes | None:
    filtros = _valor(dicionario, b"Filter") or b""
    if b"FlateDecode" not in filtros:
        # Sem compressao, ou com um filtro que nao interessa a texto.
        return bruto if not filtros.strip() else None
    try:
        dados = zlib.decompress(bruto)
    except zlib.error:
        try:
            dados = zlib.decompressobj().decompress(bruto)
        except zlib.error:
            return None
    parametros = _valor(dicionario, b"DecodeParms")
    if parametros and b"Predictor" in parametros:
        dados = _aplicar_preditor(dados, parametros)
    return dados


class DocumentoPDF:
    """Indexa os objetos de um PDF e devolve o texto de cada pagina."""

    def __init__(self, dados: bytes):
        if not dados.startswith(b"%PDF"):
            raise ErroDePDF("nao comeca com %PDF")
        self._dados = dados
        self.objetos: dict[int, Objeto] = {}
        self._indexar()
        self._expandir_fluxos_de_objetos()

    @classmethod
    def de_arquivo(cls, caminho) -> "DocumentoPDF":
        with open(caminho, "rb") as arquivo:
            return cls(arquivo.read())

    # -- indexacao -------------------------------------------------------
    def _indexar(self) -> None:
        for achado in _OBJETO.finditer(self._dados):
            numero = int(achado.group(1))
            inicio = achado.end()
            fim = self._dados.find(b"endobj", inicio)
            if fim == -1:
                continue
            corpo = self._dados[inicio:fim]
            dicionario = self._dicionario_de(corpo)
            fluxo = None
            marca = _FLUXO.search(corpo)
            if marca:
                bruto = corpo[marca.end():]
                final = bruto.rfind(b"endstream")
                if final != -1:
                    bruto = bruto[:final].rstrip(b"\r\n")
                tamanho = _inteiro(dicionario, b"Length")
                if tamanho and tamanho <= len(bruto):
                    bruto = bruto[:tamanho]
                fluxo = _descomprimir(dicionario, bruto)
            self.objetos[numero] = Objeto(numero, dicionario, fluxo)

    @staticmethod
    def _dicionario_de(corpo: bytes) -> bytes:
        inicio = corpo.find(b"<<")
        if inicio == -1:
            return b""
        profundidade, i = 0, inicio
        while i < len(corpo) - 1:
            par = corpo[i:i + 2]
            if par == b"<<":
                profundidade += 1
                i += 2
                continue
            if par == b">>":
                profundidade -= 1
                i += 2
                if profundidade == 0:
                    return corpo[inicio:i]
                continue
            i += 1
        return corpo[inicio:]

    def _expandir_fluxos_de_objetos(self) -> None:
        """Um ``/ObjStm`` guarda varios objetos comprimidos juntos."""
        for objeto in list(self.objetos.values()):
            if b"/ObjStm" not in objeto.dicionario or not objeto.fluxo:
                continue
            quantidade = _inteiro(objeto.dicionario, b"N") or 0
            primeiro = _inteiro(objeto.dicionario, b"First") or 0
            cabecalho = objeto.fluxo[:primeiro].split()
            corpo = objeto.fluxo[primeiro:]
            for i in range(quantidade):
                try:
                    numero = int(cabecalho[i * 2])
                    deslocamento = int(cabecalho[i * 2 + 1])
                except (IndexError, ValueError):
                    break
                fim = (
                    int(cabecalho[(i + 1) * 2 + 1])
                    if (i + 1) * 2 + 1 < len(cabecalho) else len(corpo)
                )
                trecho = corpo[deslocamento:fim]
                if numero not in self.objetos:
                    self.objetos[numero] = Objeto(
                        numero, self._dicionario_de(trecho) or trecho
                    )

    # -- paginas ---------------------------------------------------------
    @property
    def paginas(self) -> list[Objeto]:
        return [
            objeto for objeto in self.objetos.values()
            if re.search(rb"/Type\s*/Page\b", objeto.dicionario)
        ]

    def _conteudo_da_pagina(self, pagina: Objeto) -> bytes:
        bruto = _valor(pagina.dicionario, b"Contents") or b""
        partes = []
        for numero in _referencias(bruto):
            alvo = self.objetos.get(numero)
            if alvo and alvo.fluxo:
                partes.append(alvo.fluxo)
        return b"\n".join(partes)

    def _fontes_da_pagina(self, pagina: Objeto) -> dict[bytes, dict[int, str]]:
        """Mapa ``/F1`` -> tabela de codigo para caractere, quando existir."""
        recursos = _valor(pagina.dicionario, b"Resources") or b""
        dicionario_recursos = recursos
        for numero in _referencias(recursos):
            alvo = self.objetos.get(numero)
            if alvo:
                dicionario_recursos = alvo.dicionario
                break

        bloco = re.search(rb"/Font\s*<<(.*?)>>", dicionario_recursos, re.S)
        if not bloco:
            for numero in _referencias(_valor(dicionario_recursos, b"Font") or b""):
                alvo = self.objetos.get(numero)
                if alvo:
                    bloco = re.match(rb"<<(.*)>>", alvo.dicionario, re.S)
                    break
        if not bloco:
            return {}

        fontes: dict[bytes, dict[int, str]] = {}
        for nome, numero in re.findall(rb"/(\w+)\s+(\d+)\s+\d+\s+R", bloco.group(1)):
            fonte = self.objetos.get(int(numero))
            if not fonte:
                continue
            fontes[b"/" + nome] = self._tabela_unicode(fonte)
        return fontes

    def _tabela_unicode(self, fonte: Objeto) -> dict[int, str]:
        bruto = _valor(fonte.dicionario, b"ToUnicode") or b""
        for numero in _referencias(bruto):
            alvo = self.objetos.get(numero)
            if alvo and alvo.fluxo:
                return _ler_cmap(alvo.fluxo)
        return {}

    # -- texto -----------------------------------------------------------
    def linhas(self) -> list[list[str]]:
        """Linhas de texto de cada pagina, na ordem visual."""
        return [
            _agrupar_em_linhas(
                _extrair_marcas(
                    self._conteudo_da_pagina(pagina), self._fontes_da_pagina(pagina)
                )
            )
            for pagina in self.paginas
        ]

    def texto(self) -> str:
        return "\n".join(
            "\n".join(pagina) for pagina in self.linhas()
        )


# --------------------------------------------------------------------------
# CMap de ToUnicode
# --------------------------------------------------------------------------

_BFCHAR = re.compile(rb"beginbfchar(.*?)endbfchar", re.S)
_BFRANGE = re.compile(rb"beginbfrange(.*?)endbfrange", re.S)
_HEX = re.compile(rb"<([0-9A-Fa-f]+)>")


def _texto_de_hex(bruto: bytes) -> str:
    dados = bytes.fromhex(bruto.decode("ascii"))
    if len(dados) % 2:
        dados += b"\x00"
    return dados.decode("utf-16-be", errors="ignore")


def _ler_cmap(fluxo: bytes) -> dict[int, str]:
    """Le os blocos bfchar e bfrange de um CMap ToUnicode."""
    tabela: dict[int, str] = {}
    for bloco in _BFCHAR.findall(fluxo):
        itens = _HEX.findall(bloco)
        for origem, destino in zip(itens[::2], itens[1::2]):
            tabela[int(origem, 16)] = _texto_de_hex(destino)
    for bloco in _BFRANGE.findall(fluxo):
        for linha in re.finditer(
            rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*(<[0-9A-Fa-f]+>|\[.*?\])",
            bloco, re.S,
        ):
            inicio, fim, destino = linha.groups()
            primeiro, ultimo = int(inicio, 16), int(fim, 16)
            if destino.startswith(b"["):
                for deslocamento, item in enumerate(_HEX.findall(destino)):
                    tabela[primeiro + deslocamento] = _texto_de_hex(item)
            else:
                base = int(destino.strip(b"<>"), 16)
                for deslocamento in range(ultimo - primeiro + 1):
                    tabela[primeiro + deslocamento] = chr(base + deslocamento)
    return tabela


# --------------------------------------------------------------------------
# Fluxo de conteudo
# --------------------------------------------------------------------------


@dataclass
class Marca:
    """Um trecho de texto com a posicao e o tamanho com que foi desenhado."""

    x: float
    y: float
    texto: str
    tamanho: float = 10.0

    @property
    def fim(self) -> float:
        """Onde o trecho termina, estimado pela largura media de glifo."""
        return self.x + len(self.texto) * self.tamanho * LARGURA_MEDIA


_ESCAPES = {
    b"n": "\n", b"r": "\r", b"t": "\t", b"b": "\b", b"f": "\f",
    b"(": "(", b")": ")", b"\\": "\\",
}


def _multiplicar(a: list[float], b: list[float]) -> list[float]:
    """Produto de duas matrizes 3x2 no formato do PDF."""
    return [
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
        a[4] * b[0] + a[5] * b[2] + b[4],
        a[4] * b[1] + a[5] * b[3] + b[5],
    ]


#: Caracteres de controle e espacos exoticos que algumas fontes devolvem no
#: lugar de um glifo. Nunca sao conteudo, e um NUL no meio de um numero quebra
#: qualquer expressao regular que espere espaco ali.
_CONTROLE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_ESPACOS_EXOTICOS = re.compile(r"[\u00a0\u2007\u202f\u2009\u200a]")


def _limpar(texto: str) -> str:
    return _ESPACOS_EXOTICOS.sub(" ", _CONTROLE.sub("", texto))


def _decodificar_string(bruto: bytes, tabela: dict[int, str]) -> str:
    """Converte uma string do fluxo em texto, usando o CMap quando existir."""
    if not tabela:
        return _limpar(bruto.decode("latin-1", errors="replace"))
    dois_bytes = any(codigo > 0xFF for codigo in tabela)
    saida = []
    if dois_bytes:
        for i in range(0, len(bruto) - 1, 2):
            codigo = (bruto[i] << 8) | bruto[i + 1]
            saida.append(tabela.get(codigo, ""))
    else:
        for byte in bruto:
            saida.append(tabela.get(byte, chr(byte)))
    return _limpar("".join(saida))


def _ler_literal(dados: bytes, i: int) -> tuple[bytes, int]:
    """Le uma string entre parenteses a partir de ``i``, tratando escapes."""
    i += 1
    profundidade = 1
    saida = bytearray()
    while i < len(dados):
        byte = dados[i:i + 1]
        if byte == b"\\":
            proximo = dados[i + 1:i + 2]
            if proximo in _ESCAPES:
                saida += _ESCAPES[proximo].encode("latin-1")
                i += 2
                continue
            if proximo.isdigit():
                octal = dados[i + 1:i + 4]
                digitos = bytes(c for c in octal if 0x30 <= c <= 0x37)
                saida.append(int(digitos, 8) & 0xFF)
                i += 1 + len(digitos)
                continue
            if proximo in (b"\n", b"\r"):
                i += 2
                continue
            saida += proximo
            i += 2
            continue
        if byte == b"(":
            profundidade += 1
        elif byte == b")":
            profundidade -= 1
            if profundidade == 0:
                return bytes(saida), i + 1
        saida += byte
        i += 1
    return bytes(saida), i


_NUMERO = re.compile(rb"-?\d*\.?\d+")


def _extrair_marcas(
    conteudo: bytes, fontes: dict[bytes, dict[int, str]]
) -> list[Marca]:
    """Percorre o fluxo de conteudo e devolve o texto com posicao."""
    marcas: list[Marca] = []
    pilha: list[list[float]] = []
    ctm = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
    tm = tlm = list(ctm)
    tabela: dict[int, str] = {}
    corpo_da_fonte = 10.0
    entrelinha = 0.0
    operandos: list = []
    i = 0

    def emitir(bruto: bytes) -> None:
        texto = _decodificar_string(bruto, tabela)
        if not texto.strip():
            return
        posicao = _multiplicar(tm, ctm)
        # O tamanho aparente e o corpo da fonte esticado pela escala corrente.
        escala = abs(posicao[0]) or abs(posicao[3]) or 1.0
        marcas.append(Marca(
            round(posicao[4], 2), round(posicao[5], 2), texto,
            round(corpo_da_fonte * escala, 2),
        ))

    def deslocar(tx: float, ty: float) -> None:
        nonlocal tm, tlm
        tlm = _multiplicar([1, 0, 0, 1, tx, ty], tlm)
        tm = list(tlm)

    while i < len(conteudo):
        byte = conteudo[i:i + 1]
        if byte in b" \t\r\n":
            i += 1
            continue
        if byte == b"%":
            i = conteudo.find(b"\n", i) + 1 or len(conteudo)
            continue
        if byte == b"(":
            literal, i = _ler_literal(conteudo, i)
            operandos.append(literal)
            continue
        if byte == b"<" and conteudo[i + 1:i + 2] != b"<":
            fim = conteudo.find(b">", i)
            digitos = re.sub(rb"[^0-9A-Fa-f]", b"", conteudo[i + 1:fim])
            if len(digitos) % 2:
                digitos += b"0"
            operandos.append(bytes.fromhex(digitos.decode("ascii")))
            i = fim + 1
            continue
        if byte == b"[":
            fim, profundidade = i + 1, 1
            while fim < len(conteudo) and profundidade:
                if conteudo[fim:fim + 1] == b"(":
                    _, fim = _ler_literal(conteudo, fim)
                    continue
                if conteudo[fim:fim + 1] == b"[":
                    profundidade += 1
                elif conteudo[fim:fim + 1] == b"]":
                    profundidade -= 1
                fim += 1
            operandos.append(("array", conteudo[i + 1:fim - 1]))
            i = fim
            continue
        if byte == b"/":
            achado = re.match(rb"/[^\s/\[\]<>()]*", conteudo[i:])
            operandos.append(achado.group(0))
            i += achado.end()
            continue
        achado = _NUMERO.match(conteudo, i)
        if achado and byte not in b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            operandos.append(float(achado.group(0)))
            i = achado.end()
            continue

        achado = re.match(rb"[A-Za-z'\"*]+[01]?", conteudo[i:])
        if not achado:
            i += 1
            continue
        operador = achado.group(0)
        i += achado.end()

        numeros = [o for o in operandos if isinstance(o, float)]
        if operador == b"q":
            pilha.append(list(ctm))
        elif operador == b"Q" and pilha:
            ctm = pilha.pop()
        elif operador == b"cm" and len(numeros) >= 6:
            ctm = _multiplicar(numeros[-6:], ctm)
        elif operador == b"BT":
            tm = tlm = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
        elif operador == b"Tf":
            nomes = [o for o in operandos if isinstance(o, bytes) and o.startswith(b"/")]
            if nomes:
                tabela = fontes.get(nomes[-1], {})
            if numeros:
                corpo_da_fonte = numeros[-1] or corpo_da_fonte
        elif operador == b"TL" and numeros:
            entrelinha = numeros[-1]
        elif operador == b"Td" and len(numeros) >= 2:
            deslocar(numeros[-2], numeros[-1])
        elif operador == b"TD" and len(numeros) >= 2:
            entrelinha = -numeros[-1]
            deslocar(numeros[-2], numeros[-1])
        elif operador == b"Tm" and len(numeros) >= 6:
            tm = tlm = list(numeros[-6:])
        elif operador == b"T*":
            deslocar(0.0, -entrelinha)
        elif operador == b"Tj" and operandos:
            if isinstance(operandos[-1], bytes):
                emitir(operandos[-1])
        elif operador == b"'":
            deslocar(0.0, -entrelinha)
            if operandos and isinstance(operandos[-1], bytes):
                emitir(operandos[-1])
        elif operador == b'"':
            deslocar(0.0, -entrelinha)
            textos = [o for o in operandos if isinstance(o, bytes)]
            if textos:
                emitir(textos[-1])
        elif operador == b"TJ" and operandos:
            ultimo = operandos[-1]
            if isinstance(ultimo, tuple) and ultimo[0] == "array":
                partes = []
                j = 0
                corpo = ultimo[1]
                while j < len(corpo):
                    if corpo[j:j + 1] == b"(":
                        literal, j = _ler_literal(corpo, j)
                        partes.append(literal)
                        continue
                    if corpo[j:j + 1] == b"<":
                        fim = corpo.find(b">", j)
                        digitos = re.sub(rb"[^0-9A-Fa-f]", b"", corpo[j + 1:fim])
                        if len(digitos) % 2:
                            digitos += b"0"
                        partes.append(bytes.fromhex(digitos.decode("ascii")))
                        j = fim + 1
                        continue
                    j += 1
                if partes:
                    emitir(b"".join(partes))
        operandos = []

    return marcas


def _agrupar_em_linhas(marcas: list[Marca]) -> list[str]:
    """Junta as marcas que estao na mesma altura, da esquerda para a direita."""
    if not marcas:
        return []
    # A comparacao e contra a media da linha em formacao, e nao contra a
    # primeira marca dela: numa mesma linha impressa as baselines variam um
    # ponto de cada vez, e medir sempre a partir da primeira acaba expulsando
    # a ultima marca -- que pode ser justamente o sinal de menos de um estorno.
    linhas: list[list[Marca]] = []
    alturas: list[float] = []
    for marca in sorted(marcas, key=lambda m: (-m.y, m.x)):
        if linhas and abs(alturas[-1] - marca.y) <= TOLERANCIA_LINHA:
            linhas[-1].append(marca)
            alturas[-1] += (marca.y - alturas[-1]) / len(linhas[-1])
        else:
            linhas.append([marca])
            alturas.append(marca.y)

    saida = []
    for linha in linhas:
        linha.sort(key=lambda m: m.x)
        texto = ""
        ultimo_fim = None
        for marca in linha:
            if ultimo_fim is not None:
                vao = marca.x - ultimo_fim
                if vao > marca.tamanho * FRACAO_DE_ESPACO:
                    texto += " "
            texto += marca.texto
            ultimo_fim = marca.fim
        limpo = re.sub(r"\s{2,}", " ", texto).strip()
        if limpo:
            saida.append(limpo)
    return saida
