# Biblioteca de prompts do escritório · Kit de Gestão para Advogados

Versão 1.0 · setembro de 2026 · Seu Sócio Gestor

40 prompts em 5 grupos, um para cada núcleo do kit. Cada um tem: quando usar, de qual planilha
vem o bloco a colar, o prompt pronto (troque o que está entre colchetes), um exemplo com o
escritório fictício e o que conferir na resposta. Funcionam no ChatGPT, no Copilot, no Gemini e
no Claude, inclusive nas versões gratuitas.

## Regra de ouro: o que nunca entra em uma IA pública

**Nunca cole nome real de cliente, número de processo real, CPF, CNPJ, telefone, endereço,
valor de causa identificável ou qualquer trecho de peça, contrato, documento ou conversa com
o cliente.** O sigilo profissional é seu; a IA pública não tem dever de sigilo nenhum e pode
guardar o que recebe. Antes de colar, troque por "Cliente A", "Cliente B", "Processo 1",
"Processo 2". Na prática: copie o bloco da planilha para um texto, troque a coluna Cliente por
letras (A, B, C, na ordem em que aparecem), apague a coluna do número do processo e leia uma vez
procurando nome próprio antes de colar.

Mais três regras:

1. **Nenhum prompt aqui produz petição, tese, parecer, cálculo de prazo processual ou
   orientação jurídica.** São prompts de gestão do escritório: explicar o mês, escrever uma
   cobrança educada, preparar a reunião com o contador, revisar uma proposta pela margem,
   montar a rotina. O direito continua sendo feito por quem tem OAB.
2. **A IA erra com confiança.** Todo número, data e conclusão precisa ser conferido na
   planilha antes de virar e-mail, proposta ou decisão. Cada prompt diz o que revisar.
3. **Contexto é o segredo.** Diga quem lê, para quê e o que você já tem. Por isso os prompts
   começam com o papel e o contexto.

Como usar: copie o prompt inteiro, cole na IA, substitua os colchetes, cole o bloco da
planilha onde indicado e envie. Se a resposta vier ruim, não reescreva o prompt: responda
"Refaça: [o que faltou]".

Sobre os exemplos: usam o escritório fictício do kit, Ferraz & Lima Advocacia (dois sócios,
uma estagiária, 38 casos, setembro de 2026). Para você reconhecer as linhas, os exemplos citam
os nomes inventados da planilha; no bloco colado na IA, eles já viraram Cliente A, B, C.

## De onde vem cada bloco

| Planilha do kit | Aba que você copia | Usada nos prompts |
|---|---|---|
| 1 Agenda de prazos e audiências | Prazos (linhas da semana ou do mês) | Prazos 01, 03, 04 |
| 2 Andamento por processo | Processos | Prazos 05, 07 |
| 3 Rotina da semana do escritório | Rotina | Prazos 02, 06, 08 |
| 4 Checklist de abertura e encerramento | Checklist | Prazos 07, Clientes 08 |
| 5 Custo-hora do escritório | Painel, Custos fixos, Pessoas | Honorários 01, 03, Caixa 03 |
| 6 Simulador de honorário | Simulador | Honorários 02, 07 |
| 7 Proposta de honorários | Proposta | Honorários 04, 05, 08 |
| 8 Tabela de referência interna | Referência, Nossos casos | Honorários 06 |
| 9 Caixa do escritório | Painel, Lançamentos | Caixa 01, 02, 03, 08 |
| 10 Provisão de impostos, 13º e férias | Painel | Caixa 04, 05 |
| 11 Pró-labore e separação PF × escritório | Retiradas | Caixa 06 |
| 12 Reserva de três meses e metas de caixa | Painel | Caixa 07 |
| 13 Carteira de clientes e casos | Clientes, Casos | Clientes 01, 07 |
| 14 Parcelas e inadimplência | Parcelas (a régua está em Config) | Clientes 02, 03, 04, 05 |
| 15 Propostas enviadas × fechadas | Propostas | Clientes 06 |
| 16 Horas por caso e por pessoa | Horas (por caso e por pessoa) | Prazos 04, Honorários 03 |
| 17 Painel do escritório | Painel | Painel 01, 07 |
| 18 Resultado mensal simplificado | Resultado | Caixa 02, Painel 02 |
| 19 Metas do trimestre | Metas | Painel 05, 06 |
| 20 Resumo do mês para a IA e para o contador | Resumo ("Bloco único para copiar") | Painel 01, 02, 03, 04, Caixa 04 |

---

## Grupo 1 · Prazos e rotina (8)

### Prazos 01 · Priorizar os prazos da semana pela carga
**Quando usar:** na segunda de manhã, quando a aba Prazos mostra mais itens vermelhos e amarelos
do que cabe na semana. O prompt ordena pela conta de horas e pessoas, não pelo direito.
**Cole:** Planilha 1 · aba Prazos, só as linhas com situação Atrasado ou vencendo na semana (Cliente
trocado por letra; acrescente as horas estimadas de cada tarefa, da Planilha 16 ou de cabeça).

```
Você é meu assistente de organização de um escritório de advocacia pequeno. Não dê nenhuma orientação jurídica: não diga o que fazer em cada processo nem calcule prazo processual. Sua tarefa é só de agenda e de carga de trabalho.
Vou colar a lista de prazos da semana com: Cliente (letra) | Tipo de prazo | Dias para o prazo | Responsável | Horas estimadas. Somos [quantas pessoas], com [horas disponíveis por pessoa nesta semana].
Faça: 1) ordene do que vence primeiro para o que vence depois; 2) some as horas por dia e por pessoa e diga onde a carga estoura; 3) marque as tarefas que podem ser adiantadas para hoje ou terça sem prejuízo de agenda; 4) aponte quem está sobrecarregado e o que poderia passar para outra pessoa da equipe, se for tarefa que não exige o responsável. Responda em tabela e feche com três frases de plano para a semana.
Hoje é [data].
Lista:
[cole aqui]
```
**Exemplo:** Entrada: os 20 prazos com semáforo vermelho ou amarelo da Ferraz & Lima em
14/09/2026 (7 já vencidos, 13 vencendo até domingo), com Marina a 40 h disponíveis, Rafael
a 36 h e a estagiária Júlia a 20 h. Saída: tabela ordenada, três dias com carga acima de 8 h para
Marina (segunda, terça e quinta), duas tarefas de juntada de documentos sugeridas para a Júlia e
o plano: "resolver os 7 vencidos hoje, audiência da Cliente P na quinta, revisar as horas estimadas
do Cliente L".
**Confira:** a IA não sabe o que cada tarefa exige; o que "pode passar para outra pessoa" é decisão
sua. E o prazo processual continua sendo contado por você, no sistema do tribunal.

### Prazos 02 · Rotina de segunda em 30 minutos
**Quando usar:** na primeira semana com o kit, para montar a rotina de segunda (prazos) e de sexta
(caixa e painel) do jeito do seu escritório. Depois, repita quando entrar ou sair alguém da equipe.
**Cole:** Planilha 3 · aba Rotina (as linhas de segunda e de sexta do exemplo, para adaptar).

```
Monte a rotina semanal de gestão de um escritório de advocacia com [quantas pessoas: ex.: dois sócios e uma estagiária]. Dois blocos: segunda-feira (prazos e agenda), de no máximo 30 minutos, e sexta-feira (caixa, recebíveis e painel), de no máximo 30 minutos. Para cada bloco: os passos em ordem, quem faz, quantos minutos e qual planilha abre (use os nomes abaixo). Corte tudo que não cabe no tempo e diga o que ficou de fora e em que dia do mês seria feito.
Planilhas que temos: Agenda de prazos, Andamento por processo, Caixa do escritório, Parcelas e inadimplência, Painel do escritório.
Nossas particularidades: [ex.: audiências concentradas na quarta; o contador pede o fechamento até o dia 5].
Rotina de exemplo para adaptar:
[cole as linhas da aba Rotina]
```
**Exemplo:** Entrada: dois sócios e uma estagiária; audiências na quarta; contador pede o fechamento
até o dia 5; a rotina de exemplo do kit. Saída: segunda com 6 passos (abrir a Agenda de prazos,
conferir os vermelhos, atualizar o Andamento, distribuir, avisar clientes de audiência, fechar em 25
min) e sexta com 5 passos; a conciliação bancária ficou de fora e foi para o dia 1º do mês.
**Confira:** se a soma dos minutos bate e se a IA não inventou uma planilha que o kit não tem.

