# Dicionário de 60 fórmulas · Kit IA no Trabalho · Completo

Versão 1.0 · setembro de 2026 · Seu Sócio Gestor

Cada fórmula em uma frase, com o nome em português (Excel) e em inglês (Google Sheets e Excel em
inglês) e um exemplo pronto. No Brasil, as duas ferramentas usam ponto e vírgula para separar os
argumentos. Onde aparece `A5:A500`, é o intervalo da sua base.

## Somar, contar e média (12)

| # | Português | Inglês | O que faz | Exemplo |
|---|---|---|---|---|
| 1 | SOMA | SUM | Soma um intervalo | `=SOMA(E5:E500)` |
| 2 | SOMASE | SUMIF | Soma quando uma condição é verdadeira | `=SOMASE(B5:B500;"Despesa";E5:E500)` |
| 3 | SOMASES | SUMIFS | Soma com várias condições (a mais usada do kit) | `=SOMASES(E5:E500;B5:B500;"Despesa";I5:I500;9)` |
| 4 | CONT.VALORES | COUNTA | Conta células preenchidas | `=CONT.VALORES(B5:B500)` |
| 5 | CONT.NÚM | COUNT | Conta células com número | `=CONT.NÚM(E5:E500)` |
| 6 | CONT.SE | COUNTIF | Conta quando uma condição é verdadeira | `=CONT.SE(G5:G500;"Atrasada")` |
| 7 | CONT.SES | COUNTIFS | Conta com várias condições | `=CONT.SES(C5:C500;"Ana";G5:G500;"Atrasada")` |
| 8 | MÉDIA | AVERAGE | Média simples | `=MÉDIA(E5:E500)` |
| 9 | MÉDIASES | AVERAGEIFS | Média com condições | `=MÉDIASES(F5:F300;A5:A300;"Site novo")` |
| 10 | MÍNIMO / MÁXIMO | MIN / MAX | Menor e maior valor | `=MÁXIMO(E5:E500)` |
| 11 | MÍNIMOSES / MÁXIMOSES | MINIFS / MAXIFS | Menor ou maior com condições (Excel 2019+) | `=MÍNIMOSES(E5:E300;C5:C300;"Ana";G5:G300;"<>Concluída")` |
| 12 | SOMARPRODUTO | SUMPRODUCT | Multiplica e soma; serve para contar com lógica complexa | `=SOMARPRODUTO((B5:B500="Despesa")*(E5:E500>1000))` |

## Lógica e erros (8)

| # | Português | Inglês | O que faz | Exemplo |
|---|---|---|---|---|
| 13 | SE | IF | Se a condição for verdadeira, faz uma coisa; senão, outra | `=SE(E5<HOJE();"Atrasada";"No prazo")` |
| 14 | SES | IFS | Vários SE em sequência, sem aninhar (Excel 2019+) | `=SES(H5>=1;"Atingido";H5>=0,7;"No ritmo";VERDADEIRO;"Em risco")` |
| 15 | E | AND | Verdadeiro só se todas as condições forem | `=SE(E(F5<1;E5<HOJE());"Atrasada";"")` |
| 16 | OU | OR | Verdadeiro se qualquer condição for | `=SE(OU(F5="Ganha";F5="Perdida");"Fechada";"Aberta")` |
| 17 | NÃO | NOT | Inverte verdadeiro e falso | `=NÃO(ÉCÉL.VAZIA(A5))` |
| 18 | SEERRO | IFERROR | Se der erro, mostra o que você mandar | `=SEERRO(PROCV(B5;Tabela;2;0);"não encontrado")` |
| 19 | ÉCÉL.VAZIA | ISBLANK | Verdadeiro se a célula está vazia | `=SE(ÉCÉL.VAZIA(A5);"";MÊS(A5))` |
| 20 | ÉNÚM / ÉTEXTO | ISNUMBER / ISTEXT | Testa se é número ou texto | `=ÉNÚM(E5)` |

## Buscar e referenciar (8)

| # | Português | Inglês | O que faz | Exemplo |
|---|---|---|---|---|
| 21 | PROCV | VLOOKUP | Busca um valor na primeira coluna e devolve outra coluna | `=PROCV(B5;Config!$A$11:$D$20;4;0)` |
| 22 | PROCH | HLOOKUP | O mesmo, na horizontal | `=PROCH("Set";Previsto!$B$4:$M$25;3;0)` |
| 23 | ÍNDICE | INDEX | Devolve a célula de uma posição | `=ÍNDICE(B5:B300;7)` |
| 24 | CORRESP | MATCH | Devolve a posição de um valor | `=CORRESP("Setembro";H5:H16;0)` |
| 25 | ÍNDICE + CORRESP | INDEX + MATCH | Busca em qualquer direção (o par preferido do kit) | `=ÍNDICE(Config!$D$11:$D$20;CORRESP(B5;Config!$A$11:$A$20;0))` |
| 26 | PROCX | XLOOKUP | Busca moderna, com "se não achar" embutido (Excel 365 e Sheets) | `=PROCX(B5;Config!A11:A20;Config!D11:D20;"não encontrado")` |
| 27 | DESLOC | OFFSET | Intervalo deslocado a partir de uma célula (use com cuidado) | `=SOMA(DESLOC(B5;0;0;10;1))` |
| 28 | INDIRETO | INDIRECT | Transforma texto em referência (evite em planilha grande) | `=INDIRETO("Previsto!B"&LIN())` |

## Datas e horas (10)

