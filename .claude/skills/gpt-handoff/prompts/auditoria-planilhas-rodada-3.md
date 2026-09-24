Você auditou estas 53 planilhas e encontrou 32 defeitos graves e 25 médios. **Todos os 32
graves foram corrigidos**, e os arquivos deste pacote são a versão corrigida. Esta rodada
tem três tarefas: **provar que cada correção funciona**, **achar o que a correção
estragou**, e **procurar o que ninguém achou ainda**.

Leia `TRIAGEM-COMPLETA.md`, `LEIA-ME.md` e `INVENTARIO.md`. Depois abra os arquivos e
trabalhe neles. Não responda a partir dos documentos.

## Formato do achado

`GRAVIDADE | arquivo | aba!célula | o que está errado | por que quebra para o cliente | como corrigir`

**GRAVE** — número errado, dado perdido, arquivo que não abre, ou instrução que leve a
decisão errada de dinheiro, de prazo legal ou de atendimento.
**MÉDIO** — funciona mas confunde, quebra em borda previsível, ou contradiz outra parte.
**LEVE** — acabamento. "Nada" quando a seção não tiver achado. Sem elogio.

## Parte 1 · Provar as correções, uma por uma

Para cada item, **RESOLVIDO** ou **NÃO RESOLVIDO**, com a evidência: a fórmula que está
lá hoje, a conta que você fez, o número que saiu. Teste as bordas, não só o caso fácil.

**Compatibilidade.** Zero `_xlfn` e zero uso de MINIFS, MAXIFS, TEXTJOIN, IFS, SWITCH,
CONCAT, XLOOKUP, FILTER, SORT, UNIQUE, SEQUENCE por qualquer grafia. E as substituições:
o `SUMPRODUCT(MIN(cond*x+(1-cond)*1E+10))` do "Próximo fim" (02-completo/04) e do
"Próximo prazo" (/05) devolve a mesma data que o MINIFS devolvia? Teste com responsável
sem etapa aberta, com etapa sem data de fim, com etapa concluída — tem de ficar vazio, não
mostrar 1E+10 nem data de 1900. Idem o `SUMPRODUCT(MAX(...))` da /10 e a coluna auxiliar
cumulativa (H11:H30 da aba Resumo da /05), que substituiu o TEXTJOIN: monta o mesmo texto,
sem separador sobrando, e escreve "nenhuma" quando não há pendência?

**Caixa.** Reconstrua o calendário de liquidação de cartão do Kit Médicos a partir da
agenda da 01 e das taxas da 16, e confira contra os lançamentos da 09: débito D+1, crédito
à vista D+30, parcelado uma parcela a cada 30 dias. O saldo do Painel tem de ser
R$ 38.605,81. Confirme que nenhum mês recebe cartão que ainda não venceu, e que a taxa
lançada no fim de cada mês é a das liquidações daquele mês, não das vendas. No
`03-ganhos-e-gastos` dos kits 01 e 02: todos os totais de caixa filtram "Pago? = Sim", e
"A receber" e "A pagar" não duplicam nada.

**Acumulado por indicador.** A coluna "Como acumular" existe, bloqueia fora de
Soma/Média, e o Acumulado obedece. Ticket médio e custo por lead estão em Média. Troque um
para Soma e confirme que o número muda como deveria.

**Simulador de honorários.** A hora mínima do caso inclui as despesas absorvidas e dá
R$ 120,26/h no cenário preenchido. Com hora cobrada de R$ 110, o risco deixa de ser
"Baixo"? Calcule a margem efetiva e diga se o texto do alerta está coerente com ela.

**Devolução de sócio.** Receita de abril do Advogados = R$ 19.760 e imposto = R$ 1.581. A
linha de devolução aparece em algum lugar, fora da receita? O resultado do mês e a margem
batem com a planilha 20?

**Fernanda Castro.** Cronograma soma R$ 7.000, nada a cobrar, e os indicadores de
inadimplência da 14 e a carteira da 13 batem entre si. Rode a mesma verificação nos outros
28 casos: soma do cronograma igual ao contrato no fixo, entre fixo e contratado no misto.

**Trimestre com limite superior.** Nos três arquivos (funil do Completo, funil do
Advogados, orçamentos do Médicos): com referência em 30/06/2026, o total do trimestre
exclui fechamento de julho em diante? E a virada de ano (4º trimestre) funciona?

