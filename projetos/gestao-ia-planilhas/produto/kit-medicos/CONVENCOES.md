# Convenções do Kit de Gestão para Médicos (obrigatórias para todo build_*.py)

Leia também `../revisao-interna-2.md` (Relatório A: os defeitos que os revisores pegaram no Kit Advogados) e `../../02-oferta/medicos.md`.

1. **Helpers**: `from ssg import *` (cores, F, fill, hdr, inp, calc, kpi, lista, widths, como_usar, proteger, salvar) e
   `import dados`. `dados.py` é a FONTE ÚNICA do exemplo: clínica (PESSOAS, TURNOS, SALAS, FERIADOS), custos fixos, convênios
   (prazo e glosa histórica), procedimentos (duração, material, retorno) e TABELA de preços por pagador, ~156 pacientes
   (PACIENTES), agenda gerada turno a turno (AGENDA_TODA de 05/01 a hoje + 21 dias; AGENDA = o que aparece na 01, desde 01/06 — junho entra
para o Histórico da 17 ter o mês anterior ao trimestre e a "partida" das metas da 19 ser reproduzível),
   parcelas a prazo (PARCELAS), guias e lotes de convênio (GUIAS, LOTES), orçamentos (ORCAMENTOS), lançamentos do caixa
   (LANCAMENTOS, gerados dos fechamentos do dia, parcelas pagas, lotes pagos e saídas), totais mensais (TOTAIS), estado em
   qualquer data (estado), histórico da 17 (HISTORICO), agenda por mês (resumo_agenda, faltas, lista_retorno), DRE (dre),
   provisão (provisao_10) e metas (metas_19). Nunca invente outra clínica, outros nomes ou outros números: tudo vem de
   `dados.py` para as 20 planilhas baterem entre si. Os números "de verdade" do exemplo estão em `NUMEROS.md`.
2. **Arquivo standalone**: sem links entre arquivos. Se precisar de dado de outra planilha, tenha uma aba de entrada
   amarela com exemplo preenchido a partir de `dados.py` (02 e 16 copiam a Agenda da 01; 14 copia Pacientes da 01; 13 · Guias
   vem dos atendimentos de convênio da 01; 09/10/11/12/18 copiam totais do Painel da 09; 17 copia os painéis de 01, 02, 09, 13,
   14 e 15; 20 copia o Histórico da 17 e a 18).
3. **Abas**: "Como usar" (primeira, via `como_usar`), depois Painel/aba principal, depois Config e as abas de dados
   (20: Como usar, Painel, Resumo, Config, Indicadores). Nomes amigáveis, sem abreviação. Painel congelado (freeze_panes) em
   tabelas longas.
4. **Células**: amarelas (`inp`) só onde o cliente digita; tudo o mais `calc` e protegido (`proteger(wb)`, sem senha).
   Nunca pinte de amarelo célula bloqueada. Listas suspensas (`lista`) em todo campo de escolha, apontando para
   intervalos SEM células vazias no meio: use `=OFFSET(Config!$B$5,0,0,MAX(1,COUNTA(Config!$B$5:$B$30)),1)` e
   a nota "preencha de cima para baixo, sem pular linha". Colunas auxiliares (chaves de ranking, concatenação) sempre ocultas.
