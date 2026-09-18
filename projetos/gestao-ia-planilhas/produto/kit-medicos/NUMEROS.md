# NÚMEROS DO EXEMPLO · Clínica Vida Plena (Kit de Gestão para Médicos)

Gerado por `numeros.py` a partir das 20 planilhas recalculadas e de `dados.py` (fonte única). Use estes valores em prompts, slides, manual e aulas: são exatamente os que aparecem nas planilhas.

## 1. Referência e regras do exemplo

- **Hoje (data de referência, Config = data literal 14/09/2026)**: segunda-feira **14/09/2026**. **Sexta do painel**: **11/09/2026**. Nenhum lançamento pago (caixa, parcela, lote de convênio) tem data depois de 11/09/2026.
- **Meses**: caixa (09) lançado de janeiro a 11/09/2026; agenda (01) registrada de 01/06/2026 a hoje + 21 dias (antes, a recepção só fechava o caixa do dia); **17 Painel da clínica** mostra **setembro em andamento**; **18 Resultado mensal** e **20 Resumo do mês** analisam **agosto de 2026** (último mês fechado; 20 = agosto × julho); **16 Conciliação** está em **agosto**; **19 Metas** = 3º trimestre (semana 11 de 13, 82 % decorrido).
- **Inadimplência (única no kit: 14, 17, 19, 20)** = vencido ÷ (pago + vencido), só do que foi combinado a prazo. Não é vencido ÷ em aberto.
- **Alíquota de impostos** (05 a 10, 18): **11 %** (alíquota efetiva combinada com o contador; Simples anexo III/V simplificado; só imposto — a taxa da maquininha é despesa variável, conciliada na 16). **Margem mínima** 30 %, **margem alvo** 45 %, **retornos por consulta** 0,4 × 20 min (embutidos no custo da consulta), **custo do dinheiro** (07) 1,5 % ao mês, **repasse** da médica parceira 50 % da produção.
- **Fontes de cadastro**: 01 · Agenda (abas Agenda e Pacientes) é a fonte da agenda e dos pacientes: 02 e 16 copiam a Agenda, 14 copia os Pacientes, 13 · Guias vem dos atendimentos de convênio. Particular à vista entra no caixa (09) pelo fechamento do dia (uma linha por dia e forma); particular a prazo vira parcela (14) e entra no caixa quando paga; convênio vira guia (13) e entra no caixa quando o lote é pago (menos a glosa); cartão entra pelo bruto no dia da venda e as taxas do mês saem numa linha só no fim do mês (o total da 16).
- **Todas as datas são literais**: nenhuma célula do exemplo usa `=HOJE()+n`. O exemplo é uma foto de 14/09/2026 e os números fecham entre os vinte arquivos em qualquer dia em que o cliente abrir. Ao começar a usar com os seus dados, troque a data de referência em Config por `=HOJE()`.

- **Nada clínico**: procedimento é só o nome administrativo (consulta, retorno, ECG, MAPA, Holter, teste ergométrico, avaliação endócrina); pacientes têm nome fictício e contato fictício (prefixo 90000); sem diagnóstico, prontuário ou exame.

## 2. Clínica, custos e custo da hora (05, 06, 07, 08)

| Pessoa | Papel | Remuneração | Valor mensal | Horas de atendimento/mês (planejadas) | Turnos |
|---|---|---|---|---|---|
| Dra. Carolina Mendes | Sócia · clínica médica | Pró-labore | R$ 9.000 | 70 | Segunda manhã (Sala 1), Terça manhã (Sala 1), Quarta tarde (Sala 1), Quinta manhã (Sala 1) |
| Dr. Paulo Andrade | Sócio · cardiologia | Pró-labore | R$ 9.000 | 70 | Segunda tarde (Sala 2), Terça tarde (Sala 2), Quinta tarde (Sala 2), Sexta manhã (Sala 2) |
| Dra. Renata Sousa | Médica parceira · endocrinologia | Repasse (50 % da produção) | — | 35 | Terça tarde (Sala 1), Quinta tarde (Sala 1) |
| Bruna Carvalho | Recepcionista (CLT) | Salário (já nos custos fixos) | R$ 2.200 | — | — |

- Salas: Sala 1 (Carolina de manhã seg/ter/qui e quarta à tarde; Renata ter/qui à tarde) e Sala 2 (Paulo seg/ter/qui à tarde e sexta de manhã). Turnos de 4 h. Feriados de 2026 cadastrados na 01 (07/09 é feriado: setembro tem menos horas).
| Custo fixo | R$/mês |
|---|---|
| Aluguel e condomínio | R$ 3.900 |
| Recepção (salário e encargos) | R$ 3.100 |
| Contador | R$ 600 |
| Sistema de agenda e assinaturas | R$ 300 |
| Energia, água, internet e telefone | R$ 550 |
| Limpeza e material de escritório | R$ 450 |
| Marketing e site | R$ 650 |
| Anuidade CRM, seguro e cursos | R$ 450 |
| **Total de custos fixos (05, 09, 18)** | **R$ 10.000** |
| Pró-labore dos sócios (2 × 9.000) | R$ 18.000 |
| **Custo total do mês (05 Painel B11)** | **R$ 28.000** |

- **Horas de atendimento planejadas (sócios)**: 140 h (70 + 70). A médica parceira (35 h) não entra: o repasse dela é custo variável (11).
- **Custo da hora de atendimento (05 B13 = 06 Config B7 = 07 Config B5 = 08 Config B7)**: **R$ 200,00** (28.000 ÷ 140 h).
- **Hora mínima a cobrar (05)**: exata **R$ 338,98** = 200 ÷ (1 − 0,30 − 0,11); arredondada **R$ 340**. Hora alvo (08 Config): R$ 454,55. Custo direto por hora (pró-labore ÷ horas): R$ 128,57; custo da estrutura por hora (custos fixos ÷ horas, 05 B20 = 11 Config B11): R$ 71,43. **Custo de um horário vazio de 30 min**: R$ 100,00.
| Sensibilidade (05) | Queda | Horas atendidas | Custo-hora | Hora mínima |
|---|---|---|---|---|
| Agenda planejada | 0 % | 140,0 | R$ 200,00 | R$ 338,98 |
| Queda de 10% | 10 % | 126,0 | R$ 222,22 | R$ 376,65 |
| Queda de 20% | 20 % | 112,0 | R$ 250,00 | R$ 423,73 |
| Queda de 30% | 30 % | 98,0 | R$ 285,71 | R$ 484,26 |
| Agosto de 2026 realizado (horas atendidas dos sócios: Painel da 01 com Config = Agosto, coluna "Horas atendidas" da Dra. Carolina + do Dr. Paulo, sem a médica parceira) | 32 % | 94,7 | R$ 295,67 | R$ 501,14 |

- A última linha usa as horas atendidas dos sócios em agosto (Painel da 01): o custo-hora real de agosto contra os R$ 200 planejados.
**Precificação (06 = 08): custo cheio, mínimo, alvo e tabelas**

| Procedimento | Minutos | Retorno? | Material | Custo cheio | Preço mínimo | Preço alvo | Particular | Margem particular | Situação | Saúde Total | Margem | MediPlan | Margem | Vida Care | Margem |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Consulta | 30 | Sim | R$ 4 | R$ 130,67 | R$ 221,47 | R$ 296,97 | R$ 380 | 54,6 % | No alvo ou acima | R$ 120 | -19,9 % | R$ 100 | -41,7 % | R$ 90 | -56,2 % |
| Retorno | 20 | Não | R$ 2 | R$ 68,67 | R$ 116,38 | R$ 156,06 | R$ 0 | — | Sem cobrança | — | — | — | — | — | — |
| ECG | 20 | Não | R$ 8 | R$ 74,67 | R$ 126,55 | R$ 169,70 | R$ 130 | 31,6 % | Entre mínimo e alvo | R$ 40 | -97,7 % | R$ 35 | -124,3 % | R$ 32 | -144,3 % |
| MAPA | 20 | Não | R$ 15 | R$ 81,67 | R$ 138,42 | R$ 185,61 | R$ 300 | 61,8 % | No alvo ou acima | R$ 95 | 3,0 % | R$ 85 | -7,1 % | R$ 75 | -19,9 % |
| Holter | 20 | Não | R$ 18 | R$ 84,67 | R$ 143,50 | R$ 192,42 | R$ 350 | 64,8 % | No alvo ou acima | R$ 105 | 8,4 % | R$ 95 | -0,1 % | R$ 85 | -10,6 % |
| Teste ergométrico | 40 | Não | R$ 25 | R$ 158,33 | R$ 268,36 | R$ 359,85 | R$ 450 | 53,8 % | No alvo ou acima | R$ 140 | -24,1 % | R$ 125 | -37,7 % | R$ 110 | -54,9 % |
| Avaliação endócrina | 40 | Sim | R$ 4 | R$ 164,00 | R$ 277,97 | R$ 372,73 | R$ 400 | 48,0 % | No alvo ou acima | R$ 130 | -37,2 % | — | — | — | — |

- 06 Resumo: procedimentos com particular abaixo do mínimo: 0 de 7; tabelas de convênio abaixo do custo cheio + imposto: 14; maior prejuízo por atendimento em convênio: R$ 60,43. Simulação de exemplo (consulta estendida de 45 min a R$ 480): custo R$ 180,67, mínimo R$ 306,21, alvo R$ 410,61, margem 51,4 %.
- 08 Tabela (volume de agosto, Painel da 01): produção do mês R$ 48.631; valor médio por hora R$ 410,97 (21 % contra a hora mínima); particular abaixo do mínimo: 0 de 7; tabelas de convênio abaixo do custo cheio + imposto: 14 (o mesmo número do Resumo da 06).
| Procedimento (08) | Realizados em agosto | Produção | Valor médio praticado | Contra o mínimo |
|---|---|---|---|---|
| Consulta | 130 | R$ 30.730 | R$ 236,38 | 7 % |
| Retorno | 48 | R$ 0 | R$ 0,00 | — |
| ECG | 18 | R$ 1.416 | R$ 78,67 | -38 % |
| MAPA | 8 | R$ 1.345 | R$ 168,12 | 21 % |
| Holter | 10 | R$ 2.490 | R$ 249,00 | 74 % |
| Teste ergométrico | 8 | R$ 2.270 | R$ 283,75 | 6 % |
| Avaliação endócrina | 30 | R$ 10.380 | R$ 346,00 | 24 % |

