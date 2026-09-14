# Biblioteca de prompts da clínica · Kit de Gestão para Médicos

Versão 1.0 · setembro de 2026 · Seu Sócio Gestor

41 prompts em 5 grupos, um para cada núcleo do kit: Agenda, Preço, Caixa, Recebíveis e Painel. São oito por grupo; o de Caixa tem nove, porque o dinheiro pede uma pergunta a mais.
Cada um tem: quando usar, de qual planilha vem o bloco a colar, o prompt pronto (troque o que está
entre colchetes), um exemplo com a clínica fictícia e o que conferir na resposta. Funcionam no
ChatGPT, no Copilot, no Gemini e no Claude, inclusive nas versões gratuitas.

## Regra de ouro: o que nunca entra em uma IA pública

**Nunca cole nome de paciente, contato, CPF, número de carteirinha, número de guia com nome, e
nenhuma informação de saúde: motivo da consulta, diagnóstico, exame, prescrição, prontuário.** Dado
de saúde é dado pessoal sensível pela LGPD (art. 5º, II) e o sigilo profissional é seu; a IA
pública não tem dever de sigilo e pode guardar o que recebe. Antes de colar, troque por "Paciente
A", "Paciente B", "Convênio 1", "Convênio 2" e deixe só o que é gestão: procedimento (o nome
administrativo), valor, data, pagador, situação. Na prática: copie o bloco da planilha para um
texto, troque a coluna Paciente por letras na ordem em que aparecem, apague contato e número de guia
e leia uma vez procurando nome próprio antes de colar.

Mais três regras:

1. **Nenhum prompt aqui produz conteúdo clínico nem peça de divulgação.** Nada de conduta,
   diagnóstico, laudo, orientação ao paciente sobre saúde ou texto para redes sociais, site e
   anúncio. São prompts de gestão da clínica: explicar o mês ao sócio, escrever a cobrança educada,
   resumir os convênios, preparar a reunião com o contador, revisar a tabela de preços, montar a
   rotina da recepção. A medicina continua sendo feita por quem tem CRM; a divulgação segue as
   regras do CFM (Resolução CFM 2.336/2023) e do seu CRM, e este kit não redige nenhuma.
2. **A IA erra com confiança.** Todo número, data e conclusão precisa ser conferido na planilha
   antes de virar mensagem, tabela de preços ou decisão. Cada prompt diz o que revisar.
3. **Contexto é o segredo.** Diga quem lê, para quê e o que você já tem. Por isso os prompts
   começam com o papel e o contexto.

Como usar: copie o prompt inteiro, cole na IA, substitua os colchetes, cole o bloco da planilha
onde indicado e envie. Se a resposta vier ruim, não reescreva o prompt: responda "Refaça: [o que
faltou]".

Sobre os exemplos: usam a clínica fictícia do kit, Clínica Vida Plena (dois sócios, a Dra. Carolina
Mendes, clínica médica, e o Dr. Paulo Andrade, cardiologia; uma médica parceira por repasse, a Dra.
Renata Sousa, endocrinologia; a recepcionista Bruna Carvalho; três convênios fictícios: Saúde Total,
MediPlan e Vida Care), na mesma data das 20 planilhas: segunda-feira 14/09/2026, com a agenda e o
caixa de setembro em andamento e agosto como último mês fechado. Os números são os que aparecem nas
planilhas. Para você reconhecer as linhas, os exemplos citam os nomes inventados da planilha; no
bloco colado na IA, eles já viraram Paciente A, B, C.

Os prompts têm o número com que as planilhas os citam na aba "Como usar": Agenda, Preço, Recebíveis
e Painel vão de 01 a 08, e o grupo Caixa, de 01 a 09.

## De onde vem cada bloco

| Planilha do kit | Aba que você copia | Usada nos prompts |
|---|---|---|
| 1 Agenda e ocupação | Painel (tabelas por profissional, sala, dia e período; próximos 7 dias) | Agenda 01, 07, Preço 08, Caixa 07, Painel 07 |
| 2 Faltas e retornos | Painel (por dia, pagador, profissional; lista de retorno sem nomes) | Agenda 02, 03, 07 |
| 3 Rotina da semana | Rotina e Painel ("Por rotina") | Agenda 05, 07, 08 |
| 4 Checklist do dia | Painel ("O que faltou") | Agenda 06 |
| 5 Custo da hora de atendimento | Painel ("Como chegamos ao número"), Custos fixos, Equipe | Preço 01, Caixa 03, Painel 07 |
| 6 Precificação | Precificação (a tabela e o bloco Simular) | Preço 02, 05 |
| 7 Simulador convênio × particular | Simulador (quadros 2, 3 e 4) | Preço 03, 06, 08 |
| 8 Tabela de preços | Tabela e "Valor por hora por pagador" | Preço 04, 06, 07 |
| 9 Caixa da clínica | Painel ("Para onde foi", "De onde veio", "O ano mês a mês") | Caixa 01, 03, 08 |
| 10 Provisão de impostos, 13º e férias | Painel | Caixa 04, 05 |
| 11 Repasse e pró-labore | Painel ("Médicos parceiros", "Sócios no ano") | Caixa 07, Painel 07 |
| 12 Reserva e metas de caixa | Painel | Preço 08, Caixa 08 |
| 13 Convênios a receber | Painel ("Por convênio", "Lotes em aberto", guias glosadas sem nomes) | Preço 06, Recebíveis 01, 03, 08 |
| 14 Parcelas e inadimplência | Painel ("Cobrar primeiro", sem nomes; a régua está em Config) | Recebíveis 02, 04, 06, 07 |
| 15 Orçamentos | Painel (funil, motivos de recusa, por tipo) | Agenda 04, Preço 07, Recebíveis 05, Painel 05 |
| 16 Conciliação de cartão | Painel ("Por tipo de pagamento") | Caixa 09 |
| 17 Painel da clínica | Painel e Histórico | Agenda 08, Painel 05, 07, 08 |
| 18 Resultado mensal | Painel e Resultado (mês e mês anterior) | Caixa 02, Painel 02, 05 |
| 19 Metas do trimestre | Metas ("Todos os resultados-chave") | Painel 06 |
| 20 Resumo do mês | Resumo ("Bloco único para copiar") | Caixa 04, Painel 01, 02, 03 |

---

## Grupo 1 · Agenda e rotina (8)

### Agenda 01 · Onde a agenda esvazia
**Quando usar:** na segunda de manhã, com o Painel da Agenda aberto, quando a ocupação do mês está
abaixo da meta e você quer saber em que dia, período, sala ou profissional o buraco aparece.
**Cole:** Planilha 1 · aba Painel, as tabelas "Por dia da semana e período" e "Por profissional" (só
totais; nenhum nome de paciente).

```
Você é meu assistente de gestão de uma clínica médica pequena. Não comente nenhum atendimento, diagnóstico ou paciente: só os números da agenda. Vou colar duas tabelas do mês: ocupação por dia da semana e período (horas disponíveis, atendidas, ocupação, faltas) e por profissional (horas disponíveis, atendidas, ocupação, realizados, faltas, produção). Nossa meta de ocupação é [75] %.
Responda: 1) onde a agenda esvazia (os três piores cruzamentos de dia × período ou profissional, com o número); 2) quantas horas vazias por semana isso representa e quanto custam, se um horário vazio de 30 minutos custa R$ [100] (planilha 05); 3) hipóteses de gestão, separadas de "o que os dados mostram" (turno mal posicionado, falta concentrada, sala ociosa, retorno não agendado); 4) três ajustes de agenda simples para testar por quatro semanas e o que medir. Não sugira captar pacientes nem fazer divulgação: a decisão é da clínica.
Dados:
[cole as duas tabelas]
```
**Exemplo:** Entrada: setembro da Clínica Vida Plena até 11/09: 64 horas disponíveis, 51,8 atendidas,
ocupação 81 %, 12,2 horas vazias; sexta de manhã com 65 % de ocupação e 2 faltas, quinta à tarde com
73 %; Dr. Paulo Andrade com 66 % (15,8 de 24 horas) e 4 faltas, Dra. Carolina Mendes com 92 %, Dra.
Renata Sousa com 88 %; Sala 2 com 66 % e 8,2 horas vazias. Saída: os três piores cruzamentos (sexta
manhã, quinta tarde na Sala 2, Dr. Paulo no geral), 12,2 horas vazias no mês, cerca de R$ 2.440 de
estrutura parada, hipótese "as faltas de sexta de manhã são de pacientes de convênio marcados sem
confirmação de véspera" e o ajuste: "confirmar na quinta à tarde os horários de sexta e oferecer as
vagas de sexta à lista de retorno na segunda".
**Confira:** as horas vazias do Painel (a IA gosta de arredondar) e se a hipótese cabe no que você
sabe da agenda. Ajustar turno é decisão sua e do profissional.

### Agenda 02 · Reduzir faltas sem brigar com o paciente
**Quando usar:** quando a taxa de falta do mês passa da meta, para achar o padrão (dia, pagador,
profissional) e montar uma rotina de confirmação, não uma política de punição.
**Cole:** Planilha 2 · aba Painel, as tabelas "Por dia da semana", "Por pagador" e "Últimas 8 semanas".

```
Sou dono de uma clínica médica pequena e quero reduzir faltas sem constranger paciente. Vou colar a taxa de falta do mês por dia da semana, por pagador e a série das últimas 8 semanas. Não comente saúde de ninguém; é só gestão de agenda.
Responda: 1) onde a falta se concentra (dia, período, pagador), com o número; 2) o que os dados mostram e o que é hipótese; 3) uma rotina de confirmação em três passos (quando confirmar, por qual canal, o que fazer com quem não responde) que a recepção consiga fazer em 10 minutos por dia; 4) o que medir nas próximas 4 semanas para saber se funcionou. Regras: nada de multa, lista negra ou mensagem que exponha o paciente; nada que pareça divulgação da clínica.
Dados:
[cole as tabelas]
```
**Exemplo:** Entrada: setembro da Vida Plena: 6 faltas em 113 horários (5,3 %); sexta com 15,4 % (2
faltas em 13), terça 4,7 %, quinta 5,0 %; Vida Care com 12,5 % e Saúde Total com 7,1 %, particular
3,5 %; Dr. Paulo Andrade com 10 % (4 faltas); série das 8 semanas caindo de 10,9 % (S27/07) para 4,0 %
(S31/08) e 5,8 % (S07/09), desde que a recepção começou a confirmação de véspera por mensagem. Saída:
"a falta caiu pela metade depois da confirmação de véspera; sobrou a sexta de manhã e o convênio
Vida Care"; rotina em três passos (mensagem de véspera às 16h, ligação para quem não respondeu até as
18h, horário oferecido à lista de retorno se cancelar) e a medição: taxa de falta de sexta e do Vida
Care nas próximas 4 semanas.
**Confira:** a série semanal (a IA tende a ler tendência onde há só duas semanas boas) e se a rotina
cabe no tempo da recepção. O texto da mensagem de véspera está no bônus 22 (modelo 02).

### Agenda 03 · Mensagem de retorno educada
**Quando usar:** com a lista de retorno da Planilha 2 na tela: pacientes que passaram do retorno
previsto e não têm horário marcado. O prompt escreve a mensagem administrativa de lembrete de
agendamento, sem falar de saúde.
**Cole:** Planilha 2 · aba Painel, a "Lista de retorno" sem nomes (profissional, pagador, procedimento
do último atendimento, retorno previsto, dias além).