| # | Português | Inglês | O que faz | Exemplo |
|---|---|---|---|---|
| 29 | HOJE | TODAY | Data de hoje | `=HOJE()` |
| 30 | AGORA | NOW | Data e hora de agora | `=AGORA()` |
| 31 | DATA | DATE | Monta uma data a partir de ano, mês e dia | `=DATA(2026;9;30)` |
| 32 | DIA / MÊS / ANO | DAY / MONTH / YEAR | Extrai a parte da data | `=MÊS(A5)` |
| 33 | FIMMÊS | EOMONTH | Último dia do mês (0 = mesmo mês; -1 = anterior) | `=FIMMÊS(A5;0)` |
| 34 | DIATRABALHOTOTAL | NETWORKDAYS | Dias úteis entre duas datas, descontando feriados | `=DIATRABALHOTOTAL(D5;E5;Config!$H$5:$H$20)` |
| 35 | DIATRABALHO | WORKDAY | Data após N dias úteis | `=DIATRABALHO(A5;10)` |
| 36 | DATADIF | DATEDIF | Diferença entre datas em dias, meses ou anos | `=DATADIF(A5;HOJE();"Y")` |
| 37 | DIA.DA.SEMANA | WEEKDAY | Número do dia da semana (com 2, segunda = 1) | `=DIA.DA.SEMANA(A5;2)` |
| 38 | TEXTO | TEXT | Formata número ou data como texto | `=TEXTO(A5;"dd/mm/yyyy")` · `=TEXTO(E5;"R$ #.##0")` |

## Texto (10)

| # | Português | Inglês | O que faz | Exemplo |
|---|---|---|---|---|
| 39 | CONCAT / & | CONCAT / & | Junta textos | `=B5&" · "&C5` |
| 40 | UNIRTEXTO | TEXTJOIN | Junta com separador, ignorando vazios | `=UNIRTEXTO(" | ";VERDADEIRO;B5:B20)` |
| 41 | ESQUERDA / DIREITA | LEFT / RIGHT | Primeiros ou últimos caracteres | `=ESQUERDA(A5;4)` |
| 42 | EXT.TEXTO | MID | Pedaço do meio | `=EXT.TEXTO(A5;3;5)` |
| 43 | NÚM.CARACT | LEN | Quantidade de caracteres | `=NÚM.CARACT(A5)` |
| 44 | LOCALIZAR / PROCURAR | SEARCH / FIND | Posição de um texto dentro de outro | `=LOCALIZAR("-";A5)` |
| 45 | ARRUMAR | TRIM | Remove espaços extras | `=ARRUMAR(A5)` |
| 46 | MAIÚSCULA / MINÚSCULA / PRI.MAIÚSCULA | UPPER / LOWER / PROPER | Muda caixa | `=PRI.MAIÚSCULA(A5)` |
| 47 | SUBSTITUIR | SUBSTITUTE | Troca um texto por outro | `=SUBSTITUIR(A5;"R$";"")` |
| 48 | VALOR | VALUE | Texto que parece número vira número | `=VALOR(SUBSTITUIR(A5;".";""))` |

## Arredondar e classificar (6)

| # | Português | Inglês | O que faz | Exemplo |
|---|---|---|---|---|
| 49 | ARRED | ROUND | Arredonda com N casas | `=ARRED(E5/3;2)` |
| 50 | ARREDONDAR.PARA.<wbr>CIMA / BAIXO | ROUNDUP / ROUNDDOWN | Arredonda sempre para cima ou para baixo | `=ARREDONDAR.PARA.CIMA(E5;0)` |
| 51 | INT | INT | Parte inteira | `=INT((HOJE()-B6)/7)` |
| 52 | MOD | MOD | Resto da divisão | `=MOD(LIN();2)` |
| 53 | MAIOR / MENOR | LARGE / SMALL | N-ésimo maior ou menor (usado no ranking do kit) | `=MAIOR(M5:M300;1)` |
| 54 | ORDEM.EQ | RANK.EQ | Posição de um valor no ranking | `=ORDEM.EQ(E5;E$5:E$50)` |

## Utilidades (6)

| # | Português | Inglês | O que faz | Exemplo |
|---|---|---|---|---|
| 55 | LIN / COL | ROW / COLUMN | Número da linha ou coluna atual | `=LIN()-4` |
| 56 | REPT | REPT | Repete um texto N vezes (as barras do kit) | `=REPT("█";ARRED(C5*30;0))` |
| 57 | ESCOLHER | CHOOSE | Escolhe pelo número | `=ESCOLHER(2;"Baixa";"Média";"Alta")` |
| 58 | TRANSPOR | TRANSPOSE | Linhas viram colunas | `=TRANSPOR(A5:A16)` |
| 59 | HIPERLINK | HYPERLINK | Link clicável | `=HIPERLINK("#Painel!A1";"Ir ao painel")` |
| 60 | ÚNICO / FILTRO / CLASSIFICAR | UNIQUE / FILTER / SORT | Listas dinâmicas sem repetição, filtradas, ordenadas (Excel 365 e Sheets) | `=ÚNICO(C5:C500)` |

## Três hábitos que evitam 80% dos erros

1. **$ antes de copiar.** Se a fórmula vai ser copiada e uma parte não pode mudar, trave com `$`
   (`$B$7`). Aperte F4 no Excel para alternar.
2. **Nunca some um intervalo com total no meio.** O total entra duas vezes. Totais ficam fora da base.
3. **Teste com um caso que você sabe de cabeça.** Uma célula, um número conhecido, antes de
   copiar para 500 linhas.

Suporte: suporte@seusociogestor.com.br · Reembolso em até 7 dias.
