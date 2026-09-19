# NÚMEROS DO EXEMPLO · Ferraz & Lima Advocacia (Kit de Gestão para Advogados)

Gerado por `numeros.py` a partir das 20 planilhas recalculadas e de `dados.py` (fonte única). Use estes valores em prompts, slides, manual e aulas: são exatamente os que aparecem nas planilhas.

## 1. Referência e regras do exemplo

- **Hoje (data de referência, Config = data literal 14/09/2026)**: segunda-feira **14/09/2026**. **Sexta do painel**: **11/09/2026**. Nenhum lançamento pago (caixa, parcela, hora) tem data depois de 11/09/2026.
- **Meses**: caixa (09) e horas (16) lançados de janeiro (caixa) / julho (horas) a 11/09/2026; **17 Painel do escritório** mostra **setembro em andamento**; **18 Resultado mensal** e **20 Resumo do mês** analisam **agosto de 2026** (último mês fechado; 20 = agosto × julho); **19 Metas** = 3º trimestre (semana 11 de 13, 82 % decorrido).
- **Inadimplência (única no kit: 14, 17, 19, 20)** = vencido ÷ (pago + vencido). Não é vencido ÷ em aberto.
- **Alíquota de impostos** (05, 06, 08, 09, 10, 18): **8 %**. **Margem mínima** 30 %, **margem alvo** 45 %, **folga de horas** 20 %.
- **Fonte do cadastro de casos**: 13 · Carteira (aba Casos). 01, 02, 04, 08, 14 e 16 copiam de lá. Parcela paga na 14 = entrada no caixa da 09 (na data do pagamento); recebido do caso na 13 = soma das parcelas pagas (2025 + 2026; as de 2025 estão no saldo inicial do caixa).
- **Todas as datas são literais**: nenhuma célula do exemplo usa `=HOJE()+n`. O exemplo é uma foto de 14/09/2026 e os números fecham entre os vinte arquivos em qualquer dia em que o cliente abrir. A única exceção é a data da proposta na 07, que é `=HOJE()` de propósito: uma proposta leva a data do dia em que você a envia.

## 2. Escritório, custos e custo-hora (05, 06, 08, 16)

| Pessoa | Papel | Pró-labore / bolsa (R$/mês) | Horas de trabalho | Horas faturáveis (meta) | Custo-hora na 16 (R$) |
|---|---|---|---|---|---|
| Marina Ferraz | Sócia · cível e empresarial | R$ 6.000 | 160 | 110 | R$ 72,76 |
| Rafael Lima | Sócio · trabalhista e previdenciário | R$ 6.000 | 160 | 110 | R$ 72,76 |
| Júlia Prado | Estagiária | R$ 1.400 | 120 | 60 | R$ 41,55 |

| Custo fixo | R$/mês |
|---|---|
| Aluguel e condomínio | R$ 2.800 |
| Contador | R$ 600 |
| Sistemas e assinaturas | R$ 450 |
| Telefone e internet | R$ 220 |
| Anuidades OAB e cursos | R$ 250 |
| Marketing e site | R$ 400 |
| Estagiária (bolsa) | R$ 1.400 |
| Material, correio e outros | R$ 380 |
| **Total de custos fixos (05, 09, 18)** | **R$ 6.500** |
| Pró-labore dos sócios (2 × 6.000) | R$ 12.000 |
| **Custo total do mês (05 Painel B11)** | **R$ 18.500** |

- **Horas faturáveis no mês (meta, todas as pessoas)**: 280 h · horas de trabalho: 440 h · tempo faturável planejado (05): 64 %.
- **Custo-hora do escritório (05 B13 = 06 B11 = 08 Config B7 = 16 Config B23)**: **R$ 66,07** (18.500 ÷ 280 h; em 06/08 digitado como 66,0714).
- **Hora mínima a cobrar (05)**: exata **R$ 106,57** = 66,07 ÷ (1 − 0,30 − 0,08); arredondada **R$ 110**. A 06 mostra a mesma conta (R$ 120,26).
- **Hora mínima com folga (08, 20 % de horas não previstas)**: **R$ 127,88** = 66,07 × 1,20 ÷ 0,62. **Hora alvo com folga (08)**: **R$ 168,69** (margem alvo 45 %).
- **Custos indiretos por hora faturável (05)**: R$ 18,21 (custos fixos sem a bolsa, R$ 5.100, ÷ 280 h). Custos fixos sem a equipe (16 Config): R$ 5.100.
| Por pessoa (05) | Horas faturáveis | Ocupação | Custo direto/h | Custo-hora completo | Hora mínima |
|---|---|---|---|---|---|
| Marina Ferraz | 110 | 69 % | R$ 54,55 | R$ 72,76 | R$ 117,35 |
| Rafael Lima | 110 | 69 % | R$ 54,55 | R$ 72,76 | R$ 117,35 |
| Júlia Prado | 60 | 50 % | R$ 23,33 | R$ 41,55 | R$ 67,01 |

| Sensibilidade (05) | Queda | Horas faturáveis | Custo-hora | Hora mínima |
|---|---|---|---|---|
| Hoje | 0 % | 280 | R$ 66,07 | R$ 106,57 |
| Queda de 10% | 10 % | 252 | R$ 73,41 | R$ 118,41 |
| Queda de 20% | 20 % | 224 | R$ 82,59 | R$ 133,21 |
| Queda de 30% | 30 % | 196 | R$ 94,39 | R$ 152,24 |

- **08 Tabela de referência**: casos abaixo do mínimo com folga: **10 de 38**; falta até o mínimo: R$ 11.877; valor por hora médio dos casos: R$ 153,31.
| Área (08) | Casos | Contratado | Horas estimadas | Valor/hora | Contra a hora mínima com folga | Abaixo do mínimo | Falta até o mínimo |
|---|---|---|---|---|---|---|---|
| Cível | 8 | R$ 101.500 | 632 | R$ 160,60 | +26 % | 1 | R$ 1.509 |
| Trabalhista | 12 | R$ 105.400 | 838 | R$ 125,78 | -2 % | 7 | R$ 9.219 |
| Previdenciário | 7 | R$ 39.400 | 264 | R$ 149,24 | +17 % | 1 | R$ 1.115 |
| Empresarial | 8 | R$ 115.000 | 615 | R$ 186,99 | +46 % | 0 | R$ 0 |
| Família | 3 | R$ 22.600 | 155 | R$ 145,81 | +14 % | 1 | R$ 33 |


## 3. Caixa mês a mês (09 · Caixa do escritório)

- Saldo em caixa antes do 1º lançamento (01/01/2026): **R$ 22.000** (já com honorários recebidos em 2025). Lançamentos: 227 linhas; 207 pagas.
| Mês | Entrou | Saiu | Sobrou | Saldo ao fim do mês |
|---|---|---|---|---|
| Janeiro | R$ 21.050 | R$ 20.408 | R$ 642 | R$ 22.642 |
| Fevereiro | R$ 23.070 | R$ 21.684 | R$ 1.386 | R$ 24.028 |
| Março | R$ 28.590 | R$ 22.276 | R$ 6.314 | R$ 30.342 |
| Abril | R$ 20.240 | R$ 26.638 | −R$ 6.398 | R$ 23.944 |
| Maio | R$ 31.120 | R$ 21.181 | R$ 9.939 | R$ 33.883 |
| Junho | R$ 27.420 | R$ 23.085 | R$ 4.335 | R$ 38.218 |
| Julho | R$ 29.460 | R$ 28.898 | R$ 562 | R$ 38.780 |
| Agosto | R$ 26.900 | R$ 21.897 | R$ 5.003 | R$ 43.783 |
| Setembro | R$ 5.220 | R$ 5.320 | −R$ 100 | R$ 43.683 |
| **Jan–ago (8 meses fechados)** | **R$ 207.850** | **R$ 186.067** | **R$ 21.783** |  |
| Setembro = até 11/09 (mês em andamento) |  |  |  |  |

**Entradas por categoria (Pago? = Sim)**

| Mês | Honorários fixos | Honorários por hora | Honorários de êxito | Consultoria e pareceres | Reembolso de custas | Outras entradas | Total |
|---|---|---|---|---|---|---|---|
| Janeiro | R$ 15.650 | R$ 2.880 | R$ 0 | R$ 2.520 | R$ 0 | R$ 0 | R$ 21.050 |
| Fevereiro | R$ 11.350 | R$ 3.240 | R$ 6.500 | R$ 1.980 | R$ 0 | R$ 0 | R$ 23.070 |
| Março | R$ 17.450 | R$ 2.520 | R$ 5.500 | R$ 2.340 | R$ 780 | R$ 0 | R$ 28.590 |
| Abril | R$ 11.400 | R$ 3.060 | R$ 0 | R$ 5.300 | R$ 0 | R$ 480 | R$ 20.240 |
| Maio | R$ 14.300 | R$ 2.160 | R$ 9.000 | R$ 5.660 | R$ 0 | R$ 0 | R$ 31.120 |
| Junho | R$ 17.100 | R$ 2.700 | R$ 6.000 | R$ 1.620 | R$ 0 | R$ 0 | R$ 27.420 |
| Julho | R$ 20.900 | R$ 2.340 | R$ 0 | R$ 5.680 | R$ 540 | R$ 0 | R$ 29.460 |
| Agosto | R$ 15.300 | R$ 0 | R$ 0 | R$ 11.290 | R$ 310 | R$ 0 | R$ 26.900 |
| Setembro | R$ 1.000 | R$ 0 | R$ 0 | R$ 4.220 | R$ 0 | R$ 0 | R$ 5.220 |
| **Jan–ago** | **R$ 123.450** | **R$ 18.900** | **R$ 27.000** | **R$ 36.390** | **R$ 1.630** | **R$ 480** | **R$ 207.850** |