| Valor por hora por pagador (08) | Minutos c/ retorno | Particular | Saúde Total | MediPlan | Vida Care | Hora mínima | Hora alvo |
|---|---|---|---|---|---|---|---|
| Consulta | 38,0 | R$ 600 | R$ 189 | R$ 158 | R$ 142 | R$ 339 | R$ 455 |
| Retorno | 20,0 | R$ 0 | — | — | — | R$ 339 | R$ 455 |
| ECG | 20,0 | R$ 390 | R$ 120 | R$ 105 | R$ 96 | R$ 339 | R$ 455 |
| MAPA | 20,0 | R$ 900 | R$ 285 | R$ 255 | R$ 225 | R$ 339 | R$ 455 |
| Holter | 20,0 | R$ 1.050 | R$ 315 | R$ 285 | R$ 255 | R$ 339 | R$ 455 |
| Teste ergométrico | 40,0 | R$ 675 | R$ 210 | R$ 188 | R$ 165 | R$ 339 | R$ 455 |
| Avaliação endócrina | 48,0 | R$ 500 | R$ 162 | — | — | R$ 339 | R$ 455 |

**Simulador convênio × particular (07), consulta**

| Pagador | Tabela | Prazo | Glosa esperada | Após glosa | Custo do dinheiro | Impostos | Líquido | Custo cheio | Margem | Margem % | Líquido/hora | Contra a hora mínima | Leitura (agenda cheia) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Particular | R$ 380 | 0 | 0 % | R$ 380,00 | R$ 0,00 | R$ 41,80 | R$ 338,20 | R$ 130,67 | R$ 207,53 | 55 % | R$ 534,00 | +58 % | Cobre custo e margem |
| Saúde Total | R$ 120 | 30 | 3 % | R$ 116,40 | R$ 1,75 | R$ 12,80 | R$ 101,85 | R$ 130,67 | −R$ 28,82 | -24 % | R$ 160,82 | -53 % | Não cobre o custo cheio |
| MediPlan | R$ 100 | 45 | 6 % | R$ 94,00 | R$ 2,12 | R$ 10,34 | R$ 81,55 | R$ 130,67 | −R$ 49,12 | -49 % | R$ 128,76 | -62 % | Não cobre o custo cheio |
| Vida Care | R$ 90 | 60 | 10 % | R$ 81,00 | R$ 2,43 | R$ 8,91 | R$ 69,66 | R$ 130,67 | −R$ 61,01 | -68 % | R$ 109,99 | -68 % | Não cobre o custo cheio |

| Pagador (agenda vazia) | Líquido | Material | Contribuição | Contribuição/hora | Atendimentos = 1 particular | Leitura |
|---|---|---|---|---|---|---|
| Particular | R$ 338,20 | R$ 4 | R$ 334,20 | R$ 527,68 | 1,0 | Contribui: melhor que o horário vazio |
| Saúde Total | R$ 101,85 | R$ 4 | R$ 97,85 | R$ 154,50 | 3,4 | Contribui: melhor que o horário vazio |
| MediPlan | R$ 81,55 | R$ 4 | R$ 77,55 | R$ 122,44 | 4,3 | Contribui: melhor que o horário vazio |
| Vida Care | R$ 69,66 | R$ 4 | R$ 65,66 | R$ 103,67 | 5,1 | Contribui, mas o prazo pesa no caixa: só com reserva (12) |

| Mix de agosto (07, consultas realizadas) | Atendimentos | Horas | Líquido | Custo cheio | Resultado | % atend. | % líquido |
|---|---|---|---|---|---|---|---|
| Particular | 62 | 39,3 | R$ 20.968 | R$ 8.101 | R$ 12.867 | 48 % | 78 % |
| Saúde Total | 25 | 15,8 | R$ 2.546 | R$ 3.267 | −R$ 720 | 19 % | 9 % |
| MediPlan | 30 | 19,0 | R$ 2.446 | R$ 3.920 | −R$ 1.474 | 23 % | 9 % |
| Vida Care | 13 | 8,2 | R$ 906 | R$ 1.699 | −R$ 793 | 10 % | 3 % |
| **Total** | 130 | 82,3 | R$ 26.867 | R$ 16.987 | **R$ 9.880** |  |  |

- 07 KPIs: custo cheio da consulta R$ 130,67; hora mínima R$ 338,98; particular líquido por hora R$ 534,00; melhor convênio "Saúde Total: R$ 161"; pior "Vida Care: R$ 110".

## 3. Caixa mês a mês (09 · Caixa da clínica) e repasse (11)

- Saldo em caixa antes do 1º lançamento (01/01/2026): **R$ 26.000**. Lançamentos: 758 linhas; 696 pagas.
| Mês | Entrou | Saiu | Sobrou | Saldo ao fim do mês |
|---|---|---|---|---|
| Janeiro | R$ 25.310 | R$ 35.932 | −R$ 10.622 | R$ 15.378 |
| Fevereiro | R$ 25.650 | R$ 36.231 | −R$ 10.581 | R$ 4.797 |
| Março | R$ 40.540 | R$ 38.251 | R$ 2.289 | R$ 7.086 |
| Abril | R$ 40.775 | R$ 40.254 | R$ 521 | R$ 7.607 |
| Maio | R$ 45.380 | R$ 40.120 | R$ 5.260 | R$ 12.867 |
| Junho | R$ 47.240 | R$ 41.703 | R$ 5.537 | R$ 18.404 |
| Julho | R$ 44.471 | R$ 46.322 | −R$ 1.851 | R$ 16.553 |
| Agosto | R$ 55.841 | R$ 40.869 | R$ 14.972 | R$ 31.526 |
| Setembro | R$ 20.710 | R$ 13.630 | R$ 7.080 | R$ 38.606 |
| **Jan–ago (8 meses fechados)** | **R$ 325.207** | **R$ 319.681** | **R$ 5.526** |  |
| Setembro = até 11/09 (mês em andamento) |  |  |  |  |

**Entradas por categoria (Pago? = Sim)**

| Mês | Particular à vista | Particular a prazo | Convênio · Saúde Total | Convênio · MediPlan | Convênio · Vida Care | Outras entradas | Total |
|---|---|---|---|---|---|---|---|
| Janeiro | R$ 17.220 | R$ 0 | R$ 3.930 | R$ 2.660 | R$ 1.500 | R$ 0 | R$ 25.310 |
| Fevereiro | R$ 16.725 | R$ 1.825 | R$ 3.420 | R$ 2.040 | R$ 1.640 | R$ 0 | R$ 25.650 |
| Março | R$ 30.000 | R$ 3.990 | R$ 3.750 | R$ 1.530 | R$ 1.270 | R$ 0 | R$ 40.540 |
| Abril | R$ 29.830 | R$ 4.160 | R$ 3.295 | R$ 1.555 | R$ 1.315 | R$ 620 | R$ 40.775 |
| Maio | R$ 28.435 | R$ 5.865 | R$ 7.220 | R$ 2.610 | R$ 1.250 | R$ 0 | R$ 45.380 |
| Junho | R$ 31.640 | R$ 7.825 | R$ 4.335 | R$ 2.155 | R$ 1.285 | R$ 0 | R$ 47.240 |
| Julho | R$ 28.710 | R$ 5.960 | R$ 6.655 | R$ 1.570 | R$ 1.576 | R$ 0 | R$ 44.471 |
| Agosto | R$ 40.050 | R$ 4.630 | R$ 7.320 | R$ 2.130 | R$ 1.711 | R$ 0 | R$ 55.841 |
| Setembro | R$ 12.420 | R$ 2.310 | R$ 5.780 | R$ 0 | R$ 200 | R$ 0 | R$ 20.710 |
| **Jan–ago** | **R$ 222.610** | **R$ 34.255** | **R$ 39.925** | **R$ 16.250** | **R$ 11.547** | **R$ 620** | **R$ 325.207** |

**Saídas por categoria (Pago? = Sim)**

| Mês | Pró-labore dos sócios | Custos fixos (8 linhas, 10.000) | Materiais e insumos de atendimento | Taxas de cartão | Repasse à médica parceira | Manutenção de equipamentos | Impostos e taxas | Outras saídas | Total |
|---|---|---|---|---|---|---|---|---|---|
| Janeiro | R$ 18.000 | R$ 10.000 | R$ 1.120 | R$ 82 | R$ 3.100 | R$ 0 | R$ 3.630 | R$ 0 | R$ 35.932 |
| Fevereiro | R$ 18.000 | R$ 10.000 | R$ 820 | R$ 282 | R$ 3.725 | R$ 0 | R$ 2.784 | R$ 620 | R$ 36.231 |
| Março | R$ 20.000 | R$ 10.000 | R$ 1.550 | R$ 274 | R$ 3.255 | R$ 0 | R$ 2.822 | R$ 350 | R$ 38.251 |
| Abril | R$ 18.000 | R$ 10.000 | R$ 1.260 | R$ 485 | R$ 6.050 | R$ 0 | R$ 4.459 | R$ 0 | R$ 40.254 |
| Maio | R$ 18.000 | R$ 10.000 | R$ 1.420 | R$ 478 | R$ 4.385 | R$ 800 | R$ 4.417 | R$ 620 | R$ 40.120 |
| Junho | R$ 19.500 | R$ 10.000 | R$ 1.510 | R$ 456 | R$ 5.245 | R$ 0 | R$ 4.992 | R$ 0 | R$ 41.703 |
| Julho | R$ 24.409 | R$ 10.000 | R$ 1.300 | R$ 347 | R$ 4.720 | R$ 0 | R$ 5.196 | R$ 350 | R$ 46.322 |
| Agosto | R$ 18.000 | R$ 10.000 | R$ 1.380 | R$ 682 | R$ 4.845 | R$ 450 | R$ 4.892 | R$ 620 | R$ 40.869 |
| Setembro | R$ 0 | R$ 7.900 | R$ 540 | R$ 0 | R$ 5.190 | R$ 0 | R$ 0 | R$ 0 | R$ 13.630 |

