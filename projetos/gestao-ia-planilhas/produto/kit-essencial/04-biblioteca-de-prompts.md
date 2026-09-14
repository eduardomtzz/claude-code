# Biblioteca de prompts · Kit IA no Trabalho · Essencial

Versão 1.0 · setembro de 2026 · Seu Sócio Gestor

40 prompts em 6 grupos. Cada um tem: quando usar, o prompt pronto (troque o que está entre
colchetes), um exemplo de uso e o que conferir na resposta. Funcionam no ChatGPT, no Copilot,
no Gemini e no Claude, inclusive nas versões gratuitas.

## Antes de começar: três regras

1. **Nunca cole dado pessoal ou sigiloso em uma IA pública.** Nome de cliente, CPF, telefone,
   salário de alguém, contrato, diagnóstico, processo. Troque por "Cliente A", "Fornecedor 2".
   Os exemplos deste kit usam dados fictícios de propósito.
2. **A IA erra com confiança.** Todo número, data, nome e conclusão precisa ser conferido por
   você antes de virar e-mail, relatório ou decisão. Cada prompt diz o que revisar.
3. **Contexto é o segredo.** Quanto melhor você explica quem lê, para quê, e o que já tem, melhor
   a resposta. Por isso os prompts começam com o papel e o contexto.

Como usar: copie o prompt inteiro, cole na IA, substitua os colchetes, cole os seus dados onde
indicado e envie. Se a resposta vier ruim, não reescreva o prompt: responda "Refaça: [o que
faltou]".

---

## Grupo 1 · Organizar (5)

### Organizar 01 · Lista bagunçada vira tarefas prontas
**Quando usar:** depois de uma reunião, de um e-mail longo ou de um áudio transcrito. Gera as
linhas para colar na planilha Semana Organizada.

```
Você é meu assistente de organização. Vou colar um texto bagunçado com coisas que preciso fazer.
Transforme em uma tabela com as colunas: Tarefa | Projeto ou cliente | Responsável | Prazo | Impacto (1-3) | Urgência (1-3) | Horas estimadas.
Regras: uma tarefa por linha, começando com verbo no infinitivo; se o prazo não estiver no texto, escreva "definir"; impacto 3 = afeta cliente ou receita, 1 = interno e pequeno; urgência 3 = vence esta semana, 1 = sem pressa; horas como sua melhor estimativa, entre 0,5 e 8. Hoje é [data]. Meu nome é [seu nome].
Texto:
[cole aqui]
```
**Exemplo:** Entrada: "gente, lembrando que a diretoria quer o relatório até sexta, e a Aurora
pediu desconto na proposta, alguém revisa? o post de terça precisa aprovar hoje, e preciso
conferir as faturas dos fornecedores essa semana." Saída: tabela com 4 linhas ("Enviar relatório
de setembro para a diretoria", prazo sexta, impacto 3, urgência 3, 2 h; "Revisar proposta
comercial da Aurora", responsável "definir"...), prontas para colar na aba Tarefas.
**Confira:** prazos inferidos, responsável (a IA chuta), impacto e urgência (ajuste ao seu
critério).

### Organizar 02 · Dia planejado em blocos
**Quando usar:** de manhã, com a lista de tarefas do dia da aba Hoje.

```
Monte o meu dia de trabalho em blocos de tempo, das [hora de início] às [hora de fim], com almoço de [minutos] minutos. Coloque primeiro o que exige mais concentração. Tarefas de hoje, com horas estimadas:
[cole as linhas da aba Hoje]
Compromissos fixos: [ex.: reunião 14h às 15h].
Se não couber tudo, diga o que ficaria para amanhã e por quê. Responda em tabela: Horário | Tarefa | Observação.
```
**Exemplo:** Entrada: das 9h às 18h, almoço de 60 min; tarefas da aba Hoje da Ana (Prisma): enviar
relatório (2 h), montar apresentação da Horizonte (3 h), revisar proposta da Aurora (1,5 h),
atualizar planilha de leads (1 h); reunião fixa das 14h às 15h. Saída: tabela de blocos com a
apresentação logo às 9h, a reunião respeitada e "atualizar leads" empurrada para amanhã, com o
motivo (faltou 1 hora).
**Confira:** se os blocos respeitam suas reuniões e se a IA não inventou tarefas.

### Organizar 03 · Prioridade quando tudo parece urgente
**Quando usar:** quando a lista tem mais de 10 tarefas abertas e você não sabe por onde começar.

```
Ajude-me a priorizar. Para cada tarefa abaixo, classifique em uma das quatro caixas: Fazer agora (alto impacto, urgente), Agendar (alto impacto, não urgente), Delegar ou simplificar (baixo impacto, urgente), Cortar (baixo impacto, não urgente). Explique em uma frase por que cada uma caiu na caixa. No fim, diga as três que eu deveria fazer hoje.
Contexto do meu trabalho: [uma frase sobre o que você faz e o que é mais importante este mês].
Tarefas:
[cole aqui]
```
**Exemplo:** Entrada: as 14 tarefas abertas da aba Tarefas da Prisma; contexto: "analista de
marketing; o mais importante este mês é o relatório da diretoria e a proposta da Aurora". Saída:
quatro caixas com uma frase por tarefa; "Responder pesquisa de clima" e "Organizar pasta de fotos"
foram para Delegar e Cortar; as três de hoje: relatório, apresentação da Horizonte, proposta da
Aurora.
**Confira:** a IA não conhece sua política; ajuste antes de cortar algo.

