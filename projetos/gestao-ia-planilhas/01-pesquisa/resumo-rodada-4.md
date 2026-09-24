# Rodada 4: como vender na página. Cruzamento das quatro pesquisas

Data: 2026-09-13. Fontes: Manus (`rodada-4-manus.md`, 534 linhas, 79 referências + 9 dossiês
e 6 auditorias de plataforma no manifesto), ChatGPT A (`rodada-4-gpt-a-como-vender-na-pagina.md`,
698 linhas, 80 fontes datadas), ChatGPT B (`rodada-4-gpt-b-quarta-rodada.md`, 443 linhas) e
Claude (`rodada-4-claude.md` + três relatórios em `rodada-4-claude/`, 33 páginas abertas no
navegador). Este documento é a entrada da etapa 6 (página de vendas). O que está aqui vale mais
que qualquer relatório isolado.

## 1. Leitura de cada relatório

### Manus

Pontos fortes: auditoria HTTP de 28 URLs e cálculos de amostra em JSON reproduzível; separa
"página por estado" (Pix pendente não é compra aprovada; não liberar conteúdo antes do webhook);
tabela de urgência legítima com "evidência a guardar" (regra de sistema, fuso, log de fechamento);
recuperação com grupo de controle (holdout) para medir incremento real; alerta sobre "falso fim de
página" (6 de 8 usuários não rolaram quando o herói parecia página completa); traz o Decreto
7.962/2013 do comércio eletrônico; casos brasileiros com número (Diletto R$ 100 mil pela
história de origem falsa; TJSP 2025 ressarcimento + R$ 5 mil de dano moral por promessa de renda).
Registra conflitos oficiais de taxas em Hotmart, Cakto, Ticto e Eduzz e recomenda capturar o
painel antes de contratar.

Pontos fracos: as páginas brasileiras de referência são fracas para o nosso nicho (curso de efeitos
especiais, curso de carrossel, pack de páginas); a prosa é formal ao ponto de dificultar a leitura;
não abre nenhuma página no navegador nem mede altura, CTAs ou checkout real; blueprint C mistura
"VSL segmentada" sem explicar.

### ChatGPT A ("Como vender na página")

Pontos fortes: o mais completo em checkout: custo por venda em reais por plataforma e ticket
(Kiwify R$ 4,92 em R$ 27; Cakto Pix R$ 2,49; Eduzz R$ 2,49 até R$ 30), registro de que a Kiwify
tem agente gratuito de recuperação por WhatsApp ("Ana", 31/07/2026) e de que taxas da Eduzz não são
devolvidas em reembolso; lista de homologação antes de comprar tráfego (cartão, Pix pago, Pix
expirado, recusa, adicional, acesso, reenvio, reembolso); sequência de pós-compra D+0 a D+7;
alerta de que "sem contato humano para vender" não dispensa atendimento eletrônico eficaz com
resposta em até 5 dias (Decreto 7.962, art. 4º); tabela de amostra por cenário; método
estatístico explícito. Referências úteis: LUZ, Someka, Vertex42, Thomas Frank, PlanilhasBR.

Pontos fracos: cauteloso ao extremo (quase tudo é "ND" ou "hipótese"), o que é honesto mas
transfere a decisão inteira para nós; recomenda Kiwify sem quantificar o custo da escolha;
não analisa páginas brasileiras de infoproduto de verdade (só lojas de planilha e SaaS).

### ChatGPT B ("Quarta rodada")

Pontos fortes: traz a evidência mais importante que faltava aos outros três: **imagem estática
venceu vídeo de 2 minutos em 3,92% num A/B de 2 meses com 30 mil visitantes (Brookdale/VWO)** e
análise da Unbounce de 35 mil páginas em que vídeo teve efeito pequeno ou negativo. Conclusão:
não presumir que vídeo vence; tela real no herói, demo por toque. Também: Unbounce 2024 mostra
que texto difícil, mais tempo de leitura e mais palavras correlacionam com conversão 24%, 19% e
19% menor; caso de continuidade anúncio-página +63% (multicomponente); ideia do parâmetro
`angle` na URL para trocar só eyebrow, headline, poster e primeiro CTA por ângulo de anúncio,
sem cloaking; "placar mínimo" de métricas por produto; ordem prática de implementação
(instrumentação primeiro). Referências verticais boas: Someka Healthcare KPI, Clio,
SimplePractice, Ninsaúde, Simples Dental.

