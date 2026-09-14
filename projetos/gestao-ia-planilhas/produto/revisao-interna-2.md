# Revisão interna 2 · Kit de Gestão para Advogados (14/09/2026)

Três revisores independentes (agentes Claude) abriram a entrega como cliente, sem alterar nada: A (planilhas 01–20),
B (documentos 21–29 e LEIA-ME), C (aulas, página, obrigado, e-mails, copy). Este arquivo guarda os três relatórios na
íntegra e a triagem. Correções aplicadas ficam marcadas em `## Triagem e correções`.

Leitura rápida: as fórmulas estão certas (23.499 fórmulas, 0 erros nas 20 planilhas), as contagens prometidas na página
existem (20 planilhas, 40 prompts, 15 mensagens, 3 checklists, 3 modelos, 8 aulas), mas o EXEMPLO do escritório
fictício não fecha entre arquivos: setembro tem quatro versões (caixa 09 × painel 17/DRE 18/resumo 20 × prompts 21 ×
slides 27/29), horas e funil divergem entre 16/17 e 07/15, e os documentos herdaram números e grade de aulas antigos.

## Triagem e correções

Legenda: **Aceito** (aplicar como está) · **Adaptado** (aplicar de outro jeito) · **Adiado** (depende do Eduardo ou de
conta externa) · **Rejeitado** (não faz sentido para nós). Coluna "Feito" preenchida em 14/09/2026 (rodada de correções com 6 agentes: site, dados/planilhas, documentos, aulas).

### Decisões de história (valem para todos os arquivos)

| Decisão | Motivo |
|---|---|
| Referência HOJE = seg 14/09/2026; "sexta do painel" = 11/09; nenhum lançamento pago depois de 11/09 | A-9, C-7 |
| 17 Painel de sexta = semana de 11/09 com setembro em andamento, copiado dos painéis de 09/16/13/14/15/01; Histórico jan–ago do caixa real | A-1, A-3 |
| 18 Resultado e 20 Resumo analisam o último mês fechado: agosto (× julho) | A-1, B-G1 |
| Receita por modalidade em 18 = categorias reais dos lançamentos da 09; alíquota única 8 % | A-2, A-6 |
| dados.py vira fonte única de casos, propostas, parcelas, lançamentos e horas; 09 × 13 × 14 × 15 × 07 derivam dela | A-4, A-10, A-14 |
| Inadimplência = vencido ÷ (pago + vencido) em todo o kit; hora mínima = conta da 05 (R$ 110), a 08 chama a sua de "hora mínima com folga" | A-5, A-7, C-8 |
| Prompts 21, slides 27/29, manual 26 e aulas usam os números de `kit-advogados/NUMEROS.md` (gerado das planilhas recalculadas) | B-G1, C-7 |
| Títulos das aulas = os das capas dos vídeos, em todos os lugares | B-L5, C-6 |
| Slides 27/28/29: marca só no slide mestre, rodapé "modelo" só nas notas; 28 sem custo-hora/margem/planilhas internas | B-G2, B-M1 |
| Manual 26: 20 planilhas distribuídas nas 4 semanas (04 na semana 1), aula certa por semana, lista dos 8 títulos, capturas recortadas com legenda | B-G3, B-M6, C-3 |
| Página: prompt Painel 01 literal; 12/18 min; sem "mais barato"; obrigado neutro entre kits; e-mails com bloco Advogados completo; Excel 2019 | B-G6, C-2, C-4, C-9, C-10, C-13 |

### Tabela de triagem

| Achado | Decisão | Feito |
|---|---|---|
| A-1 a A-4 (setembro, DRE, horas, funil) | Aceito: refatoração de dados.py + builders | Sim: dados.py fonte única; verifica_coerencia.py 251 OK |
| A-5 a A-18 | Aceito (A-12 Excel 2016: adaptado, trocar onde não pesar; o que ficar exige 2019 e o "Como usar" diz qual aba) | Sim (A-12: nenhuma função pós-2007 sobrou; Excel 2016 em todo o kit) |
| A-19 a A-30, A-32 | Aceito | Sim |
| A-31 (página 15/15 min, oferta "38 ativos") | Aceito na página e na oferta | Sim |
| B-G1 (quatro setembros) | Aceito via NUMEROS.md | Sim: prompts, slides, manual e aulas com NUMEROS.md |
| B-G2 (marca nos slides) | Aceito | Sim: marca no mestre, "modelo" só nas notas |
| B-G3 (manual: 04 fora, aulas trocadas) | Aceito | Sim: 01–05 / 06–10 / 11–16 / 17–20, aulas certas, lista das 8 aulas |
| B-G4, B-G5, B-M3, B-M13, B-L2, B-L3 (páginas vazias e órfãos nos PDFs) | Aceito | Sim: PDFs 23 (8 p.), 24 (4 p.), 21 e 22 sem órfãos |
| B-G6 / C-2 (prompt da página) | Aceito: texto literal | Sim |
| B-M1 (28 expõe custo-hora) | Aceito | Sim: 28 só com horas e valor por etapa |
| B-M2 (29 aba Vencidos; dados de cliente ao contador) | Aceito: anexo só com totais | Sim: anexos ao contador só com totais |
| B-M4 (TXT com Markdown cru) | Aceito: txt limpo | Sim: 21 e 22 em txt limpo |
| B-M5 (metadados dos PDFs) | Aceito | Sim |
| B-M6, B-M7 (capturas do manual; exemplo da 17) | Aceito | Sim: recortes com legenda; 17 copia dos painéis |
| B-M8 / C-17 (régua de cobrança em três versões) | Aceito: a régua da 14 manda; 22 e 27 seguem | Sim: régua da 14 em 22 e 27 |
| B-M9 (avaliação pública, OAB) | Adaptado: modelo 15 vira pedido de feedback privado, com aviso de revisar pelo Provimento 205/2021 | Sim (adaptado) |
| B-M10 (recibo sem nota) | Aceito: nota fiscal obrigatória; e-mail é só confirmação; 24 trata regularização | Sim: 28 só com horas e valor por etapa |
| B-M11 (13º dos sócios, recesso) | Aceito: "reserva de fim de ano decidida pelos sócios" e "reserva de janeiro (receita menor)" | Sim: 28 só com horas e valor por etapa |
| B-M12 (22 em PDF + txt) | Aceito: gerar txt | Sim: 28 só com horas e valor por etapa |
| B-L1 / C-24 (manual 18 p. × oferta 20–30) | Adaptado: oferta passa a dizer "cerca de 20 páginas" | Sim: manual com 20 p.; oferta "cerca de 20 páginas" |
| B-L4 (estagiária R$ 700 por 20 h) | Aceito: R$ 467 | Sim |
| B-L6 (ANPD 3 dias úteis) | Aceito | Sim |
| B-L7 (descrição das 15 mensagens na página) | Aceito: descrever os 5 grupos | Sim |
| B-L8, B-L9 | Aceito | Sim |
| B-L10 ("tela real" × recorte) | Rejeitado: é a planilha real renderizada; a página não promete janela do Excel | — |
| C-1 (aula 5: 66,07 × 53 = 3.952) | Aceito: 3.501,71 + R$ 450 de despesas = 3.951,71, narrado assim | Sim: aulas 4 e 5 |
| C-3 (manual aulas) | Aceito | Sim |
| C-4 (e-mails) | Aceito | Sim (Excel 2016 no Advogados) |
| C-5 (capa das aulas 2 e 4) | Aceito: kicker fixo no rodapé | Sim: kicker fixo |
| C-6 (títulos) | Aceito | Sim: títulos das capas em página, LEIA-ME, manual, e-mails, copy |
| C-7, C-8 | Aceito via NUMEROS.md e narração da aula 4 explicando a folga | Sim |
| C-9, C-10, C-11, C-13 | Aceito | Sim |
| C-12 (valores em cache) | Adaptado: testar re-salvar com LibreOffice; aplicar só se a fidelidade for boa | Sim: aulas 4 e 5 |
| C-14 (enquadramento aulas 2, 5, 7) | Aceito | Sim: aulas 4 e 5 |
| C-15 (fase × ação) | Aceito (dados.py) | Sim: aulas 4 e 5 |
| C-16 (TEXT em locale) | Aceito: nota no Como usar; texto via FIXED/SUBSTITUTE | Sim: aulas 4 e 5 |
| C-18, C-19, C-20, C-21 | Aceito (quadro inicial, −1 dBTP, cues curtos, arredondamentos) | Sim: aulas 4 e 5 |
| C-22, C-23, C-25, C-26, C-27 | Aceito | Sim |
| Teste em Excel e Google Sheets reais | Adiado: Eduardo | Adiado |
| Narração definitiva | Adiado: chave do Google TTS | Adiado |


## Relatório A · planilhas 01–20

