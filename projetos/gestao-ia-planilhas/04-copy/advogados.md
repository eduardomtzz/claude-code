# Copy: página do Kit de Gestão para Advogados (`/advogados/`)

Base: `02-oferta/advogados.md`. Mesmo molde das páginas do Essencial e do Completo (herói com mockup e contexto,
dor logo depois, demonstração, método, inventário por núcleo, prompt anotado + aulas, para quem é/não é, quem faz,
preço em card único, FAQ). Regras: preço único R$ 497, sem âncora riscada, sem promessa de causa ganha ou de
"nunca mais perder prazo", sem conteúdo jurídico, sem telefone/WhatsApp.

## 1. Herói
- **Eyebrow:** Kit de Gestão para Advogados
- **Headline:** Você advoga o dia inteiro. O escritório, quem administra?
- **Subheadline:** Vinte planilhas prontas em cinco núcleos: prazos, honorários, caixa, carteira e painel. Você
  preenche, a planilha avisa o que vence, calcula o custo da sua hora e mostra se o mês deu lucro. Pagamento
  único de R$ 497.
- **Linha de transparência:** Kit de arquivos + aulas gravadas: 20 planilhas, 40 prompts de IA, 8 aulas de 2 a 3
  minutos, manual de implantação em 4 semanas, 3 modelos de apresentação. Não é software jurídico, não é
  consultoria, não tem mensalidade.
- **CTA:** Comprar por R$ 497 · **Topo:** Comprar R$ 497
- **Nota:** Pix ou 12× no cartão · acesso imediato · 7 dias para desistir
- **Mídia:** notebook com o Painel do Escritório e celular com a Agenda de Prazos. Título de contexto: "Vinte
  planilhas prontas, no computador e no celular. Você digita; os painéis fazem o resto:" e três chips: o semáforo
  mostra o que vence primeiro; o custo-hora diz quanto cobrar; o caixa separa o que é seu do que é do escritório.

## 2. Situação atual em três cenários
Título: **Três coisas que o escritório pequeno vive**
1. **O prazo está no caderno, na agenda do celular e no e-mail.** Você confere os três toda manhã e ainda fica com
   a sensação de que esqueceu um. → Com o kit: Agenda de Prazos com semáforo por dias e a rotina de segunda. A
   planilha avisa; você decide.
2. **O cliente pergunta "quanto fica?" e você responde de cabeça.** Fecha o caso, trabalha quarenta horas e
   descobre que cobrou menos que o custo. → Com o kit: Custo-Hora e Simulador de Honorários. Proposta com margem:
   vinte minutos na primeira vez; depois, cinco (como diz a aula 5).
3. **Entra dinheiro, sai dinheiro, e o imposto chega junto com o 13º.** A conta do escritório paga o almoço de
   domingo. → Com o kit: Caixa com provisão e Pró-labore separado. Você sabe quanto pode retirar.

## 3. Demonstração
Aula 5 inteira, por toque: "Custo-hora e proposta: quanto cobrar por este caso" (2:44). Legenda na página: "Aula 5 ·
Custo-hora e proposta: quanto cobrar por este caso · 2:44 min. Narração sintética, legendada."

## 4. Método: cinco núcleos, um fechamento por semana
1. **Prazos sob controle.** Cada processo com as próximas datas e o semáforo. Segunda-feira, 12 minutos.
2. **Honorário pela hora, não pelo chute.** Custo-hora × horas do caso + margem = proposta.
3. **Caixa com provisão.** Impostos, 13º e pró-labore separados antes de sobrar.
4. **Carteira viva.** Quem deve, quanto, e a mensagem educada pronta para cobrar.
5. **Painel de sexta.** Uma tela com prazos, horas, caixa, recebíveis e propostas. O prompt "Explicar o mês"
   transforma em texto para o sócio e para o contador. Sexta-feira, 18 minutos.
Sub: Software jurídico resolve publicação e petição, e cobra todo mês. O kit resolve o dinheiro e o tempo do
escritório, uma vez. Doze minutos na segunda, dezoito na sexta (rotina da planilha 03).

