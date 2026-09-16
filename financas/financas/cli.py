"""Linha de comando: le a planilha e os controles em texto e gera o painel.

    python -m financas.cli planilha.xlsx --texto dados/setembro-2026.txt
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import sys
from pathlib import Path

from .consolidacao import carregar
from .painel import montar_payload, renderizar

RAIZ = Path(__file__).resolve().parent.parent
TEMPLATE = RAIZ / "dashboard" / "template.html"


def argumentos(argv: list[str] | None = None) -> argparse.Namespace:
    analisador = argparse.ArgumentParser(
        prog="financas",
        description="Categoriza os pagamentos da casa e gera o painel.",
    )
    analisador.add_argument("planilha", help="arquivo .xlsx com as abas mensais")
    analisador.add_argument(
        "--texto", action="append", default=[], metavar="ARQUIVO",
        help="controle mensal em texto (repetivel); o nome do arquivo da o mes",
    )
    analisador.add_argument(
        "--saida", default="dados", metavar="PASTA",
        help="pasta de saida (padrao: dados)",
    )
    analisador.add_argument(
        "--fatura", action="append", default=[], metavar="ARQUIVO",
        help="fatura de cartao em PDF (repetivel)",
    )
    analisador.add_argument(
        "--confirmados", metavar="ARQUIVO",
        help="json com os valores confirmados pelo titular e o que falta",
    )
    analisador.add_argument(
        "--regime", metavar="AAAA-MM",
        help="primeiro mes do orcamento atual; sobrepoe a deteccao automatica",
    )
    analisador.add_argument(
        "--hoje", metavar="AAAA-MM-DD",
        help="data de referencia; util para reproduzir um relatorio antigo",
    )
    return analisador.parse_args(argv)


def gravar_csv(caminho: Path, lancamentos: list[dict]) -> None:
    colunas = [
        "competencia", "descricao", "valor", "categoria", "subcategoria",
        "pessoa", "forma", "natureza", "origem", "observacao",
    ]
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(
            arquivo, fieldnames=colunas, extrasaction="ignore"
        )
        escritor.writeheader()
        escritor.writerows(lancamentos)


def principal(argv: list[str] | None = None) -> int:
    opcoes = argumentos(argv)
    hoje = (
        _dt.date.fromisoformat(opcoes.hoje) if opcoes.hoje else _dt.date.today()
    )

    base = carregar(opcoes.planilha, opcoes.texto, opcoes.fatura)
    payload = montar_payload(
        base, hoje, regime=opcoes.regime, confirmados=opcoes.confirmados
    )

    saida = Path(opcoes.saida)
    saida.mkdir(parents=True, exist_ok=True)

    gravar_csv(saida / "lancamentos.csv", payload["lancamentos"])
    (saida / "painel.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    painel = renderizar(payload, TEMPLATE, saida / "painel.html")

    print(f"{len(payload['lancamentos'])} lancamentos "
          f"em {len(payload['meses'])} meses")
    print(f"{len(payload['oportunidades'])} oportunidades mapeadas")
    if base.faturas:
        fecham = sum(1 for f in base.faturas if f.confere)
        print(f"{fecham}/{len(base.faturas)} faturas conferem com o total declarado")
        print(f"{len(base.parcelamentos)} parcelamentos em curso")
        if base.sobreposicoes:
            print(f"  {len(base.sobreposicoes)} possiveis duplicidades planilha/cartao")
    linha_base = payload["baseline"]
    print(f"piso mensal: R$ {linha_base['piso']:,.2f} "
          f"({len(linha_base['meses_regime'])} meses do regime atual)")
    if linha_base["pendentes"]:
        print(f"  {len(linha_base['pendentes'])} itens ainda sem valor")
    for aviso in payload["avisos"]:
        print(f"  aviso: {aviso}", file=sys.stderr)
    print(f"painel: {painel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(principal())
