Você auditou estas 53 planilhas em 17/09/2026 e encontrou 32 defeitos graves. Nove foram
corrigidos e os arquivos deste pacote já são a versão corrigida. Esta rodada tem duas
tarefas: **provar que os nove foram realmente resolvidos** e **achar o que ninguém achou
ainda**, incluindo defeito que a própria correção possa ter criado.

Leia `TRIAGEM-DA-RODADA-ANTERIOR.md`, `LEIA-ME.md` e `INVENTARIO.md`. Depois abra os
arquivos e trabalhe neles. Não responda a partir dos documentos.

## Formato do achado

Uma linha por achado, e nada mais:

`GRAVIDADE | arquivo | aba!célula | o que está errado | por que quebra para o cliente | como corrigir`

- **GRAVE** — o cliente vê número errado, perde dado que digitou, ou o arquivo não abre.
  Também é grave instrução que leve a decisão errada de dinheiro, de prazo legal ou de
  atendimento.
- **MÉDIO** — funciona, mas confunde, quebra em borda previsível, ou contradiz outra parte.
- **LEVE** — acabamento.

Sem elogio, sem repetir o enunciado. "Nada" quando a seção não tiver achado.

## Parte 1 · Conferir as nove correções

Para cada item abaixo, diga **RESOLVIDO** ou **NÃO RESOLVIDO** e mostre a evidência: a
fórmula que está lá hoje, a conta que você fez, o número que saiu.

1. **`_xlfn` eliminado.** Varra o XML das 53 planilhas. Confirme zero ocorrência de
   `_xlfn.` e zero uso de MINIFS, MAXIFS, TEXTJOIN, IFS, SWITCH, CONCAT, XLOOKUP, FILTER,
   SORT, UNIQUE e SEQUENCE por qualquer grafia. Depois avalie as **substituições**: o
   `SUMPRODUCT(MIN(cond*x+(1-cond)*1E+10))` do "Próximo fim" em `02-completo/04` e do
   "Próximo prazo" em `/05` devolve a mesma data que o MINIFS devolvia? Teste com
   responsável sem nenhuma etapa aberta, com etapa sem data de fim, e com etapa concluída
   — a célula tem de ficar vazia, não mostrar 1E+10 nem uma data de 1900. Faça o mesmo com
   o `SUMPRODUCT(MAX(...))` de `/10`. E a coluna auxiliar cumulativa oculta (H11:H30 da
   aba Resumo de `/05`) monta o mesmo texto que o TEXTJOIN montava, sem separador sobrando
   no fim e escrevendo "nenhuma" quando não há pendência?
2. **`02-completo/10-base-limpa.xlsx` protegido.** Todas as abas protegidas, as 9.000
   células amarelas de Base ainda editáveis, as 4.000 fórmulas de J, L e M bloqueadas.
3. **Cartão no caixa do Kit Médicos.** Reconstrua o calendário de liquidação por conta
   própria a partir da agenda da 01 e das taxas da 16 e confira contra os lançamentos da 09:
   débito em D+1, crédito à vista em D+30, parcelado uma parcela a cada 30 dias. O saldo
   do Painel tem de ser R$ 38.605,81. Confirme que **nenhum** mês recebe cartão que ainda
   não venceu, e que a taxa lançada no fim de cada mês é a das liquidações daquele mês, não
   das vendas.
4. **"Pago?" no `03-ganhos-e-gastos`** dos kits 01 e 02: "Entrou no mês", "Saiu no mês",
   "Sobrou", "Saldo em caixa" e a tabela mensal filtram Pago? = Sim. "A receber" e "A pagar"
   mostram o não pago. Nada de dupla contagem entre os quadros.
5. **Sábado na agenda médica.** `04-medicos/01`, Config G20:G43: o INDEX/MATCH cobre
   I45:J50. Monte um turno de sábado e confirme que a capacidade deixa de ser zero.
6. **Corte de data da ocupação.** Capacidade e horas atendidas usam o mesmo Config!B9, que
   é ontem. Confirme que o dia em andamento fica fora dos dois lados, e que a 17 mostra o
   mesmo número da 01.
7. **Instrução do custo-hora** em `03-advogados/05`: manda levar o custo-hora do Painel
   B13, não a hora mínima. Confira se as planilhas 06 e 08 realmente pedem custo-hora.
8. **Instrução de prazo** em `03-advogados/01` e `/03`: prazo processual não se reagenda na
   planilha. Diga se o texto está claro o suficiente para um advogado não interpretar errado.
9. **Data-base congelada.** Zero `=TODAY()` nas 53 planilhas. O exemplo todo fecha em
   14/09/2026, e o "Como usar" explica a troca por `=HOJE()`. Diga o que ainda parece
   estranho para quem abrir o arquivo em 2027.

## Parte 2 · O que a correção pode ter estragado

As correções mexeram em `dados.py`, no motor compartilhado e em 33 dos 53 arquivos.
Procure especificamente:

- Número que mudou onde não devia. Compare `referencia/numeros-*.md` com os painéis.
- Texto de instrução que ficou descrevendo o comportamento antigo. Varra toda aba
  "Como usar" e toda nota de Config em busca de "no dia da venda", "relativo a hoje",
  "acumulado" e de qualquer número fixo escrito no texto que não bata com o painel.
- O quadro novo "A receber (não recebido)" no `03-ganhos-e-gastos`: cabe na tela? Sobrepõe
  algo? A formatação condicional ao lado ainda cobre o intervalo certo?
- A coluna auxiliar H do Resumo de `02-completo/05`: está oculta de verdade? Aparece na
  impressão? Estraga alguma fórmula que dependia de H?
- O corte `A{r}<=Config!$B$9` na coluna R da agenda médica: alguma outra fórmula do kit
  somava essa coluna esperando o mês inteiro?

## Parte 3 · Os 23 graves que ficaram

`TRIAGEM-DA-RODADA-ANTERIOR.md` lista o que não foi corrigido. Não repita o diagnóstico:
**ordene por dano ao cliente** e diga quais quatro você corrigiria primeiro, com o motivo
em uma linha cada. Se algum deles você reavaliou e hoje considera menos grave, diga.

## Parte 4 · O que você ainda não olhou

Duas frentes que a primeira rodada cobriu por amostragem:

- **Kits 01 e 02** não têm arquivo de convenções nem conferência de coerência própria.
  Trate-os como suspeitos: as três planilhas do 01 contam a mesma história? As dez do 02?
- **Fórmula que calcula liso e devolve número errado.** Escolha dez fórmulas centrais que
  a primeira rodada não recalculou à mão, refaça a conta com os números do exemplo e mostre
  o resultado.

## Parte 5 · Veredicto

Para cada um dos quatro kits: você venderia hoje, pelo preço indicado? Sim ou não, motivo
em duas linhas. Se a resposta mudou desde a primeira auditoria, diga o que mudou.

E no fim: **o que só um Excel de verdade resolveria**, atualizado. A ordem 1 do seu roteiro
anterior era abrir os três arquivos com `_xlfn` no Excel 2016 para descobrir o defeito;
agora serve para confirmar a correção. Reescreva o roteiro com isso em mente.

## Duas regras

Não corrija arquivo nenhum e não devolva planilha alterada: quero o diagnóstico, a
correção eu aplico no código que gera os arquivos.

Se faltar informação para julgar, diga qual falta e julgue com a hipótese explícita, em vez
de pular o item.
