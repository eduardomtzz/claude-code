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

## Regras que saíram da auditoria externa de 18/09/2026

Seis classes de defeito, cada uma achada em mais de um arquivo. Valem para os quatro kits.

A. **Chave de ranking é INTEIRA.** Nunca somar duas grandezas decimais na mesma chave: valor/1E+6
   junto com ROW()/1E+5 colide sempre que a diferença de valor é dez vezes a diferença de linha
   (R$ 380,00 na linha 112 e R$ 379,99 na 113 davam a mesma chave, e o LARGE/MATCH devolvia a
   mesma venda duas vezes, escondendo a outra). Padrão: cada critério num bloco de casas próprio —
   `situação*1E+15 + MIN(dias,500)*1E+12 + MIN(ROUND(valor*100,0),99999999)*1E+4 + (ÚLTIMA_LINHA+1-ROW())`
   (a 16 dos Médicos não tem situação: `MIN(dias,500)*1E+12 + centavos*1E+4 + linha`). O valor
   entra em CENTAVOS: com ROUND(valor,0), R$ 379,99 numa linha anterior vencia R$ 380,00 na
   seguinte (rodada 4). Saturações, documentadas de propósito: dias acima de 500 empatam entre
   si (ordem então pelo valor), valor acima de R$ 999.999,99 idem (ordem então pela linha) e a
   linha vai até 9.999. Máximo da chave: 3 × 1E+15 + 5E+14 + 1E+12 + 1E+4 ≈ 3,5E+15, exato em
   ponto flutuante porque fica abaixo de 2^53 = 9.007.199.254.740.992.

B. **Número de exemplo nunca fica escrito dentro de texto.** Nota, "Como usar" e referência leem a
   célula: `"... "&FIXED($B$13,0)&" ..."`. Texto com número cravado envelhece na primeira regeração
   ("julho R$ 31.591" contra B14 = 34.409; "caixa livre R$ 26.062 e 2,1 meses" contra 12.003 e 0,8).
   E **FIXED, nunca TEXT com código de formato**: `TEXT(x,"R$ #,##0")` tem o código traduzido pelo
   idioma e devolve "R$ 29500,000" em pt-BR. TEXT só para data ("dd/mm/yyyy") e percentual ("0%").

C. **Nada de endereço de linha fixo em quem LÊ a planilha** (verifica_coerencia.py, numeros.py):
   achar pelo rótulo. Quando uma categoria saiu da receita da 18, a referência passou a dizer que a
   receita de agosto era "Outras entradas" e o total da proposta virou "None / R$ 0". Referência que
   contradiz a planilha é pior do que referência nenhuma: ela é o oráculo de quem confere o gerador.
   O mesmo vale dentro do gerador: seção com âncora fixa engole a seção anterior (a nota "A pagar"
   da 11 nunca chegou ao cliente, e três das dez vagas de "Por pessoa" da 16 eram sobrescritas).

D. **Regra condicional que aponta para outra aba vai embrulhada em INDIRECT**, feito pelo
   `salvar()` do ssg.py. O Google Sheets não aceita referência a outra aba em regra condicional;
   sem isso os semáforos que dependem do mês escolhido em Config param de acompanhar depois da
   importação. Eram 120 das 470 regras.

E. **Dado ausente não vira zero.** Custo mensal em branco não pode dar custo-hora zero (a hora
   trabalhada virava trabalho de graça e a margem do projeto subia); mês sem lançamento não fecha
   trimestre nem libera lucro; sem horas estimadas o simulador não classifica risco. Em todos os
   casos: pendência escrita na célula e aviso contado no painel.

F. **Lista suspensa bloqueante só onde o universo é fechado.** Paciente, serviço e outros campos de
   nome livre usam `strict=False`: a lista sugere. Bloquear impedia o cliente de redigitar o próprio
   exemplo (159 lançamentos da 09 dos Médicos, um serviço da 15 dos Advogados).
