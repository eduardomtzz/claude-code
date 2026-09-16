"""Monta o payload do painel e injeta no template HTML."""

from __future__ import annotations

import datetime as _dt
import json
from collections import defaultdict
from pathlib import Path

from . import baseline as mod_baseline
from .analise import Analise, analisar
from .consolidacao import Base
from .modelo import MESES_CURTOS
from .regras import CATEGORIAS, CASA, SEM_CATEGORIA, papel_de

MARCA = "/*__DADOS__*/null"

#: Quantas categorias ganham cor propria no grafico empilhado. O resto vira
#: "Outros" -- a paleta categorica nao comporta mais do que isso com seguranca.
FAIXAS_COLORIDAS = 6


def rotulo_mes(competencia: str) -> str:
    ano, mes = competencia.split("-")
    return f"{MESES_CURTOS[int(mes)]}/{ano[2:]}"


def _media(mapa: dict[str, float], janela: list[str]) -> float:
    if not janela:
        return 0.0
    return round(sum(mapa.get(c, 0.0) for c in janela) / len(janela), 2)


def montar_payload(
    base: Base, hoje: _dt.date | None = None,
    regime: str | None = None, confirmados: str | None = None,
) -> dict:
    hoje = hoje or _dt.date.today()
    analise = analisar(base.lancamentos, hoje)
    linha_base = mod_baseline.montar(analise, regime, confirmados)
    janela = analise.janela

    por_categoria = analise.por_categoria_mes()
    por_pessoa = analise.por_pessoa_mes()
    totais = analise.total_por_mes()

    ordenadas = sorted(
        por_categoria.items(), key=lambda kv: -_media(kv[1], janela)
    )
    # A cor no grafico historico segue o peso em toda a base, nao o da janela:
    # senao a escola, que dominou 2024 e 2025, cairia no cinza de "Outros"
    # justamente nos meses em que ela era o maior gasto da casa.
    coloridas = [
        nome for nome, _ in sorted(
            por_categoria.items(), key=lambda kv: -sum(kv[1].values())
        )[:FAIXAS_COLORIDAS]
    ]

    meses = [{
        "id": c,
        "rotulo": rotulo_mes(c),
        "total": round(totais.get(c, 0.0), 2),
        "previsao": c in analise.previstas,
        "parcial": c == f"{hoje.year:04d}-{hoje.month:02d}",
    } for c in analise.competencias]

    categorias = [{
        "nome": nome,
        "media_mensal": _media(por_mes, janela),
        "total": round(sum(por_mes.values()), 2),
        "por_mes": {c: round(por_mes.get(c, 0.0), 2)
                    for c in analise.competencias},
        "colorida": nome in coloridas,
        "subcategorias": _subcategorias(analise, nome, janela),
    } for nome, por_mes in ordenadas]

    pessoas = [{
        "nome": nome,
        "papel": papel_de(nome),
        "media_mensal": _media(por_mes, janela),
        "total": round(sum(por_mes.values()), 2),
        "por_mes": {c: round(por_mes.get(c, 0.0), 2)
                    for c in analise.competencias},
        "itens": [
            {"rotulo": s.rotulo, "media_mensal": s.media_mensal_em(janela),
             "categoria": s.categoria}
            for s in sorted(
                (s for s in analise.series if s.pessoa == nome),
                key=lambda s: -s.media_mensal_em(janela),
            )[:8]
        ],
    } for nome, por_mes in sorted(
        por_pessoa.items(), key=lambda kv: -_media(kv[1], janela)
    )]

    series = [{
        "rotulo": s.rotulo,
        "categoria": s.categoria,
        "subcategoria": s.subcategoria,
        "pessoa": s.pessoa,
        "natureza": s.natureza,
        "tipo": s.tipo_em(janela),
        "valor_tipico": s.media_em(janela),
        "media_mensal": s.media_mensal_em(janela),
        "total": s.total,
        "meses_ativos": s.presenca_em(janela),
        "primeiro": rotulo_mes(s.primeiro) if s.primeiro else "",
        "ultimo": rotulo_mes(s.ultimo) if s.ultimo else "",
        "parcela": s.parcela,
        "parcela_total": s.parcela_total,
        "por_mes": {c: round(v, 2) for c, v in sorted(s.por_mes.items())},
    # A tabela descreve a estrutura atual: series que nao aparecem na janela
    # sao historico, e estao na secao de mudancas de patamar.
    } for s in analise.series if s.presenca_em(janela) > 0]

    resumo_tipos = defaultdict(float)
    for s in analise.series:
        resumo_tipos[s.tipo_em(janela)] += s.media_mensal_em(janela)

    return {
        "gerado_em": hoje.isoformat(),
        "competencia_atual": f"{hoje.year:04d}-{hoje.month:02d}",
        "janela": [rotulo_mes(c) for c in janela],
        "janela_ids": janela,
        "meses": meses,
        "categorias": categorias,
        "ordem_categorias": [c for c in CATEGORIAS],
        "pessoas": pessoas,
        "series": series,
        "resumo_tipos": {k: round(v, 2) for k, v in resumo_tipos.items()},
        "oportunidades": [{
            "titulo": o.titulo,
            "categoria": o.categoria,
            "detalhe": o.detalhe,
            "impacto_mensal": o.impacto_mensal,
            "impacto_anual": o.impacto_anual,
            "confianca": o.confianca,
            "evidencia": o.evidencia,
        } for o in analise.oportunidades],
        "conciliacoes": [{
            "competencia": c.competencia,
            "rotulo": rotulo_mes(c.competencia),
            "total_texto": c.total_texto,
            "total_planilha": c.total_planilha,
            "diferenca": c.diferenca,
            "divergencias": [{
                "tipo": d.tipo,
                "descricao": d.descricao,
                "categoria": d.categoria,
                "valor_texto": d.valor_texto,
                "valor_planilha": d.valor_planilha,
            } for d in c.divergencias],
        } for c in base.conciliacoes],
        "baseline": _baseline(linha_base),
        "mudancas": _mudancas(analise, hoje),
        "pendencias": [{
            "rotulo": s.rotulo,
            "total": s.total,
            "primeiro": rotulo_mes(s.primeiro) if s.primeiro else "",
            "ultimo": rotulo_mes(s.ultimo) if s.ultimo else "",
        } for s in analise.series if s.categoria == SEM_CATEGORIA],
        "lancamentos": [{
            "competencia": l.competencia,
            "rotulo_mes": rotulo_mes(l.competencia),
            "descricao": l.descricao,
            "valor": l.valor,
            "categoria": l.categoria,
            "subcategoria": l.subcategoria,
            "pessoa": l.pessoa,
            "forma": l.forma,
            "natureza": l.natureza,
            "origem": "texto" if l.origem == "texto" else "planilha",
            "observacao": l.observacao,
        } for l in base.lancamentos],
        "avisos": base.avisos,
    }


