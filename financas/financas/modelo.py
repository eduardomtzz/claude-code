"""Modelo canonico de um lancamento e utilidades de normalizacao."""

from __future__ import annotations

import datetime as _dt
import re
import unicodedata
from dataclasses import dataclass, field, asdict

MESES = {
    "janeiro": 1, "fevereiro": 2, "marco": 3, "abril": 4, "maio": 5, "junho": 6,
    "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11,
    "dezembro": 12,
}

MESES_CURTOS = {
    1: "jan", 2: "fev", 3: "mar", 4: "abr", 5: "mai", 6: "jun",
    7: "jul", 8: "ago", 9: "set", 10: "out", 11: "nov", 12: "dez",
}


def sem_acento(texto: str) -> str:
    normalizado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in normalizado if unicodedata.category(c) != "Mn")


def chave(texto: str) -> str:
    """Forma canonica de um texto para casamento de regras.

    Minusculas, sem acento, sem pontuacao e com espacos colapsados.
    """
    limpo = sem_acento(texto).lower()
    limpo = re.sub(r"[^a-z0-9]+", " ", limpo)
    return limpo.strip()


# --------------------------------------------------------------------------
# Redacao de dados pessoais
# --------------------------------------------------------------------------

# CPF, CNPJ, telefone, linha digitavel de boleto e afins. Qualquer sequencia
# longa de digitos (com ou sem separadores) e considerada identificador.
_IDENTIFICADOR = re.compile(r"\b[\d][\d.\-/ ]{8,}\d\b")
_CHAVE_PIX = re.compile(r"(?i)\b(pix|cpf|cnpj|codigo de barras|linha digitavel)\b\s*:?\s*\S.*")


def redigir(texto: str) -> str:
    """Remove identificadores pessoais de um texto livre.

    Usado em tudo que sai do parser, para que CPF, CNPJ, telefone e linha
    digitavel de boleto nunca cheguem ao disco nem ao painel.
    """
    if not texto:
        return ""
    sem_chave = _CHAVE_PIX.sub(lambda m: m.group(1) + ": [redigido]", texto)
    return _IDENTIFICADOR.sub("[redigido]", sem_chave).strip()


# --------------------------------------------------------------------------
# Parcelas
# --------------------------------------------------------------------------

_PARCELA = [
    # "(01 de 06)", "01 de 06", "1 de 6"
    re.compile(r"(?<!\d)(\d{1,2})\s*de\s*(\d{1,2})(?!\d)"),
    # "(01/03)", "parc 02/03", "3/12" -- o (?!\d) descarta datas como 05/2026
    re.compile(r"(?<!\d)(\d{1,2})\s*/\s*(\d{1,2})(?!\d)"),
    # "parc 02" -> parcela conhecida, total desconhecido
    re.compile(r"parc(?:ela)?\.?\s*(\d{1,2})(?!\d)()"),
]


def chave_parcela(texto: str) -> str:
    """Normalizacao que preserva a barra.

    :func:`chave` descarta pontuacao, o que transformaria "(02/03)" em
    "02 03" e apagaria justamente o separador que identifica a parcela.
    """
    limpo = sem_acento(texto).lower()
    limpo = re.sub(r"[^a-z0-9/]+", " ", limpo)
    return re.sub(r"\s{2,}", " ", limpo).strip()


def extrair_parcela(descricao: str) -> tuple[int | None, int | None]:
    """Devolve ``(numero, total)`` da parcela descrita, ou ``(None, None)``.

    Reconhece ``(01 de 06)``, ``(02/03)`` e ``parc 02``. Ignora pares em que o
    numero da parcela excede o total, que costumam ser datas ou medidas.
    """
    texto = chave_parcela(descricao)
    for padrao in _PARCELA:
        achado = padrao.search(texto)
        if not achado:
            continue
        numero = int(achado.group(1))
        bruto_total = achado.group(2)
        total = int(bruto_total) if bruto_total else None
        if numero < 1 or numero > 60:
            continue
        if total is not None and (total < 2 or total > 60 or numero > total):
            continue
        return numero, total
    return None, None


def limpar_descricao(descricao: str) -> str:
    """Remove o sufixo de parcela, deixando so o nome do gasto."""
    limpo = re.sub(
        r"\(?\s*\b\d{1,2}\s*(?:de|/)\s*\d{1,2}\b\s*\)?|\bparc(?:ela)?\.?\s*\d{1,2}\b",
        "",
        descricao,
        flags=re.IGNORECASE,
    )
    limpo = re.sub(r"\(\s*\)", "", limpo)
    return re.sub(r"\s{2,}", " ", limpo).strip(" -").strip()


# --------------------------------------------------------------------------
# Lancamento
# --------------------------------------------------------------------------


@dataclass
class Lancamento:
    """Uma linha de pagamento ja normalizada."""

    competencia: str          # "2026-09" -- mes ao qual o gasto pertence
    descricao: str            # texto original, ja redigido
    valor: float
    data: _dt.date | None = None
    categoria: str = "Nao classificado"
    subcategoria: str = ""
    pessoa: str = "Casa"
    forma: str = "outros"     # pix | boleto | cartao | outros
    natureza: str = "despesa" # despesa | poupanca | transferencia
    parcela: int | None = None
    parcela_total: int | None = None
    observacao: str = ""
    origem: str = ""          # de onde a linha veio (aba ou bloco do texto)
    pendente: bool = False

    @property
    def rotulo(self) -> str:
        """Descricao sem o sufixo de parcela -- usada para agrupar recorrencias."""
        return limpar_descricao(self.descricao)

    @property
    def ano(self) -> int:
        return int(self.competencia[:4])

    @property
    def mes(self) -> int:
        return int(self.competencia[5:7])

    @property
    def competencia_curta(self) -> str:
        return f"{MESES_CURTOS[self.mes]}/{str(self.ano)[2:]}"

    def como_dicionario(self) -> dict:
        dados = asdict(self)
        dados["data"] = self.data.isoformat() if self.data else ""
        dados["rotulo"] = self.rotulo
        return dados


def competencia_de(ano: int, mes: int) -> str:
    return f"{ano:04d}-{mes:02d}"


def ordenar_competencias(competencias) -> list[str]:
    return sorted(set(competencias))
