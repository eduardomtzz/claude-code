# Copy: página do Kit de Gestão para Médicos (`/medicos/`)

Base: `02-oferta/medicos.md`. Mesmo molde da página do Advogados, que passou por revisão e é o padrão (herói com
mockup e contexto, dor logo depois, demonstração, método, inventário por núcleo, prompt anotado + aulas, para quem
é/não é, quem faz, preço em card único, FAQ). Regras: preço único R$ 697, 12× no cartão sem valor da parcela, sem
âncora riscada, sem promessa de resultado, de "lotar a agenda" ou de captar pacientes, nada clínico (diagnóstico,
conduta, prontuário, receituário), sem depoimento nem número de clientes, sem escassez, sem telefone/WhatsApp. A
página nunca diz "produzido com IA" nem "clínica fictícia" (o rodapé de cada tela do produto já diz "exemplo
fictício"; na página, "clínica de exemplo"). Publicidade médica é regulada pela Resolução CFM 2.336/2023: o kit é
gestão e a página não sugere nenhuma peça de divulgação. Requisito técnico: Excel 2016 ou mais novo, Microsoft 365
ou Google Sheets; celular só para ver.

## 1. Herói
<!-- Big Idea + "sem" objeção: mesma pergunta do Advogados, trocando escritório por clínica -->
- **Eyebrow:** Kit de Gestão para Médicos
- **Headline:** Você atende o dia inteiro. A clínica, quem administra?
- **Subheadline:** Vinte planilhas prontas em cinco núcleos: agenda, preço, caixa, recebíveis e painel. Você
  preenche; a planilha mede a ocupação e as faltas, calcula o custo da sua hora de atendimento e mostra se o mês
  deu lucro. Pagamento único de R$ 697.
- **Linha de transparência:** Kit de arquivos + aulas gravadas: 20 planilhas, 41 prompts de IA, 8 aulas de 2 a 3
  minutos, manual de implantação em 4 semanas, 3 modelos de apresentação. Não é software médico, não é prontuário,
  não tem mensalidade.
- **CTA:** Comprar por R$ 697 · **Topo:** Comprar R$ 697
- **Nota:** Pix ou 12× no cartão · acesso imediato · 7 dias para desistir
- **Mídia:** notebook com o Painel da Clínica (tela 17) e celular com a Agenda e Ocupação (tela 01). Barra: "20
  planilhas · computador e celular". Título de contexto: "Vinte planilhas prontas, no computador e no celular. Você
  digita; os painéis fazem o resto:" e três chips: a agenda mede ocupação e faltas; o custo da hora diz quanto
  cobrar; o caixa separa repasse e imposto. Legenda: "Telas reais. Clínica de exemplo."

## 2. Situação atual em três cenários
<!-- PAS com as frases do avatar (01-pesquisa: "trabalho muito e não vejo o dinheiro", convênio que paga em 60 dias e glosa, preço no chute) -->
Título: **Três coisas que a clínica pequena vive**
Lead: Atender você aprendeu. Administrar a clínica, ninguém ensinou. O kit cuida dessa parte.
1. **A agenda tem buraco, e ninguém sabe quanto ele custa.** Entre faltas, remarcações e horários vazios, ninguém
   mede quantas horas a clínica atende de verdade. → Com o kit: a Agenda e Ocupação mede horas disponíveis ×
   atendidas por profissional e sala; a planilha Faltas e retornos mostra a taxa de falta por dia e por convênio.
   A planilha mede; você decide. (Nome canônico da planilha 02: "Faltas e retornos".)
2. **O convênio manda a tabela, e você aceita sem calcular.** A guia sai em setembro, o pagamento chega em novembro,
   com glosa. E o preço da consulta particular veio da tabela do vizinho. → Com o kit: Custo da Hora de
   Atendimento e Simulador Convênio × Particular. Preço pela sua hora, com prazo e glosa esperada na conta.
3. **Entra dinheiro, sai repasse, e o imposto chega junto com o 13º.** A conta da clínica paga o repasse do colega,
   o pró-labore e o almoço de domingo, e no fim do mês ninguém sabe quanto sobrou. → Com o kit: Caixa com provisão,
   com o repasse aos parceiros e o pró-labore separados. Você sabe quanto pode retirar.

## 3. Demonstração
Aula 5 inteira, por toque: "Quanto cobrar por este procedimento" (`{{med_aula5_dur}}`). Título: "Quanto cobrar por
este procedimento, na tela". Lead: "A aula 5, completa. É assim que as outras sete funcionam: tela real, narração e
legenda, direto ao que fazer." Legenda: "Aula 5 · Quanto cobrar por este procedimento · {{med_aula5_dur}}. Narração
sintética, legendada." Arquivo: `/assets/medicos/videos/aula-05-quanto-cobrar-por-este-procedimento.mp4` (+ .vtt),
poster `/assets/medicos/poster-aula-05.jpg`.

## 4. Método: cinco núcleos, um fechamento por semana
<!-- mecanismo único da oferta; contraste com software de clínica (agenda e prontuário, mensalidade) -->
Lead: Software de clínica resolve agenda online e prontuário, e cobra todo mês. O kit resolve o dinheiro e o tempo
da clínica, uma vez. Doze minutos na segunda, dezoito na sexta.
1. **Agenda que se mede.** Horas disponíveis × atendidas por profissional e sala, faltas, remarcações e lista de
   retorno. A rotina de segunda confere a semana inteira. (Os minutos aparecem uma vez só, no lead da seção.)
2. **Preço pela hora.** Custo da hora de atendimento + material + margem = preço de consulta e procedimento. O
   simulador compara convênio × particular com prazo e glosa esperada.
3. **Caixa com provisão e repasse.** Impostos, 13º e férias provisionados; repasse aos parceiros e pró-labore
   separados antes de sobrar. Reserva de três meses de custo fixo.
4. **Recebíveis sem surpresa.** Guias enviadas × pagas × glosadas por convênio, parcelas particulares com a mensagem
   educada pronta, orçamentos apresentados × aprovados e conciliação de cartão.
5. **Painel de sexta.** Uma tela com ocupação, faltas, caixa, convênio a receber, glosas e orçamentos. O prompt
   "Explicar o mês" vira texto para o sócio e o contador.

## 5. Inventário: as vinte planilhas por núcleo
Lead: Quatro planilhas por núcleo, todas com a Clínica Vida Plena preenchida como exemplo, fórmulas protegidas e
aba "Como usar". Excel e Google Sheets. Cada núcleo com mockup (notebook + celular) e as 4 planilhas em uma linha
("Responde:" / "Sai:"), na ordem da oferta:
1. **1 · Agenda** (mock-agenda: telas 01 e 02). Agenda, faltas, rotina, checklist. Responde: quantas horas vazias
   e por que a agenda esvazia? Sai: ocupação por profissional e sala, taxa de falta por dia e convênio, lista de
   retorno; rotina de segunda e sexta; checklist de abertura e fechamento do dia.
2. **2 · Preço** (mock-preco: telas 05 e 06). Custo da hora, precificação, simulador, tabela. Responde: quanto
   custa a minha hora e quanto cobrar por este procedimento? Sai: custo da hora de atendimento, preço de consulta
   e procedimento com material e margem, simulador convênio × particular (prazo, glosa, custo do dinheiro) e
   tabela de referência.
3. **3 · Caixa** (mock-caixa: telas 09 e 10). Caixa, provisão, repasse, reserva. Responde: cadê o dinheiro e quanto
   posso retirar? Sai: entradas por paciente, convênio e categoria; provisão de impostos, 13º e férias; repasse aos
   parceiros e pró-labore separados; reserva de três meses.
4. **4 · Recebíveis** (mock-convenios: telas 13 e 14). Convênios, parcelas, orçamentos, cartão. Responde: quanto o
   convênio deve e quem atrasou? Sai: guias enviadas, pagas e glosadas com recurso de glosa; parcelas particulares
   com régua de cobrança; orçamentos apresentados × aprovados; conciliação de cartão e taxas.
5. **5 · Painel** (mock-painel: telas 17 e 20-painel). Painel, resultado, metas, resumo. Responde: a clínica deu
   lucro e estamos no ritmo? Sai: painel de sexta em uma tela, resultado do mês, metas do trimestre e o resumo que
   a IA transforma em texto.
Rodapé do bloco: "Nenhuma planilha guarda prontuário, diagnóstico ou conduta: só nome, contato, valor e data. O kit
é gestão da clínica. No celular, os aplicativos do Excel e do Sheets abrem e mostram as planilhas; para preencher,
use o computador."

## 6. Prompts e aulas
Título: **A IA explica o mês, escreve a cobrança e prepara a reunião com o contador. Você confere.**
Lead: Um prompt como ele é entregue, e a grade das aulas. São 8 prompts por núcleo e 9 no Caixa, 41 no total.
Regra número um: nunca cole nome, contato ou qualquer dado de paciente em IA pública. Os prompts usam Paciente A,
Convênio 1, e funcionam nas versões gratuitas atuais do ChatGPT, Copilot, Gemini e Claude, que são serviços de
terceiros, com regras próprias. (A soma é 41 porque o grupo Caixa tem um prompt a mais; o número não muda.)

### Prompt anotado (texto definitivo; a biblioteca 21 copia literalmente)

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
**Exemplo:** Entrada: o bloco único de agosto da Planilha 20 da Clínica Vida Plena (entrou, saiu,
resultado e margem do mês; horas disponíveis × atendidas da Dra. Carolina, do Dr. Paulo e da Dra. Renata;
guias enviadas, pagas e glosadas de Saúde Total, MediPlan e Vida Care; a receber e vencido dos particulares;
orçamentos apresentados, aprovados e abertos); comentário: "a Dra. Renata teve dois turnos com falta em
sequência; o MediPlan glosou três guias de consulta por código de procedimento errado; o Vida Care pagou o
lote de julho; o repasse da Renata saiu no dia 10". Saída: texto de 240 palavras com um "[explicar]" na
agenda (o bloco da 20 não traz ocupação por sala: acrescente a da Planilha 1 à mão) e a decisão: "recorrer
das três glosas do MediPlan até o dia 20 e confirmar por mensagem, na véspera, os retornos da terça de manhã".
**Confira:** cada "[explicar]" e se nenhum número foi alterado. O bloco da 20 só tem totais: nunca acrescente
nome de paciente nos comentários.

Nota fixa na página: "Nenhum prompt do kit produz conteúdo clínico nem peça de divulgação."

### Grade das 8 aulas
Títulos canônicos (os das capas dos vídeos); durações em `site/config.json`, `med_aulaN_dur` (provisórias "2:30 min"
até a gravação):
1. Antes de abrir a planilha: os cinco núcleos e a rotina · 2. Agenda, ocupação e faltas · 3. Custo da hora de
atendimento · 4. Preço e simulador de convênio · 5. Quanto cobrar por este procedimento · 6. Caixa, provisão e
repasse · 7. Convênios, parcelas e cobrança · 8. Painel de sexta e fechamento.
Nota: "Sem apresentador, sem enrolação. Cada aula vai direto ao que fazer na tela. Narração sintética, sempre
legendada."

### Bônus (3 cards, thumbs 300×400)
<!-- cada bônus mata uma objeção da oferta -->
- **thumb-mensagens** · 15 mensagens de confirmação, lembrete e cobrança: confirmação de consulta, lembrete da
  véspera, falta e remarcação, retorno, cobrança educada em degraus, confirmação de pagamento. E-mail e WhatsApp,
  tom educado, campos para preencher. Mensagens de rotina da recepção, não peças de divulgação. Mensagem enviada a
  um grupo grande de pacientes deve ser revista pelas regras do CFM e do seu CRM antes de usar (mesma ressalva do
  bônus 22 e da biblioteca 21).
- **thumb-lgpd** · Guia LGPD para clínica pequena: dado de saúde é sensível. O que guardar, onde, por quanto tempo,
  e o que nunca colar em IA pública. Com aviso de privacidade modelo.
- **thumb-contador** · Roteiro da reunião mensal com o contador: PJ médica, Simples × presumido, o que levar do kit,
  o que perguntar. Mais 3 modelos de apresentação (resultado do mês, proposta de parceria, convênios e caixa para o
  contador) e 3 checklists.

## 7. Para quem é / não é
É para você se: tem consultório ou clínica pequena, atende particular e convênio e faz o administrativo; quer saber
quanto custa a sua hora antes de aceitar a tabela de um convênio; quer que a gestão caiba em 30 minutos por semana;
já viu software de clínica e paga sem usar a parte financeira, ou desistiu.
Não é para você se: precisa de prontuário eletrônico, agenda online ou envio de guias (isso é software); quer
orientação clínica, modelo de contrato ou peça de divulgação; tem clínica grande, com vários usuários lançando ao
mesmo tempo; espera que a planilha decida por você.

## 8. Quem faz
Mesmo bloco das outras páginas (ZTRAINING SERVICE LTDA, recalculada e conferida célula a célula, sem depoimento
inventado). Acrescentar: "Uma tela real de cada núcleo está nesta página; cada arquivo tem versão e data de
revisão. O
exemplo é a Clínica Vida Plena, uma clínica de exemplo: nenhum dado de clínica ou paciente real."

## 9. Preço e direito de arrependimento
- Eyebrow: Um plano, um preço. Título: Pagamento único de R$ 697.
- Sub (mono): Ou 12× no cartão (total informado no checkout). Pagamento único: software de clínica cobra
  mensalidade enquanto você usar; aqui você paga uma vez e os arquivos ficam com você. (A âncora é a forma de
  cobrança — pagamento único × mensalidade —, não o valor: a comparação "menos que um ano de software" tinha folga
  de 6 % contra o plano mais barato da nossa pesquisa, R$ 62/mês em `01-pesquisa/saas-precos.md`. Sem superlativo,
  sem marca.)
- Lista: 20 planilhas em 5 núcleos (Excel e Google Sheets), exemplo preenchido e fórmulas protegidas · 41 prompts da
  clínica em 5 grupos (PDF e txt): 8 por núcleo e 9 no Caixa · 8 aulas curtas com legenda · manual de implantação em 4 semanas · 3 modelos de apresentação
  e 3 checklists · 3 bônus: mensagens, guia LGPD e roteiro da reunião com o contador · acesso imediato após a
  aprovação.
- CTA: Comprar por R$ 697. Nota: Pix ou 12× no cartão · acesso imediato · nota fiscal.
- Card: Direito de arrependimento de 7 dias (texto padrão).

## 10. FAQ (10)
1. **Isso substitui o software da clínica?** Não. O kit cuida do dinheiro, da agenda em números e da rotina.
   Prontuário, agenda online e envio de guias continuam onde estão.
2. **É prontuário? Tem algum conteúdo clínico?** Não. Nenhuma planilha guarda dado clínico: só nome, contato, valor
   e data. Nada de diagnóstico, conduta ou receita. O kit é gestão da clínica.
3. **Serve para clínica com convênio e particular?** Sim. O simulador compara os dois com prazo e glosa; o caixa
   separa as entradas por convênio e particular; os recebíveis têm guia, glosa e parcela. Só particular ou só
   convênio também funciona: as colunas que não usar ficam vazias.
4. **Preciso saber Excel?** Precisa saber digitar em uma célula. As fórmulas estão prontas e protegidas; as aulas
   mostram cada planilha na tela.
5. **Funciona no Google Sheets?** Sim, todas as vinte abrem no Sheets e no Excel 2016 ou mais novo (inclusive
   Microsoft 365): só usam funções que existem nos dois. No celular, os aplicativos abrem e mostram; para
   preencher, use o computador.
6. **Posso usar com os sócios e a equipe da clínica?** Sim. A licença é de uso da clínica que comprou, em quantos
   computadores quiser; sócios, médicos parceiros e recepção preenchem as planilhas com você. O que não pode é
   revender, redistribuir ou usar o kit para implantar em outras clínicas.
7. **E os dados dos meus pacientes?** Ficam no seu arquivo, no seu computador ou no seu Drive. Nada passa por nós. As
   planilhas pedem só nome, contato, valor e data; os prompts usam apelidos, e o guia LGPD explica o que nunca
   colar em IA pública.
8. **Preciso pagar ChatGPT ou outra IA?** Não. Os prompts funcionam nas versões gratuitas atuais. ChatGPT,
   Copilot, Gemini e Claude são serviços de terceiros, com regras próprias: os planos e os limites podem mudar sem
   aviso. (Mesma FAQ da /advogados; a /medicos não pode afirmar o gratuito sem essa ressalva.)
9. **Como recebo?** Na hora, após a aprovação: e-mail com o link da área de download. Pix e cartão aprovam em
   minutos.
10. **E se eu não gostar?** 7 dias para desistir, sem perguntas. É a lei, e a gente cumpre sem burocracia.

## Página de obrigado
`/obrigado/` (e `/obrigado/pix/`, `/obrigado/recusado/`) segue neutra entre os kits. Card "Comece pelo manual":
manual de 20 minutos no Advogados e no Médicos; a aula 1 vem antes de qualquer planilha. Card "Primeiros 7 dias",
bloco do Médicos: dia 1 aula 1 + 05 Custo da hora de atendimento (20 min, como no manual) → dia 2 01 Agenda e
ocupação com a agenda desta semana → dia 3 06 Precificação e 07 Simulador convênio × particular com um procedimento
real (aulas 4 e 5: a 07 é assunto da aula 4) → dia 5 09 Caixa da clínica e o primeiro painel de sexta. Os quatro
kits ficam cada um em um `<details>`, com o Essencial aberto, para o comprador não rolar roteiro alheio. Em `/obrigado/pix/`, "volte à página do kit" com os quatro links
(/kit/, /completo/, /advogados/, /medicos/).

## E-mails
Mesma sequência de `05-checkout/emails.md`, com bloco **Médicos**: D+0 assunto "Seu Kit de Gestão para Médicos está
pronto para baixar", ordem manual (20 min) → aula 1 → 05 Custo da hora de atendimento → 01 Agenda e ocupação;
D+1 assunto "15 minutos para saber quanto custa a sua hora de atendimento" (aula 3); D+5 "Quanto cobrar por este
procedimento" (aula 5). Requisito: Excel 2016 ou mais novo, Microsoft 365 ou Google Sheets. Regra número um: nunca
cole nome ou dado de paciente em IA pública.

## Anúncios (3 ângulos)
<!-- sem atributo pessoal, sem promessa, sem "lotar agenda"; público "Para médicos" -->
**Ângulo 1 · A clínica, quem administra?** Primária curta: Você atende o dia inteiro. A clínica, quem administra?
20 planilhas prontas: agenda, preço, caixa, convênios e painel. R$ 697, uma vez. Primária média: Atender você
aprendeu; administrar a clínica, ninguém ensinou. O Kit de Gestão para Médicos traz 20 planilhas prontas em 5
núcleos, 41 prompts de IA e 8 aulas curtas. Doze minutos na segunda, dezoito na sexta. Sem mensalidade. Headlines:
Quanto custa a sua hora? · Agenda que se mede · Caixa com provisão e repasse · Kit de Gestão para Médicos · Sem
mensalidade. Descrições: 20 planilhas, 41 prompts, 8 aulas. R$ 697, uma vez. · Não é software, não é prontuário. ·
7 dias para desistir.
**Ângulo 2 · O convênio na conta.** Primária: A tabela do convênio paga em 60 dias, com glosa. Vale a pena? O Custo
da Hora de Atendimento e o Simulador Convênio × Particular colocam prazo e glosa na conta antes de você assinar.
Headlines: Preço pela hora, não pela tabela · Simulador convênio × particular · 20 planilhas, 5 núcleos. Descrições:
Custo da sua hora em 15 minutos. · Pagamento único, arquivos seus. · Excel e Google Sheets.
**Ângulo 3 · Veja funcionando.** Primária: Tela real, clínica de exemplo: a agenda que mede ocupação e faltas e o
painel de sexta em uma tela. Não é software, não é prontuário, não tem mensalidade. Headlines: Tela real, sem
promessa · Painel de sexta · Pagamento único, sem mensalidade. Descrições: Aula 5 inteira na página. · 20
planilhas em 5 núcleos. · R$ 697, uma vez.