Revisor A · 14/09/2026 · Cópias em `scratchpad/revA/recalc/` (originais intactos). Método: recalc com LibreOffice
(`recalc.py <cópia> 240`), leitura com openpyxl em dois modos (fórmulas e `data_only`), recálculo manual de 2–3
números por painel, cruzamento de casos/pessoas/valores entre os 20 arquivos contra `dados.py`, checagem de
células amarelas × bloqueio, listas suspensas, funções, textos e promessas da página `advogados.html` e de
`02-oferta/advogados.md`.

### Testes feitos

| Arquivo | Fórmulas | Erros (#N/A, #REF!, #DIV/0!, #VALUE!, #NAME?) |
|---|---|---|
| 01-agenda-de-prazos | 1.465 | 0 |
| 02-andamento-por-processo | 1.833 | 0 |
| 03-rotina-da-semana | 595 | 0 |
| 04-checklist-abertura-e-encerramento | 2.389 | 0 |
| 05-custo-hora | 150 | 0 |
| 06-simulador-de-honorarios | 71 | 0 |
| 07-proposta-de-honorarios | 263 | 0 |
| 08-tabela-de-referencia | 1.401 | 0 |
| 09-caixa-do-escritorio | 1.643 | 0 |
| 10-provisao-de-impostos | 189 | 0 |
| 11-pro-labore | 987 | 0 |
| 12-reserva-e-metas-de-caixa | 230 | 0 |
| 13-carteira-de-clientes-e-casos | 1.573 | 0 |
| 14-parcelas-e-inadimplencia | 4.585 | 0 |
| 15-funil-de-propostas | 2.068 | 0 |
| 16-horas-por-caso | 3.333 | 0 |
| 17-painel-do-escritorio | 143 | 0 |
| 18-resultado-mensal | 244 | 0 |
| 19-metas-do-trimestre | 144 | 0 |
| 20-resumo-do-mes | 153 | 0 |

Outras verificações automáticas (20 arquivos): nenhuma célula amarela bloqueada; nenhuma fórmula desbloqueada fora
das datas-exemplo `=TODAY()±n` (que são amarelas de propósito); nenhum XLOOKUP/FILTER/SORT/UNIQUE/LET; nenhum "Sheet1",
TODO, placeholder ou texto em inglês; todas as abas protegidas sem senha; título A1 cabe na mesclagem em todas as abas;
listas suspensas com OFFSET/COUNTA (sem "" no meio); 38 casos, 18 clientes, 3 pessoas, custo-hora 66,07, pró-labore
12.000 e custos fixos 6.500 batem com `dados.py` em 01, 02, 04, 08, 13, 14, 16 (número, cliente, área, fase,
responsável, modalidade, contratado, recebido, horas). Recalculei à mão e conferiram: 01 (33 abertos = 20+11+2; 21
urgentes), 02 (30 ativos por fase/área/responsável), 03 (aderência 30/36 = 83 %; 30 min/semana), 04 (12 pendências),
05 (18.500/280 = 66,07; 66,07/(1−0,30−0,08) = 106,57 → 110), 06 (misto 4.500 + 15 %×33.000 = 9.450; margem 4.742,29),
07 (28.800 fechado; 20.600 em aberto), 08 (5 áreas somam 38 casos e 374.200), 09 (saldo 22.000 + 200.920 − 182.125 =
40.795), 10 (Set: 10.800×8 % = 864), 11 (1º tri 4.619×50 % = 2.309,50 = 1.155×2 pagos), 12 (43.500/3.000 = 14,5 meses →
Dez/2027), 13 (374.200 / 245.920 / 128.280), 14 (26.590/(26.590+126.350) = 17,4 %), 15 (7/(7+5) = 58 %), 16 (Ago 282,5 h;
216,5/280 = 77 %), 19 (semana 11 de 13; 82 %; média 53 %), 20 (bloco de texto coerente com Indicadores).

Os problemas abaixo são, na maioria, de **coerência entre planilhas** e de **exemplo que não fecha**; as fórmulas
em si estão certas.

#### GRAVE

1. **17, 18 e 20 usam um "setembro" que não existe no caixa (09).** `17 Dados!B10` = 29.400 (Entrou no mês),
   `17 Dados!B11` = 20.264, `17 Histórico!G13:H13` idem, `18 Resultado!J10` = 29.400 e `J26` = 20.264,
   `20 Indicadores!G5:G7` = 29.400 / 20.264 / 9.136. No caixa, `09 Painel!A5` (Setembro, Pago? = Sim) = **10.800**,
   `C5` = 5.970, `E5` = 4.830; e as planilhas 10 (`Entradas e pagamentos!B13` = 10.800), 11 (`Resultado mensal!B13`
   = 10.800) e 12 (`Config!C27` = 67.630 = 30.170 + 26.660 + 10.800) seguem o caixa. `17 Dados!E10` manda "copiar de
   09 · Caixa (Painel)" e `18 Resultado!A31` afirma que "os valores de exemplo batem com o Caixa (09)": não batem.
   O "painel de sexta em uma tela" prometido na página mostra um caixa de setembro 2,7× maior que o caixa do kit,
   na mesma data (14/09/2026). O mesmo vale para "Saiu no mês" de janeiro a agosto: `17 Histórico!H5:H12` (20.520,
   19.340, 19.674…) copia a 18 (custos + pró-labore + provisão de 6 %), não o caixa (`09 Painel!C80:C87` = 20.408,
   22.273, 22.200…), embora o rótulo em `17 Dados!E11` diga "09 · Caixa do escritório (Painel)".
2. **18 (DRE) e 19 inventam uma receita por modalidade que o caixa não tem.** `18 Resultado!B6:J9` (fixos / hora /
   êxito / consultivo mensal) não corresponde às categorias de `09 Lançamentos`: janeiro em 09 = fixos 18.560, hora
   13.300, consultoria 1.800, êxito 0; em 18 = 13.360 / 8.200 / 9.100 / 3.000 (só o total 33.660 coincide). No ano:
   êxito 09 = 15.800 × 18 `N8` = 53.000; "Consultivo mensal (recorrente)" 18 `N9` = 41.700 × 09 "Consultoria e
   pareceres" = 22.200, todos avulsos. `19 Metas!G5` = "5 contratos de consultivo mensal ativos" e `G6` = 7.200
   de receita recorrente: a carteira (13) tem 4 casos Consultivo, todos de valor único, e 09 não tem nenhuma
   entrada recorrente de consultivo.
3. **Horas do painel (17/20) não existem em 16.** `17 Dados!B7:B8` = 318 h / 226 faturáveis (Setembro) e
   `17 Histórico!D12:E12` = 298 / 232 (Agosto); `20 Indicadores!F9:G10` idem. Em `16 Lançamentos` (255 linhas,
   01/07 a 14/09): agosto = **282,5 h / 216,5 faturáveis** (`16 Painel!A5` e `C5`), setembro = 184,5 / 149. `17
   Dados!E7` manda "copiar de 16 · Horas por caso (Painel)": nenhum dos quatro números está lá.
4. **07 Registro e 15 Propostas são dois funis diferentes do mesmo escritório, na mesma data.** `07 Registro!A9:K18`
   tem 10 propostas (4 fechadas = 28.800; 3 enviadas = 20.600); `15 Propostas!A5:K24` tem 20 (7 fechadas = 52.400;
   8 abertas = 68.400). Contradições diretas: Ana Beatriz Moreira 6.000 **Perdida** em 07 (`J10`) × **Fechada** em
   15 (`G6`); Loja Verde 14.400 Perdida (07 `J13`) × 7.200 Fechada (15 `G9`); Fernanda Castro 7.000 Fechada (07 `J14`)
   × 6.500 Perdida (15 `G13`); Construtora Horizonte 12.000 "Disputa sobre contrato de obra" (07) × 12.500 "Cobrança
   judicial" (15); Bistrô 42 8.500 × 5.200; Roberto Almeida 4.500 Enviada hoje (07 `A18`, é a proposta da aba
   Proposta) não existe em 15, que tem Roberto 9.800 Perdida. `17 Painel!A11/C11` (8 propostas / 68.400) e `20`
   seguem a 15; quem preencher a 07 (a planilha "Proposta de honorários" da página) nunca chega a esses números.
   Além disso, as propostas "fechadas" de jun–ago/2026 em 07 e 15 não viram casos na carteira 13 (nenhum caso de
   Construtora, Loja Verde ou Escola Aurora aberto em 2026).

#### MÉDIO

5. **"Inadimplência" tem duas definições.** `14 Painel!A7`: vencido ÷ (pago + vencido) = 26.590/152.940 =
   **17,4 %** (`K5`). Mas `17 Dados!A15`, `17 Painel!A25`, `19 Metas!B8` e `20 Indicadores!A14` chamam o mesmo 17,4 %
   de "vencido ÷ parcelas em aberto"; com as parcelas em aberto de 14 (`E5` = 66.050) daria **40,3 %**. O contador
   vai perguntar qual é.