```
Escreva uma mensagem de WhatsApp de até 60 palavras para a recepção de uma clínica médica lembrar um paciente de agendar o retorno previsto com [Dr./Dra. Nome], que estava indicado para [mês]. Regras: a mensagem é administrativa (agenda), não fala do motivo da consulta, de exame, de sintoma nem de resultado; não usa palavras que sugiram urgência ou medo; oferece dois horários concretos ([dia e hora], [dia e hora]) e um caminho fácil de resposta; diz que, se o paciente já agendou em outro lugar ou não quer retorno agora, basta responder para a clínica atualizar o cadastro. Tom educado e curto. Depois, uma segunda versão para e-mail, com assunto. Nada de texto de divulgação da clínica.
```
**Exemplo:** Entrada: os 7 pacientes da lista de retorno da Vida Plena em 14/09 (5 do Dr. Paulo
Andrade, 1 da Dra. Carolina Mendes, 1 da Dra. Renata Sousa; de 1 a 37 dias além do previsto), com as
vagas da semana do Painel da 01 (segunda 1,3 h, terça 1,3 h, quinta 2,8 h). Saída: mensagem de 55
palavras ("o retorno com o Dr. Paulo estava previsto para agosto; temos horário na quinta às 15h ou às
16h30; se preferir outro dia ou já tiver resolvido, é só responder") e a versão de e-mail.
**Confira:** que nenhuma frase fale de saúde ou pressione ("é importante para o seu tratamento" está
fora). Retorno é decisão clínica do profissional; a recepção só oferece o horário. Se a mensagem for
usada para um grupo grande de pacientes, revise pelas regras do CFM/CRM antes de usar.

### Agenda 04 · Mensagem de retomada de orçamento
**Quando usar:** com a lista "Retomar contato primeiro" da Planilha 15: orçamento apresentado ou em
análise, parado há mais dias que o limite. Uma mensagem para perguntar se ficou dúvida, sem
insistência e sem promessa.
**Cole:** Planilha 15 · aba Painel, a linha do orçamento sem nome (itens, valor, etapa, dias em aberto,
profissional).

```
Escreva uma mensagem de WhatsApp de até 60 palavras para a recepção de uma clínica médica retomar contato sobre um orçamento apresentado há [dias] dias: [itens, ex.: MAPA + Holter], no valor de R$ [ ], com [Dr./Dra. Nome]. Objetivo: perguntar se ficou alguma dúvida sobre valores, formas de pagamento ou agenda, e oferecer a conversa com a recepção. Regras: não fale do motivo do exame nem de saúde; não diga que o exame é necessário ou urgente; não ofereça desconto; sem tom de venda e sem frase de divulgação da clínica; deixe claro que o paciente pode responder "não agora" e a clínica atualiza o cadastro. Depois, uma versão de e-mail com assunto.
```
**Exemplo:** Entrada: o orçamento em análise há 12 dias de MAPA + Holter, R$ 650, com o Dr. Paulo
Andrade (Mariana Reis na planilha; na IA, Paciente A). Saída: mensagem de 50 palavras ("ficou alguma
dúvida sobre valores ou formas de pagamento? Podemos parcelar em 2 vezes e há vaga na próxima semana;
se preferir deixar para depois, é só avisar") e a versão de e-mail.
**Confira:** parcelamento e vagas que a recepção pode oferecer de verdade; a IA inventa condições.
Se o paciente disser não, registre o motivo na Planilha 15 (é a parte mais valiosa dela).

### Agenda 05 · Rotina da recepção em 30 minutos por semana
**Quando usar:** na primeira semana com o kit, para montar a rotina de segunda (agenda, faltas,
retornos) e de sexta (caixa, guias, orçamentos e painel) do jeito da sua clínica. Depois, quando
mudar a equipe ou os turnos.
**Cole:** Planilha 3 · aba Rotina (as linhas de segunda e de sexta do exemplo, para adaptar) e a tabela
"Por rotina" do Painel.

```
Monte a rotina semanal de gestão de uma clínica médica com [quantas pessoas: ex.: dois sócios, uma médica parceira e uma recepcionista]. Dois blocos: segunda-feira (agenda, confirmações, faltas e lista de retorno), de no máximo 12 minutos, e sexta-feira (caixa, guias de convênio, parcelas, orçamentos e painel), de no máximo 18 minutos. Para cada bloco: os passos em ordem, quem faz (recepção ou sócio), quantos minutos e qual planilha abre (use os nomes abaixo). Corte tudo que não cabe no tempo e diga o que ficou de fora e em que dia do mês seria feito.
Planilhas que temos: Agenda e ocupação, Faltas e retornos, Checklist do dia, Caixa da clínica, Convênios a receber, Parcelas e inadimplência, Orçamentos, Painel da clínica.
Nossas particularidades: [ex.: a recepção fecha o caixa todo dia; o lote de convênio sai dia 5; o Dr. Paulo só está na clínica à tarde].
Rotina de exemplo para adaptar:
[cole as linhas da aba Rotina]
```
**Exemplo:** Entrada: dois sócios, uma parceira, uma recepcionista; caixa fechado todo dia pela
recepção; lote de convênio dia 5; a rotina de exemplo do kit (3 passos de segunda com a recepção, 5
de sexta; o exemplo registra da semana 29 (20/07) em diante, com 84 % de aderência nas últimas 4
semanas, e a rotina mais pulada é "conferir os fechamentos da semana no Caixa (09)", feita em 2 de 4
semanas). Saída: segunda com 3 passos em 12 minutos (vagas dos próximos 7 dias, confirmações da
semana, lista de retorno e faltas da semana passada) e sexta com 5 passos em 18 minutos (conferir no
caixa os fechamentos do dia que a recepção lançou, parcelas e cobrança, guias e lotes, orçamentos,
painel com 3 decisões); a conciliação do cartão ficou para a sexta seguinte, alternando.
**Confira:** se a soma dos minutos bate e se a IA não inventou uma planilha que o kit não tem. Toda
rotina precisa de dono: no exemplo, a mais pulada é justamente a única que não é da recepção.

### Agenda 06 · Pendências do dia viram tarefas da recepção
**Quando usar:** quando o Painel da Planilha 4 mostra o mesmo item de fechamento pendente em vários
dias (caixa não conferido, guias não separadas, retornos não agendados).
**Cole:** Planilha 4 · aba Painel, "Dias com pendência" (data, dia, % abertura, % fechamento, o que
faltou) e "Item mais esquecido".

```
Transforme a lista de pendências administrativas abaixo, de uma clínica médica, em tarefas para a recepção. Cada linha vem como: data | dia da semana | % da abertura feita | % do fechamento feito | o que faltou. Agrupe por tipo de pendência (caixa, guias de convênio, agenda e situação dos horários, retornos, troco e maquininha), escreva uma tarefa por grupo com verbo no infinitivo, diga em que momento do dia ela cabe (antes do primeiro paciente, na hora do almoço, depois do último) e sugira um jeito de a tarefa não depender de memória (lembrete, ordem fixa, item impresso). Não culpe ninguém: descreva a rotina, não a pessoa. Nada sobre pacientes ou atendimentos.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: os 32 dias com pendência da Vida Plena (73 dias registrados de 01/06 a 11/09;
abertura completa em 80 % dos últimos 20 dias, fechamento em 55 %; 46 itens pendentes; o mais
esquecido: "Fechamento do dia lançado no Caixa (09)"; depois "Caixa do dia fechado e conferido (Pix,
cartão, dinheiro)" e "Guias do dia conferidas e guardadas para o lote"). Saída: quatro tarefas
("lançar o fechamento no Caixa (09) com a planilha aberta na tela, antes de sair", "fechar e conferir
o caixa antes de desligar a maquininha", "guias na pasta do lote ao fim de cada turno", "retornos
agendados na saída do paciente"), o momento de cada uma e a sugestão: imprimir o checklist de
fechamento (bônus 25) e deixar ao lado do computador da recepção.
**Confira:** o que é de fato responsabilidade da recepção e o que o sócio precisa fazer. No exemplo,
quem lança o fechamento do dia no Caixa (09) é a recepção, todo dia; a sócia da semana é quem confere
na sexta (saldo, A receber e extrato).

### Agenda 07 · Pauta da reunião de segunda com a recepção
**Quando usar:** para a conversa de 12 minutos de segunda entre o sócio da semana e a recepção, com
os números da semana na mão.
**Cole:** Planilha 1 · aba Painel, "Próximos 7 dias" (agendados, confirmados, vagas) e os cartões do
Painel da Planilha 2 (taxa de falta, lista de retorno); Planilha 3 · Rotina (linhas de segunda).

```
Monte a pauta de uma reunião de 12 minutos de segunda-feira entre o sócio e a recepção de uma clínica médica. Objetivo: todo mundo sair sabendo o que confirmar, o que oferecer e o que travou. Estrutura: 1) números da semana (horários agendados × confirmados por dia, vagas, faltas da semana passada, lista de retorno); 2) o que ficou pendente na semana passada (checklist do dia) e como resolver, sem culpa; 3) quem confirmar hoje e quais vagas oferecer à lista de retorno; 4) pendências com pacientes (parcela em aberto, orçamento sem resposta), sem nomes; 5) uma decisão que precisa ser tomada hoje. Diga quantos minutos cada item leva. Nada clínico.
Dados:
[cole aqui]
```
**Exemplo:** Entrada: semana de 14/09 da Vida Plena: quinta 17/09 com 19 agendados e nenhum
confirmado (2,8 horas de vaga), sexta com 9 agendados e 0,5 hora de vaga; 6 faltas em setembro, 7
pacientes na lista de retorno; 2 dias da semana passada com fechamento incompleto; 6 orçamentos em
aberto (R$ 3.460); decisão: oferecer as vagas de quinta à lista de retorno ou segurar para encaixe.
Saída: pauta de cinco itens em 12 minutos, com o item 3 marcado como "confirmar os 19 de quinta até
quarta à tarde" e o item 5 como "decidir hoje".
**Confira:** só o que está na planilha; a IA gosta de acrescentar itens genéricos ("alinhamento de
equipe"). Nomes de pacientes ficam na planilha, não na pauta.

### Agenda 08 · Semana revisada na sexta
**Quando usar:** na sexta, no fechamento, com o que foi feito e o que ficou. Alimenta a rotina da
semana seguinte e a conversa com o sócio.
**Cole:** Planilha 3 · aba Rotina (linhas de sexta, o que foi feito e o que ficou) e os cartões do
Painel da Planilha 17.

```
Faça a revisão semanal de uma clínica médica pequena. Com a lista abaixo (horas atendidas e vazias, faltas, o que entrou de dinheiro, lotes de convênio enviados ou pagos, parcelas cobradas, orçamentos aprovados, o que da rotina não foi feito), responda: 1) o que andou de mais importante; 2) o que travou e a causa provável de gestão (não de atendimento); 3) três ajustes simples para a próxima semana; 4) uma mensagem de duas linhas que eu possa mandar para [o sócio / a equipe] resumindo a semana. Tom direto, sem elogio vazio. Não comente nenhum atendimento nem paciente.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: semana de 7 a 11/09 da Vida Plena: 49 atendimentos realizados e 3 faltas (5,8
%), feriado na segunda 07/09; R$ 21.920 entrados em setembro até sexta; lote de julho da Saúde Total
pago em 08/09 (R$ 5.780, glosa R$ 170) e os três lotes de agosto enviados em 08/09 (R$ 9.631); lote de
junho da Vida Care atrasado desde 04/09 (R$ 1.727); 14 parcelas vencidas (R$ 3.775); 6 orçamentos
aprovados na semana (R$ 2.350); a rotina "atualizar os orçamentos apresentados e aprovados (15)" não
foi feita. Saída: os quatro blocos, causa provável do que travou ("a sexta ficou apertada com os três
lotes de agosto e a atualização dos orçamentos foi a primeira a cair"), ajuste "atualizar os
orçamentos na quinta, quando a sexta tiver envio de lote" e a mensagem pronta para o sócio.
**Confira:** a causa provável é hipótese; a IA não viu a semana.

---

## Grupo 2 · Preço e convênio (8)

### Preço 01 · Entender o custo da minha hora
**Quando usar:** logo depois de preencher a Planilha 5 pela primeira vez, quando o número aparece e
você quer saber se faz sentido e o que muda se mexer em alguma coisa.
**Cole:** Planilha 5 · aba Painel ("Como chegamos ao número": custos fixos, pró-labore, custo total,
horas de atendimento, custo-hora, hora mínima, custo do horário vazio) e a sensibilidade.

```
Explique para mim, médico dono de uma clínica pequena, o que o custo da hora de atendimento abaixo significa na prática, em até 200 palavras e sem jargão. Depois: 1) refaça a conta passo a passo para eu conferir; 2) diga o que acontece com o custo-hora se as horas atendidas caírem 20 % (férias, feriado, faltas); 3) diga o que acontece se eu somar [ex.: um segundo turno de recepção por R$ 2.500 com encargos]; 4) aponte o que costuma ficar de fora dessa conta em clínicas pequenas (material, retorno sem cobrança, glosa, tempo administrativo do médico). Não sugira preço de consulta nem comente tabela de convênio: isso é com a planilha 06 e com a clínica.
Números:
[cole o painel]
```
**Exemplo:** Entrada: o painel da Vida Plena: custos fixos R$ 10.000, pró-labore dos dois sócios
R$ 18.000, custo total R$ 28.000, 140 horas de atendimento planejadas no mês (70 + 70; a médica
parceira não entra, o repasse dela é custo variável), custo-hora R$ 200,00, hora mínima R$ 338,98
(arredondada para R$ 340), custo de um horário vazio de 30 minutos R$ 100. Saída: explicação em
linguagem simples ("cada hora de agenda dos sócios custa R$ 200 antes de qualquer lucro, com ou sem
paciente na sala"), a conta refeita, custo-hora subindo para R$ 250 com 20 % menos horas (112 h; a
sensibilidade da planilha mostra o mesmo, e agosto realizado deu R$ 295,67 com 94,7 h) e o alerta de
que o retorno sem cobrança já está embutido no custo da consulta na planilha 06.
**Confira:** a conta refeita, com calculadora. Se a IA chegar a outro número, o erro pode ser dela.

### Preço 02 · Revisar a tabela de preços pela margem
**Quando usar:** com a Planilha 6 preenchida, antes de mudar qualquer preço particular. É o
"advogado do diabo" da sua própria conta: onde a margem está boa, onde está fina, onde o preço
praticado é só hábito.
**Cole:** Planilha 6 · aba Precificação (procedimento, minutos, retorno, material, custo cheio, preço
mínimo, preço alvo, particular praticado, margem, situação).

```
Revise a tabela de preços particulares de uma clínica médica pela ótica da margem. Vou colar, por procedimento: minutos, se gera retorno, material, custo cheio, preço mínimo (margem mínima de [30] %), preço alvo (margem alvo de [45] %), preço praticado e margem. Impostos: [11] %.
Responda: 1) quais procedimentos estão abaixo do mínimo, entre mínimo e alvo, e no alvo ou acima; 2) para os que estão abaixo do alvo, quanto falta em reais e em %; 3) onde a margem parece alta demais para a duração (sinal de que o tempo estimado está errado, não de que o preço está alto); 4) três perguntas que eu deveria responder antes de mexer em qualquer preço. Não sugira preço com base em mercado, concorrente ou tabela de entidade: use só os meus custos. Não comente nada clínico e não escreva texto de divulgação de preços.
Tabela:
[cole aqui]
```
**Exemplo:** Entrada: os 7 procedimentos da Vida Plena com custo-hora R$ 200: consulta (30 min +
retorno embutido, custo cheio R$ 130,67, mínimo R$ 221,47, alvo R$ 296,97, praticado R$ 380, margem
54,6 %), ECG (custo R$ 74,67, mínimo R$ 126,55, alvo R$ 169,70, praticado R$ 130, margem 31,6 %), MAPA
R$ 300 (61,8 %), Holter R$ 350 (64,8 %), teste ergométrico R$ 450 (53,8 %), avaliação endócrina R$ 400
(48,0 %), retorno sem cobrança. Saída: nenhum particular abaixo do mínimo; ECG é o único entre mínimo
e alvo (faltam R$ 40 para o alvo); MAPA e Holter com margem acima de 60 % em 20 minutos ("confira se
o tempo de instalação e de laudo está nos 20 minutos"); perguntas: "o ECG é porta de entrada para a
consulta?", "quantos ECG por mês?", "o material de R$ 8 está atualizado?".
**Confira:** as duas contas de margem. E lembre que margem sobre custo cheio não é lucro líquido:
falta glosa, inadimplência, falta e hora vazia. A divulgação de preços segue as regras do CFM/CRM.

### Preço 03 · Vale a pena este convênio?
**Quando usar:** antes de renovar, aceitar ou descredenciar um convênio, com o Simulador da Planilha
7 preenchido para o procedimento mais frequente. Prepara os argumentos da conversa de tabela; a
decisão e o contrato são seus.
**Cole:** Planilha 7 · aba Simulador, quadro 2 (agenda cheia: tabela, prazo, glosa esperada, custo do
dinheiro, impostos, líquido, custo cheio, margem, líquido por hora contra a hora mínima) e quadro 3
(agenda vazia: contribuição por atendimento e por hora).

```
Ajude-me a avaliar um convênio de uma clínica médica pelos números, sem decidir por mim. Vou colar duas leituras do mesmo procedimento: com agenda cheia (o que cada pagador deixa líquido por hora, contra a hora mínima da clínica) e com agenda vazia (o que cada pagador ainda contribui além do material). Nossa ocupação atual é [ ] % e temos [ ] horas vazias por mês.
Responda: 1) em qual das duas situações a clínica está hoje e o que isso muda na leitura; 2) para cada convênio, o líquido por hora contra a hora mínima e quantos atendimentos dele equivalem a um particular; 3) três argumentos administrativos para negociar a tabela (prazo, glosa, valor por hora), com o número de cada um; 4) o que a clínica ganharia e perderia ao reduzir os horários deste convênio, em horas e em reais, sem contar com pacientes novos que não existem. Não comente nada clínico, não sugira descredenciar e não escreva texto para paciente ou divulgação.
Dados:
[cole os quadros 2 e 3]
```
**Exemplo:** Entrada: a consulta na Vida Plena: particular R$ 380 (líquido R$ 338,20; R$ 534 por
hora, +58 % contra a hora mínima de R$ 338,98); Saúde Total R$ 120 a 30 dias com 3 % de glosa
(líquido R$ 101,85; R$ 160,82 por hora, −53 %); MediPlan R$ 100 a 45 dias, 6 % (R$ 81,55; R$ 128,76,
−62 %); Vida Care R$ 90 a 60 dias, 10 % (R$ 69,66; R$ 109,99, −68 %); nenhum convênio cobre o custo
cheio de R$ 130,67; com agenda vazia, todos contribuem (3,4, 4,3 e 5,1 atendimentos para valer um
particular); ocupação de setembro 81 %, 12,2 horas vazias. Saída: "a clínica está entre as duas
leituras: Sala 1 cheia, Sala 2 com 34 % de horas vazias"; argumentos com número (prazo real do Vida
Care de 61 dias contra 60 de contrato; glosa de 11,3 % no ano; R$ 110 por hora contra R$ 339 de hora
mínima) e a conta do que muda ao tirar o Vida Care da terça à tarde.
**Confira:** as horas vazias de verdade (Planilha 1) e o contrato do convênio (prazo de aviso,
exclusividade). Descredenciamento tem regra própria; a IA não a conhece.

### Preço 04 · Revisar a tabela de preços
**Quando usar:** com a Planilha 8 preenchida com o volume do mês fechado: para saber, procedimento
por procedimento, quanto a clínica de fato recebeu por hora (misturando particular e convênio) e
onde a tabela interna precisa de revisão.
**Cole:** Planilha 8 · aba Tabela (procedimento, realizados no mês, produção, valor médio praticado,
contra o mínimo) e o quadro "Valor por hora de atendimento, por pagador".

```
Vou colar a tabela de preços de uma clínica médica com o volume do mês fechado: por procedimento, quantos foram realizados, a produção, o valor médio praticado (misturando particular e convênio) e quanto ele fica acima ou abaixo do preço mínimo; e o valor por hora que cada pagador paga, contra a hora mínima de R$ [ ] e a hora alvo de R$ [ ]. Responda: 1) quais procedimentos puxam o valor médio por hora para cima e quais puxam para baixo, com o número; 2) onde o valor médio está abaixo do mínimo por causa do mix (muito convênio) e onde é o preço particular mesmo; 3) o que mudaria no valor médio por hora se a proporção particular × convênio de [um procedimento] passasse de [ ] % para [ ] %; 4) três decisões de gestão possíveis, cada uma com o que ganha e o que perde. Não sugira preço com base em mercado; não escreva nada para divulgar.
Tabela:
[cole aqui]
```
**Exemplo:** Entrada: agosto da Vida Plena na Planilha 8: 130 consultas (R$ 30.730; valor médio
R$ 236,38, +7 % contra o mínimo de R$ 221,47), 18 ECG (valor médio R$ 78,67, −38 % contra o mínimo de
R$ 126,55), 8 MAPA (R$ 168,12), 10 Holter (R$ 249), 8 testes ergométricos (R$ 283,75), 30 avaliações
endócrinas (R$ 346); produção R$ 48.631; valor médio por hora R$ 410,97 (+21 % contra a hora mínima);
14 tabelas de convênio abaixo do custo cheio mais o imposto. Saída: "o ECG é o único procedimento com valor médio abaixo do
mínimo, e é o mix: 10 dos 18 foram por convênio, a R$ 32 (Vida Care) ou R$ 40 (Saúde Total)"; consulta a +7 % porque 48 % das 130
foram particulares; a conta do que muda se o ECG particular subir de R$ 130 para R$ 170 (o alvo);
três decisões com ganho e perda.
**Confira:** os realizados por pagador (Planilha 1, "Por pagador") antes de aceitar a explicação de
mix. Referência de mercado é opcional e sua; a divulgação de preços segue as regras do CFM/CRM.

### Preço 05 · Quanto cobrar por este procedimento
**Quando usar:** com um procedimento novo, um pacote ou uma consulta mais longa, antes de dar o
preço. O bloco "Simular" da Planilha 6 faz a conta; o prompt ajuda a pensar no que a conta não vê.
**Cole:** Planilha 6 · bloco "Simular um procedimento ou um preço novo" (minutos, retorno, material,
custo cheio, mínimo, alvo, preço pretendido, margem).

```
Estou definindo o preço particular de um procedimento novo em uma clínica médica. A conta da planilha: [minutos] de atendimento, [gera / não gera] retorno, material R$ [ ], custo cheio R$ [ ], preço mínimo R$ [ ] (margem mínima [30] %), preço alvo R$ [ ] (margem alvo [45] %), preço que pretendo cobrar R$ [ ], margem [ ] %. Não avalie nada clínico nem a indicação do procedimento; avalie só a conta e a operação.
Responda: 1) a margem refeita para eu conferir; 2) o que muda se o tempo real for 20 % maior que o estimado; 3) custos que a planilha não vê e eu deveria checar (laudo fora do horário, equipamento, insumo descartável, segundo profissional, retorno extra); 4) três perguntas para responder antes de colocar na tabela; 5) como registrar o preço na planilha 08 e na agenda (01) para o valor não ficar diferente em cada lugar.
```
**Exemplo:** Entrada: a simulação de exemplo da Vida Plena: consulta particular estendida de 45
minutos, com retorno, material R$ 4, custo cheio R$ 180,67, mínimo R$ 306,21, alvo R$ 410,61, preço
pretendido R$ 480, margem 51,4 %. Saída: margem conferida; com 54 minutos reais a margem cai para
cerca de 45 %; checar se o retorno da consulta estendida também dura mais; perguntas ("quantas por
mês?", "vai tomar o lugar de uma consulta de 30?", "o convênio cobre isso como consulta simples?") e
o lembrete de atualizar 08 e a Config da 01 no mesmo dia.
**Confira:** que o tempo estimado inclui o que acontece antes e depois do paciente entrar. Preço é
decisão da clínica; a IA só organiza a conta. Nada de divulgar o preço sem revisar pelas regras do
CFM/CRM.

### Preço 06 · Argumentos para negociar a tabela com o convênio
**Quando usar:** antes de uma conversa de reajuste de tabela ou de prazo com um convênio. O prompt
organiza os números da clínica em argumentos administrativos; a negociação, o contrato e o que
pode ser dito ao convênio são seus.
**Cole:** Planilha 8 · quadro "Valor por hora de atendimento, por pagador" (só a coluna do convênio em
questão), Planilha 7 · quadro 2 (prazo, glosa esperada, líquido) e Planilha 13 · "Por convênio" (prazo
contratual × real, glosa %).

```
Vou negociar tabela e prazo com um convênio. Sou dono de uma clínica médica pequena. Vou colar: o valor de tabela e o valor por hora que esse convênio paga em cada procedimento, contra a hora mínima da clínica de R$ [ ]; o prazo contratual e o prazo real de pagamento dos lotes; a glosa histórica em %; e quantos atendimentos desse convênio fizemos no mês. Monte: 1) três argumentos objetivos, cada um com um número e uma frase (valor por hora, prazo, glosa); 2) o que pedir, em ordem de prioridade (reajuste da tabela de [procedimento], prazo, revisão de glosas recorrentes), com uma faixa de pedido calculada a partir dos meus custos, não de mercado; 3) o que eu posso oferecer em troca (volume, agenda, prazo de envio do lote); 4) as perguntas que o convênio vai fazer e uma resposta curta para cada. Tom administrativo e cordial. Não invente regra da ANS nem do contrato; não escreva nada sobre pacientes ou sobre a qualidade do atendimento.
Dados:
[cole aqui]
```
**Exemplo:** Entrada: o Vida Care na Vida Plena: consulta R$ 90 (R$ 142 por hora contra R$ 339 de hora
mínima), ECG R$ 32, MAPA R$ 75; prazo contratual de 60 dias e real de 61; glosa de 11,3 % no ano
(R$ 1.423 em R$ 12.640 pagos), a maior dos três convênios; 13 consultas em agosto (10 % dos
atendimentos e 3 % do líquido). Saída: três argumentos com número, o pedido em ordem ("consulta de
R$ 90 para uma faixa de R$ 110 a R$ 130, que ainda fica abaixo do custo cheio de R$ 130,67", "prazo
de 45 dias", "glosa: revisão dos motivos recorrentes"), a oferta de manter a terça à tarde e as
perguntas prováveis.
**Confira:** os números de glosa e prazo na Planilha 13 e a faixa de pedido (a IA gosta de arredondar
para cima). Regras de reajuste e de aviso estão no contrato do convênio e na regulação da ANS: leia
antes, ou pergunte a quem cuida do jurídico.

### Preço 07 · Responder a um pedido de desconto
**Quando usar:** quando o paciente pediu desconto ou parcelamento em um orçamento e a recepção
precisa responder sem ceder no escuro e sem constranger.
**Cole:** Planilha 15 · a linha do orçamento sem nome (itens, valor, etapa) e a margem do procedimento
na Planilha 8 ou 6.

```
A recepção de uma clínica médica recebeu um pedido de desconto em um orçamento: [itens, ex.: teste ergométrico], R$ [ ]; o paciente pediu [ex.: 20 % de desconto / dividir em 4 vezes]. A margem do procedimento no preço cheio é [ ] % e o preço mínimo da clínica é R$ [ ]. Minha posição: posso [ex.: parcelar em até 3 vezes sem juros no cartão, oferecer desconto de 5 % no Pix] e não posso [ex.: baixar do preço mínimo].
Escreva a resposta em até 100 palavras, para WhatsApp: reconheça o pedido em uma frase, exponha a posição com clareza, ofereça as alternativas concretas e feche com um próximo passo (agendar ou pensar com calma). Sem justificar com o caso do paciente, sem tom defensivo, sem frase de venda e sem prometer nada sobre o exame. Antes do texto, calcule o que cada alternativa faz com a margem.
```
**Exemplo:** Entrada: teste ergométrico a R$ 450 (custo cheio R$ 158,33, mínimo R$ 268,36, margem
53,8 %), paciente pediu 20 % de desconto; posso parcelar em 3 vezes no cartão (taxa de 3,9 %) ou dar
5 % no Pix; não posso baixar de R$ 400. Saída: cálculo (20 % de desconto leva a R$ 360: ainda acima
do preço mínimo da planilha, R$ 268,36, mas abaixo do piso de R$ 400 que a própria clínica definiu
para este exame; 5 % no Pix leva a R$ 427,50 com margem de 52,0 %; 3 vezes no cartão custa R$ 17,55
de taxa) e resposta de 90 palavras com as duas alternativas.
**Confira:** o que a clínica realmente pode ceder; a IA tende a oferecer mais do que você disse.
Desconto e parcelamento são condições comerciais, não podem virar texto de divulgação sem revisão
pelas regras do CFM/CRM.

### Preço 08 · Antes de aceitar um convênio novo: a conta de horas e de caixa
**Quando usar:** quando um convênio novo propõe credenciamento, antes de dizer sim. Não é análise
de contrato; é a conta de se a agenda e o caixa aguentam o prazo e a glosa.
**Cole:** Planilha 1 · aba Painel (horas vazias por profissional e sala), Planilha 7 · quadro 3 (agenda
vazia) com a tabela proposta e Planilha 12 · aba Painel (reserva, caixa livre).

```
Estou decidindo se aceito o credenciamento de um convênio novo em uma clínica médica pequena. Não avalie o contrato nem regras da ANS; avalie a capacidade da clínica. Dados: tabela proposta para consulta R$ [ ] e para [procedimentos] R$ [ ]; prazo de pagamento [dias]; glosa esperada [ ] % (uso a média dos convênios que já tenho); horas vazias hoje por profissional e sala [ ]; custo cheio da consulta R$ [ ]; contribuição por atendimento com agenda vazia R$ [ ]; caixa livre R$ [ ]; reserva R$ [ ]; custo fixo mensal R$ [ ].
Responda: 1) cabe na agenda? (quantos atendimentos por semana o convênio traria e onde eles entrariam sem tirar particular); 2) cabe no caixa? (quanto dinheiro fica preso no prazo de pagamento em regime, com o volume estimado); 3) o que teria de sair ou ser adiado para caber; 4) três condições que eu poderia colocar na conversa para reduzir o risco de gestão (volume máximo por semana, procedimentos incluídos, prazo); 5) uma versão menor do mesmo sim (um turno, um profissional, três meses de teste). Não me diga o que decidir.
```
**Exemplo:** Entrada: um convênio propondo consulta a R$ 110 e ECG a R$ 38, prazo de 45 dias; glosa
esperada 6 %; horas vazias na Vida Plena: Sala 2 com 8,2 horas em setembro, Dr. Paulo Andrade com
34 % de agenda livre; custo cheio da consulta R$ 130,67; contribuição com agenda vazia de um
convênio parecido (MediPlan): R$ 77,55 por consulta; caixa livre R$ 26.836; reserva R$ 14.000; custo
fixo R$ 28.000 com pró-labore. Saída: "cabe na agenda só na Sala 2, à tarde: até 16 consultas por
semana sem tirar particular"; cerca de R$ 2.600 presos no prazo em regime; condições (só consulta e
ECG, teto de 16 por semana, envio de lote dia 5); versão menor: quinta à tarde por três meses.
**Confira:** as horas vazias de verdade (a Planilha 1 mostra por dia e período); a contribuição por
atendimento vem do quadro 3 da 07, não da IA. Contrato e regras de credenciamento: leia antes de
assinar.

---

## Grupo 3 · Caixa e contador (9)

### Caixa 01 · Explicar o mês do caixa
**Quando usar:** na sexta de fechamento, com o Painel do Caixa, para explicar ao sócio (ou a você
mesmo) o que aconteceu com o dinheiro.
**Cole:** Planilha 9 · aba Painel ("Para onde foi o dinheiro", "De onde veio", saldo, comparação com o
mês anterior).

```
Explique o resultado de caixa do mês de uma clínica médica para [o sócio / eu mesmo], em até 200 palavras e linguagem simples: quanto entrou (e de onde: particular à vista, particular a prazo, cada convênio), quanto saiu, para onde foi a maior parte (pró-labore, custos fixos, repasse ao médico parceiro, impostos, materiais, taxas de cartão), quanto sobrou, o que mudou em relação ao mês anterior e uma decisão sugerida para o próximo mês. Separe "entrou" de "produziu": lote de convênio enviado e parcela a receber não são dinheiro. Sem termos técnicos. Nada sobre pacientes.
Números:
[cole o painel]
Contexto: [o que aconteceu de diferente no mês].
```
**Exemplo:** Entrada: o Painel de agosto da Vida Plena (Config = Agosto): entrou R$ 49.651 (particular
à vista R$ 33.860, particular a prazo R$ 4.630, Saúde Total R$ 7.320, MediPlan R$ 2.130, Vida Care
R$ 1.711), saiu R$ 41.660 (pró-labore R$ 18.000, custos fixos R$ 10.000, guia de impostos R$ 5.881,
repasse à Dra. Renata R$ 4.845, materiais R$ 1.380, taxas de cartão R$ 484, manutenção R$ 450,
despesa pessoal a acertar R$ 620), sobrou R$ 7.991, saldo R$ 44.468; julho: entrou R$ 53.461 e sobrou
R$ 9.894. Contexto: "julho teve a distribuição do 2º trimestre e agosto teve manutenção do
equipamento". Saída: 190 palavras em linguagem de conversa e a decisão sugerida: "levar R$ 3.000
para a reserva, que cobre só meio mês de custo fixo".
**Confira:** números e a decisão. Se a sobra parece grande, veja se a guia de impostos e o repasse
do mês foram lançados.

### Caixa 02 · Comparar dois meses do resultado
**Quando usar:** mês contra mês, com o Resultado mensal (DRE simplificada), quando algo mudou e você
quer saber o quê.
**Cole:** Planilha 18 · aba Resultado, colunas dos dois meses (ou a tabela "Comparação" do Painel).

```
Compare os dois meses abaixo do resultado de uma clínica médica, linha por linha: variação absoluta, variação percentual e um comentário de uma linha. Depois, os três maiores avanços, os três maiores recuos e uma conclusão de duas frases. Classifique cada linha como "melhorou", "piorou" ou "estável" (estável = variação menor que [3] %). Lembre que para custos, despesas, impostos, glosa e inadimplência, menor é melhor; e que variação de margem se diz em pontos percentuais. Não invente causas: separe "o que os números mostram" de "hipóteses". Nada sobre pacientes.
Mês 1 ([nome]):
[cole]
Mês 2 ([nome]):
[cole]
```
**Exemplo:** Entrada: julho e agosto da Vida Plena na Planilha 18 (receita R$ 53.461 para R$ 49.651;
despesas variáveis R$ 6.662 para R$ 7.159; total de saídas R$ 42.505 para R$ 42.583; resultado
R$ 10.956 para R$ 7.068; margem 20,5 % para 14,2 %). Saída: tabela com as linhas, receita −7,1 %
(piorou), custos fixos estável, variáveis +7,5 % (piorou: manutenção de R$ 450 e repasse maior),
resultado −35,5 % (piorou), margem −6,3 p.p. e a conclusão: "a queda é de receita particular à vista
(R$ 37.700 para R$ 33.860), não de custo; os convênios até subiram".
**Confira:** sinais de "menor é melhor" e as porcentagens; a IA erra conta de variação.

### Caixa 03 · Cortar custo fixo sem cortar atendimento
**Quando usar:** quando o custo da hora subiu, a sobra do mês encolheu ou o custo fixo passou do que a
clínica combinou, e você quer saber o que dá para cortar sem mexer no que o paciente sente.
**Cole:** Planilha 5 · aba Custos fixos (as linhas do mês, uma a uma) e a Planilha 9 · aba Painel
("Para onde foi o dinheiro", com os custos fixos ao lado das outras saídas do mês).

```
Sou dono de uma clínica médica pequena e quero revisar o custo fixo sem piorar o atendimento. Vou colar duas listas: os custos fixos do mês, linha por linha, e para onde foi o dinheiro do caixa no mês (todas as categorias de saída). Horas de atendimento planejadas por mês: [140]. Margem mínima [30] % e impostos [11] %.
Responda: 1) ordene os custos fixos por peso, em R$ e em % do fixo e do total que saiu do caixa; 2) separe em três grupos: o que o paciente sente se sumir, o que a equipe sente e o que ninguém sente; 3) para cada linha do terceiro grupo, o que dá para renegociar, trocar de plano, cancelar ou juntar, e uma pergunta para eu levar ao fornecedor; 4) refaça a conta do custo da hora e da hora mínima com o corte proposto, mostrando o antes e o depois; 5) o que NÃO cortar, e por quê. Não sugira demitir ninguém, não sugira cortar material de atendimento, limpeza, seguro, anuidade de conselho nem contador, e não sugira captar pacientes: a decisão é da clínica.
Custos fixos:
[cole a aba Custos fixos]
Para onde foi o dinheiro no mês:
[cole o Painel da 09]
```
**Exemplo:** Entrada: os custos fixos da Clínica Vida Plena (aluguel e condomínio R$ 3.900, recepção
R$ 3.100, contador R$ 600, sistema de agenda e assinaturas R$ 300, energia, água, internet e telefone
R$ 550, limpeza e material de escritório R$ 450, marketing e site R$ 650, anuidade do CRM, seguro e
cursos R$ 450; total R$ 10.000) e o Painel do Caixa de agosto (saiu R$ 41.660: pró-labore R$ 18.000,
custos fixos R$ 10.000, guia de impostos R$ 5.881, repasse à parceira R$ 4.845, materiais R$ 1.380,
taxas de cartão R$ 484, manutenção R$ 450, despesa pessoal a acertar R$ 620); 140 horas planejadas.
Saída: aluguel e recepção são R$ 7.000, 70 % do custo fixo, e o fixo inteiro é 24 % do que saiu do
caixa em agosto; no grupo "ninguém sente", o sistema de agenda (R$ 300, com assinatura antiga
duplicada) e parte do marketing; com um corte de R$ 700 por mês, o custo fixo cai para R$ 9.300, o
custo-hora de R$ 200,00 para R$ 195,00, a hora mínima de R$ 338,98 para R$ 330,51 e o custo da
estrutura por hora de R$ 71,43 para R$ 66,43 — R$ 8.400 por ano, o equivalente a 22 consultas
particulares de R$ 380; não cortar: seguro, anuidade do CRM, contador e limpeza.
**Confira:** refaça a conta do custo-hora com o novo total (a planilha 05 faz sozinha quando você
muda a linha) e veja se o corte não é só adiamento (assinatura anual que volta em janeiro). Corte que
mexe em pessoa é assunto trabalhista: fale com o contador e com quem cuida do jurídico antes.

### Caixa 04 · Preparar a reunião mensal com o contador
**Quando usar:** dois dias antes da reunião com o contador, com o Resumo do mês pronto. Junta o que
enviar, o que perguntar e o que anotar (o roteiro completo é o bônus 24).
**Cole:** Planilha 20 · aba Resumo ("Bloco único para copiar") e a Planilha 10 · aba Painel (provisão
acumulada).

```
Vou me reunir com o contador da minha clínica médica (pessoa jurídica) por 30 minutos. Com o resumo do mês abaixo, monte: 1) a lista do que eu envio antes (documentos e números, com o nome da planilha de origem; só totais, nunca nome de paciente); 2) a pauta em 4 blocos com minutos; 3) oito perguntas objetivas para o contador, priorizando o que muda dinheiro (alíquota efetiva e enquadramento, provisão, pró-labore, repasse ao médico parceiro, notas fiscais, glosa, retenções dos convênios); 4) uma tabela vazia "Pergunta | Resposta | Ação | Prazo" para eu preencher na reunião. Não responda as perguntas no lugar do contador nem dê orientação tributária.
Resumo do mês:
[cole aqui]
Dúvidas que já tenho: [liste]
```
**Exemplo:** Entrada: o Resumo de agosto da Vida Plena (receita R$ 49.651, saídas R$ 42.583, resultado
R$ 7.068, margem 14,2 %; provisão acumulada na Planilha 10 R$ 17.527 ao fim de agosto e guia de
20/09 prevista em R$ 5.462; repasse à Dra. Renata R$ 5.190 pago em 10/09; R$ 5.440 a acertar com os
sócios no ano) e a dúvida "a glosa entra na base do imposto ou só o que o convênio pagou?". Saída:
lista de 7 itens para enviar (só totais), pauta de 4 blocos (5 + 10 + 10 + 5 min), 8 perguntas ("a
alíquota efetiva de 11 % continua certa para o faturamento dos últimos 12 meses?", "como formalizar o
repasse à parceira?") e a tabela vazia.
**Confira:** as perguntas são para o contador responder; não use a resposta da IA como resposta
dele.

### Caixa 05 · Perguntas sobre provisão de impostos, 13º e férias
**Quando usar:** quando o número da provisão parece alto ou baixo e você não sabe se está certo. O
prompt não calcula imposto; ele monta as perguntas certas para o contador.
**Cole:** Planilha 10 · aba Painel (entradas do mês, alíquota informada pelo contador, provisão do
mês, 13º e férias, saldo provisionado, compromisso do mês seguinte).

```
Sou dono de uma clínica médica (pessoa jurídica) e provisiono impostos, 13º e férias em uma planilha com a alíquota efetiva que o contador me informou. Não calcule imposto nem diga qual regime é melhor: isso é do contador. Com os números abaixo, faça: 1) confira se a conta provisão = entradas × alíquota está aritmeticamente certa; 2) diga se o saldo provisionado cobre o que vence nos próximos 90 dias e, se não, o buraco em reais; 3) monte cinco perguntas para o contador que esclareçam o que a planilha não sabe (o que entra na base: repasse ao parceiro, glosa, taxas de cartão; retenções feitas pelos convênios; 13º e férias de quem; o que muda em dezembro); 4) uma regra simples de quanto separar por semana.
Números:
[cole aqui]
```
**Exemplo:** Entrada: setembro da Vida Plena até 11/09: entradas R$ 21.920, alíquota 11 %, provisão
R$ 2.411, mais R$ 1.698 de 13º (R$ 750 de cada sócio, decididos pelos sócios, e R$ 198 da
recepcionista) e R$ 264 de férias (R$ 4.373 a separar no mês); saldo provisionado R$ 21.900;
compromisso do mês seguinte R$ 2.411; guia de agosto (R$ 5.462) vence em 20/09. Saída: conta
conferida, saldo suficiente para 90 dias, cinco perguntas ("o repasse pago à médica parceira reduz
a base?", "o convênio retém algum imposto no pagamento do lote?") e a regra: "separar cerca de
R$ 1.100 por semana (o total a separar do mês dividido por quatro)".
**Confira:** a alíquota é a que o contador disse, não a que a IA sugerir. Se ela sugerir alguma,
ignore.

### Caixa 06 · Separar o que é da clínica e o que é pessoal
**Quando usar:** quando o extrato veio misturado (conta única, cartão do sócio) e você precisa
classificar antes de lançar na aba Retiradas da Planilha 11.
**Cole:** o extrato do mês, só com data, descrição resumida e valor, sem número de conta, sem nome de
paciente ou de terceiros.

```
Vou colar lançamentos de um extrato bancário misturado (clínica médica e vida pessoal do sócio), com data, descrição resumida e valor. Classifique cada linha em: Clínica: custo fixo | Clínica: material ou despesa variável | Clínica: receita | Repasse a médico parceiro | Pró-labore ou retirada | Pessoal | Não sei. Use "Não sei" sempre que a descrição for ambígua; não chute. Depois some cada grupo e diga: quanto o sócio retirou além do pró-labore combinado de R$ [ ]; e quais lançamentos pessoais foram pagos pela conta da clínica. Responda em tabela. Nada sobre pacientes: se uma linha tiver nome de pessoa, eu já troquei por "Paciente A".
Lançamentos:
[cole aqui]
```
**Exemplo:** Entrada: os 94 lançamentos de agosto da conta da Vida Plena, descrição resumida. Saída:
tabela classificada, 5 linhas em "Não sei" (farmácia, posto, restaurante), o pró-labore de R$ 9.000 de
cada sócio em 28/08 (dentro do combinado) e um lançamento pessoal pago pela clínica: R$ 620 do plano
de saúde da família da Dra. Carolina, em 06/08, a lançar na aba Retiradas da Planilha 11 como despesa
pessoal a acertar. No ano, o a acertar soma R$ 5.440 (Carolina R$ 2.740, Paulo R$ 2.700), e a única
retirada extra da Carolina foi R$ 1.500 em 19/06.
**Confira:** cada "Não sei" e as retiradas; corrija na tabela e só então lance na planilha. O
tratamento de cada retirada (pró-labore, distribuição, adiantamento) é assunto do contador.

### Caixa 07 · Conversa sobre o repasse com o médico parceiro
**Quando usar:** antes de propor ou revisar o percentual de repasse de um médico parceiro, ou quando
o parceiro pergunta "por que 50 %?". Prepara a conversa com os números da clínica; o contrato de
parceria é assunto jurídico e não está no kit.
**Cole:** Planilha 11 · aba Painel, "Médicos parceiros" (produção, repasse devido, horas, o que fica
com a clínica, custo da estrutura das horas) e a Planilha 1 · "Por profissional".

```
Vou conversar com um médico parceiro que atende na minha clínica por repasse. Dados: repasse atual [ ] % da produção do mês; produção dele no mês R$ [ ] em [ ] horas; o que fica com a clínica R$ [ ]; custo da estrutura por hora (sala, recepção, sistema, rateio do fixo) R$ [ ]; ocupação da agenda dele [ ] %. Proposta ou dúvida em pauta: [ex.: o parceiro pede 60 %; quero manter 50 % e abrir um terceiro turno].
Responda: 1) a conta da parceria como ela está (o que a clínica recebe por hora dele contra o que a estrutura custa por hora), em linguagem que os dois entendam; 2) o que muda para cada lado em cada alternativa em pauta, em reais por mês; 3) o que a clínica fornece que costuma ficar invisível na conversa (recepção, agenda, cobrança, faturamento do convênio, glosa absorvida, materiais); 4) três combinados administrativos que evitam atrito (dia do pagamento, base do repasse: produção ou recebido; como tratar glosa e falta); 5) uma proposta de conversa em cinco frases. Não redija contrato nem cláusula; não comente nada clínico.
```
**Exemplo:** Entrada: a Dra. Renata Sousa na Vida Plena: 50 % da produção, paga dia 10; agosto:
produção R$ 10.380 em 23,7 horas, repasse R$ 5.190 (pago em 10/09), o que ficou com a clínica
R$ 5.190; no ano: produção R$ 80.680, repasse R$ 40.340, custo da estrutura das horas R$ 14.600
(horas × R$ 71,43); ocupação de 88 % em setembro; pauta: a parceira pergunta se 50 % é justo. Saída:
a conta ("a clínica fica com R$ 219 por hora dela e a estrutura custa R$ 71: a parceria paga a sala
e sobra"), o que muda a 55 % e a 60 % (R$ 519 e R$ 1.038 a menos por mês para a clínica, no volume de
agosto), o invisível (faturamento e glosa do convênio, recepção, cobrança das parcelas), quatro
combinados e a conversa em cinco frases.
**Confira:** os números da 11 e da 01; a IA não sabe o que está no contrato. Como formalizar a
parceria (contrato, nota da parceira, tributação do repasse) é pergunta para o contador e para quem
cuida do jurídico (bônus 24).

### Caixa 08 · Plano para a reserva de três meses
**Quando usar:** quando a Planilha 12 mostra menos de três meses de custo fixo guardados e você
quer um plano que caiba no caixa real.
**Cole:** Planilha 12 · aba Painel (meta, reserva atual, falta, meses cobertos, mês previsto) e a sobra
média dos últimos 3 meses (Planilha 9).

```
Monte um plano para uma clínica médica chegar a três meses de custo fixo em reserva. Dados: custo fixo mensal com pró-labore R$ [ ]; reserva atual R$ [ ]; sobra média mensal dos últimos 3 meses R$ [ ]; entradas previstas fora do comum nos próximos 6 meses: [ex.: recuperação de glosa em recurso, R$ 240, sem data certa]; meses de receita menor: [ex.: janeiro e julho].
Responda: 1) a meta em reais e quantos meses faltam no ritmo atual; 2) três ritmos (conservador, provável, ambicioso) com o valor a separar por mês e a data de chegada; 3) regras: o que a reserva pode pagar e o que não pode; 4) o que fazer com uma entrada extraordinária quando vier. Não conte com a entrada extraordinária no cenário provável.
```
**Exemplo:** Entrada: custo fixo mensal com pró-labore R$ 29.732 (média de junho, julho e agosto;
meta de 3 meses: R$ 89.197), reserva R$ 14.000, sobra média dos três últimos meses fechados R$ 6.838
(junho R$ 2.628, julho R$ 9.894, agosto R$ 7.991), sem entrada extraordinária certa; janeiro e
fevereiro fecharam negativos. Saída: faltam R$ 75.197; conservador R$ 3.000 por mês (26 meses:
novembro de 2028, como na Planilha 12), provável R$ 5.000 (16 meses), ambicioso R$ 6.500 (12 meses,
quase toda a sobra média, e por isso só com o mês de junho fora da curva explicado); regra: "a reserva
paga custo fixo e repasse em mês fraco; não paga equipamento nem retirada extra"; entrada
extraordinária: 50 % para a reserva até a meta.
**Confira:** a sobra média, refazendo a conta com os três meses que você colou (a IA erra média), e
se o ritmo cabe no pró-labore combinado. O
resultado após pró-labore do 3º trimestre (Planilha 11) diz quanto sobra de verdade.

### Caixa 09 · A taxa da maquininha está comendo a margem?
**Quando usar:** no fechamento do mês, com o Painel da Planilha 16, para decidir entre absorver a
taxa, oferecer desconto no Pix, mudar o parcelamento ou trocar de operadora.
**Cole:** Planilha 16 · aba Painel, os cartões e "Por tipo de pagamento no mês" (vendas, bruto, taxas,
taxa média, líquido, % do bruto).

```
Vou colar a conciliação de cartão de uma clínica médica em um mês: vendas por tipo (Pix, débito, crédito à vista, crédito parcelado), valor bruto, taxas, taxa média, líquido e prazo de recebimento. Preço da consulta particular: R$ [ ]. Margem da consulta no preço cheio: [ ] %.
Responda: 1) quanto as taxas custaram no mês e no ano projetado, e a quantas consultas equivalem; 2) qual tipo de pagamento pesa mais na taxa e qual mais no prazo (dinheiro parado); 3) o que muda em reais se [ex.: 30 % do crédito parcelado migrar para Pix com 3 % de desconto / o parcelamento passar a ser só em 2 vezes / a operadora cobrar 1,2 % no débito]; 4) três decisões possíveis, com o que a clínica ganha, o que perde e o que precisa avisar ao paciente. Não sugira repassar taxa ao paciente sem me lembrar que isso tem regra própria; não escreva texto de divulgação.
Dados:
[cole aqui]
```
**Exemplo:** Entrada: agosto da Vida Plena: R$ 31.820 em Pix e cartão; taxas R$ 484,12 (1,52 %);
Pix 37 vendas, R$ 13.380, sem taxa; débito 22 vendas, R$ 8.090, R$ 121,35 (1,5 %, cai em 1 dia); crédito à vista R$ 5.840, R$ 186,88 (3,2 %);
crédito parcelado 12 vendas, R$ 4.510, R$ 175,89 (3,9 %, cai de 30 em 30 dias); ainda vai cair
R$ 12.388; consulta particular R$ 380. Saída: "R$ 484 no mês equivalem a 1,3 consultas; no ano, cerca
de R$ 5.800"; o parcelado pesa na taxa e no prazo (R$ 4.510 pingando em até 3 meses); migrar 30 % do
parcelado para Pix com 3 % de desconto troca R$ 53 de taxa por R$ 41 de desconto e adianta o
dinheiro; três decisões com ganho e perda.
**Confira:** as taxas do contrato da operadora (Config da 16) e se o parcelamento é com ou sem
juros. Repasse de custo de cartão ao consumidor tem regra própria: pergunte ao contador antes.

---

## Grupo 4 · Recebíveis e cobrança (8)

### Recebíveis 01 · Resumir os convênios para o sócio
**Quando usar:** na sexta de fechamento ou na reunião de sócios, para responder "quanto o convênio
deve, quanto atrasou e quanto ele não pagou".
**Cole:** Planilha 13 · aba Painel, os cartões e "Por convênio" (lotes, enviado, pago, glosa, glosa %,
recuperado, a receber, atrasado, prazo contratual × real) e "Lotes em aberto".

```
Resuma a posição dos convênios de uma clínica médica para um sócio, em até 200 palavras: 1) total a receber (lotes enviados e não pagos), atrasado e em recurso; 2) por convênio: a receber, glosa no ano em % e prazo real contra o contratual; 3) o convênio que mais pesa no caixa (valor preso × prazo) e o que mais glosa; 4) o que vence nos próximos 30 dias; 5) três perguntas de gestão que a posição levanta. Não comente guia, atendimento ou paciente; só totais. Use só os números colados.
Convênios:
[cole aqui]
```
**Exemplo:** Entrada: a Vida Plena em 11/09: a receber R$ 15.758, atrasado R$ 1.727 (lote de junho do
Vida Care, previsto para 04/09), em recurso R$ 240 (lote de junho da Saúde Total), glosa no ano
R$ 4.273 (5,5 %); Saúde Total 3,3 % de glosa e prazo real de 32 dias (contrato 30), MediPlan 7,5 % e
47 dias (45), Vida Care 11,3 % e 61 dias (60); lotes de agosto enviados em 08/09 (R$ 9.631); MediPlan
de julho previsto para 19/09 (R$ 2.875). Saída: 190 palavras: "o Vida Care é 3 % do líquido e 33 % da
glosa"; o MediPlan pesa mais no caixa (R$ 6.305 presos a 47 dias); vence nos próximos 30 dias
R$ 8.955 (MediPlan de julho R$ 2.875 em 19/09, Vida Care de julho R$ 1.525 em 04/10 e Saúde Total de
agosto R$ 4.555 em 08/10), fora o lote atrasado; perguntas:
"as duas guias glosadas de julho já foram recorridas?", "o lote de junho do Vida Care já foi cobrado
ao convênio?".
**Confira:** a divisão a receber × atrasado e a glosa % (glosa ÷ (pago + glosa) dos lotes pagos, a
mesma conta em todo o kit).

### Recebíveis 02 · Quem cobrar primeiro
**Quando usar:** na segunda, com a aba Painel da Planilha 14 mostrando mais parcelas vencidas do que
dá para contatar em uma manhã. Ordena pela conta, não pela vontade.
**Cole:** Planilha 14 · aba Painel, "Cobrar primeiro" sem nomes (procedimento, parcela, vencimento,
valor, dias de atraso, faixa, ação sugerida); acrescente à mão a data do último contato e se o
paciente já atrasou antes.

```
Ordene as parcelas atrasadas de uma clínica médica abaixo para eu decidir quem cobrar primeiro hoje. Critérios, nesta ordem: valor × dias de atraso; paciente que nunca atrasou antes (cobre cedo, com leveza: provavelmente esqueceu); último contato há mais de 7 dias; parcela de atendimento com retorno ainda por acontecer (eu marco). Para cada linha: prioridade (1 a 3), o degrau da régua de cobrança (1 dia: lembrete gentil por WhatsApp; 7 dias: mensagem da recepção perguntando se houve imprevisto e oferecendo nova data; 15 dias: ligação da recepção com o demonstrativo e proposta de nova data ou divisão; 30 dias: conversa do médico ou da administração para combinar um plano de pagamento, registrado por escrito) e o canal. Sem tom de ameaça em nenhuma sugestão; sem citar consequência, negativação ou suspensão de atendimento: isso não entra em mensagem de cobrança de paciente.
Parcelas:
[cole aqui]
```
**Exemplo:** Entrada: as 14 parcelas vencidas da Vida Plena em 14/09 (R$ 3.775): 12 com 30 dias ou
mais (R$ 3.455; entre elas Paciente A, avaliação endócrina, R$ 400, 158 dias; Paciente B, avaliação
endócrina, R$ 400, 130 dias; Paciente C, R$ 200, 214 dias) e 2 entre 1 e 6 dias (R$ 320, nunca
atrasaram); nenhuma nas faixas de 7 a 14 e de 15 a 29. Saída: os 12 antigos como prioridade 1 no
degrau 30 (conversa e plano por escrito) e as 2 de 1 a 6 dias como prioridade 2 no degrau 1 (lembrete
leve, primeiro atraso); e a observação: "R$ 3.455 estão há mais de 30 dias: mensagem já não resolve;
agende as conversas".
**Confira:** o histórico de atraso; a planilha só sabe o que foi lançado. Cobrança de paciente sem
exposição nem constrangimento (CDC e ética médica): revise cada sugestão.

### Recebíveis 03 · Recurso de glosa em linguagem administrativa
**Quando usar:** com uma guia glosada na lista "Guias glosadas para recorrer" da Planilha 13 e o
motivo administrativo da glosa (código, data, autorização, valor de tabela, duplicidade). O prompt
escreve o texto administrativo do recurso; nada clínico entra nele.
**Cole:** Planilha 13 · aba Painel, a linha da guia sem o nome do paciente (número da guia, data,
convênio, procedimento, profissional, valor, motivo da glosa informado pelo convênio).

```
Escreva o texto de um recurso administrativo de glosa para a operadora [Convênio 1], em até 200 palavras, em nome de uma clínica médica. Dados: guia nº [ ], atendimento em [data], procedimento [nome administrativo], valor glosado R$ [ ], motivo informado pela operadora: [ex.: "código de procedimento divergente da tabela contratada" / "autorização não localizada" / "valor acima da tabela"]. Nosso argumento administrativo: [ex.: o código usado é o da tabela contratada, anexo; a autorização nº [ ] foi emitida em [data]; o valor é o da tabela vigente desde [data]].
Regras: linguagem administrativa e objetiva; cite o contrato ou a tabela quando eu indicar; liste os anexos ([guia, autorização, tabela, comprovante de envio]); peça a reanálise e o pagamento no próximo lote, com o prazo do contrato. Não inclua nenhuma informação clínica (diagnóstico, justificativa médica, laudo, prontuário): se o motivo da glosa for clínico, diga que o recurso precisa ser escrito pelo médico responsável e pare. Não identifique o paciente além do número da guia.
```
**Exemplo:** Entrada: guia G2026-0582 da Saúde Total, ECG em 10/07/2026 com o Dr. Paulo Andrade,
R$ 40 glosados, motivo informado "código de procedimento divergente"; argumento: o código enviado é
o da tabela contratada em vigor desde 01/2026, anexa. Saída: texto de 180 palavras com identificação
da guia, o motivo, o argumento, a lista de anexos (guia, tabela contratada, comprovante de envio do
lote de 05/08) e o pedido de reanálise no lote seguinte, dentro do prazo contratual de 30 dias.
**Confira:** número da guia, data, valor e o motivo exato da glosa no demonstrativo do convênio. Se a
glosa for por razão clínica (justificativa, indicação, laudo), o recurso é do médico, com o
prontuário, e não passa pela IA. Marque o recurso na aba Lotes da 13 e, se for aceito, lance o
recuperado.

### Recebíveis 04 · Cobrança educada em três versões
**Quando usar:** com uma parcela atrasada e a régua da Planilha 14 dizendo em que degrau está. Os
15 modelos do bônus são a versão pronta; este prompt é para quando o caso pede algo sob medida.
**Cole:** Planilha 14 · aba Painel, a linha da parcela sem nome (procedimento, parcela, valor,
vencimento, dias de atraso, ação sugerida pela régua).

```
Escreva três versões de mensagem de cobrança de uma clínica médica para [Paciente A], sobre a parcela [n de N] de R$ [ ] do atendimento de [procedimento, nome administrativo], vencida em [data]: 1) lembrete amigável (primeiro contato, presuma esquecimento); 2) segunda mensagem, firme e cordial, da recepção; 3) convite para uma conversa sobre como regularizar, claro e sem ameaça. Cada uma com até 80 palavras, com a forma de pagamento (Pix [chave], link, cartão na recepção) e um caminho fácil para resolver (responder esta mensagem, ligar para [telefone]). Tom de clínica: respeitoso, sem "prezado" em excesso. Não mencione o motivo do atendimento, nada de saúde, nenhuma consequência (negativação, suspensão de atendimento, juros): cobrança de paciente é sem exposição e sem constrangimento.
```
**Exemplo:** Entrada: Paciente D, parcela 1 de 2 de R$ 380 de uma consulta, vencida em 12/06/2026 (94
dias), Pix pelo CNPJ da clínica. Saída: três mensagens de 60 a 80 palavras, da primeira ("pode ter
passado despercebido") à terceira ("podemos conversar sobre a melhor forma de regularizar? A Bruna
atende no telefone da clínica"), todas com valor, data e chave.
**Confira:** valor, data, parcela; e se nenhuma versão insinua consequência ou fala do atendimento.
Aos 94 dias, a régua já está no degrau 30: a terceira versão é a que vale.

### Recebíveis 05 · Por que os orçamentos não fecham
**Quando usar:** no fim do trimestre, com o funil da Planilha 15 mostrando muito orçamento parado,
recusado ou sem retorno.
**Cole:** Planilha 15 · aba Painel: "Funil por etapa", "Por tipo" (orçamentos, aprovados, taxa de
aprovação, valor) e "Motivos de recusa".

```
Analise o funil de orçamentos de uma clínica médica (exames e pacotes particulares apresentados pela recepção). Para o trimestre: taxa de aprovação geral e por tipo; valor médio dos aprovados e dos recusados; dias até a decisão; motivos de recusa mais frequentes; orçamentos abertos há mais de [7] dias que merecem um contato. Separe "o que os dados mostram" de "hipóteses". Termine com três testes simples para o próximo trimestre (ex.: apresentar o parcelamento junto com o valor, retomar contato no terceiro dia, oferecer data na hora). Não sugira baixar preço com base em mercado; não sugira campanha, divulgação ou captação; nada clínico (não discuta se o exame era indicado).
Orçamentos:
[cole aqui]
```
**Exemplo:** Entrada: os 36 orçamentos da Vida Plena desde junho: 22 aprovados (R$ 8.960), 5
recusados (R$ 1.860), 3 sem retorno (R$ 1.660), 6 em aberto (R$ 3.460); taxa de aprovação 73 %; exames
cardiológicos 84 % (21 de 25 decididos), pacotes de consultas 0 de 2 e avaliação endócrina 0 de 1;
motivos: "vai pensar / sem retorno" 3 (R$ 1.660), preço 2 (R$ 680), fez em outro lugar 1, vai fazer
pelo convênio 1, sem indicação no momento 1; 11 dias em média até decidir. Saída: aprovação alta em
exame e nula em pacote; "sem retorno" é o maior motivo, não preço; hipótese "o orçamento sai sem data
de retomada"; três testes (retomar no 3º dia com o Agenda 04, oferecer a data do exame junto com o
valor, apresentar o pacote só depois da consulta).
**Confira:** as taxas por grupo com poucos orçamentos (2 pacotes) não provam nada; olhe o tamanho da
amostra. Orçamento é ato administrativo: a indicação do exame é do médico.

### Recebíveis 06 · Roteiro de ligação de cobrança
**Quando usar:** antes de a recepção ligar para um paciente com parcela atrasada há 15 dias ou mais
(degrau 3 da régua), quando a mensagem já não resolveu.
**Cole:** Planilha 14 · a linha da parcela sem nome e o seu registro de contatos com esse paciente
(datas e canal).

```
Monte um roteiro de ligação de até 4 minutos para a recepção de uma clínica médica cobrar uma parcela atrasada de [Paciente A]: parcela de R$ [ ], do atendimento de [procedimento], vencida há [dias], já enviamos [quantas mensagens, em que datas]. Estrutura: abertura (uma frase, sem rodeio e sem "desculpa incomodar"); pergunta aberta sobre o que aconteceu; escuta (o que anotar); três saídas possíveis que a recepção pode oferecer: [ex.: pagar até sexta / dividir em duas / nova data]; fechamento com combinado explícito e confirmação por mensagem. Inclua o que NÃO dizer (ameaça, comparação com outros pacientes, comentário sobre o atendimento ou a saúde da pessoa, negativação) e o que fazer se a pessoa ficar irritada ou disser que não pode pagar agora. Português falado, curto.
```
**Exemplo:** Entrada: Paciente E, parcela 1 de R$ 450 de um teste ergométrico, 22 dias de atraso, duas
mensagens (24/08 e 31/08). Saída: roteiro de uma página: abertura em uma frase, pergunta "aconteceu
alguma coisa com o pagamento desta parcela?", três saídas, fechamento "então fica combinado dia 25/09,
e eu confirmo por mensagem agora" e a lista do que não dizer.
**Confira:** as saídas que a recepção oferece têm de caber no caixa e na sua regra; a IA não sabe o
que você pode. Quem liga é a recepção, com o demonstrativo da Planilha 14 na tela.

### Recebíveis 07 · Responder a um pedido de prazo ou parcelamento
**Quando usar:** quando o paciente pediu para adiar, dividir ou parar de pagar. Responde sem ceder
no escuro e sem entrar no atendimento.
**Cole:** Planilha 14 · aba Parcelas (o que falta receber desse paciente, sem nome) e a data do
próximo retorno, se houver.

```
Recebi de [Paciente A] o pedido abaixo sobre as parcelas de um atendimento particular em uma clínica médica. Situação: falta receber R$ [ ] em [n] parcelas; já recebemos R$ [ ]; há retorno marcado para [data / não há]. Minha posição: posso [ex.: adiar 30 dias / dividir a parcela em duas] e não posso [ex.: reduzir o total]. Escreva a resposta em até 150 palavras: reconheça a situação em uma frase, exponha a posição sem se justificar, ofereça uma alternativa concreta com datas e feche pedindo confirmação por mensagem. Antes do texto, mostre o que cada alternativa faz com o caixa da clínica nos próximos 3 meses. Não mencione nada sobre o atendimento, a saúde do paciente, o retorno como condição, nem consequências.
Pedido do paciente (sem dados pessoais):
[cole]
```
**Exemplo:** Entrada: Paciente F (avaliação endócrina de R$ 400 em 2 parcelas de R$ 200): falta
receber R$ 200 (parcela 2, vence em 21/09), recebido R$ 200, retorno marcado; o paciente pediu 60
dias; posso adiar 30 dias ou dividir em duas de R$ 100. Saída: tabela de caixa (adiar tira R$ 200 de
setembro; dividir tira R$ 100) e resposta de 120 palavras com a alternativa de dividir.
**Confira:** os números do trimestre e se a resposta não condiciona o retorno ao pagamento: o
atendimento continua sendo decisão do médico, não da cobrança.

### Recebíveis 08 · Mensagem ao convênio sobre lote atrasado
**Quando usar:** quando um lote passou da previsão de pagamento (Planilha 13, "Lotes em aberto":
situação Atrasada) e a clínica precisa cobrar a operadora por escrito, em tom administrativo.
**Cole:** Planilha 13 · aba Painel, a linha do lote (convênio, competência, nº de guias, valor enviado,
data de envio, previsão, dias de atraso) e o prazo contratual (Config).

```
Escreva um e-mail administrativo de até 150 palavras, com assunto, de uma clínica médica para a operadora [Convênio 1], sobre o lote de [competência] enviado em [data], com [n] guias e R$ [ ], cujo pagamento estava previsto para [data] pelo prazo contratual de [dias] dias e não foi identificado até hoje. Pedir: a confirmação do recebimento do lote, a previsão de pagamento e, se houver glosa ou pendência, o demonstrativo para análise. Tom cordial e objetivo; citar o número do protocolo de envio [ ]; sem nome de paciente e sem nada clínico. Depois, uma versão curta para registro no portal da operadora.
```
**Exemplo:** Entrada: lote de junho de 2026 do Vida Care: 19 guias, R$ 1.727, enviado em 06/07,
previsão 04/09 (60 dias), 10 dias de atraso em 14/09. Saída: e-mail de 130 palavras com assunto
"Lote 06/2026 · previsão de pagamento" e a versão curta para o portal.
**Confira:** as datas e o protocolo de envio. O que fazer se o convênio não responder (prazo,
notificação, ANS) é assunto do contrato e de quem cuida do jurídico; a IA não conhece o seu
contrato.

---

## Grupo 5 · Painel e sócios (8)

### Painel 01 · Explicar o mês ao sócio
**Quando usar:** na sexta de fechamento, com o Painel da clínica e o Resumo do mês. É o prompt
mais usado do kit.
**Cole:** Planilha 20 · aba Resumo ("Bloco único para copiar"), que reúne agenda, convênios, caixa,
particulares e orçamentos do mês.

```
Explique o mês de uma clínica médica para o meu sócio, em até 250 palavras e linguagem direta. Use só os números abaixo. Estrutura: uma frase com o resultado do mês; agenda (horas disponíveis × atendidas por profissional, ocupação, faltas e remarcações, o padrão); convênios (guias enviadas, pagas e glosadas, o convênio que mais glosou, prazo médio de pagamento); caixa (entrou, saiu, sobrou, provisão feita, repasse pago); particulares (a receber, atrasado); orçamentos (apresentados, aprovados, abertos); uma decisão para o mês que vem. Onde faltar explicação, escreva "[explicar]" para eu preencher. Não comente nenhum atendimento, diagnóstico ou paciente: só os números da gestão.
Meus comentários: [o que aconteceu, por quê].
Números:
[cole o bloco da aba Resumo]
```
**Exemplo:** Entrada: o bloco único de agosto da Planilha 20 da Clínica Vida Plena (entrou R$ 49.651,
saiu R$ 42.583, resultado R$ 7.068 e margem 14,2 %; ocupação 70,4 % e 118,3 horas atendidas; taxa de
falta 8,4 %; convênio a receber R$ 12.077 e glosa dos lotes pagos no mês 5,6 %; vencido R$ 4.005 e
inadimplência a prazo 10,5 %; orçamentos em aberto R$ 2.700); comentário: "a Dra. Renata teve duas
faltas no mesmo turno em 06/08; o lote de junho da Saúde Total foi pago em 05/08 com R$ 240 de glosa,
que entrou em recurso; o lote de maio do Vida Care caiu em 05/08; o repasse da Renata saiu no dia
10". Saída: texto de 240 palavras com um "[explicar]" na agenda (o bloco da 20 não traz ocupação por
sala: acrescente a da Planilha 1 à mão) e a decisão: "recorrer das duas guias glosadas de julho
(Saúde Total, R$ 170) até o dia 20 e confirmar por mensagem, na véspera, os retornos da terça de
manhã".
**Confira:** cada "[explicar]" e se nenhum número foi alterado. O bloco da 20 só tem totais: nunca
acrescente nome de paciente nos comentários.

### Painel 02 · Relatório mensal para os sócios
**Quando usar:** para a reunião de sócios, em vez do texto corrido do Painel 01: formato de
relatório, com destaques, atenções e próximos passos.
**Cole:** Planilha 20 · aba Resumo e a Planilha 18 · aba Painel (mês e mês anterior).

```
Escreva o relatório mensal de gestão de uma clínica médica para os sócios, em até 300 palavras, com a estrutura: Resultado do mês em uma frase (com o resultado do mês anterior ao lado); Destaques (3 tópicos com número); Pontos de atenção (até 3, com causa provável e ação); Próximos passos (3, com responsável e prazo). Tom profissional e direto, sem jargão contábil. Use apenas os números abaixo; onde faltar explicação, escreva "[explicar]". Nada sobre atendimentos ou pacientes.
Meus comentários: [o que aconteceu].
Números:
[cole o bloco da aba Resumo e a comparação do Painel da 18]
```
**Exemplo:** Entrada: agosto e julho da Vida Plena; comentário: "a manutenção de R$ 450 foi única; a
recepção começou a confirmação de véspera em agosto". Saída: relatório de 280 palavras: resultado
R$ 7.068 (julho: R$ 10.956), destaques (receita 7,9 % acima do previsto; convênios pagos R$ 11.161, o
maior mês de convênio do ano; taxa de falta caiu para 8,4 %), atenções (margem −6,3 p.p.; vencido R$ 4.005 e
inadimplência 10,5 % acima da meta de 8 %; ocupação 70,4 % contra meta de 75 %; um "[explicar]" na
agenda) e próximos passos com dono.
**Confira:** que o "extraordinário" apareça como tal e não como tendência.

### Painel 03 · Roteiro de 8 slides para a reunião de sócios
**Quando usar:** com o modelo de apresentação "Resultado do mês para os sócios" do kit (8 slides).
**Cole:** Planilha 20 · aba Resumo e os comentários do Painel 01.

```
Monte o roteiro de uma apresentação de 8 slides sobre o mês de [mês] de uma clínica médica, para os sócios, usando só os números abaixo. Para cada slide: título em uma frase que já diga a conclusão; 3 tópicos curtos; o número ou gráfico em destaque; uma frase do que eu falo. Estrutura: 1 capa; 2 resumo do mês; 3 agenda, ocupação e faltas; 4 preço e mix particular × convênio; 5 caixa, provisão e repasse; 6 convênios, parcelas e inadimplência; 7 orçamentos e metas do trimestre; 8 decisões que precisamos tomar. Onde faltar explicação, escreva "[explicar]". Nada sobre atendimentos ou pacientes.
Meus comentários: [o que aconteceu].
Números:
[cole]
```
**Exemplo:** Entrada: agosto da Vida Plena e os comentários do Painel 01. Saída: 8 slides; slide 4
"Consulta de convênio não cobre o custo cheio: das 130 consultas de agosto, 62 particulares deram
R$ 12.867 de resultado e as 68 de convênio, −R$ 2.987"; slide 8 com duas decisões: aporte de R$ 3.000
por mês na reserva e a conversa de tabela com o Vida Care.
**Confira:** cada "[explicar]"; o slide 8 precisa ter decisões de verdade, não "alinhar".

### Painel 04 · Perguntas difíceis que o sócio vai fazer
**Quando usar:** na véspera da reunião de sócios, para não ser pego de surpresa.
**Cole:** o relatório do Painel 02 ou o roteiro do Painel 03.

```
Com base no relatório abaixo, liste as 8 perguntas mais prováveis que um sócio cético faria e uma resposta curta e honesta para cada, incluindo o que dizer quando eu não souber ("não tenho o dado agora; trago até sexta"). Marque as 3 mais difíceis. As perguntas devem ser de gestão (dinheiro, agenda, convênios, parcelas, equipe), não sobre atendimentos ou pacientes.
Relatório:
[cole]
```
**Exemplo:** Entrada: o relatório de agosto do Painel 02. Saída: 8 perguntas ("por que a margem caiu
de 20,5 % para 14,2 % se os convênios pagaram mais?", "quanto do a receber dos convênios vai virar
glosa?", "a provisão cobre a guia de setembro?", "vale manter o Vida Care?"), respostas curtas e as
três mais difíceis marcadas.
**Confira:** as respostas devem ser as suas; use as da IA como rascunho.

### Painel 05 · Meta realista para o trimestre
**Quando usar:** no início do trimestre, com o histórico dos últimos meses, para preencher a
Planilha 19.
**Cole:** Planilha 18 · aba Resultado (receita e resultado dos últimos 6 meses), Planilha 17 · aba
Histórico (ocupação, faltas, glosa, inadimplência) e a Planilha 15 (orçamentos abertos).

```
Com o histórico abaixo de uma clínica médica, sugira metas para o próximo trimestre em três cenários (conservador, provável, ambicioso) para: receita recebida, resultado, ocupação da agenda, taxa de falta, glosa e inadimplência a prazo. Explique o cálculo de cada um (média, tendência, sazonalidade, feriados, férias dos profissionais). Diga o que precisaria acontecer para o ambicioso e o que ameaça o conservador. Não conte com pacientes novos nem com convênio novo no cenário provável; não sugira divulgação.
Histórico mês a mês:
[cole]
Orçamentos abertos: [valor e quantidade]
```
**Exemplo:** Entrada: receita de março a agosto (R$ 48.330, 39.555, 44.745, 44.160, 53.461, 49.651),
resultado, ocupação de julho e agosto (71,7 % e 70,4 %), taxa de falta (8,8 % e 8,4 %), glosa dos lotes
pagos no mês (4,3 % e 5,6 %), inadimplência (10,0 % e 10,5 %), 6 orçamentos abertos somando R$ 3.460.
Saída: receita mensal conservadora em torno de R$ 44.000, provável R$ 48.000, ambiciosa R$ 52.000 (com
a Sala 2 acima de 75 %); ocupação provável 74 %; e a ameaça ao conservador: "outubro tem feriado e o
Dr. Paulo tira férias em novembro".
**Confira:** a sazonalidade que você conhece (férias, feriados, congresso); a IA só viu seis meses.

### Painel 06 · Meta × realizado: explicar o desvio
**Quando usar:** no meio e no fim do trimestre, com a Planilha 19 mostrando o ritmo da meta.
**Cole:** Planilha 19 · aba Metas ("Todos os resultados-chave": partida, meta, atual, progresso,
esperado, semáforo).

```
Compare meta e realizado do trimestre de uma clínica médica. Para cada resultado-chave: % atingido, % do tempo decorrido, o que falta por semana até o fim e se está "no ritmo", "atrás" ou "à frente" (lembre que em alguns, menor é melhor). Depois: os dois mais atrás e, para cada um, três causas possíveis de gestão e uma ação para as próximas duas semanas. Separe "o que os números mostram" de "hipóteses". Nada sobre atendimentos ou pacientes.
Metas:
[cole]
Hoje é [data]; o trimestre vai de [data] a [data].
```
**Exemplo:** Entrada: 14/09/2026, 3º trimestre (semana 11 de 13, 82 % decorrido); os 9
resultados-chave da Vida Plena: ocupação nas últimas 4 semanas 74,5 % (meta 80 %, partida 75,2 %);
taxa de falta 7,1 % (meta 5 %); lista de retorno 8 (meta 8, atingido); glosa no ano 5,5 % (meta 4 %);
prazo real dos lotes 44 dias (meta 40); glosa recuperada R$ 200 (meta R$ 1.000); inadimplência 9,4 %
(meta 8 %); reserva R$ 14.000 (meta R$ 17.000); conta de provisão R$ 17.500 (meta R$ 17.527). Saída:
6 em risco, 1 em atenção, 1 no ritmo, 1 atingido, progresso médio 45 %; os dois mais atrás (ocupação, que caiu em vez de subir; glosa
recuperada, 20 %); causas e ações ("recorrer das duas guias glosadas de julho esta semana", "oferecer
as vagas de quinta à tarde à lista de retorno").
**Confira:** a conta do ritmo por semana; refaça você.

### Painel 07 · Trazer um médico parceiro ou abrir um turno: os números antes da decisão
**Quando usar:** antes de trazer um médico parceiro por repasse, abrir um turno novo, contratar
uma segunda recepcionista ou alugar outra sala. Não decide; organiza a conta.
**Cole:** Planilha 17 · aba Painel (ocupação, horas vazias, caixa, vencido), Planilha 1 · "Por sala"
(turnos por semana, horas vazias), Planilha 5 (custo fixo, custo da estrutura por hora) e Planilha 11
(margem da parceria atual).

```
Vou tomar a decisão: [ex.: trazer um segundo médico parceiro por repasse de 50 % para dois turnos na Sala 2 / contratar uma segunda recepcionista por R$ 3.100 com encargos / manter como está]. Com os dados abaixo de uma clínica médica, liste: 1) o que os dados sustentam; 2) o que eles NÃO respondem; 3) o custo mensal total da decisão e quanta produção a mais ela precisa gerar para se pagar (custo ÷ o que fica com a clínica por hora); 4) cinco perguntas que eu deveria responder antes de decidir; 5) o pior cenário realista e como me proteger dele; 6) uma versão menor ou reversível da mesma decisão. Não me diga o que decidir; não conte com pacientes que ainda não existem; nada sobre atendimentos.
Dados:
[cole]
```
**Exemplo:** Entrada: "trazer um segundo parceiro para a Sala 2 na segunda e na quarta à tarde"; a
Sala 2 tem 4 turnos por semana e 8,2 horas vazias em setembro (66 % de ocupação); a Sala 1 tem 6 turnos
e 90 %; custo da estrutura R$ 71,43 por hora; a parceria atual (Dra. Renata) deixa com a clínica
R$ 5.190 em agosto por 23,7 horas e a margem da parceria no ano é R$ 39.114; caixa livre R$ 26.836;
reserva R$ 14.000; vencido R$ 3.775. Saída: os dados sustentam que há sala e recepção ociosas nas
tardes de segunda e quarta; não respondem se há demanda; custo da decisão perto de zero fixo (repasse
é variável), mas dois turnos de 4 horas por semana são cerca de 32 horas por mês, que custam R$ 2.286
de estrutura (32 × R$ 71,43); como a clínica fica com metade da produção no repasse de 50 %, o novo
turno precisa de cerca de R$ 4.600 de produção por mês só para pagar a estrutura; versão reversível:
um turno por três meses, com data de revisão.
**Confira:** as horas vazias por sala (Planilha 1) e o custo da estrutura por hora (05), que a IA
chuta. A formalização da parceria é pergunta para o contador e para quem cuida do jurídico.

### Painel 08 · Segunda opinião sobre uma decisão da clínica
**Quando usar:** antes de uma decisão de gestão que custa dinheiro ou é difícil de desfazer: mudar
de sala, assinar um software, descredenciar um convênio, comprar um equipamento, dar desconto
grande.
**Cole:** o que for relevante do Painel da Planilha 17; sem nomes.

```
Vou tomar a decisão de gestão: [descreva]. Meus motivos: [liste]. Faça o papel do advogado do diabo: os três melhores argumentos contra, o que eu posso estar ignorando, e uma versão menor ou reversível da mesma decisão. Depois, diga honestamente se os argumentos contra são fortes ou fracos. Não entre em nenhuma questão clínica, ética ou regulatória da decisão (CFM, ANS, contrato, publicidade médica): isso é comigo e com quem cuida do jurídico.
Dados de apoio:
[cole]
```
**Exemplo:** Entrada: "assinar um software de clínica de R$ 300 por mês só pela agenda online e
confirmação automática; motivos: a recepção gasta 1 hora por dia confirmando". Saída: três argumentos
contra (R$ 3.600 por ano equivalem a 18 horas de custo da clínica a R$ 200; a confirmação de véspera
por mensagem já derrubou a falta de 10,9 % para 5,8 % sem software; o problema pode ser de rotina, não
de ferramenta), o que estou ignorando (o teste gratuito e o custo de migrar o cadastro), versão
reversível (assinar por três meses com data de revisão) e o veredito.
**Confira:** a decisão continua sua. Se ela envolve regra do CFM, da ANS ou contrato, é assunto do
seu jurídico, não da IA.

---

## Modelo em branco para criar os seus

```
Papel: você é [assistente de gestão de uma clínica médica; não dá orientação clínica nem escreve divulgação].
Contexto: [quem sou, para quem é, o que já tenho].
Tarefa: [o que fazer, em uma frase].
Formato: [tabela, lista, mensagem, até N palavras].
Regras: [o que não fazer; marque dúvidas com colchetes; use só os dados colados; nada sobre pacientes].
Dados (sem nome de paciente, sem contato, sem nada de saúde):
[cole]
```
**Exemplo:** Entrada: sócia da Vida Plena; explicar à recepcionista como fechar o caixa do dia e
lançar no Caixa (09) toda tarde; formato: passo a passo de 8 itens. Saída: lista de 8 passos com o que
conferir (Pix, cartão, dinheiro), em que ordem, como lançar uma linha por dia e forma de pagamento e
o que fazer quando um valor não bate.

Suporte: suporte@seusociogestor.com.br · Reembolso em até 7 dias.