def _baseline(linha_base: mod_baseline.Baseline) -> dict:
    compromisso = lambda c: {
        "rotulo": c.rotulo, "categoria": c.categoria,
        "subcategoria": c.subcategoria, "pessoa": c.pessoa, "valor": c.valor,
        "natureza": c.natureza, "origem": c.origem, "nota": c.nota,
        "meses_observados": c.meses_observados, "meses_regime": c.meses_regime,
    }
    return {
        "regime_inicio": linha_base.regime_inicio,
        "regime_rotulo": rotulo_mes(linha_base.regime_inicio) if linha_base.regime_inicio else "",
        "meses_regime": [rotulo_mes(c) for c in linha_base.meses_regime],
        "piso": linha_base.piso,
        "poupanca": linha_base.poupanca,
        "variavel_esperado": linha_base.variavel_esperado,
        "provisao_sazonal": linha_base.provisao_sazonal,
        "meses_sazonais": [rotulo_mes(c) for c in linha_base.meses_sazonais],
        "esperado": linha_base.esperado,
        "completo": linha_base.completo,
        "comprometidos": [compromisso(c) for c in linha_base.comprometidos],
        "variaveis": [compromisso(c) for c in linha_base.variaveis],
        "sazonais": [compromisso(c) for c in linha_base.sazonais],
        "pendentes": [compromisso(c) for c in linha_base.pendentes],
    }