6. **Alíquota de impostos: 8 % em 05/06/08/09/10, 6 % em 18.** `18 Config!B7` = 6,0 % ("Impostos provisionados"),
   `10 Config!B8` = 8,0 %, `05 Config!B8` = 8 %, `06 Config!B7` = 8 %, `08 Config!B8` = 8 %, e as guias em
   `09 Lançamentos` (ex.: 20/02 = 2.693 = 33.660 × 8 %) usam 8 %. Resultado: `18 Resultado!J25` provisiona 1.764 em
   setembro, `10 Painel!C17` separa 864 sobre 10.800 e 2.352 se fosse sobre 29.400. Margem de 18 (`G5` 31,1 %) está
   inflada por isso.
7. **Três "hora mínima" diferentes para o mesmo escritório.** `05 Painel!G5` = R$ 110,00 (exata `B16` = 106,57);
   `06 Simulador!I5` = 106,56 (custo-hora digitado 66,07 arredondado); `08 Referência!A5` = **127,88** (`08
   Config!B12` = 66,07 × 1,20 ÷ (1 − 0,08 − 0,30), com "folga de 20 %" que 05 e 06 não têm). Em 08, 2 casos ficam
   "abaixo do mínimo" (`E5`) que em 05 estariam acima. Nada explica ao usuário por que o mínimo mudou de nome e de
   valor entre a planilha 5 e a 8.
8. **Exemplo com combinações fase × próxima ação que um advogado não aceita** (`02 Processos`, repetidas em
   `01 Prazos`): Padaria do Sol 9236009 fase **Inicial** → "Protocolar: cumprimento de sentença" (`02 Processos!D5/F5`);
   Patrícia Gomes 3118925 Inicial → cumprimento de sentença (`D34/F34`); Fernanda Castro 4112092 Inicial → alegações
   finais (`D28/F28`); Helena Duarte 1808451 **Execução** → contestação (`D22/F22`); Carlos Eduardo 6904743 Sentença →
   contestação (`D26/F26`); Bistrô 42 8875326 e Escola Aurora 7658179 **Acordo** → contrarrazões; Ana Beatriz 3930894
   Acordo → alegações finais; Agência Prisma 9717671 Recurso → audiência de instrução. Os 4 casos "Consultivo" têm
   número CNJ e observação "Sem movimentação; verificar andamento" (`02 Processos!I5`, `I9`, `I11`). Origem:
   `dados.py` sorteia fase e prazo sem relação. Mina a credibilidade do exemplo logo na planilha 1 e 2.
9. **Caixa com dinheiro "recebido" em datas futuras.** `09 Lançamentos` com Pago? = Sim e data depois de 14/09:
   15/09 Oficina Mecânica 1.500 (entrada), 15/09 Anuidades 250, 18/09 Material 380, 20/09 Marketing 400, 22/09
   Padaria do Sol 2.600 (entrada). `09 Painel!A5` (10.800) e a meta `12 Config!C27` (67.630) já contam 4.100 que
   ainda não entraram na data do painel.
10. **09 × 13: clientes receberam em 2026 mais do que a carteira diz que já receberam na vida.** Oficina Mecânica
    Central: `09 Painel!C59` = 23.500 × recebido em 13 (`Casos`, 2 casos) = 16.500; Escola Aurora `C57` 23.900 ×
    22.300; Transportadora Rota Sul `C55` 15.520 × 12.620; Bistrô 42 `C51` 6.500 × 4.600. Causa: 09 lança parcelas de
    um caso "Encerrado em 2025" (12 × 1.500 da Oficina) e "Consultivo avulso" (pareceres) que não existem em 13.
11. **16 está em agosto; o resto do kit está em setembro.** `16 Config!B6` = "Agosto" → `16 Painel!A1` "Horas por
    caso · Agosto de 2026" e "Por pessoa em Agosto" (`A21`), com lançamentos até 14/09. O único painel do kit fora da
    data de referência; combinado com o item 3, o usuário não consegue ligar 16 a 17.
12. **Funções que não abrem no Excel 2016** (viram #NAME?): `_xlfn.MINIFS` em 01 (20×, `Painel!G28:G37`) e 02
    (20×), `_xlfn.MAXIFS` em 03 (1×) e 13 (120×, `Clientes`), `_xlfn.TEXTJOIN` em 04 (300×, `Checklist!AD5:AD304`).
    "Como usar" diz "Excel 2019 ou mais novo" e a página avisa que "algumas funções pedem Excel 2019"; mas a
    convenção interna pede 2016 e há alternativa simples (coluna auxiliar + MIN/MAX; concatenação por IF) para 01,
    02, 03 e 13.
13. **Variação de indicadores em % mostrada como % relativa.** `20 Resumo!A11` "Margem do mês: 31.1% (+26% em relação
    a Agosto)", `A13` "Horas faturáveis: 71.1% (−9%)", `A17` "Inadimplência: 17.4% (+2%)"; `17 Painel!G19` = −9 %,
    `G25` = +2 %. A 18 faz certo (`Painel!E15` em "p.p."). Para o sócio, "+26 %" de margem é outra coisa.
14. **Cadastro de casos repetido em 7 arquivos, sem uma fonte declarada.** Os 38 casos são digitados em 01, 02, 04,
    08, 13, 14 e 16 (`14 Casos!A2` e `16 Casos!A2` dizem "copie da 13"; 01, 02, 04 e 08 não dizem de onde). Trocar
    uma fase, um valor ou um responsável exige abrir sete planilhas; nada no kit avisa isso nem diz a ordem.
15. **Metas de caixa com prazo relativo que só faz sentido hoje.** `12 Config!D26` = `=TODAY()+108` (mostra
    31/12/2026 hoje; amanhã 01/01/2027), `D27:D28` = `=TODAY()+16` (30/09/2026 hoje; 07/10 na semana que vem) para
    metas rotuladas "no trimestre" e "Reserva com 1 mês... até 31/12". `12 Painel!G37:G39` ("Dias restantes") nunca
    diminui. Aqui a data fixa é a certa.
16. **01 Painel esconde 6 dos 21 prazos urgentes.** `01 Painel!A5:E5` = 7 atrasados + 3 hoje + 11 em 7 dias; a lista
    "O que vence primeiro" (`A10:H24`) mostra 15 (`A8` avisa), então 6 prazos da semana só aparecem como contagem em
    `D43:G49`. Na planilha que promete "o que vence primeiro", 15 linhas é pouco: 30 caberiam.
17. **"A receber" tratado como "menor é melhor".** `17 Dados!D13` = "Menor é melhor" e `20 Indicadores!E12` = "Não"
    para "A receber (carteira)" 128.280 com meta 120.000 → semáforo "Perto"/"Acima da meta" (`17 Painel!E23`,
    `20 Painel!G12`). Na 13, 128.280 inclui 36.000 de êxito de casos ativos (que não é atraso). Um sócio lê como
    problema o que é carteira contratada.
18. **08 e 14 deixam colunas auxiliares visíveis.** `08 Nossos casos!L5:L204` "Ordem" (formato 0,00, todas 0,00 ou
    0,00…30) e `14 Parcelas!N5:N404` (valores como 99.994,0) estão visíveis; as equivalentes em 01 (`J`), 02 (`N`),
    04 (`AE`), 13 (`K`), 14 (`M`), 15 (`R`) e 16 (`M`) estão ocultas.

#### LEVE

19. Abril tem dois totais: `09 Painel` (mês a mês) e `18 Resultado!E10` = 20.900 (inclui 480 de "Outras entradas",
    a devolução da sócia em `11 Retiradas`); `10 Entradas e pagamentos!B8` = 20.420 e `11 Resultado mensal!B8` = 20.420
    (sem os 480). No ano, `10 !B17` = 200.440 × `09 Painel!E41` = 200.920, embora `10 !A2` mande copiar "o total do
    Painel da planilha 09".
20. `01 Prazos` atribui 3 prazos a Júlia Prado (`E5:E404`, casos 9717671, 8735513, 8986364) e `02`, `04` e `13`
    mostram Júlia com 0 casos (`02 Painel!B25`, `04 Painel!C45`, `13 Painel!B24`). Possível, mas não explicado.
21. `02 Painel!G23:G24` "Ação mais próxima" = 11/09/2026 (já passada) para os dois sócios: o rótulo sugere futuro.
22. Textos montados por `&` sem formato pt-BR: `06 Simulador!H53` "Hora mínima sem prejuízo: R$ 81.04 (você cobra
    R$ 130)", `06 K52`, `12 Painel!G7` "Contando o caixa livre (R$ 26062): 2.1 meses". No Excel pt-BR a vírgula vem
    certa, mas o milhar não (R$ 26062).
23. `20 Painel!B5:C16` e `E5:E16` com formato fixo `#,##0.00`: "7,00" prazos atrasados, "30,00" casos, "31,10"
    margem; `Indicadores!C` (casas decimais) só é usado no texto do Resumo. Mesmo achado da revisão 1 (item 16).
24. `06 Simulador!I5` = 106,56 × `05 Painel!B16` = 106,57 (66,07 digitado em `06 B11` em vez de 66,0714): 1 centavo
    de diferença entre duas planilhas que se dizem a mesma conta.