Pontos fracos: mesma cautela do A; sugere bump não marcado como padrão sem discutir o controle
sem bump; refere a Notomantra e Notion Marketplace sem abrir; não compara custo de checkout.

### Claude (referência para comparação)

Único que abriu 33 páginas em modo celular e mediu altura, CTAs, timers, CNPJ e checkouts reais
(Hotmart e Kiwify em modo Brasil); único com custo efetivo por ticket em percentual e com dados
brasileiros de Pix (Gmattos, Appmax, Nuvemshop). Erros que os outros corrigem: apoiei o herói em
vídeo num caso único da Vidyard de 2011; sugeri três planos como âncora sem exigir diferença
real; propus 15 dias de garantia como diferencial sem lembrar que 7 dias é direito legal, não
bônus; não citei o Decreto 7.962/2013; recomendei Cakto pelo custo sem pesar maturidade e
conflitos de documentação.

## 2. Onde os quatro concordam (entra no blueprint sem discussão)

1. Primeira tela decide: 57% da atenção acima da dobra (NN/g). Herói = o que é, para quem, que
   tarefa resolve, tela real, preço e um CTA. Sinal de continuidade para não parecer fim de página.
2. Não existe tamanho de página comprovado por faixa de preço. Regra: uma seção fica se responde
   "o que é / serve para mim / como funciona / o que recebo / é compatível / por que acreditar /
   quanto custa / como recebo / como desisto". Profundidade cresce com o preço, não adjetivos.
3. Preço total à vista sempre visível; parcelas só com total e juros (Decreto 5.903, art. 9º IV;
   CDC 52 e 54-B). Nada de "de/por" sem preço anterior praticado. Comparação com software mensal
   só recurso a recurso, com preço datado e fonte.
4. Urgência apenas real: preço de lançamento com data, hora e fuso, que muda de verdade no
   servidor; ou nenhuma. Sem contador reiniciável, sem "últimas vagas" em arquivo ilimitado.
5. Prova social no lançamento = prova do produto: tela real, demonstração, inventário auditável,
   amostra, empresa identificada (CNPJ, razão social, endereço, e-mail), fontes junto do dado.
   Avaliações só reais, com consentimento separado da compra (LGPD art. 8º), revogável, com
   disclosure de beta ou desconto. Cinco avaliações já bastam para o efeito principal (Spiegel).
6. Sete dias é direito de arrependimento (CDC art. 49), não bônus: chamar pelo nome, explicar
   como pedir, sem condicionar a nada.
7. Banner de cookies com "rejeitar não necessários" tão visível quanto "aceitar" (ANPD). Pixel só
   após aceite; CAPI respeita o mesmo estado e não é atalho; deduplicar por event_id; nunca
   enviar CPF, texto de formulário ou dado de paciente/cliente a evento de anúncio.
8. Mobile: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1; corpo 16 a 18 px; uma coluna; contraste 4,5:1;
   alvos de 44 a 48 px; vídeo com poster, play explícito, mudo por padrão, legenda revisada.
9. Checkout: só campos necessários; cupom recolhido; sem timer decorativo; resumo com total antes
   de pagar; adicional nunca pré-marcado; recusa do upsell leva ao acesso já comprado; conteúdo
   liberado só após aprovação (Pix pendente não é compra).
10. Não existe benchmark brasileiro de compra por faixa de preço, aceite de bump, reembolso ou
    recuperação. Todos são "ND". A base própria substitui o benchmark. Testes de compra exigem
    10 a 20 mil visitas por variante; começar por métricas de funil e correção de erros óbvios.
11. Rodapé obrigatório (Decreto 7.962/2013): nome empresarial, CNPJ, endereço físico e
    eletrônico, atendimento eletrônico com resposta em até 5 dias, termos, privacidade, meio de
    arrependimento pela mesma ferramenta da compra.

## 3. Onde divergem e a decisão

