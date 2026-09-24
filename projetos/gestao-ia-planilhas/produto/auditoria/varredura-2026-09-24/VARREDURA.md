# Varredura automática das entradas dos sete arquivos de preço (versão da rodada 8)

Base: a versão da rodada 7 (todas as entradas preenchidas, linha nova, NEW, decisões limitadas por
saída, TEXTCOL estreito). O que entrou por causa do seu parecer final-7:

- **Zero e ×10.** Cada entrada numérica recebe também **0** (quando o exemplo não é zero) e o **valor
  ×10**. São dados válidos, que podem ser incoerentes com outro campo: F7-M01 era 110 faturáveis
  contra 10 de trabalho, F7-G01 eram dois zeros. Nesses dois modos a mudança de número é esperada, por
  isso só contam ERR e INV.
- **INV: regras de negócio conferidas fora da planilha, em TODO modo.** Não dependem de a célula
  mudar, o que fecha o ponto cego "resultado indevido que fica igual ao exemplo":
  - 03/05: ocupação ≤ 100 % em cada pessoa;
  - 03/08: mínimo ≤ máximo em cada faixa;
  - 04/06: prejuízo auxiliar de cada tabela de convênio recalculado em Python como
    MIN(0, preço × (1 − imposto) − custo cheio), zero só na linha Retorno com tabela 0; e mínimo ≤ alvo;
  - 04/08: quantidade de tabelas abaixo do custo recalculada por linha; e mínimo ≤ alvo.
- **Cor.** As regras de cor da 04/08 que multiplicavam o preço agora são IF(ISNUMBER(...), teste,
  FALSE), como no seu apêndice I. A varredura continua sem avaliar predicados de cor.

## Resultado final (arquivos deste pacote)

| Arquivo | Células de entrada testadas | Mutações (vazio, texto, −1, zero, ×10, linha nova) | Com regra violada | Com erro de fórmula |
|---|---:|---:|---:|---:|
| kit-advogados-05-custo-hora | 51 | 171 | 0 | 0 |
| kit-advogados-06-simulador-de-honorarios | 51 | 170 | 0 | 0 |
| kit-advogados-08-tabela-de-referencia | 427 | 1247 | 0 | 0 |
| kit-medicos-05-custo-da-hora | 62 | 190 | 0 | 0 |
| kit-medicos-06-precificacao | 78 | 299 | 0 | 0 |
| kit-medicos-07-simulador-convenio-x-particular | 65 | 236 | 0 | 0 |
| kit-medicos-08-tabela-de-precos | 91 | 357 | 0 | 0 |

Total: 2670 mutações.

```
== 05-custo-hora: 0 caso(s) a triar

== 06-simulador-de-honorarios: 0 caso(s) a triar

== 08-tabela-de-referencia: 0 caso(s) a triar

== 05-custo-da-hora: 0 caso(s) a triar

== 06-precificacao: 0 caso(s) a triar

== 07-simulador-convenio-x-particular: 0 caso(s) a triar

== 08-tabela-de-precos: 0 caso(s) a triar

TOTAL a triar: 0
```

A única dispensa nova é renomear a linha do Retorno (04/06 A6, 04/08 A9). Com isso a exceção sai e a
tabela 0 dela passa a contar, que é o comportamento pedido. A dispensa está limitada às saídas E25/E26
e O9/E5.

Limites que continuam:
- uma entrada por vez; as combinações ficam nos cenários nomeados;
- a primeira linha vazia é a seguinte à última preenchida de cada coluna;
- só existem as invariantes listadas acima;
- predicados de cor e validação não são avaliados;
- tudo roda no LibreOffice, não no Excel nem no Sheets.