25. `05 Painel!I5` "Ocupação da equipe" = 64 % (faturáveis ÷ horas de trabalho) e `16 Painel!G5` "Ocupação da equipe"
    = 77 % (faturáveis lançadas ÷ meta): mesmo nome, contas diferentes.
26. `03 Config!B6` = 05/01/2026 fixo e `Rotina!E3:BD3` são só 52 semanas de 2026; em janeiro de 2027 o painel "Semana
    atual" passa de 52 e nada diz para trocar B6 (`C6` só explica o exemplo).
27. Ordem de abas em 20: `Resumo` vem antes de `Painel` (`Como usar`, `Resumo`, `Painel`, `Config`, `Indicadores`);
    nas outras 19 a aba principal é sempre a segunda. `20 Como usar!B8` manda "abra Resumo", mas `Resumo!A2` diz que
    os números vêm de Painel/Indicadores, que estão depois.
28. `13 Painel!E5` "A receber" 128.280 e `14 Painel!E5` "Em aberto (total)" 66.050 chegam a 17 como "A receber
    (carteira)" e "Vencido"; ninguém explica que 62.230 da carteira ainda não viraram parcela (êxito e casos sem
    parcelamento em `14 Casos!E5, E8, E12…` = 0 parcelas).
29. Nomes de prompt citados nas planilhas que não existem com esse nome na biblioteca (21): "Escrever cobrança
    educada" (`14 Como usar!B10`; na biblioteca é "Clientes 03 · Cobrança educada em três versões"), "Revisar a
    proposta de honorários" (`15 Como usar!B10`, `16 Como usar!B11`; biblioteca: "Honorários 02 · Revisar a proposta
    pela margem"), "Preparar a reunião com o contador" (10, 18, 20; biblioteca: "Caixa 04 · Preparar a reunião mensal
    com o contador"), "Explicar o mês" (17, 18, 19, 20; há "Painel 01 · Explicar o mês ao sócio" e "Caixa 01 ·
    Explicar o mês do caixa"). As citações de 01–04, 09, 11–13 e 15 (Clientes 06) estão certas.
30. `16 Casos!I` "Fase" e `E` "Modalidade" são listas fixas digitadas na validação (`"Consultivo,Inicial,…"`,
    `"Fixo,Hora,Êxito,Misto,Interno"`), enquanto 02 e 13 puxam de Config: quem renomear uma fase em 13 não consegue
    escolhê-la em 16.
31. Página `advogados.html`: "Quinze minutos na segunda, quinze na sexta" × `03 Painel!C9/C13` = 12 min (segunda) e
    18 min (sexta) e `01 Como usar!B8` "Rotina de segunda: 10 minutos". Oferta (`02-oferta/advogados.md`): "38 casos
    ativos" × kit = 30 ativos + 8 encerrados (`13 Painel!I5/K5`). Fora do escopo das planilhas, mas visto de passagem:
    a página ainda tem `{{adv_aula1_dur}}`…`{{adv_aula8_dur}}` e `{{empresa.razao_social}}` sem substituir.
32. `07 Proposta!A1` e `D56` imprimem "Ferraz & Lima Advocacia (exemplo fictício)" na proposta para o cliente (vem de
    `Config!B4`); `Config!A2` não avisa que o "(exemplo fictício)" precisa sair do nome antes da primeira proposta.

#### Promessas da página × planilhas (item 6)

Existem e funcionam: semáforo por dias (01), casos parados (02), rotina segunda/sexta (03), checklist abertura e
encerramento (04), custo-hora (05), comparação fixo × hora × êxito × misto com margem e risco (06), proposta
pronta para imprimir A4 com cronograma (07, `print_area A1:E58`, fitToPage), tabela de referência por área/tipo (08),
entradas e saídas por caso e categoria (09), provisão de impostos/13º/férias (10), pró-labore e PF × escritório com
distribuição por trimestre (11), reserva de 3 meses e metas (12), carteira com contratado/recebido/a receber (13),
parcelas com régua de 4 faixas e "cobrar primeiro" (14), funil por etapa/área/origem/motivo (15), horas por caso e
por pessoa (16), painel de uma tela com prazos/horas/caixa/recebíveis/propostas (17), DRE com previsto (18), metas do
trimestre (19), resumo em bloco único para a IA e o contador (20). O que falha é o **exemplo**: os itens 1–4 fazem
o painel de sexta, o DRE, o resumo e o funil contarem uma história diferente da agenda, do caixa, da carteira e das
horas — exatamente o "tudo bate entre si" que a página e a oferta vendem.

Não verificado: abertura em Excel e Google Sheets reais (locale, FIXED/TEXT em pt-BR), impressão da 07 em papel,
arquivos 21–29, vídeos e LEIA-ME.


## Relatório B · documentos 21–29

Data: 2026-09-14. Revisor B (cliente exigente). Nenhum arquivo do projeto foi alterado; cópias e renders em `scratchpad/revB/`.

### Testes feitos

| Teste | Resultado |
|---|---|
| Páginas por PDF (PyMuPDF; `pdfinfo`/`pdftoppm` não instalados) | 21: **24** · 22: **8** · 23: **10** · 24: **5** · 25: **1** · 26: **18** |
| Render de todas as 66 páginas em PNG (70 dpi, folhas-contato) + 3 páginas do manual a 110 dpi | olhadas uma a uma (`sheet2N-*.png`, `manual-p*-110dpi.png`) |
| Texto extraído por página (`2N-texto.txt`) e grep de "Sheet N", TODO, lorem, `{{`, inglês | nenhum placeholder ou inglês; sem "Sheet N" |
| Metadados dos 6 PDFs | Título = nome do HTML de origem (ver MÉDIO 5) |
| Prompts (21): contagem por `###` no MD | **40** (5 grupos × 8); os 40 têm "Quando usar", "Cole", bloco de prompt, "Exemplo" e "Confira" |
| 21 TXT × 21 MD | `cmp` idêntico (o .txt é o Markdown cru) |
| Abas citadas nos prompts, no manual, no 22/24/25 e nos slides × abas reais (openpyxl nas 20 planilhas) | todas existem, exceto "Vencidos" na 14 (slide 29/8) |
| Recálculo das 20 planilhas em cópia (recalc.py, LibreOffice) | 0 erros; valores dos painéis 05, 09, 13, 14, 16, 17, 18, 20 usados no cruzamento com slides e prompts |
| Slides: python-pptx (texto, geometria, notas) + soffice → PDF → PNG | 27: **8** slides · 28: **10** · 29: **8** (batem com o nome do arquivo, a página e a oferta); nenhuma caixa fora do slide; notas do apresentador em todos |
| Mensagens (22) | **15** (01–15): contratação 2, parcelas/cobrança 5 (03–07), confirmação de pagamento 2, documentos/agenda 4, encerramento/avaliação 2 |
| Checklists (25) | **3** (abertura de caso, fechamento do mês, antes de enviar a proposta): 11 + 12 + 11 itens |
| Vídeos (ffprobe) | 8 mp4 (1280×720, h264/aac): 2:28, 2:18, 2:19, 2:15, 2:44, 2:33, 2:38, 2:47; 8 .srt; legenda também gravada no vídeo (quadros extraídos) |
| Zip `kit-de-gestao-para-advogados-v1.zip` × pasta `entrega/` | 47 arquivos, nomes idênticos, inclusive `videos/` e `.srt` |
| LEIA-ME × arquivos | lista os 30 arquivos + 8 aulas com nomes idênticos; explica cada um |
| Página `advogados.html` e `02-oferta/advogados.md` × entrega | 20 planilhas, 40 prompts (PDF e txt), 8 aulas de 2 a 3 min, manual em 4 semanas, 3 modelos (8/10/8), 3 checklists, 3 bônus: **existem**. Divergências listadas abaixo |

---

#### GRAVE