| Tema | Claude | Manus | GPT A | GPT B | Decisão |
|---|---|---|---|---|---|
| Plataforma de checkout | Cakto (custo), Ticto alternativa | Qualquer completa; conflitos oficiais em Cakto/Ticto/Eduzz | Kiwify (operação única, agente de recuperação grátis); Hotmart alternativa | Kiwify; piloto Eduzz se ≤ R$ 30 | **Kiwify no lançamento.** Mudo minha recomendação: maturidade, documentação, área de membros, Pixel/CAPI e recuperação por WhatsApp nativos pesam mais que R$ 2,43 a menos por venda de R$ 27. Reavaliar com dados após 90 dias; Cakto/Eduzz como piloto de margem depois |
| Herói: vídeo ou tela | Vídeo curto autoplay mudo | Poster leve + vídeo por toque | Tela real primeiro; demo opcional | Tela real venceu vídeo (Brookdale) | **Tela real legível no herói; vídeo por toque logo abaixo.** Nada de autoplay. Testar vídeo x imagem como teste 2 |
| Duração do vídeo | 15–30 s / 60–90 s / 60–90 s por núcleo | 35–55 s e 3–6 min como faixas de teste | 20–45 s / 60–120 s / 2–4 min | 45–75 s / 90–180 s / tour 4–6 min | 45–60 s (entrada), 90–120 s (intermediário), tour 2–4 min com capítulos + microdemos por núcleo (vertical) |
| Planos (bom/melhor/ótimo) | 3 opções como âncora | Só planos materialmente distintos; ≤ 2 no mobile | Comparar só formatos reais | Um plano no lançamento | **Um plano por produto no lançamento.** Tiers só quando houver diferença real (licença multiusuário, suporte) |
| Order bump | 1 bump, 10–25% do preço | Controle sem bump; variante com 1 | Sem bump no R$ 27 para medir a compra principal | 1 bump desmarcado | **1 bump desmarcado desde o início** (padrão do mercado, baixo risco), medir compra principal e aceite; sem volume para A/B de bump |
| Garantia | 7 dias; testar 15 como diferencial | 7 dias é o mínimo legal, não privilégio | Idem | Idem | Bloco "Direito de arrependimento de 7 dias". Testar 15 dias só depois de baseline |
| Telefone no checkout | Manter (recuperação por WhatsApp) | Só com finalidade documentada | Opcional quando possível | Opcional + consentimento para WhatsApp | Manter o padrão da Kiwify (CPF e telefone) com uma linha explicando a finalidade; mensagem de recuperação só transacional; marketing só com opt-in |
| Comparação com SaaS mensal | Gancho principal ("menos que 4 meses de Clinicorp") | Comparar só funções equivalentes | Idem, datado | Idem, recurso a recurso | Manter a âncora, com escopo explícito: "o kit não substitui agenda online, prontuário ou emissão de nota", preço do software com data e fonte |
| Nome "na metade do tempo" | Não questionei | Alegação sem ensaio: evitar quantificar | Ônus da prova é do anunciante (CDC 38); usar headline de utilidade | Idem | **Decisão do Eduardo.** Recomendo: tirar "na metade do tempo" do nome e da headline; usar "planilhas, relatórios e apresentações com modelos prontos e IA". "Economia de tempo" fica como proposta de valor, sem percentual |
| Advertorial | Testar depois para R$ 697 | Direta como controle; pré-venda só com educação necessária e identificada | Idem | Idem, e nunca imitar notícia | Página direta nos três produtos. Pré-venda identificada como publicidade só como teste posterior no vertical |

## 4. Blueprint final (o que vamos construir)

### Comum a todas as páginas

- HTML estático próprio, uma coluna, marca Seu Sócio Gestor (tokens.css), fundo claro, uma cor
  de ação (sol sobre uva), telas reais ampliáveis com dados fictícios rotulados.
