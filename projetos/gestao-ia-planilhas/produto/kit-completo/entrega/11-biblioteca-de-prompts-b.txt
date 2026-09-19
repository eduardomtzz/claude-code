# Biblioteca de prompts B · Estruturar e Produzir · Kit IA no Trabalho · Completo

Versão 1.0 · setembro de 2026 · Seu Sócio Gestor

40 prompts em 2 grupos, que completam os 40 da Biblioteca A (organizar, analisar, escrever,
apresentar, revisar, aprender). Estes só fazem sentido com método: **Estruturar** é o passo antes
de abrir o Excel; **Produzir** é fazer a planilha, o relatório e a apresentação com a IA de
parceira, não de muleta. Cada prompt tem: quando usar, o prompt pronto (troque o que está entre
colchetes), um exemplo e o que conferir.

## Antes de começar: as mesmas três regras

1. **Nunca cole dado pessoal ou sigiloso em uma IA pública.** Troque nomes por "Cliente A".
2. **A IA erra com confiança.** Fórmula, número e conclusão passam por você antes de virar entrega.
3. **Contexto é o segredo.** Diga quem lê, para quê e o que você já tem.

Regra extra deste grupo: **peça a fórmula em português do Excel e em inglês do Google Sheets**
quando não souber qual programa vai usar. As duas ferramentas aceitam ponto e vírgula como
separador no Brasil.

---

## Grupo 7 · Estruturar (12)

### Estruturar 01 · O que a planilha precisa responder
**Quando usar:** antes de abrir o Excel, sempre. Cinco minutos aqui poupam uma tarde depois.

```
Você é um analista experiente que desenha planilhas simples. Vou descrever uma necessidade e você me devolve, em uma tabela: Pergunta que a planilha responde | Quem lê e com que frequência | Dado de entrada necessário | De onde vem o dado | Saída (número, lista, gráfico).
Depois, diga em até 5 linhas se isso cabe em uma planilha só ou se são duas, e o que NÃO deve entrar.
Necessidade: [descreva em 3 a 5 frases o que você quer controlar, para quem e por quê].
```
**Exemplo:** "Quero controlar as propostas que envio aos clientes, saber quanto tenho em aberto e
quanto devo fechar no mês. Sou eu quem lê, toda sexta. Meu sócio olha no fim do mês."
**Confira:** se a IA inventou perguntas que você não fez. Corte. Planilha boa responde poucas
perguntas.

### Estruturar 02 · Entrada, saída e quem lê, em uma frase
**Quando usar:** para nomear a planilha e escrever a primeira linha da aba "Como usar".

```
Resuma em uma frase de até 25 palavras, no formato "Você [preenche X]; a planilha [mostra Y] para [quem] [quando]", a planilha descrita abaixo. Depois sugira 3 nomes curtos (até 3 palavras) para o arquivo.
Descrição: [cole a tabela do prompt Estruturar 01 ou descreva].
```
**Confira:** se a frase menciona a saída (o que a planilha mostra), não só a entrada.

### Estruturar 03 · Desenhar as colunas da base
**Quando usar:** para montar a aba de lançamento (a "base") de qualquer planilha nova. Gera o
cabeçalho para colar na Base Limpa.

```
Você é um especialista em bases de dados em planilha. Desenhe a aba de lançamento para o controle descrito abaixo, seguindo as regras: uma linha por registro; uma coluna por informação; nada de totais no meio; datas como data; categorias vindas de lista; o que for calculado em coluna própria.
Devolva uma tabela: Coluna | Tipo (data, texto, número, lista, fórmula) | Exemplo | Obrigatória? | Observação. Máximo de 14 colunas. Marque com * as colunas de lista e diga de que lista vêm.
Controle: [descreva]. Registro = [o que é uma linha: uma venda, uma tarefa, uma hora trabalhada].
```
**Exemplo:** "Controle de horas da equipe. Registro = uma pessoa, um dia, um projeto."
**Confira:** colunas demais (corte o que você não vai preencher toda vez) e colunas de cálculo
misturadas com colunas de entrada.

### Estruturar 04 · Listas e validações
**Quando usar:** depois de desenhar as colunas, para evitar "marketing", "Marketing" e "MKT".

