"""Agregacoes, deteccao de recorrencia e motor de oportunidades."""

from __future__ import annotations

import datetime as _dt
import statistics
from collections import defaultdict
from dataclasses import dataclass, field

from .modelo import Lancamento, MESES_CURTOS, chave
from .regras import (
    CASA, CONTAS, EDUCACAO, IMPOSTOS, MORADIA, SAUDE, SEGURANCA, SERVICOS,
    papel_de,
)

#: Quantos meses fechados entram na janela usada como "situacao atual".
JANELA = 6

#: Coeficiente de variacao abaixo do qual um gasto recorrente e considerado fixo.
LIMITE_FIXO = 0.15

#: Fracao das ocorrencias que uma grafia precisa somar para nomear a serie.
DOMINANCIA_DE_GRAFIA = 0.6

#: Fracao dos meses da janela em que um item precisa aparecer para ser recorrente.
PRESENCA_RECORRENTE = 0.8

#: Categorias cujo valor nao se renegocia com um telefonema: aluguel e escola
#: sao contratuais e encargos sao definidos por lei.
CATEGORIAS_NAO_NEGOCIAVEIS = {MORADIA, EDUCACAO, IMPOSTOS}

#: Subcategorias que seguem tabela legal ou folha, nao contrato de fornecedor.
SUBCATEGORIAS_NAO_NEGOCIAVEIS = {
    "Encargos (GPS/DAE)", "Salários", "13º e férias", "Rescisão", "IPVA",
    "Aplicação dos filhos",
}


def _cv(valores: list[float]) -> float:
    """Coeficiente de variacao. Zero quando nao ha dispersao mensuravel."""
    if len(valores) < 2:
        return 0.0
    media = statistics.fmean(valores)
    if media == 0:
        return 0.0
    return statistics.pstdev(valores) / media


@dataclass
class Serie:
    """Um item de gasto acompanhado ao longo dos meses."""

    rotulo: str
    categoria: str
    subcategoria: str
    pessoa: str
    natureza: str
    por_mes: dict[str, float] = field(default_factory=dict)
    parcela: int | None = None
    parcela_total: int | None = None

    @property
    def total(self) -> float:
        return round(sum(self.por_mes.values()), 2)

    @property
    def meses(self) -> list[str]:
        return sorted(self.por_mes)

    @property
    def primeiro(self) -> str:
        return self.meses[0] if self.por_mes else ""

    @property
    def ultimo(self) -> str:
        return self.meses[-1] if self.por_mes else ""

    def media_em(self, competencias: list[str]) -> float:
        """Valor tipico do item nos meses em que ele aparece."""
        valores = [self.por_mes[c] for c in competencias if c in self.por_mes]
        return round(statistics.fmean(valores), 2) if valores else 0.0

    def media_mensal_em(self, competencias: list[str]) -> float:
        """Peso do item no orcamento: total da janela dividido por todos os meses.

        Diferente de :meth:`media_em`, que ignora os meses sem ocorrencia. Um
        gasto de 1200 que aconteceu uma vez em seis meses pesa 200 por mes no
        orcamento, ainda que o valor tipico dele seja 1200.
        """
        if not competencias:
            return 0.0
        total = sum(self.por_mes.get(c, 0.0) for c in competencias)
        return round(total / len(competencias), 2)

    def parcela_ativa_em(self, competencias: list[str]) -> bool:
        """A parcela ainda corre se a ultima ocorrencia dela esta na janela."""
        return bool(self.parcela_total) and self.ultimo in competencias

    def presenca_em(self, competencias: list[str]) -> int:
        return sum(1 for c in competencias if c in self.por_mes)

    def tipo_em(self, competencias: list[str]) -> str:
        """Classifica o item como fixo, recorrente variavel, parcelado ou eventual."""
        if self.parcela_ativa_em(competencias):
            return "parcelado"
        presentes = self.presenca_em(competencias)
        if not competencias or presentes == 0:
            return "eventual"
        fracao = presentes / len(competencias)
        if fracao < PRESENCA_RECORRENTE:
            return "eventual"
        valores = [self.por_mes[c] for c in competencias if c in self.por_mes]
        return "fixo" if _cv(valores) <= LIMITE_FIXO else "recorrente variavel"


@dataclass
class Oportunidade:
    titulo: str
    categoria: str
    detalhe: str
    impacto_mensal: float = 0.0
    confianca: str = "media"          # alta | media | a confirmar
    evidencia: list[str] = field(default_factory=list)

    @property
    def impacto_anual(self) -> float:
        return round(self.impacto_mensal * 12, 2)