**Saídas por categoria (Pago? = Sim)**

| Mês | Pró-labore dos sócios | Custos fixos (8 linhas, 6.500) | Impostos e taxas | Custas e despesas de processo | Deslocamento e viagens | Outras saídas | Total |
|---|---|---|---|---|---|---|---|
| Janeiro | R$ 12.000 | R$ 6.500 | R$ 1.648 | R$ 260 | R$ 0 | R$ 0 | R$ 20.408 |
| Fevereiro | R$ 12.000 | R$ 6.500 | R$ 1.684 | R$ 780 | R$ 240 | R$ 480 | R$ 21.684 |
| Março | R$ 13.500 | R$ 6.500 | R$ 1.846 | R$ 130 | R$ 0 | R$ 300 | R$ 22.276 |
| Abril | R$ 17.311 | R$ 6.500 | R$ 2.287 | R$ 540 | R$ 0 | R$ 0 | R$ 26.638 |
| Maio | R$ 12.000 | R$ 6.500 | R$ 1.581 | R$ 310 | R$ 310 | R$ 480 | R$ 21.181 |
| Junho | R$ 14.000 | R$ 6.500 | R$ 2.490 | R$ 95 | R$ 0 | R$ 0 | R$ 23.085 |
| Julho | R$ 19.594 | R$ 6.500 | R$ 2.194 | R$ 310 | R$ 0 | R$ 300 | R$ 28.898 |
| Agosto | R$ 12.000 | R$ 6.500 | R$ 2.357 | R$ 380 | R$ 180 | R$ 480 | R$ 21.897 |
| Setembro | R$ 0 | R$ 5.250 | R$ 0 | R$ 70 | R$ 0 | R$ 0 | R$ 5.320 |

- "Pró-labore dos sócios" inclui o pró-labore fixo (12.000/mês), as retiradas extras (Rafael 1.500 em 16/03; Marina 2.000 em 19/06) e a distribuição de lucro dos trimestres fechados (paga dia 10 do mês seguinte: 1º tri em abril, 2º tri em julho). "Outras saídas" = despesas pessoais dos sócios pagas pelo escritório (a acertar). "Outras entradas" = devolução de despesa pessoal (Marina, 480 em 14/04).
- Guia de impostos: paga dia 20, 8 % das entradas do mês anterior (sem Outras entradas); janeiro sobre dezembro/2025 (fictício, base 20.600). A guia de setembro (20/09) ainda não foi paga.
- Setembro: custos fixos com vencimento depois de 11/09 (telefone, anuidades, marketing, material), pró-labore (28/09) e a guia (20/09) estão como Pago? = Não → **A pagar R$ 15.402**. **A receber (Pago? = Não) R$ 25.930** = parcelas vencidas + a vencer até 30/09 (o cronograma completo fica na 14).
- **09 Painel (Config = Setembro)**: Entrou R$ 5.220 · Saiu R$ 5.320 · Sobrou −R$ 100 · Saldo acumulado **R$ 43.683** · A receber R$ 25.930 · A pagar R$ 15.402.
| Por cliente (09, ano até 11/09) | Entrou no ano | A receber (Pago? = Não) | Custas pagas no ano |
|---|---|---|---|
| Padaria do Sol Ltda | R$ 11.250 | R$ 0 | R$ 0 |
| Ana Beatriz Moreira | R$ 5.500 | R$ 0 | R$ 0 |
| Construtora Horizonte | R$ 16.080 | R$ 2.100 | R$ 780 |
| Carlos Eduardo Nunes | R$ 7.500 | R$ 1.500 | R$ 0 |
| Loja Verde Comércio | R$ 3.800 | R$ 2.800 | R$ 0 |
| Fernanda Castro | R$ 1.400 | R$ 0 | R$ 0 |
| Bistrô 42 | R$ 5.300 | R$ 4.200 | R$ 95 |
| Roberto Almeida | R$ 16.510 | R$ 0 | R$ 310 |
| Clínica Bem-Estar | R$ 32.760 | R$ 2.700 | R$ 0 |
| Marcos Vinícius Teles | R$ 14.150 | R$ 2.250 | R$ 0 |
| Transportadora Rota Sul | R$ 12.400 | R$ 0 | R$ 130 |
| Patrícia Gomes | R$ 13.500 | R$ 2.100 | R$ 380 |
| Escola Aurora | R$ 3.400 | R$ 0 | R$ 70 |
| José Antônio Ribeiro | R$ 6.000 | R$ 0 | R$ 260 |
| Oficina Mecânica Central | R$ 16.500 | R$ 1.500 | R$ 310 |
| Luciana Farias | R$ 15.600 | R$ 0 | R$ 0 |
| Agência Prisma | R$ 26.440 | R$ 3.780 | R$ 540 |
| Helena Duarte | R$ 4.500 | R$ 3.000 | R$ 0 |

| 11 · Trimestre | Entradas (sem devoluções) | Saídas sem sócios | Pró-labore fixo | Resultado após pró-labore | Fechado? | Distribuível (50 %) | Já distribuído |
|---|---|---|---|---|---|---|---|
| 1º trimestre | R$ 72.710 | R$ 26.088 | R$ 36.000 | R$ 10.622 | Sim | R$ 5.311 | R$ 5.311 |
| 2º trimestre | R$ 78.300 | R$ 27.113 | R$ 36.000 | R$ 15.187 | Sim | R$ 7.594 | R$ 7.594 |
| 3º trimestre | R$ 61.580 | R$ 23.741 | R$ 36.000 | R$ 1.839 | Em andamento | R$ 0 | R$ 0 |

- 11: pró-labore combinado R$ 12.000/mês; a acertar com o escritório no ano R$ 5.060 (Marina: retirada extra 2.000 + despesas pessoais 1.440 − devolução 480 = 2.960; Rafael: 1.500 + 600 = 2.100). Setembro: pró-labore ainda não pago (dia 28).

## 4. Agosto de 2026 fechado (18 · Resultado mensal) e julho para comparação

| Linha da DRE | Julho | Agosto | Jan–ago (total) | Média jan–ago |
|---|---|---|---|---|
| Honorários fixos | R$ 20.900 | R$ 15.300 | R$ 123.450 | R$ 15.431 |
| Honorários por hora | R$ 2.340 | R$ 0 | R$ 18.900 | R$ 2.362 |
| Honorários de êxito | R$ 0 | R$ 0 | R$ 27.000 | R$ 3.375 |
| Consultoria e pareceres | R$ 5.680 | R$ 11.290 | R$ 36.390 | R$ 4.549 |
| Reembolso de custas | R$ 540 | R$ 310 | R$ 1.630 | R$ 204 |
| **Receita total** | R$ 29.460 | R$ 26.900 | R$ 207.370 | R$ 25.921 |
| Custos fixos (8 linhas) | R$ 6.500 | R$ 6.500 | R$ 52.000 | R$ 6.500 |
| Custas e despesas de processo | R$ 310 | R$ 380 | R$ 2.805 | R$ 351 |
| Deslocamento e viagens | R$ 0 | R$ 180 | R$ 730 | R$ 91 |
| **Despesas de casos e viagens** | R$ 310 | R$ 560 | R$ 3.535 | R$ 442 |
| Pró-labore fixo (Marina 6.000 + Rafael 6.000) | R$ 12.000 | R$ 12.000 | R$ 96.000 | R$ 12.000 |
| Impostos provisionados (8 % da receita) | R$ 2.357 | R$ 2.152 | R$ 16.591 | R$ 2.074 |
| **Total de saídas** | R$ 21.167 | R$ 21.212 | R$ 168.126 | R$ 21.016 |
| **Resultado do mês** | R$ 8.293 | R$ 5.688 | R$ 39.244 | R$ 4.906 |
| **Margem (resultado ÷ receita)** | **28,2 %** | **21,1 %** | 18,9 % | 17,1 % |

- Agosto: receita **R$ 26.900**, saídas **R$ 21.212**, resultado **R$ 5.688**, margem **21,1 %** (julho: 28,2 %; variação **−7,1 p.p.**). Previsto de agosto: receita 27.000, custos fixos 6.500, despesas 400, pró-labore 12.000 → resultado previsto 5.940, margem prevista 22,0 %.
| Comparação (18 Painel, agosto) | Mês | Mês anterior | Variação | Previsto | Vs. previsto | Situação |
|---|---|---|---|---|---|---|
| Receita total | R$ 26.900 | R$ 29.460 | -8,7 % | R$ 27.000 | -0,4 % | Perto |
| Custos fixos | R$ 6.500 | R$ 6.500 | +0,0 % | R$ 6.500 | +0,0 % | Dentro do previsto |
| Despesas de casos e viagens | R$ 560 | R$ 310 | +80,6 % | R$ 400 | +40,0 % | Fora do previsto |
| Pró-labore | R$ 12.000 | R$ 12.000 | +0,0 % | R$ 12.000 | +0,0 % | Informativo |
| Impostos provisionados | R$ 2.152 | R$ 2.357 | -8,7 % | R$ 2.160 | -0,4 % | Informativo |
| Total de saídas | R$ 21.212 | R$ 21.167 | +0,2 % | R$ 21.060 | +0,7 % | Perto |
| Resultado do mês | R$ 5.688 | R$ 8.293 | -31,4 % | R$ 5.940 | -4,2 % | Perto |
| Margem | 21,1 % | 28,2 % | -7,0 p,p, | 22,0 % | -0,9 p,p, | Perto |