```
Para as colunas de lista abaixo, sugira os valores da lista (até 10 por coluna), em português, curtos e sem ambiguidade. Depois, para cada coluna numérica ou de data, sugira a validação (mínimo, máximo, formato) e a mensagem de erro em uma frase amigável.
Colunas: [cole a tabela do Estruturar 03].
Contexto do negócio: [uma frase].
```
**Confira:** listas com itens que se sobrepõem ("Serviço" e "Consultoria"). Uma coisa só pode
cair em um item.

### Estruturar 05 · Planejar o painel antes de montar
**Quando usar:** para decidir o que vai na primeira aba, a que o chefe ou cliente olha.

```
Você é um designer de painéis para gestores ocupados. Com base na base de dados abaixo, proponha um painel de uma tela com: 3 a 4 números grandes (nome, fórmula em palavras, por que importa); 1 gráfico (tipo, eixo X, eixo Y, pergunta que responde); 1 tabela pequena (colunas, ordenada por quê); 1 alerta (condição que acende vermelho). Diga o que você deixou de fora e por quê.
Quem lê: [cargo], [frequência]. Decisão que a pessoa toma com isso: [uma frase].
Colunas da base: [cole o cabeçalho].
```
**Confira:** se cada número grande tem uma decisão ligada a ele. Número bonito sem decisão sai.

### Estruturar 06 · O gráfico certo para a pergunta
**Quando usar:** antes de inserir um gráfico. A aula 4 explica o porquê de cada tipo.
*Amplia o Analisar 07 (Gráfico certo para o dado) da Biblioteca A: lá, um gráfico; aqui, vários de uma vez, com eixos e título.*

```
Para cada pergunta abaixo, diga o tipo de gráfico ideal (barra, coluna, linha, área, pizza só se couber, tabela) e o motivo em uma frase, mais o que colocar no eixo X, no eixo Y e no título (título deve ser a conclusão, não o tema).
Perguntas:
1. [ex.: como a receita evoluiu nos últimos 12 meses?]
2. [ex.: qual categoria pesa mais nas despesas?]
3. [ex.: previsto contra realizado por mês]
```
**Confira:** se a IA sugeriu pizza para mais de 5 fatias ou para comparar ao longo do tempo. Não use.

### Estruturar 07 · Planilha demais? Dividir em duas
**Quando usar:** quando a planilha começa a ter 8 abas e ninguém acha nada.

```
Tenho uma planilha com as abas e colunas abaixo. Diga se ela deveria ser dividida, e como: quais abas ficam juntas, qual é o arquivo principal, o que vira arquivo separado, e como um alimenta o outro (copiar e colar mensal, ou referência). Critério: cada arquivo responde uma pergunta e tem um dono.
Abas e colunas: [liste]. Quem usa cada aba: [liste].
```
**Confira:** se a divisão cria retrabalho de digitar o mesmo dado duas vezes. Se cria, não divida.

### Estruturar 08 · Traduzir um processo em planilha
**Quando usar:** quando alguém descreve "como a gente faz" e você precisa transformar em controle.

```
Vou descrever um processo em texto corrido. Transforme em: 1) etapas numeradas com quem faz e o que entra e sai de cada uma; 2) o que precisa ser registrado em cada etapa (isso vira coluna); 3) os 3 indicadores que mostram se o processo está saudável; 4) o desenho de uma planilha de acompanhamento (abas e colunas).
Processo: [cole o texto].
```
**Confira:** se as etapas batem com a realidade. Pergunte a quem executa antes de montar.

### Estruturar 09 · Migrar do caderno (ou do WhatsApp) para a planilha
**Quando usar:** quando os dados estão em anotações soltas, prints ou mensagens.

```
Vou colar anotações soltas. Extraia os registros para uma tabela com as colunas [liste as colunas da sua base], uma linha por registro. Onde faltar informação, escreva "?" na célula. Ao fim, liste as linhas que ficaram com "?" e o que perguntar para completar.
Anotações (dados fictícios ou sem nomes reais):
[cole]
```
**Confira:** valores e datas (a IA erra ordem dia/mês). Preencha os "?" antes de colar na planilha.

### Estruturar 10 · Regras de preenchimento da equipe
**Quando usar:** quando mais de uma pessoa lança na mesma planilha.

