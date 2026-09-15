# Convenções do Kit de Gestão para Advogados (obrigatórias para todo build_*.py)

Leia também `../revisao-interna-1.md` (erros que os revisores pegaram nos kits 1 e 2) e `../../02-oferta/advogados.md`.

1. **Helpers**: `from ssg import *` (cores, F, fill, hdr, inp, calc, kpi, lista, widths, como_usar, proteger, salvar) e
   `import dados`. `dados.py` é a FONTE ÚNICA do exemplo: escritório, pessoas, custos, clientes, 38 casos (com cronograma de
   parcelas), 20 propostas, agenda (PRAZOS), lançamentos do caixa (LANCAMENTOS, gerados das parcelas pagas), horas (HORAS),
   totais mensais (TOTAIS), estado da carteira em qualquer data (estado), histórico da 17 (HISTORICO), DRE (dre), provisão
   (provisao_10) e metas (metas_19). Nunca invente outro escritório, outros sócios, outros clientes ou outros números:
   tudo vem de `dados.py` para as 20 planilhas baterem entre si. Os números "de verdade" do exemplo estão em `NUMEROS.md`.
2. **Arquivo standalone**: sem links entre arquivos. Se precisar de dado de outra planilha, tenha uma aba de entrada
   amarela com exemplo preenchido a partir de `dados.py`.
3. **Abas**: "Como usar" (primeira, via `como_usar`), depois Painel/aba principal, depois Config e as abas de dados.
   Nomes amigáveis, sem abreviação. Painel congelado (freeze_panes) em tabelas longas.
4. **Células**: amarelas (`inp`) só onde o cliente digita; tudo o mais `calc` e protegido (`proteger(wb)`, sem senha).
   Nunca pinte de amarelo célula bloqueada. Listas suspensas (`lista`) em todo campo de escolha, apontando para
   intervalos SEM células vazias no meio: use `=OFFSET(Config!$B$5,0,0,MAX(1,COUNTA(Config!$B$5:$B$30)),1)` e
   a nota "preencha de cima para baixo, sem pular linha".
5. **Fórmulas**: só Excel 2007+ (SUMIFS, COUNTIFS, INDEX/MATCH, IFERROR, SUMPRODUCT), para abrir no Excel 2016 e no Google
   Sheets. Nada de MINIFS/MAXIFS/TEXTJOIN/IFS (nem com `_xlfn.`): mínimo/máximo condicional via
   `SUMPRODUCT(MIN(cond*x+(1-cond)*1E+10))` / `SUMPRODUCT(MAX(cond*x))`; concatenação condicional via coluna auxiliar oculta
   com `IF(...,item&"; ","")` e `LEFT(...,LEN-2)`. Nunca XLOOKUP/FILTER/SORT/UNIQUE. Ranking via coluna auxiliar de
   pontuação (oculta) + LARGE/MATCH/INDEX. Data vazia via `IF(x="","",x)`. Número dentro de texto: `FIXED(x,casas)`
   (separadores seguem o idioma do Excel), nunca `ROUND(x,2)&""` nem `TEXT(x,"#,##0")`.
   Formatos: `BRL`, `BRL0`, `DATA`, `PCT` do ssg; nunca formatar taxa como soma.
6. **Datas do exemplo**: prazos e "próxima ação" como fórmula relativa (`dados.prazo_formula(d)` = `=TODAY()+d`);
   histórico (abertura, lançamentos) fixo em 2026. Data de referência em Config = `=TODAY()`.
7. **Textos**: português do Brasil, direto, sem "você" acusatório. Nenhum conteúdo jurídico (peça, tese, prazo legal
   específico): o kit é gestão do escritório. Nunca prometer "nunca mais perder prazo": a planilha AVISA.
8. **Exemplo coerente**: HOJE = segunda 14/09/2026 (Config = `=TODAY()`); a sexta do painel é 11/09/2026 e nenhum lançamento
   pago (caixa, parcela, hora) tem data depois dela. 17 mostra setembro em andamento; 18 e 20 analisam agosto (último mês
   fechado); 16 fica em Setembro. Uma só definição de inadimplência (vencido ÷ (pago + vencido)), uma só hora mínima
   (05: R$ 106,57 → R$ 110; 08 mostra a "hora mínima com folga" de 20 %), alíquota única de 8 %. Parcela paga ⇔ entrada no
   caixa; recebido (13) = soma das parcelas pagas (14). Próxima ação coerente com a fase (dados.ACOES_POR_FASE); horas
   gastas ≤ 1,3× estimadas; recebido ≤ contratado; êxito só recebe ao fim. A 13 é a fonte do cadastro de casos: as abas
   de dados de 01, 02, 04, 08, 14 e 16 dizem isso.
9. **Cabeçalho da aba principal**: `titulo(ws, "Ferraz & Lima Advocacia (exemplo fictício) · <nome da aba> · <mês ou data>",
   "Nada para digitar aqui..." ou a instrução certa)`. Rodapé/nota com fonte `nota()`.
10. **Verificação obrigatória** antes de entregar: copiar o .xlsx para o scratchpad e rodar
    `python3 /root/.claude/skills/synced/196a43ae-ea62-4685-8684-e86dad1734fb_be351cae-a2b1-428f-a734-2c8f11d7ae5e/xlsx/scripts/recalc.py <copia> 240`
    → zero erros; ler a cópia com `data_only=True` e conferir 3 valores do painel à mão. Nunca recalcular o original.
    Depois, com as 20 cópias recalculadas na mesma pasta: `python3 verifica_coerencia.py <pasta>` (0 falhas) e
    `python3 cache_valores.py <pasta>` (grava só os valores calculados nos .xlsx originais, para a pré-visualização em
    celular/Drive não aparecer vazia; não use "abrir e salvar" no LibreOffice, que reescreve estilos, gráficos e colunas
    ocultas). Regerar `NUMEROS.md` com `python3 numeros.py <pasta>` e as telas com `cd .. && python3 telas.py advogados`.
11. **Nomes de arquivo**: `NN-nome-em-minusculas-com-hifens.xlsx`, gerados por `build_NN_nome.py` na pasta `kit-advogados/`
    (salvar em `kit-advogados/NN-....xlsx`; `entrega/` é montada depois pelo empacotador).
12. **Título do documento** (`salvar(wb, arquivo, "<Nome> · Kit de Gestão para Advogados")`).
