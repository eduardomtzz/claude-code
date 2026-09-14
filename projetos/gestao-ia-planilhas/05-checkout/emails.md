# E-mails de entrega e pós-compra · Kit IA no Trabalho (Essencial e Completo), Kit de Gestão para Advogados e Kit de Gestão para Médicos

Texto final, pronto para colar na automação de e-mail da Kiwify (ou no provedor que for usado).
Data: 13/09/2026. Remetente sugerido: `Seu Sócio Gestor <suporte@seusociogestor.com.br>`.

Regras que valem para todos:
- Transacionais (acesso, Pix pendente, reembolso) vão para todo comprador. Os demais só com opt-in
  de comunicação marcado no checkout (LGPD, art. 7º, I). Todo e-mail não transacional tem link de descadastro.
- Sem WhatsApp, sem telefone. Suporte só por e-mail, resposta em até 5 dias úteis.
- Sem desconto automático, sem "última chance", sem contagem regressiva.
- Campos entre colchetes são variáveis do provedor: `[Nome]`, `[Nº do pedido]`, `[Data]`, `[Valor]`,
  `[Link de acesso]`, `[Link do pedido]`, `[Validade do Pix]`. Mapear para as variáveis da Kiwify ao configurar.
- Onde o texto muda por kit, há quatro blocos: **Essencial**, **Completo**, **Advogados** e **Médicos**. O resto é igual.
- Rodapé fixo em todos (abaixo).

Rodapé fixo:
```
Seu Sócio Gestor é uma marca da ZTRAINING SERVICE LTDA · CNPJ 68.796.613/0001-10
Praça das Dracenas, 50, Térreo, Condomínio Centro Comercial Alphaville, Barueri/SP, CEP 06453-064
Atendimento: suporte@seusociogestor.com.br (resposta em até 5 dias úteis)
Termos de uso: https://seusociogestor.com.br/termos/ · Privacidade: https://seusociogestor.com.br/privacidade/
```

---

## 1. D+0 · Acesso liberado (transacional, dispara no pagamento aprovado)

**Assunto (Essencial):** Seu Kit IA no Trabalho · Essencial está pronto para baixar
**Assunto (Completo):** Seu Kit IA no Trabalho · Completo está pronto para baixar
**Assunto (Advogados):** Seu Kit de Gestão para Advogados está pronto para baixar
**Assunto (Médicos):** Seu Kit de Gestão para Médicos está pronto para baixar

```
Olá, [Nome].

Pagamento confirmado. Seus arquivos já estão liberados:

    [Link de acesso]

Esse link também fica na sua área de compras da plataforma de pagamento. Guarde este e-mail.

RESUMO DO PEDIDO
Produto: [Kit IA no Trabalho · Essencial | Kit IA no Trabalho · Completo | Kit de Gestão para Advogados | Kit de Gestão para Médicos]
Pedido: [Nº do pedido] · Data: [Data] · Valor: [Valor] (pagamento único, sem renovação)
Nota fiscal: emitida em nome do comprador e enviada por e-mail.

POR ONDE COMEÇAR (15 minutos)
```

**Essencial:**
```
1. Abra o "05-mini-manual.pdf". Ele mostra a ordem e o que apagar.
2. Abra "01-semana-organizada.xlsx", apague as tarefas de exemplo e digite cinco das suas.
3. Veja a aba Hoje montar a sua semana. Pronto: primeiro arquivo funcionando.
Os 40 prompts estão em "04-biblioteca-de-prompts" (PDF e TXT). Os 3 vídeos estão na pasta "videos".
```

**Completo:**
```
1. Abra o "14-manual-do-metodo.pdf" e assista à aula 1 (2 min 25 s). Ela vem antes de qualquer planilha.
2. Abra "01-semana-organizada.xlsx", apague as tarefas de exemplo e digite cinco das suas.
3. Amanhã: "06-metas-do-trimestre.xlsx" com uma meta real. O semáforo faz o resto.
Os 80 prompts estão nas bibliotecas "11-a" e "11-b" (PDF e TXT). As 8 aulas estão na pasta "videos".
```

