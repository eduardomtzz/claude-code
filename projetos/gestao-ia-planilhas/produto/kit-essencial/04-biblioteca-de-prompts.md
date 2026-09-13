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
**Exemplo de entrada:** "gente, lembrando que a diretoria quer o relatório até sexta, e a Aurora
pediu desconto na proposta, alguém revisa? o post de terça precisa aprovar hoje, e preciso
conferir as faturas dos fornecedores essa semana."
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
**Confira:** se os blocos respeitam suas reuniões e se a IA não inventou tarefas.

### Organizar 03 · Prioridade quando tudo parece urgente
**Quando usar:** quando a lista tem mais de 10 tarefas abertas e você não sabe por onde começar.

```
Ajude-me a priorizar. Para cada tarefa abaixo, classifique em uma das quatro caixas: Fazer agora (alto impacto, urgente), Agendar (alto impacto, não urgente), Delegar ou simplificar (baixo impacto, urgente), Cortar (baixo impacto, não urgente). Explique em uma frase por que cada uma caiu na caixa. No fim, diga as três que eu deveria fazer hoje.
Contexto do meu trabalho: [uma frase sobre o que você faz e o que é mais importante este mês].
Tarefas:
[cole aqui]
```
**Confira:** a IA não conhece sua política; ajuste antes de cortar algo.

### Organizar 04 · Ata de reunião em 5 minutos
**Quando usar:** logo depois da reunião, com suas anotações soltas ou a transcrição.

```
Transforme estas anotações em uma ata curta com quatro partes: Decisões tomadas; Tarefas (quem, o quê, até quando); Pendências sem dono; Próxima reunião. Use frases curtas. Não invente decisões que não estão no texto; se algo ficou ambíguo, marque com "[confirmar]".
Reunião: [assunto], em [data], com [participantes por função, sem nomes se preferir].
Anotações:
[cole aqui]
```
**Confira:** cada "[confirmar]" e os prazos.

### Organizar 05 · Semana revisada na sexta
**Quando usar:** no fechamento de sexta, com o que foi feito e o que ficou.

```
Faça a minha revisão semanal. Com a lista abaixo (tarefas feitas, atrasadas e para a próxima semana), responda: 1) o que andou de mais importante; 2) o que travou e a causa provável; 3) três ajustes simples para a próxima semana; 4) uma mensagem de duas linhas que eu possa mandar para [chefe/cliente/equipe] resumindo a semana. Tom direto, sem elogio vazio.
Lista:
[cole aqui]
```
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
**Confira:** sinais de "menor é melhor" e percentuais.

### Analisar 03 · Onde cortar gastos
**Quando usar:** com a tabela "Para onde foi o dinheiro" da planilha Ganhos e Gastos.

```
Analise meus gastos por categoria e me ajude a decidir onde cortar sem prejudicar o essencial. Para cada categoria: é fixo ou variável? É essencial, importante ou supérfluo? Quanto seria realista reduzir em 30 dias e como? Depois, monte um plano com três cortes que somem pelo menos R$ [valor alvo] por mês, do mais fácil ao mais difícil. Seja específico e não moralize.
Contexto: [pessoa ou negócio, renda média mensal, objetivo do corte].
Gastos do mês:
[cole aqui]
```
**Confira:** a IA não sabe o que é essencial para você; ajuste a classificação.

### Analisar 04 · Meta realista
**Quando usar:** para definir a meta de um indicador com base no histórico.

```
Com o histórico abaixo, sugira uma meta mensal para os próximos três meses em três cenários: conservador, provável e ambicioso. Explique o cálculo de cada um (média, tendência, sazonalidade). Diga o que precisaria acontecer para atingir o cenário ambicioso.
Indicador: [nome, unidade, maior é melhor ou menor é melhor].
Histórico mês a mês:
[cole]
```
**Confira:** se a IA respeitou a sazonalidade que você conhece.

### Analisar 05 · Achar o erro na planilha
**Quando usar:** quando um total não bate ou um número parece estranho.

```
Vou colar um trecho de planilha em que algo não bate. Ajude-me a encontrar o erro: verifique somas, percentuais, sinais, unidades e valores repetidos ou faltando. Liste cada suspeita com a célula ou linha, o que esperava e o que encontrou. Se precisar de mais contexto, diga exatamente qual.
O que eu esperava: [ex.: o total deveria ser 12.400].
Trecho:
[cole]
```
**Confira:** tudo. Este prompt encontra suspeitas, não prova erros.

### Analisar 06 · Perguntas antes de decidir
**Quando usar:** antes de uma decisão com base em números (contratar, comprar, cortar).