- A DRE não inclui retiradas extras, distribuição de lucro nem despesas pessoais dos sócios (ficam na 11); por isso "Saiu no mês" do caixa (agosto: 21.897) é diferente do "Total de saídas" da DRE (21.212: impostos são provisão de 8 % da receita, e não a guia paga).

## 5. A semana de 11/09/2026 (17 · Painel do escritório, aba Dados)

| Indicador | Valor desta sexta | Limite ou meta | Sentido | Situação | Copiado de |
|---|---|---|---|---|---|
| Prazos de hoje e dos próximos 7 dias | 14 | — | — | Informativo | 01 · Agenda de prazos (Painel: Hoje + Próximos 7 dias) |
| Prazos atrasados | 7 | 0 | Menor é melhor | Fora | 01 · Agenda de prazos (Painel) |
| Horas registradas no mês | 109,5 | — | — | Informativo | 16 · Horas por caso e por pessoa (Painel, Config = mês do painel) |
| Horas faturáveis no mês | 87 | — | — | Informativo | 16 · Horas por caso e por pessoa (Painel) |
| % de horas faturáveis | 79,5 % | 75 % | Maior é melhor | No alvo | calculado aqui |
| Entrou no mês (recebimentos) | R$ 5.220 | — | — | Informativo | 09 · Caixa do escritório (Painel: Entrou no mês) |
| Saiu no mês (tudo o que saiu do caixa) | R$ 5.320 | — | — | Informativo | 09 · Caixa do escritório (Painel: Saiu no mês) |
| Sobrou no mês | −R$ 100 | — | — | Informativo | calculado aqui |
| A receber (carteira; inclui êxito de casos ativos) | R$ 111.990 | — | — | Informativo | 13 · Carteira de clientes e casos (Painel: A receber) |
| Vencido (parcelas em atraso) | R$ 13.080 | R$ 10.000 | Menor é melhor | Fora | 14 · Parcelas e inadimplência (Painel: Vencido) |
| Inadimplência (vencido ÷ (pago + vencido)) | 4,6 % | 4 % | Menor é melhor | Fora | 14 · Parcelas e inadimplência (Painel: Inadimplência) |
| Propostas abertas (quantidade) | 9 | — | — | Informativo | 15 · Funil de propostas (Painel: soma do funil por etapa) |
| Propostas abertas (valor) | R$ 72.900 | R$ 40.000 | Maior é melhor | No alvo | 15 · Funil de propostas (Painel: Em aberto) |
| Casos ativos | 30 | 30 | Maior é melhor | No alvo | 13 · Carteira de clientes e casos (Painel: Casos ativos) |

### Prazos (01 · Agenda de prazos, 14/09/2026)

- **Atrasados 7 · Hoje 3 · Próximos 7 dias 11** · de 8 a 30 dias 13 · abertos no total 36 · feitos 2. Agenda: 38 linhas (prazo principal de cada caso ativo = próxima ação da 02, mais 8 compromissos extras, 2 já feitos).
| # | Processo | Cliente | Tipo de prazo | Data | Dias | Situação | Responsável |
|---|---|---|---|---|---|---|---|
| 1 | 7099226-69.2026.8.26.0433 | Luciana Farias | Juntada de documentos | 08/09/2026 | -6 | Atrasado | Júlia Prado |
| 2 | CONS-2026-06 | Transportadora Rota Sul | Reunião com cliente | 09/09/2026 | -5 | Atrasado | Rafael Lima |
| 3 | 5900991-46.2026.8.26.0469 | José Antônio Ribeiro | Manifestação sobre laudo | 10/09/2026 | -4 | Atrasado | Rafael Lima |
| 4 | 9586960-92.2026.8.26.0106 | Construtora Horizonte | Réplica | 11/09/2026 | -3 | Atrasado | Marina Ferraz |
| 5 | 9616569-91.2026.8.26.0079 | Patrícia Gomes | Impugnação | 12/09/2026 | -2 | Atrasado | Marina Ferraz |
| 6 | 5025425-10.2025.8.26.0629 | Roberto Almeida | Embargos de declaração | 13/09/2026 | -1 | Atrasado | Marina Ferraz |
| 7 | 9605863-76.2026.8.26.0026 | Marcos Vinícius Teles | Manifestação sobre o recurso | 13/09/2026 | -1 | Atrasado | Rafael Lima |
| 8 | CONS-2026-03 | Marcos Vinícius Teles | Entrega de parecer | 14/09/2026 | 0 | Hoje | Rafael Lima |
| 9 | 2645033-67.2026.8.26.0012 | Clínica Bem-Estar | Contestação | 14/09/2026 | 0 | Hoje | Marina Ferraz |
| 10 | 6832730-55.2026.8.26.0386 | Patrícia Gomes | Minuta de acordo | 14/09/2026 | 0 | Hoje | Marina Ferraz |
| 11 | 7679821-77.2026.8.26.0265 | Helena Duarte | Réplica | 15/09/2026 | 1 | Até 7 dias | Rafael Lima |
| 12 | 2998500-50.2026.8.26.0515 | Ana Beatriz Moreira | Prazo interno | 15/09/2026 | 1 | Até 7 dias | Rafael Lima |
| 13 | 2998500-50.2026.8.26.0515 | Ana Beatriz Moreira | Audiência de conciliação | 16/09/2026 | 2 | Até 7 dias | Rafael Lima |
| 14 | 6710873-21.2025.8.26.0571 | Escola Aurora | Recurso de apelação | 16/09/2026 | 2 | Até 7 dias | Marina Ferraz |
| 15 | CONS-2026-04 | Escola Aurora | Reunião com cliente | 17/09/2026 | 3 | Até 7 dias | Marina Ferraz |
| 16 | 8045862-82.2026.8.26.0491 | Carlos Eduardo Nunes | Embargos de declaração | 17/09/2026 | 3 | Até 7 dias | Rafael Lima |
| 17 | CONS-2026-02 | Loja Verde Comércio | Entrega de parecer | 18/09/2026 | 4 | Até 7 dias | Marina Ferraz |
| 18 | 9225646-96.2025.8.26.0322 | Transportadora Rota Sul | Manifestação sobre laudo | 18/09/2026 | 4 | Até 7 dias | Rafael Lima |
| 19 | CONS-2025-05 | Clínica Bem-Estar | Reunião com cliente | 19/09/2026 | 5 | Até 7 dias | Marina Ferraz |
| 20 | 8056747-83.2026.8.26.0561 | Bistrô 42 | Juntada de documentos | 19/09/2026 | 5 | Até 7 dias | Júlia Prado |
| 21 | 4746093-86.2026.8.26.0637 | Carlos Eduardo Nunes | Juntada de documentos | 20/09/2026 | 6 | Até 7 dias | Júlia Prado |
| 22 | 2354318-24.2026.8.26.0295 | Roberto Almeida | Contrarrazões | 22/09/2026 | 8 | Até 30 dias | Marina Ferraz |
| 23 | CONS-2026-01 | Padaria do Sol Ltda | Reunião com cliente | 23/09/2026 | 9 | Até 30 dias | Marina Ferraz |
| 24 | 8056747-83.2026.8.26.0561 | Bistrô 42 | Audiência de instrução | 23/09/2026 | 9 | Até 30 dias | Rafael Lima |
| 25 | 3363714-92.2025.8.26.0592 | Oficina Mecânica Central | Alegações finais | 24/09/2026 | 10 | Até 30 dias | Rafael Lima |
| 26 | 6184138-13.2026.8.26.0378 | Oficina Mecânica Central | Audiência de conciliação | 26/09/2026 | 12 | Até 30 dias | Rafael Lima |
| 27 | 3363714-92.2025.8.26.0592 | Oficina Mecânica Central | Reunião com cliente | 26/09/2026 | 12 | Até 30 dias | Rafael Lima |
| 28 | 9236009-85.2025.8.26.0452 | Bistrô 42 | Cumprimento de sentença | 29/09/2026 | 15 | Até 30 dias | Rafael Lima |
| 29 | CONS-2026-07 | Agência Prisma | Entrega de parecer | 30/09/2026 | 16 | Até 30 dias | Marina Ferraz |
| 30 | 4526984-60.2026.8.26.0258 | Transportadora Rota Sul | Juntada de documentos | 30/09/2026 | 16 | Até 30 dias | Júlia Prado |

| Carga por responsável (01) | Abertos | Atrasados | Hoje | Em alerta (7 dias) | Mais antigo em aberto | Feitos |
|---|---|---|---|---|---|---|
| Marina Ferraz | 15 | 3 | 2 | 4 | 11/09/2026 | 1 |
| Rafael Lima | 16 | 3 | 1 | 5 | 09/09/2026 | 0 |
| Júlia Prado | 5 | 1 | 0 | 2 | 08/09/2026 | 1 |

- Júlia Prado (estagiária) responde pelos prazos de juntada de documentos; os casos continuam com o sócio responsável (por isso ela tem prazos na 01 e nenhum caso na 02, 04 e 13).
### Andamento (02): casos ativos 30 · ação atrasada 7 · hoje ou esta semana 12 · sem próxima ação 0 · parados há mais de 30 dias 4 · encerrados 8

| Fase (02) | Casos | Ação atrasada | Esta semana | Sem próxima ação | Parados |
|---|---|---|---|---|---|
| Consultivo | 7 | 1 | 4 | 0 | 0 |
| Inicial | 8 | 2 | 4 | 0 | 1 |
| Instrução | 4 | 1 | 1 | 0 | 0 |
| Sentença | 3 | 1 | 2 | 0 | 0 |
| Recurso | 3 | 1 | 0 | 0 | 0 |
| Execução | 3 | 1 | 0 | 0 | 2 |
| Acordo | 2 | 0 | 1 | 0 | 1 |
| Encerrado | 8 | 0 | 0 | 0 | 0 |

