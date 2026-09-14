# Convenções do Kit de Gestão para Advogados (obrigatórias para todo build_*.py)

Leia também `../revisao-interna-1.md` (erros que os revisores pegaram nos kits 1 e 2) e `../../02-oferta/advogados.md`.

1. **Helpers**: `from ssg import *` (cores, F, fill, hdr, inp, calc, kpi, lista, widths, como_usar, proteger, salvar) e
   `import dados` (ESCRITORIO, PESSOAS, CUSTOS_FIXOS, CLIENTES, CASOS, HOJE, prazo_formula). Nunca invente outro escritório,
   outros sócios ou outros clientes: tudo vem de `dados.py` para as 20 planilhas baterem entre si.
2. **Arquivo standalone**: sem links entre arquivos. Se precisar de dado de outra planilha, tenha uma aba de entrada
   amarela com exemplo preenchido a partir de `dados.py`.
3. **Abas**: "Como usar" (primeira, via `como_usar`), depois Painel/aba principal, depois Config e as abas de dados.
   Nomes amigáveis, sem abreviação. Painel congelado (freeze_panes) em tabelas longas.
4. **Células**: amarelas (`inp`) só onde o cliente digita; tudo o mais `calc` e protegido (`proteger(wb)`, sem senha).
   Nunca pinte de amarelo célula bloqueada. Listas suspensas (`lista`) em todo campo de escolha, apontando para
   intervalos SEM células vazias no meio: use `=OFFSET(Config!$B$5,0,0,MAX(1,COUNTA(Config!$B$5:$B$30)),1)` e
   a nota "preencha de cima para baixo, sem pular linha".
5. **Fórmulas**: só Excel 2007+ (SUMIFS, COUNTIFS, INDEX/MATCH, IFERROR, SUMPRODUCT). Pós-2007 com prefixo `_xlfn.`
   (`_xlfn.MINIFS`, `_xlfn.MAXIFS`, `_xlfn.TEXTJOIN`, `_xlfn.IFS`). Nunca XLOOKUP/FILTER/SORT/UNIQUE. Ranking via
   coluna auxiliar de pontuação + LARGE/MATCH/INDEX. Data vazia via `IF(x="","",x)`; MINIFS que dá 0 vira "".
   Formatos: `BRL`, `BRL0`, `DATA`, `PCT` do ssg; nunca formatar taxa como soma.
6. **Datas do exemplo**: prazos e "próxima ação" como fórmula relativa (`dados.prazo_formula(d)` = `=TODAY()+d`);
   histórico (abertura, lançamentos) fixo em 2026. Data de referência em Config = `=TODAY()`.
7. **Textos**: português do Brasil, direto, sem "você" acusatório. Nenhum conteúdo jurídico (peça, tese, prazo legal
   específico): o kit é gestão do escritório. Nunca prometer "nunca mais perder prazo": a planilha AVISA.
8. **Exemplo coerente**: painel de referência 14/09/2026; totais devem fazer sentido (ex.: horas gastas ≤ 1,3× estimadas;
   recebido ≤ contratado; êxito não recebe antes do fim).
9. **Cabeçalho da aba principal**: `titulo(ws, "Ferraz & Lima Advocacia (exemplo fictício) · <nome da aba> · <mês ou data>",
   "Nada para digitar aqui..." ou a instrução certa)`. Rodapé/nota com fonte `nota()`.
10. **Verificação obrigatória** antes de entregar: copiar o .xlsx para o scratchpad e rodar
    `python3 /root/.claude/skills/synced/196a43ae-ea62-4685-8684-e86dad1734fb_be351cae-a2b1-428f-a734-2c8f11d7ae5e/xlsx/scripts/recalc.py <copia> 240`
    → zero erros; ler a cópia com `data_only=True` e conferir 3 valores do painel à mão. Nunca recalcular o original.
11. **Nomes de arquivo**: `NN-nome-em-minusculas-com-hifens.xlsx`, gerados por `build_NN_nome.py` na pasta `kit-advogados/`
    (salvar em `kit-advogados/NN-....xlsx`; `entrega/` é montada depois pelo empacotador).
12. **Título do documento** (`salvar(wb, arquivo, "<Nome> · Kit de Gestão para Advogados")`).
