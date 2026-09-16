"""Parcelas em curso no cartao e o quanto elas ja comprometem dos meses a vir.

Uma parcela aparece em todas as faturas ate acabar, entao somar as faturas
todas contaria a mesma compra varias vezes. O retrato correto vem da ultima
fatura de cada cartao ativo: ali cada parcelamento aparece uma vez, com o
numero da parcela atual, e o que falta e aritmetica.

Cartao trocado nao conta duas vezes. Quando um cartao para de receber faturas,
o saldo dele migrou para o novo, e contar os dois dobraria o compromisso.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from .fatura import Fatura
from .modelo import Lancamento, competencia_de


@dataclass
class Parcelamento:
    descricao: str
    cartao: str
    categoria: str
    valor: float                # valor de cada parcela
    parcela: int                # numero da parcela na ultima fatura lida
    total: int
    competencia_atual: str      # fatura em que foi vista pela ultima vez

    @property
    def restantes(self) -> int:
        return max(self.total - self.parcela, 0)

    @property
    def comprometido(self) -> float:
        """Quanto ainda vai ser cobrado ate a ultima parcela."""
        return round(self.valor * self.restantes, 2)

    @property
    def ultima_competencia(self) -> str:
        return _somar_meses(self.competencia_atual, self.restantes)


def _somar_meses(competencia: str, meses: int) -> str:
    ano, mes = int(competencia[:4]), int(competencia[5:7])
    total = (ano * 12 + mes - 1) + meses
    return competencia_de(total // 12, total % 12 + 1)


def cartoes_ativos(faturas: list[Fatura]) -> dict[str, Fatura]:
    """Ultima fatura de cada cartao que ainda esta recebendo faturas.

    Um cartao cuja ultima fatura e mais antiga que a do conjunto foi
    substituido, e o saldo dele ja esta na fatura do cartao novo.
    """
    if not faturas:
        return {}
    ultima_competencia = max(f.competencia for f in faturas if f.competencia)
    por_cartao: dict[str, Fatura] = {}
    for fatura in faturas:
        if not fatura.competencia:
            continue
        atual = por_cartao.get(fatura.cartao)
        if atual is None or fatura.competencia > atual.competencia:
            por_cartao[fatura.cartao] = fatura
    return {
        cartao: fatura for cartao, fatura in por_cartao.items()
        if fatura.competencia == ultima_competencia
    }


def em_curso(faturas: list[Fatura]) -> list[Parcelamento]:
    """Parcelamentos que ainda tem parcela a vencer."""
    saida: list[Parcelamento] = []
    for cartao, fatura in cartoes_ativos(faturas).items():
        for lancamento in fatura.lancamentos:
            if not lancamento.parcela or not lancamento.parcela_total:
                continue
            if lancamento.parcela >= lancamento.parcela_total:
                continue
            saida.append(Parcelamento(
                descricao=lancamento.rotulo,
                cartao=cartao,
                categoria=lancamento.categoria,
                valor=lancamento.valor,
                parcela=lancamento.parcela,
                total=lancamento.parcela_total,
                competencia_atual=fatura.competencia,
            ))
    return sorted(saida, key=lambda p: -p.comprometido)


def cronograma(
    parcelamentos: list[Parcelamento], meses: int = 24
) -> list[tuple[str, float, int]]:
    """Quanto de parcela cai em cada mes a frente, e quantas sao."""
    por_mes: dict[str, list[float]] = defaultdict(list)
    for parcelamento in parcelamentos:
        for passo in range(1, parcelamentos and parcelamento.restantes + 1 or 1):
            competencia = _somar_meses(parcelamento.competencia_atual, passo)
            por_mes[competencia].append(parcelamento.valor)
    return [
        (competencia, round(sum(valores), 2), len(valores))
        for competencia, valores in sorted(por_mes.items())[:meses]
    ]


def total_comprometido(parcelamentos: list[Parcelamento]) -> float:
    return round(sum(p.comprometido for p in parcelamentos), 2)