| Área (02) | Ativos | Encerrados | Ação atrasada | Parados |
|---|---|---|---|---|
| Cível | 7 | 1 | 3 | 1 |
| Trabalhista | 10 | 2 | 1 | 3 |
| Previdenciário | 5 | 2 | 2 | 0 |
| Empresarial | 6 | 2 | 0 | 0 |
| Família | 2 | 1 | 1 | 0 |

- Parados (>30 dias sem atualização): Bistrô 42 (execução, 41 dias), Oficina Mecânica Central (inicial, aguardando audiência, 36), Luciana Farias (acordo, aguardando homologação, 33), Helena Duarte (execução, 47).
### Horas (16 · Horas por caso, Config = Setembro; setembro até 11/09)

- **Setembro (até 11/09)**: horas **109,5** · faturáveis **87,0** (79,5 %) · custo das horas R$ 7.031 · meta de faturáveis atingida 31,1 % · consomem mais do que pagam: 0.
- **Agosto (fechado)**: 304,0 h, faturáveis 248,0 h (81,6 %). **Julho**: 233,5 h, faturáveis 179,5 h (76,9 %). Lançamentos: 278 linhas de 01/07 a 11/09; o controle de horas começou em julho (antes: "horas gastas antes" por caso).
| Pessoa | Set (h) | Set faturáveis | Ago (h) | Ago faturáveis | Jul (h) | Jul faturáveis | Meta faturável/mês | Custo-hora |
|---|---|---|---|---|---|---|---|---|
| Marina Ferraz | 44,0 | 38,0 | 111,5 | 101,5 | 73,5 | 62,0 | 110 | R$ 72,76 |
| Rafael Lima | 35,5 | 29,0 | 112,0 | 88,0 | 98,0 | 64,5 | 110 | R$ 72,76 |
| Júlia Prado | 30,0 | 20,0 | 80,5 | 58,5 | 62,0 | 53,0 | 60 | R$ 41,55 |

| Casos para olhar primeiro (16, ativos) | Cliente | Responsável | Horas estimadas | Horas gastas | Custo das horas | Contratado | Margem | Situação |
|---|---|---|---|---|---|---|---|---|
| 9236009-85.2025.8.26.0452 | Bistrô 42 | Rafael Lima | 45 | 50,0 | R$ 3.314 | R$ 4.000 | R$ 686 | Estourou as horas |
| 6710873-21.2025.8.26.0571 | Escola Aurora | Marina Ferraz | 90 | 100,0 | R$ 6.647 | R$ 10.000 | R$ 3.353 | Estourou as horas |

### Caixa, carteira, parcelas e propostas na sexta

- Caixa de setembro até 11/09 (09): entrou **R$ 5.220**, saiu **R$ 5.320**, sobrou −R$ 100; saldo acumulado R$ 43.683.
- Carteira (13): contratado **R$ 383.900** · recebido **R$ 271.910** · **a receber R$ 111.990** (71 % recebido) · **casos ativos 30** · encerrados 8. A receber inclui o êxito esperado de casos ativos e o que ainda não virou parcela: não é atraso.
- Parcelas (14): vence em 7 dias R$ 2.800 · vence em 30 dias R$ 15.450 · em aberto (total) R$ 55.330 · **vencido R$ 13.080** em **7 parcelas** · **inadimplência 4,6 %** = R$ 13.080 ÷ (R$ 271.910 pago + R$ 13.080). Pela outra conta (vencido ÷ em aberto) daria 23,6 %: não use.
- Propostas (15): abertas **9** somando **R$ 72.900** · previsão ponderada R$ 30.805 · **fechado no trimestre R$ 53.000** (88 % da meta de R$ 60.000) · taxa de fechamento 64 % (7 fechadas ÷ 11 decididas) · dias até fechar (média) 20.

## 6. Carteira (13 · Carteira de clientes e casos)

| Área | Casos | Ativos | Contratado | Recebido | A receber | % recebido |
|---|---|---|---|---|---|---|
| Cível | 8 | 7 | R$ 101.500 | R$ 70.300 | R$ 31.200 | 69 % |
| Trabalhista | 12 | 10 | R$ 105.400 | R$ 67.700 | R$ 37.700 | 64 % |
| Previdenciário | 7 | 5 | R$ 39.400 | R$ 27.650 | R$ 11.750 | 70 % |
| Empresarial | 8 | 6 | R$ 115.000 | R$ 85.760 | R$ 29.240 | 75 % |
| Família | 3 | 2 | R$ 22.600 | R$ 20.500 | R$ 2.100 | 91 % |

| Responsável | Casos | Ativos | Contratado | Recebido | A receber | % recebido |
|---|---|---|---|---|---|---|
| Marina Ferraz | 19 | 15 | R$ 239.100 | R$ 176.560 | R$ 62.540 | 74 % |
| Rafael Lima | 19 | 15 | R$ 144.800 | R$ 95.350 | R$ 49.450 | 66 % |

| Modalidade | Casos | Ativos | Contratado | Recebido | A receber | % recebido |
|---|---|---|---|---|---|---|
| Fixo | 21 | 17 | R$ 209.400 | R$ 163.550 | R$ 45.850 | 78 % |
| Hora | 2 | 2 | R$ 45.600 | R$ 38.160 | R$ 7.440 | 84 % |
| Êxito | 7 | 5 | R$ 42.500 | R$ 12.500 | R$ 30.000 | 29 % |
| Misto | 8 | 6 | R$ 86.400 | R$ 57.700 | R$ 28.700 | 67 % |

| # | Top 5 clientes | Tipo | Casos | Contratado | Recebido | A receber | % recebido |
|---|---|---|---|---|---|---|---|
| 1 | Clínica Bem-Estar | PJ | 2 | R$ 39.600 | R$ 34.560 | R$ 5.040 | 87 % |
| 2 | Oficina Mecânica Central | PJ | 3 | R$ 36.000 | R$ 31.500 | R$ 4.500 | 88 % |
| 3 | Construtora Horizonte | PJ | 2 | R$ 33.500 | R$ 24.300 | R$ 9.200 | 73 % |
| 4 | Agência Prisma | PJ | 2 | R$ 31.000 | R$ 25.900 | R$ 5.100 | 84 % |
| 5 | Padaria do Sol Ltda | PJ | 2 | R$ 30.000 | R$ 16.500 | R$ 13.500 | 55 % |

| Situação | Casos | Contratado | Recebido | A receber | % recebido |
|---|---|---|---|---|---|
| Ativo | 30 | R$ 307.900 | R$ 195.910 | R$ 111.990 | 64 % |
| Encerrado | 8 | R$ 76.000 | R$ 76.000 | R$ 0 | 100 % |

- A receber dos encerrados: R$ 0 (todos os casos encerrados estão quitados; o checklist da 04 não tem parcela pendente).
| Cliente (13) | Tipo | Área | Casos | Ativos | Contratado | Recebido | A receber | Último caso aberto |
|---|---|---|---|---|---|---|---|---|
| Padaria do Sol Ltda | PJ | Empresarial | 2 | 1 | R$ 30.000 | R$ 16.500 | R$ 13.500 | 29/06/2026 |
| Ana Beatriz Moreira | PF | Trabalhista | 2 | 1 | R$ 14.500 | R$ 8.500 | R$ 6.000 | 07/07/2026 |
| Construtora Horizonte | PJ | Cível | 2 | 1 | R$ 33.500 | R$ 24.300 | R$ 9.200 | 22/07/2026 |
| Carlos Eduardo Nunes | PF | Previdenciário | 2 | 2 | R$ 13.000 | R$ 7.500 | R$ 5.500 | 28/07/2026 |
| Loja Verde Comércio | PJ | Empresarial | 2 | 1 | R$ 14.400 | R$ 8.800 | R$ 5.600 | 11/08/2026 |
| Fernanda Castro | PF | Família | 1 | 0 | R$ 7.000 | R$ 7.000 | R$ 0 | 06/10/2025 |
| Bistrô 42 | PJ | Trabalhista | 2 | 2 | R$ 13.500 | R$ 5.300 | R$ 8.200 | 12/01/2026 |
| Roberto Almeida | PF | Cível | 2 | 2 | R$ 25.200 | R$ 22.200 | R$ 3.000 | 04/05/2026 |
| Clínica Bem-Estar | PJ | Empresarial | 2 | 2 | R$ 39.600 | R$ 34.560 | R$ 5.040 | 18/05/2026 |
| Marcos Vinícius Teles | PF | Previdenciário | 3 | 2 | R$ 16.400 | R$ 14.150 | R$ 2.250 | 19/08/2026 |
| Transportadora Rota Sul | PJ | Trabalhista | 3 | 3 | R$ 26.900 | R$ 17.900 | R$ 9.000 | 13/07/2026 |
| Patrícia Gomes | PF | Família | 2 | 2 | R$ 15.600 | R$ 13.500 | R$ 2.100 | 08/06/2026 |
| Escola Aurora | PJ | Cível | 2 | 2 | R$ 23.200 | R$ 8.200 | R$ 15.000 | 03/08/2026 |
| José Antônio Ribeiro | PF | Previdenciário | 2 | 1 | R$ 10.000 | R$ 6.000 | R$ 4.000 | 26/01/2026 |
| Oficina Mecânica Central | PJ | Trabalhista | 3 | 2 | R$ 36.000 | R$ 31.500 | R$ 4.500 | 13/04/2026 |
| Luciana Farias | PF | Cível | 2 | 2 | R$ 19.600 | R$ 15.600 | R$ 4.000 | 29/06/2026 |
| Agência Prisma | PJ | Empresarial | 2 | 2 | R$ 31.000 | R$ 25.900 | R$ 5.100 | 06/04/2026 |
| Helena Duarte | PF | Trabalhista | 2 | 2 | R$ 14.500 | R$ 4.500 | R$ 10.000 | 22/06/2026 |