1. **Setembro de 2026 tem quatro versões diferentes dentro do kit (slides 27/29 × prompts 21 × planilhas).** O escritório é o mesmo, o mês é o mesmo, e o cliente que abrir a planilha 17 ao lado do modelo 27 vê números diferentes:
   - Entrou/saiu/sobrou: **27 (s2, s5) e 29 (s1, s3)** = 29.400 / 20.179 / 9.221, agosto 27.900 e sobra 7.836 · **planilhas 17, 18 e 20** = 29.400 / 20.264 / 9.136, agosto 26.660 e sobra 6.560 · **planilha 09 (Painel, Setembro)** = 10.800 / 5.970 / 4.830 (a captura da seção 4.9 do manual, p. 10, mostra exatamente isso) · **prompts Caixa 01, Caixa 02, Painel 01, Painel 02 (21, p. 12–13, 20–21)** = 31.400 / 21.900 / 9.500, agosto 26.800 e resultado 4.500.
   - Vencido e inadimplência: **27 s6 e 29 s5** = R$ 21,6 mil (16,8%) · **planilhas 14, 17, 19, 20** = R$ 26.590, 8 parcelas (17,4%) · **prompts Painel 01, Caixa 02, Clientes 02** = R$ 3.090 em 3 parcelas (clientes e valores que não existem na 14: "Patrícia Gomes R$ 750", "Helena Duarte R$ 790 há 7 dias"; na 14 Helena Duarte tem R$ 2.760 há 38 dias e R$ 2.770 há 8).
   - Êxito recebido em setembro: **27 s2** "nenhum êxito recebido" × **29 s2** "Honorários de êxito R$ 4.000" × **planilha 18** R$ 6.600 × **planilha 09** R$ 0 no mês.
   - Receita por modalidade: **29 s2** (fixos 8.800, hora 9.600, êxito 4.000, "mistos" 4.400, consultoria 2.600) × **18** (fixos 9.700, hora 5.900, êxito 6.600, consultivo 7.200). A categoria "Honorários mistos (parte fixa)" não existe na Config da 09.
   - Custo fixo: **29 s3** R$ 6.415 (Anuidades 150, Material 395) × **05, 09, 18 e prompt Caixa 03** R$ 6.500 (250, 380); logo **27 s2** "R$ 6,4 mil" também não bate.
   - Horas por pessoa no mês: **27 s3/s4** Marina 128, Rafael 118, Júlia 72 (= 318) × **16 Painel** 114 / 90,5 / 78 (= 282,5) × **17** 318 × **prompts Painel 01 e Painel 07** 98 / 104 / 52.
   - Custo-hora: **05 e prompts** R$ 66 (escritório) e R$ 72,76 por sócio · **27 s4** R$ 73 (coerente) · **29 s3** "R$ 84 = custo fixo com pró-labore ÷ 220 h", conta que não existe na 05.
   - Acumulados jan–set: **29 s6** pró-labore R$ 108.000 × **09** R$ 103.842; **29 s4** impostos R$ 13.236 × **09** R$ 14.688.
   - Propostas abertas: **17** 8 / R$ 68.400 × **prompts Painel 01, Clientes 06, Painel 05** 5 abertas / R$ 41.500. Prazos hoje + 7 dias: **17** 14 × **27 s3 e prompt Prazos 01** 13.
   Esperado (CONVENCOES §1 e §8; oferta): "tudo vem de dados.py para as 20 planilhas baterem entre si"; slides e exemplos deveriam sair das planilhas recalculadas (o que bate: 13 Carteira — 374.200 / 245.920 / 128.280, 30 ativos, 4 casos de êxito com R$ 36 mil, fases por caso — e Honorários 03).

2. **28 (proposta que vai para o cliente do advogado): logo "Seu Sócio Gestor" e rodapé "Kit de Gestão para Advogados · modelo v1.0 · set/2026" em todos os 10 slides**, como formas soltas (layout DEFAULT, nada no slide mestre). Para enviar uma proposta o advogado precisa apagar logo e rodapé slide a slide; se esquecer um, o cliente dele recebe um documento com marca de terceiro. O mesmo vale para 27 (8 slides, reunião de sócios) e 29 (8 slides, contador). Esperado: marca só no mestre (uma edição) ou ausente; rodapé de "modelo" apenas nas notas.

3. **26 Manual, seção 3 (p. 4–5): a planilha 04 não entra em nenhuma semana e as aulas citadas estão trocadas.** Semana 1 = 01, 02, 03, 05; Semana 2 = 06–10; Semana 3 = 11–16; Semana 4 = 17–20: o Checklist de abertura e encerramento (04) nunca é implantado. A seção abre com "Um núcleo por semana" (repetido no LEIA-ME: "4 semanas, um núcleo por semana"), mas são 5 núcleos e as semanas misturam núcleos (1 = prazos + custo-hora; 2 = honorários + caixa; 3 = pró-labore/reserva + carteira). Aulas: Semana 2 (com 09 Caixa e 10 Provisão) manda ver "Aulas 4 e 5" e não a 6 (Caixa, provisão e pró-labore); Semana 3 · Carteira manda ver "Aula 6" (que é caixa) e não a 7 (Carteira, parcelas e cobrança); Semana 4 · Painel manda ver "Aulas 7 e 8" (a 7 é carteira). Esperado: as 20 planilhas distribuídas nas 4 semanas e cada semana apontando a aula certa.

4. **24 Roteiro do contador, p. 5: página inteira com uma linha** ("Suporte: … Reembolso em até 7 dias."). Num PDF de 5 páginas, 20% é página em branco. Esperado: a linha no pé da p. 4.

5. **23 Guia LGPD, p. 8: página com o título da seção 9 e duas linhas, ~80% em branco**, porque o bloco do aviso de privacidade (`page-break-inside: avoid`) pula inteiro para a p. 9. Esperado: bloco quebrável ou seção 9 começando na p. 9.

6. **Página `advogados.html`, bloco "Um dos 40 prompts, como vem no kit · Painel 01 · Explicar o mês ao sócio": o texto não é o do kit.** Página: "Você é o gestor de um escritório de advocacia pequeno. Escreva um resumo do mês para os sócios, em até 250 palavras, com: resultado em uma frase; três destaques com número; dois pontos de atenção…". Kit (21, p. 20): "Explique o mês de um escritório de advocacia para o meu sócio, em até 250 palavras e linguagem direta. Use só os números abaixo. Estrutura: uma frase com o resultado do mês; prazos (…); horas (…); caixa (…); recebíveis (…); propostas (…); uma decisão para o mês que vem…". O "Confira" também difere. Esperado: a página cita o prompt literalmente ou não diz "como vem no kit".

#### MÉDIO

1. **28 s4 e s5 expõem ao cliente o método interno de preço**: "Custo-hora do escritório × 110 horas estimadas + margem, conferido com a tabela interna de casos do mesmo tipo (planilha 08)" e "base do valor da próxima página (planilha Simulador de honorário, 06)". O checklist 25 ("Nenhum dado de outro cliente, nenhum número interno (custo-hora, margem) no arquivo enviado") e o manual 4.7 dizem o contrário. Esperado: o slide "Como chegamos ao valor" sem custo-hora/margem/planilhas internas.

2. **29 s8: "13 · Carteira e 14 · Parcelas: abas Painel e Vencidos"**. A 14 tem as abas Como usar, Painel, Config, Casos, Parcelas; "Vencidos" não existe. O anexo também manda ao contador a aba Painel da 14, que lista nome de cliente e número CNJ de cada parcela vencida, enquanto o 24 (p. 2) diz que o contador "não precisa saber do que se trata o processo".

3. **21 PDF, títulos órfãos no pé da página**: p. 10 "Honorários 06 · Montar a tabela de referência interna" com o "Quando usar" cortado no pé e o prompt na p. 11; p. 19 "Clientes 08 · Encerramento do caso…" com "Cole: Planilha 4 ·" no pé e o resto na p. 20. Contraria a regra do próprio `build_pdfs.py` ("o título e o Quando usar ficam na mesma página que o prompt"). Também: p. 3 metade vazia (tabela "De onde vem cada bloco" e nada mais), p. 21 ~40% vazia.

4. **21 TXT é o Markdown cru**: 249 ocorrências de `**` e crases, cercas ``` em cada um dos 40 prompts, `#`/`##`/`###` nos títulos, tabela em pipes. A página vende o txt "para copiar no celular"; quem seleciona o prompt leva as cercas junto. Esperado: txt limpo (título, quando usar, prompt, confira) sem sintaxe Markdown.

5. **Metadados dos 6 PDFs: Título = "21-biblioteca-de-prompts-do-escritorio.html", "26-manual-de-implantacao.html" etc.** É o que aparece na aba do Chrome/Acrobat e na lista "Recentes". Esperado: "Biblioteca de prompts · Kit de Gestão para Advogados".

6. **26 Manual, seção 4 (p. 6–15): as 21 capturas são ilegíveis e sem legenda.** Imagens de 1950×1350 px impressas em 90×62 mm: a 100% de zoom nenhuma célula se lê (p. 10: os R$ 10.800 / 5.970 / 4.830 do painel da 09 só aparecem porque estão em caixa alta; p. 10 e p. 15 têm blocos de texto de nota reduzidos a manchas cinzas). Nenhuma captura diz qual aba está na tela. O item 3 da pauta desta revisão pergunta "capturas com contexto?": não. Esperado: recorte do painel (só os cartões e a primeira tabela) em largura total, com legenda "Planilha 09 · aba Painel".

7. **26 Manual 4.17 e tabela "Quem alimenta quem" (p. 4): "copie os 14 totais de sexta das 01, 16, 09, 13, 14 e 15"**, mas os valores de exemplo da 17 não são os das planilhas de origem (16 Painel = 282,5 h, 17 = 318; 09 Painel Setembro = 10.800, 17 = 29.400). Quem seguir a instrução e conferir descobre que o exemplo da 17 foi digitado à mão. Esperado: exemplo da 17 igual aos painéis de origem, ou o manual explicando que o exemplo da 17 representa o mês fechado (dia 30) e o da 09 o dia 14.