## 5. Inventário: as vinte planilhas por núcleo
Cada núcleo com print do painel e as 4 planilhas em uma linha cada ("Responde:" / "Sai:"), na ordem da oferta.
Rodapé do bloco: "Todas com o escritório fictício Ferraz & Lima preenchido como exemplo, fórmulas protegidas e aba
Como usar. Excel e Google Sheets. Nenhuma planilha contém peça, modelo ou orientação jurídica. No celular, os
aplicativos do Excel e do Sheets abrem e mostram as planilhas; para preencher, use o computador."

## 6. Prompts e aulas
Título: **A IA explica o mês, escreve a cobrança e prepara a reunião com o contador. Você confere.**
Prompt anotado: "Painel 01 · Explicar o mês ao sócio", texto literal da biblioteca (21, seção Painel 01):
- Quando usar: na sexta de fechamento, com o Painel do escritório e o Resumo do mês. É o prompt mais usado do kit.
- Cole: Planilha 20 · aba Resumo ("Bloco único para copiar").
- Prompt:
  ```
  Explique o mês de um escritório de advocacia para o meu sócio, em até 250 palavras e linguagem direta. Use só os números abaixo. Estrutura: uma frase com o resultado do mês; prazos (quantos cumpridos, quantos atrasaram, o padrão); horas (gastas × faturáveis por pessoa, o caso que mais consumiu); caixa (entrou, saiu, sobrou, provisão feita); recebíveis (a receber, atrasado); propostas (enviadas, fechadas, abertas); uma decisão para o mês que vem. Onde faltar explicação, escreva "[explicar]" para eu preencher. Não comente o mérito de nenhum caso.
  Meus comentários: [o que aconteceu, por quê].
  Números:
  [cole o bloco da aba Resumo]
  ```
- Confira: cada "[explicar]" e se nenhum número foi alterado.
Nota fixa: "Nenhum prompt do kit produz petição, parecer ou tese. E a regra número um: nunca cole nome de cliente
ou número de processo real em IA pública. Os prompts usam Cliente A, Processo 1."
Grade das 8 aulas (títulos canônicos, os das capas dos vídeos; durações em `site/config.json`, `adv_aulaN_dur`):
1. Antes de abrir a planilha: os cinco núcleos e a rotina (2:28) · 2. Agenda de prazos e andamento (2:19) ·
3. Custo-hora do escritório (2:20) · 4. Simulador e tabela de honorários (2:15) · 5. Custo-hora e proposta: quanto
cobrar por este caso (2:44) · 6. Caixa, provisão e pró-labore (2:33) · 7. Carteira, parcelas e cobrança (2:38) ·
8. Painel de sexta e fechamento (2:47).
Bônus (3 cards): mensagens de cobrança e confirmação (15 modelos) · guia LGPD para escritório pequeno · roteiro
da reunião mensal com o contador. Mais: 3 modelos de apresentação (resultado do mês, proposta, carteira para o
contador) e 3 checklists.

## 7. Para quem é / não é
É para você se: advoga solo ou em escritório de até 4 pessoas; cobra fixo, por hora ou êxito e quer saber a margem;
faz o administrativo e quer que caiba em 30 minutos por semana; já viu software jurídico e achou caro ou grande demais.
Não é para você se: precisa de controle de publicações e intimações automático (isso é software); quer modelos de
petição ou orientação jurídica; tem equipe grande com vários usuários ao mesmo tempo; espera que a planilha decida
por você.

## 8. Quem faz
Mesmo bloco das outras páginas (ZTRAINING SERVICE LTDA, recalculada e conferida célula a célula, sem depoimento
inventado). Acrescentar: "A tela real das vinte está nesta página; cada arquivo tem versão e data de revisão. O exemplo
é um escritório fictício, Ferraz & Lima: nenhum dado de escritório real."

## 9. Preço e direito de arrependimento
- Eyebrow: Um plano, um preço. Título: Pagamento único de R$ 497.
- Sub (mono): Ou 12× no cartão (total informado no checkout). Menos que três meses de um software jurídico típico,
  uma vez, e os arquivos ficam com você. (Sem superlativo: "mais barato" não é verificável.)
- Lista: 20 planilhas em 5 núcleos (Excel e Google Sheets), exemplo preenchido e fórmulas protegidas · 40 prompts do
  escritório (PDF e txt) · 8 aulas curtas com legenda · manual de implantação em 4 semanas · 3 modelos de apresentação
  e 3 checklists · 3 bônus: cobrança, LGPD e reunião com o contador · acesso imediato após a aprovação.
