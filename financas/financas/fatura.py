"""Leitura de faturas de cartao de credito em PDF.

Uma fatura tem duas partes que interessam: o cabecalho, que diz de qual cartao
ela e, quando vence e quanto foi comprado no periodo, e a lista de lancamentos.
O resto da pagina -- limites, taxas, pontos do programa de milhas -- e ruido.

A pagina e diagramada em duas colunas, e a coluna da direita cai no meio das
linhas da esquerda quando o texto e remontado. Por isso um lancamento e lido da
esquerda para a direita e termina no primeiro valor monetario depois da
descricao: o que vier depois e a outra coluna.

A leitura se valida sozinha. A fatura declara quanto foi comprado no periodo, e
a soma dos lancamentos lidos tem que bater com esse numero. Quando nao bate, a
diferenca e reportada em vez de passar despercebida.
"""

from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass, field
from pathlib import Path

from .modelo import Lancamento, competencia_de, extrair_parcela, redigir
from .pdf import DocumentoPDF, ErroDePDF
from .regras import classificar

#: Um lancamento: dia/mes, descricao, e o primeiro valor monetario depois dela.
#: O ``(?!/)`` evita casar uma data completa vinda da outra coluna. A varredura
#: e feita na linha inteira, e nao so no comeco: as paginas tem lancamentos nas
#: duas colunas, e remontar o texto poe dois deles na mesma linha.
_VALOR = r"\d{1,3}(?:\.\d{3})*,\d{2}"

#: Compra em moeda estrangeira. A linha termina em tres numeros: o valor em
#: dolar, a cotacao do dia com quatro casas, e o valor em real que foi de fato
#: cobrado. E o ultimo que interessa -- pegar o primeiro cobra a viagem inteira
#: pelo preco em dolar.
_INTERNACIONAL = re.compile(
    r"(?:^|\s)(\d{2}/\d{2})(?!/)\s+(.+?)\s+" + _VALOR +
    r"\s*\d+,\d{4}\s+(" + _VALOR + r")(\s*-)?(?=\s|$)"
)

#: Compra em real: data, descricao e o primeiro valor monetario depois dela.
#: O ``(?!/)`` evita casar uma data completa vinda da outra coluna.
_LANCAMENTO = re.compile(
    r"(?:^|\s)(\d{2}/\d{2})(?!/)\s+(.+?)\s+(" + _VALOR + r")(\s*-)?(?=\s|$)"
)

#: Sobra do valor em dolar dentro da descricao de uma compra internacional.
_MOEDA_NA_DESCRICAO = re.compile(
    r"(?i)\s*\b(usd|eur|gbp)\b\s*" + _VALOR + r"?|\s*" + _VALOR + r"(?=\s|$)"
)

_DINHEIRO = r"R\$\s*(\d{1,3}(?:\.\d{3})*,\d{2})"
_VENCIMENTO = re.compile(r"(\d{2})\s*/\s*(\d{2})\s*/\s*(\d{4})")
_CARTAO = re.compile(r"Cart[ãa]o\s+(\d{4})\s+[X\s]+\s*(\d{4,5})", re.I)
_TOTAL_FATURA = re.compile(r"Total de fatura.*?" + _DINHEIRO, re.I | re.S)
_COMPRAS = re.compile(r"Compras\s*/\s*D[ée]bitos\.*\s*" + _DINHEIRO, re.I)
_PARCELADO_FUTURO = re.compile(
    r"Total para as pr[óo]ximas faturas\s*" + _DINHEIRO, re.I
)

#: Linhas que sao da mecanica do cartao, e nao consumo da casa.
_NAO_E_COMPRA = re.compile(
    r"(?i)^(pag(amento)?\b|pgto\b).*(boleto|fatura|banc)"
    r"|^(cr[ée]dito|estorno|devolu|reembolso|cancelamento|saldo anterior)"
    r"|ajuste a cr[ée]dito"
)