@dataclass
class Alerta:
    titulo: str
    detalhe: str
    valor: float = 0.0


@dataclass
class Analise:
    lancamentos: list[Lancamento]
    competencias: list[str]
    realizadas: list[str]
    previstas: list[str]
    janela: list[str]
    series: list[Serie]
    oportunidades: list[Oportunidade] = field(default_factory=list)
    alertas: list[Alerta] = field(default_factory=list)

    # -- agregacoes ------------------------------------------------------
    def total_por_mes(self, natureza: str | None = None) -> dict[str, float]:
        saida: dict[str, float] = {c: 0.0 for c in self.competencias}
        for l in self.lancamentos:
            if natureza and l.natureza != natureza:
                continue
            saida[l.competencia] = round(saida.get(l.competencia, 0.0) + l.valor, 2)
        return saida

    def por_categoria_mes(self) -> dict[str, dict[str, float]]:
        saida: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
        for l in self.lancamentos:
            saida[l.categoria][l.competencia] += l.valor
        return {c: {m: round(v, 2) for m, v in sorted(ms.items())}
                for c, ms in saida.items()}

    def por_pessoa_mes(self) -> dict[str, dict[str, float]]:
        saida: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
        for l in self.lancamentos:
            saida[l.pessoa][l.competencia] += l.valor
        return {p: {m: round(v, 2) for m, v in sorted(ms.items())}
                for p, ms in saida.items()}

    def media_mensal(self, mapa: dict[str, float]) -> float:
        valores = [mapa.get(c, 0.0) for c in self.janela]
        return round(statistics.fmean(valores), 2) if valores else 0.0


# --------------------------------------------------------------------------
# Construcao
# --------------------------------------------------------------------------