```
Vou tomar a decisão: [descreva]. Com os dados abaixo, liste: 1) o que os dados sustentam; 2) o que eles NÃO respondem; 3) cinco perguntas que eu deveria responder antes de decidir; 4) o pior cenário realista e como me proteger dele. Não me diga o que decidir; me ajude a pensar.
Dados:
[cole]
```
**Confira:** as perguntas costumam ser o mais útil; os cenários são hipóteses.

### Analisar 07 · Gráfico certo para o dado
**Quando usar:** antes de montar um gráfico para relatório ou slide.

```
Quero mostrar [o que você quer que a pessoa entenda] para [público]. Os dados são: [descreva as colunas e o período]. Indique o tipo de gráfico mais adequado, o que vai em cada eixo, se precisa de linha de meta, e o título em uma frase que já diga a conclusão (ex.: "Receita cresceu 12% em setembro, puxada por serviços"). Diga também o que evitar (ex.: pizza com 12 fatias).
```
**Confira:** título deve ser verdadeiro para os seus dados.

### Analisar 08 · Resumo executivo de uma tabela grande
**Quando usar:** quando a tabela tem muitas linhas e você só precisa da essência.

```
Resuma a tabela abaixo em no máximo 120 palavras para alguém que tem um minuto: comece pela conclusão principal, dê os dois números que a sustentam, aponte o maior risco e termine com a ação recomendada. Sem adjetivos, sem introdução.
Contexto: [o que é, período, unidade].
Tabela:
[cole]
```
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
**Confira:** cada "[explicar]" e se nenhum número foi alterado.

### Escrever 02 · E-mail curto que pede algo
**Quando usar:** pedido de aprovação, informação, prazo.

```
Escreva um e-mail de até 120 palavras para [pessoa e cargo] pedindo [o quê] até [prazo]. Comece pelo pedido na primeira frase, explique o motivo em duas linhas, diga o que acontece se não vier no prazo (sem ameaça) e termine com uma pergunta fechada. Assunto de até 8 palavras. Tom: [cordial e direto / formal].
Contexto extra: [o que a pessoa já sabe].
```
**Confira:** prazo e o que exatamente você está pedindo.

### Escrever 03 · Responder um e-mail difícil
**Quando usar:** reclamação, cobrança, pedido de desconto, crítica.

```
Recebi o e-mail abaixo e preciso responder. Meu objetivo: [ex.: manter o cliente sem dar o desconto]. Minha posição: [o que posso e não posso ceder]. Escreva a resposta em até 150 palavras: reconheça o ponto da pessoa em uma frase, exponha a posição com clareza, ofereça uma alternativa concreta e feche com próximo passo. Sem pedir desculpas em excesso e sem tom defensivo.
E-mail recebido (sem dados pessoais):
[cole]
```
**Confira:** se a resposta não promete o que você não pode cumprir.

### Escrever 04 · Justificativa para chefe ou cliente
**Quando usar:** explicar um atraso, um custo a mais, uma mudança de escopo.

```
Escreva uma justificativa de até 180 palavras para [quem] sobre [o fato]. Estrutura: o que aconteceu (fato, sem culpa); impacto real (prazo, custo, qualidade); o que já foi feito; o que proponho; o que preciso da pessoa. Tom responsável e objetivo, sem desculpas em cascata.
Fatos:
[cole]
```
**Confira:** que os fatos estejam corretos e que a proposta seja viável.

### Escrever 05 · Explicar o mês financeiro para alguém
**Quando usar:** com o Painel de Ganhos e Gastos, para explicar a um sócio, cliente ou à família.

```
Explique o resultado financeiro do mês para [quem, e o quanto entende de números], em até 200 palavras e linguagem simples: quanto entrou, quanto saiu, quanto sobrou, para onde foi a maior parte, o que mudou em relação ao mês anterior e uma decisão sugerida para o próximo mês. Sem termos técnicos.
Números:
[cole o painel]
Contexto: [o que aconteceu de diferente no mês].
```
**Confira:** números e a decisão sugerida.

### Escrever 06 · Proposta comercial simples
**Quando usar:** orçamento ou proposta de serviço de uma página.

```
Escreva uma proposta de serviço de uma página para [cliente e ramo] com as seções: Entendimento do pedido (2 frases); O que será entregue (lista objetiva); O que não está incluído; Prazo; Investimento (R$ [valor], condições de pagamento [ex.: 50% na aprovação, 50% na entrega]); Validade da proposta ([dias]); Próximo passo. Tom profissional e claro. Não invente entregas além das listadas.
O pedido do cliente: [descreva].
O que vou entregar: [liste].
```
**Confira:** escopo, valor e condições; nada de promessa extra.