- "Pró-labore dos sócios" inclui o pró-labore fixo (18.000/mês), as retiradas extras (Paulo 2.000 em 16/03; Carolina 1.500 em 19/06) e a distribuição de lucro dos trimestres fechados (paga dia 10 do mês seguinte, quando o resultado do trimestre após pró-labore passa de R$ 3.000). "Outras saídas" = despesas pessoais dos sócios pagas pela clínica (a acertar). "Outras entradas" = devolução de despesa pessoal (Carolina, 620 em 14/04).
- Guia de impostos: paga dia 20, 11 % das entradas do mês anterior (sem Outras entradas); janeiro sobre dezembro/2025 (fictício, base 33.000). A guia de setembro (20/09) ainda não foi paga. Taxas de cartão: uma saída no último dia do mês (o total da 16). Repasse: dia 10, 50 % da produção da Dra. Renata no mês anterior.
- Setembro: custos fixos com vencimento depois de 11/09, pró-labore (28/09), materiais (22/09) e a guia (20/09) estão como Pago? = Não → **A pagar R$ 26.603**. **A receber (Pago? = Não) R$ 25.467** = lotes de convênio enviados com previsão até 30/09 + parcelas a prazo vencidas e a vencer até 30/09.
- **09 Painel (Config = Setembro)**: Entrou R$ 20.710 · Saiu R$ 13.630 · Sobrou R$ 7.080 · Saldo acumulado **R$ 38.606** · A receber R$ 25.467 · A pagar R$ 26.603.
| Entradas por forma (09, setembro / ano) | No mês | % do mês | No ano | % do ano |
|---|---|---|---|---|
| Pix | R$ 6.530 | 32 % | R$ 134.745 | 39 % |
| Dinheiro | R$ 300 | 1 % | R$ 14.800 | 4 % |
| Cartão de débito | R$ 3.310 | 16 % | R$ 46.970 | 14 % |
| Cartão de crédito | R$ 4.590 | 22 % | R$ 75.700 | 22 % |
| Transferência | R$ 5.980 | 29 % | R$ 73.702 | 21 % |
| Boleto | R$ 0 | 0 % | R$ 0 | 0 % |

| 11 · Parceira (mês / ano até setembro) | Produção no mês | Repasse devido no mês | Produção no ano | Repasse no ano | Pago no ano | A pagar | Fica com a clínica | Material e insumo (ano) | Margem da parceria (ano) | Custo indireto das horas (informativo) |
|---|---|---|---|---|---|---|---|---|---|---|
| Dra. Renata Sousa | R$ 5.850 | R$ 2.925 | R$ 80.680 | R$ 40.340 | R$ 37.415 | R$ 2.925 | R$ 40.340 | R$ 1.226 | R$ 39.114 | R$ 14.600 |

| Repasse (11), mês a mês | Produção | Horas atendidas | Repasse devido (50 %) | Pago em | Valor pago | Fica com a clínica | Material e insumo | Margem da parceria | Custo indireto (inform.) |
|---|---|---|---|---|---|---|---|---|---|
| Janeiro | R$ 7.450 | 17,7 | R$ 3.725 | 10/02/2026 | R$ 3.725 | R$ 3.725 | R$ 106 | R$ 3.619 | R$ 1.264 |
| Fevereiro | R$ 6.510 | 18,3 | R$ 3.255 | 10/03/2026 | R$ 3.255 | R$ 3.255 | R$ 110 | R$ 3.145 | R$ 1.307 |
| Março | R$ 12.100 | 28,0 | R$ 6.050 | 10/04/2026 | R$ 6.050 | R$ 6.050 | R$ 168 | R$ 5.882 | R$ 2.000 |
| Abril | R$ 8.770 | 24,0 | R$ 4.385 | 10/05/2026 | R$ 4.385 | R$ 4.385 | R$ 144 | R$ 4.241 | R$ 1.714 |
| Maio | R$ 10.490 | 26,7 | R$ 5.245 | 10/06/2026 | R$ 5.245 | R$ 5.245 | R$ 160 | R$ 5.085 | R$ 1.907 |
| Junho | R$ 9.440 | 24,0 | R$ 4.720 | 10/07/2026 | R$ 4.720 | R$ 4.720 | R$ 144 | R$ 4.576 | R$ 1.714 |
| Julho | R$ 9.690 | 28,0 | R$ 4.845 | 10/08/2026 | R$ 4.845 | R$ 4.845 | R$ 168 | R$ 4.677 | R$ 2.000 |
| Agosto | R$ 10.380 | 23,7 | R$ 5.190 | 10/09/2026 | R$ 5.190 | R$ 5.190 | R$ 142 | R$ 5.048 | R$ 1.693 |
| Setembro | R$ 5.850 | 14,0 | R$ 2.925 | — | — | R$ 2.925 | R$ 84 | R$ 2.841 | R$ 1.000 |

| 11 · Trimestre | Entradas (sem devoluções) | Saídas sem sócios | Pró-labore fixo | Resultado após pró-labore | Fechado? | Distribuível (50 %) | Já distribuído |
|---|---|---|---|---|---|---|---|
| 1º trimestre | R$ 91.500 | R$ 53.444 | R$ 54.000 | −R$ 15.944 | Sim | R$ 0 | R$ 0 |
| 2º trimestre | R$ 132.775 | R$ 65.957 | R$ 54.000 | R$ 12.818 | Sim | R$ 6.409 | R$ 6.409 |
| 3º trimestre | R$ 121.022 | R$ 57.441 | R$ 54.000 | R$ 9.581 | Em andamento | R$ 0 | R$ 0 |

- 11 KPIs: repasse devido no mês R$ 2.925 (setembro até 11/09, pago em 10/10); a pagar no ano R$ 2.925; pró-labore combinado R$ 18.000/mês; a acertar com a clínica no ano R$ 5.440 (Carolina: retirada extra 1.500 + despesas pessoais 1.860 − devolução 620 = 2.740; Paulo: 2.000 + 700 = 2.700). Setembro: pró-labore ainda não pago (dia 28).

## 4. Agosto de 2026 fechado (18 · Resultado mensal) e julho para comparação

| Linha da DRE | Julho | Agosto | Jan–ago (total) | Média jan–ago |
|---|---|---|---|---|
| Particular à vista | R$ 28.710 | R$ 40.050 | R$ 222.610 | R$ 27.826 |
| Particular a prazo | R$ 5.960 | R$ 4.630 | R$ 34.255 | R$ 4.282 |
| Convênio · Saúde Total | R$ 6.655 | R$ 7.320 | R$ 39.925 | R$ 4.991 |
| Convênio · MediPlan | R$ 1.570 | R$ 2.130 | R$ 16.250 | R$ 2.031 |
| Convênio · Vida Care | R$ 1.576 | R$ 1.711 | R$ 11.547 | R$ 1.443 |
| **Receita total** | R$ 44.471 | R$ 55.841 | R$ 324.587 | R$ 40.573 |
| Reembolsos de sócios (fora da receita e do imposto) | R$ 0 | R$ 0 | R$ 620 | R$ 78 |
| Custos fixos (8 linhas) | R$ 10.000 | R$ 10.000 | R$ 80.000 | R$ 10.000 |
| Materiais e insumos | R$ 1.300 | R$ 1.380 | R$ 10.360 | R$ 1.295 |
| Taxas de cartão | R$ 347 | R$ 682 | R$ 3.085 | R$ 386 |
| Repasse à médica parceira | R$ 4.720 | R$ 4.845 | R$ 35.325 | R$ 4.416 |
| Manutenção de equipamentos | R$ 0 | R$ 450 | R$ 1.250 | R$ 156 |
| **Despesas variáveis** | R$ 6.367 | R$ 7.357 | R$ 50.020 | R$ 6.253 |
| Pró-labore fixo (Carolina 9.000 + Paulo 9.000) | R$ 18.000 | R$ 18.000 | R$ 144.000 | R$ 18.000 |
| Provisão de 13º e férias (planilha 10) | R$ 1.962 | R$ 1.962 | R$ 15.696 | R$ 1.962 |
| Impostos provisionados (11 % da receita) | R$ 4.892 | R$ 6.143 | R$ 35.705 | R$ 4.463 |
| **Total de saídas** | R$ 41.221 | R$ 43.462 | R$ 325.421 | R$ 40.678 |
| **Resultado do mês** | R$ 3.250 | R$ 12.379 | −R$ 834 | −R$ 104 |
| **Margem (resultado ÷ receita)** | **7,3 %** | **22,2 %** | -0,3 % | -6,0 % |