```
Escreva as regras de preenchimento desta planilha para uma equipe, em até 10 itens curtos, tom direto, sem jargão: o que é obrigatório, o que vem de lista, como escrever descrições (verbo + objeto, até 8 palavras), quando lançar, o que fazer quando não sabe a categoria, e o que nunca fazer (mesclar, apagar linha, digitar em coluna de fórmula).
Colunas: [cole o cabeçalho]. Frequência de lançamento: [diária/semanal].
```
**Confira:** se dá para colar as regras na aba "Como usar" sem adaptar. Deve dar.

### Estruturar 11 · De relatório a modelo reutilizável
**Quando usar:** quando você fez um relatório bom uma vez e quer repetir todo mês sem refazer.

```
Vou colar um relatório que fiz. Transforme em um modelo reutilizável: 1) a estrutura fixa (seções e ordem); 2) o que muda a cada mês, marcado entre colchetes; 3) quais números vêm de qual planilha ou aba; 4) uma lista de conferência de 5 itens antes de enviar.
Relatório: [cole, sem dados sigilosos].
```
**Confira:** se a estrutura tem no máximo 6 seções. Relatório mensal longo ninguém lê.

### Estruturar 12 · Revisar a estrutura de uma planilha existente
**Quando usar:** quando herdou uma planilha e não sabe se confia nela.

```
Você é um auditor de planilhas. Vou descrever (ou colar) a estrutura de uma planilha. Aponte, em ordem de gravidade: 1) riscos de erro (fórmulas copiadas até a metade, totais no meio dos dados, células mescladas, categorias digitadas à mão, números como texto); 2) o que dificulta análise (várias tabelas na mesma aba, cabeçalho em linhas diferentes); 3) o que fazer primeiro, em 3 passos. Seja específico: cite a aba e a coluna.
Estrutura: [descreva abas, colunas e onde estão as fórmulas, ou cole 20 linhas sem dados reais].
```
**Confira:** teste um dos riscos apontados antes de mexer em tudo.

---

## Grupo 8 · Produzir (28)

### Produzir 01 · A fórmula certa a partir de uma frase
**Quando usar:** sempre que souber o que quer calcular e não souber a fórmula.

```
Escreva a fórmula de planilha para o cálculo abaixo. Dê duas versões: Excel em português (separador ;) e Google Sheets em inglês (separador ;). Use referências absolutas ($) onde a fórmula será copiada para baixo. Explique em 2 linhas o que cada parte faz e diga qual erro pode aparecer e por quê.
Cálculo: [em palavras: ex. "somar a coluna Valor quando a coluna Tipo for Despesa e o Mês for igual à célula B7"].
Colunas: [ex. A=Data, B=Tipo, C=Categoria, E=Valor, I=Mês]. Linha dos dados: [ex. 5 a 500].
```
**Exemplo de resposta esperada:** `=SOMASES(E5:E500;B5:B500;"Despesa";I5:I500;$B$7)` e
`=SUMIFS(E5:E500;B5:B500;"Despesa";I5:I500;$B$7)`.
**Confira:** teste em 2 células com resultado que você sabe de cabeça antes de copiar para tudo.

### Produzir 02 · Explicar uma fórmula que já existe
**Quando usar:** planilha herdada, fórmula de 3 linhas, ninguém sabe o que faz.

```
Explique esta fórmula para quem não é de Excel: 1) o que ela devolve, em uma frase; 2) o passo a passo de dentro para fora; 3) em que situação ela dá erro; 4) uma versão mais simples, se existir, com o mesmo resultado.
Fórmula: [cole]. Contexto das colunas: [ex. A=Data, B=Cliente...].
```
**Confira:** a "versão mais simples" em uma célula de teste antes de trocar.

### Produzir 03 · Corrigir um erro (#VALOR!, #REF!, #N/D, #DIV/0!)
**Quando usar:** quando a célula mostra erro e você não sabe por quê.

```
Esta fórmula está devolvendo [erro]. Liste as 3 causas mais prováveis, em ordem, com um teste de 10 segundos para confirmar cada uma. Depois dê a fórmula corrigida, com SEERRO só se fizer sentido (não esconda erro de dado).
Fórmula: [cole]. O que tem nas células referenciadas: [descreva: número, texto, vazio, data como texto].
```
**Confira:** se a correção usa SEERRO para mascarar um dado errado. Corrija o dado, não o sintoma.

### Produzir 04 · SOMASES e CONT.SES com várias condições
**Quando usar:** para totais por mês, categoria, pessoa, status, tudo junto.

