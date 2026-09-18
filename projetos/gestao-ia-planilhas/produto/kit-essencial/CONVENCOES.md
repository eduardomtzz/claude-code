# Convenções do Kit IA no Trabalho Essencial (obrigatórias para todo build_*.py)

Este kit veio antes dos outros três e por isso não usa `ssg.py` nem um `dados.py` único: cada
`build_*.py` é autossuficiente e traz as suas próprias constantes de cor e helpers (`F`, `fill`,
`hdr`, `inp`, `calc`). Não vale a pena refatorar agora — vale registrar as regras, porque as duas
últimas correções nasceram justamente de regra não escrita.

Leia também `../revisao-interna-1.md`, `../auditoria/triagem-2026-09-17.md` e `../../02-oferta/kit-essencial.md`.

1. **Três arquivos, três painéis**: `01-semana-organizada.xlsx` (tarefas e prazos),
   `02-relatorio-mensal-pronto.xlsx` (12 indicadores por mês) e `03-ganhos-e-gastos.xlsx`
   (entradas e saídas). Cada um é standalone: nenhum link entre arquivos.
2. **Abas**: "Como usar" primeiro, depois o painel de leitura, depois Config, depois as abas de
   digitação. Painel com `freeze_panes` e `showGridLines=False`.
3. **Células**: `AMARELO="FFF4CC"` com `Protection(locked=False)` só onde o cliente digita; todo o
   resto bloqueado por `ws.protection.sheet=True`, sem senha. Nunca pintar de amarelo célula
   bloqueada, nunca deixar desbloqueada célula com fórmula. Em célula de entrada não se põe
   fórmula: a primeira digitação a apagaria (foi o caso do B18 da 02, que virou valor literal).
4. **Fórmulas**: só Excel 2007+ (SUMIFS, COUNTIFS, INDEX/MATCH, IFERROR, SUMPRODUCT, LARGE,
   REPT, CHOOSE), para abrir no Excel 2016 e no Google Sheets. Proibido mesmo com `_xlfn.`:
   MINIFS, MAXIFS, TEXTJOIN, IFS, SWITCH, CONCAT, XLOOKUP, FILTER, SORT, UNIQUE, SEQUENCE.
   Mínimo/máximo condicional via `SUMPRODUCT(MIN(cond*x+(1-cond)*1E+10))` /
   `SUMPRODUCT(MAX(cond*x))`. Ranking via coluna auxiliar de pontuação oculta + LARGE/MATCH/INDEX.
5. **Listas suspensas** com `showErrorMessage=True` (recusa o que está fora da lista) e apontando
   para intervalo sem vazio no meio: `=OFFSET(Config!$B$9,0,0,MAX(1,COUNTA(Config!$B$9:$B$16)),1)`,
   com a nota "preencha de cima para baixo, sem pular linha".
6. **Datas do exemplo da 01**: relativas, `=TODAY()+k`, com Config!B4 = `=TODAY()`. É a única
   exceção do catálogo inteiro (os outros três kits congelam o exemplo numa data literal) e é
   deliberada: a 01 é um painel do dia, não tem número de mês para fechar com outro arquivo, e o
   cliente que abre em novembro tem de ver "2 atrasadas, 1 para hoje, 9 nesta semana" — não um
   exemplo de setembro todo vermelho. O deslocamento das 20 tarefas reproduz essa distribuição em
   qualquer dia. As 02 e 03 não têm data relativa: usam mês escolhido em Config.
7. **Dois exemplos diferentes, de propósito**: a 01 e a 02 usam a Prisma Comunicação (agência
   fictícia); a 03 usa a Rafa Design (designer autônoma). A 03 serve também para dinheiro pessoal
   e para negócio de uma pessoa só, então o exemplo é de uma pessoa. O "Como usar" das duas
   explica isso — sem essa frase parece descuido.
8. **A 03 é painel de CAIXA**: todo número do painel filtra `Pago? = "Sim"`, sem exceção — KPIs,
   tabela "Para onde foi o dinheiro", "De onde veio", média de 3 meses, reserva e o bloco do ano.
   O que falta pagar ou receber aparece só nos quadros "A pagar (não pago)" e "A receber (não
   recebido)". Foi meia regra que criou o defeito de 18/09: o KPI dizia R$ 4.173,90 e o total logo
   abaixo, R$ 4.535,90, com a coluna "% do total" somando 108,7 %.
9. **Acumulado da 02 depende do indicador**: coluna "Como acumular" (Soma ou Média, lista
   obrigatória). Soma para o que se empilha (receita, despesa, quantidade, horas); Média para
   razão (ticket médio, custo por lead, taxa, nota). Somar razão não significa nada: doze meses de
   ticket médio somados davam R$ 80.700 de "ticket do ano".
10. **NA() é proposital** nas linhas auxiliares do gráfico da 02 (fonte branca, abaixo do
    gráfico): mês sem valor vira `#N/D` para o Excel deixar o vão em vez de puxar a linha a zero.
    Não é erro — `../recalc_todos.py` sabe disso e não conta.
11. **Verificação obrigatória** antes de entregar, na ordem:
    ```
    python3 build_semana.py && python3 build_relatorio.py && python3 build_ganhos.py
    # copiar os três .xlsx para uma pasta de trabalho e recalcular no LibreOffice em perfil pt-BR
    soffice --headless -env:UserInstallation=file://<perfil> --convert-to xlsx --outdir <pasta>/calc <pasta>/*.xlsx
    python3 cache_valores.py <pasta>/calc     # grava só os <v>; nunca "abrir e salvar" no LibreOffice
    python3 verifica_coerencia.py <pasta>/calc  # 0 falhas
    cd .. && python3 recalc_todos.py            # 0 erros de fórmula nos quatro kits
    ```
    `verifica_coerencia.py` recalcula em Python todo número do painel a partir das linhas
    digitadas. Quando mudar a estrutura de um painel, ajuste as linhas de referência dele —
    verificação que aponta para a linha errada passa calada, que é pior do que não existir.
