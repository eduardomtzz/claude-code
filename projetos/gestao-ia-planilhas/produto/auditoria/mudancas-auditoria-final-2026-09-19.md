# O que mudou desde o zip `seu-socio-gestor-auditoria-final.zip`

Nove achados do parecer final, todos reproduzidos antes de mexer; nenhum falso. Toda correção foi no
gerador; os 53 arquivos foram regenerados e recalculados em LibreOffice pt-BR. Ao corrigir, achei mais
um por conta própria (o último item da tabela).

## Graves

| # | Arquivo · célula | O que mudou | Prova |
|---|---|---|---|
| G01 | 03/05 Pessoas!H:J; 03/06 Simulador; 04/05 Equipe!H:J; 04/06 Precificação | custo obrigatório em branco não é zero. A linha escreve o que falta ("falta o pró-labore", "faltam as horas faturáveis / planejadas", "falta o custo-hora"); uma coluna oculta K marca a pessoa incompleta e o Painel suspende custo do mês, custo-hora, hora mínima e a sensibilidade com **"cadastro incompleto"**, com aviso contado (A6 na 03/05, A3 na 04/05). No simulador, custo do caso, margem, ponto de equilíbrio, risco e recomendação ficam suspensos ("Falta o custo-hora"); na precificação, custo cheio, preços, margem e situação idem | 03/05 C5 vazio: H5 "falta o pró-labore", B11/B13/B16/B17 "cadastro incompleto", sensibilidade vazia. 04/05 D5 vazio: idem, B21 idem. 03/06 B11 vazio: B15 "Falta o custo-hora (B11)", risco "Falta o custo-hora" nas quatro modalidades, margens vazias, A5 "Preencha o custo-hora primeiro". 04/06 B7 vazio: F5/G5 "falta o custo-hora em Config", K5 "Falta o custo-hora", simulação "Falta o custo-hora em Config". Zero digitado onde zero é legítimo continua zero (E = Sim na 05 dos Médicos) |
| G02 | Config das mesmas quatro | validação customizada em imposto e margens: 0 ≤ % < 100 e imposto + margem < 100 % (na 04/06, mínima ≤ alvo ≤ 99 %); e guarda nas fórmulas, para colagem: qualquer hora mínima, preço ou risco vira **"margens inválidas (Config)"** em vez de número negativo | 03/05 B7 = 95 %: J5, B16, B17 "margens inválidas (Config)". 04/05 B7 = 90 %: idem. 03/06 B8 = 95 %: B15 "Margens inválidas (Config)", risco "Margens inválidas" ×4, A5 "Corrija as margens em Config". 04/06 B9 = B10 = 90 %: G5 "margens inválidas (Config)", K5 "Margens inválidas", simulação "Margens inválidas em Config" |
| G03 | 03/04 Checklist!O40 | o exemplo (dados.py) deixa de marcar "Última parcela cobrada e recebida" = Não para Fernanda Castro, quitada na 13 e na 14; fica só a avaliação do cliente pendente. O verificador ganhou a conferência 04 × 14: caso encerrado e quitado → item Sim | O40 = Sim; Painel "encerrados com pendência" = 3; 13 e 14 inalteradas |
| G04 | 04/13 Guias!N | chave inteira em centavos, como as outras cinco (regra A): `MIN(ROUND(valor×100;0);99.999.999)×1E+4 + (última+1−ROW())` | GUIA-380 (linha 5) N = 380.001.500; GUIA-37999 (linha 1005) N = 379.990.500; lista de glosas: GUIA-380, GUIA-37999 |
| G05 | 03/07 Proposta E24, E26, C32:C43, C44:C45 | entrada e parcela-base arredondadas ao centavo; a última parcela fecha a diferença; total e "Confere" somam o que será cobrado; o verificador confere total e centavos | B25 = 7: 1.800 + 6 × 385,71 + 385,74 = 4.500,00; "Confere com o valor da proposta? Sim" |
| G06 | 04/01 Pacientes!I; 02/04 Etapas!G:H e Painel | o próximo agendamento exige data > 0; etapa sem fim previsto vira **"Falta o prazo"** (cinza), dias vazio, fora de "Atrasada" e "Vence em breve", contada em aviso no Painel A6 | Ana Costa com linha 3004 sem data: I5 = 16/09/2026. Etapa 304 sem prazo e 0 %: G = "Falta o prazo", H vazio, Painel atrasadas = 2, A6 "Atenção: 1 etapa(s) sem fim previsto" |

## Médios e leve

| # | Arquivo | O que mudou | Prova |
|---|---|---|---|
| M01 | referencia/numeros-03-advogados.md | a f-string que faltava; "a receber dos encerrados" lido da 13; observação do escritório lida da célula A6 da 20 | sem `{brl(`; "A receber dos encerrados: R$ 0 (todos os casos encerrados estão quitados…)"; observação igual à 20 |
| M02 | referencia/oferta-02/03/04 | Completo: 8 aulas de 2 a 3 min e a tabela com as durações reais (2:00 a 2:56); Advogados: "Excel 2016 ou mais novo (inclusive Microsoft 365)" e "exemplo congelado em 14/09/2026; só a proposta 07 e o registro usam a data do dia"; Médicos: "horas de atendimento planejadas" e exemplo congelado. A FAQ do site do Completo, que ainda citava Excel 2019 e três funções que saíram, foi corrigida | textos |
| L01 | 20 fórmulas em 13 geradores | nenhum TEXT com código de data: `TEXT(DAY(x);"00")&"/"&TEXT(MONTH(x);"00")&"/"&YEAR(x)` e chave `YEAR(x)&"-"&TEXT(MONTH(x);"00")`; TEXT só com código de dígito ("0", "00", "000", "0%"). Regra B reescrita nos quatro kits, com o motivo: o Excel em português espera "aaaa", e "yyyy" nunca foi provado lá | 0 códigos de data nos 53; "painel de 14/09/2026", "prazo: 15/09"; chaves de Guias e Lotes iguais ("2026-08") |
| meu | 02/09 Painel!A7; 04/12 Config!D13; 04/05 Painel | ao corrigir, varri os 53 por texto literal de fórmula acima de 255 caracteres, limite do Excel que o LibreOffice não acusa: havia dois (350 e 339/278), e a nota nova da 05 dos Médicos caiu na mesma borda (#VALUE!). Textos partidos com `&`; o inventário ganhou a coluna "Literal > 255" | 0 literais acima de 255 nos 53 |

## Travas, todas verdes

| Trava | Resultado |
|---|---|
| `recalc_todos.py` | 189.794 fórmulas · 0 erro |
| Coerência Essencial / Completo / Advogados / Médicos | 594 / 3.559 / 293 / 702 · 0 falhas |
| `verifica_lancamento.py` | 25 · 0 falhas |
| Inventário | 0 `_xlfn`, 0 regra condicional direta, 0 célula solta, 0 literal > 255; 2 listas abertas deliberadas |

## O que continua pendente e não depende de mim

O roteiro nativo da parte 8 do seu parecer final, em Excel 2016 e Google Sheets.
