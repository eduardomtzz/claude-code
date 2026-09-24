# O que mudou desde o zip `seu-socio-gestor-auditoria-final-5.zip`

Os dois achados da confirmação 5 (F5-G01 e F5-G02) foram reproduzidos antes de mexer, com os números
do seu parecer; nenhum falso. Além dos contraexemplos do parecer, construí uma **varredura
automática** de todas as entradas dos sete arquivos de preço (`varredura/VARREDURA.md`): 514
mutações (vazio, texto, −1), cada uma recalculada e comparada célula a célula com o exemplo. As
correções abaixo são o que a varredura e o parecer acharam juntos; a varredura final termina com
**zero** erro de fórmula e **zero** número ou rótulo mudado sem aviso fora das decisões de produto
escritas.

## F5-G01 — parâmetro vazio, texto ou negativo usado como número

| Arquivo | Antes | Depois |
|---|---|---|
| 03/05, 04/05 Config!B9 (múltiplo) | vazio → hora arredondada 0; texto → #VALUE! | "falta o múltiplo de arredondamento em Config" em B17 e no cartão G5 (múltiplo > 0) |
| 04/05 Config!B10 (duração da consulta) | vazio → custo do horário vazio 0 | "falta a duração da consulta em Config" (> 0) |
| 03/05, 04/05 sensibilidade B42:B44 e horas realizadas C45 | texto → cinco #VALUE!; −1 → queda de −100 % | "Percentual inválido (0 a 99 %)", linha vazia; horas realizadas > 0 |
| 03/05, 04/05 custos fixos, pró-labore, valor mensal, horas | negativos aceitos (custo-hora 44,64, 56,07, 405,80…) | custo fixo, pró-labore e valor ≥ 0; horas faturáveis/planejadas > 0; senão "cadastro incompleto". Eco da margem no Painel mostra "falta em Config" quando vazia; espelho das horas da pessoa não mostra 0 quando vazia |
| 03/06 bloco 3 (despesas) | B34 vazio com nome e "Não" → despesa sumia (recomendação Hora, margem 5.125,02); C33 vazio → "Não" | linha com qualquer dado exige valor ≥ 0 e "reembolsa?" = Sim/Não; senão "Despesa incompleta (bloco 3)", custo do caso, hora mínima, riscos e recomendação suspensos |
| 03/06 bloco 2 (horas) | B19 = −1 → 48 h e recomendação Misto; etapa com nome e sem horas → somava as outras | toda etapa com dado exige horas ≥ 0; total de horas, custo das horas, receita da Hora e recomendação dizem "horas faltando ou inválidas" |
| 03/06 blocos 2 e 3 | — | validação decimal ≥ 0 nas horas e nos valores de despesa |
| 04/06, 04/08, 04/07 preços, volumes, produção | negativos aceitos (margem +13.156 %, receita/hora 950) | preço particular, tabela de convênio, volume e produção ≥ 0; negativo = "Preço inválido" / "tabela inválida" / "volume ou produção faltando ou negativos", e o resumo conta a linha como incompleta |
| 03/08 casos e faixa | valor, horas e horas típicas negativos aceitos | ≥ 0; senão "valor ou horas inválidos" / "horas inválidas" |

## F5-G02 — agregado que ignora parte da linha incompleta

| Arquivo | Antes | Depois |
|---|---|---|
| 03/08 cartões e quadro por área | G5 "abc": I5 = 157,85 e Empresarial 211,79 (+65,6 %), somando o dinheiro e excluindo as horas; A5 vazio reduzia a "10 de 37" sem aviso | "caso incompleto" = linha com algum dado e sem nº, área cadastrada, valor ≥ 0 ou horas ≥ 0. Cartões E5, G5 e I5 dizem "n caso(s) incompletos (nº, área, valor ou horas)"; na área do caso, total, horas, média, contagem e falta ficam suspensos ("caso incompleto") |
| 04/08 cartão de produção | Q8 vazio com P8 = 130: G5 = 17.901 | "produção incompleta em n linha(s)"; Q8 = 0 digitado continua 17.901 |
| 04/06, 04/08 linha sem nome com dado (resíduo) | apagar só o nome tirava a classificação mas os totais somavam o resto | resíduo conta como linha incompleta em todos os resumos e cartões |
| 04/07 melhor e pior convênio | glosa C11 vazia: "Melhor convênio: MediPlan R$ 129" sem a Saúde Total | "incompleto: n convênio(s) sem líquido" enquanto um convênio com tabela não tiver líquido por hora |
| 04/07 mix | pagador apagado com atendimentos: custo do mês 8.885,33 | "atendimentos inválidos ou sem pagador" no total; a linha diz "pagador sem nome" |

Prazo zero dispensa juros (seu teste: B11 = 0 e B8 vazio → Saúde Total 103,596; o mix acusa os dois
convênios restantes).

## Decisões de produto (branco = "não se aplica"), agora escritas nas convenções

Preço de convênio em branco (06 e 08 dos Médicos): o convênio não atende o procedimento. Valor de
tabela em branco (07): o pagador não atende. Atendimentos em branco no mix (07): sem volume no mês.
Renomear uma área (08 dos Advogados): os casos dela saem da lista e os cartões gerais avisam caso
incompleto; a área de origem de um caso sem área não é conhecida, então só os cartões gerais avisam.

## Arquivos cujo conteúdo mudou, comparados com o pacote final-5

| Arquivo | Células diferentes | Abas | Validação (dv) ou regra de cor (cf) |
|---|---:|---|---|
| 03-advogados/05-custo-hora.xlsx | 57 | Custos fixos, Painel, Pessoas | — |
| 03-advogados/06-simulador-de-honorarios.xlsx | 29 | Simulador | Simulador:dv |
| 03-advogados/08-tabela-de-referencia.xlsx | 403 | Nossos casos, Referência | — |
| 04-medicos/05-custo-da-hora.xlsx | 39 | Custos fixos, Equipe, Painel | — |
| 04-medicos/06-precificacao.xlsx | 78 | Precificação | — |
| 04-medicos/07-simulador-convenio-x-particular.xlsx | 22 | Simulador | — |
| 04-medicos/08-tabela-de-precos.xlsx | 112 | Tabela | — |

Os outros 46 arquivos não mudaram de fórmula, dado, validação ou regra.

## Travas

| Trava | Resultado |
|---|---|
| `recalc_todos.py` | 189.800 fórmulas · 0 erro |
| Coerência Essencial / Completo / Advogados / Médicos | 594 / 3.559 / 293 / 702 · 0 falhas |
| `verifica_lancamento.py` | 25 · 0 falhas |
| Inventário | 308 validações (+2 na 06 dos Advogados) · 483 regras · 0 `_xlfn` · 0 regra sem INDIRECT · 0 literal > 255 · 0 TEXT com data · 0 entrega ≠ gerado |
| Varredura (`varredura/`) | 514 mutações · 0 erro de fórmula · 0 mudança silenciosa fora das decisões |
| Cenários (`CENARIOS.md`) | 98 cenários, das cinco rodadas · 0 com erro de fórmula · exemplo com os mesmos números |
| `HASHES.md` | 53 · 0 diferença |

## Pendente e fora do meu alcance

Roteiro nativo em Excel 2016 e Google Sheets. Durações das aulas medidas por você (zip de 78 MB não
anexável aqui; `DURACOES-AULAS.md` tem ffprobe, tamanho e SHA-256).