```
Monte as fórmulas para uma tabela-resumo com [linhas: ex. categorias] nas linhas e [colunas: ex. meses] nas colunas, somando [coluna de valor] com as condições [liste]. Use referências que permitam copiar a fórmula para toda a tabela (misturando $ na linha e na coluna). Dê a fórmula da célula do canto superior esquerdo e explique como ela se ajusta ao copiar.
Base: aba [nome], colunas [liste com letras], linhas [de-até].
```
**Confira:** copie para o canto oposto da tabela e veja se as referências continuam certas.

### Produzir 05 · PROCV, ÍNDICE+CORRESP ou PROCX?
**Quando usar:** para buscar um dado de outra tabela (preço do produto, custo-hora da pessoa).

```
Preciso buscar [o que] na tabela [onde] a partir de [chave]. Diga qual função usar (PROCV, ÍNDICE+CORRESP ou PROCX) considerando: a chave está à esquerda ou à direita do resultado? o arquivo vai abrir em Excel antigo ou Google Sheets? Dê a fórmula nas duas linguagens, com SEERRO devolvendo "não encontrado".
Tabela de busca: [aba e colunas]. Onde vai a fórmula: [aba e coluna].
```
**Confira:** teste com uma chave que você sabe que não existe e veja se aparece "não encontrado".

### Produzir 06 · Tabela dinâmica passo a passo
**Quando usar:** para resumir uma base de 500 linhas em 3 cliques (aula 2 mostra na tela).
*Amplia o Aprender 02 (Montar uma tabela dinâmica) da Biblioteca A: acrescenta filtros, contagem, formato em R$ e a conferência do total.*

```
Me guie, passo a passo e com os nomes exatos dos menus, para criar uma tabela dinâmica no [Excel/Google Sheets] que mostre [ex.: valor total por categoria nas linhas e por mês nas colunas, só status Pago]. Diga o que arrastar para Linhas, Colunas, Valores e Filtros, como mudar de soma para contagem, como formatar em R$ e como atualizar quando entrar dado novo.
Base: aba [nome], colunas [liste].
```
**Confira:** se o total da dinâmica bate com um SOMASES simples na base.

### Produzir 07 · Limpar dados antes de analisar
**Quando usar:** base exportada de um sistema, cheia de espaço, texto em maiúsculas, número como texto.

```
Tenho uma base com os problemas abaixo. Para cada um, dê a fórmula ou o recurso do [Excel/Google Sheets] que resolve, em ordem de execução, e como aplicar a toda a coluna sem quebrar a base: [ex.: espaços no início e fim; nomes em maiúsculas e minúsculas misturadas; datas como texto "13/09/2026"; valores com "R$" e ponto de milhar como texto; linhas duplicadas; linhas vazias no meio].
```
**Confira:** faça em uma cópia da base. Compare a contagem de linhas antes e depois.

### Produzir 08 · Coluna calculada com regras (SE, SES, PROCURAR)
**Quando usar:** para criar "Situação", "Faixa", "Semáforo" a partir de regras.

```
Escreva a fórmula de uma coluna que devolve [ex.: "Atrasada", "Hoje", "Esta semana" ou "No prazo"] a partir de [ex.: a data em D e a data de hoje], com as regras: [liste em ordem de prioridade]. Use SE aninhado (compatível com tudo) e, opcionalmente, SES. Trate célula vazia devolvendo "".
Colunas: [liste]. Linha inicial: [n].
```
**Confira:** teste um caso de cada regra e o caso vazio.

### Produzir 09 · Formatação condicional que avisa
**Quando usar:** para a linha ficar vermelha quando atrasa, verde quando fecha.

```
Quero que a linha inteira de [aba] fique [cor] quando [condição, ex.: a coluna G for "Atrasada"], e [outra cor] quando [outra condição]. Me dê a fórmula da regra de formatação condicional (com o $ certo para valer na linha inteira), o intervalo a aplicar e o caminho nos menus do [Excel/Google Sheets]. Diga a ordem das regras se uma sobrepõe a outra.
```
**Confira:** a referência da regra deve apontar para a primeira linha do intervalo, com $ na coluna.

### Produzir 10 · Datas: dias úteis, vencimento, idade, mês
**Quando usar:** qualquer conta com data.