### Prazos 03 · O que os prazos atrasados têm em comum
**Quando usar:** no fim do mês, com as linhas que ficaram vermelhas em algum momento. Serve para
achar o padrão de gestão (pessoa, dia, tipo de tarefa), não para discutir o mérito.
**Cole:** Planilha 1 · aba Prazos, linhas do mês marcadas como Feito depois da data ou ainda Atrasado, sem os
nomes (a coluna Observação ajuda a explicar).

```
Você é um analista de processos internos. Vou colar a lista de prazos internos que atrasaram neste mês em um escritório de advocacia, com: Cliente (letra) | Tipo de prazo | Dias de atraso | Responsável | Dia da semana em que venceu | Observação. Não comente o conteúdo jurídico nem o efeito do atraso no processo; isso é comigo.
Responda: 1) o que essas linhas têm em comum (pessoa, tipo de tarefa, dia da semana, semana do mês); 2) hipóteses de causa de gestão, separadas de "o que os dados mostram"; 3) três mudanças de rotina, simples, para testar no mês que vem; 4) o que eu deveria medir para saber se funcionou. Sem culpar ninguém: descreva o sistema, não a pessoa.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: 9 linhas de setembro da Ferraz & Lima (4 juntadas de documentos, 3 manifestações,
2 reuniões com cliente; 6 com Marina; 5 venceram na sexta). Saída: padrão "tarefa curta, sexta-feira,
Marina"; hipótese: sexta é dia de caixa e as tarefas curtas ficam para o fim do dia; mudanças: mover
as juntadas para quarta, delegar a preparação à estagiária, criar um semáforo de 5 dias em vez de 3.
**Confira:** as hipóteses são chutes educados; teste uma por vez.

### Prazos 04 · Distribuir a semana entre as pessoas
**Quando usar:** quando uma pessoa está com o mês estourado e a outra folgada, ou quando entra
alguém novo. Junta prazos e horas.
**Cole:** Planilha 1 · aba Prazos (semana) e Planilha 16 (Horas por Caso, aba Painel, quadro por pessoa).

```
Ajude-me a redistribuir o trabalho da semana em um escritório de advocacia. Não é para decidir estratégia de nenhum caso; é agenda. Regras: [ex.: audiências e prazos de mérito ficam com o responsável do caso; preparação de documentos, contato com cliente, protocolo e organização podem ir para a estagiária; ninguém passa de 9 horas por dia].
Pessoas e horas já gastas no mês: [cole o resumo por pessoa da Planilha 16].
Tarefas da semana: [cole a aba Prazos].
Entregue: uma tabela por pessoa com as tarefas do dia e as horas; a lista do que mudou de mão; e uma mensagem curta para cada pessoa explicando o que ficou com ela e por quê.
```
**Exemplo:** Entrada: Marina com 98 h gastas em setembro contra 110 faturáveis, Rafael com 104, Júlia
com 52 de 60; 20 tarefas da semana. Saída: 6 tarefas mudaram de mão (5 preparações para a Júlia, 1
reunião com cliente de Marina para Rafael porque o caso é de área compartilhada), tabela por pessoa
e três mensagens de quatro linhas.
**Confira:** a regra de quem pode fazer o quê é sua e da OAB; a IA só aplica o que você escreveu.

### Prazos 05 · Resumo de andamento para o sócio
**Quando usar:** antes da reunião de sócios ou quando um sócio volta de férias. Transforma a aba
Processos em um resumo de gestão: fase, próxima ação, quem cuida.
**Cole:** Planilha 2 · aba Processos, colunas Cliente (letra), Área, Fase, Próxima ação, Data da próxima ação,
Responsável, Dias sem atualizar, Parado?.

```
Resuma a carteira de processos abaixo para um sócio que quer saber "em que pé está cada coisa" em dois minutos. Não interprete o mérito nem sugira estratégia processual; descreva a situação de gestão.
Formato: 1) uma frase com o total de casos ativos e a distribuição por fase; 2) uma lista dos casos com próxima ação nos próximos 7 dias (letra do cliente, ação, data, responsável); 3) casos sem próxima ação definida (isso é um problema de gestão: aponte); 4) três coisas que o sócio deveria perguntar na reunião. Até 200 palavras.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: os 30 casos ativos da Ferraz & Lima (6 na fase inicial, 5 em recurso, 8 em acordo,
4 consultivos, os demais em sentença, instrução e execução). Saída: resumo de 180 palavras, 13 casos com
ação na semana, 4 consultivos sem próxima ação definida ("Cliente C e Cliente L estão parados há mais
de 30 dias") e três perguntas para a reunião.
**Confira:** "parado" é o que a planilha mostra; confirme antes de falar isso ao sócio.

### Prazos 06 · Pauta da reunião de segunda com a equipe
**Quando usar:** para a reunião de 15 minutos de segunda, com os dados da semana.
**Cole:** Planilha 3 · aba Rotina (linhas de segunda) e os totais do Painel da Planilha 1 (atrasados, hoje,
próximos dias).

```
Monte a pauta de uma reunião de 15 minutos de segunda-feira em um escritório de advocacia com [quantas pessoas]. Objetivo: todo mundo sair sabendo o que vence, quem faz e o que travou. Estrutura: 1) números da semana (prazos vermelhos, amarelos e verdes; audiências); 2) o que atrasou na semana passada e o que aprendemos (sem culpa); 3) distribuição do que vence esta semana; 4) pendências com cliente (documento que falta, pagamento em aberto); 5) uma decisão que precisa ser tomada hoje. Diga quantos minutos cada item leva.
Dados:
[cole aqui]
```
**Exemplo:** Entrada: 7 vermelhos, 13 amarelos, 10 verdes, 3 audiências na semana; 2 tarefas atrasadas
na semana anterior; 4 clientes com documentos pendentes; decisão: aceitar ou não o caso novo do
Cliente Q. Saída: pauta de cinco itens em 15 minutos, com o item 5 marcado como "decidir hoje, com a
conta de horas do Honorários 08".
**Confira:** só o que está na planilha; a IA gosta de adicionar itens genéricos ("alinhamento").

### Prazos 07 · Pendências de abertura e encerramento viram tarefas
**Quando usar:** quando o checklist de abertura tem itens em aberto em vários casos (contrato não
assinado, procuração sem cópia, dados de cobrança sem preencher).
**Cole:** Planilha 4 · aba Checklist, linhas com pendências (colunas Cliente, Situação, Pendências, O que falta).

```
Transforme a lista de pendências administrativas abaixo em tarefas para a semana. Cada linha vem como: Cliente (letra) | Situação do caso | O que falta | Responsável | Aberto desde. Agrupe por tipo de pendência (contrato, documento, dados de cobrança, cadastro), escreva uma tarefa por grupo com verbo no infinitivo, sugira um prazo interno (hoje, esta semana, este mês) pela idade da pendência e monte, para as que dependem do cliente, uma mensagem de duas linhas pedindo o item, sem tom de cobrança. Não opine sobre o conteúdo dos documentos.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: 11 pendências em 8 casos da Ferraz & Lima (4 contratos sem a via assinada, 3 cadastros
sem dados de cobrança, 4 documentos que o cliente ainda não enviou). Saída: três tarefas com prazo,
"contratos sem via assinada" marcada como "hoje" porque a mais antiga tem 40 dias, e quatro mensagens
curtas para os clientes que devem documentos.
**Confira:** que documento pedir e por quê é decisão sua; a IA só escreve a mensagem.

### Prazos 08 · Semana revisada na sexta
**Quando usar:** na sexta, no fechamento, com o que foi feito e o que ficou. Alimenta a rotina da
semana seguinte.
**Cole:** Planilha 3 · aba Rotina (linhas de sexta, o que foi feito e o que ficou) e os números do Painel da
Planilha 17.

```
Faça a revisão semanal de um escritório de advocacia pequeno. Com a lista abaixo (prazos cumpridos, prazos que atrasaram, audiências feitas, o que entrou de dinheiro, o que vence na próxima semana), responda: 1) o que andou de mais importante; 2) o que travou e a causa provável de gestão (não de mérito); 3) três ajustes simples para a próxima semana; 4) uma mensagem de duas linhas que eu possa mandar para [o sócio / a equipe] resumindo a semana. Tom direto, sem elogio vazio.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: semana de 14 a 18/09 da Ferraz & Lima: 16 prazos cumpridos, 2 atrasados, 3
audiências, R$ 8.900 recebidos, 11 prazos na próxima semana. Saída: os quatro blocos; causa provável
dos atrasos: "as duas tarefas dependiam de documento do cliente"; ajuste: pedir documento com 10 dias
de antecedência; mensagem pronta para o sócio.
**Confira:** a causa provável é hipótese; a IA não viu a semana.