- CTA: Comprar por R$ 497. Nota: Pix ou 12× no cartão · acesso imediato · nota fiscal.
- Card: Direito de arrependimento de 7 dias (texto padrão).

## 10. FAQ (10)
1. **Isso substitui o software jurídico?** Não. O kit cuida do dinheiro, das horas e da rotina do escritório. Publicações,
   intimações e petições continuam onde estão.
2. **Tem alguma peça, modelo de petição ou contrato?** Não. Nenhum conteúdo jurídico: você sabe fazer o seu.
3. **Preciso saber Excel?** Precisa saber digitar em uma célula. As fórmulas estão prontas e protegidas; as aulas mostram
   cada planilha na tela.
4. **Funciona no Google Sheets?** Sim, todas as vinte abrem no Sheets e no Excel 2016 ou mais novo (inclusive
   Microsoft 365): só usam funções que existem nos dois. No celular, os aplicativos abrem e mostram; para preencher,
   use o computador.
5. **Serve para escritório com sócios?** Sim, até 4 pessoas. As planilhas separam por responsável e por sócio.
5b. **Posso usar com os sócios e a equipe do escritório?** Sim. A licença é de uso do escritório que comprou, em quantos
   computadores quiser; sócios, associados e estagiários preenchem as planilhas com você. O que não pode é revender,
   redistribuir ou usar o kit para implantar em outros escritórios.
6. **E os dados dos meus clientes?** Ficam no seu arquivo, no seu computador ou no seu Drive. Nada passa por nós. Os
   prompts usam apelidos; o guia LGPD explica o que nunca colar em IA pública.
7. **Preciso pagar ChatGPT ou outra IA?** Não. Os prompts funcionam nas versões gratuitas.
8. **Como recebo?** Por e-mail e área de download, logo após a aprovação do pagamento.
9. **E se eu não gostar?** 7 dias para pedir o dinheiro de volta, sem explicar, pela página do pedido ou por e-mail.

## Página de obrigado
`/obrigado/` (e `/obrigado/pix/`, `/obrigado/recusado/`) é neutra entre os três kits: eyebrow só "Seu Sócio Gestor",
sem nome de kit na description. Card "Comece pelo manual" aponta para o LEIA-ME de cada kit (manual de 20 minutos no
Advogados). Card "Primeiros 7 dias" com um bloco por kit; o do Advogados: dia 1 aula 1 + 05 Custo-hora (15 min) →
dia 2 01 Agenda de prazos → dia 3 06 Simulador e 07 Proposta (aula 5) → dia 5 09 Caixa e o primeiro painel de sexta.
Em `/obrigado/pix/`, "volte à página do kit" com os três links (/kit/, /completo/, /advogados/).

## E-mails
Mesma sequência de `05-checkout/emails.md`, com bloco **Advogados**: D+0 assunto "Seu Kit de Gestão para Advogados
está pronto para baixar", ordem manual (20 min) → aula 1 (2 min 28 s) → 05-custo-hora → 01-agenda de prazos; D+1
assunto "15 minutos para saber quanto custa a sua hora" (aula 3); D+5 "A proposta de honorários com margem" (aula 5).
Requisito: Excel 2016 ou mais novo, Microsoft 365 ou Google Sheets.

## Anúncios (3 ângulos)
**Ângulo 1 · O escritório, quem administra?** Primária curta: Você advoga o dia inteiro. O escritório, quem administra?
20 planilhas prontas: prazos, honorários, caixa, carteira e painel. R$ 497, uma vez. Headlines: Quanto custa a sua
hora? · Prazos com semáforo · Caixa com provisão · Kit de Gestão para Advogados · Sem mensalidade.
**Ângulo 2 · Cobrou menos que o custo.** Primária: Fechou o caso, trabalhou quarenta horas e cobrou menos que o
custo da sua hora. O Custo-Hora e o Simulador de Honorários mostram a margem antes de você mandar a proposta.
Headlines: Honorário pela hora, não pelo chute · Proposta com margem em 20 minutos · 20 planilhas, 5 núcleos.
**Ângulo 3 · Veja funcionando.** Primária: Tela real, escritório fictício: a agenda que ordena o que vence primeiro e o
painel de sexta em uma tela. Não é software, não tem mensalidade. Headlines: Tela real, sem promessa · Painel de
sexta · Menos que três meses de software, uma vez.
