# Varredura automática das entradas dos sete arquivos de preço (versão da rodada 7)

O que mudou depois da sua revisão ampliada, ponto a ponto:

- **Sem amostragem.** Antes eram três linhas por coluna, por isso a varredura não chegava ao custo-hora
  do simulador nem às linhas do meio. Agora TODA célula de entrada preenchida do exemplo (desbloqueada
  e sem fórmula) recebe **vazio**, **"abc"** e **−1** (quando numérica), uma por vez, a partir do
  exemplo intacto.
- **Linha nova.** Em cada coluna de tabela, a primeira célula de entrada vazia depois da última
  preenchida recebe **"abc"** e **1**. É o caso da despesa nova sem valor (F6-G03) e do resíduo sem
  nome.
- **NEW.** Além de ERR (erro de fórmula), NUM (número que mudou sem aviso) e CLS (rótulo trocado por
  outro, sem palavra de aviso), a varredura acusa fórmula que estava vazia e **passou a mostrar
  número**.
- **Decisões por saída.** Uma decisão de produto ("branco = não se aplica") não pula mais o cenário
  inteiro. Cada decisão diz, em `SAI` no código da triagem, quais células podem mudar: a margem da
  própria célula, a contagem e o maior prejuízo, o quadro por área. Qualquer outra mudança continua
  sendo triada, e erro de fórmula nunca é pulado.
- **TEXTCOL estreito.** Só as colunas de nome ou descrição livre contam como eco de texto: pessoa,
  papel, nº e cliente do caso, tipo de serviço, nome de etapa ou despesa, descrição de custo fixo,
  nome do procedimento e nome do pagador. Área, modalidade, marcações Sim/Não e listas saíram.

Cada exclusão da triagem está escrita no código (`varredura_triagem.py`), com o motivo.

## Resultado final (arquivos deste pacote)

| Arquivo | Células de entrada testadas | Mutações (vazio, texto, −1, linha nova) | Com erro de fórmula |
|---|---:|---:|---:|
| kit-advogados-05-custo-hora | 51 | 125 | 0 |
| kit-advogados-06-simulador-de-honorarios | 51 | 125 | 0 |
| kit-advogados-08-tabela-de-referencia | 427 | 985 | 0 |
| kit-medicos-05-custo-da-hora | 62 | 146 | 0 |
| kit-medicos-06-precificacao | 78 | 205 | 0 |
| kit-medicos-07-simulador-convenio-x-particular | 65 | 166 | 0 |
| kit-medicos-08-tabela-de-precos | 91 | 242 | 0 |

Total: 1994 mutações.

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

Na primeira passada desta versão, sobre os arquivos já com as correções F6, a varredura achou quatro
defeitos que a versão anterior não via. Todos foram corrigidos no gerador:

1. Custo fixo digitado sem descrição entrava no total sem aviso (05 dos dois kits).
2. As horas de trabalho de uma pessoa com cadastro incompleto entravam no total do Painel (03/05 B20).
3. O Painel mostrava 0 no papel ou na remuneração de uma pessoa nova com o campo vazio (05 dos dois kits).
4. Particular −1 no retorno fazia "valor médio contra o mínimo" mostrar −100 % (04/08 S9).

Limites que continuam: a varredura muda uma entrada por vez (não combina duas) e roda no LibreOffice,
não no Excel nem no Sheets. Os quatro arquivos que não mudaram depois da primeira passada (03/06,
03/08, 04/06, 04/07) foram varridos com o mesmo código, exceto a palavra "sem nome", que só entrou
depois na lista de avisos. A triagem aplica a mesma regra aos resultados deles.
