"""Extracao dos lancamentos das abas mensais da planilha da casa.

Formato esperado de cada aba mensal:

======  =====================  =======  =============
dia     descricao              valor    observacao
======  =====================  =======  =============
1       Comgas                 299.68
                               3300.00               <- continuacao da linha acima
Cartao  Natacao (01 de 06)     754.00   cartao
                               46812.65              <- total da aba (descartado)
======  =====================  =======  =============

A coluna de dia pode trazer o dia do mes (1..31) ou um serial de data do
Excel. Colunas a direita da observacao sao tabelas auxiliares do dono da
planilha e sao ignoradas.
"""

from __future__ import annotations

import datetime as _dt
import re

from .modelo import (
    Lancamento,
    MESES,
    chave,
    competencia_de,
    extrair_parcela,
    redigir,
    sem_acento,
)
from .xlsx import Planilha, SERIAL_MINIMO, serial_para_data

#: Abas que nao contem lancamentos.
ABAS_IGNORADAS = {"contatos"}

#: Uma linha orfa cujo valor alcanca esta fracao da soma acumulada da secao
#: e um total, nao um lancamento.
FRACAO_DE_TOTAL = 0.8

_SO_NUMERO = re.compile(r"^-?\d+(?:[.,]\d+)?$")


def numero(bruto: str) -> float | None:
    """Converte o texto de uma celula numerica em float, ou ``None``."""
    texto = (bruto or "").strip()
    if not texto or not _SO_NUMERO.match(texto):
        return None
    return round(float(texto.replace(",", ".")), 2)


def competencias_das_abas(nomes: list[str]) -> dict[str, str]:
    """Mapeia o nome de cada aba mensal para uma competencia ``AAAA-MM``.

    O ano vem da sequencia das abas: a planilha comeca em agosto e o ano
    avanca sempre que o numero do mes retrocede. Quando o nome da aba traz o
    ano ("Agosto25", "Julho 2026") ele e usado para conferir a sequencia.
    """
    saida: dict[str, str] = {}
    ano: int | None = None
    mes_anterior: int | None = None
    for nome in nomes:
        limpo = chave(nome)
        if limpo in ABAS_IGNORADAS:
            continue
        achado = re.match(r"([a-z]+)\s*(\d{2,4})?$", limpo)
        if not achado or achado.group(1) not in MESES:
            continue
        mes = MESES[achado.group(1)]
        explicito = achado.group(2)
        if ano is None:
            ano = _ano_inicial(explicito, nomes)
        elif mes_anterior is not None and mes < mes_anterior:
            ano += 1
        if explicito:
            ano = _ano_completo(explicito)
        saida[nome] = competencia_de(ano, mes)
        mes_anterior = mes
    return saida


def _ano_completo(bruto: str) -> int:
    valor = int(bruto)
    return valor if valor > 100 else 2000 + valor


def _ano_inicial(explicito: str | None, nomes: list[str]) -> int:
    """Ano da primeira aba mensal.

    Se a primeira aba ja traz o ano, usa-o. Caso contrario, conta quantas
    viradas de ano existem ate a primeira aba com ano explicito e volta no
    tempo a partir dela.
    """
    if explicito:
        return _ano_completo(explicito)
    viradas = 0
    mes_anterior: int | None = None
    for nome in nomes:
        limpo = chave(nome)
        achado = re.match(r"([a-z]+)\s*(\d{2,4})?$", limpo)
        if not achado or achado.group(1) not in MESES:
            continue
        mes = MESES[achado.group(1)]
        if mes_anterior is not None and mes < mes_anterior:
            viradas += 1
        if achado.group(2):
            return _ano_completo(achado.group(2)) - viradas
        mes_anterior = mes
    return _dt.date.today().year - viradas


def _data_da_linha(bruto: str, ano: int, mes: int) -> tuple[_dt.date | None, bool]:
    """Interpreta a coluna de dia. Devolve ``(data, e_cartao)``."""
    texto = (bruto or "").strip()
    if not texto:
        return None, False
    if "cartao" in chave(texto):
        return None, True
    valor = numero(texto)
    if valor is None:
        return None, False
    inteiro = int(valor)
    if inteiro >= SERIAL_MINIMO:
        return serial_para_data(inteiro), False
    if 1 <= inteiro <= 31:
        try:
            return _dt.date(ano, mes, inteiro), False
        except ValueError:
            return None, False
    return None, False