- Agosto: receita **R$ 55.841**, saídas **R$ 43.462**, resultado **R$ 12.379**, margem **22,2 %** (julho: 7,3 %). Previsto de agosto: receita 46.000, custos fixos 10.000, variáveis 6.000, pró-labore 18.000, provisão de 13º e férias 1.962.
| Comparação (18 Painel, agosto) | Mês | Mês anterior | Variação | Previsto | Vs. previsto | Situação |
|---|---|---|---|---|---|---|
| Receita total | R$ 55.841 | R$ 44.471 | +25,6 % | R$ 46.000 | +21,4 % | Dentro do previsto |
| Custos fixos | R$ 10.000 | R$ 10.000 | +0,0 % | R$ 10.000 | +0,0 % | Dentro do previsto |
| Despesas variáveis | R$ 7.357 | R$ 6.367 | +15,5 % | R$ 6.000 | +22,6 % | Fora do previsto |
| Pró-labore | R$ 18.000 | R$ 18.000 | +0,0 % | R$ 18.000 | +0,0 % | Informativo |
| Provisão de 13º e férias | R$ 1.962 | R$ 1.962 | +0,0 % | R$ 1.962 | +0,0 % | Informativo |
| Impostos provisionados | R$ 6.143 | R$ 4.892 | +25,6 % | R$ 5.060 | +21,4 % | Informativo |
| Total de saídas | R$ 43.462 | R$ 41.221 | +5,4 % | R$ 41.022 | +5,9 % | Fora do previsto |
| Resultado do mês | R$ 12.379 | R$ 3.250 | +280,9 % | R$ 4.978 | +148,7 % | Dentro do previsto |
| Margem | 22,2 % | 7,3 % | +14,9 p,p, | 10,8 % | +11,3 p,p, | Dentro do previsto |

- A DRE não inclui retiradas extras, distribuição de lucro nem despesas pessoais dos sócios (ficam na 11); por isso "Saiu no mês" do caixa é diferente do "Total de saídas" da DRE (impostos são provisão de 11 % da receita, e não a guia paga; a provisão de 13º e férias, R$ 1.962/mês, vem da planilha 10 e ainda não saiu do caixa).
- Reembolso de sócio (a devolução de despesa pessoal de 14/04, R$ 620) fica numa linha própria, fora da receita e fora da base do imposto: a "Receita total" da 18 é o "Entrou no mês" da 09 menos essa linha, a mesma base das planilhas 10 e 11.

## 5. A semana de 11/09/2026 (17 · Painel da clínica, aba Dados)

| Indicador | Valor desta sexta | Limite ou meta | Sentido | Situação | Copiado de |
|---|---|---|---|---|---|
| Ocupação da agenda no mês (horas atendidas ÷ disponíveis) | 81,0 % | 75,0 % | Maior é melhor | No alvo | 01 · Agenda e ocupação (Painel: Ocupação) |
| Horas atendidas no mês | 51,8 | — | — | Informativo | 01 · Agenda e ocupação (Painel: Horas atendidas) |
| Horas vazias no mês | 12,2 | — | — | Informativo | 01 · Agenda e ocupação (Painel: Horas vazias) |
| Taxa de falta no mês (faltas ÷ (faltas + realizados)) | 5,3 % | 6,0 % | Menor é melhor | No alvo | 02 · Faltas e retornos (Painel: Taxa de falta) |
| Pacientes na lista de retorno | 8 | 8 | Menor é melhor | Perto | 02 · Faltas e retornos (Painel: Na lista de retorno) |
| Entrou no mês (recebimentos) | R$ 20.710 | — | — | Informativo | 09 · Caixa da clínica (Painel: Entrou no mês) |
| Saiu no mês (tudo o que saiu do caixa) | R$ 13.630 | — | — | Informativo | 09 · Caixa da clínica (Painel: Saiu no mês) |
| Sobrou no mês | R$ 7.080 | — | — | Informativo | calculado aqui |
| Convênio a receber (lotes enviados e não pagos) | R$ 15.758 | — | — | Informativo | 13 · Convênios a receber (Painel: A receber) |
| Convênio atrasado (previsão vencida) | R$ 1.727 | R$ 0 | Menor é melhor | Fora | 13 · Convênios a receber (Painel: Atrasado) |
| Glosa no ano (glosa ÷ (pago + glosa)) | 5,5 % | 4,0 % | Menor é melhor | Fora | 13 · Convênios a receber (Painel: Glosa no ano %) |
| Vencido (parcelas a prazo em atraso) | R$ 3.775 | R$ 4.000 | Menor é melhor | No alvo | 14 · Parcelas e inadimplência (Painel: Vencido) |
| Inadimplência a prazo (vencido ÷ (pago + vencido)) | 9,4 % | 8,0 % | Menor é melhor | Fora | 14 · Parcelas e inadimplência (Painel: Inadimplência) |
| Orçamentos em aberto (quantidade) | 6 | — | — | Informativo | 15 · Orçamentos (Painel: Apresentado + Em análise) |
| Orçamentos em aberto (valor) | R$ 3.460 | — | — | Informativo | 15 · Orçamentos (Painel: Em aberto) |

### Agenda (01 · Agenda e ocupação, Config = Setembro, horas disponíveis até ontem)

- **Horas disponíveis 64,0 · atendidas 51,8 · ocupação 81,0 % · vazias 12,2 · faltas 6 · produção R$ 20.045**. Agenda: 1239 linhas de 01/06 a 05/10/2026 (895 realizados, 78 faltas, 222 agendados/confirmados). Pacientes cadastrados: 156.
| Por profissional (01, setembro) | Disponíveis | Atendidas | Ocupação | Realizados | Faltas | Taxa de falta | Produção |
|---|---|---|---|---|---|---|---|
| Dra. Carolina Mendes | 24,0 | 22,0 | 92 % | 47 | 1 | 2 % | R$ 10.050 |
| Dr. Paulo Andrade | 24,0 | 15,8 | 66 % | 36 | 4 | 10 % | R$ 4.145 |
| Dra. Renata Sousa | 16,0 | 14,0 | 88 % | 24 | 1 | 4 % | R$ 5.850 |

| Por sala (01, setembro) | Disponíveis | Atendidas | Ocupação | Vazias | Turnos por semana |
|---|---|---|---|---|---|
| Sala 1 | 40,0 | 36,0 | 90 % | 4,0 | 6 |
| Sala 2 | 24,0 | 15,8 | 66 % | 8,2 | 4 |

| Dia (01, setembro) | Manhã disp. | Manhã atend. | Manhã ocup. | Tarde disp. | Tarde atend. | Tarde ocup. | Faltas |
|---|---|---|---|---|---|---|---|
| Segunda | 0,0 | 0,0 | — | 0,0 | 0,0 | — | 0 |
| Terça | 8,0 | 6,8 | 85 % | 16,0 | 13,0 | 81 % | 2 |
| Quarta | 0,0 | 0,0 | — | 8,0 | 7,8 | 98 % | 0 |
| Quinta | 8,0 | 7,3 | 92 % | 16,0 | 11,7 | 73 % | 2 |
| Sexta | 8,0 | 5,2 | 65 % | 0,0 | 0,0 | — | 2 |

| Procedimento (01, setembro) | Realizados | Horas | Produção | Valor médio |
|---|---|---|---|---|
| Consulta | 49 | 24,5 | R$ 11.240 | R$ 229 |
| Retorno | 23 | 7,7 | R$ 0 | R$ 0 |
| ECG | 5 | 1,7 | R$ 375 | R$ 75 |
| MAPA | 5 | 1,7 | R$ 1.060 | R$ 212 |
| Holter | 1 | 0,3 | R$ 105 | R$ 105 |
| Teste ergométrico | 6 | 4,0 | R$ 1.415 | R$ 236 |
| Avaliação endócrina | 18 | 12,0 | R$ 5.850 | R$ 325 |

| Pagador (01, setembro) | Realizados | Horas | Faltas | Taxa de falta | Produção | Valor médio | % da produção |
|---|---|---|---|---|---|---|---|
| Particular | 55 | 27,0 | 2 | 4 % | R$ 15.620 | R$ 284 | 78 % |
| Saúde Total | 26 | 12,8 | 2 | 7 % | R$ 2.435 | R$ 94 | 12 % |
| MediPlan | 19 | 8,7 | 1 | 5 % | R$ 1.445 | R$ 76 | 7 % |
| Vida Care | 7 | 3,3 | 1 | 12 % | R$ 545 | R$ 78 | 3 % |

| Próximos 7 dias (01) | Data | Agendados | Confirmados | Horas marcadas | Horas de turno | Vagas (h) |
|---|---|---|---|---|---|---|
| Segunda | 14/09/2026 | 4 | 11 | 6,7 | 8,0 | 1,3 |
| Terça | 15/09/2026 | 5 | 17 | 10,7 | 12,0 | 1,3 |
| Quarta | 16/09/2026 | 2 | 5 | 3,0 | 4,0 | 1,0 |
| Quinta | 17/09/2026 | 19 | 0 | 9,2 | 12,0 | 2,8 |
| Sexta | 18/09/2026 | 9 | 0 | 3,5 | 4,0 | 0,5 |
| Sábado | 19/09/2026 | 0 | 0 | 0,0 | 0,0 | 0,0 |
| Domingo | 20/09/2026 | 0 | 0 | 0,0 | 0,0 | 0,0 |

- **Julho fechado (01 com Config = Julho)**: disponíveis 180,0 h · atendidas 129,0 h · ocupação 71,7 % · faltas 26 (8,8 %) · produção R$ 52.740.
- **Agosto fechado (01 com Config = Agosto)**: disponíveis 168,0 h · atendidas 118,3 h · ocupação 70,4 % · faltas 23 (8,4 %) · produção R$ 48.631.
### Faltas e retornos (02, Config = Setembro)

- **Taxa de falta 5,3 % · faltas 6 · realizados 107 · cancelamentos 3 · remarcações 0 · na lista de retorno 8**.
| Dia da semana (02, setembro) | Realizados | Faltas | Taxa de falta | Cancel. | Remarc. |
|---|---|---|---|---|---|
| Segunda | 0 | 0 | — | 0 | 0 |
| Terça | 41 | 2 | 4,7 % | 2 | 0 |
| Quarta | 17 | 0 | 0,0 % | 0 | 0 |
| Quinta | 38 | 2 | 5,0 % | 0 | 0 |
| Sexta | 11 | 2 | 15,4 % | 1 | 0 |

