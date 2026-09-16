# Controle da Casa

Pipeline que lê o controle de pagamentos mensais de uma casa — uma planilha com
uma aba por mês, mais o controle que se escreve no celular em texto corrido — e
produz um painel único: categorias, custo por pessoa, o que é fixo, o que é
parcela, o que mudou de patamar e onde há espaço de negociação.

Sem dependências: só a biblioteca padrão do Python 3.11. O leitor de `.xlsx` é
próprio, porque um `.xlsx` é um zip de XML e isso dispensa pandas e openpyxl.

## Uso

```bash
python3 -m financas.cli planilha.xlsx --texto dados/setembro-2026.txt
```

Isso grava três arquivos em `dados/`:

| arquivo | o que é |
|---|---|
| `painel.html` | o painel, autocontido, abre no navegador sem servidor |
| `lancamentos.csv` | a base categorizada, uma linha por pagamento |
| `painel.json` | o mesmo conteúdo do painel em dados, para outras análises |

O nome do arquivo de texto define a competência: `setembro-2026.txt` ou
`2026-09.txt`. Pode repetir `--texto` para vários meses.

## Dados pessoais

**Os dados da casa não entram no repositório.** A pasta `dados/` está no
`.gitignore`. Este repositório é um fork público; os valores, os nomes e os
salários são de pessoas reais.

Além disso, o parser **descarta** chaves PIX, CPF, CNPJ, telefones e linhas
digitáveis de boleto na leitura (`modelo.redigir`). Eles não chegam ao CSV, ao
JSON nem ao HTML, mesmo que estejam no texto de entrada.

## Como funciona

```
planilha .xlsx ─┐
                ├─► lançamento normalizado ─► classificação ─► séries ─► painel
controle .txt ──┘                                              │
                                                               └─► oportunidades
```

| módulo | responsabilidade |
|---|---|
| `xlsx.py` | lê `.xlsx` sem dependências |
| `modelo.py` | o lançamento canônico, redação de dados pessoais, parcelas |
| `planilha.py` | abas mensais → lançamentos; deduz o ano pela ordem das abas |
| `texto.py` | controle em texto → lançamentos; e a conciliação entre os dois |
| `regras.py` | taxonomia e regras de categoria, subcategoria e pessoa |
| `analise.py` | séries mensais, fixo/variável/parcelado, oportunidades |
| `consolidacao.py` | junta as duas fontes sem contar o mesmo pagamento duas vezes |
| `painel.py` | monta o payload e injeta no template |

### Decisões que valem saber

**Competência, não data de pagamento.** Um salário pago em 30/ago pertence a
setembro. A aba manda; a data da linha é só informação.

**A planilha é a fonte principal.** Quando o mês aparece nos dois controles, do
texto entram apenas os itens que faltam na planilha — e a diferença aparece na
conciliação em vez de sumir na soma.

**Séries são agrupadas pela classificação, não pelo texto.** "Akuguel e IPTU",
"Aluguel e IPTU" e "Aluguel / IPTU" são o mesmo aluguel escrito de três jeitos.
Agrupar por descrição transformaria um gasto fixo em três avulsos.

**Totais da planilha são recalculados.** Várias abas guardam um total de fórmula
desatualizado. O parser identifica a linha de total pela ordem de grandeza e a
descarta, somando os lançamentos de novo.

**A janela é de seis meses fechados.** O mês corrente fica de fora das médias
porque ainda está incompleto; o mês futuro é marcado como previsão.

## Testes

```bash
python3 -m unittest discover -s testes
```

Os testes usam dados sintéticos. Nenhum número real da casa está versionado.