---

## Grupo 2 · Honorários e propostas (8)

### Honorários 01 · Entender o meu custo-hora
**Quando usar:** logo depois de preencher a Planilha 5 pela primeira vez, quando o número aparece
e você quer saber se faz sentido e o que muda se mexer em alguma coisa.
**Cole:** Planilha 5 · aba Painel (custo total, horas faturáveis, custo-hora, hora mínima) e a aba Pessoas.

```
Explique para mim, dono de um escritório de advocacia pequeno, o que o custo-hora abaixo significa na prática, em até 200 palavras e sem jargão. Depois: 1) refaça a conta passo a passo para eu conferir; 2) diga o que acontece com o custo-hora se as horas faturáveis caírem 20% (mês de férias, por exemplo); 3) diga o que acontece se eu somar [ex.: um estagiário a mais por R$ 1.400]; 4) aponte o que costuma ficar de fora dessa conta em escritórios pequenos. Não sugira preço de honorário: a tabela da OAB e o contrato são comigo.
Números:
[cole o painel]
```
**Exemplo:** Entrada: o painel da Ferraz & Lima: custo fixo R$ 6.500, pró-labore dos dois sócios
R$ 12.000, 280 horas faturáveis por mês (110 + 110 + 60), custo-hora de cerca de R$ 66. Saída:
explicação em linguagem simples ("cada hora de trabalho do escritório custa R$ 66 antes de qualquer
lucro"), a conta refeita, custo-hora subindo para cerca de R$ 83 com 20% menos horas, e o alerta de
que férias, inadimplência e horas não faturáveis (administrativo, captação) não estão na conta.
**Confira:** a conta refeita, com calculadora. Se a IA chegar a outro número, o erro pode ser dela.

### Honorários 02 · Revisar a proposta pela margem
**Quando usar:** com a proposta montada no Simulador, antes de enviar. É o "advogado do diabo" da
sua própria conta.
**Cole:** Planilha 6 · aba Simulador (tipo de honorário, horas estimadas, custo-hora, margem, valor
proposto, condições de pagamento).

```
Revise a conta de uma proposta de honorários pela ótica da margem, não do direito. Dados: custo-hora do escritório R$ [ ]; horas estimadas [ ]; margem desejada [ ]%; valor proposto R$ [ ]; forma: [fixo / por hora / êxito / misto]; parcelas: [ ]; prazo esperado do caso: [meses].
Responda: 1) a margem real embutida no valor proposto (valor ÷ custo das horas − 1); 2) em quantas horas gastas a mais a margem vira zero; 3) o custo de esperar: se o pagamento só vier em [meses], quanto custa manter o caso no caixa até lá; 4) três perguntas que eu deveria responder antes de enviar. Não opine sobre a viabilidade jurídica nem sobre limites éticos de honorário: isso é comigo e com a OAB.
```
**Exemplo:** Entrada: caso novo da Escola Aurora (na IA: Cliente M), por hora, 50 horas estimadas,
custo-hora R$ 66, margem desejada 40%, valor proposto R$ 8.000 em 4 parcelas. Saída: margem real de
142% sobre o custo das horas (R$ 8.000 contra R$ 3.300 de custo), margem zero só com 121 horas, custo
de espera baixo porque as parcelas começam no mês 1, e três perguntas (quem paga as custas, o que
acontece se passar de 50 horas, há outro caso do mesmo cliente consumindo horas).
**Confira:** as duas contas de margem. E lembre que margem sobre custo-hora não é lucro líquido:
falta imposto, inadimplência e horas não faturáveis.

### Honorários 03 · Casos que consomem mais do que pagam
**Quando usar:** no fim do mês, cruzando horas gastas com valor contratado. Mostra onde a estimativa
errou e onde o próximo contrato do mesmo tipo precisa ser diferente.
**Cole:** Planilha 16 (horas por caso: Cliente em letra, Modalidade, Valor contratado, Horas estimadas, Horas
gastas, Recebido) e o custo-hora da Planilha 5.

```
Vou colar a lista de casos ativos com horas estimadas, horas gastas, valor contratado e recebido. Custo-hora do escritório: R$ [ ]. Para cada caso, calcule: custo das horas gastas (horas × custo-hora), valor contratado por hora gasta, e o desvio entre estimado e gasto em %. Depois: 1) liste os casos em que as horas gastas já passaram das estimadas; 2) os casos em que o valor por hora gasta está abaixo do custo-hora; 3) os casos de êxito com muitas horas e nada recebido, como risco de caixa; 4) o que isso sugere para a próxima estimativa de casos parecidos. Não comente estratégia jurídica.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: os 30 casos ativos da Ferraz & Lima com custo-hora R$ 66. Saída: 12 casos acima da
estimativa; o pior é o Cliente A (Padaria do Sol, empresarial, êxito): 74 h gastas para 63 estimadas,
R$ 4.900 de custo e nada recebido ainda; Cliente C (Construtora Horizonte, cível): 58 h para 45; a
sugestão: "casos empresariais estão saindo 20% acima da estimativa; use 1,2× na próxima proposta".
**Confira:** horas gastas dependem de todo mundo lançar; se a Júlia não lançou, a conta engana.

### Honorários 04 · Texto de apresentação da proposta
**Quando usar:** com a tabela de honorários pronta na Planilha 7, para escrever a página de
apresentação que vai antes da tabela. Só o texto comercial e administrativo; o contrato é seu.
**Cole:** Planilha 7 · aba Proposta (escopo em uma frase, forma de honorário, valor, parcelas, validade).

```
Escreva a apresentação de uma proposta de honorários de um escritório de advocacia, em até 250 palavras, para [pessoa física / empresa] que nos procurou para [descreva o serviço em uma frase, sem detalhes do caso]. Estrutura: entendimento do pedido (2 frases); como trabalhamos (quem atende, como o cliente é informado, canal e prazo de resposta); o que está incluído e o que não está (só o que eu listar); investimento (R$ [ ], forma [ ], parcelas [ ]); validade da proposta ([dias]); próximo passo. Tom profissional, claro, sem promessa de resultado, sem prazo de conclusão do caso e sem juridiquês. Não invente serviços além dos listados.
Incluído: [liste]. Não incluído: [liste].
```
**Exemplo:** Entrada: empresa (Clínica Bem-Estar, na IA: Cliente I), consultoria mensal de rotina
empresarial, R$ 9.300 em 6 parcelas, validade de 10 dias; incluído: reuniões mensais, revisão de
documentos administrativos até 10 por mês, resposta em 2 dias úteis; não incluído: contencioso e
custas. Saída: texto de 230 palavras, com "como trabalhamos" explicando canal e prazo de resposta e
sem nenhuma frase do tipo "garantimos".
**Confira:** se aparecer qualquer promessa de resultado ou de prazo do caso, apague. Valor e
parcelas iguais aos do Simulador.

### Honorários 05 · Responder a um pedido de desconto
**Quando usar:** quando o cliente pediu desconto ou parcelamento maior e você quer responder sem
ceder no escuro.
**Cole:** Planilha 7 · aba Proposta (valor, parcelas) e a margem do Simulador (Planilha 6).

```
Recebi um pedido de desconto em uma proposta de honorários. Valor proposto R$ [ ]; custo estimado das horas R$ [ ]; margem atual [ ]%. O cliente pediu [ex.: 20% de desconto / 10 parcelas em vez de 4]. Minha posição: posso [ex.: parcelar em 6, tirar uma reunião mensal do escopo] e não posso [ex.: baixar o valor total].
Escreva a resposta em até 150 palavras: reconheça o pedido em uma frase, exponha a posição com clareza, ofereça as alternativas concretas e feche com um próximo passo. Sem pedir desculpas em excesso, sem tom defensivo e sem justificar com o caso em si. Antes do texto, calcule o que cada alternativa faz com a margem.
```
**Exemplo:** Entrada: proposta de R$ 9.300 em 6 parcelas, custo das horas R$ 3.560, cliente pediu 20% de
desconto; posso parcelar em 9 ou reduzir o escopo. Saída: cálculo (20% de desconto derruba a margem
de 161% para 109%; parcelar em 9 não muda a margem, mas atrasa o caixa em 3 meses) e resposta de
140 palavras com as duas alternativas.
**Confira:** o que você realmente pode ceder. A IA tende a oferecer mais do que você disse.

### Honorários 06 · Montar a tabela de referência interna
**Quando usar:** depois de três meses com o kit, quando a Planilha 16 já tem histórico de horas por tipo
de caso. Cria faixas para as propostas ficarem coerentes entre si.
**Cole:** Planilha 16 (Horas por Caso, aba Painel), colunas Área, Modalidade, Horas estimadas, Horas gastas, Valor
contratado (casos encerrados e ativos); a Planilha 8 · aba Nossos casos tem o valor por hora já calculado.

```
Com o histórico abaixo de casos de um escritório de advocacia (área, modalidade de honorário, horas estimadas, horas gastas, valor contratado), monte uma tabela de referência interna por área: horas típicas (mínimo, mediana, máximo), valor contratado típico, valor por hora gasta, e uma faixa sugerida de horas para a próxima estimativa (mediana × 1,2 quando o histórico mostra que estouramos). Marque as áreas com menos de 3 casos como "amostra pequena". Isso é referência interna de gestão; não sugira preço com base em tabela da OAB nem em mercado, só nos meus dados.
Custo-hora: R$ [ ].
Histórico:
[cole aqui]
```
**Exemplo:** Entrada: os 38 casos da Ferraz & Lima (8 encerrados), custo-hora R$ 66. Saída: tabela com
cinco áreas; Empresarial com mediana de 70 h e valor típico de R$ 14.000; Previdenciário com 42 h e
R$ 5.900; "Família" e "Instrução" marcadas como amostra pequena; faixa sugerida com 1,2× para
Empresarial e Cível.
**Confira:** mediana e não média (um caso gigante distorce); preencha a aba Referência da Planilha 8 só
depois de conferir dois valores à mão.

### Honorários 07 · Fixo, hora, êxito ou misto: perguntas antes de escolher
**Quando usar:** com um caso novo em que a forma de cobrar não é óbvia. O prompt ajuda a pensar na
conta e no caixa; a escolha, o contrato e os limites éticos são seus.
**Cole:** Planilha 6 · aba Simulador, os quatro cenários já calculados para o caso.

```
Vou colar quatro cenários de honorário para um mesmo caso (fixo, por hora, êxito, misto), com valor esperado, horas estimadas, quando o dinheiro entra e a margem sobre o custo-hora. Não me diga qual escolher e não comente a viabilidade jurídica nem regras da OAB: isso é comigo. Ajude-me a pensar: 1) para cada cenário, o melhor e o pior caso de caixa (quanto entra e quando); 2) o que cada cenário pressupõe sobre o cliente e sobre o caso; 3) cinco perguntas que eu deveria responder antes de decidir; 4) que cenário exige mais reserva de caixa do escritório e quanto.
Custo fixo mensal do escritório: R$ [ ]. Reserva atual: R$ [ ].
Cenários:
[cole aqui]
```
**Exemplo:** Entrada: caso cível novo da Luciana Farias (na IA: Cliente P), 69 h estimadas; fixo R$ 12.000
em 6×, hora R$ 110 × 69 h, êxito 20% sobre valor estimado, misto R$ 5.000 + 10%; custo fixo R$ 6.500,
reserva R$ 14.000. Saída: pior caso de caixa no êxito (R$ 0 por 18 meses, R$ 4.550 de custo de horas),
cinco perguntas (capacidade de pagamento do cliente, duração provável, quantos casos de êxito já
estão abertos) e a conta: "o êxito exige cerca de dois meses de custo fixo a mais na reserva".
**Confira:** os números de "quando entra" são hipóteses suas; a IA só organizou.

### Honorários 08 · Antes de aceitar o caso: a conta de horas e de caixa
**Quando usar:** na primeira conversa com um cliente novo, antes de dizer sim. Não é análise de
viabilidade jurídica; é a conta de se o escritório aguenta o caso.
**Cole:** Planilha 17 · aba Painel (horas disponíveis no mês, casos ativos por pessoa, caixa) e a
estimativa de horas do caso.

```
Estou decidindo se aceito um caso novo em um escritório de advocacia pequeno. Não avalie o mérito nem a chance de êxito; avalie a capacidade do escritório. Dados: horas estimadas do caso [ ], distribuídas em [meses]; responsável seria [pessoa], que tem [horas livres por mês] e [casos ativos]; forma de cobrar [ ]; primeira entrada de dinheiro em [meses]; custo-hora R$ [ ]; caixa atual R$ [ ]; custo fixo mensal R$ [ ].
Responda: 1) cabe na agenda? (horas do caso por mês contra horas livres); 2) cabe no caixa? (custo das horas até a primeira entrada); 3) o que teria de sair ou ser adiado para caber; 4) três condições que eu poderia colocar na proposta para reduzir o risco de gestão (entrada, parcelas, limite de horas); 5) uma versão menor do mesmo trabalho, se existir. Não me diga o que decidir.
```
**Exemplo:** Entrada: caso trabalhista de 60 h em 8 meses para Rafael, que tem 6 h livres por mês e 15 casos;
êxito, primeira entrada em 12 meses; custo-hora R$ 66; caixa R$ 21.000; custo fixo R$ 6.500. Saída: "não
cabe na agenda: 7,5 h por mês contra 6 livres"; custo de R$ 3.960 até a primeira entrada; adiar o
consultivo do Cliente L; condições: entrada de 20%, teto de horas; versão menor: só a fase inicial.
**Confira:** as horas livres de verdade (a Planilha 16 mostra); o resto é conta simples.

---

## Grupo 3 · Caixa e contador (8)

### Caixa 01 · Explicar o mês do caixa
**Quando usar:** na sexta de fechamento, com o Painel do Caixa, para explicar ao sócio (ou a você
mesmo) o que aconteceu com o dinheiro.
**Cole:** Planilha 9 · aba Painel (entradas por tipo, saídas por categoria, saldo, comparação com o
mês anterior).

```
Explique o resultado de caixa do mês de um escritório de advocacia para [o sócio / eu mesmo], em até 200 palavras e linguagem simples: quanto entrou (e de que tipo: fixo, hora, êxito, parcelas antigas), quanto saiu, para onde foi a maior parte, quanto sobrou, o que mudou em relação ao mês anterior e uma decisão sugerida para o próximo mês. Separe "entrou" de "faturou": se eu marcar algo como a receber, não conte como dinheiro. Sem termos técnicos.
Números:
[cole o painel]
Contexto: [o que aconteceu de diferente no mês].
```
**Exemplo:** Entrada: o Painel de setembro da Ferraz & Lima: entradas R$ 31.400 (R$ 19.200 de parcelas
fixas, R$ 8.900 por hora, R$ 3.300 de um acordo), saídas R$ 21.900 (pró-labore R$ 12.000, fixos R$ 6.500,
provisão R$ 2.000, variáveis R$ 1.400), sobra R$ 9.500; agosto: entradas R$ 26.800. Contexto: "entrou o
acordo do Cliente H". Saída: 190 palavras em linguagem de conversa e a decisão sugerida: "levar
R$ 3.000 para a reserva, porque R$ 3.300 vieram de um acordo que não se repete".
**Confira:** números e a decisão. Se a sobra parece grande, veja se a provisão de impostos foi lançada.

### Caixa 02 · Comparar dois meses do resultado
**Quando usar:** mês contra mês, com o Resultado mensal (DRE simplificado), quando algo mudou e você
quer saber o quê.
**Cole:** Planilha 18 · aba Resultado, colunas dos dois meses.

```
Compare os dois meses abaixo do resultado de um escritório de advocacia, linha por linha: variação absoluta, variação percentual e um comentário de uma linha. Depois, os três maiores avanços, os três maiores recuos e uma conclusão de duas frases. Classifique cada linha como "melhorou", "piorou" ou "estável" (estável = variação menor que [3]%). Lembre que para despesas, provisão e inadimplência, menor é melhor. Não invente causas: separe "o que os números mostram" de "hipóteses".
Mês 1 ([nome]):
[cole]
Mês 2 ([nome]):
[cole]
```
**Exemplo:** Entrada: agosto e setembro da Ferraz & Lima (receita R$ 26.800 para R$ 31.400; despesas
R$ 22.300 para R$ 21.900; resultado R$ 4.500 para R$ 9.500; inadimplência R$ 4.100 para R$ 3.090).
Saída: tabela com 9 linhas, receita +17,2% (melhorou), despesas −1,8% (estável), inadimplência −24,6%
(melhorou) e a conclusão: "o mês foi melhor por uma entrada extraordinária; sem ela, estável".
**Confira:** sinais de "menor é melhor" e as porcentagens; a IA erra conta de variação.

### Caixa 03 · Onde cortar custo fixo sem prejudicar o escritório
**Quando usar:** quando o custo fixo subiu, um sócio vai tirar férias ou o caixa apertou.
**Cole:** Planilha 5 · aba Custos fixos (custo por categoria) e a Planilha 9 · aba Painel (saídas por
categoria dos últimos 3 meses).

```
Analise o custo fixo de um escritório de advocacia por categoria e me ajude a decidir onde cortar sem prejudicar o atendimento nem a regularidade profissional. Para cada categoria: fixo ou variável? Essencial, importante ou supérfluo? Quanto seria realista reduzir em 60 dias e como? Depois, um plano com três cortes que somem pelo menos R$ [valor alvo] por mês, do mais fácil ao mais difícil, e o que eu perco com cada um. Não sugira cortar anuidade da OAB, contador nem seguro; são obrigatórios ou de proteção.
Custo fixo:
[cole aqui]
```
**Exemplo:** Entrada: os R$ 6.500 de custo fixo da Ferraz & Lima (aluguel R$ 2.800, bolsa da estagiária
R$ 1.400, contador R$ 600, sistemas R$ 450, marketing R$ 400, material R$ 380, anuidades e cursos R$ 250,
telefone R$ 220); alvo: R$ 600. Saída: sistemas marcados como "conferir o que ninguém usa", marketing
como variável, e três cortes (assinaturas duplicadas R$ 180, telefone fixo R$ 120, material R$ 150 com
compra trimestral) que chegam perto do alvo, com o aviso de que o aluguel é o único corte grande.
**Confira:** a IA não sabe o que é essencial para o seu atendimento; ajuste a classificação.

### Caixa 04 · Preparar a reunião mensal com o contador
**Quando usar:** dois dias antes da reunião com o contador, com o Resumo do mês pronto. Junta o que
enviar, o que perguntar e o que anotar (o roteiro completo é o bônus 24).
**Cole:** Planilha 20 · aba Resumo ("Bloco único para copiar") e a Planilha 10 · aba Painel (provisão
acumulada).

```
Vou me reunir com o contador do meu escritório de advocacia por 30 minutos. Com o resumo do mês abaixo, monte: 1) a lista do que eu envio antes (documentos e números, com o nome da planilha de origem); 2) a pauta em 4 blocos com minutos; 3) oito perguntas objetivas para o contador, priorizando o que muda dinheiro (provisão, pró-labore, regime, notas, retenções); 4) uma tabela vazia "Pergunta | Resposta | Ação | Prazo" para eu preencher na reunião. Não responda as perguntas no lugar do contador nem dê orientação tributária.
Resumo do mês:
[cole aqui]
Dúvidas que já tenho: [liste]
```
**Exemplo:** Entrada: o Resumo de setembro da Ferraz & Lima (receita R$ 31.400, pró-labore R$ 12.000,
provisão acumulada R$ 5.400, 3 notas emitidas para PJ, 1 recebimento de PF sem nota) e a dúvida "o
acordo do Cliente H entra como receita do mês?". Saída: lista de 6 itens para enviar, pauta de 4
blocos (5 + 10 + 10 + 5 min), 8 perguntas ("a provisão de R$ 5.400 cobre o que vence até dezembro?")
e a tabela vazia.
**Confira:** as perguntas são para o contador responder; não use a resposta da IA como resposta
dele.

### Caixa 05 · Perguntas sobre a provisão de impostos, 13º e férias
**Quando usar:** quando o número da provisão parece alto ou baixo e você não sabe se está certo.
O prompt não calcula imposto; ele monta as perguntas certas para o contador.
**Cole:** Planilha 10 · aba Painel (receita do mês, alíquota informada pelo contador, provisão do mês,
acumulado, próximos vencimentos).

```
Sou dono de um escritório de advocacia pequeno e provisiono impostos, 13º e férias em uma planilha com a alíquota que o contador me informou. Não calcule imposto nem diga qual regime é melhor: isso é do contador. Com os números abaixo, faça: 1) confira se a conta provisão = receita × alíquota está aritmeticamente certa; 2) diga se o acumulado cobre o que vence nos próximos 90 dias e, se não, o buraco em reais; 3) monte cinco perguntas para o contador que esclareçam o que a planilha não sabe (o que entra na base, retenções, 13º de quem, férias de quem); 4) uma regra simples de quanto separar por semana.
Números:
[cole aqui]
```
**Exemplo:** Entrada: receita de setembro R$ 31.400, alíquota informada 6%, provisão do mês R$ 1.884,
acumulado R$ 5.400, vencimentos dos próximos 90 dias R$ 5.650 (impostos) + R$ 1.400 (13º da estagiária,
se devido). Saída: conta conferida, buraco de R$ 1.650, cinco perguntas ("a estagiária tem 13º?"; "o
recebimento de PF sem nota entra na base?") e a regra: "separar R$ 470 por semana (a provisão do mês
dividida por quatro) mais R$ 130 até fechar o buraco".
**Confira:** a alíquota é a que o contador disse, não a que a IA sugerir. Se ela sugerir alguma, ignore.

### Caixa 06 · Separar o que é do escritório e o que é pessoal
**Quando usar:** quando o extrato veio misturado (conta única, cartão do sócio) e você precisa
classificar antes de lançar na aba Retiradas da Planilha 11.
**Cole:** o extrato do mês, só com data, descrição resumida e valor, sem número de conta, sem nome
de terceiros.

```
Vou colar lançamentos de um extrato bancário misturado (escritório de advocacia e vida pessoal do sócio), com data, descrição resumida e valor. Classifique cada linha em: Escritório: custo fixo | Escritório: custo variável | Escritório: receita | Pró-labore ou retirada | Pessoal | Não sei. Use a categoria "Não sei" sempre que a descrição for ambígua; não chute. Depois some cada grupo e diga: quanto o sócio retirou além do pró-labore combinado de R$ [ ]; e quais lançamentos pessoais foram pagos pela conta do escritório. Responda em tabela.
Lançamentos:
[cole aqui]
```
**Exemplo:** Entrada: 42 lançamentos de setembro da conta da Marina (sócia), descrição resumida.
Saída: tabela classificada, 6 linhas em "Não sei" (posto de gasolina, restaurante), retirada de
R$ 7.300 contra pró-labore de R$ 6.000 (R$ 1.300 a mais) e três lançamentos pessoais na conta do
escritório (mercado, escola, streaming).
**Confira:** cada "Não sei" e as retiradas; corrija na tabela e só então lance na planilha.

### Caixa 07 · Plano para a reserva de três meses
**Quando usar:** quando a Planilha 12 mostra menos de três meses de custo fixo guardados e você
quer um plano que caiba no caixa real.
**Cole:** Planilha 12 · aba Painel (custo fixo mensal, reserva atual, meses cobertos, sobra média dos
últimos 3 meses).

```
Monte um plano para um escritório de advocacia chegar a três meses de custo fixo em reserva. Dados: custo fixo mensal R$ [ ]; reserva atual R$ [ ]; sobra média mensal dos últimos 3 meses R$ [ ]; entradas previstas fora do comum nos próximos 6 meses: [ex.: êxito do Cliente A, R$ 14.400, sem data certa].
Responda: 1) a meta em reais e quantos meses faltam no ritmo atual; 2) três ritmos (conservador, provável, ambicioso) com o valor a separar por mês e a data de chegada; 3) regras: o que a reserva pode pagar e o que não pode; 4) o que fazer com uma entrada extraordinária (êxito, acordo) quando vier. Não conte com a entrada extraordinária no cenário provável.
```
**Exemplo:** Entrada: custo fixo R$ 6.500 (meta R$ 19.500), reserva R$ 14.000, sobra média R$ 5.200, êxito
possível de R$ 14.400 sem data. Saída: faltam R$ 5.500; conservador R$ 1.500 por mês (4 meses),
provável R$ 2.500 (3 meses), ambicioso R$ 3.500 (2 meses); regra: "a reserva paga custo fixo em mês sem
entrada; não paga férias nem equipamento"; entrada extraordinária: 50% para a reserva até a meta.
**Confira:** a sobra média (que a planilha calcula) e se o ritmo cabe no pró-labore combinado.

### Caixa 08 · Achar o erro no caixa
**Quando usar:** quando o saldo do Painel não bate com o banco ou um total parece estranho.
**Cole:** Planilha 9 · aba Painel e as linhas suspeitas da aba Lançamentos (sem nomes).

```
Vou colar um trecho da planilha de caixa de um escritório de advocacia em que algo não bate. Ajude-me a encontrar o erro: verifique somas, sinais (entrada lançada como saída), lançamentos duplicados, transferências para a reserva contadas como despesa, valores em texto, datas fora do mês. Liste cada suspeita com a linha, o que esperava e o que encontrou. Se precisar de mais contexto, diga exatamente qual.
O que eu esperava: [ex.: sobra do mês de R$ 9.500; o banco mostra R$ 7.250].
Trecho:
[cole]
```
**Exemplo:** Entrada: "esperava sobra de R$ 9.500; o banco mostra R$ 7.250"; o Painel e 18 lançamentos
da última semana. Saída: duas suspeitas: a transferência de R$ 1.500 para a reserva não foi lançada
como saída, e a parcela de R$ 750 do Cliente F aparece duas vezes (dia 10 e dia 11). A soma das duas
(R$ 2.250) explica a diferença.
**Confira:** tudo. Este prompt acha suspeitas, não prova erros.

---

## Grupo 4 · Clientes e cobrança (8)

### Clientes 01 · Resumir a carteira para o sócio
**Quando usar:** na reunião de sócios ou no fechamento do mês, para responder "quanto ainda vai
entrar e de onde".
**Cole:** Planilha 13 · aba Casos, colunas Cliente (letra), Área, Modalidade, Fase, Valor contratado,
Recebido, A receber (a aba Clientes dá o total por cliente).

```
Resuma a carteira de um escritório de advocacia abaixo para um sócio, em até 200 palavras: 1) total contratado, recebido e a receber; 2) o a receber dividido em "parcelas com data" e "êxito sem data"; 3) os cinco clientes que mais devem ao escritório (pela letra) e o que é parcela atrasada versus parcela futura; 4) concentração: quanto dos recebíveis depende de um só cliente; 5) três perguntas de gestão que a carteira levanta. Não comente o mérito de nenhum caso. Use só os números colados.
Carteira:
[cole aqui]
```
**Exemplo:** Entrada: os 38 casos da Ferraz & Lima: R$ 374.200 contratados, R$ 245.920 recebidos, R$ 128.280
a receber. Saída: 190 palavras: a receber com R$ 77.380 em parcelas com data e R$ 50.900 em êxito sem
data; os cinco maiores (Cliente P com R$ 26.730 em dois casos, Cliente A, Cliente L, Cliente G, Cliente H);
concentração de 21% no Cliente P; perguntas: "quantos meses de custo fixo estão presos em êxito?", "o Cliente A tem
parcela atrasada há quanto tempo?".
**Confira:** a divisão parcela × êxito; e o total a receber, que precisa ser contratado menos recebido.

### Clientes 02 · Quem cobrar primeiro
**Quando usar:** na sexta, com a aba Parcelas mostrando mais atrasos do que dá para ligar em uma
tarde. Ordena pela conta, não pela vontade.
**Cole:** Planilha 14 · aba Parcelas, linhas vencidas (Cliente em letra, Nº da parcela, Valor, Dias de atraso,
Faixa, Ação sugerida); acrescente à mão a data do último contato e se o cliente já atrasou antes.

```
Ordene as parcelas atrasadas de um escritório de advocacia abaixo para eu decidir quem cobrar primeiro hoje. Critérios, nesta ordem: valor × dias de atraso; cliente que nunca atrasou antes (cobre cedo, com leveza: provavelmente esqueceu); último contato há mais de 7 dias; parcela que trava a continuidade de algo combinado no contrato (eu marco). Para cada linha: prioridade (1 a 3), o degrau da régua de cobrança (lembrete, segunda cobrança, conversa, proposta de acordo) e o canal (WhatsApp, e-mail, ligação). Sem tom de ameaça em nenhuma sugestão. Não cite consequências processuais nem contratuais: isso é comigo.
Parcelas:
[cole aqui]
```
**Exemplo:** Entrada: 3 parcelas vencidas em 14/09: Cliente L (Patrícia Gomes) R$ 750 há 15 dias, nunca
atrasou; Cliente R (Helena Duarte) R$ 790 há 7 dias, segundo atraso; Cliente O (Oficina Mecânica Central)
R$ 1.550 há 30 dias, último contato há 12 dias. Saída: Cliente O prioridade 1 (ligação, degrau
"conversa"), Cliente L prioridade 2 (WhatsApp, lembrete leve), Cliente R prioridade 2 (e-mail,
segunda cobrança).
**Confira:** o histórico de atraso; a planilha só sabe o que foi lançado.

### Clientes 03 · Cobrança educada em três versões
**Quando usar:** com uma parcela atrasada e a régua da Planilha 14 dizendo em que degrau está. Os
15 modelos do bônus são a versão pronta; este prompt é para quando o caso pede algo sob medida.
**Cole:** Planilha 14 · aba Parcelas, a linha da parcela (cliente em letra, valor, vencimento, dias de atraso,
ação sugerida pela régua).

```
Escreva três versões de mensagem de cobrança de honorários para [Cliente A], sobre a parcela [n de N] de R$ [ ], vencida em [data]: 1) lembrete amigável (primeiro contato, presuma esquecimento); 2) segunda cobrança, firme e cordial; 3) convite para uma conversa sobre como regularizar, claro e sem ameaça. Cada uma com até 80 palavras, com a forma de pagamento (Pix [chave], boleto) e um caminho fácil para resolver (responder esta mensagem, ligar para [telefone]). Tom de escritório de advocacia: respeitoso, sem "prezado" em excesso e sem juridiquês. Não mencione consequências processuais, contratuais ou de suspensão de atendimento: isso é decisão minha e do contrato.
```
**Exemplo:** Entrada: Cliente L, parcela 3 de 6 de R$ 750, vencida em 30/08/2026, Pix pelo CNPJ do
escritório. Saída: três mensagens de 60 a 80 palavras, da primeira ("pode ter passado despercebido")
à terceira ("podemos conversar sobre a melhor forma de regularizar?"), todas com valor, data e chave.
**Confira:** valor, data, parcela; e se nenhuma versão insinua consequência que você não decidiu.

### Clientes 04 · Roteiro de ligação de cobrança
**Quando usar:** antes de ligar para um cliente com parcela atrasada há mais de 15 dias, quando
mensagem já não resolveu.
**Cole:** Planilha 14 · aba Parcelas (a linha) e o seu registro de contatos com esse cliente (datas e canal).

```
Monte um roteiro de ligação de até 4 minutos para cobrar uma parcela de honorários atrasada de [Cliente A]: parcela de R$ [ ], vencida há [dias], já enviamos [quantas mensagens, em que datas]. Estrutura: abertura (uma frase, sem rodeio e sem "desculpa incomodar"); pergunta aberta sobre o que aconteceu; escuta (o que anotar); três saídas possíveis que eu posso oferecer: [ex.: pagar até sexta / dividir a parcela em duas / nova data]; fechamento com combinado explícito e confirmação por escrito. Inclua o que NÃO dizer (ameaça, comparação com outros clientes, comentário sobre o caso) e o que fazer se a pessoa ficar irritada. Português falado, curto.
```
**Exemplo:** Entrada: Cliente O, R$ 1.550, 30 dias de atraso, duas mensagens (dias 1 e 8 de setembro).
Saída: roteiro de uma página: abertura em uma frase, pergunta "aconteceu alguma coisa com o
pagamento deste mês?", três saídas, fechamento "então fica combinado dia 18, e eu confirmo por
WhatsApp agora" e a lista do que não dizer.
**Confira:** as saídas que você oferece têm de caber no caixa; a IA não sabe o que você pode.

### Clientes 05 · Responder a um pedido de prazo ou renegociação
**Quando usar:** quando o cliente pediu para adiar, dividir ou parar de pagar. Responde sem ceder no
escuro e sem entrar no contrato.
**Cole:** Planilha 14 · aba Parcelas (o que falta receber desse cliente) e a Planilha 13 (valor
contratado, horas gastas).

```
Recebi de [Cliente A] o pedido abaixo sobre as parcelas de honorários. Situação: falta receber R$ [ ] em [n] parcelas; já recebemos R$ [ ]; horas já gastas no caso [ ]. Minha posição: posso [ex.: adiar 30 dias / dividir a parcela] e não posso [ex.: reduzir o total]. Escreva a resposta em até 150 palavras: reconheça a situação em uma frase, exponha a posição sem se justificar com o caso, ofereça uma alternativa concreta com datas e feche pedindo confirmação por escrito. Antes do texto, mostre o que cada alternativa faz com o caixa do escritório nos próximos 3 meses. Não mencione nada sobre o andamento do caso nem consequências contratuais.
Pedido do cliente (sem dados pessoais):
[cole]
```
**Exemplo:** Entrada: Cliente R (Helena Duarte, trabalhista, misto): falta receber R$ 5.530 em 7 parcelas,
recebido R$ 2.370, 31 h gastas; cliente pediu para pausar 2 meses; posso adiar 30 dias ou reduzir a
parcela e alongar. Saída: tabela de caixa (pausa de 2 meses tira R$ 1.580 do trimestre; alongar tira
R$ 790) e resposta de 130 palavras com a alternativa de alongar.
**Confira:** os números do trimestre e se a resposta não promete o que o contrato não permite.

### Clientes 06 · Por que as propostas não fecham
**Quando usar:** no fim do trimestre, com o funil da Planilha 15 mostrando muita proposta aberta ou
perdida.
**Cole:** Planilha 15 · aba Propostas (Cliente em letra, Área, Serviço, Origem, Valor, Etapa, Data de entrada,
Motivo se perdida, Dias parada, Dias até fechar).

```
Analise o funil de propostas de honorários de um escritório de advocacia. Para o trimestre: taxa de fechamento geral, por área e por forma de honorário; valor médio das fechadas e das perdidas; tempo médio até a resposta; motivos de perda mais frequentes; propostas abertas há mais de [15] dias que merecem um contato. Separe "o que os dados mostram" de "hipóteses". Termine com três testes simples para o próximo trimestre (ex.: mudar a validade, ligar no terceiro dia, oferecer duas formas de pagamento). Não sugira baixar preço com base em mercado; use só os meus dados.
Propostas:
[cole aqui]
```
**Exemplo:** Entrada: 22 propostas do trimestre da Ferraz & Lima (12 fechadas, 5 perdidas, 5 abertas
somando R$ 41.500). Saída: fechamento de 55% (71% nas de valor fixo, 33% nas de êxito), valor médio
fechado R$ 8.900, 9 dias até a resposta, motivo de perda mais comum "preço" (3 de 5), 2 abertas há
mais de 15 dias e três testes.
**Confira:** as taxas por grupo com poucas propostas (3 de êxito) não provam nada; olhe o tamanho da
amostra.

### Clientes 07 · Confirmação de contratação em linguagem simples
**Quando usar:** logo depois de assinar o contrato, para o cliente saber como funciona o dia a dia:
canal, prazo de resposta, parcelas, o que ele precisa mandar. O contrato continua sendo o que vale.
**Cole:** Planilha 13 · aba Casos (valor), Planilha 14 · aba Parcelas (parcelas e datas) e Planilha 7 · aba
Proposta (o que foi combinado).

```
Escreva um e-mail de boas-vindas de até 200 palavras para [Cliente A], pessoa [física/jurídica], que acabou de contratar o escritório para [serviço em uma frase]. Conteúdo: quem é o responsável e quem mais atende; canal e prazo de resposta ([ex.: WhatsApp do escritório, resposta em 1 dia útil]); as parcelas ([n] de R$ [ ], vencendo dia [ ] de cada mês, por [Pix/boleto]); o que precisamos que o cliente envie até [data] (lista curta, sem justificar); como ele vai ser informado do andamento. Tom acolhedor e direto, sem promessa de resultado, sem prazo de conclusão e sem explicar o caso. Diga que o contrato assinado é o que vale em caso de dúvida.
```
**Exemplo:** Entrada: Cliente I (Clínica Bem-Estar), pessoa jurídica, consultoria mensal; responsável Marina,
Júlia auxilia; WhatsApp do escritório, 1 dia útil; 6 parcelas de R$ 1.550 no dia 10 por Pix; enviar
contrato social e últimos contratos com fornecedores até 20/09. Saída: e-mail de 180 palavras com
os cinco pontos e a frase final sobre o contrato.
**Confira:** parcelas, datas e a lista de documentos, que é sua; a IA não deve acrescentar nada nela.

### Clientes 08 · Encerramento do caso e pedido de avaliação
**Quando usar:** quando o checklist de encerramento da Planilha 4 estiver completo (última parcela
recebida, documentos devolvidos). Fecha bem e pede a avaliação sem constranger.
**Cole:** Planilha 4 · aba Checklist (colunas de encerramento) e a Planilha 13 · aba Casos (situação
financeira do caso).

```
Escreva duas mensagens para [Cliente A], cujo caso com o escritório foi encerrado: 1) encerramento, até 120 palavras: agradece, confirma que não há valores pendentes (ou informa a última parcela em aberto de R$ [ ] com vencimento em [ ]), diz como o cliente recebe os documentos de volta e por quanto tempo o escritório guarda uma cópia ([prazo que o escritório definiu]), e deixa a porta aberta; 2) pedido de avaliação, até 60 palavras, enviado uma semana depois, com o link [ ] e a frase de que a avaliação é opcional e pode ser sobre o atendimento, não sobre o resultado. Não comente o resultado do caso nem use palavras como "vitória" ou "ganhamos".
```
**Exemplo:** Entrada: Cliente F (Fernanda Castro, família, encerrado em abril), sem pendências, documentos
devolvidos em mãos, cópia guardada pelo prazo definido no guia LGPD do escritório. Saída: duas
mensagens, a primeira com 110 palavras e a segunda com 55, nenhuma mencionando o resultado.
**Confira:** o prazo de guarda que você escreveu no guia LGPD (bônus 23) e a pendência financeira.

---

## Grupo 5 · Painel e sócios (8)

### Painel 01 · Explicar o mês ao sócio
**Quando usar:** na sexta de fechamento, com o Painel do escritório e o Resumo do mês. É o prompt
mais usado do kit.
**Cole:** Planilha 20 · aba Resumo ("Bloco único para copiar"), que reúne prazos, horas, caixa,
recebíveis e propostas do mês.

```
Explique o mês de um escritório de advocacia para o meu sócio, em até 250 palavras e linguagem direta. Use só os números abaixo. Estrutura: uma frase com o resultado do mês; prazos (quantos cumpridos, quantos atrasaram, o padrão); horas (gastas × faturáveis por pessoa, o caso que mais consumiu); caixa (entrou, saiu, sobrou, provisão feita); recebíveis (a receber, atrasado); propostas (enviadas, fechadas, abertas); uma decisão para o mês que vem. Onde faltar explicação, escreva "[explicar]" para eu preencher. Não comente o mérito de nenhum caso.
Meus comentários: [o que aconteceu, por quê].
Números:
[cole o bloco da aba Resumo]
```
**Exemplo:** Entrada: o Resumo de setembro da Ferraz & Lima (56 prazos, 9 atrasados; Marina 98 h, Rafael
104 h, Júlia 52 h; entrou R$ 31.400, saiu R$ 21.900, provisão R$ 1.884; a receber R$ 128.280, atrasado
R$ 3.090; 7 propostas enviadas, 4 fechadas, 5 abertas); comentário: "o acordo do Cliente H entrou;
setembro teve 3 audiências na mesma semana". Saída: texto de 240 palavras com um "[explicar]" nos
9 prazos atrasados e a decisão: "mover as tarefas curtas para quarta".
**Confira:** cada "[explicar]" e se nenhum número foi alterado.

### Painel 02 · Relatório mensal para os sócios
**Quando usar:** para a reunião de sócios, em vez do texto corrido do Painel 01: formato de relatório,
com destaques, atenções e próximos passos.
**Cole:** Planilha 20 · aba Resumo e a Planilha 18 · aba Resultado (mês e mês anterior).

```
Escreva o relatório mensal de gestão de um escritório de advocacia para os sócios, em até 300 palavras, com a estrutura: Resultado do mês em uma frase (com o resultado do mês anterior ao lado); Destaques (3 tópicos com número); Pontos de atenção (até 3, com causa provável e ação); Próximos passos (3, com responsável e prazo). Tom profissional e direto, sem jargão contábil. Use apenas os números abaixo; onde faltar explicação, escreva "[explicar]". Nada sobre o mérito dos casos.
Meus comentários: [o que aconteceu].
Números:
[cole o bloco da aba Resumo e as duas colunas do Resultado]
```
**Exemplo:** Entrada: setembro e agosto da Ferraz & Lima; comentário: "o acordo do Cliente H é entrada
extraordinária". Saída: relatório de 280 palavras: resultado R$ 9.500 (agosto: R$ 4.500), destaques
(inadimplência caiu 25%, 4 propostas fechadas, 2 casos encerrados), atenções (12 casos acima das horas
estimadas; R$ 50.900 presos em êxito; um "[explicar]" nos prazos) e próximos passos com dono.
**Confira:** que o "extraordinário" apareça como tal e não como tendência.

### Painel 03 · Roteiro de 8 slides para a reunião de sócios
**Quando usar:** com o modelo de apresentação "Resultado do mês para os sócios" do kit (8 slides).
**Cole:** Planilha 20 · aba Resumo e os comentários do Painel 01.

```
Monte o roteiro de uma apresentação de 8 slides sobre o mês de [mês] de um escritório de advocacia, para os sócios, usando só os números abaixo. Para cada slide: título em uma frase que já diga a conclusão; 3 tópicos curtos; o número ou gráfico em destaque; uma frase do que eu falo. Estrutura: 1 capa; 2 resumo do mês; 3 prazos e rotina; 4 horas e casos que mais consomem; 5 caixa e provisão; 6 recebíveis e inadimplência; 7 propostas e carteira; 8 decisões que precisamos tomar. Onde faltar explicação, escreva "[explicar]". Nada sobre o mérito dos casos.
Meus comentários: [o que aconteceu].
Números:
[cole]
```
**Exemplo:** Entrada: setembro da Ferraz & Lima e os comentários do Painel 01. Saída: 8 slides; slide 4
"Doze casos já passaram das horas estimadas; o Cliente A consome 74 h sem nada recebido"; slide 8 com
duas decisões: reserva de R$ 3.000 e nova regra de 1,2× nas estimativas empresariais.
**Confira:** cada "[explicar]"; o slide 8 precisa ter decisões de verdade, não "alinhar".

### Painel 04 · Perguntas difíceis que o sócio vai fazer
**Quando usar:** na véspera da reunião de sócios, para não ser pego de surpresa.
**Cole:** o relatório do Painel 02 ou o roteiro do Painel 03.

```
Com base no relatório abaixo, liste as 8 perguntas mais prováveis que um sócio cético faria e uma resposta curta e honesta para cada, incluindo o que dizer quando eu não souber ("não tenho o dado agora; trago até sexta"). Marque as 3 mais difíceis. As perguntas devem ser de gestão (dinheiro, horas, prazos, clientes), não sobre o mérito dos casos.
Relatório:
[cole]
```
**Exemplo:** Entrada: o relatório de setembro do Painel 02. Saída: 8 perguntas ("por que 12 casos passaram
das horas?", "quanto do a receber é êxito que pode nunca vir?", "a provisão cobre dezembro?"), respostas
curtas e as três mais difíceis marcadas.
**Confira:** as respostas devem ser as suas; use as da IA como rascunho.

### Painel 05 · Meta realista para o trimestre
**Quando usar:** no início do trimestre, com o histórico dos últimos meses, para preencher a Planilha 19.
**Cole:** Planilha 18 · aba Resultado (receita e resultado dos últimos 6 meses) e a Planilha 15 (propostas
abertas).

```
Com o histórico abaixo de um escritório de advocacia, sugira metas para o próximo trimestre em três cenários (conservador, provável, ambicioso) para: receita recebida, resultado, propostas fechadas e inadimplência. Explique o cálculo de cada um (média, tendência, sazonalidade, propostas abertas). Diga o que precisaria acontecer para o ambicioso e o que ameaça o conservador. Não conte com êxito sem data no cenário provável.
Histórico mês a mês:
[cole]
Propostas abertas: [valor e quantidade]
```
**Exemplo:** Entrada: receita de abril a setembro (R$ 24.100, 27.300, 25.800, 29.400, 26.800, 31.400),
resultado, 5 propostas abertas somando R$ 41.500. Saída: receita mensal conservadora em torno de
R$ 26.000, provável R$ 28.500, ambiciosa R$ 32.000 (com metade das propostas abertas fechando), e a
ameaça ao conservador: "dezembro costuma ter menos recebimento".
**Confira:** a sazonalidade que você conhece (recesso, férias); a IA só viu seis meses.

### Painel 06 · Meta × realizado: explicar o desvio
**Quando usar:** no meio e no fim do trimestre, com a Planilha 19 mostrando o ritmo da meta.
**Cole:** Planilha 19 · aba Metas (meta, realizado até hoje, ritmo necessário, dias restantes).

```
Compare meta e realizado do trimestre de um escritório de advocacia. Para cada meta: % atingido, % do tempo decorrido, ritmo necessário por semana até o fim e se está "no ritmo", "atrás" ou "à frente". Depois: as duas metas mais atrás e, para cada uma, três causas possíveis de gestão e uma ação para as próximas duas semanas. Separe "o que os números mostram" de "hipóteses". Nada sobre o mérito dos casos.
Metas:
[cole]
Hoje é [data]; o trimestre vai de [data] a [data].
```
**Exemplo:** Entrada: 14/09/2026, trimestre de julho a setembro; receita meta R$ 90.000, realizado R$ 71.200;
propostas fechadas meta 15, realizado 12; inadimplência meta abaixo de R$ 3.000, realizado R$ 3.090.
Saída: receita a 79% com 83% do tempo (quase no ritmo; faltam R$ 18.800, cerca de R$ 8.200 por semana), propostas a 80%
(atrás), inadimplência quase na meta; ações para as duas semanas.
**Confira:** a conta do ritmo por semana; refaça você.

### Painel 07 · Contratar, associar ou não: os números antes da decisão
**Quando usar:** antes de contratar alguém, associar um advogado ou pagar um freelancer fixo. Não
decide; organiza a conta.
**Cole:** Planilha 17 · aba Painel (horas × faturáveis por pessoa, casos ativos, caixa, reserva) e a
Planilha 5 (custo fixo).

```
Vou tomar a decisão: [ex.: contratar um advogado júnior por R$ 3.500 por mês com encargos / associar um advogado por percentual / manter como está]. Com os dados abaixo de um escritório de advocacia, liste: 1) o que os dados sustentam; 2) o que eles NÃO respondem; 3) o custo mensal total da decisão e quantas horas faturáveis a mais ela precisa gerar para se pagar (custo ÷ valor médio por hora faturada); 4) cinco perguntas que eu deveria responder antes de decidir; 5) o pior cenário realista e como me proteger dele; 6) uma versão menor ou reversível da mesma decisão. Não me diga o que decidir.
Dados:
[cole]
```
**Exemplo:** Entrada: "contratar um advogado júnior por R$ 3.500 com encargos"; Marina a 98 h de 110,
Rafael a 104 de 110, Júlia a 52 de 60; 30 casos ativos; caixa R$ 21.000; reserva R$ 14.000; valor
médio por hora faturada R$ 105. Saída: os dados sustentam que os sócios estão no limite; não respondem
se a demanda continua; custo total cerca de R$ 4.900; precisa de 47 h faturáveis a mais por mês;
versão reversível: freelancer por caso por três meses.
**Confira:** o valor médio por hora faturada (Planilha 16) e os encargos, que a IA chuta.

### Painel 08 · Segunda opinião sobre uma decisão do escritório
**Quando usar:** antes de uma decisão de gestão que custa dinheiro ou é difícil de desfazer: mudar de
sala, assinar um software, dar desconto grande, encerrar uma área de atuação.
**Cole:** o que for relevante do Painel da Planilha 17; sem nomes.

```
Vou tomar a decisão de gestão: [descreva]. Meus motivos: [liste]. Faça o papel do advogado do diabo: os três melhores argumentos contra, o que eu posso estar ignorando, e uma versão menor ou reversível da mesma decisão. Depois, diga honestamente se os argumentos contra são fortes ou fracos. Não entre em nenhuma questão jurídica da decisão (contrato, ética, regulamentação): isso é comigo.
Dados de apoio:
[cole]
```
**Exemplo:** Entrada: "assinar um software jurídico de R$ 400 por mês; motivos: publicações automáticas,
os sócios perdem tempo conferindo diário". Saída: três argumentos contra (custo anual de R$ 4.800 equivale
a 73 horas de custo do escritório; a rotina de segunda já confere; o problema pode ser de disciplina,
não de ferramenta), o que estou ignorando (o teste gratuito), versão reversível (assinar por três meses
com data de revisão) e o veredito.
**Confira:** a decisão continua sua. Se ela envolve regra da OAB ou contrato, é assunto do seu jurídico,
não da IA.

---

## Modelo em branco para criar os seus

```
Papel: você é [assistente de gestão de um escritório de advocacia; não dá orientação jurídica].
Contexto: [quem sou, para quem é, o que já tenho].
Tarefa: [o que fazer, em uma frase].
Formato: [tabela, lista, e-mail, até N palavras].
Regras: [o que não fazer; marque dúvidas com colchetes; use só os dados colados].
Dados (sem nomes reais, sem número de processo real):
[cole]
```
**Exemplo:** Entrada: sócio da Ferraz & Lima; explicar à estagiária como preencher a aba Horas toda
sexta; formato: passo a passo de 8 itens. Saída: lista de 8 passos com o que lançar, em que unidade e
o que fazer quando não souber a qual caso a hora pertence.

Suporte: suporte@seusociogestor.com.br · Reembolso em até 7 dias.