| Pagador (02, setembro) | Realizados | Faltas | Taxa de falta |
|---|---|---|---|
| Particular | 55 | 2 | 3,5 % |
| Saúde Total | 26 | 2 | 7,1 % |
| MediPlan | 19 | 1 | 5,0 % |
| Vida Care | 7 | 1 | 12,5 % |

| Profissional (02, setembro) | Realizados | Faltas | Taxa de falta |
|---|---|---|---|
| Dra. Carolina Mendes | 47 | 1 | 2,1 % |
| Dr. Paulo Andrade | 36 | 4 | 10,0 % |
| Dra. Renata Sousa | 24 | 1 | 4,0 % |

| Últimas 8 semanas (02) | Segunda-feira | Realizados | Faltas | Taxa de falta |
|---|---|---|---|---|
| S27/07 | 27/07/2026 | 57 | 7 | 10,9 % |
| S03/08 | 03/08/2026 | 58 | 6 | 9,4 % |
| S10/08 | 10/08/2026 | 64 | 5 | 7,2 % |
| S17/08 | 17/08/2026 | 52 | 6 | 10,3 % |
| S24/08 | 24/08/2026 | 64 | 6 | 8,6 % |
| S31/08 | 31/08/2026 | 72 | 3 | 4,0 % |
| S07/09 | 07/09/2026 | 49 | 3 | 5,8 % |
| S14/09 | 14/09/2026 | 0 | 0 | — |

| Lista de retorno (02) | Profissional | Pagador | Último atendimento | Procedimento | Retorno previsto | Dias além |
|---|---|---|---|---|---|---|
| Gabriel Fernandes | Dr. Paulo Andrade | Particular | 25/06/2026 | Consulta | 25/07/2026 | 51 |
| Priscila Pinto | Dr. Paulo Andrade | Saúde Total | 09/07/2026 | Consulta | 08/08/2026 | 37 |
| Roberta Almeida | Dr. Paulo Andrade | Saúde Total | 27/07/2026 | Consulta | 26/08/2026 | 19 |
| Rafael Araújo | Dr. Paulo Andrade | MediPlan | 31/07/2026 | Consulta | 30/08/2026 | 15 |
| Viviane Teixeira | Dr. Paulo Andrade | Particular | 04/08/2026 | Consulta | 03/09/2026 | 11 |
| Patrícia Vieira | Dr. Paulo Andrade | Saúde Total | 07/08/2026 | Consulta | 06/09/2026 | 8 |
| Tatiana Rocha | Dra. Carolina Mendes | Vida Care | 11/08/2026 | Consulta | 10/09/2026 | 4 |
| Paulo Freitas | Dra. Renata Sousa | Saúde Total | 30/07/2026 | Avaliação endócrina | 13/09/2026 | 1 |

### Caixa, convênios, parcelas e orçamentos na sexta

- Caixa de setembro até 11/09 (09): entrou **R$ 20.710**, saiu **R$ 13.630**, sobrou R$ 7.080; saldo acumulado R$ 38.606.
- Convênios (13): **a receber R$ 15.758** (lotes enviados e não pagos) · **atrasado R$ 1.727** (lote de junho da Vida Care) · recebido no ano R$ 73.702 · glosa no ano R$ 4.273 (**5,5 %**) · em recurso R$ 240.
- Parcelas a prazo (14): vence em 7 dias R$ 970 · vence em 30 dias R$ 4.705 · em aberto (total) R$ 9.855 · **vencido R$ 3.775** em **14 parcelas** · **inadimplência 9,4 %** = R$ 3.775 ÷ (R$ 36.565 pago + R$ 3.775).
- Orçamentos (15): em aberto **R$ 3.460** · previsão ponderada R$ 1.318 · **aprovado no trimestre R$ 8.960** (50 % da meta de R$ 18.000) · taxa de aprovação 73 % · dias até decidir (média) 11.

## 6. Convênios (13 · Convênios a receber)

| Convênio | Prazo (dias) | Glosa histórica (Config) | Lotes no ano | Enviado | Pago | Glosa | Glosa % | Recuperado | A receber | Atrasado | Prazo real (média) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Saúde Total | 30 | 3 % | 9 | R$ 47.560 | R$ 45.565 | R$ 1.550 | 3,3 % | R$ 140 | R$ 4.555 | R$ 0 | 32 |
| MediPlan | 45 | 6 % | 9 | R$ 20.985 | R$ 16.120 | R$ 1.300 | 7,5 % | R$ 130 | R$ 6.305 | R$ 0 | 47 |
| Vida Care | 60 | 10 % | 9 | R$ 14.228 | R$ 11.217 | R$ 1.423 | 11,3 % | R$ 530 | R$ 4.898 | R$ 1.727 | 61 |

| Lote | Competência | Guias | Enviado | Envio | Previsão | Pagamento | Pago | Glosa | Recurso | Recuperado | Recebido em | Situação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Saúde Total | out/2025 | 46 | R$ 4.290 | 05/11/2025 | 05/12/2025 | 08/12/2025 | R$ 4.180 | R$ 110 | — | — | — | Paga com glosa |
| MediPlan | out/2025 | 31 | R$ 2.580 | 05/11/2025 | 20/12/2025 | 22/12/2025 | R$ 2.440 | R$ 140 | — | — | — | Paga com glosa |
| Vida Care | out/2025 | 22 | R$ 1.730 | 05/11/2025 | 04/01/2026 | 05/01/2026 | R$ 1.500 | R$ 230 | Aceito | R$ 140 | 06/02/2026 | Paga com glosa |
| Saúde Total | nov/2025 | 44 | R$ 4.110 | 05/12/2025 | 04/01/2026 | 07/01/2026 | R$ 3.930 | R$ 180 | — | — | — | Paga com glosa |
| MediPlan | nov/2025 | 33 | R$ 2.740 | 05/12/2025 | 19/01/2026 | 21/01/2026 | R$ 2.660 | R$ 80 | — | — | — | Paga com glosa |
| Vida Care | nov/2025 | 20 | R$ 1.580 | 05/12/2025 | 03/02/2026 | 03/02/2026 | R$ 1.500 | R$ 80 | — | — | — | Paga com glosa |
| Saúde Total | dez/2025 | 38 | R$ 3.560 | 05/01/2026 | 04/02/2026 | 04/02/2026 | R$ 3.420 | R$ 140 | — | — | — | Paga com glosa |
| MediPlan | dez/2025 | 27 | R$ 2.250 | 05/01/2026 | 19/02/2026 | 20/02/2026 | R$ 2.040 | R$ 210 | Negado | — | — | Paga com glosa |
| Vida Care | dez/2025 | 17 | R$ 1.350 | 05/01/2026 | 06/03/2026 | 09/03/2026 | R$ 1.270 | R$ 80 | — | — | — | Paga com glosa |
| Saúde Total | jan/2026 | 34 | R$ 3.830 | 05/02/2026 | 07/03/2026 | 10/03/2026 | R$ 3.750 | R$ 80 | — | — | — | Paga com glosa |
| MediPlan | jan/2026 | 18 | R$ 1.600 | 05/02/2026 | 22/03/2026 | 25/03/2026 | R$ 1.530 | R$ 70 | — | — | — | Paga com glosa |
| Vida Care | jan/2026 | 17 | R$ 1.570 | 05/02/2026 | 06/04/2026 | 06/04/2026 | R$ 1.315 | R$ 255 | Aceito | R$ 190 | 15/05/2026 | Paga com glosa |
| Saúde Total | fev/2026 | 30 | R$ 3.455 | 05/03/2026 | 04/04/2026 | 06/04/2026 | R$ 3.295 | R$ 160 | — | — | — | Paga com glosa |
| MediPlan | fev/2026 | 17 | R$ 1.655 | 05/03/2026 | 19/04/2026 | 22/04/2026 | R$ 1.555 | R$ 100 | — | — | — | Paga com glosa |
| Vida Care | fev/2026 | 15 | R$ 1.156 | 05/03/2026 | 04/05/2026 | 04/05/2026 | R$ 1.060 | R$ 96 | — | — | — | Paga com glosa |
| Saúde Total | mar/2026 | 65 | R$ 7.455 | 06/04/2026 | 06/05/2026 | 08/05/2026 | R$ 7.220 | R$ 235 | Aceito | R$ 140 | 09/06/2026 | Paga com glosa |
| MediPlan | mar/2026 | 31 | R$ 2.845 | 06/04/2026 | 21/05/2026 | 22/05/2026 | R$ 2.610 | R$ 235 | Aceito | R$ 130 | 24/06/2026 | Paga com glosa |
| Vida Care | mar/2026 | 17 | R$ 1.555 | 06/04/2026 | 05/06/2026 | 05/06/2026 | R$ 1.285 | R$ 270 | Negado | — | — | Paga com glosa |
| Saúde Total | abr/2026 | 39 | R$ 4.410 | 05/05/2026 | 04/06/2026 | 08/06/2026 | R$ 4.195 | R$ 215 | Negado | — | — | Paga com glosa |
| MediPlan | abr/2026 | 26 | R$ 2.310 | 05/05/2026 | 19/06/2026 | 22/06/2026 | R$ 2.025 | R$ 285 | Negado | — | — | Paga com glosa |
| Vida Care | abr/2026 | 21 | R$ 1.698 | 05/05/2026 | 04/07/2026 | 06/07/2026 | R$ 1.576 | R$ 122 | — | — | — | Paga com glosa |
| Saúde Total | mai/2026 | 57 | R$ 6.785 | 05/06/2026 | 05/07/2026 | 06/07/2026 | R$ 6.655 | R$ 130 | — | — | — | Paga com glosa |
| MediPlan | mai/2026 | 19 | R$ 1.755 | 05/06/2026 | 20/07/2026 | 20/07/2026 | R$ 1.570 | R$ 185 | — | — | — | Paga com glosa |
| Vida Care | mai/2026 | 24 | R$ 2.001 | 05/06/2026 | 04/08/2026 | 05/08/2026 | R$ 1.711 | R$ 290 | Aceito | R$ 200 | 08/09/2026 | Paga com glosa |
| Saúde Total | jun/2026 | 70 | R$ 7.560 | 06/07/2026 | 05/08/2026 | 05/08/2026 | R$ 7.320 | R$ 240 | Em recurso | — | — | Em recurso |
| MediPlan | jun/2026 | 25 | R$ 2.265 | 06/07/2026 | 20/08/2026 | 20/08/2026 | R$ 2.130 | R$ 135 | — | — | — | Paga com glosa |
| Vida Care | jun/2026 | 19 | R$ 1.727 | 06/07/2026 | 04/09/2026 | — | — | — | — | — | — | Atrasada |
| Saúde Total | jul/2026 | 49 | R$ 5.950 | 05/08/2026 | 04/09/2026 | 08/09/2026 | R$ 5.780 | R$ 170 | — | — | — | Paga com glosa |
| MediPlan | jul/2026 | 31 | R$ 2.875 | 05/08/2026 | 19/09/2026 | — | — | — | — | — | — | Aguardando |
| Vida Care | jul/2026 | 20 | R$ 1.525 | 05/08/2026 | 04/10/2026 | — | — | — | — | — | — | Aguardando |
| Saúde Total | ago/2026 | 43 | R$ 4.555 | 08/09/2026 | 08/10/2026 | — | — | — | — | — | — | Aguardando |
| MediPlan | ago/2026 | 34 | R$ 3.430 | 08/09/2026 | 23/10/2026 | — | — | — | — | — | — | Aguardando |
| Vida Care | ago/2026 | 20 | R$ 1.646 | 08/09/2026 | 07/11/2026 | — | — | — | — | — | — | Aguardando |
| Saúde Total | set/2026 | 21 | R$ 2.435 | — | — | — | — | — | — | — | — | Em separação |
| MediPlan | set/2026 | 15 | R$ 1.445 | — | — | — | — | — | — | — | — | Em separação |
| Vida Care | set/2026 | 6 | R$ 545 | — | — | — | — | — | — | — | — | Em separação |