**Advogados:**
```
1. Abra o "26-manual-de-implantacao.pdf" (20 minutos de leitura) e assista à aula 1, "Antes de abrir a planilha: os cinco núcleos e a rotina" (2 min 35 s). Ela vem antes de qualquer planilha.
2. Abra "05-custo-hora.xlsx", troque os custos fixos e as horas pelos seus: quinze minutos e você sabe quanto custa a sua hora.
3. Amanhã: "01-agenda-de-prazos.xlsx" com os prazos desta semana. O semáforo faz o resto.
Os 40 prompts estão em "21-biblioteca-de-prompts-do-escritorio" (PDF e TXT). As 8 aulas estão na pasta "videos".
Regra número um: nunca cole nome de cliente ou número de processo real em IA pública.
```

**Médicos:**
```
1. Abra o "26-manual-de-implantacao.pdf" (20 minutos de leitura) e assista à aula 1, "Antes de abrir a planilha: os cinco núcleos e a rotina" (2 min 30 s). Ela vem antes de qualquer planilha.
2. Abra "05-custo-da-hora.xlsx", troque os custos fixos, a equipe, o pró-labore e as horas de atendimento pelos seus: quinze minutos e você sabe quanto custa a sua hora de atendimento.
3. Amanhã: "01-agenda-e-ocupacao.xlsx" com a agenda desta semana. A ocupação e as faltas aparecem sozinhas.
Os 40 prompts estão em "21-biblioteca-de-prompts-da-clinica" (PDF e TXT). As 8 aulas estão na pasta "videos".
Regra número um: nunca cole nome, contato ou qualquer dado de paciente em IA pública. Nenhuma planilha do kit guarda dado clínico: só nome, contato, valor e data.
```
(Nomes de arquivo e duração da aula 1 conferidos com o `LEIA-ME.txt` do kit antes de colar na Kiwify.)

```
REQUISITOS
Essencial, Advogados e Médicos: Excel 2016 ou mais novo (inclusive Microsoft 365) ou Google Sheets. Completo:
Excel 2019 ou mais novo (inclusive Microsoft 365) ou Google Sheets; no Excel 2016 ou anterior, as
planilhas que usam MÍNIMOSES, MÁXIMOSES e UNIRTEXTO mostram "#NOME?".
No celular, abre nos aplicativos dos dois; para preencher, use o computador. Os prompts funcionam nas versões gratuitas do ChatGPT,
Copilot, Gemini e Claude. Sem macros, sem login, sem mensalidade.

SE ALGO NÃO ABRIR
Responda este e-mail com o nome do arquivo e o que apareceu na tela. Respondemos em até 5 dias úteis.

DIREITO DE ARREPENDIMENTO
Você tem 7 dias corridos a partir de hoje para desistir, sem explicar (CDC, art. 49). Peça pela sua
área de compras ou respondendo este e-mail. O valor volta pelo mesmo meio de pagamento.

Ao comprar, você aceitou os Termos de uso. Uma cópia está sempre em https://seusociogestor.com.br/termos/.

Bom trabalho,
Seu Sócio Gestor
```
+ rodapé fixo.

---

## 2. D+1 · Primeira tarefa (opt-in)

**Assunto (Essencial e Completo):** 15 minutos para a Semana Organizada funcionar
**Assunto (Advogados):** 15 minutos para saber quanto custa a sua hora
**Assunto (Médicos):** 15 minutos para saber quanto custa a sua hora de atendimento

**Essencial e Completo:**
```
Olá, [Nome].

Ontem você recebeu o kit. Hoje é o dia de fazer o primeiro arquivo trabalhar para você.

1. Abra "01-semana-organizada.xlsx" na aba Tarefas.
2. Apague as linhas de exemplo (só as amarelas são suas).
3. Digite cinco tarefas reais, com prazo e impacto.
4. Vá para a aba Hoje. Ela já ordenou o que fazer primeiro e mostra a carga dos próximos 7 dias.

Se quiser que a IA ajude a priorizar: copie o prompt "Organizar 01" da biblioteca, cole a sua lista
no campo indicado e compare com a ordem da planilha.
```