```
Dê as fórmulas (Excel PT e Sheets EN) para: [escolha: dias entre duas datas; dias úteis entre duas datas descontando feriados de uma lista; data de vencimento = data + 30 dias; primeiro e último dia do mês de uma data; nome do mês por extenso; semana do ano; idade em anos completos]. Explique o que acontece se a célula de data estiver vazia e como tratar.
Célula da data: [ex. A5]. Lista de feriados: [ex. Config!H5:H20].
```
**Confira:** teste com 31/12 e 29/02 de ano bissexto.

### Produzir 11 · Texto: juntar, separar, extrair
**Quando usar:** nome e sobrenome juntos, código dentro de uma descrição, e-mail em maiúsculas.

```
Dê as fórmulas (Excel PT e Sheets EN) para: [escolha: juntar nome e sobrenome com espaço; separar "Nome Sobrenome" em duas colunas; extrair os 4 primeiros caracteres; extrair o texto antes do hífen; deixar só a primeira letra maiúscula; remover espaços extras; contar quantas vezes uma palavra aparece]. Explique a lógica em uma linha cada.
Célula de origem: [ex. B5]. Exemplo do conteúdo: [ex. "AURORA MÓVEIS - proposta 042"].
```
**Confira:** teste com uma célula sem o separador esperado (o hífen ausente) e trate o erro.

### Produzir 12 · Consolidar várias abas ou meses em uma
**Quando usar:** 12 abas iguais (uma por mês) e você precisa do ano inteiro.

```
Tenho [n] abas com a mesma estrutura ([colunas]). Quero uma aba consolidada com todas as linhas e uma coluna extra dizendo de que aba veio. Dê: 1) a forma mais simples no Google Sheets (com a função de empilhar intervalos); 2) a forma no Excel (Power Query passo a passo ou copiar e colar com procedimento); 3) o que fazer daqui para frente para não precisar consolidar (uma base só, coluna Mês).
```
**Confira:** conte as linhas: a consolidada deve ter a soma das abas.

### Produzir 13 · Validar a planilha inteira em 10 testes
**Quando usar:** antes de entregar uma planilha que outra pessoa vai usar.

```
Crie um roteiro de 10 testes para validar a planilha descrita abaixo antes de entregar: casos de borda (célula vazia, zero, negativo, data futura, texto onde vai número), totais que devem bater, o que acontece ao apagar uma linha de exemplo, ao inserir linha no meio e ao ordenar. Para cada teste: o que fazer, o resultado esperado, o que corrigir se falhar.
Planilha: [abas, colunas, principais fórmulas].
```
**Confira:** execute os 10. Anote a versão e a data na aba "Como usar".

### Produzir 14 · Do bloco de números ao relatório executivo (versão longa)
**Quando usar:** relatório mensal ou trimestral com mais de uma página. Versão ampliada do
Escrever 01 da Biblioteca A.

```
Escreva o relatório [mensal/trimestral] para [quem lê], em até [600] palavras, com a estrutura: 1) Resultado do período em duas frases (o número principal e a comparação com [período anterior/meta]); 2) O que explica o resultado (3 fatores, cada um com número); 3) Pontos de atenção (até 3, com causa provável e ação proposta, responsável e prazo); 4) O que vem no próximo período (3 itens); 5) Uma decisão que precisamos tomar, se houver. Tom profissional, frases curtas, sem adjetivos. Use apenas os números abaixo; onde faltar explicação, escreva "[explicar]".
Meus comentários: [o que aconteceu, por quê].
Números:
[cole o bloco da aba Resumo, Painel ou "O ano, mês a mês"]
```
**Confira:** cada "[explicar]", cada número contra a planilha, e se a seção 5 pede uma decisão de
verdade (se não pede, apague).

### Produzir 15 · Transformar tabela em narrativa
**Quando usar:** quando você tem a tabela e precisa do parágrafo que a explica.

```
Vou colar uma tabela. Escreva o parágrafo (até 120 palavras) que a explica para [quem lê], começando pelo mais importante, com no máximo 4 números citados, e terminando com o que isso implica. Não repita a tabela em texto. Depois, escreva a legenda de uma linha para a tabela.
Tabela:
[cole]
```
**Confira:** os 4 números citados, um a um.

### Produzir 16 · Comparar dois períodos ou dois cenários
**Quando usar:** este mês contra o anterior; previsto contra realizado; plano A contra plano B.