- Guias na aba Guias (jun–set): 353 (uma por atendimento de convênio realizado); glosadas: 6. Lotes de out/2025 a mai/2026 vêm dos registros anteriores à agenda (sem detalhe por guia).
| Guias glosadas para recorrer (13 Painel) | Data | Paciente | Convênio | Procedimento | Profissional | Valor | Recurso |
|---|---|---|---|---|---|---|---|
| G2026-0577 | 09/07/2026 | Isabela Barbosa | Saúde Total | Avaliação endócrina | Dra. Renata Sousa | R$ 130 | — |
| G2026-0495 | 18/06/2026 | Daniel Melo | Saúde Total | Consulta | Dra. Carolina Mendes | R$ 120 | Em recurso |
| G2026-0481 | 16/06/2026 | Carlos Castro | Saúde Total | Consulta | Dra. Carolina Mendes | R$ 120 | Em recurso |
| G2026-0483 | 16/06/2026 | Sérgio Teixeira | MediPlan | Consulta | Dr. Paulo Andrade | R$ 100 | — |
| G2026-0582 | 10/07/2026 | Débora Machado | Saúde Total | ECG | Dr. Paulo Andrade | R$ 40 | — |
| G2026-0527 | 25/06/2026 | Sérgio Batista | MediPlan | ECG | Dr. Paulo Andrade | R$ 35 | — |


## 7. Parcelas a prazo e inadimplência (14)

| Faixa de atraso | Parcelas | Valor | % do vencido |
|---|---|---|---|
| 1 a 6 dias | 2 | R$ 320 | 8 % |
| 7 a 14 dias | 0 | R$ 0 | 0 % |
| 15 a 29 dias | 0 | R$ 0 | 0 % |
| 30 dias ou mais | 12 | R$ 3.455 | 92 % |
| Antes da régua | 0 | R$ 0 | 0 % |

| Cobrar primeiro (14) | Paciente | Procedimento | Parcela | Vencimento | Valor | Dias de atraso | Faixa |
|---|---|---|---|---|---|---|---|
| 1 | Gabriel Reis | Avaliação endócrina | 1 | 09/04/2026 | R$ 400 | 158 | 30 dias ou mais |
| 2 | Priscila Reis | Avaliação endócrina | 1 | 07/05/2026 | R$ 400 | 130 | 30 dias ou mais |
| 3 | Márcia Duarte | Avaliação endócrina | 1 | 12/02/2026 | R$ 200 | 214 | 30 dias ou mais |
| 4 | Helena Moreira | Consulta | 1 | 13/06/2026 | R$ 380 | 93 | 30 dias ou mais |
| 5 | Mônica Martins | Consulta | 1 | 13/03/2026 | R$ 190 | 185 | 30 dias ou mais |
| 6 | Mariana Nascimento | Consulta | 1 | 19/06/2026 | R$ 380 | 87 | 30 dias ou mais |
| 7 | Mariana Nascimento | Consulta | 1 | 27/06/2026 | R$ 380 | 79 | 30 dias ou mais |
| 8 | Patrícia Fernandes | Consulta | 2 | 18/05/2026 | R$ 190 | 119 | 30 dias ou mais |
| 9 | Rafael Dias | Consulta | 2 | 23/05/2026 | R$ 190 | 114 | 30 dias ou mais |
| 10 | Cláudia Costa | Consulta | 1 | 22/07/2026 | R$ 380 | 54 | 30 dias ou mais |

| Vencem nos próximos 30 dias (14) | Paciente | Procedimento | Parcela | Vencimento | Valor | Dias para vencer |
|---|---|---|---|---|---|---|
| 1 | Elaine Cardoso | Consulta | 1 | 16/09/2026 | R$ 190 | 2 |
| 2 | Fábio Gomes | Avaliação endócrina | 1 | 17/09/2026 | R$ 400 | 3 |
| 3 | Eduardo Lima | Consulta | 1 | 19/09/2026 | R$ 380 | 5 |
| 4 | Eduardo Lima | Teste ergométrico | 2 | 22/09/2026 | R$ 225 | 8 |
| 5 | Cláudia Santos | Consulta | 1 | 23/09/2026 | R$ 380 | 9 |
| 6 | Rodrigo Moreira | Teste ergométrico | 2 | 25/09/2026 | R$ 225 | 11 |
| 7 | Sérgio Martins | Consulta | 1 | 25/09/2026 | R$ 380 | 11 |
| 8 | Rafael Pereira | Avaliação endócrina | 2 | 26/09/2026 | R$ 200 | 12 |

- Total de parcelas cadastradas: 173 (pagas 134), de 60 pacientes; 55 atendimentos em 2 parcelas. Régua de cobrança: 1 dia (lembrete), 7 dias (mensagem da recepção), 15 dias (ligação com demonstrativo), 30 dias (conversa e plano de pagamento).

## 8. Orçamentos (15 · Apresentados × aprovados)

| Etapa (15) | Orçamentos | Valor | Ponderado |
|---|---|---|---|
| Apresentado | 3 | R$ 2.060 | R$ 618 |
| Em análise | 3 | R$ 1.400 | R$ 700 |
| Aprovado (total) | 22 | R$ 8.960 | — |
| Recusado (total) | 5 | R$ 1.860 | — |
| Sem retorno (total) | 3 | R$ 1.660 | — |
| Valor médio dos aprovados | R$ 407 |  |  |