**Essencial:** `O vídeo 1 (57 s) mostra tudo isso na tela.`
**Completo:** `A aula 1 (2 min 25 s) explica por que definir quem lê e quando antes de abrir o Excel. Vale ver antes.`

**Advogados (bloco inteiro, no lugar do de cima):**
```
Olá, [Nome].

Ontem você recebeu o kit. Hoje é o dia de descobrir quanto custa a sua hora, o número que sustenta todo o resto.

1. Abra "05-custo-hora.xlsx" na aba Custos.
2. Troque os custos fixos, o pró-labore e as horas faturáveis do exemplo pelos seus (só as células amarelas).
3. A hora mínima a cobrar aparece no painel. Compare com o que você cobrou no último caso.

A aula 3, "Custo-hora do escritório" (2 min 20 s), mostra tudo isso na tela.
```

**Médicos (bloco inteiro, no lugar do de cima):**
```
Olá, [Nome].

Ontem você recebeu o kit. Hoje é o dia de descobrir quanto custa a sua hora de atendimento, o número que sustenta o preço da consulta, do procedimento e a conversa com o convênio.

1. Abra "05-custo-da-hora.xlsx" na aba Custos.
2. Troque os custos fixos, a equipe, o pró-labore e as horas de atendimento do exemplo pelos seus (só as células amarelas).
3. O custo da hora aparece no painel. Compare com o que o seu convênio mais usado paga por consulta.

A aula 3, "Custo da hora de atendimento" (2 min 30 s), mostra tudo isso na tela.
```

```
Dúvida? Responda este e-mail.

Seu Sócio Gestor
```
+ rodapé fixo + link de descadastro.

---

## 3. D+3 · Conseguiu abrir? (opt-in)

**Assunto:** Tudo abriu certo?

```
Olá, [Nome].

Uma pergunta só: você conseguiu abrir e preencher o primeiro arquivo?

Se sim, ótimo. O próximo passo está no e-mail de depois de amanhã.

Se não, os três erros mais comuns e a solução:
- "A planilha abriu só leitura": salve uma cópia no seu computador ou no seu Drive antes de editar.
- "As fórmulas mostram #NOME?": abra no Excel 2016 ou mais novo (Essencial, Advogados e Médicos) ou no Excel 2019 ou mais novo (Completo), ou no Google Sheets. Versões antigas não têm algumas funções.
- "Apaguei uma fórmula sem querer": baixe o arquivo de novo pelo link de acesso. Só as células amarelas são para digitar.

Qualquer outra coisa, responda este e-mail com o nome do arquivo e o que apareceu. Respondemos em até 5 dias úteis.

Seu Sócio Gestor
```
+ rodapé fixo + descadastro.

---

## 4. D+5 · Segunda aplicação (opt-in)

**Assunto (Essencial):** O relatório do mês em 45 minutos
**Assunto (Completo):** O relatório do mês em 45 minutos, com a aula 5
**Assunto (Advogados):** A proposta de honorários com margem
**Assunto (Médicos):** Quanto cobrar por este procedimento

```
Olá, [Nome].

Semana organizada. Agora o relatório do mês, que costuma atrasar.

1. Abra "02-relatorio-mensal-pronto.xlsx" e digite os 12 números do mês (receita, despesas, clientes...). Só as células amarelas.
2. A aba Resumo escreve as frases-base sozinha e monta o "bloco único para copiar".
3. Cole esse bloco no prompt "Escrever 01". A IA devolve um relatório de 300 palavras.
4. Confira cada "[explicar]" e cada número. Se nada mudou, envie.
```