**Os outros.** Sábado com capacidade na agenda médica; corte de data igual nos dois lados
da ocupação e a 17 mostrando o mesmo número da 01; pessoa fora do cadastro recusada e
custo avisando em vez de zerar; Resumo da base cobrindo 30 cadastros; parcelas recusando
zero com saldo; 4º trimestre fechando; indicador de casos cobrindo 200; base zero na
variação com frase própria; meta zero contada; pontuação de faltas exata (teste com 2 e
com 3 faltas); "Recebido no mês" mudando o repasse de verdade; os três defeitos da
conciliação de cartão; "quatro propostas" virando três.

**Data-base.** Zero `=TODAY()` nas 53. Tudo fecha em 14/09/2026. Diga o que fica estranho
para quem abrir o arquivo em 2027.

**Validações.** 276 de 276 bloqueiam. Alguma virou restritiva demais, impedindo entrada
legítima? Isso seria um defeito que eu criei.

## Parte 2 · O que a correção pode ter estragado

Mexi em `dados.py` dos dois kits, no motor compartilhado e em 53 dos 53 arquivos. Procure:

- Número que mudou onde não devia: compare `referencia/numeros-*.md` com os painéis.
- Texto de instrução descrevendo o comportamento antigo. Varra toda aba "Como usar" e toda
  nota de Config procurando "no dia da venda", "relativo a hoje", "acumulado", "só as abas
  Checklist e Resumo", e qualquer número fixo escrito em texto que não bata com o painel.
- Layout: o quadro novo "A receber (não recebido)" no `03-ganhos-e-gastos` cabe na tela?
  A aba **Meses** nova na 06 do Completo está correta (mês 1 = semanas 1-4, mês 2 = 5-9,
  mês 3 = 10-13) e o LOOKUP(9.99E+307) pega o último valor mesmo com semana em branco no
  meio? As colunas ocultas novas (L em Etapas do Completo/04, K-L-M em Casos do
  Advogados/16, H no Resumo do Completo/05, O em Repasse do Médicos/11) estão realmente
  ocultas, não aparecem na impressão, e não quebraram fórmula que dependia daquela letra?
- O bloco de totais do Resumo da base-limpa mudou de linha 16 para 38: alguma fórmula,
  formatação condicional ou referência ainda aponta para a linha velha?
- O corte `A{r}<=Config!$B$9` na coluna R da agenda médica: alguma outra fórmula do kit
  somava essa coluna esperando o mês inteiro?

## Parte 3 · O que você ainda não olhou

- **Kits 01 e 02** continuam sem arquivo de convenções e sem conferência de coerência
  própria. Trate-os como suspeitos: as três planilhas do 01 contam a mesma história? As
  dez do 02? Vale a pena eu escrever uma conferência de coerência para eles, e o que ela
  deveria checar?
- **Dez fórmulas centrais que a rodada anterior não recalculou à mão.** Escolha, refaça a
  conta com os números do exemplo e mostre o resultado.
- **A discordância registrada.** Eu mantive duas empresas de exemplo nos kits 01 e 02
  (Prisma Comunicação para as planilhas de empresa, Rafa Design para o Ganhos e Gastos,
  que a oferta posiciona também para uso pessoal), tornando a diferença explícita nos dois
  "Como usar". Você tinha pedido uma só. Leia os textos como estão e diga se resolve, ou
  se você mantém que uma empresa única é melhor — e nesse caso qual, e o que fazer com o
  posicionamento de uso pessoal.

## Parte 4 · Veredicto

Para cada um dos quatro kits: você venderia hoje, pelo preço indicado? Sim ou não, motivo
em duas linhas. Se a resposta mudou desde a primeira auditoria, diga o que mudou. Se
continua não, diga exatamente o que ainda falta.

E no fim, atualizado: **o que só um Excel de verdade resolveria**, em ordem de prioridade,
com o teste concreto de cada item.

## Duas regras

Não corrija arquivo nenhum e não devolva planilha alterada: quero o diagnóstico, a
correção eu aplico no código que gera os arquivos.

Se faltar informação para julgar, diga qual falta e julgue com a hipótese explícita, em vez
de pular o item.