- Herói: eyebrow (categoria), headline de tarefa + artefato, subheadline com formato, acesso e
  limite, tela real, preço à vista + parcelas com total, CTA único ("Comprar acesso" ou "Ver o que
  vem no kit"), início do próximo bloco visível.
- Linha de transparência logo após o herói (regra de 2026-09-12): kit de planilhas + manual +
  demonstrações + prompts; não é software; sem mensalidade; sem atendimento por telefone.
- Bloco de preço: nome da oferta, "pagamento único", preço à vista, Pix, parcelas com total e
  juros, entrega ("acesso imediato após aprovação"), direito de arrependimento de 7 dias, CTA,
  CNPJ e processador identificados ao lado.
- FAQ com as perguntas obrigatórias: o que recebo; funciona em que programa; preciso pagar outra
  ferramenta; uso no celular; como recebo e recupero o acesso; por quanto tempo; licença; o que
  não está incluído; suporte e prazo de resposta; como pedir reembolso; nota fiscal; dados pessoais.
- Rodapé: razão social, CNPJ, endereço, e-mail de atendimento (resposta em até 5 dias), termos,
  privacidade, cookies (link permanente), reembolso.
- CTA fixo no mobile após a primeira rolagem, com preço, sem cobrir banner de cookies. Testar.
- Parâmetro `angle` na URL: troca só eyebrow, headline, poster e primeiro CTA por ângulo de
  anúncio; oferta, preço e garantia nunca mudam por parâmetro.
- Sem: contador, "últimas vagas", data automática, preço riscado, estrelas decorativas, número de
  clientes, foto de banco, caixa alta com medo, capa 3D de robô, bônus "de R$ 97 por R$ 0",
  vídeo do YouTube como herói, pop-up de saída, três bumps.

### Kit IA no Trabalho (R$ 27 a 47)

1. Herói (tela real da planilha; preço; CTA).
2. O que vem: nome real dos 3 arquivos e das categorias de prompts, com print de cada um.
3. Como funciona: 3 microloops mudos de 6 a 12 s (preencher, copiar prompt, ver saída) + vídeo
   de 45 a 60 s por toque.
4. Três usos: cartões entrada → ação → saída, com uma limitação por cartão.
5. Recebimento e compatibilidade: Excel, Google Sheets, versão, celular, licença, atualização.
6. Preço e direito de arrependimento em um card.
7. FAQ curto (6 a 8). 8. Rodapé legal.
Extensão: 6 a 8 blocos, 500 a 900 palavras, 5 a 8 mil px no celular. Um plano. Sem urgência no
controle. Checkout Kiwify com Pix e cartão expostos, 1 bump desmarcado.

### IA no Trabalho (R$ 197 a 297)

1. Herói por tarefa (sem "metade do tempo"). 2. Situação atual em três cenários operacionais.
3. Demonstração de 90 a 120 s por toque (arquivo vazio → dado → prompt → relatório → revisão).
4. Método em 4 passos. 5. Inventário das 10 planilhas em tabela (nome, uso, entrada, saída,
formato) com prints. 6. Prompts e aulas: um prompt anotado, grade das aulas com duração real.
7. Para quem é / não é. 8. Prova sem clientes: empresa, processo de QA, dados fictícios, betas
identificados quando houver. 9. Preço em card único. 10. FAQ completo. 11. Rodapé.
Extensão: 10 a 14 blocos, 900 a 1.500 palavras, 10 a 14 mil px. Preço de lançamento com data
real, se adotado. Upsell em um clique após a compra: kit vertical ou Pro, com recusa clara.

### Verticais (R$ 497 a 697)

1. Herói vertical: profissão, 20 planilhas em 5 núcleos, tela do núcleo mais reconhecível,
"compra única", CTAs "Explorar os cinco núcleos" e "Ver preço".
2. Linha de transparência (não é prontuário, não é software, não é consultoria).
3. Mapa dos 5 núcleos com abas/âncoras: tarefa, arquivos e print de cada um.
4. Tour do núcleo 1 em 60 a 90 s; os outros em acordeão com microdemos.
5. Três rotinas profissionais com dados fictícios (falas da rodada 3 como abertura).
6. Antes/depois de organização, rotulado como demonstração de layout.
7. Compatibilidade, privacidade e limites (LGPD; não inserir dados sensíveis em IA pública).
8. Implantação: checklist de 30 a 60 min (validar o tempo internamente antes de publicar).
9. Para quem é / não é. 10. Prova e empresa (Z2 Data Services, CNPJ, QA, fontes CFO/OAB).
11. Comparação com software mensal recurso a recurso, datada. 12. Amostra grátis de uma
planilha em troca de e-mail (gera lead; automação de e-mail converte muito mais que campanha).
13. Oferta e preço. 14. FAQ técnico e legal (10 a 14). 15. Rodapé.
Extensão: 14 a 18 blocos, 1.400 a 2.200 palavras, 12 a 16 mil px, com sumário de âncoras.

### Checkout e pós-compra (Kiwify)

- Campos: nome, e-mail, CPF, telefone (com finalidade explicada), pagamento. Pix e cartão
  expostos; Pix pré-selecionado abaixo de R$ 100; 12x pré-selecionado acima. Cupom recolhido.
  Sem timer. 1 bump desmarcado a 10 a 25% do preço, texto de duas frases.
- Página de obrigado por estado: aprovado (botão "Acessar meu material", e-mail usado, suporte,
  arrependimento); Pix pendente (QR, copia e cola, validade real, "ainda não confirmado");
  recusado (alternativa sem reiniciar). Evento Purchase só no webhook de aprovação.
- Sequência D+0 acesso; D+1 primeira tarefa; D+3 "conseguiu abrir?"; D+5 segunda aplicação;
  D+6 lembrete neutro do direito de arrependimento; D+10 a 14 pedido de avaliação com
  consentimento separado. Reembolso aprovado sem atrito.
- Recuperação: agente da Kiwify (transacional) + e-mail em 1 h, 24 h, 48 h; Pix não pago em
  15 a 30 min e antes da expiração; holdout de 10% para medir incremento real.
- Homologação antes de comprar tráfego: cartão, Pix pago, Pix expirado, recusa, compra com bump,
  acesso, reenvio de acesso, reembolso, nota fiscal, evento deduplicado, tudo em 4G e aparelho
  real, inclusive no navegador do Instagram.

### Medição e testes

- Contrato de eventos: landing_view → cta_click → price_view → checkout_view →
  payment_started → approved (1 h / 24 h) → refunded (7 / 30 d) → chargeback (60 d) →
  acesso D+1 → primeira planilha aberta. Consentimento e diferença pedido↔evento de anúncio.
- Ordem de testes: (1) herói genérico x tarefa do anúncio; (2) tela x vídeo por toque; (3) bloco
  de preço agrupado; (4) campos do checkout; (5) CTA fixo; (6) requisitos junto da oferta.
  Amostra: ~10 a 20 mil visitas por variante para compra; 7 mil para início de checkout; 6 mil
  para clique. Um teste por página, dois ciclos semanais, regra de parada definida antes.
- Conversão mínima de equilíbrio = custo por visitante ÷ contribuição líquida por compra.
  Exemplo: visitante a R$ 1,00 e contribuição de R$ 20 (kit) → 5%; R$ 100 → 1%; R$ 250 → 0,4%.

## 5. Decisões pendentes do Eduardo

1. **Checkout no lançamento: Kiwify** (recomendação unânime após o cruzamento). Confirmar.
2. **Nome do produto 2 sem "na metade do tempo".** Sugestão: "IA no Trabalho: planilhas,
   relatórios e apresentações com modelos prontos". Confirmar ou pedir alternativas.
3. **Atendimento eletrônico:** a lei exige resposta em até 5 dias. Proposta: FAQ + e-mail
   automático que resolve acesso e reembolso; exceções chegam a uma caixa que o Eduardo (ou eu,
   pelo repositório) revisa uma vez por semana. Confirmar quem olha a caixa.
4. **Urgência:** preço de lançamento com data real ou nenhuma. Sugestão: nenhuma no Kit;
   preço de lançamento com data registrada em DECISOES.md nos produtos de R$ 197+.

## 6. Ordem de implementação (etapas 6 a 8 do pipeline)

1. Instrumentação e contrato de eventos (Pixel + CAPI com consentimento, UTMs, `angle`).
2. Base do site: home, termos, privacidade, cookies, suporte, rodapé legal.
3. Biblioteca visual reutilizável: poster, captura, microdemo, inventário e compatibilidade por
   arquivo, otimizados para LCP.
4. Página do Kit IA no Trabalho + checkout Kiwify + página de obrigado por estado + sequência
   D+0 a D+14.
5. Homologação de ponta a ponta em aparelho real. Só então tráfego.