#: Encargos do proprio cartao: sao despesa, mas de outra natureza que consumo.
_ENCARGO = re.compile(r"(?i)encargo|juros|anuidade|iof|multa|mora|tarifa")


def valor_brasileiro(bruto: str) -> float:
    return round(float(bruto.replace(".", "").replace(",", ".")), 2)


@dataclass
class Fatura:
    arquivo: str
    cartao: str                       # rotulo legivel do cartao
    produto: str = ""                 # nome do produto impresso na fatura
    vencimento: _dt.date | None = None
    competencia: str = ""
    total: float = 0.0                # o que a fatura manda pagar
    compras: float = 0.0              # o que a fatura diz ter sido comprado
    parcelado_futuro: float = 0.0     # parcelas ja comprometidas
    lancamentos: list[Lancamento] = field(default_factory=list)
    creditos: list[Lancamento] = field(default_factory=list)

    @property
    def soma_lida(self) -> float:
        return round(sum(l.valor for l in self.lancamentos), 2)

    @property
    def diferenca(self) -> float:
        """Quanto a leitura se afasta do que a fatura declara ter comprado."""
        return round(self.soma_lida - self.compras, 2) if self.compras else 0.0

    @property
    def confere(self) -> bool:
        return self.compras > 0 and abs(self.diferenca) <= max(1.0, self.compras * 0.005)


def _texto_do_cabecalho(paginas: list[list[str]]) -> str:
    return "\n".join(paginas[0]) if paginas else ""


def _rotulo_do_cartao(todas: str, arquivo: str) -> tuple[str, str]:
    """Nome legivel do cartao e o produto impresso na fatura.

    Usa so os digitos que a propria fatura ja mostra mascarados.
    """
    produto = ""
    for linha in todas.splitlines():
        limpo = linha.strip()
        if re.fullmatch(r"[A-ZÀ-Ú][A-ZÀ-Ú \-*]{6,40}", limpo) and "CARD" in limpo.upper():
            produto = limpo.title()
            break
    achado = _CARTAO.search(todas)
    if achado:
        bandeira = "Amex" if achado.group(1).startswith("37") else "Visa"
        return f"{bandeira} final {achado.group(2)}", produto
    return Path(arquivo).stem[:16], produto


def _competencia_do_vencimento(texto: str) -> tuple[_dt.date | None, str]:
    achado = _VENCIMENTO.search(texto)
    if not achado:
        return None, ""
    dia, mes, ano = (int(g) for g in achado.groups())
    try:
        data = _dt.date(ano, mes, dia)
    except ValueError:
        return None, ""
    return data, competencia_de(ano, mes)


def _data_do_lancamento(bruto: str, vencimento: _dt.date | None) -> _dt.date | None:
    """A fatura traz so dia/mes; o ano vem do vencimento.

    Uma compra de dezembro numa fatura de janeiro pertence ao ano anterior.
    """
    if not vencimento:
        return None
    dia, mes = (int(p) for p in bruto.split("/"))
    ano = vencimento.year - 1 if mes > vencimento.month else vencimento.year
    try:
        return _dt.date(ano, mes, dia)
    except ValueError:
        return None


def ler(caminho: str) -> Fatura:
    """Le uma fatura em PDF e devolve os lancamentos ja classificados."""
    try:
        paginas = DocumentoPDF.de_arquivo(caminho).linhas()
    except (ErroDePDF, OSError) as erro:
        raise ErroDePDF(f"{Path(caminho).name}: {erro}") from erro

    todas = "\n".join("\n".join(pagina) for pagina in paginas)
    cabecalho = _texto_do_cabecalho(paginas)
    cartao, produto = _rotulo_do_cartao(todas, caminho)
    vencimento, competencia = _competencia_do_vencimento(cabecalho)

    fatura = Fatura(
        arquivo=Path(caminho).name,
        cartao=cartao,
        produto=produto,
        vencimento=vencimento,
        competencia=competencia,
    )
    for expressao, campo in (
        (_TOTAL_FATURA, "total"), (_COMPRAS, "compras"),
        (_PARCELADO_FUTURO, "parcelado_futuro"),
    ):
        achado = expressao.search(todas)
        if achado:
            setattr(fatura, campo, valor_brasileiro(achado.group(1)))

    for pagina in paginas:
        for linha in pagina:
            for lancamento in _ler_linha(linha, fatura):
                if lancamento.natureza == "credito":
                    fatura.creditos.append(lancamento)
                else:
                    fatura.lancamentos.append(lancamento)

    return fatura


