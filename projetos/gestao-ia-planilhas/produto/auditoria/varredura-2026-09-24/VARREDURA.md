# Varredura automática das entradas dos sete arquivos de preço

Por que existe: as rodadas 3 a 5 acharam, uma de cada vez, entradas vazias ou em texto tratadas
como zero e agregados que ignoravam a linha incompleta. Em vez de esperar o próximo contraexemplo,
cada célula de entrada preenchida do exemplo (desbloqueada, sem fórmula; nas tabelas longas, a
primeira, a do meio e a última linha de cada coluna) recebe três mutações, uma por vez, a partir
do exemplo intacto: **vazio**, **"abc"** e **−1** (quando numérica). Cada cópia é recalculada no
LibreOffice pt-BR e TODAS as fórmulas do arquivo são comparadas com o exemplo:

- **ERR**: célula com erro de fórmula;
- **NUM**: número que mudou de valor (a entrada inválida produziu outro número em vez de aviso);
- **CLS**: rótulo que virou outro rótulo (por exemplo "Baixo" → "Médio") sem palavra de aviso.

`varredura_triagem.py` separa o que não é defeito, e cada exclusão está escrita no código:
colunas auxiliares ocultas (flag da pessoa, prejuízo auxiliar, pontuação), predicados da Config
que viram "Não", eco da entrada (margem mostrada no Painel, horas da pessoa, lista dos 8 casos que
se reordena) e as decisões de produto em que branco significa "não se aplica" (convenções,
seção "Domínio, resíduo e decisões de em branco").

## Resultado final (arquivos deste pacote)

| Arquivo | Células de entrada testadas | Mutações (vazio, texto, −1) | Com erro de fórmula |
|---|---:|---:|---:|
| kit-advogados-05-custo-hora | 31 | 79 | 0 |
| kit-advogados-06-simulador-de-honorarios | 15 | 33 | 0 |
| kit-advogados-08-tabela-de-referencia | 48 | 110 | 0 |
| kit-medicos-05-custo-da-hora | 35 | 85 | 0 |
| kit-medicos-06-precificacao | 27 | 73 | 0 |
| kit-medicos-07-simulador-convenio-x-particular | 17 | 43 | 0 |
| kit-medicos-08-tabela-de-precos | 33 | 91 | 0 |

Total: 514 mutações.

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

Antes das correções desta rodada, a mesma varredura sobre o pacote final-5 marcava 10 mutações com
erro de fórmula e centenas de números mudados sem aviso (custo fixo e pró-labore negativos, horas
negativas, múltiplo de arredondamento vazio, preço negativo, produção vazia, resíduos de linha sem
nome, entre outros). Os resultados brutos por arquivo estão nos `.json` desta pasta.

Limites: a varredura muda uma entrada por vez (não combina duas), testa três linhas por coluna nas
tabelas longas e roda no LibreOffice, não no Excel nem no Sheets.