def _indices_de_total(linhas: list[list[str]]) -> set[int]:
    """Indices das linhas que sao totais de secao, e nao lancamentos.

    Uma linha "orfa" (sem dia e sem descricao, apenas valor) pode ser duas
    coisas: o segundo pagamento de um item ja descrito na linha acima, ou o
    total de uma secao. A distincao e feita pela ordem de grandeza -- um total
    fecha a soma da secao, um pagamento avulso e uma fracao dela. A ultima orfa
    da aba e sempre total, o que cobre as abas cujo total esta desatualizado
    porque a formula nao foi recalculada.
    """
    orfas: list[int] = []
    totais: set[int] = set()
    acumulado = 0.0

    for indice, linha in enumerate(linhas):
        valor = numero(linha[2] if len(linha) > 2 else "")
        if valor is None or valor == 0:
            continue
        if _e_orfa(linha):
            orfas.append(indice)
            if acumulado > 0 and valor >= FRACAO_DE_TOTAL * acumulado:
                totais.add(indice)
                acumulado = 0.0
            else:
                acumulado += valor
        else:
            acumulado += valor

    if orfas:
        totais.add(orfas[-1])
    return totais


def _e_orfa(linha: list[str]) -> bool:
    """Linha sem dia e sem descricao, com valor diferente de zero."""
    dia = (linha[0] if len(linha) > 0 else "").strip()
    descricao = (linha[1] if len(linha) > 1 else "").strip()
    valor = numero(linha[2] if len(linha) > 2 else "")
    return not dia and not descricao and valor is not None and valor != 0


def ler_abas(caminho: str) -> list[Lancamento]:
    """Le todas as abas mensais e devolve os lancamentos ainda sem categoria."""
    with Planilha(caminho) as arquivo:
        nomes = [aba.nome for aba in arquivo.abas if aba.visivel]
        competencias = competencias_das_abas(nomes)
        lancamentos: list[Lancamento] = []
        for aba in arquivo.abas:
            if not aba.visivel or aba.nome not in competencias:
                continue
            competencia = competencias[aba.nome]
            lancamentos.extend(
                _ler_uma_aba(arquivo.linhas(aba), aba.nome, competencia)
            )
    return lancamentos


def _ler_uma_aba(
    linhas: list[list[str]], nome_aba: str, competencia: str
) -> list[Lancamento]:
    ano, mes = int(competencia[:4]), int(competencia[5:7])
    totais = _indices_de_total(linhas)
    saida: list[Lancamento] = []
    ultimo: Lancamento | None = None

    for indice, linha in enumerate(linhas):
        if indice in totais:
            continue
        dia_bruto = linha[0] if len(linha) > 0 else ""
        descricao = redigir((linha[1] if len(linha) > 1 else "").strip())
        valor = numero(linha[2] if len(linha) > 2 else "")
        nota = redigir((linha[3] if len(linha) > 3 else "").strip())

        if valor is None or valor == 0:
            continue
        cabecalho = chave(descricao) in {"valor", "dia", ""} and not descricao
        if chave(descricao) == "valor":
            continue

        data, no_cartao = _data_da_linha(dia_bruto, ano, mes)

        if not descricao:
            # Linha orfa: segundo pagamento do mesmo item da linha anterior.
            if ultimo is None:
                continue
            descricao = ultimo.descricao
            if data is None:
                data = ultimo.data
            no_cartao = no_cartao or ultimo.forma == "cartao"

        parcela, parcela_total = extrair_parcela(descricao)
        pendente = "a pagar" in chave(nota)
        lancamento = Lancamento(
            competencia=competencia,
            descricao=descricao,
            valor=valor,
            data=data,
            forma="cartao" if (no_cartao or chave(nota) == "cartao") else "outros",
            parcela=parcela,
            parcela_total=parcela_total,
            observacao="" if chave(nota) in {"cartao", "a pagar"} else nota,
            origem=f"planilha:{nome_aba}",
            pendente=pendente,
        )
        saida.append(lancamento)
        if (linha[1] if len(linha) > 1 else "").strip():
            ultimo = lancamento
    return saida