| Chave | Número | Cliente | Área | Fase | Responsável | Modalidade | Contratado | Recebido | Horas est./gastas | Abertura | Próxima ação (prazo principal) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A01 | CONS-2026-01 | Padaria do Sol Ltda | Empresarial | Consultivo | Marina Ferraz | Fixo | R$ 18.000 | R$ 4.500 | 72/16 | 29/06/2026 | Reunião com cliente · 23/09/2026 (+9 dias) |
| A02 | 2998500-50.2026.8.26.0515 | Ana Beatriz Moreira | Trabalhista | Inicial | Rafael Lima | Êxito | R$ 6.000 | R$ 0 | 70/22 | 07/07/2026 | Audiência de conciliação · 16/09/2026 (+2 dias) |
| A03 | 9586960-92.2026.8.26.0106 | Construtora Horizonte | Cível | Inicial | Marina Ferraz | Misto (fixo R$ 10.500 + êxito R$ 5.000) | R$ 15.500 | R$ 6.300 | 90/34 | 22/07/2026 | Réplica · 11/09/2026 (-3 dias) |
| A04 | 4746093-86.2026.8.26.0637 | Carlos Eduardo Nunes | Previdenciário | Inicial | Rafael Lima | Fixo | R$ 5.400 | R$ 3.900 | 40/15 | 28/07/2026 | Juntada de documentos · 20/09/2026 (+6 dias) |
| A05 | CONS-2026-02 | Loja Verde Comércio | Empresarial | Consultivo | Marina Ferraz | Fixo | R$ 8.400 | R$ 2.800 | 45/24 | 11/08/2026 | Entrega de parecer · 18/09/2026 (+4 dias) |
| A06 | CONS-2026-03 | Marcos Vinícius Teles | Previdenciário | Consultivo | Rafael Lima | Fixo | R$ 4.500 | R$ 2.250 | 24/16 | 19/08/2026 | Entrega de parecer · 14/09/2026 (hoje) |
| A07 | CONS-2026-04 | Escola Aurora | Cível | Consultivo | Marina Ferraz | Fixo | R$ 13.200 | R$ 2.200 | 72/9 | 03/08/2026 | Reunião com cliente · 17/09/2026 (+3 dias) |
| A08 | 8056747-83.2026.8.26.0561 | Bistrô 42 | Trabalhista | Instrução | Rafael Lima | Fixo | R$ 9.500 | R$ 5.300 | 80/70 | 12/01/2026 | Audiência de instrução · 23/09/2026 (+9 dias) |
| A09 | 9236009-85.2025.8.26.0452 | Bistrô 42 | Trabalhista | Execução | Rafael Lima | Êxito | R$ 4.000 | R$ 0 | 45/50 | 18/08/2025 | Cumprimento de sentença · 29/09/2026 (+15 dias) |
| A10 | 5025425-10.2025.8.26.0629 | Roberto Almeida | Cível | Sentença | Marina Ferraz | Fixo | R$ 15.000 | R$ 15.000 | 95/88 | 01/12/2025 | Embargos de declaração · 13/09/2026 (-1 dia) |
| A11 | 2354318-24.2026.8.26.0295 | Roberto Almeida | Cível | Recurso | Marina Ferraz | Misto (fixo R$ 7.200 + êxito R$ 3.000) | R$ 10.200 | R$ 7.200 | 60/48 | 04/05/2026 | Contrarrazões · 22/09/2026 (+8 dias) |
| A12 | CONS-2025-05 | Clínica Bem-Estar | Empresarial | Consultivo | Marina Ferraz | Hora | R$ 21.600 | R$ 19.260 | 120/107 | 10/11/2025 | Reunião com cliente · 19/09/2026 (+5 dias) |
| A13 | 2645033-67.2026.8.26.0012 | Clínica Bem-Estar | Empresarial | Inicial | Marina Ferraz | Fixo | R$ 18.000 | R$ 15.300 | 110/45 | 18/05/2026 | Contestação · 14/09/2026 (hoje) |
| A14 | 9225646-96.2025.8.26.0322 | Transportadora Rota Sul | Trabalhista | Instrução | Rafael Lima | Fixo | R$ 13.500 | R$ 13.500 | 90/78 | 01/12/2025 | Manifestação sobre laudo · 18/09/2026 (+4 dias) |
| A15 | 4526984-60.2026.8.26.0258 | Transportadora Rota Sul | Trabalhista | Inicial | Rafael Lima | Êxito | R$ 9.000 | R$ 0 | 80/30 | 13/04/2026 | Audiência de conciliação · 04/10/2026 (+20 dias) |
| A16 | CONS-2026-06 | Transportadora Rota Sul | Trabalhista | Consultivo | Rafael Lima | Fixo | R$ 4.400 | R$ 4.400 | 28/24 | 13/07/2026 | Reunião com cliente · 09/09/2026 (-5 dias) |
| A17 | 6832730-55.2026.8.26.0386 | Patrícia Gomes | Família | Acordo | Marina Ferraz | Fixo | R$ 9.000 | R$ 9.000 | 55/48 | 16/03/2026 | Minuta de acordo · 14/09/2026 (hoje) |
| A18 | 9616569-91.2026.8.26.0079 | Patrícia Gomes | Família | Execução | Marina Ferraz | Fixo | R$ 6.600 | R$ 4.500 | 45/33 | 08/06/2026 | Impugnação · 12/09/2026 (-2 dias) |
| A19 | 6710873-21.2025.8.26.0571 | Escola Aurora | Cível | Sentença | Marina Ferraz | Misto (fixo R$ 6.000 + êxito R$ 4.000) | R$ 10.000 | R$ 6.000 | 90/100 | 20/10/2025 | Recurso de apelação · 16/09/2026 (+2 dias) |
| A20 | 5900991-46.2026.8.26.0469 | José Antônio Ribeiro | Previdenciário | Instrução | Rafael Lima | Êxito | R$ 4.000 | R$ 0 | 40/30 | 26/01/2026 | Manifestação sobre laudo · 10/09/2026 (-4 dias) |
| A21 | 3363714-92.2025.8.26.0592 | Oficina Mecânica Central | Trabalhista | Instrução | Rafael Lima | Fixo | R$ 15.000 | R$ 15.000 | 95/86 | 17/11/2025 | Alegações finais · 24/09/2026 (+10 dias) |
| A22 | 6184138-13.2026.8.26.0378 | Oficina Mecânica Central | Trabalhista | Inicial | Rafael Lima | Misto (fixo R$ 6.000 + êxito R$ 3.000) | R$ 9.000 | R$ 4.500 | 60/27 | 13/04/2026 | Audiência de conciliação · 26/09/2026 (+12 dias) |
| A23 | 7099226-69.2026.8.26.0433 | Luciana Farias | Cível | Inicial | Marina Ferraz | Fixo | R$ 12.000 | R$ 12.000 | 75/45 | 25/05/2026 | Juntada de documentos · 08/09/2026 (-6 dias) |
| A24 | 2521428-61.2026.8.26.0600 | Luciana Farias | Cível | Acordo | Marina Ferraz | Misto (fixo R$ 3.600 + êxito R$ 4.000) | R$ 7.600 | R$ 3.600 | 40/34 | 29/06/2026 | Homologação do acordo · 02/10/2026 (+18 dias) |
| A25 | 9362688-24.2025.8.26.0436 | Agência Prisma | Empresarial | Recurso | Marina Ferraz | Hora | R$ 24.000 | R$ 18.900 | 133/126 | 08/12/2025 | Contrarrazões · 11/10/2026 (+27 dias) |
| A26 | CONS-2026-07 | Agência Prisma | Empresarial | Consultivo | Marina Ferraz | Fixo | R$ 7.000 | R$ 7.000 | 30/26 | 06/04/2026 | Entrega de parecer · 30/09/2026 (+16 dias) |
| A27 | 9495290-86.2025.8.26.0503 | Helena Duarte | Trabalhista | Execução | Rafael Lima | Êxito | R$ 7.000 | R$ 0 | 70/58 | 14/07/2025 | Cumprimento de sentença · 06/10/2026 (+22 dias) |
| A28 | 7679821-77.2026.8.26.0265 | Helena Duarte | Trabalhista | Inicial | Rafael Lima | Fixo | R$ 7.500 | R$ 4.500 | 55/24 | 22/06/2026 | Réplica · 15/09/2026 (+1 dia) |
| A29 | 8045862-82.2026.8.26.0491 | Carlos Eduardo Nunes | Previdenciário | Sentença | Rafael Lima | Misto (fixo R$ 3.600 + êxito R$ 4.000) | R$ 7.600 | R$ 3.600 | 40/40 | 09/03/2026 | Embargos de declaração · 17/09/2026 (+3 dias) |
| A30 | 9605863-76.2026.8.26.0026 | Marcos Vinícius Teles | Previdenciário | Recurso | Rafael Lima | Fixo | R$ 5.400 | R$ 5.400 | 35/30 | 01/06/2026 | Manifestação sobre o recurso · 13/09/2026 (-1 dia) |
| E01 | 4766902-26.2025.8.26.0051 | Padaria do Sol Ltda | Empresarial | Encerrado | Marina Ferraz | Fixo | R$ 12.000 | R$ 12.000 | 60/64 | 03/11/2025 | encerrado em 25/03/2026 |
| E02 | 9778116-95.2025.8.26.0106 | Construtora Horizonte | Cível | Encerrado | Marina Ferraz | Misto (fixo R$ 9.000 + êxito R$ 9.000) | R$ 18.000 | R$ 18.000 | 110/120 | 02/06/2025 | encerrado em 30/04/2026 |
| E03 | 8204296-70.2025.8.26.0146 | Marcos Vinícius Teles | Previdenciário | Encerrado | Rafael Lima | Êxito | R$ 6.500 | R$ 6.500 | 45/50 | 14/02/2025 | encerrado em 30/01/2026 |
| E04 | 9088515-39.2025.8.26.0125 | Loja Verde Comércio | Empresarial | Encerrado | Marina Ferraz | Fixo | R$ 6.000 | R$ 6.000 | 45/40 | 15/09/2025 | encerrado em 12/06/2026 |
| E05 | 8663770-96.2025.8.26.0481 | Oficina Mecânica Central | Trabalhista | Encerrado | Rafael Lima | Fixo | R$ 12.000 | R$ 12.000 | 95/100 | 05/05/2025 | encerrado em 31/07/2026 |
| E06 | 5211189-81.2025.8.26.0412 | Fernanda Castro | Família | Encerrado | Marina Ferraz | Fixo | R$ 7.000 | R$ 7.000 | 55/58 | 06/10/2025 | encerrado em 14/08/2026 |
| E07 | 6161129-80.2025.8.26.0663 | José Antônio Ribeiro | Previdenciário | Encerrado | Rafael Lima | Êxito | R$ 6.000 | R$ 6.000 | 40/44 | 01/04/2025 | encerrado em 26/06/2026 |
| E08 | 9420478-99.2025.8.26.0491 | Ana Beatriz Moreira | Trabalhista | Encerrado | Rafael Lima | Misto (fixo R$ 3.000 + êxito R$ 5.500) | R$ 8.500 | R$ 8.500 | 70/76 | 20/01/2025 | encerrado em 13/03/2026 |