#: Uma serie precisa aparecer ao menos este tanto de vezes para que a entrada
#: ou a saida dela conte como mudanca estrutural, e nao como gasto avulso.
MINIMO_OCORRENCIAS = 3

#: E pesar ao menos este valor por mes enquanto esteve ativa.
MINIMO_MENSAL = 400.0


def _mudancas(analise: Analise, hoje: _dt.date) -> dict[str, list[dict]]:
    """Itens que entraram ou sairam do orcamento -- a mudanca de patamar.

    Comparar um mes de 2024 com um de 2026 sem isso e comparar duas casas
    diferentes: a escola dos filhos sai da planilha, o aluguel entra.
    """
    atual = f"{hoje.year:04d}-{hoje.month:02d}"
    realizadas = analise.realizadas
    if len(realizadas) < 6:
        return {"sairam": [], "entraram": []}
    corte_saida = realizadas[-4]
    corte_entrada = realizadas[-14] if len(realizadas) > 14 else realizadas[0]

    sairam, entraram = [], []
    for serie in analise.series:
        if len(serie.por_mes) < MINIMO_OCORRENCIAS:
            continue
        ativo = round(sum(serie.por_mes.values()) / len(serie.por_mes), 2)
        if ativo < MINIMO_MENSAL:
            continue
        registro = {
            "rotulo": serie.rotulo,
            "categoria": serie.categoria,
            "pessoa": serie.pessoa,
            "valor_tipico": ativo,
            "primeiro": rotulo_mes(serie.primeiro),
            "ultimo": rotulo_mes(serie.ultimo),
            "meses": len(serie.por_mes),
        }
        if serie.ultimo < corte_saida:
            sairam.append(registro)
        elif serie.primeiro > corte_entrada:
            entraram.append(registro)

    ordenar = lambda itens: sorted(itens, key=lambda r: -r["valor_tipico"])[:12]
    return {"sairam": ordenar(sairam), "entraram": ordenar(entraram)}


def _subcategorias(analise: Analise, categoria: str, janela: list[str]) -> list[dict]:
    """Subcategorias de uma categoria, com a serie mensal completa.

    O mes a mes vai junto para que o seletor de periodo do painel recalcule as
    subcategorias sem precisar voltar ao Python.
    """
    agrupado: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for serie in analise.series:
        if serie.categoria != categoria:
            continue
        destino = agrupado[serie.subcategoria or categoria]
        for competencia, valor in serie.por_mes.items():
            destino[competencia] += valor
    saida = [
        {
            "nome": nome,
            "media_mensal": _media(por_mes, janela),
            "por_mes": {c: round(por_mes.get(c, 0.0), 2)
                        for c in analise.competencias},
        }
        for nome, por_mes in agrupado.items()
    ]
    return sorted(
        (s for s in saida if sum(s["por_mes"].values()) > 0),
        key=lambda s: -s["media_mensal"],
    )


def renderizar(payload: dict, template: Path, destino: Path) -> Path:
    """Injeta o payload no template e grava o painel autocontido."""
    html = template.read_text(encoding="utf-8")
    if MARCA not in html:
        raise ValueError(f"marcador {MARCA!r} nao encontrado em {template}")
    dados = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    destino.write_text(html.replace(MARCA, dados), encoding="utf-8")
    return destino
