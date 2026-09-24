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
6. **Datas do exemplo**: TODAS literais, inclusive as futuras — `dados.prazo_formula(d)` devolve `HOJE+d` como data,
   não `=TODAY()+d`. Data de referência em Config = a data literal 14/09/2026, com a nota que manda trocar por
   `=HOJE()` ao começar a usar. Motivo: com `=TODAY()` o histórico ficava preso em setembro e só a parte futura
   andava, então a mesma empresa mostrava números diferentes conforme o dia em que o cliente abria o arquivo.
   Única exceção do kit: a data da proposta na 07, que é `=HOJE()` de propósito — uma proposta leva a data do dia
   em que você a envia.
7. **Textos**: português do Brasil, direto, sem "você" acusatório. Nenhum conteúdo jurídico (peça, tese, prazo legal
   específico): o kit é gestão do escritório. Nunca prometer "nunca mais perder prazo": a planilha AVISA.
8. **Exemplo coerente**: HOJE = segunda 14/09/2026 (Config = data literal); a sexta do painel é 11/09/2026 e nenhum lançamento
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
   idioma e devolve "R$ 29500,000" em pt-BR. TEXT só com código de DÍGITO ("0", "00", "000", "0%"),
   que é igual em qualquer idioma. Data em texto é montada com
   `TEXT(DAY(x),"00")&"/"&TEXT(MONTH(x),"00")&"/"&YEAR(x)` e chave de competência com
   `YEAR(x)&"-"&TEXT(MONTH(x),"00")`: os códigos "dd/mm/yyyy" e "yyyy-mm" passam no LibreOffice e no
   Sheets, mas o Excel em português espera "aaaa" — nunca ficou provado que "yyyy" funciona lá
   (auditoria final, L01).

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
   trimestre nem libera lucro; sem horas estimadas o simulador não classifica risco; pró-labore,
   horas ou custo-hora em branco nas 05 e 06 suspendem custo, preço, margem e risco com "cadastro
   incompleto" / "falta o custo-hora"; data em branco não é atraso nem "próximo agendado = 0"; meta,
   partida, atual ou sentido em branco viram "Faltam dados". Em todos os casos: pendência escrita
   na célula e aviso contado no painel. E **parâmetro impossível não vira número**: imposto + margem
   em 100 % ou mais dá "margens inválidas (Config)", nunca preço negativo (validação + guarda).

F. **Lista suspensa bloqueante só onde o universo é fechado.** Paciente, serviço e outros campos de
   nome livre usam `strict=False`: a lista sugere. Bloquear impedia o cliente de redigitar o próprio
   exemplo (159 lançamentos da 09 dos Médicos, um serviço da 15 dos Advogados).

## Configuração de preço: um predicado só (auditoria final-2)

Impostos, margens e folga valem por um predicado único, escrito uma vez na Config e consultado
por TODA saída de preço: "Margem e impostos conferem?" (05), "Impostos e margem(ns) conferem?"
(06 e 08 dos Médicos) ou dentro da hora mínima (08 dos Advogados, 07 dos Médicos). O predicado
repete as condições da validação de digitação (cada percentual de 0 % a 99 %, mínima ≤ alvo,
impostos + margem abaixo de 100 %, folga ≥ 0) e começa por ISNUMBER, para texto, branco e colagem
não virarem #VALUE! nem número. Proibido guardar só o denominador (`1 − impostos − margem ≤ 0`):
margem negativa passa por essa guarda. Com o predicado em "Não", preço, margem, situação, risco,
resumo e totais dizem "margens inválidas (Config)"; com o custo-hora em branco, dizem "falta o
custo-hora". Subtotal e contagem que dependem dessas linhas também: SUM, COUNTIF e MIN ignoram texto
e devolveriam zero como se fosse resultado apurado. Zero digitado continua zero.

## Zero legítimo não é denominador (auditoria final-3)

