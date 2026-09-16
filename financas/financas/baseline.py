"""Piso mensal: de quanto se parte antes de decidir qualquer gasto novo.

O baseline responde a uma pergunta diferente da do historico. O historico diz
quanto saiu; o baseline diz quanto vai sair de novo no mes que vem sem que
ninguem decida nada. Por isso ele olha so o regime atual -- depois da mudanca de
casa, um mes de 2024 nao diz mais nada sobre o proximo -- e separa tres coisas:

* **comprometido**: aparece em quase todo mes do regime. E o piso.
* **variavel**: aparece com frequencia mas oscila. Entra por media, nao por
  valor fixo, porque o valor de um mes nao prediz o do outro.
* **pendente**: sabe-se que existe e ainda nao se sabe quanto. Fica visivel
  com valor zero em vez de sumir da conta e dar um piso falsamente baixo.
"""

from __future__ import annotations

import json
import statistics
from dataclasses import dataclass, field
from pathlib import Path

from .analise import Analise, Serie
from .modelo import chave
from .regras import AVULSOS

#: Presenca minima nos meses do regime para o item ser parte do piso.
PRESENCA_COMPROMETIDA = 0.8

#: Abaixo desta presenca o item e avulso e nao entra no baseline.
PRESENCA_VARIAVEL = 0.4

#: Quantos meses de historico entram no rateio das despesas sazonais.
MESES_DE_SAZONAIS = 12

#: Subcategorias que voltam uma vez por ano por natureza, e por isso entram na
#: provisao mesmo sem terem ocorrido ainda dentro do regime atual.
ANUAIS = {"13º e férias", "IPVA", "IPTU", "Contabilidade e IRPF", "Rescisão"}


@dataclass
class Compromisso:
    rotulo: str
    categoria: str
    subcategoria: str
    pessoa: str
    valor: float
    tipo: str                 # comprometido | variavel | pendente
    natureza: str = "despesa"
    meses_observados: int = 0
    meses_regime: int = 0
    origem: str = "histórico"  # histórico | confirmado | pendente
    nota: str = ""


@dataclass
class Baseline:
    regime_inicio: str
    meses_regime: list[str]
    comprometidos: list[Compromisso] = field(default_factory=list)
    variaveis: list[Compromisso] = field(default_factory=list)
    sazonais: list[Compromisso] = field(default_factory=list)
    pendentes: list[Compromisso] = field(default_factory=list)
    meses_sazonais: list[str] = field(default_factory=list)

    @property
    def piso(self) -> float:
        """O que sai todo mes sem ninguem decidir nada."""
        return round(sum(c.valor for c in self.comprometidos), 2)

    @property
    def poupanca(self) -> float:
        """Parte do piso que e aplicacao, e nao consumo."""
        return round(
            sum(c.valor for c in self.comprometidos if c.natureza == "poupanca"), 2
        )

    @property
    def variavel_esperado(self) -> float:
        return round(sum(c.valor for c in self.variaveis), 2)

    @property
    def provisao_sazonal(self) -> float:
        """Quanto guardar por mes para o que so acontece uma vez por ano."""
        return round(sum(c.valor for c in self.sazonais), 2)

    @property
    def esperado(self) -> float:
        """Piso, mais o que oscila, mais o rateio do que e anual.

        E o numero de planejamento: abaixo dele o mes so fecha por sorte.
        """
        return round(
            self.piso + self.variavel_esperado + self.provisao_sazonal, 2
        )

    @property
    def completo(self) -> bool:
        return not self.pendentes


def detectar_regime(analise: Analise) -> str:
    """Mes em que o orcamento atual comecou.

    Usa a entrada do maior recorrente novo: quando o aluguel entra, a casa
    anterior deixou de existir e os meses antes dele nao descrevem mais o que
    vem pela frente.
    """
    realizadas = analise.realizadas
    if len(realizadas) < 4:
        return realizadas[0] if realizadas else ""
    corte = realizadas[-14] if len(realizadas) > 14 else realizadas[0]
    candidatos = [
        s for s in analise.series
        if s.primeiro > corte and len(s.por_mes) >= 3 and s.total > 0
    ]
    if not candidatos:
        return realizadas[max(len(realizadas) - 6, 0)]
    maior = max(candidatos, key=lambda s: s.total / max(len(s.por_mes), 1))
    return maior.primeiro


def _carregar_confirmados(caminho: str | None) -> dict:
    if not caminho:
        return {}
    dados = json.loads(Path(caminho).read_text(encoding="utf-8"))
    return dados if isinstance(dados, dict) else {}


