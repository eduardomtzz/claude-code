# O que mudou desde o zip `seu-socio-gestor-auditoria-final-4.zip`

Os dois achados da confirmação 4 (F4-G01 e F4-G02) foram reproduzidos antes de mexer, com os números
do seu parecer; nenhum falso. Correção no gerador dos sete arquivos de preço, regenerados e
recalculados em LibreOffice pt-BR. A busca de "mesma causa" foi estendida aos dois 05, onde a
sua matriz mostrou o mesmo padrão (custo fixo em texto, horas em texto) sem contá-lo como achado.

## F4-G01 — dado obrigatório vazio ou em texto tratado como zero ou classificado

| Arquivo | Antes (reproduzido) | O que mudou | Depois |
|---|---|---|---|
| 03/06 Simulador | B45 "abc": Hora "Baixo", recomendação Misto, #VALUE! na receita; B13 vazio = chance zero; B12 "abc" = 7 #VALUE!; hora com texto no bloco 2 = #VALUE! em cadeia; despesa com texto sumia do custo (C5 subia para 5.125) | nova conferência **B16 "Dados do caso conferem?"**: valor em discussão ≥ 0, chance 0–100 %, fixo ≥ 0, hora ≥ 0, % de êxito 0–100 %, entrada ≥ 0, % do misto 0–100 %; diz qual falta. Cada modalidade exige só o que usa (Fixo: fixo; Hora: hora; Êxito: %, valor, chance; Misto: entrada, %, valor, chance) e, sem ele, diz "Falta …". Recomendação: "Complete os dados do caso"; KPIs vazios. Horas ou despesas com texto: custo do caso diz "Horas com texto (bloco 2)" / "Despesa com texto (bloco 3)" e tudo que depende do custo fica suspenso. Validação decimal nova nessas sete células | B45 "abc": Hora "Falta a hora cobrada", A5 "Complete os dados do caso". B13 vazio: Êxito e Misto "Falta …", Fixo e Hora mantidos. B19 "abc": custo "Horas com texto (bloco 2)", recomendação "Corrija horas ou despesas". Zero digitado no fixo continua classificado (Alto: não cobre as despesas) |
| 04/06 Precificação, 04/08 Tabela | B5/B8 vazio: custo 30,67, mínimo 51,98, "No alvo ou acima"; D5 "abc" = #VALUE!; gera retorno? vazio ou retorno da Config vazio = consulta sem o tempo do retorno; convênio "abc" = #VALUE! no prejuízo | tempo com retorno e custo cheio por uma regra só (`f_tempo`, `f_custo`): minutos ≥ 0, "gera retorno?" = Sim/Não, retorno da Config numérico quando Sim, material ≥ 0; a linha diz "faltam os minutos", "falta: gera retorno?", "falta o retorno em Config" ou "falta o material". Situação "Faltam dados da linha" ou "Preço inválido" (vermelho). Resumo da 06 e KPIs da 08: "n linha(s) ou preço(s) incompletos" em vez de contar só as linhas completas | 04/06 B5 vazio: E5:G5 "faltam os minutos", K5 "Faltam dados da linha", E24:E25 "1 linha(s) … incompletos". 04/08 B8 vazio: idem em E8:N8 e C5/E5. Sem #VALUE! |
| 04/07 Simulador | glosa vazia = 0 % (líquido 26.945,33); prazo e juros vazios = 0; minutos, retorno e material vazios na Config = 0 via INDEX (custo 104 e 126,67) | INDEX da Config passa por `ISNUMBER(INDEX(…))`; tempo e custo pela mesma regra da 06; prazo e glosa exigem número (glosa 0–100 %); custo do dinheiro exige juros quando o prazo é maior que zero (prazo zero dispensa); a leitura (N) diz o dado que falta, em vermelho | C11 vazio: N20 "falta a glosa", líquido e resultado do mês suspensos. E19 vazio: custo "falta o retorno em Config". Juros vazio: só os três convênios suspensos; o particular (prazo 0) segue |
| 03/08 Tabela de referência | valor ou horas do caso em texto: #VALUE! em H:K e em G5 | "valor ou horas inválidos" na linha; KPIs "n caso(s) com valor ou horas inválidos"; horas típicas em texto na faixa: "horas inválidas" | F5 "abc": H5/J5 avisam, E5 e G5 avisam; 0 #VALUE! |
| 03/05, 04/05 | custo fixo em texto ou com nome e sem valor sumia da soma (custo-hora 56,07 e 172,14); "já está nos custos fixos?" vazio tirava a pessoa da soma; horas de trabalho em texto = #VALUE! na ocupação | total de custos fixos diz "custo fixo sem valor numérico"; a pessoa sem a marcação vira cadastro incompleto; ocupação só com números; aviso do Painel diz qual aba | custo-hora "cadastro incompleto" nos três casos; 0 #VALUE! |