### Escrever 07 · Resumo de reunião para quem não foi
**Quando usar:** logo após a reunião, para atualizar quem faltou.

```
Escreva um resumo de até 150 palavras para [quem] que não participou da reunião sobre [assunto]. Comece com a decisão principal, depois o que muda para a pessoa, e o que ela precisa fazer (se algo). Anexe a lista de tarefas com prazo. Baseie-se só na ata abaixo.
Ata:
[cole]
```
**Confira:** o que "muda para a pessoa" é interpretação; revise.

### Escrever 08 · Texto simplificado
**Quando usar:** quando seu texto ficou longo, técnico ou confuso.

```
Reescreva o texto abaixo para ser lido em metade do tempo, mantendo todo o conteúdo factual: frases curtas, voz ativa, sem jargão, sem repetição. Marque entre colchetes qualquer trecho em que você teve dúvida do sentido. Mantenha o tom [formal/informal].
Texto:
[cole]
```
**Confira:** cada colchete e se nada importante sumiu.

### Escrever 09 · Descrição de tarefa para delegar
**Quando usar:** quando vai passar uma tarefa para outra pessoa (equipe, estagiário, freelancer).

```
Escreva a descrição de uma tarefa para eu delegar a [quem, nível de experiência]. Estrutura: objetivo em uma frase; o que exatamente entregar (formato, tamanho, exemplo); como saberemos que está bom (3 critérios); o que evitar; prazo e onde entregar; a quem perguntar em caso de dúvida. Máximo 200 palavras.
Tarefa: [descreva do seu jeito].
```
**Confira:** critérios de qualidade são o que evita retrabalho; ajuste-os.

### Escrever 10 · Mensagem de cobrança educada
**Quando usar:** com a lista "a pagar" ou um recebível atrasado.

```
Escreva três versões de mensagem de cobrança para [cliente], sobre [o que, valor R$ [ ], vencido em [data]]: 1) lembrete amigável (primeiro contato); 2) segunda cobrança, firme e cordial; 3) última antes de suspender o serviço, clara e sem ameaça. Cada uma com até 80 palavras, com Pix/forma de pagamento e um caminho fácil para resolver. Tom respeitoso: presuma que foi esquecimento.
```
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
**Confira:** cada "[explicar]"; o slide 8 precisa ser um pedido real.

### Apresentar 02 · Fala de abertura de 60 segundos
**Quando usar:** para começar a reunião ou a apresentação sem enrolar.

```
Escreva o que eu digo nos primeiros 60 segundos da apresentação sobre [assunto] para [público]: o que vamos ver, por que importa para eles, qual a decisão que preciso no fim, e quanto tempo vai durar. Máximo 120 palavras, linguagem falada, sem "bom dia a todos" genérico.
```
**Confira:** a decisão que você pede no fim deve ser a mesma do slide 8.

### Apresentar 03 · Perguntas prováveis e respostas
**Quando usar:** na véspera, para não ser pego de surpresa.

```
Com base no roteiro abaixo, liste as 8 perguntas mais prováveis de [público] e uma resposta curta e honesta para cada, incluindo o que dizer quando eu não souber. Marque as 3 mais difíceis.
Roteiro:
[cole]
```
**Confira:** respostas honestas; não use as que prometem o que você não sabe.

### Apresentar 04 · Um slide que explica tudo
**Quando usar:** quando só há tempo para um slide.

```
Condense o assunto abaixo em UM slide: título-conclusão (até 12 palavras), três tópicos com número, um gráfico sugerido (tipo e o que mostra) e uma frase de pedido. Máximo 60 palavras no slide.
Assunto e dados:
[cole]
```
**Confira:** os três números.

### Apresentar 05 · Transformar relatório em apresentação
**Quando usar:** quando o relatório já existe e você precisa apresentar.

```
Transforme o relatório abaixo em uma apresentação de [n] slides. Um tema por slide, título-conclusão, no máximo 25 palavras por slide, e uma nota do apresentador com o que falar (até 40 palavras). Corte tudo que não muda uma decisão.
Relatório:
[cole]
```
**Confira:** o que foi cortado; às vezes a IA corta o que importa.

### Apresentar 06 · Feedback do meu roteiro
**Quando usar:** com o roteiro pronto, antes de montar os slides.