### Organizar 04 · Ata de reunião em 5 minutos
**Quando usar:** logo depois da reunião, com suas anotações soltas ou a transcrição.

```
Transforme estas anotações em uma ata curta com quatro partes: Decisões tomadas; Tarefas (quem, o quê, até quando); Pendências sem dono; Próxima reunião. Use frases curtas. Não invente decisões que não estão no texto; se algo ficou ambíguo, marque com "[confirmar]".
Reunião: [assunto], em [data], com [participantes por função, sem nomes se preferir].
Anotações:
[cole aqui]
```
**Exemplo:** Entrada: reunião "Alinhamento Aurora", 14/09, gerente de conta e analista; anotações:
"cliente quer 10% de desconto, Ana vê a margem até quarta; pauta de outubro fecha dia 16 (Carla);
vídeo institucional: orçamento ainda sem dono; próxima reunião 21/09, hora a combinar". Saída: ata
com 1 decisão, 2 tarefas com dono e prazo, 1 pendência sem dono (orçamento do vídeo) e
"[confirmar]" na hora da próxima reunião.
**Confira:** cada "[confirmar]" e os prazos.

### Organizar 05 · Semana revisada na sexta
**Quando usar:** no fechamento de sexta, com o que foi feito e o que ficou.

```
Faça a minha revisão semanal. Com a lista abaixo (tarefas feitas, atrasadas e para a próxima semana), responda: 1) o que andou de mais importante; 2) o que travou e a causa provável; 3) três ajustes simples para a próxima semana; 4) uma mensagem de duas linhas que eu possa mandar para [chefe/cliente/equipe] resumindo a semana. Tom direto, sem elogio vazio.
Lista:
[cole aqui]
```
**Exemplo:** Entrada: feitas: relatório de mídia de agosto, backup mensal; atrasadas: proposta da
Aurora, pesquisa de clima; próxima semana: apresentação da Horizonte, pauta de outubro. Saída: os
quatro blocos; causa provável do atraso: "a proposta esperava a decisão sobre o desconto";
mensagem de duas linhas para a diretoria, pronta para copiar.
**Confira:** se a "causa provável" faz sentido; a IA não viu o que aconteceu.

---

## Grupo 2 · Analisar dados (8)

### Analisar 01 · O que esses números dizem
**Quando usar:** com qualquer tabela pequena (até 50 linhas) que você quer entender rápido.

```
Você é um analista objetivo. Vou colar uma tabela. Faça: 1) descreva em três frases o que a tabela mostra; 2) aponte os cinco fatos mais relevantes com os números; 3) liste anomalias ou valores que parecem errados; 4) diga o que você perguntaria antes de tirar conclusões. Não invente causas: separe claramente "o que os dados mostram" de "hipóteses".
Contexto: [o que é a tabela, período, unidade dos valores].
Tabela:
[cole aqui]
```
**Exemplo:** Entrada: a tabela da aba Indicadores da Prisma Comunicação, janeiro a setembro de
2026, 12 indicadores em R$, % e unidades. Saída: três frases (receita em alta, inadimplência em
queda), cinco fatos com número (receita de 131.200 em setembro, a maior do ano) e uma anomalia
para conferir: horas extras caíram de 26 para 12 enquanto os atendimentos subiram.
**Confira:** recalcule mentalmente um ou dois números citados.

### Analisar 02 · Comparar dois períodos
**Quando usar:** mês contra mês, trimestre contra trimestre, com a aba Painel do Relatório Mensal.

```
Compare os dois períodos abaixo, indicador por indicador. Para cada um: variação absoluta, variação percentual e um comentário de uma linha. Depois, os três maiores avanços, os três maiores recuos e uma conclusão de duas frases. Classifique os indicadores em "melhorou", "piorou" ou "estável" (estável = variação menor que [2]%). Lembre que para alguns indicadores menor é melhor: [liste quais].
Período 1 ([nome]):
[cole]
Período 2 ([nome]):
[cole]
```
**Exemplo:** Entrada: o Painel da Prisma, agosto contra setembro; menor é melhor: Despesas,
Inadimplência, Horas extras, Custo por lead; estável = variação menor que 2%. Saída: tabela com os
12 indicadores; receita +5,3% (124.600 para 131.200, melhorou), despesas +2,9% (piorou), leads 142
para 137 (−3,5%, piorou) e uma conclusão de duas frases.
**Confira:** sinais de "menor é melhor" e percentuais.

### Analisar 03 · Onde cortar gastos
**Quando usar:** com a tabela "Para onde foi o dinheiro" da planilha Ganhos e Gastos.