def montar(
    analise: Analise, regime_inicio: str | None = None,
    confirmados: str | None = None,
) -> Baseline:
    config = _carregar_confirmados(confirmados)
    inicio = regime_inicio or config.get("regime_inicio") or detectar_regime(analise)
    meses = [c for c in analise.realizadas if c >= inicio]
    base = Baseline(regime_inicio=inicio, meses_regime=meses)
    if not meses:
        return base

    fixados = {
        chave(item.get("rotulo", "")): item
        for item in config.get("confirmados", [])
    }
    usados: set[str] = set()

    for serie in analise.series:
        presentes = serie.presenca_em(meses)
        if presentes == 0 or serie.categoria == AVULSOS:
            continue
        fracao = presentes / len(meses)
        if fracao < PRESENCA_VARIAVEL:
            continue

        valores = [serie.por_mes[c] for c in meses if c in serie.por_mes]
        comprometido = fracao >= PRESENCA_COMPROMETIDA
        # Comprometido usa a mediana: o valor que se repete, imune a um mes
        # atipico. Variavel usa a media sobre todos os meses do regime, que e
        # o peso real dele no orcamento, inclusive os meses em que nao veio.
        valor = (
            round(statistics.median(valores), 2) if comprometido
            else round(sum(valores) / len(meses), 2)
        )

        item = fixados.get(chave(serie.rotulo))
        if item:
            usados.add(chave(serie.rotulo))
            valor = round(float(item.get("valor", valor)), 2)

        compromisso = Compromisso(
            rotulo=item.get("rotulo", serie.rotulo) if item else serie.rotulo,
            categoria=serie.categoria,
            subcategoria=serie.subcategoria,
            pessoa=serie.pessoa,
            valor=valor,
            tipo="comprometido" if comprometido else "variavel",
            natureza=serie.natureza,
            meses_observados=presentes,
            meses_regime=len(meses),
            origem="confirmado" if item else "histórico",
            nota=item.get("nota", "") if item else "",
        )
        alvo = base.comprometidos if comprometido else base.variaveis
        alvo.append(compromisso)

    # Itens que o titular confirmou e que o historico ainda nao mostra: um
    # gasto novo tem um mes de base, e um mes nao vira recorrencia sozinho.
    for identificador, item in fixados.items():
        if identificador in usados:
            continue
        base.comprometidos.append(Compromisso(
            rotulo=item.get("rotulo", ""),
            categoria=item.get("categoria", ""),
            subcategoria=item.get("subcategoria", ""),
            pessoa=item.get("pessoa", "Casa"),
            valor=round(float(item.get("valor", 0.0)), 2),
            tipo="comprometido",
            meses_observados=0,
            meses_regime=len(meses),
            origem="confirmado",
            nota=item.get("nota", ""),
        ))

    for item in config.get("pendentes", []):
        base.pendentes.append(Compromisso(
            rotulo=item.get("rotulo", ""),
            categoria=item.get("categoria", ""),
            subcategoria="",
            pessoa=item.get("pessoa", "Casa"),
            valor=round(float(item.get("valor", 0.0)), 2),
            tipo="pendente",
            meses_regime=len(meses),
            origem="pendente",
            nota=item.get("nota", ""),
        ))

    _ratear_sazonais(analise, base)
    base.comprometidos.sort(key=lambda c: -c.valor)
    base.variaveis.sort(key=lambda c: -c.valor)
    base.sazonais.sort(key=lambda c: -c.valor)
    return base


def _ratear_sazonais(analise: Analise, base: Baseline) -> None:
    """Rateia por mes o que so acontece uma ou duas vezes por ano.

    13o, ferias, IPVA e IPTU nao aparecem em mes nenhum do regime, entao o
    piso os ignora -- e quem planeja pelo piso leva um susto em dezembro. Aqui
    eles voltam divididos pelos doze meses, como provisao.
    """
    ja_contados = {
        (c.categoria, c.subcategoria, c.pessoa)
        for c in base.comprometidos + base.variaveis
    }
    janela = analise.realizadas[-MESES_DE_SAZONAIS:]
    if not janela:
        return
    base.meses_sazonais = janela

    for serie in analise.series:
        if serie.categoria == AVULSOS:
            continue
        if (serie.categoria, serie.subcategoria, serie.pessoa) in ja_contados:
            continue
        # Gasto que parou antes do regime atual pertence a casa anterior: a
        # pintura da casa antiga nao volta. O que e anual por natureza fica,
        # mesmo sem ter acontecido ainda depois da mudanca.
        if serie.ultimo < base.regime_inicio and serie.subcategoria not in ANUAIS:
            continue
        total = sum(serie.por_mes.get(c, 0.0) for c in janela)
        if total <= 0:
            continue
        base.sazonais.append(Compromisso(
            rotulo=serie.rotulo,
            categoria=serie.categoria,
            subcategoria=serie.subcategoria,
            pessoa=serie.pessoa,
            # Sempre dividido por doze, e nao pelos meses disponiveis: um gasto
            # anual visto num historico de seis meses nao custa o dobro.
            valor=round(total / MESES_DE_SAZONAIS, 2),
            tipo="sazonal",
            natureza=serie.natureza,
            meses_observados=serie.presenca_em(janela),
            meses_regime=len(janela),
            origem="histórico",
            nota=(f"{_formata_total(total)} observados em {len(janela)} "
                  f"{'mês' if len(janela) == 1 else 'meses'}, rateado por "
                  f"{MESES_DE_SAZONAIS}"),
        ))


def _formata_total(valor: float) -> str:
    inteiro = f"{valor:,.2f}"
    return "R$ " + inteiro.replace(",", "@").replace(".", ",").replace("@", ".")
