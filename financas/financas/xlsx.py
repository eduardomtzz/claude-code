"""Leitor minimalista de arquivos .xlsx, sem dependencias externas.

Um .xlsx e um zip de XML. Este modulo le apenas o necessario para extrair
celulas como texto/numero, o que evita depender de pandas ou openpyxl.
"""

from __future__ import annotations

import datetime as _dt
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass

_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_RELS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
_NS = {"m": _MAIN}
_R = "{%s}" % _RELS

# O Excel conta dias a partir de 1899-12-30 (o bug do ano bissexto de 1900
# faz o dia 0 cair nessa data).
_EPOCH = _dt.date(1899, 12, 30)

#: Menor serial aceito como data. 40000 == 2009-07-06. Abaixo disso um numero
#: na coluna de dia e tratado como dia do mes, nao como data completa.
SERIAL_MINIMO = 40000


@dataclass(frozen=True)
class Aba:
    nome: str
    caminho: str
    estado: str

    @property
    def visivel(self) -> bool:
        return self.estado == "visible"


def serial_para_data(serial: float) -> _dt.date:
    """Converte um serial de data do Excel em ``datetime.date``."""
    return _EPOCH + _dt.timedelta(days=int(serial))


class Planilha:
    """Acesso somente leitura a um arquivo .xlsx."""

    def __init__(self, caminho: str):
        self._zip = zipfile.ZipFile(caminho)
        self._textos = self._ler_textos()
        self.abas = self._ler_abas()

    def __enter__(self) -> "Planilha":
        return self

    def __exit__(self, *_exc) -> None:
        self.fechar()

    def fechar(self) -> None:
        self._zip.close()

    def _ler_textos(self) -> list[str]:
        try:
            bruto = self._zip.read("xl/sharedStrings.xml")
        except KeyError:
            return []
        raiz = ET.fromstring(bruto)
        return [
            "".join(t.text or "" for t in si.iter("{%s}t" % _MAIN))
            for si in raiz.findall("m:si", _NS)
        ]

    def _ler_abas(self) -> list[Aba]:
        livro = ET.fromstring(self._zip.read("xl/workbook.xml"))
        alvos = {
            rel.get("Id"): rel.get("Target")
            for rel in ET.fromstring(self._zip.read("xl/_rels/workbook.xml.rels"))
        }
        abas: list[Aba] = []
        for no in livro.find("m:sheets", _NS):
            alvo = (alvos[no.get(_R + "id")] or "").lstrip("/")
            if not alvo.startswith("xl/"):
                alvo = "xl/" + alvo
            abas.append(Aba(no.get("name") or "", alvo, no.get("state") or "visible"))
        return abas

    def linhas(self, aba: Aba) -> list[list[str]]:
        """Devolve as linhas da aba como listas de strings.

        Linhas e colunas vazias viram strings vazias, de modo que o indice de
        cada celula corresponde sempre a sua coluna real na planilha.
        """
        raiz = ET.fromstring(self._zip.read(aba.caminho))
        dados = raiz.find("m:sheetData", _NS)
        if dados is None:
            return []
        saida: list[list[str]] = []
        for linha in dados.findall("m:row", _NS):
            celulas: dict[int, str] = {}
            for celula in linha.findall("m:c", _NS):
                indice = _indice_coluna(celula.get("r") or "")
                if indice is None:
                    continue
                celulas[indice] = _valor_celula(celula, self._textos)
            largura = max(celulas) + 1 if celulas else 0
            saida.append([celulas.get(i, "") for i in range(largura)])
        return saida


def _indice_coluna(referencia: str) -> int | None:
    """``"C7"`` -> ``2``. Devolve ``None`` se a referencia nao tiver letras."""
    letras = "".join(c for c in referencia if c.isalpha()).upper()
    if not letras:
        return None
    indice = 0
    for letra in letras:
        indice = indice * 26 + (ord(letra) - 64)
    return indice - 1


def _valor_celula(celula: ET.Element, textos: list[str]) -> str:
    tipo = celula.get("t")
    valor = celula.find("m:v", _NS)
    if tipo == "s" and valor is not None and valor.text is not None:
        indice = int(valor.text)
        return textos[indice] if 0 <= indice < len(textos) else ""
    if tipo == "inlineStr":
        bloco = celula.find("m:is", _NS)
        if bloco is None:
            return ""
        return "".join(t.text or "" for t in bloco.iter("{%s}t" % _MAIN))
    if valor is not None and valor.text is not None:
        return valor.text
    return ""