```
Analise meus gastos por categoria e me ajude a decidir onde cortar sem prejudicar o essencial. Para cada categoria: é fixo ou variável? É essencial, importante ou supérfluo? Quanto seria realista reduzir em 30 dias e como? Depois, monte um plano com três cortes que somem pelo menos R$ [valor alvo] por mês, do mais fácil ao mais difícil. Seja específico e não moralize.
Contexto: [pessoa ou negócio, renda média mensal, objetivo do corte].
Gastos do mês:
[cole aqui]
```
**Exemplo:** Entrada: gastos de setembro da Rafa Design por categoria (Moradia 1.660, Alimentação
cerca de 930, Saúde 390, Educação 297, Ferramentas 189, Transporte cerca de 180, Marketing 150,
Lazer cerca de 140); contexto: designer autônomo, renda média de R$ 6.000, quer sobrar R$ 500 a
mais por mês. Saída: cada categoria marcada como fixa ou variável e essencial, importante ou
supérflua; três cortes (almoços fora, lazer, adiar o curso) que somam pouco mais de R$ 500.
**Confira:** a IA não sabe o que é essencial para você; ajuste a classificação.

### Analisar 04 · Meta realista
**Quando usar:** para definir a meta de um indicador com base no histórico.

```
Com o histórico abaixo, sugira uma meta mensal para os próximos três meses em três cenários: conservador, provável e ambicioso. Explique o cálculo de cada um (média, tendência, sazonalidade). Diga o que precisaria acontecer para atingir o cenário ambicioso.
Indicador: [nome, unidade, maior é melhor ou menor é melhor].
Histórico mês a mês:
[cole]
```
**Exemplo:** Entrada: indicador "Leads recebidos, unidades, maior é melhor"; histórico de janeiro
a setembro: 88, 95, 110, 102, 131, 118, 109, 142, 137. Saída: conservador em torno de 125,
provável 135 e ambicioso 150 por mês, com o cálculo de cada um (média dos últimos meses e
tendência) e o que precisaria acontecer para o ambicioso (campanha de fim de ano no ar em
outubro).
**Confira:** se a IA respeitou a sazonalidade que você conhece.

### Analisar 05 · Achar o erro na planilha
**Quando usar:** quando um total não bate ou um número parece estranho.

```
Vou colar um trecho de planilha em que algo não bate. Ajude-me a encontrar o erro: verifique somas, percentuais, sinais, unidades e valores repetidos ou faltando. Liste cada suspeita com a célula ou linha, o que esperava e o que encontrou. Se precisar de mais contexto, diga exatamente qual.
O que eu esperava: [ex.: o total deveria ser 12.400].
Trecho:
[cole]
```
**Exemplo:** Entrada: "esperava que Sobrou fosse Entrou menos Saiu"; trecho do painel de setembro
da Rafa Design: Entrou 6.670, Saiu 4.580, Sobrou 1.590. Saída: aponta que 6.670 − 4.580 = 2.090,
não 1.590; suspeita de um lançamento de R$ 500 contado duas vezes (a transferência para a reserva)
e pede a aba Lançamentos para confirmar.
**Confira:** tudo. Este prompt encontra suspeitas, não prova erros.

### Analisar 06 · Perguntas antes de decidir
**Quando usar:** antes de uma decisão com base em números (contratar, comprar, cortar).

```
Vou tomar a decisão: [descreva]. Com os dados abaixo, liste: 1) o que os dados sustentam; 2) o que eles NÃO respondem; 3) cinco perguntas que eu deveria responder antes de decidir; 4) o pior cenário realista e como me proteger dele. Não me diga o que decidir; me ajude a pensar.
Dados:
[cole]
```
**Exemplo:** Entrada: decisão "contratar um segundo designer júnior na Prisma"; dados: receita de
janeiro a setembro, atendimentos de 52 para 63, horas extras de 26 para 12. Saída: os dados
sustentam que a demanda cresceu; não respondem quanto desse trabalho é design; cinco perguntas
(custo total, prazo de retorno, freelancer como alternativa...); pior cenário: receita cair e o
custo fixo ficar.
**Confira:** as perguntas costumam ser o mais útil; os cenários são hipóteses.

### Analisar 07 · Gráfico certo para o dado
**Quando usar:** antes de montar um gráfico para relatório ou slide.

```
Quero mostrar [o que você quer que a pessoa entenda] para [público]. Os dados são: [descreva as colunas e o período]. Indique o tipo de gráfico mais adequado, o que vai em cada eixo, se precisa de linha de meta, e o título em uma frase que já diga a conclusão (ex.: "Receita cresceu 12% em setembro, puxada por serviços"). Diga também o que evitar (ex.: pizza com 12 fatias).
```
**Exemplo:** Entrada: "quero mostrar para a diretoria que a inadimplência caiu em 2026; dados: mês
e inadimplência em %, janeiro a setembro; meta de 3%". Saída: gráfico de linha com a meta
pontilhada, eixo em %, título "Inadimplência caiu de 4,1% para 2,4% e fechou dois meses seguidos
abaixo da meta"; evitar pizza e eixo que não começa em zero.
**Confira:** título deve ser verdadeiro para os seus dados.

### Analisar 08 · Resumo executivo de uma tabela grande
**Quando usar:** quando a tabela tem muitas linhas e você só precisa da essência.