def _ler_linha(linha: str, fatura: Fatura) -> list[Lancamento]:
    """Extrai os lancamentos de uma linha remontada da pagina.

    As compras internacionais sao lidas primeiro e retiradas da linha: elas
    terminam em tres numeros, e o regex simples pararia no primeiro deles, que
    e o valor em dolar. O que sobra da linha e lido como compra em real.
    """
    achados: list[Lancamento] = []
    restante = linha
    for achado in _INTERNACIONAL.finditer(linha):
        lancamento = _montar(achado, fatura, internacional=True)
        if lancamento is not None:
            achados.append(lancamento)
        inicio, fim = achado.span()
        restante = restante[:inicio] + " " * (fim - inicio) + restante[fim:]
    for achado in _LANCAMENTO.finditer(restante):
        lancamento = _montar(achado, fatura)
        if lancamento is not None:
            achados.append(lancamento)
    return achados


def _montar(
    achado: re.Match, fatura: Fatura, internacional: bool = False
) -> Lancamento | None:
    """Transforma um casamento do regex num lancamento, ou descarta."""
    bruto_data, descricao, bruto_valor, negativo = achado.groups()
    if internacional:
        # A descricao absorveu o valor em dolar e a cidade; limpa o que e numero.
        descricao = _MOEDA_NA_DESCRICAO.sub(" ", descricao)
    descricao = redigir(re.sub(r"\s{2,}", " ", descricao).strip(" .-"))
    if len(descricao) < 3:
        return None
    valor = valor_brasileiro(bruto_valor)
    if valor == 0:
        return None

    numero, total = extrair_parcela(descricao)
    lancamento = Lancamento(
        competencia=fatura.competencia,
        descricao=descricao,
        valor=valor,
        data=_data_do_lancamento(bruto_data, fatura.vencimento),
        forma="cartao",
        parcela=numero,
        parcela_total=total,
        origem=f"fatura:{fatura.cartao}",
    )
    # Pagamento da fatura anterior e estorno nao sao consumo: entram como
    # credito para nao inflar o gasto do mes.
    if negativo or _NAO_E_COMPRA.search(descricao):
        lancamento.natureza = "credito"
        return lancamento

    classificar(lancamento)
    if _ENCARGO.search(descricao):
        lancamento.categoria = "Financeiro"
        lancamento.subcategoria = "Encargos do cartão"
        lancamento.pessoa = "Casa"
    return lancamento


def ler_varias(caminhos: list[str]) -> tuple[list[Fatura], list[str]]:
    """Le um lote de faturas. Devolve as lidas e os avisos do que nao fechou."""
    faturas: list[Fatura] = []
    avisos: list[str] = []
    for caminho in sorted(caminhos):
        try:
            fatura = ler(caminho)
        except ErroDePDF as erro:
            avisos.append(f"fatura ilegivel: {erro}")
            continue
        if not fatura.competencia:
            avisos.append(f"{fatura.arquivo}: nao achei o vencimento")
        elif not fatura.confere:
            avisos.append(
                f"{fatura.cartao} {fatura.competencia}: li "
                f"R$ {fatura.soma_lida:,.2f} e a fatura declara "
                f"R$ {fatura.compras:,.2f}"
            )
        faturas.append(fatura)
    return faturas, avisos