- Casos consultivos têm referência CONS-ano-nº (sem número CNJ). Casos por hora (Clínica Bem-Estar CONS-2025-05, Agência Prisma): contratado = estimativa (horas × R$ 180), faturas mensais no dia 10 pelas horas do mês anterior.

## 7. Parcelas e inadimplência (14)

| Faixa de atraso | Parcelas | Valor | % do vencido |
|---|---|---|---|
| 1 a 6 dias | 1 | R$ 1.980 | 15 % |
| 7 a 14 dias | 0 | R$ 0 | 0 % |
| 15 a 29 dias | 1 | R$ 1.500 | 11 % |
| 30 dias ou mais | 5 | R$ 9.600 | 73 % |
| Antes da régua | 0 | R$ 0 | 0 % |

| Cobrar primeiro (14) | Cliente | Caso | Parcela | Vencimento | Valor | Dias de atraso | Faixa |
|---|---|---|---|---|---|---|---|
| 1 | Bistrô 42 | 8056747-83.2026.8.26.0561 | 3 | 18/03/2026 | R$ 2.100 | 180 | 30 dias ou mais |
| 2 | Bistrô 42 | 8056747-83.2026.8.26.0561 | 4 | 17/04/2026 | R$ 2.100 | 150 | 30 dias ou mais |
| 3 | Oficina Mecânica Central | 6184138-13.2026.8.26.0378 | 3 | 19/06/2026 | R$ 1.500 | 87 | 30 dias ou mais |
| 4 | Patrícia Gomes | 9616569-91.2026.8.26.0079 | 3 | 14/08/2026 | R$ 2.100 | 31 | 30 dias ou mais |
| 5 | Agência Prisma | 9362688-24.2025.8.26.0436 | 8 | 10/08/2026 | R$ 1.800 | 35 | 30 dias ou mais |
| 6 | Helena Duarte | 7679821-77.2026.8.26.0265 | 3 | 28/08/2026 | R$ 1.500 | 17 | 15 a 29 dias |
| 7 | Agência Prisma | 9362688-24.2025.8.26.0436 | 9 | 10/09/2026 | R$ 1.980 | 4 | 1 a 6 dias |

| Vencem nos próximos 30 dias (14) | Cliente | Caso | Parcela | Vencimento | Valor | Dias para vencer |
|---|---|---|---|---|---|---|
| 1 | Loja Verde Comércio | CONS-2026-02 | 2 | 17/09/2026 | R$ 2.800 | 3 |
| 2 | Clínica Bem-Estar | 2645033-67.2026.8.26.0012 | 5 | 24/09/2026 | R$ 2.700 | 10 |
| 3 | Marcos Vinícius Teles | CONS-2026-03 | 2 | 25/09/2026 | R$ 2.250 | 11 |
| 4 | Construtora Horizonte | 9586960-92.2026.8.26.0106 | 3 | 28/09/2026 | R$ 2.100 | 14 |
| 5 | Helena Duarte | 7679821-77.2026.8.26.0265 | 4 | 28/09/2026 | R$ 1.500 | 14 |
| 6 | Carlos Eduardo Nunes | 4746093-86.2026.8.26.0637 | 3 | 30/09/2026 | R$ 1.500 | 16 |
| 7 | Padaria do Sol Ltda | CONS-2026-01 | 4 | 05/10/2026 | R$ 1.500 | 21 |
| 8 | Escola Aurora | CONS-2026-04 | 3 | 10/10/2026 | R$ 1.100 | 26 |

- Total de parcelas cadastradas: 152 (pagas 118, das quais 30 pagas em 2025). Régua de cobrança: 1 dia (lembrete), 7 dias (mensagem do responsável), 15 dias (demonstrativo e renegociação), 30 dias (ligação e plano de pagamento).

## 8. Propostas (15 · Funil e 07 · Registro)

| Etapa (15) | Propostas | Valor | Ponderado | Taxa de passagem |
|---|---|---|---|---|
| Contato | 2 | R$ 18.800 | R$ 1.880 | 90 % |
| Reunião feita | 2 | R$ 13.700 | R$ 3.425 | 89 % |
| Proposta enviada | 3 | R$ 19.200 | R$ 9.600 | 81 % |
| Negociação | 2 | R$ 21.200 | R$ 15.900 | 85 % |
| Fechadas (total) | 7 | R$ 71.000 |  |  |
| Perdidas (total) | 4 | R$ 27.100 |  |  |
| Honorário médio das fechadas | R$ 10.143 |  |  |  |