```
Resuma a tabela abaixo em no máximo 120 palavras para alguém que tem um minuto: comece pela conclusão principal, dê os dois números que a sustentam, aponte o maior risco e termine com a ação recomendada. Sem adjetivos, sem introdução.
Contexto: [o que é, período, unidade].
Tabela:
[cole]
```
**Exemplo:** Entrada: a aba Lançamentos da Rafa Design, julho a setembro, cerca de 50 linhas,
valores em R$. Saída: 100 palavras: sobrou dinheiro nos três meses; os dois números (cerca de
6.700 de entrada em setembro, 500 por mês para a reserva); risco: duas contas a pagar vencendo dia
30; ação: quitar as duas antes de comprar equipamento novo.
**Confira:** os dois números citados.

---

## Grupo 3 · Escrever (10)

### Escrever 01 · Relatório executivo a partir do Resumo
**Quando usar:** com o "Bloco único para copiar" da planilha Relatório Mensal Pronto.

```
Escreva o relatório mensal para [quem lê: diretoria, cliente, sócio], em até 300 palavras, com a estrutura: Resultado do mês em uma frase; Destaques (3 tópicos com número); Pontos de atenção (até 3, com causa e ação); Próximos passos (3, com responsável e prazo). Tom profissional e direto, sem jargão. Use apenas os números abaixo; onde faltar explicação, escreva "[explicar]" para eu preencher.
Meus comentários sobre o mês: [o que aconteceu, por quê].
Números:
[cole o bloco da aba Resumo]
```
**Exemplo:** Entrada: para a diretoria; o "Bloco único para copiar" da aba Resumo da Prisma,
setembro de 2026; comentário: "receita subiu com dois projetos novos da Horizonte; despesas
subiram com o freelancer de vídeo". Saída: relatório de cerca de 250 palavras com os quatro blocos
e um "[explicar]" na queda dos leads, que o comentário não cobria.
**Confira:** cada "[explicar]" e se nenhum número foi alterado.

### Escrever 02 · E-mail curto que pede algo
**Quando usar:** pedido de aprovação, informação, prazo.

```
Escreva um e-mail de até 120 palavras para [pessoa e cargo] pedindo [o quê] até [prazo]. Comece pelo pedido na primeira frase, explique o motivo em duas linhas, diga o que acontece se não vier no prazo (sem ameaça) e termine com uma pergunta fechada. Assunto de até 8 palavras. Tom: [cordial e direto / formal].
Contexto extra: [o que a pessoa já sabe].
```
**Exemplo:** Entrada: para a gerente de marketing da Aurora, pedindo a aprovação da pauta de
outubro até quarta, 16/09; tom cordial e direto; ela já recebeu a pauta na sexta. Saída: e-mail de
cerca de 90 palavras, assunto "Pauta de outubro: aprovação até quarta?", pedido na primeira frase
e pergunta fechada no fim.
**Confira:** prazo e o que exatamente você está pedindo.

### Escrever 03 · Responder um e-mail difícil
**Quando usar:** reclamação, cobrança, pedido de desconto, crítica.

```
Recebi o e-mail abaixo e preciso responder. Meu objetivo: [ex.: manter o cliente sem dar o desconto]. Minha posição: [o que posso e não posso ceder]. Escreva a resposta em até 150 palavras: reconheça o ponto da pessoa em uma frase, exponha a posição com clareza, ofereça uma alternativa concreta e feche com próximo passo. Sem pedir desculpas em excesso e sem tom defensivo.
E-mail recebido (sem dados pessoais):
[cole]
```
**Exemplo:** Entrada: objetivo "manter a Aurora sem dar os 10% de desconto"; posição "posso
parcelar em 3 vezes ou tirar uma entrega do escopo"; e-mail do cliente pedindo o desconto. Saída:
resposta de cerca de 130 palavras que reconhece o pedido, mantém o valor, oferece as duas
alternativas e fecha com uma ligação na quinta.
**Confira:** se a resposta não promete o que você não pode cumprir.

### Escrever 04 · Justificativa para chefe ou cliente
**Quando usar:** explicar um atraso, um custo a mais, uma mudança de escopo.

```
Escreva uma justificativa de até 180 palavras para [quem] sobre [o fato]. Estrutura: o que aconteceu (fato, sem culpa); impacto real (prazo, custo, qualidade); o que já foi feito; o que proponho; o que preciso da pessoa. Tom responsável e objetivo, sem desculpas em cascata.
Fatos:
[cole]
```
**Exemplo:** Entrada: para a diretoria, atraso de três dias no relatório de setembro; fatos: os
dados de vendas chegaram na sexta e não na quarta, o gráfico teve de ser refeito, nova data terça.
Saída: justificativa de cerca de 150 palavras, sem culpar a equipe de vendas, propondo antecipar o
prazo dos dados no próximo mês e pedindo o "de acordo" com a nova data.
**Confira:** que os fatos estejam corretos e que a proposta seja viável.

### Escrever 05 · Explicar o mês financeiro para alguém
**Quando usar:** com o Painel de Ganhos e Gastos, para explicar a um sócio, cliente ou à família.

