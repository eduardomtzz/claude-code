# O que mudou desde o zip `seu-socio-gestor-auditoria-final-7.zip`

Os dois achados da confirmação 7 foram reproduzidos antes de mexer, com os números do seu parecer.
Nenhum é falso:
- F7-G01: I5 = 0 + L5 = 0 dava T5 = 0, E25 = 13 e E26 = 60,43; H8 = 0 + I8 = 0 dava O8 = 2 e E5 = 13.
- F7-M01: E5 = 10 e F5 = 110 dava G5 = 11, K5 = 0 e A6 vazio.

Cada contraexemplo está em `CENARIOS.md` (prefixo F7-).

## Grave

| Achado | Antes | Depois |
|---|---|---|
| F7-G01 (continuação de F6-G04) · 04/06 e 04/08 | a exceção valia para qualquer linha com particular 0 e convênio 0 | a exceção vale só para a linha identificada como Retorno: o procedimento chamado "Retorno", cujo tempo já está no custo da consulta pela Config (retornos por consulta e duração). Consulta com I5 = 0 e L5 = 0 dá T5 = −130,67, E25 = 14 e E26 = 130,67. Com H8 = 0 e I8 = 0: O8 = 3 e E5 = 14. Renomear a linha do Retorno tira a exceção: E25 = 17, O9 = 3, E5 = 17. A cor usa o mesmo predicado: na 04/08 o vermelho da tabela, na 04/06 uma regra nova em vermelho na tabela 0 que conta |

## Médio

| Achado | Antes | Depois |
|---|---|---|
| F7-M01 · 03/05 Pessoas | E5 = 10 e F5 = 110 publicava ocupação de 1.100 %, sem aviso | faturáveis > trabalho (as duas numéricas) é pendência: G5 = "faturáveis > trabalho", H5 = "faturáveis acima das horas de trabalho", K5 = 1, e A6 avisa com o custo-hora em "cadastro incompleto". E5 = F5 = 110 dá 100 %, sem aviso; E5 = 160 dá 68,75 % |

## Precisão do apêndice I (sem gravidade)

As duas regras de cor de Tabela!I8:M19 (04/08) passaram a ser
`IF(AND(ISNUMBER(preço), ISNUMBER(custo), ISNUMBER(mínimo)), teste, FALSE)`. Não avaliam mais a
multiplicação de texto.

## Expectativa corrigida (F6-G05)

Você tem razão sobre B19 = −1: C31 = 4, D31 = 334,20 e F31 = 1 são valores por atendimento que não
usam minutos, e ficam. Minutos inválidos suspendem só as medidas por hora e o custo cheio. O prompt
desta rodada não pede mais que C31:G36 fique vazio com minutos inválidos.

## Arquivos cujo conteúdo mudou, comparados com o pacote final-7

| Arquivo | Células diferentes | Abas | Validação (dv) ou regra de cor (cf) |
|---|---:|---|---|
| 03-advogados/05-custo-hora.xlsx | 31 | Painel, Pessoas | — |
| 04-medicos/06-precificacao.xlsx | 49 | Precificação | Precificação:cf |
| 04-medicos/08-tabela-de-precos.xlsx | 13 | Tabela | Tabela:cf |

Os outros 50 arquivos não mudaram de fórmula, dado, validação ou regra. Os números do exemplo são os
mesmos. Só as notas 04/06 A19 e 04/08 A21 mudaram de texto: a regra do convênio 0 agora cita a linha
chamada Retorno.

## Travas

| Trava | Resultado |
|---|---|
| `recalc_todos.py` | 189.800 fórmulas · 0 erro |
| Coerência Essencial / Completo / Advogados / Médicos | 594 / 3.559 / 293 / 702 · 0 falhas |
| `verifica_lancamento.py` | 0 falhas (pendências externas: link de checkout dos Médicos e ID do Pixel) |
| Inventário | 313 validações · 487 regras (+4: tabela 0 que conta, na 04/06) · 0 TEXT com data · 0 entrega ≠ gerado |
| Varredura (`varredura/`) | 2.670 mutações (agora com zero e ×10) · 0 erro de fórmula · 0 regra de negócio violada · 0 mudança silenciosa fora das decisões |
| Cenários (`CENARIOS.md`) | 134 cenários das sete rodadas · 0 com erro de fórmula |
| `HASHES.md` | 53 · 0 diferença |

## Pendente e fora do meu alcance

Roteiro nativo em Excel 2016 e Google Sheets. As durações das aulas precisam ser medidas por você: o
zip de 78 MB não pode ser anexado aqui, e `DURACOES-AULAS.md` traz ffprobe, tamanho e SHA-256.