5. **Fórmulas**: só Excel 2007+ (SUMIFS, COUNTIFS, INDEX/MATCH, IFERROR, SUMPRODUCT), para abrir no Excel 2016 e no Google
   Sheets. Nada de MINIFS/MAXIFS/TEXTJOIN/IFS (nem com `_xlfn.`): mínimo/máximo condicional via
   `SUMPRODUCT(MIN(cond*x+(1-cond)*1E+10))` / `SUMPRODUCT(MAX(cond*x))`; concatenação condicional via coluna auxiliar oculta
   com `IF(...,item&"; ","")` e `LEFT(...,LEN-2)`. Nunca XLOOKUP/FILTER/SORT/UNIQUE. Ranking via coluna auxiliar de
   pontuação (oculta) + LARGE/MATCH/INDEX. Data vazia via `IF(x="","",x)`. Nunca `OR(x="",y+z=0)` quando y pode ser "" (dá
   #VALUE!): aninhe os IFs. Nunca IF com matriz dentro de SUMPRODUCT (não é avaliado como matriz): use coluna auxiliar.
   Número dentro de texto: `FIXED(x,casas)` (separadores seguem o idioma do Excel), nunca `ROUND(x,2)&""` nem
   `TEXT(x,"#,##0")`. Formatos: `BRL`, `BRL0`, `DATA`, `PCT` do ssg; hora como `hh:mm` (valor de tempo, não texto);
   nunca formatar taxa como soma.
6. **Datas do exemplo**: TODAS literais, inclusive as futuras — `dados.prazo_formula(d)` devolve `HOJE+d` como data,
   não `=TODAY()+d`. Data de referência em Config = a data literal 14/09/2026, com a nota que manda trocar por
   `=HOJE()` ao começar a usar. Motivo: com `=TODAY()` o histórico ficava preso em setembro e só a parte futura
   andava, então a mesma empresa mostrava números diferentes conforme o dia em que o cliente abria o arquivo.
   Horas disponíveis da agenda só contam dias já passados (até ontem).
7. **Textos**: português do Brasil, direto, sem "você" acusatório. Nada clínico (diagnóstico, conduta, prontuário, código de
   procedimento, exame): "procedimento" é só o nome administrativo do atendimento; pacientes têm nome e contato fictícios e
   nada mais. Nunca prometer "lotar a agenda", captar pacientes ou resultado financeiro: a planilha AVISA e mede; a decisão é
   da clínica. Divulgação de preços e de serviços segue as regras do CFM (o kit lembra, não redige). Cobrança de paciente
   sem exposição ou constrangimento.
8. **Exemplo coerente**: HOJE = segunda 14/09/2026 (Config = data literal); a sexta do painel é 11/09/2026 e nenhum lançamento
   pago (caixa, parcela, lote) tem data depois dela; nada "Realizado" na agenda depois de 11/09 e nada "Agendado/Confirmado"
   antes de hoje. 17 mostra setembro em andamento (variação de agenda e caixa só quando Config diz que o mês fechou); 18 e 20
   analisam agosto (último mês fechado; 20 = agosto × julho); 16 fica em agosto; 08 usa o volume de agosto. Uma só definição
   de inadimplência (vencido ÷ (pago + vencido), só do que foi combinado a prazo); uma só glosa (glosa ÷ (pago + glosa) dos
   lotes pagos); uma só hora mínima (05: R$ 200 ÷ (1 − 0,30 − 0,11) = R$ 338,98 → R$ 340; 06/07/08 usam a mesma conta);
   custo cheio do procedimento = (minutos + 0,4 × 20 min de retorno nas consultas) ÷ 60 × custo-hora + material (06 = 07 =
   08); alíquota única de 11 % (efetiva, "combinada com o contador"); repasse 50 % da produção do mês, pago dia 10; custo do
   dinheiro 1,5 % ao mês (07). Parcela paga ⇔ entrada no caixa; lote pago ⇔ entrada no caixa (menos a glosa); recurso
   aceito ⇔ entrada "Recurso de glosa"; taxas de cartão do mês (16) ⇔ uma saída no fim do mês (09); repasse devido (11) =
   50 % da produção da parceira no Painel da 01. A 01 é a fonte da agenda e do cadastro de pacientes.
9. **Cabeçalho da aba principal**: `titulo(ws, "Clínica Vida Plena (exemplo fictício) · <nome da aba> · <mês ou data>",
   "Nada para digitar aqui..." ou a instrução certa)`. Rodapé/nota com fonte `nota()`.
10. **Verificação obrigatória** antes de entregar: copiar o .xlsx para o scratchpad e rodar
    `python3 /root/.claude/skills/synced/*/xlsx/scripts/recalc.py <copia> 300` → zero erros; ler a cópia com `data_only=True` e
    conferir 3 valores do painel contra `dados.py`. Nunca recalcular o original. Depois, com as 20 cópias recalculadas na
    mesma pasta: `python3 verifica_coerencia.py <pasta>` (0 falhas; hoje são 677 verificações) e
    `python3 cache_valores.py <pasta>` (grava só os valores calculados nos .xlsx originais, para a pré-visualização em
    celular/Drive não aparecer vazia; não use "abrir e salvar" no LibreOffice, que reescreve estilos, gráficos e colunas
    ocultas). Regerar `NUMEROS.md` com `python3 numeros.py <pasta>` (inclui a lista dos nomes de prompt citados) e as telas
    com `cd .. && python3 telas.py medicos`.
11. **Nomes de arquivo**: `NN-nome-em-minusculas-com-hifens.xlsx` exatamente como a tabela da oferta, gerados por
    `build_NN_nome.py` na pasta `kit-medicos/` (salvar em `kit-medicos/NN-....xlsx`; `entrega/` é montada depois pelo
    empacotador `../empacotar_medicos.py`).
12. **Título do documento** (`salvar(wb, arquivo, "<Nome> · Kit de Gestão para Médicos")`).
13. **Prompts citados** nos "Como usar" usam nomes provisórios no formato "Grupo NN · Título" (Agenda, Preço, Caixa,
    Recebíveis, Painel). A lista completa está no fim de `NUMEROS.md`: quem escrever a biblioteca de prompts usa exatamente
    esses nomes (ou troca aqui e regera as 20).

14. **Fonte única da tabela de preços**: a planilha **08** é onde o preço é decidido. A 06 (precificação), a 07 (simulador) e a
    Config da 01 (agenda) COPIAM de lá e dizem isso no texto. Ordem de atualização quando um preço muda: **08 → 06 → 07 → 01**.
    Procedimento novo: 01 e 02 (Config), 08, 06, 07. Convênio novo: 01, 02, 06, 07, 08, 09 (categorias) e 13 (Config).
15. **Capacidade das abas de lançamento** (dita no "Como usar" de cada planilha, com o jeito de estender ou de virar o ano):
    01 · Agenda 3.000 linhas (≈ 10 meses a 300 atendimentos/mês), 02 · Agenda 3.000 (cópia da 01), 09 · Lançamentos 1.500
    (≈ 80/mês, mais de um ano), 16 · Vendas 2.000 (≈ 100 pagamentos/mês), 13 · Guias 1.500 e Lotes 150, 14 · Parcelas 400,
    15 · Orçamentos 300, 04 · Checklist 300 dias, 01/14 · Pacientes 400.
16. **Regras de conteúdo fixadas na revisão** (valem para todo build e para o exemplo):
    - **A receber (09)** = parcelas (14) e lotes (13) com previsão de recebimento **até o fim do mês de referência**. A regra está
      escrita em `Lançamentos!A2` e na Config. Descrições de lançamento nunca trazem rótulo que envelhece ("(vencida)", "(a vencer)",
      "(atrasado)"): use a data ("· vence dd/mm", "· previsão dd/mm").
    - **Custo-hora (05)** = custo total ÷ horas de atendimento **planejadas** (turnos × 4,33 semanas). É essa base que 06, 07 e 08
      usam. As horas realmente atendidas aparecem só na sensibilidade da 05 (última linha: agosto da 01), com nota no Painel.
    - **"Tabela de convênio abaixo do custo cheio + imposto"** é a ÚNICA definição (margem negativa depois dos 11 %), com esse
      rótulo e o mesmo número na 06 (Resumo) e na 08 (KPI e coluna).
    - **Margem da parceria (11)** = o que fica com a clínica − material e insumo do parceiro. O custo indireto por hora (05) entra
      só como informação: a estrutura já está dentro do custo-hora dos sócios e não pode ser cobrada duas vezes.
    - **18** tem linha de **provisão de 13º e férias** (da 10) antes do resultado, e **reembolsos de sócios** (a categoria "Outras
      entradas" da 09) numa linha própria, fora da receita e fora da base do imposto — a mesma base da 10 e da 11.
    - **Crédito**: o exemplo nunca combina pagamento a prazo (14) nem orçamento aprovado a prazo (15) com paciente que tem parcela
      vencida em aberto; nesse dia o atendimento é à vista.
    - **Orçamentos (15)**: a data da decisão é sempre ≥ a da apresentação, e nenhuma das duas fica no futuro; orçamento ligado a
      agendamento futuro fica "Aprovado" com as duas datas no passado e o agendamento na observação.
    - **Rotina da semana (03)**: 12 minutos na segunda (01: 4 · confirmação: 4 · 02: 4) e 18 na sexta (09 conferir: 5 · 14: 4 ·
      13: 3 · 15: 3 · 17: 3). A recepção lança o fechamento do dia na 09 todo dia (04); na sexta a sócia CONFERE. 12, 16 e 19 são
      mensais/quinzenais e dizem isso; a 04 é o roteiro diário da recepção (3 + 10 min), fora dos 30 minutos dos sócios.
    - **Meta de provisão (12 e 19)** = saldo provisionado do último mês **fechado** (agosto), não o do mês em andamento.
    - "Custo fixo" na 12 é **custo fixo + pró-labore** e o rótulo diz isso (nas 05, 09 e 18, "custo fixo" é só a estrutura).

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

## Cronograma monetário único do cartão (rodada 5 da auditoria)

Uma venda no cartão tem UM cronograma de liquidações, compartilhado por `dados.py` (caixa 09) e
pela 16: o bruto de cada parcela é `ROUND(bruto/n;2)` e a última leva a diferença; a taxa de
cada parcela é `ROUND(taxa/n;2)` e a última leva a diferença; o líquido da parcela é bruto − taxa.
Assim `bruto = líquido + taxa` fecha em CADA liquidação, não só no total (arredondar líquido e
taxa separadamente dava 216,23 + 8,78 = 225,01 numa parcela de 225,00). A 16 lista toda venda
com alguma liquidação a partir do início do controle (01/06), inclusive as de abril e maio: o mês
selecionado no Painel tem todas as liquidações e a taxa do mês (N5) é a saída do caixa. O
`verifica_coerencia.py` cobra as duas coisas (identidade por liquidação e taxa/bruto por mês).
