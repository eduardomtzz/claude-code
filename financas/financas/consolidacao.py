"""Junta a planilha e o controle em texto num unico conjunto de lancamentos."""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from pathlib import Path

from . import parcelas as mod_parcelas
from .fatura import Fatura, ler_varias
from .modelo import Lancamento
from .planilha import ler_abas
from .regras import classificar_todos, marcar_avulsos
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
class Sobreposicao:
    """Um gasto que parece estar sendo contado na planilha e no cartao."""

    competencia: str
    categoria: str
    subcategoria: str
    valor_planilha: float
    valor_cartao: float
    meses_em_comum: list[str] = field(default_factory=list)
    itens_cartao: list[str] = field(default_factory=list)


@dataclass
class Base:
    lancamentos: list[Lancamento]
    conciliacoes: list[Conciliacao] = field(default_factory=list)
    faturas: list[Fatura] = field(default_factory=list)
    parcelamentos: list[mod_parcelas.Parcelamento] = field(default_factory=list)
    sobreposicoes: list[Sobreposicao] = field(default_factory=list)
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
    caminho_planilha: str, textos: list[str] | None = None,
    faturas: list[str] | None = None,
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

    if faturas:
        _juntar_faturas(base, faturas)

    # A regra de avulsos olha a base inteira, entao roda de novo depois que as
    # faturas entraram: um nome que so aparecia uma vez na planilha pode ser
    # recorrente no cartao.
    marcar_avulsos(base.lancamentos)
    base.lancamentos.sort(key=lambda l: (l.competencia, -l.valor))
    return base


#: Uma categoria so e apontada como possivel duplicidade quando os dois
#: controles registram valores relevantes nela.
MINIMO_DE_SOBREPOSICAO = 300.0

#: E quando isso se repete em ao menos este tanto de meses. Um mes em comum e
#: coincidencia; tres meses e um padrao.
MESES_DE_SOBREPOSICAO = 3


def _juntar_faturas(base: Base, caminhos: list[str]) -> None:
    """Acrescenta as compras do cartao e aponta o que pode estar em dobro."""
    lidas, avisos = ler_varias(caminhos)
    base.faturas = lidas
    base.avisos.extend(avisos)

    cobertas = {f.competencia for f in lidas if f.competencia}
    # Onde existe fatura, as linhas de cartao da planilha viram duplicata.
    base.lancamentos = [
        l for l in base.lancamentos
        if not (l.forma == "cartao" and l.competencia in cobertas)
    ]
    for fatura in lidas:
        base.lancamentos.extend(fatura.lancamentos)

    base.parcelamentos = mod_parcelas.em_curso(lidas)
    _apontar_sobreposicoes(base, cobertas)


def _apontar_sobreposicoes(base: Base, cobertas: set[str]) -> None:
    """Marca o que a planilha e o cartao parecem cobrar ao mesmo tempo.

    Coincidir de categoria num mes nao quer dizer nada: jantar fora e jantar
    fora, esteja no boleto ou no cartao. O que importa e a repeticao -- a mesma
    subcategoria saindo pelos dois controles em varios meses seguidos e o que
    sugere que uma conta esta sendo contada duas vezes no piso.

    A funcao nao decide qual dos dois esta certo. Quem sabe se a hipica do
    boleto e a mesma da fatura e quem paga.
    """
    from collections import defaultdict

    meses_por_fonte: dict[tuple, dict[str, set[str]]] = defaultdict(
        lambda: {"planilha": set(), "cartao": set()}
    )
    valores: dict[tuple, dict[str, float]] = defaultdict(
        lambda: {"planilha": 0.0, "cartao": 0.0}
    )
    itens: dict[tuple, set[str]] = defaultdict(set)

    for l in base.lancamentos:
        if l.competencia not in cobertas or not l.subcategoria:
            continue
        identidade = (l.categoria, l.subcategoria)
        fonte = "cartao" if l.origem.startswith("fatura:") else "planilha"
        meses_por_fonte[identidade][fonte].add(l.competencia)
        valores[identidade][fonte] += l.valor
        if fonte == "cartao":
            itens[identidade].add(l.descricao)

    for identidade, meses in sorted(meses_por_fonte.items()):
        comuns = meses["planilha"] & meses["cartao"]
        if len(comuns) < MESES_DE_SOBREPOSICAO:
            continue
        soma = valores[identidade]
        if min(soma["planilha"], soma["cartao"]) < MINIMO_DE_SOBREPOSICAO:
            continue
        categoria, subcategoria = identidade
        base.sobreposicoes.append(Sobreposicao(
            competencia=min(comuns),
            categoria=categoria,
            subcategoria=subcategoria,
            valor_planilha=round(soma["planilha"], 2),
            valor_cartao=round(soma["cartao"], 2),
            meses_em_comum=sorted(comuns),
            itens_cartao=sorted(itens[identidade])[:6],
        ))
    base.sobreposicoes.sort(key=lambda s: -min(s.valor_planilha, s.valor_cartao))