```
Compare os dois conjuntos abaixo. Devolva: 1) uma tabela com item | A | B | diferença | diferença % | comentário de até 8 palavras; 2) os 3 maiores desvios e a causa provável de cada um, marcando "[confirmar]" quando for hipótese; 3) uma frase de conclusão para abrir um e-mail.
A = [nome, ex. Agosto]: [cole]
B = [nome, ex. Setembro]: [cole]
```
**Confira:** sinais das diferenças (a IA troca A e B) e as porcentagens com base pequena.

### Produzir 17 · Explicar um resultado ruim sem esconder e sem drama
**Quando usar:** o mês veio abaixo da meta e você precisa comunicar.

```
Escreva o texto (até 200 palavras) para comunicar a [quem lê] um resultado abaixo do esperado, com: o número e a distância da meta na primeira frase; as 2 causas principais com evidência; o que já foi feito; o que será feito, com prazo; o que você precisa de quem lê. Sem justificativa emocional, sem culpar terceiros, sem minimizar.
Números: [cole]. Causas que eu vejo: [liste]. O que já fiz: [liste].
```
**Confira:** se a primeira frase diz o número. Se enrola, reescreva você.

### Produzir 18 · Roteiro de apresentação de 15 minutos
**Quando usar:** reunião mensal de resultados, apresentação para cliente.

```
Monte o roteiro de uma apresentação de 15 minutos sobre [tema] para [público], com 10 a 12 slides: para cada slide, título (que é a conclusão), o número ou gráfico que entra, a fala em 2 a 3 frases, e o tempo. Abra com o resultado e feche com a decisão pedida. Inclua um slide de "o que pode dar errado" antes do fechamento.
Números e fatos:
[cole o bloco do Resumo ou do Painel]
```
**Confira:** some os tempos. Corte até caber em 12 minutos: sempre atrasa.

### Produzir 19 · Roteiro de 5 minutos (versão curta)
**Quando usar:** ponto em pauta de reunião maior, atualização rápida.

```
Reduza o assunto abaixo a 5 minutos e 4 slides: 1) resultado em um número; 2) por quê (2 fatores); 3) próximo passo; 4) o que preciso de vocês. Para cada slide, título-conclusão, o dado e a fala em 2 frases.
Assunto e números: [cole]
```
**Confira:** se o slide 4 pede algo concreto (aprovação, verba, prazo, decisão).

### Produzir 20 · Perguntas difíceis da diretoria e como responder
**Quando usar:** antes de apresentar. Prepara você para o que vão perguntar.
*Amplia o Apresentar 03 (Perguntas prováveis e respostas) da Biblioteca A: aqui a IA faz o papel do diretor cético e marca o que os seus números não respondem.*

```
Você é um diretor cético que vai assistir à apresentação abaixo. Liste as 8 perguntas mais prováveis, das mais difíceis para as mais fáceis, e para cada uma: a resposta curta (2 frases) com o número que sustenta, e o que fazer se eu não souber responder. Marque as perguntas que os números que tenho não conseguem responder.
Apresentação: [cole o roteiro]. Números que tenho: [cole].
```
**Confira:** prepare os números das perguntas marcadas antes da reunião, ou assuma que não tem.

### Produzir 21 · Um slide que explica tudo (resumo executivo)
**Quando usar:** quando só vão ler um slide. Versão ampliada do Apresentar 04.

```
Crie o conteúdo de um único slide de resumo executivo sobre [tema]: título-conclusão (até 12 palavras); 3 números grandes com rótulo de 3 palavras; 3 frases de contexto (até 15 palavras cada); 1 pedido ou próximo passo. Diga também qual gráfico simples entraria e por quê.
Números: [cole]
```
**Confira:** se os 3 números contam a história sozinhos. Se precisam de explicação, troque.

### Produzir 22 · E-mail de resultado por público
**Quando usar:** o mesmo resultado precisa ir para o chefe, para o cliente e para a equipe.

```
Escreva 3 versões de um e-mail sobre o resultado abaixo, cada uma com até 120 palavras: 1) para o chefe (decisão e risco); 2) para o cliente (entrega e próximo passo, sem número interno); 3) para a equipe (reconhecimento e o que muda). Assunto de até 8 palavras em cada.
Resultado e números: [cole]. O que é interno e não pode ir ao cliente: [liste].
```
**Confira:** a versão do cliente, palavra por palavra, contra a lista do que é interno.

### Produzir 23 · Proposta comercial a partir de um briefing
**Quando usar:** proposta de serviço, com escopo, prazo e preço. Alimenta a planilha Funil de Propostas.