```
Aja como um diretor exigente que vai assistir a esta apresentação. Aponte: onde perco a atenção; o que está em ordem errada; frases vagas e como torná-las concretas; slides que podem ser cortados; a pergunta desconfortável que você faria. Seja específico e direto.
Roteiro:
[cole]
```
**Confira:** aplique só o que faz sentido para o seu público.

---

## Grupo 5 · Revisar (6)

### Revisar 01 · Revisão de texto antes de enviar
```
Revise o texto abaixo em três passes: 1) erros de português e digitação (liste com correção); 2) clareza (frases que podem ser mal entendidas, com sugestão); 3) tom (algo que pode soar rude, defensivo ou exagerado). Não reescreva tudo; aponte e sugira. Português do Brasil.
Texto:
[cole]
```
**Confira:** aceite as correções uma a uma.

### Revisar 02 · Conferir uma conta de porcentagem ou variação
```
Confira os cálculos abaixo. Para cada linha, refaça a conta passo a passo e diga se está certa; se não, dê o valor correto. Explique a diferença entre variação percentual e pontos percentuais quando aparecer.
Cálculos:
[cole]
```
**Confira:** este é o prompt em que a IA mais erra: refaça você o que for decisivo.

### Revisar 03 · Checar consistência entre planilha e texto
```
Compare os números do texto com os da tabela e liste toda divergência (número no texto, número na tabela, onde). Aponte também números citados no texto que não existem na tabela.
Texto:
[cole]
Tabela:
[cole]
```
**Confira:** as divergências apontadas; a IA pode deixar passar alguma.

### Revisar 04 · Simplificar uma fórmula ou explicar o que ela faz
```
Explique em português simples o que esta fórmula de planilha faz, passo a passo, e diga se há uma forma mais simples ou mais segura de escrevê-la (compatível com Excel e Google Sheets). Aponte casos em que ela pode dar erro (célula vazia, divisão por zero, texto no lugar de número).
Fórmula:
[cole]
```
**Confira:** teste a fórmula sugerida em uma cópia antes de trocar.

### Revisar 05 · Checklist antes de entregar
```
Monte um checklist de verificação para [o que vou entregar: relatório, planilha, apresentação, proposta] para [público], com no máximo 12 itens, do mais crítico ao menos crítico. Inclua itens de número, de texto, de formato e de envio (destinatário, anexo, assunto).
```
**Confira:** use o checklist do bônus do kit como base e complete com o da IA.

### Revisar 06 · Segunda opinião sobre uma decisão
```
Vou tomar a decisão: [descreva]. Meus motivos: [liste]. Faça o papel do advogado do diabo: os três melhores argumentos contra, o que eu posso estar ignorando, e uma versão menor ou reversível da mesma decisão. Depois, diga honestamente se os argumentos contra são fortes ou fracos.
```
**Confira:** a decisão continua sua.

---

## Grupo 6 · Aprender (5)

### Aprender 01 · Explicar um termo de planilha ou de gestão
```
Explique "[termo]" para alguém que nunca estudou gestão, em até 100 palavras, com um exemplo do dia a dia de [seu tipo de trabalho]. Depois dê a definição técnica em uma frase.
```

### Aprender 02 · Montar uma tabela dinâmica (passo a passo)
```
Tenho uma tabela com as colunas [liste] no [Excel/Google Sheets]. Quero ver [ex.: total de vendas por mês e por vendedor]. Me dê o passo a passo, clique por clique, para montar uma tabela dinâmica que mostre isso, e diga como atualizar quando eu incluir dados novos.
```
**Confira:** os nomes de menu mudam entre versões; se não achar, diga a versão para a IA.

### Aprender 03 · Escolher a função certa
```
No [Excel/Google Sheets], preciso [descreva o que quer calcular, com exemplo de entrada e saída]. Diga qual função usar, escreva a fórmula pronta para as células [ex.: valores em B2:B50, categorias em A2:A50], explique cada parte e dê uma alternativa mais simples se existir. Evite funções que só existem nas versões mais novas.
```
**Confira:** teste em uma cópia.

### Aprender 04 · Plano de estudo de 4 semanas
```
Monte um plano de 4 semanas, com 30 minutos por dia, para eu aprender [tema, ex.: fórmulas essenciais de planilha / apresentações objetivas / usar IA no trabalho] partindo de [nível]. Cada semana: objetivo, o que praticar por dia, um exercício com meus próprios dados e como saber que aprendi. Sem cursos pagos.
```

### Aprender 05 · Como explicar meu trabalho com números
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

Suporte: suporte@seusociogestor.com.br · Reembolso em até 7 dias.