## F4-G02 — totais e médias sobre populações diferentes

| Arquivo | Antes | O que mudou | Depois |
|---|---|---|---|
| 04/07 mix do mês | B20 apagado com 25 atendimentos: D49 = 24.320,33, E49 = 16.986,67, F49 = 10.600,33 (≠ D49 − E49) | pagador com atendimentos e sem líquido conhecido: a linha diz "falta o valor líquido"; D49 e F49 dizem "líquido incompleto em n pagador(es)"; E49 continua (custo não depende do preço). Atendimentos em texto: total "atendimentos com texto" | B20 vazio: D49/F49 "líquido incompleto em 1 pagador(es)", E49 = 16.986,67. B20 = 0: D44 = 0, F44 = −3.266,67 e F49 = 7.333,66 = D49 − E49 |
| 04/08 KPIs | P8 apagado: receita/hora 911,83 e "contra a hora mínima" +169 % | receita por hora exige volume, produção e minutos em toda linha com dados: "volume incompleto em n linha(s)"; "valor médio praticado" da linha diz "volume ou produção faltando" | P8 vazio: I5 "volume incompleto em 1 linha(s)", K5 vazio |

## Arquivos cujo conteúdo mudou, comparados com o pacote final-4

Comparação célula a célula, incluindo listas de validação (dv) e regras de cor (cf). Os outros 46
arquivos não mudaram de fórmula, dado, validação ou regra.

| Arquivo | Células diferentes | Abas | Validação (dv) ou regra de cor (cf) |
|---|---:|---|---|
| 03-advogados/05-custo-hora.xlsx | 40 | Custos fixos, Painel, Pessoas | — |
| 03-advogados/06-simulador-de-honorarios.xlsx | 52 | Simulador | Simulador:cf, Simulador:dv |
| 03-advogados/08-tabela-de-referencia.xlsx | 882 | Nossos casos, Referência | — |
| 04-medicos/05-custo-da-hora.xlsx | 29 | Custos fixos, Equipe, Painel | — |
| 04-medicos/06-precificacao.xlsx | 104 | Precificação | Precificação:cf |
| 04-medicos/07-simulador-convenio-x-particular.xlsx | 100 | Simulador | Simulador:cf |
| 04-medicos/08-tabela-de-precos.xlsx | 148 | Tabela | Tabela:cf |

## Travas

| Trava | Resultado |
|---|---|
| `recalc_todos.py` | 189.800 fórmulas · 0 erro (+1: B16 da 06 dos Advogados) |
| Coerência Essencial / Completo / Advogados / Médicos | 594 / 3.559 / 293 / 702 · 0 falhas |
| `verifica_lancamento.py` | 25 · 0 falhas |
| Inventário | 306 validações (+7 na 06 dos Advogados) · 483 regras · 0 `_xlfn` · 0 regra sem INDIRECT · 0 literal > 255 · 0 TEXT com data · 0 entrega ≠ gerado |
| Cenários (`CENARIOS.md`) | 76 cenários, das quatro rodadas, em 7 arquivos · 0 com erro de fórmula · exemplo com os mesmos números em todas |
| `HASHES.md` | 53 arquivos · 0 diferença entre gerado e pacote |

## O que continua pendente e não depende de mim

O roteiro nativo em Excel 2016 e Google Sheets (parte 7 do seu parecer, passos 7.4 e 7.5 novos).
As durações das aulas: o zip dos vídeos tem 78 MB e não pôde ser anexado; `DURACOES-AULAS.md` traz
ffprobe, tamanho e SHA-256.