8. **Régua de cobrança descrita de três jeitos**: planilha 14 Config (1 dia = lembrete gentil; 7 = mensagem do responsável; 15 = e-mail com demonstrativo e renegociação; 30 = ligação ou reunião); bônus 22 (p. 4–5 e p. 8: 1 = WhatsApp; 7 = e-mail; 15 = WhatsApp + ligação; 30 = e-mail com três alternativas); slide 27 s6 ("lembrete no vencimento, mensagem em 7 dias, ligação em 15, reunião em 30"). O 22 diz "a mensagem só acompanha o degrau" da 14, e não acompanha.

9. **22, modelo 15 (p. 7) pede avaliação pública "em [Link]… ajuda outras pessoas a nos encontrar"**: finalidade explícita de captação de clientela. Publicidade e captação na advocacia são reguladas (Código de Ética, arts. 39 ss.; Provimento 205/2021 da OAB) e o modelo não traz nenhum aviso de "revise com as regras da OAB antes de usar". Exige revisão profissional sem dizer.

10. **22, modelo 09 (p. 5): "Vale como recibo simples; o contador diz se você precisa emitir outro documento."** e **24, p. 3, Bloco 2, item 3: "recebimento de PF sem nota"** tratado como situação corriqueira. Prestação de serviço advocatício gera nota fiscal de serviço (ISS) na regra geral; os dois textos naturalizam recebimento sem nota. Esperado: "a nota fiscal é obrigatória; o e-mail é só a confirmação" e, no 24, "se houve recebimento sem nota, como regularizar".

11. **29 s4: linhas de provisão com lógica contábil frouxa**: "13º dos sócios = 1/12 do pró-labore" (sócio não tem 13º; é decisão, não obrigação, e o slide não diz) e "Recesso de janeiro = 1/12 do custo fixo sem pró-labore" (o custo fixo de janeiro é o mesmo de qualquer mês; o que cai é a receita, e provisionar 1/12 do custo fixo não cobre isso). **29 s6** soma a bolsa da estagiária em "Pró-labore mensal · Total R$ 13.400". Vai para o contador com o nome do kit; exige revisão sem dizer.

12. **Oferta (`02-oferta/advogados.md`, tabela de bônus) promete as 15 mensagens em "PDF + txt"**; a entrega tem só o PDF (o LEIA-ME e a página não prometem o txt, mas a oferta aprovada sim).

13. **23 Guia LGPD, p. 3: metade da página em branco** ("Faça a lista real, sem vergonha:" e nada; a tabela da seção 3 só cabe inteira na p. 4).

#### LEVE

1. **26 Manual tem 18 páginas**; a oferta diz "PDF, 20 a 30 páginas". A página não promete número, mas a oferta sim.
2. **25 Checklists (p. 1)**: texto em 9,2 pt com ~40% da página em branco embaixo; a lista "Fechamento do mês" continua na 2ª coluna sem repetir o título; o subtítulo sai na fonte mono (estilo `h1+p`) e parece cabeçalho de código; "Três listas de dois minutos" com 11, 12 e 11 itens.
3. **22, p. 7 e p. 8**: metade e dois terços vazios (o título "Encerramento" abre página nova só para 2 modelos; "Registro e cadência" idem).
4. **27 s7**: "Contratar mais 20 horas por mês da estagiária (R$ 700)": a bolsa é R$ 1.400 por 60 h (R$ 23/h); 20 h = R$ 467.
5. **LEIA-ME × página**: título da aula 2 "Agenda de prazos e andamento" × página "Agenda de prazos e andamento por processo". Página (FAQ) diz que os prompts funcionam em "ChatGPT, Copilot e Gemini"; o 21 (p. 2) acrescenta "e no Claude".
6. **23, p. 7, item 4**: "comunicação à ANPD… em prazo razoável definido pela autoridade (consulte a regulamentação vigente)". A Resolução CD/ANPD 15/2024 fixa 3 dias úteis; o guia fica vago onde já existe regra escrita (ressalva de "não é parecer" está na p. 2 e p. 10, o que atenua).
7. **22 × página**: a página descreve as 15 como "lembrete antes do vencimento, atraso de 1 a 30 dias, confirmação de pagamento, encerramento"; 4 das 15 (10–13: documentos, audiência, reunião) não cabem nessa descrição. Só 5 são cobrança de fato.
8. **21 e slides usam "Ferraz & Lima" e 27/29 escrevem "R$ 29,4 mil" enquanto o 20 Resumo escreve "R$ 29.400"**: estilo de número muda de documento para documento (mil × ponto). Cosmético.
9. **28 s10**: telefones "(11) 9 0000-0000" e e-mail "@ferrazlima.exemplo" ficam no modelo sem colchetes; quem esquecer de trocar envia contato falso. Os demais campos do 28 não usam colchetes, ao contrário do 22.
10. **Vídeos**: a "tela real" das aulas é um recorte ampliado da planilha renderizado com cabeçalho da marca (aula 5, 45 s; aula 1, 20 s), não a janela do Excel/Sheets; a página promete "tela real". Funciona, mas quem espera ver o Excel não vê.


## Relatório C · aulas, página, obrigado, e-mails, copy

Data: 14/09/2026. Versão revisada: `site/src/pages/advogados.html` no HEAD 85f273b (única mudança recente: `og_image`), build de 17:36; vídeos de `produto/kit-advogados/entrega/videos/` gerados às 10:00–10:36. Nenhum arquivo do projeto foi alterado.

### Cabeçalho de testes

**Vídeos (ffprobe)** — todos 1280×720, H.264 30 fps, AAC 44,1 kHz mono 128 kb/s, áudio e vídeo com a mesma duração.

| Aula | Arquivo | Medido | config.json | Cues .srt | Fim do .srt |
|---|---|---|---|---|---|
| 1 | aula-01-antes-de-abrir-a-planilha | 148,15 s = 2:28 | 2:28 ✓ | 39 | 2:27,05 |
| 2 | aula-02-agenda-de-prazos-e-andamento | 138,87 s = 2:19 | 2:19 ✓ | 40 | 2:17,88 |
| 3 | aula-03-custo-hora-do-escritorio | 139,90 s = 2:20 | 2:20 ✓ | 38 | 2:18,80 |
| 4 | aula-04-simulador-e-tabela-de-honorarios | 135,11 s = 2:15 | 2:15 ✓ | 38 | 2:14,01 |
| 5 | aula-05-custo-hora-e-proposta | 164,20 s = 2:44 | 2:44 ✓ | 45 | 2:43,10 |
| 6 | aula-06-caixa-provisao-e-pro-labore | 153,40 s = 2:33 | 2:33 ✓ | 42 | 2:32,34 |
| 7 | aula-07-carteira-parcelas-e-cobranca | 158,13 s = 2:38 | 2:38 ✓ | 45 | 2:37,07 |
| 8 | aula-08-painel-de-sexta-e-fechamento | 167,47 s = 2:47 | 2:47 ✓ | 45 | 2:46,42 |