```
Com o briefing abaixo, escreva uma proposta comercial de 1 página com: entendimento do problema (3 frases); o que será entregue (lista com até 6 itens, cada um verificável); o que não está incluído (3 itens); prazo por etapa; investimento (valor total, forma de pagamento) e validade; próximo passo. Tom direto, sem superlativos.
Briefing: [cole]. Preço e prazo que decidi: [informe]. O que não faço: [liste].
```
**Confira:** escopo e "não incluído". É ali que mora o retrabalho.

### Produzir 24 · Plano de ação a partir de um diagnóstico
**Quando usar:** depois de uma análise que apontou problemas. Gera as linhas para a Semana Organizada ou para Projetos e Prazos.

```
A partir do diagnóstico abaixo, monte um plano de ação em tabela: Ação (verbo + objeto) | Resolve qual problema | Responsável | Prazo | Como saber que deu certo (medida) | Esforço (baixo/médio/alto). Máximo 8 ações, ordenadas por impacto ÷ esforço. Diga o que ficou de fora e por quê.
Diagnóstico: [cole]. Pessoas disponíveis: [liste]. Prazo total: [ex. 30 dias].
```
**Confira:** prazos (a IA distribui de forma otimista) e se toda ação tem medida de sucesso.

### Produzir 25 · Indicadores para um objetivo
**Quando usar:** para preencher a planilha Metas do Trimestre com resultados-chave que medem de verdade.

```
Para o objetivo abaixo, proponha 3 a 4 resultados-chave mensuráveis, cada um com: nome (até 8 palavras), unidade, ponto de partida provável, meta sugerida para 90 dias, de onde sai o número (planilha, sistema, contagem manual) e se maior ou menor é melhor. Evite indicadores que dependem só de esforço (ex.: "fazer 10 reuniões"); prefira resultado.
Objetivo: [uma frase]. Contexto: [tamanho da equipe, negócio, o que já medimos].
```
**Confira:** se você consegue medir cada um toda semana em menos de 5 minutos. Se não, troque.

### Produzir 26 · Orçamento do ano a partir do histórico
**Quando usar:** para preencher a aba Previsto da planilha Orçamento.

```
Com o histórico abaixo (por categoria e mês), proponha o orçamento do próximo ano por categoria e mês, com premissas explícitas: crescimento aplicado, sazonalidade (meses acima e abaixo da média), itens fixos e variáveis, e um cenário conservador e um otimista para a receita. Devolva uma tabela categoria × mês e uma lista de premissas de até 8 linhas.
Histórico: [cole "O ano, mês a mês" ou "Por categoria"]. O que sei que muda: [ex.: contratamos 1 pessoa em março].
```
**Confira:** as premissas, uma a uma. O número é consequência delas.

### Produzir 27 · Precificar uma hora ou um projeto
**Quando usar:** com a planilha Horas e Custo por Projeto na mão.

```
Com os dados abaixo, calcule e explique: custo-hora de cada pessoa; custo do projeto pelas horas estimadas; preço mínimo para margem de [30]%; preço sugerido considerando [risco de estouro de X%]; o que acontece se as horas estourarem em 20%. Mostre as contas. Ao fim, uma frase para justificar o preço ao cliente sem citar custo interno.
Pessoas (custo mensal e horas/mês): [cole]. Horas estimadas por pessoa: [cole]. Custos extras: [liste].
```
**Confira:** refaça a conta do custo-hora à mão. É a base de tudo.

### Produzir 28 · Rotina de fechamento mensal (o passo a passo)
**Quando usar:** dia 30. Gera o checklist do mês com as 10 planilhas do kit.

```
Monte o checklist de fechamento mensal de [meu negócio/minha área] usando estas planilhas: [liste as que você usa: Ganhos e Gastos, Orçamento, Relatório Mensal, Funil, Horas, Metas]. Para cada passo: o que abrir, o que preencher ou conferir, quanto tempo leva, o que sai (número, texto) e qual prompt usar em seguida. Ordene do dado bruto ao relatório enviado. Meta: fechar em [2 horas].
Quem recebe o fechamento: [cargo]. Dia de entrega: [dia].
```
**Confira:** rode o checklist uma vez cronometrando. Ajuste os tempos e cole na aba "Como usar" do Relatório Mensal.

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