| Data | Paciente | Profissional | Tipo | Itens | Valor | Etapa | Decisão | Motivo | Observação |
|---|---|---|---|---|---|---|---|---|---|
| 25/06/2026 | Helena Moreira | Dr. Paulo Andrade | Exame cardiológico | MAPA | R$ 300 | Aprovado | 13/07/2026 | — | Agendado para 14/07 |
| 26/06/2026 | Gustavo Ferreira | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Aprovado | 08/07/2026 | — | Agendado para 09/07 |
| 06/07/2026 (-70 dias) | Ana Costa | Dr. Paulo Andrade | Exame cardiológico | MAPA | R$ 300 | Recusado | 11/07/2026 (-65 dias) | Preço | — |
| 13/07/2026 | Débora Ramos | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 17/07/2026 | — | Agendado para 20/07 |
| 14/07/2026 | Wagner Santos | Dr. Paulo Andrade | Exame cardiológico | MAPA | R$ 300 | Aprovado | 31/07/2026 | — | Agendado para 03/08 |
| 15/07/2026 | Lucas Lopes | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 21/07/2026 | — | Agendado para 24/07 |
| 15/07/2026 | Eduardo Lima | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 22/07/2026 | — | Agendado para 24/07 |
| 16/07/2026 | Otávio Nascimento | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Aprovado | 24/07/2026 | — | Agendado para 28/07 |
| 21/07/2026 (-55 dias) | Carlos Freitas | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Recusado | 25/07/2026 (-51 dias) | Vai fazer pelo convênio | — |
| 31/07/2026 | Regina Duarte | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 07/08/2026 | — | Agendado para 11/08 |
| 31/07/2026 (-45 dias) | Cláudia Costa | Dra. Carolina Mendes | Pacote de consultas | Consulta + 2 retornos (acompanhamento) | R$ 380 | Recusado | 04/08/2026 (-41 dias) | Sem indicação no momento | — |
| 03/08/2026 | Helena Moreira | Dr. Paulo Andrade | Exame cardiológico | MAPA | R$ 300 | Aprovado | 14/08/2026 | — | Agendado para 17/08 |
| 05/08/2026 (-40 dias) | Eduardo Lima | Dr. Paulo Andrade | Check-up cardiológico | Consulta + ECG + teste ergométrico | R$ 960 | Sem retorno | 15/08/2026 (-30 dias) | Vai pensar / sem retorno | — |
| 07/08/2026 | Regina Teixeira | Dr. Paulo Andrade | Check-up cardiológico | Consulta + ECG + teste ergométrico | R$ 960 | Aprovado | 18/08/2026 | — | Agendado para 20/08 |
| 07/08/2026 | Sérgio Martins | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Aprovado | 21/08/2026 | — | Agendado para 24/08 |
| 13/08/2026 | Roberta Araújo | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Aprovado | 24/08/2026 | — | Agendado para 25/08 |
| 13/08/2026 (-32 dias) | Fábio Machado | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Recusado | 22/08/2026 (-23 dias) | Fez em outro lugar | — |
| 14/08/2026 | Rafael Barros | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 31/08/2026 | — | Agendado para 03/09 |
| 14/08/2026 | Rafael Dias | Dr. Paulo Andrade | Exame cardiológico | MAPA | R$ 300 | Aprovado | 03/09/2026 | — | Agendado para 04/09 |
| 17/08/2026 | Paulo Reis | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Aprovado | 24/08/2026 | — | Agendado para 25/08 |
| 19/08/2026 (-26 dias) | Beatriz Gomes | Dra. Renata Sousa | Avaliação endócrina | Avaliação endócrina + retorno | R$ 400 | Sem retorno | 28/08/2026 (-17 dias) | Vai pensar / sem retorno | — |
| 21/08/2026 | Fernanda Freitas | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 02/09/2026 | — | Agendado para 04/09 |
| 24/08/2026 | Rodrigo Moreira | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 10/09/2026 | — | Agendado para 02/10 |
| 25/08/2026 (-20 dias) | Carlos Fernandes | Dra. Carolina Mendes | Pacote de consultas | Consulta + 2 retornos (acompanhamento) | R$ 380 | Recusado | 28/08/2026 (-17 dias) | Preço | — |
| 28/08/2026 | Leandro Oliveira | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 11/09/2026 | — | Agendado para 22/09 |
| 28/08/2026 | Gisele Ribeiro | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Aprovado | 10/09/2026 | — | Agendado para 05/10 |
| 29/08/2026 (-16 dias) | Patrícia Dias | Dr. Paulo Andrade | Exame cardiológico | MAPA | R$ 300 | Sem retorno | 05/09/2026 (-9 dias) | Vai pensar / sem retorno | — |
| 31/08/2026 | Lucas Lopes | Dr. Paulo Andrade | Exame cardiológico | MAPA | R$ 300 | Aprovado | 10/09/2026 | — | Agendado para 01/10 |
| 01/09/2026 | Paulo Reis | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Aprovado | 09/09/2026 | — | Agendado para 17/09 |
| 02/09/2026 (-12 dias) | Mariana Reis | Dr. Paulo Andrade | Exame cardiológico | MAPA + Holter | R$ 650 | Em análise | — | — | — |
| 04/09/2026 | Wagner Lima | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Aprovado | 10/09/2026 | — | Agendado para 22/09 |
| 05/09/2026 (-9 dias) | Beatriz Monteiro | Dra. Renata Sousa | Avaliação endócrina | Avaliação endócrina + retorno | R$ 400 | Em análise | — | — | — |
| 08/09/2026 (-6 dias) | Rafael Dias | Dr. Paulo Andrade | Exame cardiológico | Holter | R$ 350 | Em análise | — | — | — |
| 11/09/2026 (-3 dias) | Roberta Lima | Dr. Paulo Andrade | Check-up cardiológico | Consulta + ECG + teste ergométrico | R$ 960 | Apresentado | — | — | — |
| 13/09/2026 (-1 dia) | Wagner Costa | Dr. Paulo Andrade | Exame cardiológico | Teste ergométrico | R$ 450 | Apresentado | — | — | — |
| 14/09/2026 (hoje) | Fábio Correia | Dr. Paulo Andrade | Exame cardiológico | MAPA + Holter | R$ 650 | Apresentado | — | — | — |

| Por tipo (15) | Orçamentos | Aprovados | Recusados / sem retorno | Taxa de aprovação | Valor aprovado | Em aberto |
|---|---|---|---|---|---|---|
| Check-up cardiológico | 3 | 1 | 1 | 50 % | R$ 960 | R$ 960 |
| Exame cardiológico | 29 | 21 | 4 | 84 % | R$ 8.000 | R$ 2.100 |
| Avaliação endócrina | 2 | 0 | 1 | 0 % | R$ 0 | R$ 400 |
| Pacote de consultas | 2 | 0 | 2 | 0 % | R$ 0 | R$ 0 |

| Motivo de recusa (15) | Recusados | Valor | % dos recusados |
|---|---|---|---|
| Preço | 2 | R$ 680 | 25 % |
| Vai fazer pelo convênio | 1 | R$ 350 | 12 % |
| Vai pensar / sem retorno | 3 | R$ 1.660 | 38 % |
| Fez em outro lugar | 1 | R$ 450 | 12 % |
| Sem indicação no momento | 1 | R$ 380 | 12 % |


## 9. Cartão e taxas (16 · Conciliação, Config = Agosto)

- **Agosto**: vendas no cartão e Pix R$ 31.820 · taxas **R$ 484,12** (1,52 %) · líquido R$ 31.335,88 · ainda vai cair R$ 12.388,26 · a conferir R$ 4.758,98. "As taxas das vendas do mês equivalem a 1,3 consultas particulares. Para o caixa (09), a saída 'Taxas de cartão' do mês é R$ 681,60: é a taxa das liquidações que caíram neste mês, e não a das vendas feitas nele."
| Tipo (16, agosto) | Vendas | Bruto | Taxas | Taxa média | Líquido | % do bruto |
|---|---|---|---|---|---|---|
| Pix | 37 | R$ 13.380 | R$ 0,00 | 0,00 % | R$ 13.380 | 42 % |
| Cartão de débito | 22 | R$ 8.090 | R$ 121,35 | 1,50 % | R$ 7.969 | 25 % |
| Cartão de crédito à vista | 16 | R$ 5.840 | R$ 186,88 | 3,20 % | R$ 5.653 | 18 % |
| Cartão de crédito parcelado | 12 | R$ 4.510 | R$ 175,89 | 3,90 % | R$ 4.334 | 14 % |

- Taxas do exemplo (Config): Pix 0 %, débito 1,5 % (D+1), crédito à vista 3,2 % (D+30), crédito parcelado 3,9 % (parcelas de 30 em 30 dias); sem antecipação. Vendas na aba: 298 (01/06 a 11/09). Taxas de julho (saída do caixa em 31/07): R$ 346,61; de agosto (31/08): R$ 681,60.

## 10. Metas do trimestre (19), reserva (12) e provisão (10)

- 3º trimestre de 2026 (01/07 a 30/09): semana **11 de 13**, 82 % decorrido. Resultados-chave: 9 · atingidos 1 · em risco 6 · progresso médio 44 %.
| Objetivo | Resultado-chave | Dono | Unid. | Partida (30/06) | Meta | Atual (14/09) | Progresso | Semáforo | Sentido | S1…S11 (sextas 03/07 → 11/09; S11 = atual) |
|---|---|---|---|---|---|---|---|---|---|---|
| Agenda cheia, sem faltas | Ocupação da agenda nas últimas 4 semanas (%) | Bruna | % | 75,2 | 80,0 | 74,5 | 0 % | Em risco | Maior é melhor | 75,2 · 74,5 · 71,7 · 72,6 · 71,7 · 70,8 · 72,0 · 68,1 · 70,3 · 74,5 · 74,5 |
| Convênio sob controle | Glosa nos lotes pagos no ano (%) | Paulo | % | 6,1 | 4,0 | 5,5 | 29 % | Em risco | Menor é melhor | 6,1 · 5,6 · 5,6 · 5,8 · 5,8 · 5,8 · 5,8 · 5,8 · 5,8 · 5,8 · 5,5 |
| Caixa previsível | Inadimplência a prazo: vencido ÷ (pago + vencido) (%) | Carolina | % | 10,9 | 8,0 | 9,4 | 52 % | Em risco | Menor é melhor | 10,6 · 9,8 · 10,9 · 10,7 · 10,0 · 10,9 · 9,5 · 10,8 · 10,1 · 8,8 · 9,4 |

- **12 Reserva**: meta 3 meses de custo fixo + pró-labore × custo fixo + pró-labore médio R$ 30.636 (jun/jul/ago, como a 09 mostra) = **R$ 91.909**; reserva hoje **R$ 14.000**; falta R$ 77.909; cobre **0,5 meses**; semáforo "Vermelho: menos de 1 mês de custo fixo + pró-labore guardado"; com aporte de R$ 3.000/mês a meta chega em **Novembro/2028**. Saldo em caixa R$ 38.606 − compromissos não pagos R$ 26.603 = caixa livre R$ 12.003.
| Meta de caixa do trimestre (12) | Alvo | Atual | Progresso | Prazo | Situação |
|---|---|---|---|---|---|
| Reserva com 1 mês de custo fixo + pró-labore | R$ 28.000 | R$ 14.000 | 50 % | 31/12/2026 | Em andamento |
| Receber R$ 130.000 no trimestre | R$ 130.000 | R$ 121.022 | 93 % | 30/09/2026 | Em andamento |
| Conta de provisão de impostos com o saldo de agosto (planilha 10) | R$ 18.209 | R$ 17.500 | 96 % | 30/09/2026 | Em andamento |

