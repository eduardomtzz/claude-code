Você vai auditar 53 planilhas de um produto digital que está a dias de ir à venda
no Brasil. Elas ainda não foram abertas em nenhum Excel real: toda a validação até
agora foi feita com LibreOffice e openpyxl. Você é a segunda leitura independente.

Leia `LEIA-ME.md` e `INVENTARIO.md` antes de começar. As regras obrigatórias de
construção estão em `referencia/convencoes-*.md`, o que cada kit promete ao cliente
em `referencia/oferta-*.md`, e os números corretos do exemplo em
`referencia/numeros-*.md`. Atenção: os kits 01 e 02 **não têm** arquivo de
convenções nem de números — infira a regra pelos kits 03 e 04 e aponte onde os
dois primeiros divergem.

Abra os arquivos e trabalhe neles de verdade. Não responda a partir do LEIA-ME.

## Como quero o achado

Uma linha por achado, nesta forma, e nada mais:

`GRAVIDADE | arquivo | aba!célula | o que está errado | por que quebra para o cliente | como corrigir`

Gravidade em três níveis, e seja duro no critério:

- **GRAVE** — o cliente vê número errado, perde dado que digitou, ou o arquivo
  não abre. Também é grave: instrução que leve a decisão errada de dinheiro, de
  prazo legal ou de atendimento.
- **MÉDIO** — funciona, mas confunde, quebra em caso de borda previsível, ou
  contradiz outra parte do produto.
- **LEVE** — acabamento: rótulo, largura de coluna, texto.

Se não houver achado numa seção, escreva "nada" e siga. Não encha de elogio.
Não repita o enunciado de volta.

## O que conferir, em ordem de prioridade

**1. Lógica de fórmula, com olhos novos.** O recálculo já garante que nenhuma dá
erro. O que eu preciso é o oposto: fórmula que calcula liso e entrega número
errado. Procure intervalo que começa ou termina uma linha fora, `MATCH` sem o
terceiro argumento, `SUMIFS` com critério que nunca casa, `$` que falta ou sobra
ao arrastar, denominador que pode ser zero sem guarda, e soma que inclui a própria
linha de total. Escolha ao menos dez fórmulas centrais (painel, resultado,
provisão, custo da hora, honorário) e **recalcule na mão, com os números do
exemplo**, comparando com `numeros-*.md`. Mostre a conta.

**2. Compatibilidade real com Excel 2016 e Google Planilhas.** Liste toda função
usada nos 53 arquivos. Aponte qualquer uma que não exista no Excel 2016 ou no
Google Planilhas, qualquer nome escrito com prefixo `_xlfn.` no XML, qualquer
fórmula de matriz que dependa de derrame (spill), e qualquer referência externa a
outro arquivo. A regra é: nada além de Excel 2007.

**3. O que o cliente pode digitar e o que não pode.** Para cada arquivo: as
células amarelas estão desbloqueadas? Existe célula desbloqueada que não é amarela
(fora de mescla cuja âncora é amarela)? Existe célula amarela que contém fórmula,
ou seja, que promete entrada e na verdade é cálculo? A proteção de aba está
ligada? Diga se dá para o cliente destruir uma fórmula sem perceber.

**4. Listas suspensas e validação.** Abra as 274 validações. Cada lista aponta
para um intervalo que existe? O intervalo tem célula vazia no meio, que corta a
lista? A validação permite valor fora da lista? Tem lista apontando para outra
aba de um jeito que o Google Planilhas não aceita?

**5. Formatação condicional.** Liste as regras de cada arquivo. Alguma usa recurso
que o Google Planilhas ignora? Alguma tem intervalo que não cobre a tabela toda,
ou que cobre linhas vazias e pinta o que não devia? Semáforo de prazo e de meta
estão com o sinal certo (vermelho quando é ruim, e para despesa "acima da meta"
é ruim, não bom)?

**6. Coerência do exemplo entre arquivos.** Nos kits 03 e 04 o mesmo exemplo
atravessa 20 arquivos. Confira contra `numeros-*.md`: o mesmo valor, o mesmo nome
de pessoa, o mesmo mês aparecem iguais em todos os lugares? Nos kits 01 e 02 não
há esse documento: verifique se as três planilhas do 01 contam a mesma história,
e se as dez do 02 também. **Um mês diferente, um nome diferente ou um total que
não fecha entre arquivos é GRAVE**: destrói a confiança no produto inteiro.

**7. Formato e locale.** Todo valor em dinheiro está com formato de moeda e não
como texto? Data é data de verdade, não texto? Percentual é fração formatada, e
não número inteiro com sinal de porcentagem colado? Hora é valor de tempo? Algum
número aparece embutido em texto de um jeito que saia em formato americano
(`131,200.00`) quando o Excel estiver em português?

**8. Datas relativas.** O exemplo usa `=TODAY()+n` onde precisa parecer atual.
Isso funciona hoje. Diga o que quebra ou fica estranho se o cliente abrir o
arquivo em três meses, ou em 2027: vencimento que virou passado, agenda vazia,
meta de trimestre fora de contexto, "mês anterior" apontando para nada.

**9. O texto que o cliente lê.** Cada arquivo tem uma aba "Como usar". Ela está
correta para aquele arquivo, ou é texto genérico copiado? As instruções batem com
o que a planilha realmente faz? Tem algum texto que **promete resultado** ("vai
aumentar", "garante", "lota a agenda"), que dê **conselho jurídico, contábil ou
clínico**, ou que condicione atendimento a pagamento? Isso é GRAVE: viola
política de anúncio e o Código de Defesa do Consumidor brasileiro.

**10. A promessa contra a entrega.** Leia `referencia/oferta-*.md`. Cada coisa
prometida existe nos arquivos, com a contagem certa? Tem planilha entregue que
não aparece na oferta, ou prometida e ausente?

## Três coisas que eu quero explicitamente

**A. O seu veredicto por kit.** Para cada um dos quatro: você venderia este kit
pelo preço indicado, hoje, do jeito que está? Sim ou não, e o motivo em duas
linhas. Os kits 01 e 02 são os mais antigos e os primeiros a receber anúncio —
olhe os dois com desconfiança extra.

**B. A pior coisa que você achou.** Uma só, com o caminho até ela.

**C. O que só um Excel de verdade resolveria.** Se a sua auditoria também foi por
biblioteca, e não abrindo no Excel, diga a lista exata do que ficou sem
verificação e o que eu deveria abrir à mão, em que ordem, para fechar o risco no
menor tempo. Não finja cobertura que você não teve.

## Duas regras sobre você

Não corrija arquivo nenhum e não me devolva planilha alterada: quero o
diagnóstico, a correção eu aplico no código que gera os arquivos.

Se em algum ponto faltar informação para julgar, diga qual falta e julgue com a
hipótese explícita, em vez de pular o item.
