"""Leitura do controle mensal escrito em texto livre e conciliacao.

O controle chega em blocos, com o dia e a forma de pagamento no cabecalho:

    PAGAMENTOS PIX - DIA 1 DO MES
    - Adriano Jardineiro R$ 600,00
    PIX: 11974226896

    PAGAMENTOS BOLETO - DIA 1 DO MES
    - Comgas R$ 299,68
    34191099661852547293480116380009115560000029968

As linhas de chave PIX e de codigo de barras sao identificadores pessoais:
sao descartadas na leitura e nunca chegam ao disco.
"""

from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass, field

from .modelo import Lancamento, MESES, chave, extrair_parcela, redigir
from .regras import classificar

#: Cabecalho de bloco: define forma de pagamento e dia de vencimento.
_CABECALHO = re.compile(r"(?i)^\s*pagamentos?\b.*?\bdia\s*(\d{1,2})\b")
_FORMA_NO_CABECALHO = re.compile(r"(?i)\b(pix|boleto|cart[ao]{2,3}|debito)\b")
_FORMA_SOLTA = re.compile(r"(?i)^\s*(pix|boleto|cart[ao]{2,3}|debito)\s*$")

#: Nome do mes isolado numa linha, usado como competencia do bloco.
_MES_SOZINHO = re.compile(r"(?i)^\s*([a-zA-Zçãéó]+)\s*(\d{4})?\s*$")

_VALOR = re.compile(r"R\$\s*([\d][\d.,]*)")

#: Linha que so carrega identificador de pagamento: chave PIX, CPF/CNPJ ou a
#: linha digitavel de um boleto, com ou sem separadores e com o visto de pago.
_SO_IDENTIFICADOR = re.compile(r"(?i)^\s*(pix|cpf|cnpj|codigo de barras)\b\s*:?")


def _e_identificador(linha: str) -> bool:
    """Verdadeiro para linhas que sao so numeros de pagamento."""
    if _SO_IDENTIFICADOR.match(linha):
        return True
    digitos = sum(1 for c in linha if c.isdigit())
    return digitos >= 12 and digitos >= 0.5 * len(linha.strip())

#: Continuacao de um item ja lido ("2 dias / R$ 300").
_CONTINUACAO = re.compile(r"(?i)^\s*\d+\s*(dias?|x|vezes?)\b")

#: Marcadores de lista e de status que nao fazem parte da descricao.
_RUIDO = "•⁠-–—*·•⁠​"
_FEITO = re.compile(r"(?i)✅|\bfeito\b|\bpago\b")


def valor_brasileiro(bruto: str) -> float | None:
    """Converte ``"3.000,00"``, ``"2.410"`` ou ``"2,077,42"`` em float.

    O ultimo separador so e decimal quando sobram exatamente dois digitos
    depois dele, o que tolera o texto digitado com virgula no lugar do ponto.
    """
    limpo = bruto.strip().rstrip(".,")
    if not limpo:
        return None
    partes = re.split(r"[.,]", limpo)
    if len(partes) == 1:
        return round(float(partes[0]), 2)
    if len(partes[-1]) == 2:
        inteiro = "".join(partes[:-1])
        return round(float(f"{inteiro}.{partes[-1]}"), 2)
    return round(float("".join(partes)), 2)


@dataclass
class LeituraDeTexto:
    lancamentos: list[Lancamento] = field(default_factory=list)
    ignoradas: list[str] = field(default_factory=list)