- **10 Provisão (Config = Setembro, alíquota 11 %)**: 13º dos sócios 750 + 750 (reserva de dezembro decidida pelos sócios) e da recepcionista 198,00 (com FGTS), férias da recepcionista 264,00 por mês; entradas de setembro até 11/09 R$ 20.710; a separar no mês R$ 4.240; **saldo provisionado ao fim de setembro R$ 22.449**; compromisso do mês seguinte R$ 2.278; situação Coberto.
| Mês (10) | Entradas (sem Outras) | Provisão 11 % | Total a separar | Guia paga no mês | Saldo provisionado |
|---|---|---|---|---|---|
| Janeiro | R$ 25.310 | R$ 2.784 | R$ 4.746 | R$ 3.630 | R$ 1.116 |
| Fevereiro | R$ 25.650 | R$ 2.822 | R$ 4.784 | R$ 2.784 | R$ 3.116 |
| Março | R$ 40.540 | R$ 4.459 | R$ 6.421 | R$ 2.822 | R$ 6.715 |
| Abril | R$ 40.155 | R$ 4.417 | R$ 6.379 | R$ 4.459 | R$ 8.635 |
| Maio | R$ 45.380 | R$ 4.992 | R$ 6.954 | R$ 4.417 | R$ 11.172 |
| Junho | R$ 47.240 | R$ 5.196 | R$ 7.158 | R$ 4.992 | R$ 13.338 |
| Julho | R$ 44.471 | R$ 4.892 | R$ 6.854 | R$ 5.196 | R$ 14.996 |
| Agosto | R$ 55.841 | R$ 6.143 | R$ 8.105 | R$ 4.892 | R$ 18.209 |
| Setembro | R$ 20.710 | R$ 2.278 | R$ 4.240 | R$ 0 | R$ 22.449 |


## 11. Resumo do mês (20): agosto × julho de 2026

| Indicador | Agosto | Julho | Variação | Meta | Vs. meta | Situação |
|---|---|---|---|---|---|---|
| Entrou no mês (recebimentos) | R$ 55,841 | R$ 44,471 | +25.6% | R$ 46,000 | +21.4% | No alvo |
| Saídas do mês (custos, variáveis, pró-labore, provisões e impostos) | R$ 43,462 | R$ 41,221 | +5.4% | R$ 44,000 | -1.2% | No alvo |
| Resultado do mês | R$ 12,379 | R$ 3,250 | +280.9% | R$ 5,000 | +147.6% | No alvo |
| Margem do mês | 22.2% | 7.3% | +14.9 p.p. | 12.0% | +10.2 p.p. | No alvo |
| Ocupação da agenda | 70.4% | 71.7% | -1.3 p.p. | 75.0% | -4.6 p.p. | Abaixo da meta |
| Taxa de falta | 8.4% | 8.8% | -0.4 p.p. | 6.0% | +2.4 p.p. | Acima da meta |
| Horas atendidas no mês | 118.3 h | 129.0 h | -8.3% | 140.0 h | -15.5% | Abaixo da meta |
| Convênio a receber (lotes enviados) | R$ 12,077 | R$ 13,553 | -10.9% | — | — | informativo |
| Glosa dos lotes pagos no mês | 5.6% | 4.3% | +1.3 p.p. | 4.0% | +1.6 p.p. | Acima da meta |
| Vencido (parcelas a prazo) | R$ 4,005 | R$ 3,290 | +21.7% | R$ 4,000 | +0.1% | Acima da meta |
| Inadimplência a prazo (vencido ÷ (pago + vencido)) | 10.5% | 10.0% | +0.5 p.p. | 8.0% | +2.5 p.p. | Acima da meta |
| Orçamentos em aberto (valor) | R$ 2,700 | R$ 830 | +225.3% | — | — | informativo |

(Valores como o Excel em português mostra; os separadores seguem o idioma do Excel.)
- Destaques automáticos: • Maior melhora contra Julho: Margem do mês (+14.9 p.p.), • Maior piora contra Julho: Ocupação da agenda (-1.3 p.p.), • Mais longe da meta: Ocupação da agenda (-4.6 p.p. da meta. abaixo da meta), • Indicadores no alvo: 4 de 10 com meta,
- Observações da clínica (célula amarela do exemplo): "Agosto fechou com a agenda da Dra. Renata mais cheia (dois turnos por semana desde julho) e o lote de junho da Saúde Total pago com glosa, parte dela em recurso; o lote de junho da Vida Care tinha previsão para 04/09 e ainda estava dentro do prazo no fechamento de agosto — em setembro venceu e entrou na cobrança ao convênio; as faltas de segunda de manhã continuam acima da média e a recepção começou a confirmação de véspera por mensagem."

## 12. Histórico mensal (17 · Histórico; jan–ago = Painel mensal da 09, agenda desde junho, convênios/parcelas no fim de cada mês; setembro = Dados)

| Mês | Ocupação | Horas atendidas | Vazias | Taxa de falta | Lista de retorno | Entrou | Saiu | Sobrou | Convênio a receber | Atrasado | Glosa no mês | Vencido | Inadimpl. | Orçamentos abertos | Valor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Janeiro | — | — | — | — | — | R$ 25.310 | R$ 35.932 | −R$ 10.622 | R$ 8.740 | R$ 0 | 5,7 % | R$ 0 | 0,0 % | — | — |
| Fevereiro | — | — | — | — | — | R$ 25.650 | R$ 36.231 | −R$ 10.581 | R$ 8.350 | R$ 0 | 5,8 % | R$ 200 | 9,9 % | — | — |
| Março | — | — | — | — | — | R$ 40.540 | R$ 38.251 | R$ 2.289 | R$ 7.836 | R$ 0 | 3,4 % | R$ 390 | 6,3 % | — | — |
| Abril | — | — | — | — | — | R$ 40.775 | R$ 40.254 | R$ 521 | R$ 13.011 | R$ 0 | 7,7 % | R$ 790 | 7,3 % | — | — |
| Maio | — | — | — | — | — | R$ 45.380 | R$ 40.120 | R$ 5.260 | R$ 9.973 | R$ 0 | 4,9 % | R$ 2.140 | 11,9 % | — | — |
| Junho | 74 % | 123,7 | 44,3 | 8,0 % | 0 | R$ 47.240 | R$ 41.703 | R$ 5.537 | R$ 12.239 | R$ 0 | 9,3 % | R$ 2.900 | 10,9 % | 2 | R$ 650 |
| Julho | 72 % | 129,0 | 51,0 | 8,8 % | 1 | R$ 44.471 | R$ 46.322 | −R$ 1.851 | R$ 13.553 | R$ 0 | 4,3 % | R$ 3.290 | 10,0 % | 2 | R$ 830 |
| Agosto | 70 % | 118,3 | 49,7 | 8,4 % | 4 | R$ 55.841 | R$ 40.869 | R$ 14.972 | R$ 12.077 | R$ 0 | 5,6 % | R$ 4.005 | 10,5 % | 7 | R$ 2.700 |
| Setembro | 81 % | 51,8 | 12,2 | 5,3 % | 8 | R$ 20.710 | R$ 13.630 | R$ 7.080 | R$ 15.758 | R$ 1.727 | 2,9 % | R$ 3.775 | 9,4 % | 6 | R$ 3.460 |

- Agenda: a planilha 01 começou em junho (antes fica em branco). Orçamentos: o funil (15) começou em junho. Glosa no mês = dos lotes pagos naquele mês; no Dados (setembro), o acumulado do ano.

## 13. Rotina (03) e checklist do dia (04)

- **03 Rotina**: 8 rotinas (3 de segunda = 12 min, com a recepção; 5 de sexta = 18 min; **30 min/semana**); registradas S29 a S36 (20/07 a 07/09/2026); semana atual S37 · 14/09; aderência nas últimas 4 semanas **84 %**; rotina mais pulada: "Conferir os fechamentos da semana no Caixa (09)".
- **04 Checklist do dia**: dias registrados 73 (dias úteis de 01/06 a 11/09) · abertura completa nos últimos 20 dias 80 % · fechamento completo 55 % · dias com pendência 32 · itens pendentes no total 46. Item mais esquecido no fechamento: "Fechamento do dia lançado no Caixa (09)".

## 14. Nomes de prompt citados nas planilhas (a biblioteca de prompts deve usar exatamente estes)

**Agenda**

- Agenda 01 · Onde a agenda esvazia
- Agenda 02 · Reduzir faltas sem brigar com o paciente
- Agenda 03 · Mensagem de retorno educada
- Agenda 04 · Mensagem de retomada de orçamento
- Agenda 04 · Recebíveis 05
- Agenda 05 · Rotina da recepção em 30 minutos por semana
- Agenda 06 · Pendências do dia viram tarefas da recepção

**Preço**

- Preço 01 · Entender o custo da minha hora
- Preço 02 · Revisar a tabela de preços pela margem
- Preço 03 · Vale a pena este convênio?
- Preço 04 · Revisar a tabela de preços

**Caixa**

- Caixa 01 · Explicar o mês do caixa
- Caixa 02 · Comparar dois meses do resultado
- Caixa 04 · Preparar a reunião mensal com o contador
- Caixa 05 · Perguntas sobre provisão de impostos, 13º e férias
- Caixa 06 · Separar o que é da clínica e o que é pessoal
- Caixa 07 · Conversa sobre o repasse com o médico parceiro
- Caixa 08 · Plano para a reserva de três meses
- Caixa 09 · A taxa da maquininha está comendo a margem?

**Recebíveis**

- Recebíveis 01 · Resumir os convênios para o sócio
- Recebíveis 03 · Recurso de glosa em linguagem administrativa
- Recebíveis 04 · Cobrança educada em três versões
- Recebíveis 05 · Por que os orçamentos não fecham

**Painel**

- Painel 01 · Explicar o mês ao sócio
- Painel 05 · Meta realista para o trimestre
- Painel 06 · Meta × realizado: explicar o desvio

Total: 26 nomes citados em 22 planilhas. Os números das planilhas citadas nos "Como usar" (01 a 20) são os desta lista de arquivos.