Total 1.204 s = 20,1 min (manual 26 diz "20 min no total" ✓; LEIA-ME "2 a 3 minutos" ✓; página "8 aulas de 2 a 3 minutos" ✓).
Sincronia vídeo × áudio: bordas de cena medidas pela troca da barra roxa de legenda (10 fps) ficaram a no máximo 0,5 s do esperado pelas durações dos `cena*.wav` (pior caso aula 5 cena 8: 118,4 s × 117,9 s; aula 8 cena 8: 123,0 × 122,6). O .srt é gerado a partir do roteiro por proporção de caracteres (`produto/legendas.py`), e a legenda gravada é o próprio .srt: portanto legenda gravada = .srt por construção; sincronia dentro de cada cena é aproximada (não há alinhamento por áudio; whisper não disponível no ambiente). Frames extraídos a cada 8 s (151 quadros) + 16 quadros pontuais em resolução total foram olhados.
Áudio: média −15,7 a −16,5 dB, pico 0,0 dBFS nas 8 aulas. Primeiro quadro de todas as aulas é claro (#FFFAF0) por ~0,3 s antes da capa aparecer.

**Entrega (produto/kit-advogados/entrega)** — 20 .xlsx ✓ (5 núcleos × 4); aba "Como usar" em 20/20; proteção de aba em todas; 0 valores em cache (todas as ~23.000 fórmulas sem resultado gravado); recálculo no LibreOffice sem nenhum #NOME?/#VALOR!/#REF!. Biblioteca 21: 40 prompts (5 grupos × 8) ✓, todos os prompts citados nas aulas existem (Prazos 02/04/06/07, Honorários 01/02/04/06/07, Caixa 04/06/08, Clientes 02/03, Painel 01/06). Bônus 22: 15 mensagens ✓ (PDF 8 p.). 23 guia LGPD (10 p.) com "Modelo simples de aviso de privacidade" ✓. 24 roteiro (5 p.) com "pauta de 30 minutos" ✓. 25 checklists: 3 ✓ (1 p.). 26 manual: 18 páginas, 4 semanas ✓. 27/28/29: 8/10/8 slides ✓. Abas citadas nas aulas existem (Rotina, Prazos, Config, Nossos casos, Lançamentos, Retiradas, Dados, Histórico, Indicadores, Resumo, Registro).
Números narrados × planilhas recalculadas: conferidos um a um nas 20 (ver GRAVE 1 e MÉDIO 7, 8, 21 para os que divergem; o resto bate).

**Página /advogados (Playwright, Chromium)** — 390×844 e 1366×768 (+360 e 768 para quebra de texto): 0 erros de console, 0 respostas ≥ 400, 0 requests falhas; `scrollWidth == clientWidth` (sem overflow horizontal); nenhum elemento além da borda; todos os `href` internos existem em `site/public` (/, /kit/, /completo/, /sobre/, /reembolso/, /suporte/, /termos/, /privacidade/, /cookies/, assets, vídeo .mp4 e .vtt); âncoras `#preco`, `#conteudo` resolvem; poster do vídeo responde 200 (`poster-aula-05-960.webp`), `preload=none`, track pt-BR; 9 `<details>` e o primeiro abre ao clique; nenhum `.btn`, `.tag`, `.tela__chips li`, `.hero__nota span`, `.tela__barra b`, `.aulas li span` quebra linha em 360/390/768/1366 (só o rótulo `.exemplo__rot` quebra em 360 px, e não é chip); heurística de contraste (WCAG 4,5:1 / 3:1) sem falhas. Páginas /obrigado/, /obrigado/pix/ e /obrigado/recusado/ geradas, sem erro nem overflow em 390 px.

---

#### GRAVE

1. **Aula 5, cena 9 (2:13–2:29), card "Quanto cobrar por este caso" + narração + .srt cues 38–39 + `build_aulas.py`.** Visto na tela e narrado: "Custo: R$ 66,07 × 53 horas = R$ 3.952". Esperado: 66,07 × 53 = **R$ 3.501,71** (planilha 06, Simulador!C29). R$ 3.951,71 é o custo total do caso (horas 3.501,71 + R$ 450 de despesas que o escritório absorve, D40). A aula que a página usa como demonstração pública mostra uma multiplicação errada; é a primeira coisa que um advogado confere. A aula 4, cena 2 (0:25–0:43), também diz "Cinquenta e três horas, custo de três mil novecentos e cinquenta e dois" logo após listar as horas por etapa, misturando os dois números.

2. **Página, seção `#prompts-aulas`, card "Um dos 40 prompts, como vem no kit · Painel 01".** Visto: texto "Você é o gestor de um escritório de advocacia pequeno. Escreva um resumo do mês para os sócios, em até 250 palavras, com: resultado em uma frase; três destaques com número; dois pontos de atenção com causa provável e ação; próximos passos com responsável e prazo…". Esperado (biblioteca 21, Painel 01): "Explique o mês de um escritório de advocacia para o meu sócio, em até 250 palavras e linguagem direta. Use só os números abaixo. Estrutura: uma frase com o resultado do mês; prazos (…); horas (…); caixa (…); recebíveis (…); propostas (…); uma decisão para o mês que vem. Onde faltar explicação, escreva "[explicar]"… Não comente o mérito de nenhum caso." A página promete "como vem no kit" e entrega outro texto (a aula 8, cena 8, descreve a versão real). Amostra diferente do produto: problema de CDC (art. 30/31) e de confiança.

3. **Manual 26, seção 3 "Implantação em 4 semanas" (docs/26-manual-de-implantacao.html → PDF).** Visto: "Semana 2 · 06, 07, 08, 09, 10 · Aulas 4 e 5"; "Semana 3 · Carteira (11–16) · Aula 6"; "Semana 4 · Painel (17–20) · Aulas 7 e 8". Esperado pela entrega: aula 5 = custo-hora e proposta (não cobre caixa 09/10), aula 6 = **caixa, provisão e pró-labore (09–12)**, aula 7 = **carteira (13–16)**, aula 8 = painel (17–20). O manual segue a grade antiga de `04-copy/advogados.md` (5 Caixa, 6 Carteira, 7 Painel, 8 Fechamento). O comprador da semana 3 é mandado ver a aula de caixa, e a semana 4 manda ver a aula de carteira. O manual também não lista os títulos das 8 aulas em nenhuma seção (seção 1 só diz "8 aulas de 2 a 3 minutos"), então não dá para o leitor se corrigir.

4. **E-mails, `05-checkout/emails.md`, bloco Advogados.** (a) D+0: "Assunto (Essencial)/(Completo)" e "Produto: Kit IA no Trabalho · [Essencial|Completo]" no RESUMO DO PEDIDO não têm variante Advogados; o comprador do kit de R$ 497 recebe assunto e nome de produto de outro kit. (b) D+1: assunto "15 minutos para a Semana Organizada funcionar" e abertura "Ontem você recebeu o kit… primeiro arquivo" não são substituídos (o bloco Advogados só troca os passos). (c) REQUISITOS (D+0) e D+3 dizem "Excel 2016 ou mais novo" e "abra no Excel 2016 ou mais novo"; LEIA-ME, manual e FAQ da página dizem Excel 2019+ e avisam que 01–04 e 13 mostram #NOME? no 2016. O e-mail de suporte manda o comprador para a versão que quebra. (d) Título do documento: "Kit IA no Trabalho (Essencial e Completo)" — a regra "há dois blocos: Essencial e Completo" está desatualizada.

5. **Vídeo, aulas 2 e 4, capa (0:00–0:11).** Visto no quadro 0:06 das duas: a legenda gravada ("em que pé está cada caso e o que falta na abertura e no encerramento." / "Planilhas seis e oito: comparar fixo, hora, êxito e misto para um caso,") passa por cima da linha amarela "Kit de Gestão para Advogados · Seu Sócio Gestor". Causa: título de duas linhas ("Agenda de prazos e andamento", "Simulador e tabela de honorários") empurra o kicker (`.capa .k`, margin-top 60 px) para a faixa da legenda (base a 88 px do rodapé). Aulas 1, 3, 5, 6, 7, 8 (título de uma linha) não sobrepõem. Esperado: legenda abaixo do kicker ou kicker fixo no rodapé.

#### MÉDIO

6. **Título de cada aula não é o mesmo nos cinco lugares.** Aula 2: página "Agenda de prazos e andamento **por processo**" × LEIA-ME e capa "Agenda de prazos e andamento" × arquivo `…-e-andamento`. Aula 7: LEIA-ME e página "Carteira, parcelas e cobrança **educada**" × capa "Carteira, parcelas e cobrança" × arquivo `…-e-cobranca`. Aula 8: LEIA-ME e página "Painel de sexta e fechamento **do mês com o contador**" × capa "Painel de sexta e fechamento". Aulas 1 e 5: LEIA-ME/página juntam título + subtítulo da capa ("Antes de abrir a planilha: os cinco núcleos e a rotina"; "Custo-hora e proposta: quanto cobrar por este caso"), o que seria a regra, mas 7 e 8 não a seguem. A `figcaption` e o `aria-label` da demo criam um quarto título: "Custo-hora e proposta de honorários". Manual 26: nenhum título (ver GRAVE 3).

7. **Exemplo Ferraz & Lima incoerente entre núcleos, para o mesmo mês (setembro, referência 14/09).** Planilha 09 Caixa e 10 Provisão: "Entrou no mês R$ 10.800" (aula 6, cenas 1 e 4). Planilhas 17 Painel, 18 Resultado e 20 Resumo: "Entrou no mês R$ 29.400" (aula 8, cenas 1, 3, 6). Planilha 16 Horas por caso está em "**Agosto** de 2026" (282,5 h, 77% faturáveis — aula 7, cena 8) enquanto 17 mostra "Horas do mês 318 · 71%" de setembro (aula 8, cena 1) e 20 diz "318 h". O exemplo da biblioteca 21, Painel 01, usa um terceiro conjunto ("56 prazos, 9 atrasados… entrou R$ 31.400, saiu R$ 21.900, atrasado R$ 3.090"), diferente do bloco único da planilha 20 (7 atrasados, 29.400, 20.264, vencido 26.590). Quem assistir às 8 aulas em sequência vê o mesmo escritório com três "entrou no mês" diferentes.

8. **Hora mínima R$ 110 × R$ 127,88 sem explicação.** Aulas 3 e 5 (planilha 05): "hora mínima a cobrar: cento e dez". Aula 4, cena 5 (planilha 08): "Hora mínima cento e vinte e sete, hora alvo cento e sessenta e oito, calculadas do custo-hora". A diferença vem da folga de 20% de horas (Config!B11 da 08) e da margem alvo de 45%, mas a narração não diz; o espectador recebe duas "horas mínimas" do mesmo escritório, uma aula depois da outra.

9. **Página `#metodo` e `#cenarios` × produto.** H2 "Cinco núcleos, um fechamento por semana" com uma lista de **quatro** passos (`passos--4`; "Carteira e painel" fundidos) — a copy previa cinco. Lead "Quinze minutos na segunda, quinze na sexta" × planilha 03/aula 1: **12 min na segunda, 18 na sexta** (manual seção 1 e 6 também diz 15/15). Cenário 2 "Proposta com margem, em quinze minutos" × aula 5, cena 1: "Vinte minutos na primeira vez; depois, cinco" × manual seção 6: "Antes de cada proposta, 15 minutos". Três tempos para a mesma tarefa.

10. **Páginas de obrigado (3 estados) e rodapé para quem comprou o Advogados.** Eyebrow "Seu Sócio Gestor · **Kit IA no Trabalho**" nos três estados; `description` de /obrigado/pix/ e /obrigado/recusado/ diz "pedido do Kit IA no Trabalho". Card "Primeiros 7 dias" só tem Semana Organizada, Relatório Mensal, Ganhos e Gastos, Metas do Trimestre (kits 1 e 2); nada dos passos do Advogados (05 → 01 → 06/07). "São 15 minutos de leitura" × LEIA-ME e manual "20 minutos". /obrigado/pix/: "Volte à página do kit (Essencial ou Completo)" sem link para /advogados/. Rodapé do layout: "Para advogados" aponta para `/#kits` embora `/advogados/` exista (a home já linka `/advogados/` no card).

11. **`04-copy/advogados.md` desatualizado em relação à página e ao produto.** Grade das aulas (4 "Simulador e proposta de honorários", 5 "Caixa…", 6 "Carteira…", 7 "Painel de sexta e resultado do mês", 8 "Fechamento do mês com o contador e a IA") não é a entregue; prompt anotado "**Caixa 01** · Explicar o mês ao sócio" (na biblioteca, Caixa 01 é "Explicar o mês do caixa"; o certo é Painel 01); método com 5 itens; FAQ 3 "Não." × página "Precisa saber digitar em uma célula"; FAQ 4 "Três funções pedem Excel 2019" × página "Algumas funções". Foi essa copy que contaminou o manual (GRAVE 3); quem revisar pela copy reintroduz o erro.

12. **20 planilhas entregues sem valores calculados em cache** (openpyxl grava a fórmula sem resultado). Pré-visualização no Drive, Gmail, WhatsApp, Quick Look e alguns visualizadores de celular mostram painéis vazios até um recálculo; a página promete "20 planilhas · computador e celular" e "Telas reais". Abrir e salvar cada arquivo no Excel (ou LibreOffice) antes de zipar resolve. Anotar também que o LibreOffice recalculou sem erro, mas o teste em Excel/Sheets reais ainda consta como pendente no README.

13. **Alegação comparativa não comprovada:** "Menos que três meses do software jurídico **mais barato**, uma vez" (`#preco`, `.preco__anc`; ângulo 3 dos anúncios: "Menos que três meses de software, uma vez"). A oferta só cita ADVBOX (R$ 220–1.800/mês); existem SaaS jurídicos abaixo de R$ 166/mês. Superlativo sem fonte é publicidade comparativa sem prova (CDC art. 37 § 1º; política da Meta sobre alegações). Trocar por "menos que três meses de um software jurídico típico" ou citar a referência.

14. **Enquadramento de tela nos vídeos.** Aula 7, cena 1 (0:12–0:28): gráfico "Contratado × recebido por área" cortado à direita — aparece "Con" e os rótulos Família/Previdenciário/Cível pela metade (foco com 66% da largura). Aula 2, cena 7 (1:40–1:54): topo da tabela cortado, linha "…filtrada pela coluna Pendências." meio visível. Aula 5, cena 3 (0:41–0:54): o zoom mostra a coluna de comentário da planilha 06 quebrada em 6 linhas estreitas ("Copie da planilha 05 · Custo-hora (Painel, "Custo-hora do escritório")"), ocupando metade do quadro; a célula de valor que importa fica pequena.

15. **Dados jurídicos do exemplo que um advogado estranha (aparecem nas aulas 2 e 4).** Planilha 02, "Parados há mais de 30 dias": "Padaria do Sol Ltda · fase **Inicial** · próxima ação: Protocolar: **cumprimento de sentença**" (não existe cumprimento de sentença em fase inicial); "Bistrô 42 · fase **Acordo** · Protocolar: **contrarrazões**". Planilha 01, "O que vence primeiro": "Audiência de conciliação · 11/09 · **Atrasado**" (audiência passada tratada como prazo em atraso; o que atrasa é a baixa). Planilha 08 "Nossos casos": "Padaria do Sol · Empresarial · Êxito · fase Inicial" com 63 h estimadas e "Roberto Almeida · Cível · Êxito · fase Acordo" — plausível, mas o mesmo Roberto Almeida é o "caso novo" da aula 5.

16. **Planilha 20, aba Resumo (aula 8, cenas 6–7):** "em relação a **Agosto**" com inicial maiúscula (mês em minúscula). As frases usam `TEXTO()` com máscara "#.##0": no recálculo em locale en-US saiu "R$ 29,400" e "31.1%"; no Google Sheets com localidade fora do Brasil ou Excel em inglês o bloco único sai com separadores trocados. Testar e avisar no "Como usar".

17. **Régua de cobrança (planilha 14, aula 7, cena 4) × bônus 22.** Régua: 15–29 dias = "e-mail com demonstrativo e renegociação"; 30+ = "ligação ou reunião e plano por escrito". Bônus: "06 · Atraso de 15 dias (**WhatsApp + ligação**)" e "07 · Atraso de 30 dias (**e-mail**)". Canais invertidos em relação ao que a aula ensina ("o bônus segue a mesma régua").

#### LEVE

18. Todos os vídeos abrem com ~0,3 s de quadro creme (#FFFAF0) antes de a capa surgir (medido 0,0–0,2 s claro, escuro a partir de ~0,4 s). Um `trim` mais justo ou capa sem fade inicial resolve.
19. Pico de áudio em 0,0 dBFS nas 8 aulas (normalizado no teto); média −16 dB. Deixar −1 dBTP evita distorção em alto-falante de celular.
20. `.srt`: cues com menos de 1 s piscam — aula 4 "Risco baixo." (0,77 s), aula 6 "No ano:" (0,42 s), aula 7 "Para o seu tom," (0,89 s), aula 8 "propostas." (0,63 s) e "Fim do curso." (0,78 s). Linhas com mais de 46 caracteres por causa do corte fixo em 42 só na primeira linha: aula 3 cues 5, 10, 12; aula 5 cue 30; aula 8 cue 26. Sincronia dentro da cena é por proporção de caracteres: em frases com números por extenso a legenda chega a ~1 s fora.
21. Arredondamentos na narração que destoam da tela: aula 7, cena 5 "Luciana Farias, **sete mil**, onze dias" (tela: R$ 7.450, na mesma cena em que Helena Duarte é dita com centena); aula 6, cena 1 "Saldo acumulado, quarenta mil" (R$ 40.795); aula 4, cena 5 "cento e vinte e sete / cento e sessenta e oito" (R$ 127,88 / 168,69).
22. Página: `figcaption` e `aria-label` da demo com título próprio (ver 6); nota do inventário reutiliza `.hero__transp` com `style="margin-top:18px"` inline; FAQ "Funciona no Google Sheets?" diz "Algumas funções" sem nomear (a página do Completo nomeia MÍNIMOSES, MÁXIMOSES e UNIRTEXTO); inventário promete "Excel, Google Sheets e celular" e o manual avisa "no celular os aplicativos abrem e mostram; para preencher, use o computador" — a página não faz essa ressalva.
23. E-mail D+0 Advogados: "assista à aula 1 (2 min)" — são 2 min 28 s (o Completo cita "2 min 25 s" exato).
24. Manual 26 tem 18 páginas; a oferta prometia "20 a 30 páginas". LEIA-ME "20 minutos de leitura" × obrigado "15 minutos" (ver 10).
25. Consistência com /completo: mesma sequência de seções, herói com mockup e chips, inventário em notebook+celular, prompt anotado + grade, para quem é, quem faz, preço, FAQ — segue o padrão. Diverge sem motivo em: falta a FAQ de licença/equipe ("Posso usar com a minha equipe?"), relevante para escritório com sócios; o bloco "Quem faz" perdeu "cada arquivo tem versão e data de revisão"; o Completo escreve a parcela ("12× de R$ 19,90"), o Advogados não (aceitável pela regra do preço único, mas é divergência). Tags do inventário por núcleo ("1 · Prazos") em vez de por arquivo ("01") é escolha coerente com 20 planilhas.
26. `04-copy` diz "Segunda-feira, 15 minutos" e manual seção 1 "15 min na segunda / 15 min na sexta" enquanto a planilha 03 soma 12 + 18 (já em 9); alinhar todos a 12/18 ou mudar a planilha.
27. Planilha 17 Painel, cartão "Entrou no mês 29.400" vem da aba Dados digitada à mão; nada avisa que difere do Caixa (09) do mesmo mês (já em 7). Sugerir que Dados do exemplo copie os totais reais de 09/10/13/14/15/16.
