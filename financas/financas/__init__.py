"""Pipeline de categorizacao dos pagamentos da casa.

O caminho normal e pela linha de comando::

    python3 -m financas.cli planilha.xlsx --texto dados/setembro-2026.txt

Para usar como biblioteca, :func:`financas.consolidacao.carregar` devolve a base
ja lida e classificada, e :func:`financas.analise.analisar` produz as series
mensais e as oportunidades.
"""

__all__ = [
    "analise", "cli", "consolidacao", "modelo", "painel", "planilha",
    "regras", "texto", "xlsx",
]