**Essencial:** `Quer apresentar? O modelo de 8 slides ("06-modelo-apresentacao-8-slides.pptx") já tem a ordem certa. E o "07-checklist-antes-de-enviar.pdf" fecha o trabalho.`
**Completo:** `A aula 5 (2 min 26 s) faz esse caminho inteiro na tela. Para apresentar, use o modelo de 8 slides ("15-modelo-relatorio-mensal-8-slides.pptx") e o prompt "Apresentar 01".`
**Advogados (substitui os passos acima):** `Hora calculada. Agora a proposta. Abra "06-simulador-de-honorarios.xlsx" com um caso real: horas por etapa, custo-hora, margem. Compare fixo, hora, êxito e misto. Depois "07-proposta-de-honorarios.xlsx" monta a tabela para o cliente. Vinte minutos na primeira vez; depois, cinco. A aula 5, "Custo-hora e proposta: quanto cobrar por este caso" (2 min 44 s), mostra tudo na tela.`
**Médicos (substitui os passos acima):** `Hora calculada. Agora o preço. Abra "06-precificacao.xlsx" com um procedimento real: custo da hora, tempo, material, margem. Depois "07-simulador-convenio-x-particular.xlsx" compara a tabela do convênio com o particular, contando prazo de pagamento e glosa esperada. Vinte minutos na primeira vez; depois, cinco. A aula 5, "Quanto cobrar por este procedimento" (2 min 30 s), mostra tudo na tela.`

```
Seu Sócio Gestor
```
+ rodapé fixo + descadastro.

---

## 5. D+6 · Lembrete neutro do prazo (opt-in; se não houver opt-in, não enviar)

**Assunto:** Seu prazo de 7 dias termina amanhã

```
Olá, [Nome].

Amanhã termina o prazo de 7 dias para desistir da compra, sem explicar.

Se o kit não serviu: peça o reembolso pela sua área de compras ou respondendo este e-mail. O valor volta pelo mesmo meio de pagamento. Sem perguntas.

Se travou em alguma etapa: responda este e-mail dizendo onde. A gente ajuda a destravar antes de você decidir.

Se está funcionando: não precisa fazer nada.

Seu Sócio Gestor
```
+ rodapé fixo + descadastro.

---

## 6. D+12 · Avaliação (opt-in)

**Assunto:** Uma pergunta sobre o kit

```
Olá, [Nome].

Duas semanas com o kit. Três perguntas rápidas, sem formulário longo. Responda este e-mail:

1. De 0 a 10, quanto o kit ajudou no seu trabalho?
2. O que funcionou melhor?
3. O que ficou confuso ou faltou?

Se você autorizar, a sua resposta pode aparecer na página do kit com o seu primeiro nome e profissão. Para isso, escreva "pode publicar" na resposta. Se não escrever, fica só entre nós.

Obrigado pelo tempo.
Seu Sócio Gestor
```
+ rodapé fixo + descadastro.

---

## 7. Pix pendente (transacional)

**7a · 15 minutos após gerar o Pix.** Assunto: Seu Pix do Seu Sócio Gestor ainda não foi confirmado
```
Olá, [Nome].

Seu pedido está registrado, mas o Pix ainda não foi pago. Nada foi cobrado e nada foi liberado.

O código vale até [Validade do Pix]. Para pagar: [Link do pedido]
Abra o aplicativo do seu banco, cole o código (ou leia o QR) e confirme. A liberação leva até 2 minutos após o pagamento.

Se o código venceu, gere um novo pela página do kit: https://seusociogestor.com.br/kit/ (Essencial), https://seusociogestor.com.br/completo/ (Completo), https://seusociogestor.com.br/advogados/ (Advogados) ou https://seusociogestor.com.br/medicos/ (Médicos). O pedido antigo não gera cobrança.

Seu Sócio Gestor
```
**7b · 30 minutos antes de expirar.** Assunto: Seu código Pix vence em 30 minutos
```
Olá, [Nome].

O código Pix do seu pedido vence às [Validade do Pix]. Se ainda quiser o kit, pague por aqui: [Link do pedido]

Se preferir, faça um novo pedido depois pela página do kit. Nada foi cobrado.

Seu Sócio Gestor
```
+ rodapé fixo.