def montar_series(lancamentos: list[Lancamento]) -> list[Serie]:
    """Agrupa os lancamentos em series acompanhaveis mes a mes.

    A chave e a classificacao -- categoria, subcategoria e pessoa -- e nao o
    texto da descricao. E isso que faz "Akuguel e IPTU", "Aluguel e IPTU" e
    "Aluguel / IPTU" virarem uma serie so, em vez de tres itens que aparecem
    um mes cada e parecem gastos avulsos.
    """
    mapa: dict[tuple, Serie] = {}
    rotulos: dict[tuple, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for l in lancamentos:
        identidade = (l.categoria, l.subcategoria, l.pessoa)
        serie = mapa.get(identidade)
        if serie is None:
            serie = Serie(
                rotulo=l.rotulo,
                categoria=l.categoria,
                subcategoria=l.subcategoria,
                pessoa=l.pessoa,
                natureza=l.natureza,
            )
            mapa[identidade] = serie
        serie.por_mes[l.competencia] = round(
            serie.por_mes.get(l.competencia, 0.0) + l.valor, 2
        )
        rotulos[identidade][l.rotulo] += 1
        # Guarda a parcela mais avancada vista, que e a que diz quanto falta.
        if l.parcela_total and (l.parcela or 0) > (serie.parcela or 0):
            serie.parcela = l.parcela
            serie.parcela_total = l.parcela_total

    for identidade, serie in mapa.items():
        serie.rotulo = _melhor_rotulo(rotulos[identidade], serie)

    return sorted(mapa.values(), key=lambda s: -s.total)


def _melhor_rotulo(contagem: dict[str, int], serie: Serie) -> str:
    """Nome de exibicao da serie.

    Com uma unica grafia, usa a grafia. Com varias -- consertos diferentes,
    o mesmo aluguel escrito de tres jeitos -- usa a subcategoria, que e o que
    as linhas tem em comum, e acrescenta a pessoa quando o gasto e de alguem.
    """
    distintos = {r: n for r, n in contagem.items() if r}
    if not distintos:
        return serie.subcategoria or serie.categoria
    grafia, ocorrencias = max(distintos.items(), key=lambda kv: kv[1])
    total = sum(distintos.values())
    # Uma grafia dominante e o nome que a casa usa; sem dominante, as linhas
    # sao coisas diferentes e o que elas tem em comum e a subcategoria.
    if len(distintos) == 1 or ocorrencias / total >= DOMINANCIA_DE_GRAFIA:
        return grafia
    base = serie.subcategoria or serie.categoria
    if serie.pessoa != CASA and serie.pessoa not in base:
        return f"{base} - {serie.pessoa}"
    return base


def analisar(
    lancamentos: list[Lancamento], hoje: _dt.date | None = None
) -> Analise:
    hoje = hoje or _dt.date.today()
    atual = f"{hoje.year:04d}-{hoje.month:02d}"
    competencias = sorted({l.competencia for l in lancamentos})
    realizadas = [c for c in competencias if c <= atual]
    previstas = [c for c in competencias if c > atual]
    # A janela usa meses ja fechados; o mes corrente ainda esta incompleto.
    fechadas = [c for c in realizadas if c < atual]
    janela = fechadas[-JANELA:] if fechadas else realizadas[-JANELA:]

    series = montar_series(lancamentos)
    analise = Analise(
        lancamentos=lancamentos,
        competencias=competencias,
        realizadas=realizadas,
        previstas=previstas,
        janela=janela,
        series=series,
    )
    analise.oportunidades = detectar_oportunidades(analise)
    return analise


# --------------------------------------------------------------------------
# Oportunidades
# --------------------------------------------------------------------------


def _formata(valor: float) -> str:
    inteiro = f"{valor:,.2f}"
    return "R$ " + inteiro.replace(",", "@").replace(".", ",").replace("@", ".")


def _decimal(valor: float, casas: int = 1) -> str:
    """Numero com virgula decimal, como se escreve em portugues."""
    return f"{valor:.{casas}f}".replace(".", ",")


def _rotulo_mes(competencia: str) -> str:
    ano, mes = competencia.split("-")
    return f"{MESES_CURTOS[int(mes)]}/{ano[2:]}"


def detectar_oportunidades(analise: Analise) -> list[Oportunidade]:
    achados: list[Oportunidade] = []
    janela = analise.janela
    ativas = [s for s in analise.series if s.presenca_em(janela) > 0]

    achados += _fornecedores_concorrentes(ativas, janela)
    achados += _contas_com_pico(ativas, janela)
    achados += _parcelas_a_terminar(ativas, janela)
    achados += _concentracao(analise, ativas, janela)
    achados += _itens_estaveis_grandes(ativas, janela)

    return sorted(achados, key=lambda o: -o.impacto_mensal)


#: Grupos de fornecedores que entregam servicos proximos e podem ser
#: renegociados ou consolidados em um contrato so.
GRUPOS_CONSOLIDAVEIS = [
    ("Segurança", SEGURANCA, ["Câmeras", "Monitoramento", "Vigilância da rua"],
     "Três contratos separados de segurança para o mesmo endereço."),
    ("Telecom", CONTAS, ["Internet e TV", "Telefonia"],
     "Internet/TV e telefonia em contas separadas."),
    ("Limpeza e lavanderia", SERVICOS, ["Lavanderia", "Enjoy House"],
     "Serviços de limpeza e lavanderia contratados em paralelo."),
]


def _fornecedores_concorrentes(series: list[Serie], janela: list[str]) -> list[Oportunidade]:
    saida = []
    for titulo, categoria, subcategorias, detalhe in GRUPOS_CONSOLIDAVEIS:
        membros = [s for s in series
                   if s.categoria == categoria and s.subcategoria in subcategorias]
        if len(membros) < 2:
            continue
        total = round(sum(s.media_mensal_em(janela) for s in membros), 2)
        if total <= 0:
            continue
        saida.append(Oportunidade(
            titulo=f"Consolidar {titulo.lower()}",
            categoria=categoria,
            detalhe=(
                f"{detalhe} Somados, são {_formata(total)} por mês. "
                f"Uma renegociação única de 15% devolve "
                f"{_formata(total * 0.15)} por mês."
            ),
            impacto_mensal=round(total * 0.15, 2),
            confianca="media",
            evidencia=[
                f"{s.rotulo}: {_formata(s.media_mensal_em(janela))}/mês"
                for s in sorted(membros, key=lambda s: -s.media_mensal_em(janela))
            ],
        ))
    return saida


def _contas_com_pico(series: list[Serie], janela: list[str]) -> list[Oportunidade]:
    """Contas de consumo cujo pico destoa da mediana indicam desperdicio."""
    saida = []
    for serie in series:
        if serie.categoria not in {CONTAS, SERVICOS}:
            continue
        valores = [serie.por_mes[c] for c in janela if c in serie.por_mes]
        if len(valores) < 4:
            continue
        mediana = statistics.median(valores)
        maximo = max(valores)
        if mediana <= 0 or maximo < 2.5 * mediana or maximo - mediana < 200:
            continue
        mes_pico = max(
            (c for c in janela if c in serie.por_mes),
            key=lambda c: serie.por_mes[c],
        )
        saida.append(Oportunidade(
            titulo=f"Investigar picos em {serie.rotulo}",
            categoria=serie.categoria,
            detalhe=(
                f"A mediana de {serie.rotulo} na janela é {_formata(mediana)}, "
                f"mas em {_rotulo_mes(mes_pico)} a conta foi {_formata(maximo)}, "
                f"{_decimal(maximo / mediana)} vezes a mediana. Vazamento, tarifa "
                f"errada ou consumo pontual valem a checagem."
            ),
            impacto_mensal=round((maximo - mediana) / len(janela), 2),
            confianca="a confirmar",
            evidencia=[f"{_rotulo_mes(c)}: {_formata(serie.por_mes[c])}"
                       for c in janela if c in serie.por_mes],
        ))
    return saida


def _parcelas_a_terminar(series: list[Serie], janela: list[str]) -> list[Oportunidade]:
    saida = []
    for serie in series:
        if not serie.parcela or not serie.parcela_ativa_em(janela):
            continue
        restantes = serie.parcela_total - serie.parcela
        if restantes < 0:
            continue
        valor = serie.media_em(janela) or (serie.total / max(len(serie.por_mes), 1))
        saida.append(Oportunidade(
            titulo=f"Parcela termina: {serie.rotulo}",
            categoria=serie.categoria,
            detalhe=(
                f"Parcela {serie.parcela} de {serie.parcela_total} a "
                f"{_formata(valor)}. Faltam {restantes}; quando acabar, "
                f"{_formata(valor)} por mês voltam para o caixa."
            ),
            impacto_mensal=round(valor, 2),
            confianca="alta",
            evidencia=[f"última ocorrência em {_rotulo_mes(serie.ultimo)}"],
        ))
    return saida


def _concentracao(
    analise: Analise, series: list[Serie], janela: list[str]
) -> list[Oportunidade]:
    """Aponta a categoria que domina o gasto -- onde qualquer ganho e maior."""
    por_categoria = defaultdict(float)
    for serie in series:
        por_categoria[serie.categoria] += serie.media_mensal_em(janela)
    if not por_categoria:
        return []
    total = sum(por_categoria.values())
    # Aluguel e escola sao contratuais: entram no total, mas nao sao o alvo.
    alvos = {c: v for c, v in por_categoria.items()
             if c not in {MORADIA, EDUCACAO}}
    if not alvos:
        return []
    maior, valor = max(alvos.items(), key=lambda kv: kv[1])
    if total <= 0 or valor / total < 0.15:
        return []
    membros = sorted(
        (s for s in series if s.categoria == maior),
        key=lambda s: -s.media_mensal_em(janela),
    )[:6]
    return [Oportunidade(
        titulo=f"{maior} é a maior categoria ajustável da casa",
        categoria=maior,
        detalhe=(
            f"{maior} custa {_formata(valor)} por mês, {valor / total:.0%} de "
            f"tudo o que sai. Fora aluguel e escola, que são contratuais, é a "
            f"maior categoria da casa. Uma redução de 10% aqui vale mais do "
            f"que zerar categorias inteiras lá embaixo: "
            f"{_formata(valor * 0.10)} por mês."
        ),
        impacto_mensal=round(valor * 0.10, 2),
        confianca="alta",
        evidencia=[f"{s.rotulo}: {_formata(s.media_mensal_em(janela))}/mês"
                   for s in membros],
    )]


def _verbo_de_revisao(serie: Serie) -> str:
    """Saude nao se "renegocia" como um contrato de internet."""
    return "Revisar" if serie.categoria == SAUDE else "Renegociar"


def _itens_estaveis_grandes(series: list[Serie], janela: list[str]) -> list[Oportunidade]:
    """Contratos fixos e caros: onde a renegociacao tem efeito composto."""
    saida = []
    for serie in series:
        if serie.natureza != "despesa":
            continue
        if serie.tipo_em(janela) != "fixo":
            continue
        media = serie.media_em(janela)
        if media < 1500:
            continue
        if serie.categoria in CATEGORIAS_NAO_NEGOCIAVEIS:
            continue
        if serie.subcategoria in SUBCATEGORIAS_NAO_NEGOCIAVEIS:
            continue
        saida.append(Oportunidade(
            titulo=f"{_verbo_de_revisao(serie)} {serie.rotulo}",
            categoria=serie.categoria,
            detalhe=(
                f"{_formata(media)} por mês, com pouca variação nos "
                f"últimos {len(janela)} meses, {_formata(media * 12)} por ano. "
                f"Valor estável é o candidato natural a uma revisão de contrato."
            ),
            impacto_mensal=round(media * 0.10, 2),
            confianca="media",
            evidencia=[f"{_rotulo_mes(c)}: {_formata(serie.por_mes[c])}"
                       for c in janela if c in serie.por_mes],
        ))
    return saida
