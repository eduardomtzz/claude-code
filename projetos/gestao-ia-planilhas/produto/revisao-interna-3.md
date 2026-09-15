# Revisão interna 3 · Kit de Gestão para Médicos (14 e 15/09/2026)

Três revisores independentes (agentes Claude) abriram a entrega como cliente, sem alterar nada: A (planilhas 01–20),
B (documentos 21–29 e LEIA-ME), C (página, copy, oferta, e-mails e obrigado). Este arquivo guarda os três relatórios
na íntegra e a triagem. Foram 76 achados; todos tratados nesta rodada, exceto os marcados como adiados.

Leitura rápida: as fórmulas estavam certas desde o começo (56.472 fórmulas, 0 erros), mas o exemplo da Clínica Vida
Plena tinha furos de coerência (tabela de preços sem cabeçalho, orçamento aprovado antes de apresentado, agenda que
acabava em quatro meses, DRE sem provisão, repasse cobrando a estrutura duas vezes), os documentos citavam um prompt
que não existia e mandavam ao contador planilha com nome de paciente, e a página trazia uma afirmação falsa ("a tela
real das vinte está nesta página") e as durações das aulas ainda como marcador.

## Triagem e correções

| Achado | Decisão | Feito |
|---|---|---|
| A-1 a A-25 (planilhas) | Aceito | Sim: `dados.py` continua fonte única; 677 verificações de coerência OK |
| A-5 (custo-hora ÷ horas atendidas) | Adaptado | Base segue nas horas planejadas, com rótulo explícito; a oferta e a página passaram a dizer "horas de atendimento" |
| B-G1 a B-G3, B-M1 a B-M11, B-L1 a B-L13 (documentos) | Aceito | Sim: prompt "Caixa 03" criado (41 prompts, o grupo Caixa tem 9), anexo do contador só com totais, ECG 10 de 18 |
| B-M10 (marca no slide mestre) | Adaptado | pptxgenjs desenha no layout, não no mestre: o texto passou a dizer "apague nos dois layouts" |
| C-G1 (atendimento condicionado a pagamento) | Aceito | Sim: a planilha 14 agora separa parcelamento de atendimento |
| C-G2 (tela das vinte) | Aceito | Sim, nas páginas /medicos e /advogados |
| C-G3 (durações marcador) | Aceito | Sim: medidas por ffprobe depois da regravação (2:47 a 2:55) |
| C-G4 (anúncios com "quarenta prompts") | Aceito | Sim: carrossel, vídeo de venda e de 15 s regravados com 41 |
| C-M5 (formato en-US no cache) | Aceito | Sim: planilhas 12, 14 e 20 recalculadas em pt-BR antes de empacotar |
| C-M6 (Caixa com 9 prompts) | Adaptado | Mantido 41, com a explicação na biblioteca, no LEIA-ME, na página e na oferta |
| C-M7 a C-M15, C-L16 a C-L23 | Aceito | Sim |
| C-M12 (imagens defasadas das planilhas) | Adaptado | `heroi_poster.py` virou script do repositório; a regeneração entra no roteiro de publicação |
| C-L20 (títulos internos em caixa-alta nas planilhas 17–20) | Adiado | Cosmético; entra na próxima revisão de convenções |
| C-L24 (segunda com zero na tela do inventário) | Adiado | O exemplo está certo (feriado + dia corrente) e a planilha explica em nota |
| C-L26 ("gráficos funcionam" no Como usar da 20) | Adiado | Frase é do texto comum das 20; muda junto com a próxima revisão do `ssg.py` |
| Teste em Excel e Google Sheets reais | Adiado | Eduardo |
| Narração definitiva | Adiado | Depende da chave do Google TTS |


## Relatório A · planilhas 01–20

Revisor A · 14/09/2026 · Cópias recalculadas em `scratchpad/revMA/recalc/` (originais de `produto/kit-medicos/entrega/` intactos).
Método: recalc com LibreOffice (`recalc.py <cópia> 300`), leitura com openpyxl em dois modos (fórmulas e `data_only`),
recálculo manual de 2–3 números por painel, cruzamento de pessoas/convênios/procedimentos/pacientes/valores entre os 20
arquivos contra `dados.py` e `NUMEROS.md`, checagem de amarelo × bloqueio, listas suspensas, funções, textos, e das
promessas de `site/src/pages/medicos.html` e `02-oferta/medicos.md`. Leitura feita como médico dono de clínica pequena
sem aula de gestão e como contador de PJ médica.

### Testes feitos

| Arquivo | Fórmulas | Erros (#N/A, #REF!, #DIV/0!, #VALUE!, #NAME?) |
|---|---|---|
| 01-agenda-e-ocupacao | 10.631 | 0 |
| 02-faltas-e-retornos | 13.862 | 0 |
| 03-rotina-da-semana | 595 | 0 |
| 04-checklist-do-dia | 3.205 | 0 |
| 05-custo-da-hora | 144 | 0 |
| 06-precificacao | 185 | 0 |
| 07-simulador-convenio-x-particular | 181 | 0 |
| 08-tabela-de-precos | 221 | 0 |
| 09-caixa-da-clinica | 2.685 | 0 |
| 10-provisao-de-impostos | 189 | 0 |
| 11-repasse-e-pro-labore | 1.279 | 0 |
| 12-reserva-e-metas-de-caixa | 227 | 0 |
| 13-convenios-a-receber | 9.368 | 0 |
| 14-parcelas-e-inadimplencia | 5.405 | 0 |
| 15-orcamentos | 2.366 | 0 |
| 16-conciliacao-de-cartao | 5.149 | 0 |
| 17-painel-da-clinica | 138 | 0 |
| 18-resultado-mensal | 285 | 0 |
| 19-metas-do-trimestre | 144 | 0 |
| 20-resumo-do-mes | 213 | 0 |

Verificações automáticas (20 arquivos): nenhuma célula amarela bloqueada; nenhuma fórmula desbloqueada fora das datas
`=TODAY()±n` (amarelas de propósito); funções usadas: ABS, AND, AVERAGE, AVERAGEIFS, CEILING, CHAR, CHOOSE, COUNT,
COUNTA, COUNTIF, COUNTIFS, DATE, DAY, FIXED, IF, IFERROR, INDEX, INT, ISNUMBER, LARGE, LEFT, LEN, LOWER, MATCH, MAX,
MIN, MOD, MONTH, OR, REPT, ROUND, ROUNDUP, ROW, SUM, SUMIF, SUMIFS, SUMPRODUCT, TEXT, TIME, TODAY, WEEKDAY, YEAR (nada
pós-2007, nenhum `_xlfn.`); nenhum "Sheet1", TODO, placeholder ou inglês; todas as abas protegidas sem senha; "Como
usar" é a primeira aba em todas; listas suspensas de escolha com `OFFSET/COUNTA` (01 Config/Pacientes/Agenda, 02
Agenda, 03 Rotina, 04 Checklist, 07 Simulador B8, 09 Lançamentos, 11 Repasse/Retiradas, 13 Guias/Lotes, 14 Parcelas,
15 Orçamentos, 19 Metas) e listas fixas só para Sim/Não, situações, formas e dias; colunas auxiliares ocultas em 02
(U:V), 04 (Z:AB), 06 (T:W), 11 (N), 13 (N, S:T), 14 (N:O), 15 (Q), 16 (O), 20 (N:U); hora como `hh:mm`; datas
`dd/mm/yyyy`; competência `mm/yyyy`; variação de indicadores em % como p.p. (17, 18, 20); `verifica_coerencia.py` nas 20
cópias: 518 verificações OK, 0 falhas; nenhum lançamento pago depois de 11/09, nada "Realizado" depois de 11/09, nada
"Agendado/Confirmado" antes de hoje; nenhum dado clínico (procedimentos só com nome administrativo, pacientes só com
nome e contato fictício 90000-xxxx, sem CID, prontuário ou exame).

Recalculei à mão e conferiram: 05 (10.000 + 18.000 = 28.000; ÷ 140 h = 200,00; 200 ÷ (1 − 0,30 − 0,11) = 338,98 →
CEILING 340; 18.000/140 = 128,57; 10.000/140 = 71,43; horário vazio 200 × 30/60 = 100; agosto sócios 94,67 h → 295,67
e 501,14); 06 (consulta: 30 + 0,4 × 20 = 38 min; 38/60 × 200 + 4 = 130,67; mínimo 221,47; alvo 296,97; margem
particular (380 × 0,89 − 130,67)/380 = 54,6 %; simulação 45 min: 180,67 / 306,21 / 410,61 / 51,4 %); 07 (Saúde Total:
120 × 0,97 = 116,40; custo do dinheiro 116,40 × 1,5 % × 30/30 = 1,75; impostos 12,80; líquido 101,85; margem −28,82 =
−24 %; líquido/hora 160,82; mix de agosto 62/25/30/13 consultas = 130 bate com a 01; 130 × 38/60 = 82,3 h; resultado
9.880); 08 (produção 48.631 = 01 agosto; valor médio por hora 48.631 ÷ 118,33 h = 410,97; consulta 236,38/221,47 − 1 =
6,7 %); 01 (setembro: disponíveis 24 + 24 + 16 = 64 h até 13/09 com 07/09 feriado; 51,83/64 = 81,0 %; produção 10.050 +
4.145 + 5.850 = 20.045); 02 (6/(6 + 107) = 5,3 %; retorno de Paulo Freitas 30/07 + 45 = 13/09); 03 (30/36 = 83 %; 12 +
18 = 30 min); 04 (52 dias, 23 com pendência, 31 itens); 09 (26.000 + 359.157 − 332.906 = 52.251; pró-labore no ano
144.000 + 2.000 + 1.500 + 3.591 = 151.091; A receber 12.642 = 36 linhas Pago? = Não); 10 (13º 750 + 750 + 2.200 ×
1,08/12 = 1.698; férias 2.200 × 4/3 × 1,08/12 = 264; janeiro 5.621,70 − 3.630 = 1.991,70 → "Falta separar" 1.668);
11 (204,4 h × 71,43 = 14.600; 40.340 − 14.600 = 25.740; 2º tri 7.182 × 50 % = 3.591 = 1.795,6 × 2; a acertar 2.740 +
2.700 = 5.440); 12 (3 × 28.000 = 84.000; 14.000/28.000 = 0,5 mês; 70.000/3.000 = 23,3 → Setembro/2028; 52.251 − 25.997 =
26.254; 3º tri 53.101 + 50.336 + 21.570 = 125.007); 13 (a receber 4.555 + 3.430 + 2.875 + 1.646 + 1.525 + 1.727 = 15.758;
glosa 4.273/(73.702 + 4.273) = 5,5 %; 73.702 = "Transferência no ano" da 09; guias glosadas 130 + 40 = 170 = glosa do lote
jul/2026 Saúde Total); 14 (4.550/(39.005 + 4.550) = 10,4 %; 39.005 = "Particular a prazo" no ano da 09; faixas 320/590/
450/3.190; ordem valor × dias); 15 (21 aprovados = 8.510; 21/29 = 72 %; 8.510/18.000 = 47 %); 16 (8.090 × 1,5 % =
121,35; 5.840 × 3,2 % = 186,88; 4.510 × 3,9 % = 175,89; 484,12 = saída "Taxas de cartão" de 31/08 na 09); 17 (15 valores
da aba Dados = painéis de 01, 02, 09, 13, 14, 15); 18 (50.336 − 40.696 = 9.640; 19,2 %; julho 23,7 %; agosto = 09
Painel por categoria); 19 (semana 11 de 13 = 82,4 %; glosa (6,1 − 5,5)/(6,1 − 4) = 28,6 %); 20 (12 indicadores = 17
Histórico jul/ago + 18; destaques coerentes).

A coerência entre planilhas (mesmas pessoas, convênios, procedimentos, pacientes, valores; 17 = painéis; 18/20 =
agosto; 09 × 13 × 14 × 16) está boa. Os defeitos abaixo são de **apresentação que trava o uso**, de **exemplo que não
fecha na história** e de **conceito que o contador vai questionar**.

#### GRAVE

1. **08 Tabela não tem cabeçalho nas colunas A a M.** `08 Tabela!A4:L5` é o bloco de KPIs (Hora mínima, Particular
   abaixo do mínimo, … Contra a hora mínima); a linha 5, que deveria ser o cabeçalho da tabela (Procedimento, Minutos,
   Gera retorno?, Material, Custo cheio, Preço mínimo, Preço alvo, Particular, Saúde Total, MediPlan, Vida Care, …), só
   existe de `M5` em diante (`M5` = 6º pagador vazio, `N5` "Situação do particular" … `T5` "Referência de mercado").
   Visto: `A6:M17` são números sem nome de coluna (30, Sim, 4, 130,67, 221,47, 296,97, 380, 120, 100, 90). Esperado: uma
   linha de cabeçalho inteira acima de `A6`. Causa em `build_08_tabela_de_precos.py`: `hdr(t,T0-1,heads)` escreve o
   cabeçalho na linha 5 e `kpi(t,4,…)` sobrescreve `A4:L5`. É a "tabela de referência" prometida na página; sem
   cabeçalho, o médico não sabe qual coluna é o convênio e qual é o custo.
2. **15 tem 4 orçamentos aprovados antes de serem apresentados.** `15 Orçamentos!A36:A39` = 15/09, 18/09, 21/09 e
   30/09/2026 (Ana Costa, Viviane Ribeiro, Wagner Costa, Gisele Ribeiro) com `H36:H39` (data da decisão) = 11/09/2026:
   `N36:N39` "Dias até decidir" = −4, −7, −10, −19. Visto: `15 Painel!K5` "Dias até decidir (média)" = 5,9; esperado
   sem esses quatro: 9,6. `E5` "Aprovado no trimestre" 8.510 inclui 1.400 de orçamentos "apresentados" no futuro. As
   datas são fixas e futuras (convenção 6 manda relativa). Origem: `dados.ORCAMENTOS` usa a data do agendamento
   (`atendimento` 21/09, 05/10, 01/10, 05/10) como data do orçamento. Um médico que abre a aba principal vê "orçamento
   de 30/09 aprovado em 11/09" na segunda tela do funil.
3. **A Agenda (01) acaba em quatro meses.** `01 Agenda!A5:R1204` tem 1.200 linhas; o exemplo usa 939 (309 em julho, 292
   em agosto, 296 em setembro, 42 em outubro: ≈ 300/mês para 3 médicos). Todas as fórmulas do Painel apontam para
   `$5:$1204` fixo, a aba é protegida e nenhum "Como usar" (01 B5:B10) fala do limite nem de como estender; `17
   Config!A11` diz "use a mesma planilha o ano inteiro". O mesmo em `02 Agenda` (cópia, 1.200 linhas) e em `16 Vendas`
   (600 linhas; ≈ 90 vendas/mês no exemplo → 6 meses). Quem apagar o exemplo e começar em outubro fica sem linha em
   fevereiro.

#### MÉDIO

4. **06 e 08 contam "tabelas de convênio abaixo do custo" de dois jeitos.** `06 Precificação!E25` "Tabelas de convênio
   que não cobrem o custo cheio" = **14** (`COUNTIF(T5:W16,"<0")`, T:W = margem **após 11 % de imposto** × tabela);
   `08 Tabela!E5` "Tabelas de convênio abaixo do custo" = **11** (`O6:O12` = tabela < custo cheio, **sem** imposto).
   Mesmas 7 linhas, mesmos valores, dois números; e o rótulo da 06 diz "custo cheio" quando a conta é "margem
   negativa". MAPA MediPlan (85 × custo 81,67) e Holter MediPlan (95 × 84,67) e MAPA Vida Care (75 × 81,67) explicam a
   diferença.
5. **Página e oferta prometem "custo da hora ÷ horas atendidas"; a 05 divide por horas planejadas.** `05 Painel!B12`
   "Horas de atendimento no mês" = 140 = `Equipe!F5:F6` (turnos × 4,33 semanas, planejadas); a ocupação real de agosto é
   70,4 % (`01` com Config = Agosto) e o custo-hora real de agosto é R$ 295,67 (`05 Painel!D45`), hora mínima R$ 501,14
   (`E45`). Todas as planilhas de preço (06 Config B7, 07 Config B5, 08 Config B7) usam os R$ 200 de agenda cheia:
   preço mínimo de consulta 221,47 (06 G5) seria 326,20 com as horas atendidas. A sensibilidade fica só na 05 e não
   chega à 06/07/08; página (`medicos.html`, núcleo Preço e "Custo da hora de atendimento (fixo + equipe + pró-labore
   ÷ horas atendidas)") e oferta (`02-oferta/medicos.md`, mecanismo 2 e tabela linha 5) dizem "horas atendidas".
6. **11 cobra a estrutura duas vezes (contador).** `05 Painel!B20` = 10.000 ÷ 140 h = R$ 71,43: os custos fixos inteiros
   já estão dentro do custo-hora dos sócios (R$ 200). `11 Config!B11` usa os mesmos 71,43 × 204,4 h da parceira = `11
   Painel!I9` 14.600 "Custo das horas (ano)" → `J9` "Margem da parceria" 25.740. Somando, 12.500/mês de estrutura
   alocados para 10.000 reais. Ou a estrutura se divide por 175 h (57,14/h; custo-hora dos sócios 185,71; hora mínima
   314,76) ou a margem da parceria não desconta estrutura já paga. Nada explica a escolha em `11 Config!D11` nem em
   `05 Equipe!A17`.
7. **A rotina de 30 minutos por semana não fecha entre as planilhas.** `03 Rotina` e a página: 12 min na segunda + 18 na
   sexta = 30. Mas os "Como usar": `01 B9` segunda 10 min, `02 B8` segunda 10 min, `14 B9` segunda 10 min (= 30 na
   segunda); `09 B8` sexta 15 min, `12 B8` sexta 5, `15 B9` sexta 10, `16 B8` sexta 10, `17 B5` sexta 10, `19 B8` sexta
   10 (= 60 na sexta), mais `04 B8` 13 min por dia. E quem lança o caixa: `04 Config!D11` "Fechamento do dia lançado no
   Caixa (09)" todo dia pela recepção (Checklist C = Bruna) × `03 Rotina!B9/D9` "Lançar os fechamentos do dia da semana
   no Caixa (09)" na sexta, 5 min, Dra. Carolina × `09 Como usar!B8` "Rotina de sexta, 15 minutos: lançar os fechamentos
   do dia da semana". Três versões da mesma tarefa.
8. **O exemplo dá crédito novo a quem está inadimplente.** Em `14 Parcelas` há 12 parcelas a prazo combinadas com
   pacientes que já tinham parcela vencida: Eduardo Lima (vencida 12/06/2026, `14 Painel!B23`) recebe a prazo em 24/07
   (teste ergométrico 450, vencida 23/08) e em 20/08 (consulta 380, vence 19/09, `14 Painel!B36`) e ainda tem MAPA
   aprovado em 08/09 (`15 Orçamentos`, agendado 10/09, realizado no cartão); Márcia Duarte (vencida desde 12/02, 214
   dias) recebe a prazo em 21/05 e 23/07; Regina Teixeira, Otávio Cardoso, Gabriel Reis, Paulo Reis, Otávio Nascimento,
   Mariana Reis idem. A régua da 14 (`Config!B13`, 30 dias: "conversa … plano de pagamento") e a lista "Cobrar primeiro"
   perdem sentido no próprio exemplo; um médico estranha e o contador pergunta por que a inadimplência de 10,4 % não
   cai.
9. **09 "A receber (Pago? = Não)" segue uma regra que não está escrita.** `09 Painel!I5` = 12.642 = 36 linhas com Pago?
   = Não (`Lançamentos` linhas 92 a 736): parcelas vencidas desde 12/02, parcelas a vencer até 26/09, os dois lotes com
   previsão até 30/09 (Vida Care jun 1.727, MediPlan jul 2.875) e as saídas até 28/09. Mas `09 Config!A39` diz
   "Particular a prazo entra por paciente, **quando a parcela é paga** (14). Convênio entra **por lote pago** (13)" e
   `Lançamentos!A2` só diz que Pago? = Não "fica em A receber". Quais lotes e parcelas pré-lançar (até o fim do mês? todas?)
   não está em lugar nenhum; `13 Painel!A5` A receber 15.758 + `14 Painel!E5` em aberto 10.585 = 26.343 ≠ 12.642 e o
   Painel da 09 não explica. As descrições em `F` são texto fixo "(vencida)" / "(a vencer)" (`F92`, `F733`) e envelhecem
   quando a data passa.
10. **18 promete "lucro de verdade" sem provisão de 13º e férias (contador).** `18 Resultado` tem custos fixos,
    variáveis, pró-labore e impostos (11 %), mas não a provisão de 13º e férias que a 10 calcula (`10 Painel!D8:E8`,
    1.698 + 264 = R$ 1.962/mês). Resultado de agosto `18 Painel!E5` 9.640 (19,2 %) seria 7.678 (15,3 %). E a 18 provisiona
    imposto sobre "Outras entradas": abril `Resultado!E33` = 4.355 = 11 % × 39.590 (com a devolução de 620 da sócia)
    contra `10 Painel!C12` = 4.286,70 sobre 38.970 e `11 Resultado mensal!B8` = 38.970; a "Receita total" de abril
    (`18 Resultado!E12` 39.590) inclui a devolução de despesa pessoal, que não é receita.
11. **19 usa uma agenda de junho que o kit não tem.** `19 Metas!E5:E6` (ponto de partida 75,2 % e 6,9 %) e `19
    Semanas!C5:F6` (S1 a S4, 03/07 a 24/07) são "últimas 4 semanas", que em 03/07 vão de 06/06 a 03/07; `01 Agenda`
    começa em 01/07 (`Agenda!A1207`) e `17 Histórico!B10:E10` deixa junho em branco. `19 Metas!L5` diz "Painel da
    planilha 01": não é reproduzível a partir da 01. O mesmo para `L9` "partida = média de janeiro a junho" do prazo real
    (46,7), que a 13 calcula (lotes desde out/2025), mas com `Semanas!C9` = 0 na S1 (ver item 19).

#### LEVE

12. `20 Resumo!A6` (observação da clínica): "o lote de **julho** da Saúde Total pago com glosa em recurso" → é o lote de
    competência **junho** (`13 Lotes` linha 29: jun/2026, enviado 06/07, pago 05/08, Em recurso 240); "o lote de junho da
    Vida Care ainda não caiu e entrou na cobrança ao convênio" no fechamento de agosto, quando a previsão era 04/09
    (`13 Lotes!L31`): em 31/08 não estava vencido.
13. `13 Painel!I53:I54` "Recurso" mostra **0** (INDEX de célula vazia) e `A65` diz "Recurso em branco = ainda não
    recorreu".
14. `06 Precificação!S4` "Margem" fica como cabeçalho órfão (R4 = "" porque não há 4º convênio); `06 K6` (Retorno) fica
    vazio enquanto `08 N7` mostra "Sem cobrança" para a mesma linha.
15. `03 Painel!J4:K7` (Última semana registrada 36 / Semana da data de referência 37 / Semanas consideradas 4 /
    Rotinas planejadas 9) é bloco auxiliar visível dentro da faixa de KPIs.
16. `16 Vendas!K` põe o líquido inteiro do parcelado na previsão da 1ª parcela (`Painel!G20:G50` "Cai na conta neste
    dia" e `K5` "A conferir" somam tudo): Ana Costa 11/08, crédito em 2× (`Painel!C61`), aparece com 365,18 em 10/09
    quando só metade cai nesse dia; `Vendas!A606` diz que "as seguintes caem de 30 em 30 dias", mas nada calcula isso.
17. `17 Dados!D19` "Orçamentos em aberto (valor)" = "Maior é melhor" com meta 5.000 → `17 Painel!E30` "Fora" e `20
    Painel!G16` "Abaixo da meta" por haver **pouco** orçamento pendente; para o médico, "Fora" aqui soa como problema.
18. `12 Config!B13:B15` = 28.000 nos três meses, mas `D13` manda copiar de "Para onde foi o dinheiro" da 09, que dá
    29.500 em junho (retirada extra 1.500) e 31.591 em julho (distribuição 3.591). E "custo fixo" vale 10.000 na 05/09/18
    e 28.000 na 12 (com pró-labore), com o mesmo nome.
19. `19 Semanas!C9` = 0 (prazo real médio na S1, sem lote pago no trimestre) entra na série e derruba o gráfico; deveria
    ficar vazio como "—".
20. `10 Painel!E5` "Saldo provisionado ao fim de setembro" 21.937 sai de entradas parciais (até 11/09) e vira **meta
    fixa** em `12 Config!B28` e `19 Metas!F13` ("Meta = saldo provisionado de setembro"): alvo que muda quando setembro
    fechar.
21. `05 Config!C8` "impostos da PJ médica **e taxas**": se "taxas" inclui maquininha, `16`/`18` contam de novo (taxas de
    cartão como despesa variável) e a `07` aplica os mesmos 11 % ao convênio, que não paga taxa de cartão. Dizer só
    "impostos" ou explicar.
22. `01 Painel!A34:H34` (Segunda) zerado em setembro porque 07/09 é feriado e 14/09 é hoje; sem nota, o leitor acha que
    ninguém atende na segunda (Carolina e Paulo atendem).
23. Tabela de preços digitada em quatro lugares: `01 Config!M5:P11`, `06 Precificação!I5:P11`, `07 Simulador!B19:B22`
    e `08 Tabela!H6:K12`; `06 Como usar!B8` manda atualizar 08 e 01, não a 07. Procedimentos em 01/02/06/07/08, pessoas
    em 01/02/03/04/05/10/11/15/19, convênios em 01/02/06/07/08/09/13: nada lista a ordem de atualização.
24. Oferta (`02-oferta/medicos.md`): "~120 pacientes fictícios" × `01 Pacientes` 156. Página: `{{med_aula1_dur}}` …
    `{{med_aula8_dur}}`, `{{empresa.razao_social}}` e `{{checkout.kit_medicos}}` ainda como marcador em
    `site/src/pages/medicos.html` (se `site/build.py` substitui, ok; não verificado).
25. `05 Painel!B45` "Agosto de 2026 realizado" = 94,7 h digitado; as horas atendidas dos sócios em agosto são 94,67
    (118,33 − 23,67 da parceira); arredonda certo, mas `A45` diz "planilha 01" e a 01 não mostra horas por sócio somadas:
    o usuário precisa somar `01 Painel!C11 + C12` com Config = Agosto, e isso não está escrito.

#### Promessas da página × planilhas (item 6)

Existem e funcionam: agenda com horas disponíveis × atendidas por profissional e sala, faltas, produção, próximos 7
dias (01); taxa de falta por dia, período, pagador e profissional, últimas 8 semanas, lista de retorno (02); rotina de
segunda e sexta com aderência (03); checklist de abertura e fechamento com pendências (04); custo da hora com
sensibilidade (05); preço de consulta e procedimento com material, retorno embutido e margem por pagador (06); simulador
convênio × particular com prazo, glosa esperada, custo do dinheiro, leitura de agenda cheia e vazia e mix do mês (07);
tabela de referência com valor por hora por pagador (08, ver item 1); caixa por categoria, forma, mês a mês, a receber e
a pagar (09); provisão de impostos, 13º e férias com saldo e compromisso (10); repasse por produção, pró-labore, fora do
combinado e distribuição por trimestre (11); reserva de 3 meses, projeção e metas de caixa (12); guias, lotes, glosa,
recurso, atrasados e prazo real (13); parcelas com régua de 4 faixas, "cobrar primeiro" e "vencem nos próximos dias"
(14); funil de orçamentos por etapa, tipo, motivo e profissional (15); conciliação de cartão com Pix, débito, crédito à
vista e parcelado, antecipação e "cai na conta neste dia" (16); painel de uma tela com 15 indicadores e semáforos (17);
DRE com previsto (18); metas do trimestre com semanas (19); resumo em bloco único (20). "Tudo bate entre si" bate: os 15
números da 17 são os painéis de origem, 18 e 20 são o caixa de agosto, 09 × 13 × 14 × 16 fecham ao real.

O que falha frente à página e à oferta: "custo da hora ÷ horas atendidas" (item 5), "rotina de 30 minutos por semana"
(item 7), "lucro de verdade" (item 10), "use a mesma planilha o ano inteiro" (item 3), e a tabela de referência sem
cabeçalho (item 1). O exemplo, que a página chama de "conferido célula a célula", tem orçamentos aprovados antes de
apresentados (item 2) e crédito a inadimplentes (item 8).

Não verificado: abertura em Excel e Google Sheets reais (locale de FIXED/TEXT, CEILING no Sheets), impressão, arquivos
21–29, vídeos, LEIA-ME e a substituição dos marcadores da página por `site/build.py`.


## Relatório B · documentos 21–29

Data: 2026-09-14. Revisor B (cliente exigente: médico dono de clínica, contador de PJ médica, leitor da Resolução CFM 2.336/2023 e da LGPD em saúde). Nenhum arquivo do projeto foi alterado; cópias, renders e scripts em `scratchpad/revMB/`. Verdade dos números: `produto/kit-medicos/NUMEROS.md`; conferências adicionais direto nas 20 planilhas (openpyxl).

### Testes feitos

| Teste | Resultado |
|---|---|
| Páginas por PDF (PyMuPDF 1.28; `pdftoppm`/`pdfinfo` não instalados) | 21: **27** · 22: **8** · 23: **10** · 24: **5** · 25: **1** · 26: **22** (oferta: "cerca de 20 páginas") |
| Render das 73 páginas a 80 dpi em folhas-contato (`sheet2N-*.png`) + manual p. 8/10/12/16/17/18/19 a 110 dpi (`manual-p*-110.png`) + `p21-empties.png` | olhadas uma a uma |
| Texto extraído por página (`2N-texto.txt`) e grep de `None`, TODO, lorem, "Sheet N", `{{`, NaN, inglês | nenhum placeholder, nenhum inglês, nenhum caractere quebrado (o único não-latino é o sinal "−" U+2212, correto) |
| Metadados (Título) dos 6 PDFs | "Biblioteca de prompts da clínica · Kit de Gestão para Médicos", "Mensagens de confirmação e cobrança · …", "Guia LGPD para a clínica pequena · …", "Roteiro da reunião com o contador · …", "Checklists da clínica · …", "Manual de implantação · …" (corrigido em relação ao kit anterior) |
| Ocupação de página (pixels, sem o rodapé) | 21: p. 13 termina a 76 %, p. 17 a 82 %; 24: p. 5 a 49 %; 26: p. 22 a 55 %; o resto acima de 85 % |
| Biblioteca 21: contagem por título no PDF e no txt | **40** prompts (Agenda 01–08, Preço 01–08, Caixa 01, 02, 04–09, Recebíveis 01–08, Painel 01–08); os 40 têm "Quando usar", "Cole", bloco de prompt, "Exemplo" e "Confira" (41 "Exemplo:" no txt = o do modelo em branco) |
| Nomes de prompt citados na aba "Como usar" das 20 planilhas (openpyxl) × títulos da biblioteca | os 26 nomes citados existem, escritos igual (inclusive "Preço 02 · Revisar a tabela de preços pela margem" e "Preço 04 · Revisar a tabela de preços"); nenhuma planilha cita "Caixa 03" |
| Abas citadas em 21, 22, 24, 25, 26 e nos slides × abas reais das 20 planilhas | todas existem (Painel, Config, Pacientes, Agenda, Rotina, Checklist, Custos fixos, Equipe, Precificação, Simulador, Tabela, Lançamentos, Entradas e pagamentos, Repasse, Resultado mensal, Retiradas, Guias, Lotes, Parcelas, Orçamentos, Vendas, Dados, Histórico, Resultado, Previsto, Metas, Semanas, Resumo, Indicadores) |
| 21 txt e 22 txt | texto puro: 0 `**`, 0 crases/cercas, 0 `#`, 0 tabela em pipes, sem BOM, LF; diferentes do .md de origem (corrigido) |
| Exemplos do 21 × NUMEROS.md × planilhas | ~180 números conferidos um a um; batem, exceto os listados em MÉDIO 3–8 |
| 22: contagem e régua | **15** modelos (01–15); régua 1/7/15/30 e textos das ações **iguais** à Config da 14 (lembrete gentil por WhatsApp · mensagem da recepção com nova data · ligação com demonstrativo · conversa do médico ou da administração e plano por escrito); "3 dias antes" = faixa "Antes da régua" da 14; nota fiscal citada em 07, 12, 13, 14 e na tabela final; CDC art. 42 citado; nenhum modelo cita negativação, juros, suspensão; nenhum pede avaliação pública ou indicação (15 pede opinião privada e cita a CFM 2.336/2023); nenhum dado de saúde |
| 23: normas citadas | LGPD art. 5º, II e art. 11 (corretos); Resolução CD/ANPD 15/2024 com 3 dias úteis (correto); prazo de prontuário **sem número**, remetido à resolução do CFM (correto); ressalva "não é parecer" na p. 2 e p. 10 |
| 24 | "fator r" (Simples anexo III/V), nota fiscal obrigatória e "como regularizar recebimento sem nota" (Bloco 2, item 3), retenção pelas operadoras, distribuição de lucro só de trimestre apurado: consistente com o que um contador de PJ médica espera |
| 25 | 3 checklists (8 + 12 + 10 itens): abertura e fechamento do dia, fechamento do mês, antes de fechar um convênio = LEIA-ME, página e oferta |
| 26: semanas × planilhas × aulas | Semana 1 = 01–05 (aulas 2, 3) · 2 = 06–10 (4, 5, 6 primeira metade) · 3 = 11–16 (6 segunda metade, 7) · 4 = 17–20 (8): **as 20 planilhas entram**; títulos das 8 aulas (p. 3) iguais aos canônicos e ao LEIA-ME; Excel 2016 (p. 3 e p. 21); rotina 12/18 (p. 2, 4, 9, 20); 21 capturas com legenda "Planilha NN · aba X (Config = …)" |
| Slides (python-pptx + soffice → PDF → PNG, `slides27/28/29.png`) | 27: **8** · 28: **10** · 29: **8**; nenhuma caixa fora do slide; notas do apresentador nos 26 slides; marca = 4 autoformas nos layouts CLARO e ESCURO (nenhuma forma solta nos slides; nada no slide mestre propriamente dito); rodapé "modelo v1.0" só nas notas |
| Slides × NUMEROS.md | 27 (50.336 / 40.696 / 9.640 / 19,2 %; 168 h, 118,3 h, 70,4 %, 23 faltas, 48.631; mix 12.867 / −720 / −1.474 / −793; caixa jun–ago; 18.311; 17.602; 5,6 %; 4.040 / 3.380; 3.190 + 1.360; 8.510) e 29 (11.161 com 665 de glosa = 5,6 %; 337.587 por origem; lotes 7.560/2.265/2.001; 15.758 = 4.555 + 6.305 + 4.898; 73.702; 4.273; 800 recuperados; 31.820 / 484,12; provisão 37.067 / 13.584 / 2.112 / 52.763 / 35.160 / 17.602; a acertar 2.740 + 2.700 = 5.440; trimestres −2.791 / 7.182 / 12.891): **todos batem** |
| 28 | sem custo-hora, custo da estrutura, hora mínima ou margem em nenhum slide (só nas notas, como proibição); contatos entre colchetes; validade 29/09 (14/09 + 15) |
| 29 | só totais nos slides; slide 3 diz "a lista de guias fica na clínica"; ver GRAVE 2 sobre o slide 8 |
| LEIA-ME × `entrega/` | 30 arquivos listados = 30 arquivos presentes (20 xlsx, 21 pdf+txt, 22 pdf+txt, 23–26 pdf, 27–29 pptx); `videos/` tem 4 das 8 aulas (01, 02, 03, 05) com .srt: fora do escopo (em gravação) |
| LEIA-ME × página `medicos.html` × oferta | 20 planilhas, 40 prompts (PDF e txt), 8 aulas de 2 a 3 min, manual em 4 semanas, 3 modelos (8/10/8), 3 checklists, 3 bônus com os mesmos nomes; 22 em PDF + txt como a oferta promete; Excel 2016 nos três; 12/18 minutos na página, LEIA-ME e manual |

---

#### GRAVE

1. **Prompt "Caixa 03" não existe, mas é citado quatro vezes, com nome.** 21, p. 2: "o grupo Caixa vai de 01 a 09 sem o 03". 21, p. 3, tabela "De onde vem cada bloco": planilha 5 → "Preço 01, **Caixa 03**, Painel 07"; planilha 9 → "Caixa 01, **03**, 06". 26, seção 4.5 (p. 10): "Prompt: Preço 01 (…), **Caixa 03 (cortar custo fixo)**, Painel 07"; seção 4.9 (p. 12): "Caixa 01 (…), **Caixa 03 (cortar custo fixo)**, Caixa 06". Visto: o manual manda o leitor abrir um prompt que a própria biblioteca diz não existir; a tabela da biblioteca contradiz o parágrafo imediatamente anterior. Esperado: ou o prompt "Caixa 03 · Cortar custo fixo" existe (e a numeração 01–08 fecha sem furo), ou as quatro citações saem. Também na tabela p. 3: planilha 9 lista "Caixa 06", que não cola nada da 9 (cola o extrato bancário e lança na 11); o que usa a 9 é o Caixa 08 (sobra média), ausente da linha.

2. **29, slide 8 "Anexos enviados com este resumo": "Tudo em .xlsx, com as fórmulas; o contador não precisa alterar nada"**, listando 09 · Caixa da clínica, 11, 16 · Conciliação de cartão, 18 e 20. O arquivo 09 tem a aba Lançamentos com **169 linhas de "Particular a prazo" com nome do paciente + procedimento** ("Márcia Duarte · Avaliação endócrina de 13/01 · parcela 1/2 (vencida)"); a 16 tem a aba Vendas com Paciente + Procedimento em 220 linhas. O 24 (p. 2) diz "Não mande (…) qualquer coisa com nome de paciente. (…) nome de paciente com procedimento já é informação de saúde"; o 23 (seção 5) diz que o contador não acessa "nome, guia, procedimento por pessoa"; o LEIA-ME diz que o 29 vai "só totais". Esperado: o slide 8 mandar só a aba Painel (cópia de valores, ou PDF) das 09 e 16, como o 24 descreve, ou o texto "tudo em .xlsx" sair.

3. **21, Preço 04 (p. 11) e 26, 4.8 (p. 12): "ECG a R$ 78,67 (38 % abaixo: 13 dos 18 foram por convênio)".** Contado na aba Agenda da 01 (agosto, Realizado, ECG): **8 particulares, 7 Saúde Total, 3 Vida Care, 0 MediPlan = 10 de 18 por convênio** (8 × 130 + 7 × 40 + 3 × 32 = 1.416, exatamente a produção da 08). "13 dos 18" é aritmeticamente impossível: 5 × 130 + 13 × 40 = 1.170 ≠ 1.416. O número aparece como fato da planilha nos dois documentos e é a primeira coisa que o médico confere ao abrir a 01. Esperado: "10 dos 18".

#### MÉDIO

1. **21 PDF: 8 dos 40 blocos de prompt são cortados pela quebra de página, com o rodapé no meio.** Agenda 02 (p. 4→5), Preço 01 (p. 8→9), Preço 04 (p. 10→11), Caixa 05 (p. 15→16), Caixa 07 (p. 16→17), Recebíveis 06 (p. 21→22), Recebíveis 08 (p. 22→23), Painel 06 (p. 25→26). Quem seleciona o prompt no PDF leva "Seu Sócio Gestor · Kit de Gestão para Médicos · página 4 de 27" junto. O txt resolve, mas o PDF é o arquivo principal. Esperado: `page-break-inside: avoid` no bloco `pre` (o kit já faz isso com "Exemplo", que nunca quebra).

2. **21, Caixa 06 (p. 16), exemplo: "48 lançamentos de junho (…) dois lançamentos pessoais pagos pela clínica (R$ 620, a acertar)".** Na aba Retiradas da 11 e no Caixa 09, junho tem só a retirada extra de R$ 1.500 (19/06); despesas pessoais de R$ 620 existem em fevereiro, maio e agosto ("Plano de saúde da família") e "Outras saídas" de junho = R$ 0 (NUMEROS §3). O exemplo inventa um lançamento que o comprador não acha ao abrir a planilha.

3. **21, Caixa 08 (p. 17), exemplo: "sobra média dos últimos 3 meses R$ 8.777 (junho R$ 2.321, julho R$ 9.674, agosto R$ 8.716)".** A média dos três números escritos é **R$ 6.904**; R$ 8.777 é a média de julho, agosto e setembro parcial (9.674 + 8.716 + 7.940). O prompt pede "conservador R$ 3.000 / provável R$ 5.000 / ambicioso R$ 7.000" — o "ambicioso" fica acima da sobra real. Conta errada no exemplo de um prompt cujo "Confira" é justamente "a sobra média".

4. **21, Painel 07 (p. 26), exemplo: "o novo turno precisa de cerca de R$ 1.150 de produção por mês só para pagar a estrutura das 16 horas".** Dois turnos por semana de 4 h = 8 h/semana ≈ 32–36 h/mês, não 16; e a 16 h × R$ 71,43 = R$ 1.143 é custo, não produção: com repasse de 50 %, a produção necessária é o dobro (o próprio prompt diz "custo ÷ o que fica com a clínica por hora"). Pela conta do kit, o turno precisa de ~R$ 4.600 de produção/mês, quatro vezes o que o exemplo diz.

5. **21, Painel 01 (p. 23), exemplo: os "comentários" do sócio contradizem as planilhas e o resto do kit.** "O MediPlan glosou três guias de consulta por código de procedimento errado" × 13 Painel: as duas únicas guias glosadas são da **Saúde Total** (G2026-0577 e 0582, avaliação endócrina e ECG); "o Vida Care pagou o lote de julho" × 13: o lote de julho do Vida Care está **Aguardando** (previsão 04/10) e o que caiu em agosto foi o de **maio**. A decisão de saída, "recorrer das três glosas do MediPlan até o dia 20", contradiz Painel 06 (p. 26), 26 (4.13) e 27 (s8): "as duas guias glosadas de julho (Saúde Total, R$ 170)". Exemplo do prompt "mais usado do kit".

6. **26, capturas das seções 4.6 a 4.20: cartões legíveis, tabelas não; a da 08 sai cortada.** As imagens têm 1.600–2.100 px de largura impressas em 90–120 mm: os cartões leem-se, mas as tabelas ("Por profissional", "Para onde foi o dinheiro", Precificação, Tabela) ficam em ~3–4 pt (`manual-p8-110.png`, `manual-p12-110.png`). Na p. 12, "Planilha 08 · aba Tabela" está **cortada à direita** (as colunas "Valor médio praticado" e "Contra o mínimo" saem pela metade, o "+7 %" do texto não aparece inteiro). Esperado: recorte dos cartões + primeira tabela em largura total, ou captura só dos cartões.

7. **22 e 25 × 23 sobre quem lança o quê.** 25 ("Fechamento: caixa do dia (…) lançado no Caixa (Planilha 9)") e 04/26 4.4 (item mais esquecido da recepção: "Fechamento do dia lançado no Caixa (09)") dizem que a recepção lança na 09; a 03 · Rotina e 21 Agenda 06 dizem que quem lança é a Dra. Carolina na sexta; o 23 (seção 5) lista o que a recepção acessa (1, 2, 4, 13, 14, 15) sem a 09 nem a 16, embora 26 4.16 mande marcar "Conferido no extrato?" toda sexta. Para quem vai montar a matriz de acesso do guia LGPD, o kit dá três respostas.

8. **21, Recebíveis 01 (p. 19), exemplo: "vence em 30 dias R$ 4.602".** Pela 13, o que vence de 11/09 a 11/10 é MediPlan jul (2.875, 19/09) + Vida Care jul (1.525, 04/10) + Saúde Total ago (4.555, 08/10) = **R$ 8.955**; R$ 4.602 = MediPlan jul + o lote **atrasado** do Vida Care (1.727), que o mesmo exemplo já contou à parte. Também Painel 02 (p. 24): "convênios pagos R$ 11.161, os três maiores do ano" — MediPlan R$ 2.130 em agosto é menor que fevereiro (2.660) e maio (2.610).

9. **28, slide 7 "Como funciona na prática: a parceria da Dra. Renata": produção e repasse mensais de uma médica identificada (R$ 74.830 / R$ 37.415 no ano, gráfico jan–ago), num documento que vai para um médico de fora.** A nota diz "só com autorização do parceiro atual", mas o slide não traz nenhum marcador de "[remover se não houver autorização por escrito]" e o 23 trata dado de equipe com nome como coisa que não sai da clínica (seção 6: "dado de equipe (salário, atestado, avaliação) com nome"). Esperado: o slide como simulação por padrão ("um parceiro com dois turnos produziu…"), com o exemplo nominal atrás de colchetes.

10. **LEIA-ME, 26 (p. 2) e notas dos 26 slides: "A marca do kit está só no slide mestre: apague lá uma vez (Exibir > Slide mestre) e some de todos".** As 4 autoformas da marca estão nos **layouts** CLARO e ESCURO, não no mestre (o mestre está vazio, `pp_extract.py`). Em "Exibir > Slide mestre" o usuário vê o mestre limpo, e precisa apagar nos dois layouts (duas vezes, não uma); quem apaga só no primeiro layout que vê deixa a marca nos slides do outro. Esperado: marca no mestre, ou o texto dizer "nos dois layouts (Claro e Escuro)".
11. **26, 4.3 (p. 9) e 21, Agenda 05 (p. 6) descrevem uma planilha 03 que a entrega não tem.** "83 % de aderência nas últimas 4 semanas", "registradas S29 a S36", "'ligar para a lista de retorno' feita em 1 de 4 semanas": na `entrega/03-rotina-da-semana.xlsx` (gravada às 22:11, depois das outras 19), a aba Rotina está com as colunas S1–S16 **todas vazias** nas 9 linhas; o Painel mostra 83 % / "Última registrada S36 · 07/09" só porque o valor está em cache. No primeiro recálculo (abrir e digitar qualquer coisa) o Painel zera e o manual passa a descrever um exemplo que não existe. É defeito da planilha, fora do escopo destes documentos, mas os dois textos dependem dele; a 16 (mesmo horário de gravação) está com a aba Vendas preenchida.

#### LEVE

1. 21, p. 13: página termina a 76 % porque "Grupo 3" abre página nova; p. 17 a 82 %. 24, p. 5: metade da página (melhorou da versão anterior, que tinha uma linha). 26, p. 22: 55 % (tabela de erros + suporte).
2. 21, Preço 07 (p. 13): "5 % no Pix leva a R$ 427,50 com margem de 51 %" — pela conta do kit (preço × 0,89 − custo cheio) ÷ preço = **52,0 %**; e a versão R$ 360 é chamada de "abaixo do piso que a clínica definiu" (R$ 400) sem dizer que também é abaixo do mínimo da planilha (R$ 268,36 não é; R$ 360 está acima). Frase confusa: o piso de R$ 400 é da clínica, não da 06.
3. 26, seção 6 "Segunda, 12 minutos": inclui "Parcelas (14): marcar as pagas e enviar as mensagens de 'Cobrar primeiro' (modelos 09 a 12)"; os modelos 11 e 12 são ligação e conversa, não mensagem, e a 03 · Rotina põe "marcar parcelas recebidas" na **sexta**. A seção 2 (p. 4) define segunda como só agenda.
4. 29, slide 8: "20 · Resumo do mês (bloco único, gerado com o prompt 'Caixa 04')" — o bloco único é gerado pela planilha 20; o Caixa 04 usa o bloco (21, p. 15). Inverte a ordem.
5. 25, "Abertura e fechamento do dia", último item: "nada clínico em WhatsApp ou e-mail sem ir para o prontuário" × 22, p. 8: "Nunca escreva, em mensagem, nada sobre a saúde do paciente". Uma lista admite conteúdo clínico em WhatsApp (se for ao prontuário), a outra proíbe.
6. 23: a palavra "encarregado" (LGPD art. 41; dispensa parcial para agente de pequeno porte pela Resolução CD/ANPD 2/2022) não aparece; o aviso de privacidade traz só "contato para assuntos de privacidade: [e-mail]". Um advogado de LGPD vai perguntar. Também 23, seção 4: "Dados das planilhas do kit [ ] anos (o mesmo do financeiro) · contador" — a 01 guarda nome + contato de 156 pacientes e a 14 nome + procedimento, que o próprio guia (p. 2) chama de "informação de saúde"; o prazo "do financeiro" não é a régua óbvia para isso.
7. 22, modelo 09 e Config da 14: "confirmar se o Pix ou o **boleto** chegou" — o kit não usa boleto em lugar nenhum (09: Boleto 0 % no ano; 16 só Pix e cartão; mensagens 07/08 oferecem "Pix ou cartão na recepção").
8. 21, p. 3, coluna "Usada nos prompts": planilha 1 não lista Caixa 07 (que cola "Por profissional" da 1) nem Agenda 03; planilha 15 não lista Painel 05; planilha 17 não lista Agenda 08 e Painel 05 (Histórico). Tabela incompleta onde os "Cole" dos prompts são a fonte.
9. 21, Agenda 07 (p. 7): "conversa de 10 minutos de segunda entre o sócio da semana e a recepção" e 01 "Como usar": "Rotina de segunda | 10 minutos" × 12 minutos em LEIA-ME, página, 26 e 03. Um terceiro tempo para a mesma segunda.
10. 27, slide 7, decisão 3: "Sala 2 com 8,2 horas vazias (…) ou um turno a mais do Dr. Paulo?" — o Dr. Paulo já é quem ocupa a Sala 2 (66 %); a frase sugere abrir turno para quem tem 34 % de agenda livre. Coerente com Painel 07, mas pede uma linha de justificativa.
11. 28, slide 3: "8 horas de agenda por semana, cerca de 32 horas por mês" × 21 Painel 07 "estrutura das 16 horas" (MÉDIO 4): o mesmo cenário com dois totais de horas.
12. Oferta (`02-oferta/medicos.md`): "~120 pacientes fictícios" × 26 (p. 3) e planilha 01: 156. Documento interno, mas é a fonte da copy.
13. 26, p. 3, tabela das aulas: coluna "Duração" com "2 a 3 min" nas oito linhas; com os mp4 prontos (4 já existem) a duração real cabe ali e evita a repetição.


## Relatório C · página, copy, e-mails e obrigado

Revisor C, revisão interna 3. Escopo: página `/medicos/`, copy, oferta, e-mails, páginas de obrigado,
contagens da entrega, conformidade (CDC, Meta, CFM 2.336/2023) e português. Nenhum arquivo do projeto
foi alterado. Estado observado: entrega reconstruída às 23:21; planilhas às 23:07–23:24; página, copy,
oferta e e-mails migrados de "40" para "41 prompts" durante a revisão (às ~23:23). Tudo abaixo foi
reconferido depois dessas mudanças. Os vídeos (22:08–22:34) não foram avaliados em qualidade: só
títulos, quantidade e durações.

### Cabeçalho de testes

**Contagens na entrega (`produto/kit-medicos/entrega/`, estado de 23:24)**

| Item | Prometido na página | Contado na entrega | ✓/✗ |
|---|---|---|---|
| Planilhas .xlsx | 20, 4 por núcleo, 5 núcleos | 20 (4+4+4+4+4) | ✓ |
| Prompts (21, PDF + txt) | 41 | 41 (Agenda 8 · Preço 8 · **Caixa 9** · Recebíveis 8 · Painel 8) | ✓ na soma, ✗ na simetria (MÉDIO 6) |
| Mensagens (bônus 22) | 15 | 15 (01–15) | ✓ |
| Checklists (25) | 3 | 3 (dia · mês · antes de fechar convênio), 1 p. | ✓ |
| Modelos .pptx | 3 (8/10/8 slides) | 27 = 8 · 28 = 10 · 29 = 8 | ✓ |
| Manual (26) | "implantação em 4 semanas" | 22 p., 4 semanas (5+5+6+4 planilhas) | ✓ |
| Aulas | 8, "de 2 a 3 minutos" | 8 .mp4 + 8 .srt | ✓ (títulos idênticos em LEIA-ME × página × manual) |
| Bônus | 3 (mensagens, LGPD, contador) | 22 (8 p.) · 23 (10 p.) · 24 (4 p.) | ✓ |

**Fórmulas e formato** — 116.737 fórmulas nas 20 planilhas; **100 % com valor em cache** (o problema 12
da revisão do Advogados não se repete). Funções usadas: só do repertório 2007+ (IF, IFERROR, INDEX,
MATCH, COUNTIFS, SUMIFS, AVERAGEIFS, SUMPRODUCT, CHOOSE, LARGE, TEXT, FIXED…); **nenhuma MÍNIMOSES,
MÁXIMOSES ou UNIRTEXTO** — logo "Excel 2016 ou mais novo" (página, FAQ 5; LEIA-ME; e-mails) está certo.
Proteção de aba em 20/20 (86 abas). Aba "Como usar" em 20/20. `fullCalcOnLoad="1"` em todas.

**Durações medidas (ffprobe)** — 01: 2:48 · 02: 2:55 · 03: 2:44 · 04: 2:55 · 05: 2:57 · 06: 2:59 ·
07: 2:56 · 08: 2:57. Total 1.391 s = **23,2 min**. `site/config.json` traz `med_aula1..8_dur` = **"2:30 min"**
nas oito (ver GRAVE 3). Legenda .vtt da aula 5 gerada (51 cues, fim 2:55,89).

**Página (Playwright/Chromium, `python3 -m http.server` sobre `site/public`)** — 390×844, 1366×768
(+360 e 768 para quebra de texto): 0 erros de console, 0 respostas ≥ 400, 0 imagens quebradas;
`scrollWidth == clientWidth` nos quatro tamanhos (sem overflow horizontal); nenhum elemento além da
borda; todos os `href` internos resolvem 200 (`/`, `/kit/`, `/completo/`, `/advogados/`, `/medicos/`,
`/sobre/`, `/reembolso/`, `/suporte/`, `/termos/`, `/privacidade/`, `/cookies/`, `/#kits`,
`/#como-funciona`); âncoras `#conteudo` e `#preco` existem; vídeo com `poster` 200
(`poster-aula-05-960.webp`), `preload="none"`, `track` pt-BR `default`; 9 `<details>` na FAQ e o primeiro
abre ao clique em 390 e 1366; ordem das seções = cenarios → demo → metodo → planilhas → prompts-aulas →
para-quem → quem → preco → faq (idêntica à /advogados); heurística de contraste WCAG (4,5:1 / 3:1) sem
falhas em /medicos/, /obrigado/, /obrigado/pix/ e /obrigado/recusado/; **nenhum `.btn`, `.tag`,
`.tela__chips li`, `.hero__nota span`, `.tela__barra b`, `.aulas li span`, `.eyebrow` ou `.preco__valor`
quebra linha** em 390/768/1366 (só `.exemplo__rot` quebra em 360 px — ver LEVE 25). As 3 páginas de
obrigado: sem erro, sem overflow, sem imagem quebrada em 360/390/1366.

**Estrutura × /advogados** — `diff` dos atributos `class` das duas páginas: **zero diferenças**
(mesmas seções, mesmos modificadores `passos--5`, `inv--10`). Divergências de conteúdo em MÉDIO 8, 9,
10 e 15 e LEVE 16.

**Screenshots** em `/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad/revMC/`
(`p_medicos_390.png`, `p_medicos_1366.png`, `sec-390-*.png`, `sec-1366-*.png`, `p_obrigado*_390.png`,
`hero_med2.png`, `mock_*.png`, `poster05.png`).

---

#### GRAVE

1. **Planilha 14 `Parcelas particulares e inadimplência`, aba Config, célula A17 (texto que o comprador
   lê ao configurar a régua).** Visto: *"Regra que vale mais que a régua: quem tem parcela vencida em
   aberto não combina novo pagamento a prazo. **O próximo atendimento é à vista (Pix, dinheiro ou
   cartão) ou fica para depois de acertar o que está em atraso** — sem constrangimento e em particular."*
   Esperado: a regra deve valer só para **crédito novo**, como já está na planilha 15 (`Como usar` B7 e
   `Orçamentos` A308: *"Orçamento aprovado a prazo: só para quem não tem parcela vencida em aberto… o
   combinado é à vista"*). Como está, a planilha manda **adiar atendimento por dívida** — o kit
   contradiz o próprio bônus 22, que no roteiro do degrau 15 escreve, em letras: *"O que não dizer: …
   nada de negativação, juros ou **suspensão de atendimento**"*. Condicionar atendimento a pagamento é
   exatamente o que o médico não pode fazer (Código de Ética Médica; nunca em urgência, emergência ou
   continuidade de tratamento em curso) e é constrangimento na cobrança (CDC art. 42). É a frase mais
   perigosa do kit inteiro: sai do produto pago, em texto de instrução, para o médico executar.

2. **Página, `#quem` (linha 192 de `site/src/pages/medicos.html`).** Visto: *"**A tela real das vinte
   está nesta página**; cada arquivo tem versão e data de revisão."* Esperado: a página mostra **10 das
   20 telas** — herói (17 + 01), `mock-agenda` (01 + 02), `mock-preco` (05 + 06), `mock-caixa` (09 + 10),
   `mock-convenios` (13 + 14), `mock-painel` (17 + 20). Distintas: 01, 02, 05, 06, 09, 10, 13, 14, 17, 20.
   As planilhas 03, 04, 07, 08, 11, 12, 15, 16, 18 e 19 não têm nenhuma imagem na página. Afirmação
   objetiva e falsa no bloco de credibilidade, ao lado de "conferida célula a célula" (CDC art. 30/31 e
   política da Meta sobre alegações verificáveis). Trocar por "a tela real de dez das vinte" ou
   "uma tela real de cada núcleo". (A mesma frase está na /advogados e passou pela revisão anterior.)

3. **Durações das 8 aulas: `site/config.json` `med_aula1_dur`…`med_aula8_dur` = "2:30 min" (placeholder)
   publicado.** Visto na página: as oito linhas de `#prompts-aulas` mostram **"2:30 min" idêntico**, e a
   `figcaption` do vídeo diz *"Aula 5 · Quanto cobrar por este procedimento · 2:30 min"* logo abaixo de um
   player cuja duração real é **2:57**. Os e-mails repetem o mesmo número três vezes: D+0 *"aula 1 …
   (2 min 30 s)"* (real 2:48), D+1 *"A aula 3 … (2 min 30 s)"* (real 2:44), D+5 *"A aula 5 … (2 min 30 s)"*
   (real 2:57). Esperado: duração lida do arquivo. Oito durações iguais ao segundo já denunciam
   placeholder; o visitante que dá play confere em 3 segundos. A copy registra o placeholder
   (`04-copy/medicos.md`, "Grade das 8 aulas": *provisórias "2:30 min" até a gravação*), mas ele está no
   ar. Na regravação, derivar `config.json` e os e-mails por ffprobe, e conferir também o teto de
   "2 a 3 minutos": hoje a aula 6 tem 2:59.

4. **Anúncios do Médicos já renderizados narram "quarenta prompts".** Visto em
   `08-ads/criativos/medicos-15s-9x16.srt` (cue 17: *"Quarenta prompts, oito…"*) e
   `medicos-venda-9x16.srt` (*"vinte planilhas reais, **quarenta prompts**, oito aulas curtas e três
   modelos de apresentação"*) — e nos .mp4 correspondentes, que têm a narração gravada. Esperado: **41**,
   como já estão a página (5 lugares), a copy, a oferta, o LEIA-ME, o manual, a biblioteca e o e-mail
   D+0 do Médicos, e como já foi corrigido em `08-ads/criativos/carrossel/textos.md` linha 139. O anúncio
   pago passa a contradizer a página de destino. Ou os dois vídeos são regravados, ou a decisão de
   passar a 41 é revertida (ver MÉDIO 6).

---

#### MÉDIO

5. **Planilha 20 `Resumo do Mês`: 56 células com número em formato en-US no cache, e "Como usar" sem o
   aviso que a 12 tem.** Visto (valores gravados no arquivo): `Painel!B5` = **"R$ 49,651"**,
   `Painel!D5` = **"-7.1%"**, e o mesmo em todo o bloco Resumo (*"Margem do mês: 14.2%"*, *"R$ 2,700"*).
   Esperado: "R$ 49.651" e "-7,1 %". As fórmulas (`FIXED`/`TEXT`) estão certas e `fullCalcOnLoad="1"`
   faz o Excel e o Sheets recalcularem ao abrir — mas **toda pré-visualização** (Drive, Gmail, WhatsApp,
   Quick Look, visualizador do celular) mostra o cache, e a 20 é justamente a planilha cujo "Bloco único
   para copiar" a página manda colar na IA (`#prompts-aulas`, "Cole: Planilha 20 · aba Resumo"). A
   planilha 12 já traz o aviso em `Como usar` (*"A frase 'Contando o caixa livre' usa a função FIXED: os
   separadores se…"*) e mesmo assim guarda "R$ 26,836): 1.4 meses" em `Painel!G7`; a 20, com 56 células,
   **não tem aviso nenhum**. Recalcular em locale pt-BR antes de empacotar e repetir o aviso na 20.

6. **A biblioteca 21 passou a ter 41 prompts, mas o grupo Caixa ficou com 9 e os outros quatro com 8.**
   Visto: `Caixa 01, 02, 03, 04, 05, 06, 07, 08, 09` × `Agenda 01–08`, `Preço 01–08`, `Recebíveis 01–08`,
   `Painel 01–08`. O cabeçalho da biblioteca e o LEIA-ME dizem *"41 prompts em 5 grupos"* sem avisar que
   um grupo é maior. Esperado: ou 40 (5 × 8, o número redondo que a página, a copy, a oferta, os e-mails
   e os dois vídeos de anúncio usavam e que o índice sugere), ou 41 assumido em todos os lugares,
   inclusive nos criativos (GRAVE 4). "41" é um número que o comprador conta e estranha; "40 em 5 grupos
   de 8" é o que a arquitetura do kit promete.

7. **Página `#cenarios`, dor 1 (linha 47): nome de planilha que não existe, e três "e" seguidos.**
   Visto: *"**Com o kit:** Agenda e Ocupação **e** Faltas **e** Remarcações."* Esperado: a planilha 02 se
   chama **"Faltas, remarcações e lista de retorno"** (título interno), o arquivo é
   `02-faltas-e-retornos.xlsx` e o LEIA-ME a lista como "Faltas e retornos" — **três nomes para o mesmo
   arquivo**, e a página inventa um quarto ("Faltas e Remarcações"). Além disso, a frase encadeia dois
   nomes de arquivo com "e" sem pontuação, e sai ilegível. A /advogados resolve a mesma linha com uma
   frase ("Agenda de Prazos com semáforo por dias e a rotina de segunda"). Fixar um nome canônico por
   planilha e usar em LEIA-ME, título interno, página e manual.

8. **A página afirma que os prompts funcionam nas IAs gratuitas sem a ressalva de terceiros que a
   /advogados tem.** Visto em `#prompts-aulas`, lead: *"…e funcionam nas versões gratuitas do ChatGPT,
   Copilot, Gemini e Claude."* Esperado: a /advogados carrega isso numa FAQ com a ressalva —
   *"Preciso pagar ChatGPT ou outra IA? Não. Os prompts funcionam nas versões gratuitas **atuais**.
   ChatGPT, Copilot e Gemini são **serviços de terceiros, com regras próprias**."* A /medicos apagou a
   FAQ e manteve só a afirmação, que é sobre o plano gratuito de quatro empresas que podem mudá-lo
   amanhã. Divergência do padrão sem motivo e afirmação sem qualificação (CDC art. 30).

9. **A página não faz nenhuma ressalva de CFM/CRM sobre as 15 mensagens ao paciente, embora o produto
   faça.** Visto no card de bônus: *"15 mensagens de confirmação, lembrete e cobrança: confirmação de
   consulta, **lembrete da véspera**, falta e remarcação, **retorno**, cobrança educada em degraus…
   Mensagens de rotina da recepção, não peças de divulgação."* Esperado: a própria biblioteca 21 (Agenda
   03) e o bônus 22 avisam *"Se a mensagem for usada para um grupo grande de pacientes, revise pelas
   regras do CFM/CRM antes de usar"*, e o modelo 15 do bônus é *"pedido de opinião privada"*, com
   advertência explícita sobre a Resolução CFM 2.336/2023. A página é o único lugar onde um médico
   decide comprar e não vê essa fronteira. Uma linha ("mensagens individuais de rotina; qualquer uso em
   massa ou público segue as regras do CFM e do seu CRM") resolve e é o guardrail que o Eduardo listou.

10. **Página `#preco`, `.preco__anc`: comparação sem fonte e com margem de 6 %.** Visto: *"Menos que um
    ano de um software de clínica típico, uma vez, e os arquivos ficam com você."* R$ 697 ÷ 12 =
    **R$ 58/mês**. A pesquisa do próprio projeto (`01-pesquisa/saas-precos.md`, 12/09/2026) registra
    Clínica Experts a **R$ 62** (× 12 = R$ 744, apenas R$ 47 acima do kit) e, na mesma lista, **"R$ 18"**
    em Corpora. Esperado: ou citar a referência na página, ou usar um recorte com folga. A /advogados,
    revisada, usa *"menos que **três meses** de um software jurídico típico"* (R$ 166/mês contra um
    mercado de R$ 220 a R$ 1.800) — folga de 3×. Esticar para "um ano" só para o número fechar é
    publicidade comparativa sem sustentação (CDC art. 37 § 1º; política da Meta).

11. **Manual 26, seção 1, linha da pasta `videos/`.** Visto: *"8 aulas de 2 a 3 minutos, tela real,
    narração e legenda | **cerca de 20 min no total**"*. Esperado: **23,2 min** (1.391 s medidos). Repor
    depois da regravação, junto com o GRAVE 3.

12. **Herói, inventário e criativos não são regenerados por `site/build.py`: ficaram ~2 h defasados das
    planilhas durante esta revisão.** Visto às 23:04: o herói (`08-ads/criativos/medicos-produto-hero-1600x1000.png`,
    de 21:34) e `mock-painel.webp` (21:35) mostravam **Entrou R$ 21.570 · Sobrou R$ 7.940 · Vencido
    R$ 4.550 · Inadimplência 10,5 % · Lista de retorno 7 · Orçamentos "Fora"**, enquanto
    `17-painel-da-clinica.xlsx` (23:07) já dizia **21.920 · 8.290 · 3.775 · 9,4 % · 8 · Informativo**.
    Corrigido por outro agente às 23:15–23:20 e reconferido: o herói atual bate com a planilha. Fica a
    causa: `build.py` só otimiza as imagens; quem as deriva são `assets_produto.py`, `mockups_cards.py`
    e `heroi_poster.py`, que ninguém é obrigado a rodar. A página promete "Telas reais" — precisa de uma
    trava (rodar os três no build, ou falhar se a planilha for mais nova que o `.png` de origem).

13. **`/obrigado/`, card "Primeiros 7 dias": os quatro kits empilhados, 16 itens.** Visto: Essencial →
    Completo → Advogados → **Médicos** (quarto bloco). Quem pagou R$ 697 rola três roteiros alheios até
    achar o seu, e vê que comprou "um dos quatro". Esperado: a Kiwify manda o produto na URL de retorno —
    filtrar o bloco, ou ao menos ancorar. (A revisão do Advogados já apontou o problema; ele cresceu com
    o quarto kit.)

14. **E-mail D+0, `05-checkout/emails.md`, cabeçalho comum × bloco Médicos.** Visto: *"POR ONDE COMEÇAR
    (**15 minutos**)"* seguido de *"1. Abra o '26-manual-de-implantacao.pdf' (**20 minutos de leitura**)
    e assista à aula 1 … 2. Abra '05-custo-da-hora.xlsx' … **quinze minutos** e você sabe quanto custa a
    sua hora"*. Esperado: os próprios passos somam ~38 min. O "(15 minutos)" é herdado do Essencial.
    Trocar por "(primeiro dia)" ou pelo tempo real.

15. **Poster do vídeo com legenda queimada, ao contrário da /advogados.** Visto em
    `site/public/assets/medicos/poster-aula-05.jpg`: o quadro escolhido tem a legenda do vídeo por cima
    da tela — *"Praticado, quatrocentos e cinquenta; margem de cinquenta e quatro por cento."* — e a
    tabela cortada à direita ("Saú…"). Esperado: quadro limpo, como o poster da /advogados
    (`assets/advogados/poster-aula-05.jpg`, tela inteira, sem legenda). Causa: `site/heroi_poster.py`
    corta sempre em 35 % da duração (`t = min(dur*0.35, 60)`), sem verificar se há legenda no quadro.
    Escolher o segundo à mão ou cortar num intervalo sem cue do .srt.

---

#### LEVE

16. Página `#metodo`: "doze minutos na segunda, dezoito na sexta" aparece **três vezes na mesma seção** —
    lead (*"Doze minutos na segunda, dezoito na sexta."*), passo 1 (*"A rotina de segunda confere a semana
    em 12 minutos."*) e passo 5 (*"Sexta-feira, 18 minutos."*). A /advogados diz uma vez, só no lead.
17. Página `#cenarios`, dor 3: *"Caixa com provisão **e** Repasse **e** Pró-labore separados."* Três "e"
    e concordância ambígua ("separados" vale para os três itens ou só para os dois últimos?). A
    /advogados: "Caixa com provisão e Pró-labore separado."
18. Página `#planilhas`, card 1: *"…rotina de segunda **e** sexta **e** checklist de abertura **e**
    fechamento do dia."* Quatro "e" numa linha; trocar um por ponto e vírgula.
19. Página `#preco`: *"Menos que um ano de um software de clínica típico, **uma vez**, e os arquivos ficam
    com você."* O "uma vez" é herdado do molde do Advogados ("menos que três meses… uma vez") e, colado a
    "um ano", fica solto.
20. Títulos internos das planilhas: 17 **"Painel da Clínica"**, 18 **"Resultado Mensal"**, 19 **"Metas do
    Trimestre"**, 20 **"Resumo do Mês"** em caixa-alta de título, contra 01–16 em frase ("Agenda e
    ocupação por profissional e sala", "Caixa da clínica"). São as quatro herdadas do Kit Advogados.
21. `02-oferta/medicos.md` linha 102: *"convênios e **recebíveis** para o contador (8)"* × LEIA-ME
    *"convênios e **caixa** para o contador"* × arquivo `29-modelo-**convenios**-para-o-contador-8-slides.pptx`.
    Três nomes para o mesmo modelo.
22. `/obrigado/`, bloco Médicos: Dia 1 *"o 05 Custo da hora de atendimento … (15 min)"* × manual, semana 1,
    *"20 para o custo da hora"*. E Dia 3 *"06 Precificação e 07 Simulador convênio × particular … (**aula 5**)"*
    quando a 07 é assunto da **aula 4** ("Preço e simulador de convênio"); o manual manda ver as duas.
23. Rodapé de todas as páginas: *"Última atualização 13 de setembro de 2026"* numa página publicada em 14/09.
24. `mock-agenda.webp` (inventário, card "1 · Agenda"), bloco "Por dia da semana e período": a linha
    **Segunda** aparece com 0 horas disponíveis e 0 atendidas. Está certo (07/09 é feriado e hoje, 14/09,
    ainda não entrou em "disponíveis até ontem"), mas numa tela pública, ao lado de "a rotina de segunda
    confere a semana em 12 minutos", lê-se como erro. Considerar outra data de referência ou outro recorte.
25. `.exemplo__rot` *"As 8 aulas · tela real, narração e legenda"* quebra em duas linhas a **360 px**
    (a 390 px, não). Mesmo comportamento na /advogados; é rótulo, não chip.
26. Planilha 20, `Como usar` B15: *"Fórmulas, listas, cores e **gráficos** funcionam."* A 20 não tem gráfico.
27. Planilha 17, herói da página, linha *"Pacientes na lista de retorno · 8 · limite 8 · **No alvo** · mês
    anterior 4 · +100,0 %"*: o cartão fica verde no mês em que a lista **dobrou**, porque o limite é "8" e a
    regra é "menor é melhor" sem empate. Rever o limite do exemplo ou tratar "igual ao limite" como
    "perto do limite" (amarelo).
