"""Junta a planilha e o controle em texto num unico conjunto de lancamentos."""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from pathlib import Path

from .modelo import Lancamento
from .planilha import ler_abas
from .regras import classificar_todos
from .texto import Divergencia, conciliar, ler_texto


@dataclass
class Conciliacao:
    competencia: str
    total_texto: float
    total_planilha: float
    divergencias: list[Divergencia] = field(default_factory=list)

    @property
    def diferenca(self) -> float:
        return round(self.total_texto - self.total_planilha, 2)


@dataclass
class Base:
    lancamentos: list[Lancamento]
    conciliacoes: list[Conciliacao] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)


def _competencia_do_arquivo(caminho: Path) -> str | None:
    """``setembro-2026.txt`` -> ``2026-09``; aceita tambem ``2026-09.txt``."""
    from .modelo import MESES, chave

    nome = chave(caminho.stem)
    partes = nome.split()
    if len(partes) == 2 and partes[0] in MESES and partes[1].isdigit():
        return f"{int(partes[1]):04d}-{MESES[partes[0]]:02d}"
    if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
        return f"{int(partes[0]):04d}-{int(partes[1]):02d}"
    return None


def carregar(
    caminho_planilha: str, textos: list[str] | None = None
) -> Base:
    """Le a planilha e os controles em texto e devolve a base consolidada.

    Quando um mes aparece nos dois controles, a planilha e a fonte principal e
    do texto entram apenas os itens que faltam nela -- e o que faltou vira uma
    conciliacao, para que a diferenca fique visivel em vez de sumir na soma.
    """
    base = Base(lancamentos=classificar_todos(ler_abas(caminho_planilha)))

    for caminho_texto in sorted(textos or []):
        arquivo = Path(caminho_texto)
        competencia = _competencia_do_arquivo(arquivo)
        if competencia is None:
            base.avisos.append(
                f"Nao consegui deduzir o mes de {arquivo.name}; "
                f"renomeie para 'setembro-2026.txt'."
            )
            continue

        leitura = ler_texto(arquivo.read_text(encoding="utf-8"), competencia)
        do_mes = [l for l in base.lancamentos if l.competencia == competencia]
        divergencias = conciliar(leitura.lancamentos, do_mes)

        base.conciliacoes.append(Conciliacao(
            competencia=competencia,
            total_texto=round(sum(l.valor for l in leitura.lancamentos), 2),
            total_planilha=round(sum(l.valor for l in do_mes), 2),
            divergencias=divergencias,
        ))

        faltantes = {
            d.descricao for d in divergencias if d.tipo == "so_no_texto"
        }
        for lancamento in leitura.lancamentos:
            if lancamento.descricao in faltantes:
                lancamento.observacao = (
                    "so no controle em texto; ausente na planilha"
                )
                base.lancamentos.append(lancamento)

        base.avisos.extend(
            f"Linha nao entendida em {arquivo.name}: {linha}"
            for linha in leitura.ignoradas
        )

    base.lancamentos.sort(key=lambda l: (l.competencia, -l.valor))
    return base