```
Explique o resultado financeiro do mês para [quem, e o quanto entende de números], em até 200 palavras e linguagem simples: quanto entrou, quanto saiu, quanto sobrou, para onde foi a maior parte, o que mudou em relação ao mês anterior e uma decisão sugerida para o próximo mês. Sem termos técnicos.
Números:
[cole o painel]
Contexto: [o que aconteceu de diferente no mês].
```
**Exemplo:** Entrada: o Painel de setembro da Rafa Design (entrou cerca de 6.670, saiu cerca de
4.580, maior gasto: moradia); para "minha mãe, que não mexe com planilha"; contexto: "teve um
cliente a mais este mês". Saída: cerca de 180 palavras em linguagem de conversa; decisão sugerida:
manter os R$ 500 da reserva e adiar o curso para o mês que vem.
**Confira:** números e a decisão sugerida.

### Escrever 06 · Proposta comercial simples
**Quando usar:** orçamento ou proposta de serviço de uma página.

```
Escreva uma proposta de serviço de uma página para [cliente e ramo] com as seções: Entendimento do pedido (2 frases); O que será entregue (lista objetiva); O que não está incluído; Prazo; Investimento (R$ [valor], condições de pagamento [ex.: 50% na aprovação, 50% na entrega]); Validade da proposta ([dias]); Próximo passo. Tom profissional e claro. Não invente entregas além das listadas.
O pedido do cliente: [descreva].
O que vou entregar: [liste].
```
**Exemplo:** Entrada: cliente Padaria do Sol, identidade visual; entregar logo, paleta e três
aplicações; R$ 3.600, 50% na aprovação e 50% na entrega; 15 dias úteis; validade de 10 dias.
Saída: proposta de uma página com as sete seções; em "O que não está incluído" a IA listou site e
papelaria, que não estavam no pedido.
**Confira:** escopo, valor e condições; nada de promessa extra.

### Escrever 07 · Resumo de reunião para quem não foi
**Quando usar:** logo após a reunião, para atualizar quem faltou.

```
Escreva um resumo de até 150 palavras para [quem] que não participou da reunião sobre [assunto]. Comece com a decisão principal, depois o que muda para a pessoa, e o que ela precisa fazer (se algo). Anexe a lista de tarefas com prazo. Baseie-se só na ata abaixo.
Ata:
[cole]
```
**Exemplo:** Entrada: para o Bruno, que faltou à reunião de alinhamento da Aurora; a ata gerada
pelo Organizar 04. Saída: cerca de 120 palavras: a decisão (sem desconto, com parcelamento), o que
muda para o Bruno (atualizar a planilha de leads até quarta) e a lista de tarefas com prazo.
**Confira:** o que "muda para a pessoa" é interpretação; revise.

### Escrever 08 · Texto simplificado
**Quando usar:** quando seu texto ficou longo, técnico ou confuso.

```
Reescreva o texto abaixo para ser lido em metade do tempo, mantendo todo o conteúdo factual: frases curtas, voz ativa, sem jargão, sem repetição. Marque entre colchetes qualquer trecho em que você teve dúvida do sentido. Mantenha o tom [formal/informal].
Texto:
[cole]
```
**Exemplo:** Entrada: parágrafo de 180 palavras do relatório mensal, cheio de "em virtude de" e
"conforme mencionado anteriormente"; tom formal. Saída: 90 palavras com as mesmas informações e um
trecho entre colchetes onde a IA não soube se "resultado" era antes ou depois dos impostos.
**Confira:** cada colchete e se nada importante sumiu.

### Escrever 09 · Descrição de tarefa para delegar
**Quando usar:** quando vai passar uma tarefa para outra pessoa (equipe, estagiário, freelancer).

```
Escreva a descrição de uma tarefa para eu delegar a [quem, nível de experiência]. Estrutura: objetivo em uma frase; o que exatamente entregar (formato, tamanho, exemplo); como saberemos que está bom (3 critérios); o que evitar; prazo e onde entregar; a quem perguntar em caso de dúvida. Máximo 200 palavras.
Tarefa: [descreva do seu jeito].
```
**Exemplo:** Entrada: delegar ao estagiário, sem experiência, "atualizar a planilha de leads da
Aurora toda segunda". Saída: descrição de cerca de 170 palavras com três critérios (nenhuma linha
duplicada, data no formato 14/09/2026, status preenchido em todas as linhas), prazo (segunda até
12h) e a quem perguntar (Bruno).
**Confira:** critérios de qualidade são o que evita retrabalho; ajuste-os.

### Escrever 10 · Mensagem de cobrança educada
**Quando usar:** com a lista "a pagar" ou um recebível atrasado.

```
Escreva três versões de mensagem de cobrança para [cliente], sobre [o que, valor R$ [ ], vencido em [data]]: 1) lembrete amigável (primeiro contato); 2) segunda cobrança, firme e cordial; 3) última antes de suspender o serviço, clara e sem ameaça. Cada uma com até 80 palavras, com Pix/forma de pagamento e um caminho fácil para resolver. Tom respeitoso: presuma que foi esquecimento.
```
**Exemplo:** Entrada: cliente Bistrô 42, cardápio, R$ 950, vencido em 20/09, pagamento por Pix.
Saída: três mensagens de até 80 palavras, do lembrete amigável à última antes de suspender o
serviço, todas com a chave Pix, o valor e a data.
**Confira:** valor, data e o que você realmente fará se não pagarem.