Custo-hora, percentual de êxito, valor em discussão e hora mínima podem ser zero de verdade. Nenhuma
classificação divide por eles: a desigualdade é multiplicada pelo denominador (`sobra ≥ custo-hora ×
horas × (1 + folga)` em vez de `sobra ÷ custo-hora ÷ horas − 1 ≥ folga`). Comparação percentual
contra uma base zero diz "sem base (mínimo zero)"; nunca #DIV/0!, nunca 0 % por IFERROR, e nunca
IFERROR convertendo erro em "Alto". Parâmetro de regra (chance mínima, folgas) tem a sua conferência
("Regras de risco conferem?" na 06 dos Advogados) e suspende só as modalidades que o usam, mais a
recomendação. Validação customizada começa por `IF(ISNUMBER(x);AND(...);FALSE)`: texto dá FALSE,
não erro. Nota ao lado de entrada não formata a entrada: o exemplo vai escrito.

## Dado obrigatório e totais sobre a mesma população (auditoria final-4)

Todo número que entra numa conta de preço, custo ou classificação é conferido antes, com
`ISNUMBER` e domínio: minutos, retorno, material, prazo, glosa, custo do dinheiro, valor em
discussão, chance, valores das modalidades, horas, despesas, custo fixo e marcações Sim/Não da
equipe. Vazio ou texto não é zero: a linha diz qual dado falta ("faltam os minutos", "falta a
glosa", "falta a hora cobrada"), só os resultados que dependem dele são suspensos, e a
recomendação ou o resumo que dependeriam da linha também. Zero digitado continua valendo onde o
domínio aceita. Lookup na Config (`INDEX`) passa por `ISNUMBER(INDEX(...))`, porque célula vazia
devolvida por INDEX vira 0 numa conta. Totais e médias somam a MESMA população: pagador com
atendimentos e sem líquido suspende o líquido e o resultado do mês; receita por hora exige volume,
produção e minutos em todas as linhas com dados. Contagens de resumo ("x de N") só com todas as
linhas completas.

## Domínio, resíduo e decisões de "em branco" (auditoria final-5)

Dinheiro, horas, minutos, quantidades e percentuais de entrada são números ≥ 0 (horas faturáveis e
planejadas > 0; múltiplo de arredondamento e duração da consulta > 0; queda da sensibilidade de 0 a
99 %). Negativo é tratado como texto: avisa e suspende o que depende dele. Linha sem nome mas com
dado (resíduo) conta como incompleta em todos os agregados da aba. Decisões de produto em que o
branco significa "não se aplica", e por isso muda o total sem aviso: preço de convênio em branco na
06 e na 08 dos Médicos (convênio não atende o procedimento); valor de tabela em branco na 07 (o
pagador não atende); atendimentos em branco no mix da 07 (sem volume no mês). Renomear uma área na
Config da 08 dos Advogados deixa os casos dela fora da lista: os cartões gerais avisam caso
incompleto. A varredura automática de entradas (vazio, texto e −1 em cada célula de entrada do
exemplo, três linhas por coluna) roda depois de cada mudança e tem de terminar com zero mudança
silenciosa fora dessas decisões.

## Custo-hora, zero legítimo e faixas (auditoria final-6)

O custo-hora é conferido como `ISNUMBER(custo-hora)` e custo-hora ≥ 0 em todos os consumidores
(custo das horas, preço mínimo, comparação e recomendação), e a célula de entrada tem validação
"número ≥ 0". Custo-hora zero continua valendo. Linha ativa é qualquer linha com algum campo
preenchido, não só a que tem nome: "falta o nome" aparece na linha e os avisos do Painel contam
o resíduo. Total bruto de despesas não soma por cima de despesa ativa sem valor, com texto ou
negativa (mostra "despesa incompleta"); a resposta de reembolso só é exigida para o custo absorvido.
Na tabela de referência (08), horas típicas "de" maior que "até" é faixa invertida: mínimo e
máximo avisam, o ponto médio fica vazio e a instrução pede a correção. A varredura automática testa
todas as células de entrada preenchidas (não mais três por coluna) e também acusa célula calculada
que passa de vazia a número.

## Coerência entre campos (auditoria final-7)

Horas faturáveis são parte das horas de trabalho: com as duas preenchidas e faturáveis maiores, a linha
diz "faturáveis acima das horas de trabalho", a ocupação não é publicada e o Painel mostra "cadastro
incompleto". Faturáveis iguais às de trabalho (100 %) valem. A varredura passou a testar também zero e
valor ×10 em cada entrada numérica e confere regras de negócio fora da planilha (ocupação ≤ 100 %,
mínimo ≤ máximo, prejuízo do convênio recalculado).