| Nº | Cliente | Área | Serviço | Origem | Resp. | Valor | Modalidade | Etapa | Entrada | Envio | Última mov. | Fech. previsto | Fechamento | Motivo | Caso na 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-005 | Padaria do Sol Ltda | Empresarial | Assessoria mensal (12 meses) | Cliente antigo | Marina | R$ 18.000 | Fixo | Fechada | 08/06/2026 | 15/06/2026 | 29/06/2026 | 03/07/2026 | 29/06/2026 | — | A01 |
| 2026-006 | Ana Beatriz Moreira | Trabalhista | Ação trabalhista | Indicação de cliente | Rafael | R$ 6.000 | Êxito | Fechada | 15/06/2026 | 24/06/2026 | 07/07/2026 | 10/07/2026 | 07/07/2026 | — | A02 |
| 2026-007 | Construtora Horizonte | Cível | Cobrança judicial | Cliente antigo | Marina | R$ 15.500 | Misto | Fechada | 01/07/2026 | 08/07/2026 | 22/07/2026 | 31/07/2026 | 22/07/2026 | — | A03 |
| 2026-008 | Carlos Eduardo Nunes | Previdenciário | Revisão de benefício | Site e Google | Rafael | R$ 5.400 | Fixo | Fechada | 13/07/2026 | 17/07/2026 | 28/07/2026 | 05/08/2026 | 28/07/2026 | — | A04 |
| 2026-009 | Escola Aurora | Cível | Assessoria mensal (12 meses) | Cliente antigo | Marina | R$ 13.200 | Fixo | Fechada | 14/07/2026 | 21/07/2026 | 03/08/2026 | 07/08/2026 | 03/08/2026 | — | A07 |
| 2026-010 | Bistrô 42 | Trabalhista | Defesa em reclamação trabalhista | Indicação de cliente | Rafael | R$ 5.200 | Hora | Perdida | 22/06/2026 | 30/06/2026 | 14/07/2026 | 17/07/2026 | 14/07/2026 | Preço | — |
| 2026-011 | Fernanda Castro | Família | Divórcio e partilha | Site e Google | Marina | R$ 6.500 | Fixo | Perdida | 06/07/2026 | 10/07/2026 | 27/07/2026 | 31/07/2026 | 27/07/2026 | Fechou com outro escritório | — |
| 2026-012 | Loja Verde Comércio | Empresarial | Contratos e consultoria | Parceria (contador, imobiliária) | Marina | R$ 8.400 | Fixo | Fechada | 20/07/2026 | 23/07/2026 | 11/08/2026 | 14/08/2026 | 11/08/2026 | — | A05 |
| 2026-013 | Marcos Vinícius Teles | Previdenciário | Planejamento previdenciário | Instagram | Rafael | R$ 4.500 | Fixo | Fechada | 03/08/2026 | 06/08/2026 | 19/08/2026 | 28/08/2026 | 19/08/2026 | — | A06 |
| 2026-014 | Oficina Mecânica Central | Trabalhista | Ação trabalhista | Evento ou palestra | Rafael | R$ 4.400 | Êxito | Perdida | 04/08/2026 | 06/08/2026 | 25/08/2026 | 28/08/2026 | 25/08/2026 | Sem resposta | — |
| 2026-015 | Agência Prisma | Empresarial | Contratos e consultoria | Instagram | Marina | R$ 11.000 | Fixo | Perdida | 12/08/2026 | 14/08/2026 | 02/09/2026 | 04/09/2026 | 02/09/2026 | Preço | — |
| 2026-016 | Transportadora Rota Sul | Trabalhista | Assessoria mensal (12 meses) | Cliente antigo | Rafael | R$ 14.400 | Fixo | Negociação | 17/08/2026 | 20/08/2026 | 10/09/2026 (-4 dias) | 20/09/2026 (+6 dias) | — | — | — |
| 2026-017 | Clínica Bem-Estar | Empresarial | Contratos com convênios | Cliente antigo | Marina | R$ 6.800 | Fixo | Negociação | 24/08/2026 | 26/08/2026 | 28/08/2026 (-17 dias) | 12/09/2026 (-2 dias) | — | — | — |
| 2026-018 | Patrícia Gomes | Família | Inventário | Indicação de cliente | Marina | R$ 10.500 | Fixo | Proposta enviada | 26/08/2026 | 29/08/2026 | 29/08/2026 (-16 dias) | 26/09/2026 (+12 dias) | — | — | — |
| 2026-019 | José Antônio Ribeiro | Previdenciário | Revisão de benefício | Site e Google | Rafael | R$ 4.200 | Fixo | Proposta enviada | 28/08/2026 | 31/08/2026 | 31/08/2026 (-14 dias) | 08/09/2026 (-6 dias) | — | — | — |
| 2026-020 | Helena Duarte | Trabalhista | Ação trabalhista | Indicação de cliente | Rafael | R$ 5.800 | Êxito | Reunião feita | 02/09/2026 | — | 11/09/2026 (-3 dias) | 04/10/2026 (+20 dias) | — | — | — |
| 2026-021 | Luciana Farias | Cível | Cobrança judicial | Parceria (contador, imobiliária) | Marina | R$ 7.900 | Misto | Reunião feita | 04/09/2026 | — | 12/09/2026 (-2 dias) | 09/10/2026 (+25 dias) | — | — | — |
| 2026-022 | Construtora Horizonte | Empresarial | Assessoria mensal (12 meses) | Cliente antigo | Marina | R$ 13.200 | Fixo | Contato | 09/09/2026 | — | 13/09/2026 (-1 dia) | 14/10/2026 (+30 dias) | — | — | — |
| 2026-023 | Roberto Almeida | Cível | Discussão de contrato de prestação de serviços | Cliente antigo | Marina | R$ 4.500 | Misto | Proposta enviada | 09/09/2026 | 14/09/2026 (hoje) | 14/09/2026 (hoje) | 29/09/2026 (+15 dias) | — | — | — |
| 2026-024 | Marcos Vinícius Teles | Família | Divórcio e partilha | Cliente antigo | Marina | R$ 5.600 | Fixo | Contato | 11/09/2026 | — | 11/09/2026 (-3 dias) | 19/10/2026 (+35 dias) | — | — | — |

- Situação na 15 em 14/09: Patrícia Gomes = Parada (16 dias sem movimento); Clínica Bem-Estar e José Antônio Ribeiro = Previsão vencida; as demais abertas = Ativa. Motivos de perda: Preço 2 (Bistrô 42, Agência Prisma), Fechou com outro escritório 1 (Fernanda Castro), Sem resposta 1 (Oficina).
- **07 Registro** (as 10 mais recentes já enviadas, mesmos valores e situação): aguardando resposta 5 · fechadas 3 · perdidas 2 · valor fechado R$ 26.100 · taxa de fechamento 60 % · em aberto R$ 40.400. Alertas: Patrícia Gomes, Clínica Bem-Estar e Transportadora com validade vencida; José Antônio vence em até 3 dias.

## 9. O caso da proposta: Roberto Almeida (06 · Simulador e 07 · Proposta nº 2026-023)

- Cliente antigo (2 casos na carteira: sentença cível de R$ 15.000 todo pago e recurso misto). Novo caso: **discussão de contrato de prestação de serviços** (Cível). Valor em discussão R$ 60.000, chance de êxito 55 % → valor esperado da causa R$ 33.000. Custo-hora R$ 66,07 → hora mínima para o caso R$ 120,26.
| Etapa (06) | Horas | Custo (R$) |
|---|---|---|
| Reunião inicial e análise dos documentos | 4 | R$ 264,29 |
| Estudo do caso e estratégia | 6 | R$ 396,43 |
| Redação e protocolo inicial | 12 | R$ 792,86 |
| Acompanhamento e manifestações | 20 | R$ 1.321,43 |
| Audiências e reuniões | 8 | R$ 528,57 |
| Encerramento e prestação de contas | 3 | R$ 198,21 |
| **Total** | **53** | **R$ 3.501,78** |

| Despesa (06) | Valor | Cliente reembolsa? | Custo para o escritório |
|---|---|---|---|
| Taxas e custas | R$ 800 | Sim | R$ 0 |
| Deslocamentos | R$ 300 | Não | R$ 300 |
| Cópias e certidões | R$ 150 | Não | R$ 150 |
| Terceiros (perito, tradutor) | R$ 0 | Sim | R$ 0 |
| **Total de despesas** | R$ 1.250 |  | **R$ 450** |
| **Custo total do caso (horas + despesas absorvidas)** |  |  | **R$ 3.951,78** |

| Modalidade (06) | Valor pretendido | Receita esperada | Impostos | Custo do caso | Margem esperada | Margem % | Se perder | Risco |
|---|---|---|---|---|---|---|---|---|
| Fixo | R$ 7.000 | R$ 7.000 | R$ 560 | R$ 3.952 | R$ 2.488 | 36 % | R$ 2.488 | Baixo |
| Hora | R$ 180,00/h | R$ 9.540 | R$ 763 | R$ 3.952 | R$ 4.825 | 51 % | R$ 4.825 | Baixo |
| Êxito | 25 % | R$ 8.250 | R$ 660 | R$ 3.952 | R$ 3.638 | 44 % | −R$ 3.952 | Alto |
| Misto | R$ 4.500 + 15 % | R$ 9.450 | R$ 756 | R$ 3.952 | R$ 4.742 | 50 % | R$ 188 | Baixo |

- Recomendação do simulador: **Hora** (margem esperada R$ 4.825, risco Baixo); fora por risco alto: Êxito. Texto do ponto de equilíbrio da hora: "Hora mínima sem prejuízo: R$ 81,05 (você cobra R$ 180,00)".
- **Proposta 07 (nº 2026-023, 19/09/2026, válida por 15 dias até 04/10/2026, modalidade Misto)**: objeto "Acompanhamento da discussão sobre contrato de prestação de serviços, da análise inicial ao encerramento.".
| Etapa ou serviço (07) | O que inclui | Prazo previsto | Horas | Valor |
|---|---|---|---|---|
| Análise inicial e planejamento | Reunião, leitura dos documentos e definição da estratégia | até 15 dias | 8 | R$ 900 |
| Fase inicial | Redação e protocolo do pedido, acompanhamento das primeiras respostas | até 60 dias | 18 | R$ 1.800 |
| Acompanhamento até a decisão | Manifestações, audiências e reuniões com o cliente | durante o caso | 22 | R$ 1.200 |
| Encerramento | Prestação de contas e organização dos documentos finais | ao fim do caso | 5 | R$ 600 |
| **Total dos honorários fixos** |  |  | **53** | **R$ 4.500** |
| Honorários de êxito | sobre o resultado, ao fim do caso |  |  | 15 % |

- Condições: entrada 40 % = **R$ 1.800** na aceitação; restante R$ 2.700 em **3 parcelas de R$ 900** (900, 900, 900; datas contadas da data da proposta = HOJE()); forma de pagamento Pix. Na 15 a proposta está como "Proposta enviada" (entrada 09/09, envio hoje, previsão de fechamento em 15 dias).

## 10. Metas do trimestre (19), reserva (12) e provisão (10)

- 3º trimestre de 2026 (01/07 a 30/09): semana **11 de 13**, 82 % decorrido. Resultados-chave: 8 · atingidos 0 · em risco 3 · progresso médio 60 %.
| Objetivo | Resultado-chave | Dono | Unid. | Partida (30/06) | Meta | Atual (11/09) | Progresso | Semáforo | Sentido | S1…S11 (sextas 03/07 → 11/09) |
|---|---|---|---|---|---|---|---|---|---|---|
| Caixa mais previsível | Inadimplência: vencido ÷ (pago + vencido) (%) | Rafael | % | 3,4 | 3,0 | 4,6 | 0 % | Em risco | Menor é melhor | 3,4 · 3,3 · 4,1 · 3,2 · 3,0 · 3,0 · 2,9 · 3,6 · 3,5 · 4,0 · 4,6 |
| Horas que viram honorário | Horas faturáveis no mês (%) | Rafael | % | 76,9 | 80,0 | 79,5 | 84 % | No ritmo | Maior é melhor | 81,7 · 81,8 · 73,8 · 76,2 · 76,9 · 75,5 · 80,0 · 80,3 · 82,3 · 85,9 · 79,5 |
| Fechar mais propostas | Propostas fechadas no trimestre | Marina | propostas | 0,0 | 8,0 | 6,0 | 75 % | No ritmo | Maior é melhor | 0,0 · 1,0 · 1,0 · 2,0 · 3,0 · 4,0 · 5,0 · 6,0 · 6,0 · 6,0 · 6,0 |