---

## Grupo 4 · Apresentar (6)

### Apresentar 01 · Roteiro de 8 slides a partir do Resumo
**Quando usar:** com o bloco da aba Resumo e o modelo de 8 slides do kit.

```
Monte o roteiro de uma apresentação de 8 slides sobre os resultados de [mês] para [público], usando só os números abaixo. Para cada slide: título em uma frase que já diga a conclusão; 3 tópicos curtos; o gráfico ou número em destaque; uma frase do que eu falo. Estrutura: 1 capa; 2 resumo do mês; 3 destaque positivo; 4 destaque positivo; 5 ponto de atenção; 6 ponto de atenção; 7 próximos passos; 8 pedido ou decisão necessária. Onde faltar explicação, escreva "[explicar]".
Meus comentários: [o que aconteceu].
Números:
[cole]
```
**Exemplo:** Entrada: setembro, para a diretoria da Prisma; o bloco da aba Resumo e os comentários
do Escrever 01. Saída: roteiro de 8 slides; slide 3 "Receita bateu 131 mil, 9% acima da meta";
slide 5 com "[explicar]" na queda dos leads; slide 8 pede aprovar o freelancer de vídeo para
outubro.
**Confira:** cada "[explicar]"; o slide 8 precisa ser um pedido real.

### Apresentar 02 · Fala de abertura de 60 segundos
**Quando usar:** para começar a reunião ou a apresentação sem enrolar.

```
Escreva o que eu digo nos primeiros 60 segundos da apresentação sobre [assunto] para [público]: o que vamos ver, por que importa para eles, qual a decisão que preciso no fim, e quanto tempo vai durar. Máximo 120 palavras, linguagem falada, sem "bom dia a todos" genérico.
```
**Exemplo:** Entrada: apresentação dos resultados de setembro para a diretoria da Prisma; decisão
que preciso: aprovar o freelancer de vídeo; 20 minutos. Saída: fala de cerca de 100 palavras que
começa pelo resultado do mês, diz o que vai ser mostrado e termina com a decisão pedida.
**Confira:** a decisão que você pede no fim deve ser a mesma do slide 8.

### Apresentar 03 · Perguntas prováveis e respostas
**Quando usar:** na véspera, para não ser pego de surpresa.

```
Com base no roteiro abaixo, liste as 8 perguntas mais prováveis de [público] e uma resposta curta e honesta para cada, incluindo o que dizer quando eu não souber. Marque as 3 mais difíceis.
Roteiro:
[cole]
```
**Exemplo:** Entrada: o roteiro dos 8 slides de setembro; público: diretoria. Saída: 8 perguntas
("por que os leads caíram?", "o que acontece se não contratar o freelancer?") com respostas curtas
e um "não tenho o dado agora, trago até sexta" para a que não dá para responder; as três mais
difíceis marcadas.
**Confira:** respostas honestas; não use as que prometem o que você não sabe.

### Apresentar 04 · Um slide que explica tudo
**Quando usar:** quando só há tempo para um slide.

```
Condense o assunto abaixo em UM slide: título-conclusão (até 12 palavras), três tópicos com número, um gráfico sugerido (tipo e o que mostra) e uma frase de pedido. Máximo 60 palavras no slide.
Assunto e dados:
[cole]
```
**Exemplo:** Entrada: "resultado de setembro da Prisma: receita 131.200 (meta 120.000),
inadimplência 2,4%, leads 137 (142 em agosto); pedido: aprovar freelancer de vídeo". Saída: título
"Setembro fechou 9% acima da meta com a menor inadimplência do ano", três tópicos com número,
gráfico de barras receita × meta e uma frase de pedido.
**Confira:** os três números.

### Apresentar 05 · Transformar relatório em apresentação
**Quando usar:** quando o relatório já existe e você precisa apresentar.

```
Transforme o relatório abaixo em uma apresentação de [n] slides. Um tema por slide, título-conclusão, no máximo 25 palavras por slide, e uma nota do apresentador com o que falar (até 40 palavras). Corte tudo que não muda uma decisão.
Relatório:
[cole]
```
**Exemplo:** Entrada: o relatório de setembro de 300 palavras gerado pelo Escrever 01; 6 slides.
Saída: 6 slides com título-conclusão e nota do apresentador; a IA cortou o parágrafo de contexto
sobre o mercado e manteve os três pontos de atenção.
**Confira:** o que foi cortado; às vezes a IA corta o que importa.

### Apresentar 06 · Feedback do meu roteiro
**Quando usar:** com o roteiro pronto, antes de montar os slides.

