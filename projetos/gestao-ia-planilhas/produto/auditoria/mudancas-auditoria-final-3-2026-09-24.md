# O que mudou desde o zip `seu-socio-gestor-auditoria-final-3.zip`

Os três achados da confirmação 3 (F3-G01, F3-G02, F3-M01) foram reproduzidos antes de mexer, com os
números do seu parecer; nenhum falso. Correção no gerador, sete arquivos regenerados e recalculados
em LibreOffice pt-BR. Também respondi aos três itens que você deixou NÃO TESTADO por falta de
material (durações das aulas, entrega × gerado, validação com texto).

## Graves

| # | Arquivo · célula | Reprodução (antes) | O que mudou | Prova (depois) |
|---|---|---|---|---|
| F3-G01 | 03/06 Config!B9:B12; Simulador!I52:I55, A5, C5, E5, A6 | B9 vazio: I54 Alto → Médio; B10 "abc": I55 Baixo → Alto; B11 "abc": I52 Baixo → Médio; Config!B13 continuava "Sim" | conferência própria das regras de risco em **Config!B14** ("Regras de risco conferem?": B9:B11 numéricos de 0 a 100 %, B12 = Sim ou Não). Cada modalidade só usa a regra que lhe cabe (Fixo: B11; Êxito: B9 e B10; Misto: B10; Hora: nenhuma) e, com ela inválida, diz **"Regra de risco inválida (Config)"** (vermelho), com explicação na coluna K. A recomendação (A5) diz "Corrija as regras de risco em Config" e os KPIs de margem e risco ficam vazios; A6 pede a correção. O IFERROR das classificações não devolve mais "Alto": devolve "Sem base para classificar" | B9 vazio: I54 = "Regra de risco inválida (Config)", A5 = "Corrija as regras de risco em Config", C5 vazio. B10 "abc": I54 e I55 idem. B11 "abc": I52 idem. Exemplo intacto: Baixo · Baixo · Alto · Baixo, recomendação Hora (inalterado) |
| F3-G02 | 03/06 Simulador!I52 (e H/K do Fixo, Êxito e Misto); 03/08 Nossos casos!I, Referência!F por área; 04/07 Simulador!M19:M24; 04/08 Tabela!K5 e S | custo-hora 0 com B45 = 50, B47 = 1.000, B48 = 1 %: Fixo "Alto" por divisão por zero e recomendação Hora (R$ 1.988); 03/08: 43 #DIV/0!; 04/07: 4 #DIV/0!; 04/08: K5 = 0 % por IFERROR | nenhuma classificação divide por valor que pode ser zero legítimo: as desigualdades foram multiplicadas pelo denominador (Fixo: `sobra ≥ custo-hora × horas × (1 + folga)`; Êxito: `(chance − folga) × êxito × valor × (1 − imp) < custo`; Misto idem com o que a entrada não cobre). Textos de ponto de equilíbrio tratam custo-hora zero e êxito zero por extenso. Comparação percentual contra base zero diz **"sem base (mínimo zero)"** (03/08, 04/07, 04/08 K5 e S) | 03/06 no cenário do parecer: Fixo Baixo, recomendação **Fixo, R$ 5.990**; com 0,01: Fixo, R$ 5.989,47 (continuidade). 03/08, 04/07, 04/08 com custo 0: "sem base (mínimo zero)", 0 #DIV/0!. Equivalência das regras reescritas: 600.000 classificações aleatórias com denominadores positivos, 0 divergência contra as fórmulas antigas |

## Médio

| # | Arquivo · célula | Reprodução | O que mudou | Prova |
|---|---|---|---|---|
| F3-M01 | 03/06 Simulador!C11 | B11 "abc" → C11 = #VALUE!; B11 vazio → "No exemplo, R$ 0,0000"; com outro valor, "No exemplo" mostrava o valor do usuário | a nota não formata mais a entrada: é texto fixo com o número do exemplo ("No exemplo, R$ 66,0714 (18.500 ÷ 280 h)") | B11 "abc", vazio ou 0: C11 igual e sem erro |

## Itens que você deixou NÃO TESTADO por falta de material

| Item | O que vai neste pacote |
|---|---|
| Validação customizada devolvia ERRO com texto, não FALSE | as 18 validações customizadas de preço passaram a `IF(ISNUMBER(x);AND(...);FALSE)`: texto dá FALSE. Só a fórmula da validação mudou |
| "Entrega ≠ gerado" sem segunda árvore | `HASHES.md`: etapa 1, SHA-256 do arquivo gerado na pasta do kit, calculado ANTES de montar o pacote; etapa 2, SHA-256 da cópia dentro do pacote, calculado depois da cópia. As duas colunas precisam ser iguais nos 53 |
| Duração das oito aulas | `DURACOES-AULAS.md`: saída literal do ffprobe, tamanho e SHA-256 de cada MP4. Os vídeos vão num zip separado e opcional (`seu-socio-gestor-aulas-completo.zip`), se você quiser medir |

## Arquivos cujo conteúdo mudou, comparados com o pacote final-3

Comparação célula a célula, incluindo listas de validação (dv) e regras de cor (cf). Os outros 46
arquivos não mudaram de fórmula, dado, validação ou regra.

| Arquivo | Células diferentes | Abas | Validação (dv) ou regra de cor (cf) |
|---|---:|---|---|
| 03-advogados/05-custo-hora.xlsx | 0 |  | Config:dv |
| 03-advogados/06-simulador-de-honorarios.xlsx | 19 | Config, Simulador | Config:dv, Simulador:cf |
| 03-advogados/08-tabela-de-referencia.xlsx | 220 | Nossos casos, Referência | Config:dv |
| 04-medicos/05-custo-da-hora.xlsx | 0 |  | Config:dv |
| 04-medicos/06-precificacao.xlsx | 0 |  | Config:dv |
| 04-medicos/07-simulador-convenio-x-particular.xlsx | 6 | Simulador | Config:dv |
| 04-medicos/08-tabela-de-precos.xlsx | 13 | Tabela | Config:dv |

Nas 05 e na 06 dos Médicos só mudou a fórmula das validações (texto dá FALSE). Na 06 dos Advogados
a regra de cor da coluna Risco ganhou os dois avisos novos.

## Travas

| Trava | Resultado |
|---|---|
| `recalc_todos.py` | 189.799 fórmulas · 0 erro (−1 fórmula em C11, +1 em Config!B14) |
| Coerência Essencial / Completo / Advogados / Médicos | 594 / 3.559 / 293 / 702 · 0 falhas |
| `verifica_lancamento.py` | 25 · 0 falhas |
| Inventário | 299 validações · 483 regras · 0 `_xlfn` · 0 regra sem INDIRECT · 0 literal > 255 · 0 TEXT com data · 0 entrega ≠ gerado · 2 listas abertas deliberadas |
| Cenários (`CENARIOS.md`) | 43 cenários em 7 arquivos · 0 com erro de fórmula |

## O que continua pendente e não depende de mim

O roteiro nativo em Excel 2016 e Google Sheets (parte 7 do seu parecer), com os passos 7.3 e 7.4.