- **12 Reserva**: meta 3 meses de custo fixo × custo fixo médio R$ 18.500 (jun/jul/ago, com pró-labore) = **R$ 55.500**; reserva hoje **R$ 12.000**; falta R$ 43.500; cobre **0,6 meses**; semáforo "Vermelho: menos de 1 mês de custo fixo guardado"; com aporte de R$ 3.000/mês a meta chega em **Dezembro/2027**. Saldo em caixa R$ 43.683 − compromissos não pagos R$ 15.402 = caixa livre R$ 28.281 ("contando o caixa livre: 2,2 meses").
| Meta de caixa do trimestre (12) | Alvo | Atual | Progresso | Prazo | Situação |
|---|---|---|---|---|---|
| Reserva com 1 mês de custo fixo | R$ 18.500 | R$ 12.000 | 65 % | 31/12/2026 | Em andamento |
| Receber R$ 75.000 no trimestre | R$ 75.000 | R$ 61.580 | 82 % | 30/09/2026 | Em andamento |
| Conta de provisão de impostos com o saldo da planilha 10 | R$ 11.320 | R$ 9.400 | 83 % | 30/09/2026 | Em andamento |

- **10 Provisão (Config = Setembro, alíquota 8 %)**: 13º dos sócios 500 + 500 e recesso da estagiária 155,56 por mês; entradas de setembro até 11/09 R$ 5.220; a separar no mês R$ 1.573; **saldo provisionado ao fim de setembro R$ 11.320** (separado 27.407 − usado 16.087 em guias); compromisso do mês seguinte R$ 418; situação Coberto. Janeiro foi o único mês com "Falta separar" (492).
| Mês (10) | Entradas (sem Outras) | Provisão 8 % | Total a separar | Guia paga no mês | Saldo provisionado |
|---|---|---|---|---|---|
| Janeiro | R$ 21.050 | R$ 1.684 | R$ 2.840 | R$ 1.648 | R$ 1.192 |
| Fevereiro | R$ 23.070 | R$ 1.846 | R$ 3.001 | R$ 1.684 | R$ 2.509 |
| Março | R$ 28.590 | R$ 2.287 | R$ 3.443 | R$ 1.846 | R$ 4.105 |
| Abril | R$ 19.760 | R$ 1.581 | R$ 2.736 | R$ 2.287 | R$ 4.555 |
| Maio | R$ 31.120 | R$ 2.490 | R$ 3.645 | R$ 1.581 | R$ 6.619 |
| Junho | R$ 27.420 | R$ 2.194 | R$ 3.349 | R$ 2.490 | R$ 7.478 |
| Julho | R$ 29.460 | R$ 2.357 | R$ 3.512 | R$ 2.194 | R$ 8.796 |
| Agosto | R$ 26.900 | R$ 2.152 | R$ 3.308 | R$ 2.357 | R$ 9.747 |
| Setembro | R$ 5.220 | R$ 418 | R$ 1.573 | R$ 0 | R$ 11.320 |


## 11. Resumo do mês (20): agosto × julho de 2026

| Indicador | Agosto | Julho | Variação | Meta | Vs. meta | Situação |
|---|---|---|---|---|---|---|
| Entrou no mês (recebimentos) | R$ 26,900 | R$ 29,460 | -8.7% | R$ 26,000 | +3.5% | No alvo |
| Saídas do mês (custos, despesas de casos, pró-labore e impostos provisionados) | R$ 21,212 | R$ 21,167 | +0.2% | R$ 21,500 | -1.3% | No alvo |
| Resultado do mês | R$ 5,688 | R$ 8,293 | -31.4% | R$ 4,000 | +42.2% | No alvo |
| Margem do mês | 21.1% | 28.2% | -7.1 p.p. | 20.0% | +1.1 p.p. | No alvo |
| Horas registradas no mês | 304.0 h | 233.5 h | +30.2% | 280.0 h | +8.6% | No alvo |
| Horas faturáveis | 81.6% | 76.9% | +4.7 p.p. | 75.0% | +6.6 p.p. | No alvo |
| A receber (carteira; inclui êxito de casos ativos) | R$ 117,210 | R$ 117,700 | -0.4% | — | — | informativo |
| Vencido (parcelas em atraso) | R$ 11,100 | R$ 7,500 | +48.0% | R$ 10,000 | +11.0% | Acima da meta |
| Inadimplência (vencido ÷ (pago + vencido)) | 4.0% | 3.0% | +1.0 p.p. | 4.0% | +0.0 p.p. | No alvo |
| Propostas abertas (valor) | R$ 46,900 | R$ 21,600 | +117.1% | R$ 40,000 | +17.3% | No alvo |
| Casos ativos | 30 | 28 | +7.1% | 30 | +0.0% | No alvo |
| Honorários fechados em propostas no mês | R$ 26,100 | R$ 26,900 | -3.0% | R$ 20,000 | +30.5% | No alvo |

(Valores como o Excel em português mostra; os separadores seguem o idioma do Excel.)
- Destaques automáticos (lidos da 20, aba Resumo): • Maior melhora contra Julho: Horas faturáveis (+4,7 p.p.). • Maior piora contra Julho: Margem do mês (-7,1 p.p.). • Mais longe da meta: Vencido (parcelas em atraso) (+11,0% da meta, acima da meta). • Indicadores no alvo: 10 de 11 com meta.
- Observações do escritório (célula amarela do exemplo, lida da 20): "Agosto fechou com três propostas novas viradas em caso (Escola Aurora, Loja Verde e Marcos Vinícius); a cobrança da Construtora já havia entrado em julho e não conta neste mês; Bistrô 42 e Agência Prisma seguem com parcelas vencidas e entraram na régua de cobrança; o caso da Oficina (execução) e o recurso da Escola Aurora estouraram as horas estimadas."
## 12. Histórico mensal (17 · Histórico; jan–ago = Painel mensal da 09 e 16, carteira no fim de cada mês; setembro = Dados)

| Mês | Prazos hoje+7 | Atrasados | Horas | Faturáveis | % fat. | Entrou | Saiu | Sobrou | A receber | Vencido | Inadimpl. | Propostas abertas | Valor das propostas | Casos ativos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Janeiro | — | — | — | — | — | R$ 21.050 | R$ 20.408 | R$ 642 | R$ 117.600 | R$ 1.200 | 1,4 % | 0 | R$ 0 | 17 |
| Fevereiro | — | — | — | — | — | R$ 23.070 | R$ 21.684 | R$ 1.386 | R$ 94.530 | R$ 2.000 | 1,9 % | 0 | R$ 0 | 17 |
| Março | — | — | — | — | — | R$ 28.590 | R$ 22.276 | R$ 6.314 | R$ 83.320 | R$ 2.100 | 1,6 % | 0 | R$ 0 | 17 |
| Abril | — | — | — | — | — | R$ 20.240 | R$ 26.638 | −R$ 6.398 | R$ 88.560 | R$ 4.200 | 2,7 % | 0 | R$ 0 | 19 |
| Maio | — | — | — | — | — | R$ 31.120 | R$ 21.181 | R$ 9.939 | R$ 97.640 | R$ 4.200 | 2,2 % | 0 | R$ 0 | 22 |
| Junho | — | — | — | — | — | R$ 27.420 | R$ 23.085 | R$ 4.335 | R$ 115.320 | R$ 7.500 | 3,4 % | 2 | R$ 11.200 | 25 |
| Julho | — | — | 233,5 | 179,5 | 77 % | R$ 29.460 | R$ 28.898 | R$ 562 | R$ 117.700 | R$ 7.500 | 3,0 % | 2 | R$ 21.600 | 28 |
| Agosto | — | — | 304,0 | 248,0 | 82 % | R$ 26.900 | R$ 21.897 | R$ 5.003 | R$ 117.210 | R$ 11.100 | 4,0 % | 5 | R$ 46.900 | 30 |
| Setembro | 14 | 7 | 109,5 | 87,0 | 79 % | R$ 5.220 | R$ 5.320 | −R$ 100 | R$ 111.990 | R$ 13.080 | 4,6 % | 9 | R$ 72.900 | 30 |

- Prazos: a agenda (01) não guarda histórico (o escritório começou a anotar em setembro). Horas: o controle (16) começou em julho. Propostas abertas: o funil (15) começou em junho.

## 13. Rotina (03) e checklist (04)

- **03 Rotina**: 9 rotinas (4 de segunda = 12 min; 5 de sexta = 18 min; **30 min/semana**); registradas S29 a S36 (20/07 a 07/09/2026); semana atual S37 · 14/09; aderência nas últimas 4 semanas **83 %** (segunda 94 %, sexta 75 %); rotina mais pulada: "Enviar a cobrança educada das parcelas atrasadas" (1 de 4). Série S29–S36: 67 %, 78 %, 89 %, 89 %, 100 %, 78 %, 78 %, 78 %.
- **04 Checklist**: casos cadastrados 38 · abertos com pendência de abertura 7 · encerrados com pendência 3 · itens pendentes no total **12** · casos sem pendência 28. Itens mais esquecidos: "Caso cadastrado no caixa e na carteira" (2) e, no encerramento, "Avaliação do cliente pedida" (2). Fernanda Castro (encerrado) pende "Última parcela cobrada e recebida" (a parcela vencida da 14).