```
Aja como um diretor exigente que vai assistir a esta apresentação. Aponte: onde perco a atenção; o que está em ordem errada; frases vagas e como torná-las concretas; slides que podem ser cortados; a pergunta desconfortável que você faria. Seja específico e direto.
Roteiro:
[cole]
```
**Exemplo:** Entrada: o roteiro dos 8 slides de setembro. Saída: apontou o slide 2 como vago ("mês
positivo"), sugeriu trocar a ordem dos dois pontos de atenção e fez a pergunta desconfortável:
"por que os leads caíram se o custo por lead também caiu?".
**Confira:** aplique só o que faz sentido para o seu público.

---

## Grupo 5 · Revisar (6)

### Revisar 01 · Revisão de texto antes de enviar
**Quando usar:** em todo texto que sai da sua mesa (e-mail, relatório, proposta), depois de pronto
e antes de enviar.

```
Revise o texto abaixo em três passes: 1) erros de português e digitação (liste com correção); 2) clareza (frases que podem ser mal entendidas, com sugestão); 3) tom (algo que pode soar rude, defensivo ou exagerado). Não reescreva tudo; aponte e sugira. Português do Brasil.
Texto:
[cole]
```
**Exemplo:** Entrada: e-mail de cobrança de 80 palavras para o Bistrô 42, escrito com o prompt
Escrever 10. Saída: dois erros de digitação com a correção, uma frase ambígua ("até dia 30", sem o
mês) e um aviso de tom ("caso contrário" soou como ameaça).
**Confira:** aceite as correções uma a uma.

### Revisar 02 · Conferir uma conta de porcentagem ou variação
**Quando usar:** antes de escrever uma variação em relatório, slide ou e-mail, ou quando dois
números não batem.

```
Confira os cálculos abaixo. Para cada linha, refaça a conta passo a passo e diga se está certa; se não, dê o valor correto. Explique a diferença entre variação percentual e pontos percentuais quando aparecer.
Cálculos:
[cole]
```
**Exemplo:** Entrada: "receita: 124.600 em agosto e 131.200 em setembro, variação de 5,3%;
inadimplência de 2,6% para 2,4%, queda de 0,2%". Saída: confirma os 5,3%; corrige o segundo: queda
de 0,2 ponto percentual, o que equivale a −7,7% em variação percentual.
**Confira:** este é o prompt em que a IA mais erra: refaça você o que for decisivo.

### Revisar 03 · Checar consistência entre planilha e texto
**Quando usar:** com o relatório escrito pela IA e a aba Painel ao lado, antes de enviar.

```
Compare os números do texto com os da tabela e liste toda divergência (número no texto, número na tabela, onde). Aponte também números citados no texto que não existem na tabela.
Texto:
[cole]
Tabela:
[cole]
```
**Exemplo:** Entrada: o relatório do Escrever 01 e a tabela do Painel de setembro da Prisma.
Saída: uma divergência (o texto diz "ticket médio de 9.400", a tabela mostra 9.700) e um número
sem origem ("crescimento de 15%" não existe na tabela).
**Confira:** as divergências apontadas; a IA pode deixar passar alguma.

### Revisar 04 · Simplificar uma fórmula ou explicar o que ela faz
**Quando usar:** quando herdar uma planilha de alguém ou quiser mexer em uma fórmula protegida do
kit.

```
Explique em português simples o que esta fórmula de planilha faz, passo a passo, e diga se há uma forma mais simples ou mais segura de escrevê-la (compatível com Excel e Google Sheets). Aponte casos em que ela pode dar erro (célula vazia, divisão por zero, texto no lugar de número).
Fórmula:
[cole]
```
**Exemplo:** Entrada: a fórmula da coluna "Dias para o prazo" da Semana Organizada,
=SE(D5="";"";D5-Config!$B$4). Saída: explicação passo a passo (se não há prazo, deixa vazio;
senão, prazo menos a data de referência), alerta de que dá erro se a data virar texto e a
recomendação de deixar como está.
**Confira:** teste a fórmula sugerida em uma cópia antes de trocar.

### Revisar 05 · Checklist antes de entregar
**Quando usar:** antes de uma entrega diferente das do kit (proposta, planilha nova, treinamento),
para adaptar o checklist do bônus.

```
Monte um checklist de verificação para [o que vou entregar: relatório, planilha, apresentação, proposta] para [público], com no máximo 12 itens, do mais crítico ao menos crítico. Inclua itens de número, de texto, de formato e de envio (destinatário, anexo, assunto).
```
**Exemplo:** Entrada: proposta comercial para a Padaria do Sol, cliente novo. Saída: 10 itens, do
mais crítico (valor e condições de pagamento iguais aos combinados por telefone) ao menos crítico
(nome do arquivo), incluindo "abrir o anexo antes de enviar".
**Confira:** use o checklist do bônus do kit como base e complete com o da IA.

### Revisar 06 · Segunda opinião sobre uma decisão
**Quando usar:** antes de uma decisão que custa dinheiro ou é difícil de desfazer (desconto,
contratação, cancelamento).

```
Vou tomar a decisão: [descreva]. Meus motivos: [liste]. Faça o papel do advogado do diabo: os três melhores argumentos contra, o que eu posso estar ignorando, e uma versão menor ou reversível da mesma decisão. Depois, diga honestamente se os argumentos contra são fortes ou fracos.
```
**Exemplo:** Entrada: "dar 10% de desconto para a Aurora; motivos: cliente antigo, mês fraco de
leads". Saída: três argumentos contra (abre precedente, come a margem, não resolve os leads), o
que estou ignorando (o cliente pode aceitar parcelar), versão reversível (desconto só por três
meses) e o veredito: os argumentos contra são "medianos, mas o precedente pesa".
**Confira:** a decisão continua sua.

---

## Grupo 6 · Aprender (5)

### Aprender 01 · Explicar um termo de planilha ou de gestão
**Quando usar:** quando um termo aparece em reunião, relatório ou na planilha e você não quer
perguntar na frente de todo mundo.

```
Explique "[termo]" para alguém que nunca estudou gestão, em até 100 palavras, com um exemplo do dia a dia de [seu tipo de trabalho]. Depois dê a definição técnica em uma frase.
```
**Exemplo:** Entrada: termo "ticket médio"; trabalho: agência de comunicação. Saída: explicação de
80 palavras com o exemplo da agência (receita do mês dividida pelo número de clientes atendidos) e
a definição técnica em uma frase.
**Confira:** o exemplo, que às vezes simplifica demais, e a definição técnica em uma segunda
fonte.

### Aprender 02 · Montar uma tabela dinâmica (passo a passo)
**Quando usar:** quando precisa cruzar duas colunas (por mês e por pessoa, por categoria e por
cliente) e o painel do kit não tem esse corte.

```
Tenho uma tabela com as colunas [liste] no [Excel/Google Sheets]. Quero ver [ex.: total de vendas por mês e por vendedor]. Me dê o passo a passo, clique por clique, para montar uma tabela dinâmica que mostre isso, e diga como atualizar quando eu incluir dados novos.
```
**Exemplo:** Entrada: colunas Data, Tipo, Categoria e Valor da aba Lançamentos, no Google Sheets;
quero o total por categoria e por mês. Saída: passo a passo (Inserir > Tabela dinâmica; Categoria
nas linhas, mês da data nas colunas, soma de Valor) e como ampliar o intervalo quando entrarem
linhas novas.
**Confira:** os nomes de menu mudam entre versões; se não achar, diga a versão para a IA.

### Aprender 03 · Escolher a função certa
**Quando usar:** quando sabe o que quer calcular e não sabe qual função faz isso.

```
No [Excel/Google Sheets], preciso [descreva o que quer calcular, com exemplo de entrada e saída]. Diga qual função usar, escreva a fórmula pronta para as células [ex.: valores em B2:B50, categorias em A2:A50], explique cada parte e dê uma alternativa mais simples se existir. Evite funções que só existem nas versões mais novas.
```
**Exemplo:** Entrada: Excel; somar o valor só das linhas "Despesa" do mês 9; valores em E5:E504,
tipo em B5:B504, mês em I5:I504. Saída: =SOMASES(E5:E504;B5:B504;"Despesa";I5:I504;9), com cada
parte explicada, e a alternativa mais simples (SOMASE por tipo em uma cópia filtrada pelo mês).
**Confira:** teste em uma cópia.

### Aprender 04 · Plano de estudo de 4 semanas
**Quando usar:** quando decidiu estudar algo por conta própria e não sabe por onde começar.

```
Monte um plano de 4 semanas, com 30 minutos por dia, para eu aprender [tema, ex.: fórmulas essenciais de planilha / apresentações objetivas / usar IA no trabalho] partindo de [nível]. Cada semana: objetivo, o que praticar por dia, um exercício com meus próprios dados e como saber que aprendi. Sem cursos pagos.
```
**Exemplo:** Entrada: "fórmulas essenciais de planilha", partindo de "sei somar e fazer média".
Saída: quatro semanas (referências e formatos; SE e SOMASES; PROCV e ÍNDICE; gráficos e tabela
dinâmica), com um exercício por dia usando as planilhas do kit e um teste de "sei que aprendi" no
fim de cada semana.
**Confira:** se o plano usa só recursos que existem na sua versão; ajuste o tempo se 30 minutos
por dia não cabem.

### Aprender 05 · Como explicar meu trabalho com números
**Quando usar:** antes de uma avaliação, de uma negociação de honorários ou de uma reunião de
resultados.

```
Trabalho como [função] e preciso mostrar meu valor para [chefe/cliente] com números. Sugira 6 indicadores que eu consiga medir sozinho com uma planilha simples, como calcular cada um, com que frequência olhar e o que seria um bom resultado. Explique em linguagem simples.
```
**Confira:** escolha 3 e coloque no Relatório Mensal Pronto.

---

## Modelo em branco para criar os seus

```
Papel: você é [quem a IA deve ser].
Contexto: [quem sou, para quem é, o que já tenho].
Tarefa: [o que fazer, em uma frase].
Formato: [tabela, lista, e-mail, até N palavras].
Regras: [o que não fazer; marque dúvidas com colchetes].
Dados:
[cole]
```
**Exemplo:** Entrada: analista de marketing na Prisma Comunicação; mostrar valor para a diretoria.
Saída: seis indicadores (leads, custo por lead, taxa de conversão, prazo de entrega, retrabalho,
NPS), como calcular cada um, frequência de olhar e uma faixa do que seria um bom resultado.

Suporte: suporte@seusociogestor.com.br · Reembolso em até 7 dias.