def ler_texto(
    texto: str, competencia: str, origem: str = "texto"
) -> LeituraDeTexto:
    """Le o controle mensal em texto e devolve os lancamentos classificados."""
    ano, mes = int(competencia[:4]), int(competencia[5:7])
    leitura = LeituraDeTexto()
    forma = "outros"
    dia: int | None = None
    ultimo: Lancamento | None = None

    for linha_bruta in texto.splitlines():
        linha = linha_bruta.strip()
        if not linha:
            continue

        cabecalho = _CABECALHO.match(linha)
        if cabecalho:
            achado_forma = _FORMA_NO_CABECALHO.search(linha)
            forma = _normalizar_forma(
                achado_forma.group(1) if achado_forma else None
            ) or forma
            dia = int(cabecalho.group(1))
            ultimo = None
            continue
        solta = _FORMA_SOLTA.match(linha)
        if solta:
            forma = _normalizar_forma(solta.group(1)) or forma
            continue
        if _e_so_mes(linha):
            continue
        if _e_identificador(linha):
            continue

        achado = _VALOR.search(linha)
        if not achado:
            # Pode ser um item sem valor informado -- vale registrar.
            if len(chave(linha)) > 3 and not _FEITO.fullmatch(linha):
                leitura.ignoradas.append(redigir(linha))
            continue

        descricao = _descricao_de(linha[: achado.start()])
        if _CONTINUACAO.match(linha) or len(chave(descricao)) < 3:
            if ultimo is not None:
                ultimo.observacao = (
                    f"{ultimo.observacao} {redigir(linha)}".strip()
                )
            else:
                leitura.ignoradas.append(redigir(linha))
            continue

        valor = valor_brasileiro(achado.group(1))
        if valor is None or valor == 0:
            leitura.ignoradas.append(redigir(linha))
            continue

        numero, total = extrair_parcela(descricao)
        lancamento = Lancamento(
            competencia=competencia,
            descricao=redigir(descricao),
            valor=valor,
            data=_data(ano, mes, dia),
            forma=forma,
            parcela=numero,
            parcela_total=total,
            origem=origem,
            pendente=not bool(_FEITO.search(linha)),
        )
        classificar(lancamento)
        leitura.lancamentos.append(lancamento)
        ultimo = lancamento

    return leitura


def _normalizar_forma(bruto: str | None) -> str | None:
    if not bruto:
        return None
    limpo = chave(bruto)
    if limpo.startswith("cart"):
        return "cartao"
    return limpo


def _e_so_mes(linha: str) -> bool:
    achado = _MES_SOZINHO.match(linha)
    return bool(achado and chave(achado.group(1)) in MESES)


def _descricao_de(bruto: str) -> str:
    limpo = bruto.strip().strip(_RUIDO).strip()
    limpo = re.sub(r"\s{2,}", " ", limpo)
    return limpo.strip(_RUIDO + " :").strip()


def _data(ano: int, mes: int, dia: int | None) -> _dt.date | None:
    if not dia:
        return None
    try:
        return _dt.date(ano, mes, dia)
    except ValueError:
        return None


# --------------------------------------------------------------------------
# Conciliacao texto x planilha
# --------------------------------------------------------------------------


@dataclass
class Divergencia:
    tipo: str            # so_no_texto | so_na_planilha | valor_diferente
    descricao: str
    categoria: str
    valor_texto: float = 0.0
    valor_planilha: float = 0.0

    @property
    def diferenca(self) -> float:
        return round(self.valor_texto - self.valor_planilha, 2)


def _identidade(lancamento: Lancamento) -> tuple[str, str, str]:
    return (lancamento.categoria, lancamento.subcategoria, lancamento.pessoa)


def conciliar(
    do_texto: list[Lancamento],
    da_planilha: list[Lancamento],
    tolerancia: float = 0.01,
) -> list[Divergencia]:
    """Compara os dois controles do mesmo mes e lista o que nao bate.

    O pareamento e feito pela classificacao (categoria, subcategoria, pessoa),
    o que faz "Deposito Z2" no texto encontrar "Para Z2" na planilha. Dentro de
    um mesmo grupo os itens sao pareados pelo valor mais proximo.
    """
    pendentes_planilha: dict[tuple, list[Lancamento]] = {}
    for l in da_planilha:
        pendentes_planilha.setdefault(_identidade(l), []).append(l)

    divergencias: list[Divergencia] = []

    for lancamento in do_texto:
        candidatos = pendentes_planilha.get(_identidade(lancamento))
        if not candidatos:
            divergencias.append(Divergencia(
                tipo="so_no_texto",
                descricao=lancamento.descricao,
                categoria=lancamento.categoria,
                valor_texto=lancamento.valor,
            ))
            continue
        par = min(candidatos, key=lambda c: abs(c.valor - lancamento.valor))
        candidatos.remove(par)
        if abs(par.valor - lancamento.valor) > tolerancia:
            divergencias.append(Divergencia(
                tipo="valor_diferente",
                descricao=f"{lancamento.descricao} / {par.descricao}",
                categoria=lancamento.categoria,
                valor_texto=lancamento.valor,
                valor_planilha=par.valor,
            ))

    for restantes in pendentes_planilha.values():
        for l in restantes:
            divergencias.append(Divergencia(
                tipo="so_na_planilha",
                descricao=l.descricao,
                categoria=l.categoria,
                valor_planilha=l.valor,
            ))

    ordem = {"so_no_texto": 0, "valor_diferente": 1, "so_na_planilha": 2}
    return sorted(
        divergencias,
        key=lambda d: (ordem[d.tipo], -max(d.valor_texto, d.valor_planilha)),
    )
