# Direção criativa do GPT-6 Astra — o que eu aceitei, adaptei e recusei

Data: 16/09/2026. Resposta original do GPT arquivada em `parecer-gpt-2026-09-16.txt`.
Quem decide o que fica: Eduardo. Abaixo está a minha leitura, com o motivo de cada escolha.

## Onde ele estava certo e eu estava errado

**1. Os números de horas não tinham fonte. Aceito e removo.**
Eu escrevi "6 horas por semana", "300 horas por ano" e "40 horas para montar as dez"
sem nenhuma medição. Inventei. Isso quebra a nossa própria regra em `CLAUDE.md`:
"Nunca inventar dados de mercado. Toda afirmação numérica cita a fonte ou é marcada
como estimativa." Marcar como estimativa não conserta uma comparação construída em
cima de um número arbitrário. **Saem os quatro ângulos que dependem dessas contas.**

**2. "Prompt sem planilha não tem dado" é falso. Aceito e reescrevo.**
O dado pode vir de e-mail, de PDF, de anotação. O que é defensável é: a IA responde
melhor quando recebe os números já organizados, e o kit entrega essa organização
pronta. A frase antiga vendia uma exclusividade que não existe.

**3. A página do Completo anunciava 12× de R$ 19,90. Corrigido hoje.**
Isso dá R$ 238,80, contra R$ 197 à vista, e a página não dizia o total. O valor da
parcela fui eu que inventei — nunca foi definido, e depende da taxa da Kiwify. Além
de errado, é exposição no CDC art. 52, que exige informar valor total, juros e número
de parcelas. Trocado por "12× no cartão (valor da parcela e total informados no
checkout)", igual às outras três páginas.

**4. "Relatório em 45 minutos" é uma promessa de desempenho que nunca medimos. Removido.**
Estava na página do Completo, num e-mail e em duas listas de headline. Trocado por
descrição do processo: você preenche, cola no prompt, revisa o que a IA devolve.
Mesma ideia, sem cronômetro que eu não posso provar. Também tirei "faz isso em
5 minutos" do passo Estruturar.

## Onde eu discordo dele

**5. Ele mata a técnica junto com o número. Eu mantenho a técnica.**
O GPT elimina os quatro ângulos de custo da inação porque os números eram inventados.
O número era o problema, não a técnica: custo da inação é um dos ângulos mais sólidos
de resposta direta. Existe versão honesta sem inventar nada — perguntar em vez de
afirmar: *"Quantas vezes você montou o mesmo relatório do zero este ano?"* Quem
responde faz a própria conta, e a conta é verdadeira porque é dele. **Mantenho um
ângulo assim por produto**, sem número na tela. Se você preferir seguir o GPT à
risca e cortar de vez, eu corto.

**6. "Sexta, 17h" ele descarta como fraco sem personagem. Concordo em parte.**
Future pacing sem rosto humano realmente perde força. Mas o problema não é a técnica:
é que eu ia mostrar a cena imaginada em vez do arquivo. Aceito a substituição dele
(mostrar onde preencher), e o future pacing volta como *frase de fecho*, não como
gancho — custa dois segundos e não depende de personagem.

**7. CTA "Ver o que vem no kit" no Completo: aceito como hipótese, com ressalva.**
Faz sentido para um produto 5,3× mais caro. A ressalva é operacional: com R$ 60/dia
o Completo vai ter pouquíssima conversão de qualquer jeito, então esse teste vai
demorar a dizer alguma coisa. O próprio GPT recomenda rodar o Essencial primeiro, e
é isso que eu faria: **o CTA mais leve só entra quando o Completo for ao ar de fato.**

## O ponto que conflita com uma regra sua

**8. Tela dentro do mockup × recorte legível.**
Sua regra desde 14/09: nenhuma tela de planilha aparece crua, sempre dentro de
notebook + celular. O GPT diz, com razão, que no celular o notebook inteiro deixa a
planilha ilegível, e que a inspeção do arquivo é justamente a prova mais forte que
temos — já que não temos depoimento nem número de vendas.

A saída que ele propõe resolve os dois: **notebook inteiro por até 1 segundo para dar
contexto, e aí a câmera entra no recorte legível**, com a etiqueta "Tela real do
arquivo · dados de empresa fictícia" visível o tempo todo. Isso não é tela crua: é
tela com contexto, que é o espírito da sua regra. **Vou produzir assim.** Se você
achar que fere a regra, eu volto atrás e mantenho só o mockup.

## Os dez ângulos finais

| # | Essencial (22 s) | Técnica |
|---|---|---|
| E1 | Relatório Mensal Pronto por dentro | Inspeção do produto |
| E2 | "Um relatório rapidinho" sobre a planilha real | Callout, com produto já na tela |
| E3 | "Seu prompt tem os números do trabalho?" | Mecanismo, demonstrado |
| E4 | "Veja onde preencher" | Primeiro uso guiado |
| E5 | "Você compra os arquivos. Não paga mensalidade." | Clareza do que se compra |
| E6* | "Quantas vezes você montou isso do zero este ano?" | Custo da inação sem número inventado |

| # | Completo (30 s) | Técnica |
|---|---|---|
| C1 | "Em qual categoria o orçamento passou do previsto?" | Pergunta concreta respondida |
| C2 | "Relatório. Projeto. Reunião." com os arquivos | Acúmulo, com prova |
| C3 | "Veja uma das dez por dentro" | Inspeção do produto |
| C4 | "Quem vai ler o seu próximo relatório?" | Destinatário, demonstrado no prompt |
| C5 | "Você cuida de projetos, metas e orçamento?" | Qualificação por escopo |

\* E6 é o meu ponto 5. São seis do Essencial: o sexto é o meu desacordo registrado.
Se você mandar cortar, ficam cinco e cinco.

## Estrutura (aceita como ele desenhou)

- **Essencial: 22 s**, cinco cenas. Preço aparece em etiqueta discreta aos 8 s,
  cartão de fechamento nos últimos 4 s.
- **Completo: 30 s**, seis cenas. Preço em etiqueta aos 12 s, fechamento nos últimos 5 s.
- Uma mudança relevante a cada 2 a 3 s; 3 a 4 s quando houver número para ler.
- Título de 4 a 7 palavras, apoio até 8. Uma ideia por tela.
- Legenda queimada em blocos de 4 a 6 palavras, no máximo duas linhas.
- Revisão final no mudo: tarefa, produto, preço e ação têm que ficar claros sem som.

## Plano de mídia (aceito, com os números dele marcados como hipótese)

Uma campanha ativa por vez, começando pelo Essencial. Um conjunto, dois criativos,
R$ 60/dia, público Brasil 18+ sem interesse, objetivo Vendas com evento Purchase.
CPA-alvo de R$ 18,50 no Essencial assume margem de 70% — **esse número muda quando
sair a taxa real da Kiwify**, e é a primeira coisa a recalcular depois que a conta
existir. Pausa do anúncio em 3× o alvo sem compra; pausa da rodada em 5×.

Isso precisa virar `08-ads/limites.json` com a sua aprovação registrada em
`DECISOES.md` antes de qualquer campanha existir. Nenhum real é gasto sem isso.

## O que ele apontou e ainda está aberto

- Ele não teve acesso aos `.xlsx` para conferir as fórmulas. Se quiser, mando os
  arquivos na próxima rodada e ele audita o produto, não só o anúncio.
- "Comprar no celular não é trabalhar no celular": o mockup com telefone pode
  sugerir uma experiência móvel que a planilha não entrega. A página precisa dizer
  qual é o ambiente recomendado. **Ainda não fiz.**
