# O que mudou desde o zip `seu-socio-gestor-auditoria-final-6.zip`

Os sete achados da revisão ampliada (F6-G01 a G05, F6-M01 e M02) foram reproduzidos antes de mexer,
com os números do seu parecer. Nenhum é falso. Cada contraexemplo seu está em `CENARIOS.md` (prefixo
F6-). A varredura foi refeita conforme os pontos cegos que você apontou (ver `varredura/VARREDURA.md`)
e achou mais quatro defeitos, também corrigidos (prefixo VARR).

## Graves

| Achado | Antes | Depois |
|---|---|---|
| F6-G01 custo-hora −1 (03/06 B11; Config!B7 de 03/08, 04/06 e 04/08; 04/07 Config!B5) | C29 = −53, B15 = 12,08, Hora recomendada; 04/06 K5 "No alvo ou acima"; 04/07 hora mínima −1,69 | predicado único `ISNUMBER(custo-hora)` e custo-hora ≥ 0 em todos os consumidores: "falta o custo-hora" e custo, preço mínimo, margem, comparação e recomendação suspensos. Zero continua valendo. Validação "número ≥ 0" nas cinco células de entrada |
| F6-G02 resíduo (03/05 A5 vazio + C5 "abc"; 04/05 A5 vazio + D5 "abc") | K5 = 0, aviso vazio, custo-hora calculado | linha ativa = qualquer campo preenchido; sem nome a linha diz "falta o nome", o K marca 1 e o Painel mostra "cadastro incompleto" |
| F6-G02 (04/07 Config!A11 vazio com tabela 120 e 25 atendimentos) | G5 "MediPlan: R$ 129" | a linha do pagador diz "pagador sem nome". G5/J5 dizem "incompleto: n convênio(s) sem líquido", e o mix e o resultado do mês avisam |
| F6-G03 total bruto de despesas (03/06 B39) | B34 vazio: B39 = R$ 950; despesa nova A37/C37 "Não" sem valor: B39 = R$ 1.250 | B39 diz "despesa incompleta" quando uma linha ativa não tem valor ou tem texto ou negativo. Não exige a resposta de reembolso: com C34 vazio e o valor conhecido, B39 soma R$ 1.250 e só D39 avisa |
| F6-G04 convênio 0 (04/06 L5; 04/08 I8) | E25 caía de 14 para 13 e E26 ficava 60,43; O8 caía de 3 para 2 | perda absoluta = preço × (1 − imposto) − custo, para todo preço numérico ≥ 0, sem depender da margem percentual. L5 = 0 dá T5 = −130,67, E25 = 14 e E26 = 130,67; I8 = 0 dá O8 = 3 e E5 = 14. A regra de cor vermelha segue a mesma conta |
| F6-G05 material e minutos −1 na Config (04/07 D19, B19) | C31 = −1, D31 = 339,20, E31 = 535,58/h, "Contribui" | os lookups de minutos e material usam o predicado ≥ 0 (`num_ok`): B9/B11 dizem o que falta, e C31:G36 fica suspenso. D19 = 0 continua valendo (D31 = 338,20) |

**Exceção do retorno (F6-G04), para você aceitar ou recusar.** No exemplo, o Retorno tem particular 0
e os três convênios 0 de propósito: o tempo dele já está no custo da consulta. Aplicada sem exceção,
a regra criaria três "tabelas abaixo do custo" falsas. Por isso, convênio 0 conta como prejuízo,
exceto quando o particular da mesma linha também é 0 (procedimento sem cobrança). Isso está escrito
na nota da aba e nas convenções.

## Médios

| Achado | Antes | Depois |
|---|---|---|
| F6-M01 particular em branco (04/06 I5; 04/08 H8) | situação vazia, resumo "0 de 7" | o particular é obrigatório: "Falta o preço particular" (vermelho), e a linha entra em "n linha(s) ou preço(s) incompletos" no resumo e nos cartões. Zero digitado continua "Sem cobrança" |
| F6-M02 faixa invertida (03/08 C9 = 8, D9 = 3) | mínimo 1.023 > máximo 506, ponto médio 764 | F9 e G9 dizem "faixa invertida (de > até)", H9 fica vazio e I9 diz "Corrija a faixa de horas: o de é maior que o até" |

## Achados pela varredura desta rodada (VARR)

| Arquivo | Antes | Depois |
|---|---|---|
| 03/05 e 04/05 Custos fixos | valor numa linha nova sem descrição entrava no total sem aviso | linha com dado e sem descrição = "custo fixo sem descrição, sem valor numérico ou negativo", e o Painel mostra "cadastro incompleto" |
| 03/05 Painel!B20 (horas de trabalho) | somava as horas de linha sem nome | usa a mesma população do resto do Painel: "cadastro incompleto" |
| 03/05 e 04/05 Painel, por pessoa | pessoa nova só com nome: papel (e remuneração, nos Médicos) mostrava 0 | fica vazio |
| 04/08 Tabela!S9 | particular −1 no retorno: −100 % contra o mínimo | vazio (a situação já diz "Preço inválido") |

## Arquivos cujo conteúdo mudou, comparados com o pacote final-6

| Arquivo | Células diferentes | Abas | Validação (dv) ou regra de cor (cf) |
|---|---:|---|---|
| 03-advogados/05-custo-hora.xlsx | 33 | Custos fixos, Painel, Pessoas | — |
| 03-advogados/06-simulador-de-honorarios.xlsx | 23 | Simulador | Simulador:dv |
| 03-advogados/08-tabela-de-referencia.xlsx | 122 | Config, Referência | Config:dv |
| 04-medicos/05-custo-da-hora.xlsx | 42 | Custos fixos, Equipe, Painel | — |
| 04-medicos/06-precificacao.xlsx | 80 | Precificação | Config:dv, Precificação:cf |
| 04-medicos/07-simulador-convenio-x-particular.xlsx | 19 | Simulador | Config:dv |
| 04-medicos/08-tabela-de-precos.xlsx | 53 | Config, Tabela | Config:dv, Tabela:cf |

Os outros 46 arquivos não mudaram de fórmula, dado, validação ou regra. Os números do exemplo nos
sete arquivos são os mesmos do final-6. Só mudaram duas notas de texto: 04/06 A19 e 04/08 A21, que
explicam a regra do convênio 0.

## Travas

| Trava | Resultado |
|---|---|
| `recalc_todos.py` | 189.800 fórmulas · 0 erro |
| Coerência Essencial / Completo / Advogados / Médicos | 594 / 3.559 / 293 / 702 · 0 falhas |
| `verifica_lancamento.py` | 0 falhas (pendências externas: link de checkout dos Médicos e ID do Pixel) |
| Inventário | 313 validações (+5 no custo-hora) · 483 regras · 0 TEXT com data · 0 entrega ≠ gerado |
| Varredura (`varredura/`) | 1.994 mutações · 0 erro de fórmula · 0 mudança silenciosa fora das decisões, cada decisão limitada às saídas listadas |
| Cenários (`CENARIOS.md`) | 124 cenários das seis rodadas · 0 com erro de fórmula. Os 98 anteriores repetem os mesmos números; só o aviso de custo fixo cita "sem descrição" |
| `HASHES.md` | 53 · 0 diferença |

## Pendente e fora do meu alcance

Roteiro nativo em Excel 2016 e Google Sheets. As durações das aulas precisam ser medidas por você: o
zip de 78 MB não pode ser anexado aqui, e `DURACOES-AULAS.md` traz ffprobe, tamanho e SHA-256.