---

## 8. Checkout abandonado (só com e-mail informado e opt-in de comunicação)

**8a · 1 hora.** Assunto: Você deixou o kit no carrinho
```
Olá, [Nome].

Você começou a compra do [Kit IA no Trabalho · Essencial | Kit IA no Trabalho · Completo | Kit de Gestão para Advogados | Kit de Gestão para Médicos] e não terminou. O pedido continua aqui: [Link do pedido]

Nada foi cobrado. Pagamento único, Pix ou cartão, 7 dias para desistir.

Seu Sócio Gestor
```
**8b · 24 horas.** Assunto: Alguma dúvida sobre o kit?
```
Olá, [Nome].

Se parou por dúvida, as mais comuns estão respondidas aqui: https://seusociogestor.com.br/suporte/
Precisa de Excel (2016 ou mais novo no Essencial, no Advogados e no Médicos; 2019 ou mais novo no Completo) ou Google Sheets. Funciona com a versão gratuita do ChatGPT. Não é curso, não é software, não tem mensalidade.

Se quiser terminar: [Link do pedido]
Se tiver outra pergunta, responda este e-mail.

Seu Sócio Gestor
```
**8c · 48 horas.** Assunto: Último lembrete, sem pressa
```
Olá, [Nome].

Este é o último e-mail sobre o pedido que ficou aberto. O link continua o mesmo: [Link do pedido]

Se não for o momento, tudo bem. A página do kit fica no ar, sem prazo e sem preço diferente.

Seu Sócio Gestor
```
+ rodapé fixo + descadastro.

---

## 9. Reembolso confirmado (transacional)

**Assunto:** Reembolso do seu pedido [Nº do pedido] confirmado

```
Olá, [Nome].

Seu pedido de reembolso foi aceito. O valor de [Valor] volta pelo mesmo meio de pagamento:
- Pix: em até 2 dias úteis.
- Cartão: o estorno aparece na fatura em até duas faturas, conforme o banco.

O acesso aos arquivos foi encerrado. Se um dia quiser voltar, a página do kit continua no ar.

Se puder responder em uma frase o que não serviu, ajuda a melhorar o kit. Sem obrigação.

Seu Sócio Gestor
```
+ rodapé fixo.

---

## Configuração na Kiwify (checklist para o Eduardo)

- [ ] Produtos Essencial (R$ 37), Completo (R$ 197, até 12× no cartão), Advogados (R$ 497, até 12× no cartão) e Médicos (R$ 697, até 12× no cartão) criados; área de membros com os arquivos do `entrega/` (zip por kit + arquivos soltos).
- [ ] E-mail 1 configurado como e-mail de acesso do produto (substitui o padrão da plataforma).
- [ ] URLs de obrigado por status: aprovado `/obrigado/`, Pix pendente `/obrigado/pix/`, recusado `/obrigado/recusado/`.
- [ ] Opt-in de comunicação no checkout (caixa desmarcada) ligado à sequência 2 a 6 e 8.
- [ ] Pix pendente (7a, 7b) e abandono (8a a 8c) nas automações de recuperação, só por e-mail.
- [ ] Nota fiscal: emissão automática pela plataforma ou pelo contador (confirmar prazo).
- [ ] Teste de ponta a ponta antes de anunciar: cartão aprovado, Pix pago, Pix expirado, cartão recusado, reenvio de acesso, reembolso, nota fiscal. Em 4G, no celular, inclusive no navegador do Instagram.
- [ ] Colocar os links reais em `site/config.json` (`checkout.kit_essencial`, `checkout.kit_completo`, `checkout.kit_advogados`, `checkout.kit_medicos`, `checkout.area_download`) e rebuildar o site.
- [ ] Médicos: order bump com o Essencial a R$ 27 no checkout (oferta), sem upsell no lançamento.
