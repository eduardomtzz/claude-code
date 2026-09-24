# O que mudou desde o zip `seu-socio-gestor-auditoria-final-2.zip`

Os cinco achados da confirmação (G01, G02, M01, N01, L01) foram reproduzidos antes de mexer; nenhum
falso. Toda correção foi no gerador; os arquivos afetados foram regenerados e recalculados em
LibreOffice pt-BR. Ao corrigir G02, a mesma causa apareceu em três arquivos que o parecer não citou
(08 dos Advogados, 07 e 08 dos Médicos): foram tratados juntos. `CENARIOS.md` traz a saída literal
dos cenários, rodados em cópias descartáveis.

## Graves

| # | Arquivo · célula | Causa reproduzida | O que mudou | Prova |
|---|---|---|---|---|
| G01 | 04/06 Precificação!E22:E26; 03/06 Simulador!C29 | com o custo-hora em branco, o resumo da 04/06 dizia hora mínima 0, "0 de 7", 0 tabelas e 0 de prejuízo (COUNTIF/MIN sobre auxiliares que viravam 0); na 03/06, `SUM(C19:C28)` ignorava o texto "falta o custo-hora" e dava 0 | resumo da 04/06: cada linha diz "falta o custo-hora em Config" (ou "margens inválidas (Config)") em vez de apurar; C29 = `IF(ISNUMBER(B11);SUM(C19:C28);"falta o custo-hora")`. Mesma regra nos totais do mix da 04/07 (custo cheio e resultado do mês) | 04/06 B7 vazio: E22:E26 = "falta o custo-hora em Config". 03/06 B11 vazio: C29 = "falta o custo-hora", D40 e B15 idem. Zero digitado: 04/06 B7 = 0 → E22 = 0, E23 = 0 e F5 = 4 (material); 03/06 B11 = 0 → C29 = 0, B15 = 13,69 |
| G02 | Config e saídas de preço de 03/05, 03/06, 03/08, 04/05, 04/06, 04/07, 04/08 | a guarda olhava só o denominador `1 − impostos − margem ≤ 0`: margem −30 %, texto, branco, mínima acima da alvo e alvo inválida com mínima válida passavam; E23 da 04/06 calculava −20.000; K5/B40 comparavam com H5/B38 em texto | um predicado único por arquivo, com as MESMAS condições da validação e ISNUMBER antes de qualquer conta: `IF(AND(ISNUMBER(imp);ISNUMBER(mín);ISNUMBER(alvo));IF(AND(imp>=0;imp<1;mín>=0;mín<=alvo;alvo<1;imp+alvo<1);"Sim";"Não");"Não")`. Fica visível na Config ("Margem e impostos conferem?": 03/05 B10, 04/05 B11, 03/06 B13, 04/06 B13, 04/08 B15) ou dentro da hora mínima (03/08 B12:B13, com a folga ≥ 0; 04/07 B14). Toda hora mínima, preço, margem, situação, risco, recomendação, resumo e KPI consulta o predicado. Validação customizada também em 03/08 (B8:B11) e 04/07 (B6:B7), que não tinham | 04/06: B9 = B10 = 90 %, só B10 = 90 %, B9 = 60 %/B10 = 30 %, B9 = −30 %, B9 = "abc", B8 vazio → G5, H5, E23:E26, K5, B37, B38, B40 = "margens inválidas"; nenhum número. 03/06 B8 = 95 %, −30 %, "abc" → B15, risco ×4, recomendação suspensos. 03/05 e 04/05: margem 95 %/90 %, −30 %, "abc", imposto vazio → J5, B16, B17 = "margens inválidas (Config)" (antes, "abc" dava #VALUE!). 03/08, 04/07, 04/08: idem nos cenários de `CENARIOS.md`. Imposto 0 e margem 0 continuam aceitos e calculados |

## Médios e leve

| # | Arquivo | Causa | O que mudou | Prova |
|---|---|---|---|---|
| M01 | referencia/numeros-03-advogados.md §13 | a frase sobre Fernanda era texto fixo no `numeros.py`, fora do alcance da correção de G03 | a linha do checklist é gerada do Checklist da 04: itens mais esquecidos contados (pendente = nem Sim nem N/A, a regra de AA/AB) e, para cada encerrado com pendência, o texto da coluna "O que falta" | "Fernanda Castro (Avaliação do cliente pedida)"; "Nenhum encerrado tem parcela pendente: todos estão quitados na 13 e na 14" |
| N01 | referencia/oferta-02-completo.md | a troca de "2 min/3 min" da M02 atingiu a coluna "O que faz" da tabela das planilhas | as oito descrições voltaram (texto anterior à troca); a tabela das aulas passou a "Duração (medida no arquivo)", com a duração lida de cada MP4 por ffprobe | 2:25 · 2:36 · 2:56 · 2:01 · 2:27 · 2:16 · 2:11 · 2:41. Nenhuma outra oferta tem "2 min"/"3 min" em tabela de planilha |
| L01 | 01/01 e 02/01 Hoje!A2 | o gerador já estava certo desde a rodada final; o arquivo regenerado não foi copiado para `entrega/` do Essencial nem para o Completo. O registro anterior afirmou "0 códigos de data nos 53" sem contar nos arquivos entregues | cópia refeita (Essencial e as três cópias do Completo); o inventário ganhou duas colunas de controle, calculadas nos arquivos de `entrega/`: **TEXT com data** (analisa o último argumento de cada TEXT, respeitando aspas e parênteses) e **Entrega ≠ gerado** (compara byte a byte com o último arquivo gerado) | Hoje!A2 = `"Painel de "&TEXT(DAY(Config!B4);"00")&"/"&TEXT(MONTH(Config!B4);"00")&"/"&YEAR(Config!B4)&…` nas duas cópias; inventário: 0 TEXT com data e 0 arquivo diferente do gerado nos 53 |

## Achados meus ao corrigir

| Arquivo | O que era | O que mudou |
|---|---|---|
| 03/08, 04/07, 04/08 | a mesma causa de G01/G02: `IFERROR(custo/(1−imp−margem);"")` sem validação; custo-hora em branco dava hora mínima 0; margem −30 % ou mínima > alvo davam faixa e situação | predicado único e "falta o custo-hora" (ver G02); KPIs, faixa por área, contagens e regras de cor só calculam com hora mínima numérica |
| 03/08 Referência!H | faixa média `(F+G)/2` quebrava em #VALUE! quando F/G eram aviso | só calcula com F e G numéricos |
| 04/07 Mix do mês | "Custo cheio no mês" somava 0 quando as margens eram inválidas, embora o custo não dependa delas | custo cheio do mês depende só do custo-hora; total diz "falta o custo-hora" / "margens inválidas" conforme a causa |
| 03/06 A6 | com horas zeradas dizia "nenhuma modalidade com risco aceitável" | "Sem recomendação ainda: complete o custo-hora, as horas estimadas e a Config." |
| 16 planilhas sem gráfico (Advogados 01, 02, 03, 04, 07, 11, 19, 20; Completo 04, 05, 06; Médicos 03, 04, 11, 19, 20) e a Semana Organizada | o texto padrão do "Como usar" dizia que "gráficos funcionam" no Google Sheets em arquivos que não têm gráfico; a Semana Organizada tinha a mesma promessa no gerador | o gerador tira a palavra "gráficos" do texto quando o arquivo não tem gráfico (decidido na hora de salvar, olhando o próprio arquivo). Só esse texto mudou nesses arquivos |
| CONVENCOES.md (Advogados e Médicos) | — | regra nova "Configuração de preço: um predicado só", com a proibição de guardar só o denominador e de somar linhas suspensas |

## Arquivos cujo conteúdo mudou (fórmulas, dados ou validação), comparados com o pacote final-2

Os outros arquivos mudaram só o valor em cache do recálculo (a proposta 07 dos Advogados muda a data
do dia, uma das três exceções de TODAY()). Comparação feita célula a célula com openpyxl, incluindo
as listas de validação.

| Arquivo | Células ou listas de validação diferentes | Abas |
|---|---:|---|
| 01-essencial/01-semana-organizada.xlsx | 2 | Como usar, Hoje |
| 02-completo/01-semana-organizada.xlsx | 2 | Como usar, Hoje |
| 02-completo/04-projetos-e-prazos.xlsx | 1 | Como usar |
| 02-completo/05-ata-e-pendencias.xlsx | 1 | Como usar |
| 02-completo/06-metas-do-trimestre.xlsx | 1 | Como usar |
| 03-advogados/01-agenda-de-prazos.xlsx | 1 | Como usar |
| 03-advogados/02-andamento-por-processo.xlsx | 1 | Como usar |
| 03-advogados/03-rotina-da-semana.xlsx | 1 | Como usar |
| 03-advogados/04-checklist-abertura-e-encerramento.xlsx | 1 | Como usar |
| 03-advogados/05-custo-hora.xlsx | 18 | Config, Painel, Pessoas |
| 03-advogados/06-simulador-de-honorarios.xlsx | 31 | Config, Simulador |
| 03-advogados/07-proposta-de-honorarios.xlsx | 1 | Como usar |
| 03-advogados/08-tabela-de-referencia.xlsx | 785 | Config, Nossos casos, Referência |
| 03-advogados/11-pro-labore.xlsx | 1 | Como usar |
| 03-advogados/19-metas-do-trimestre.xlsx | 1 | Como usar |
| 03-advogados/20-resumo-do-mes.xlsx | 1 | Como usar |
| 04-medicos/03-rotina-da-semana.xlsx | 1 | Como usar |
| 04-medicos/04-checklist-do-dia.xlsx | 1 | Como usar |
| 04-medicos/05-custo-da-hora.xlsx | 19 | Config, Equipe, Painel |
| 04-medicos/06-precificacao.xlsx | 108 | Config, Precificação |
| 04-medicos/07-simulador-convenio-x-particular.xlsx | 61 | Config, Simulador |
| 04-medicos/08-tabela-de-precos.xlsx | 81 | Config, Tabela |
| 04-medicos/11-repasse-e-pro-labore.xlsx | 1 | Como usar |
| 04-medicos/19-metas-do-trimestre.xlsx | 1 | Como usar |
| 04-medicos/20-resumo-do-mes.xlsx | 1 | Como usar |

## Travas

| Trava | Resultado |
|---|---|
| `recalc_todos.py` | 189.799 fórmulas · 0 erro (+5: as células de conferência da Config) |
| Coerência Essencial / Completo / Advogados / Médicos | 594 / 3.559 / 293 / 702 · 0 falhas |
| `verifica_lancamento.py` | 25 · 0 falhas |
| Inventário | 299 validações (+9: 03/08 B8:B11, 04/07 B6:B7, 04/08 B8:B10) · 483 regras · 0 `_xlfn` · 0 regra sem INDIRECT · 0 literal > 255 · **0 TEXT com data** · **0 entrega ≠ gerado** · 2 listas abertas deliberadas |
| Cenários (`CENARIOS.md`) | 32 cenários em 7 arquivos · 0 com erro de fórmula |

## O que continua pendente e não depende de mim

O roteiro nativo em Excel 2016 e Google Sheets (parte 7 do seu parecer), agora com os três
arquivos a mais no passo 02 de G02.
