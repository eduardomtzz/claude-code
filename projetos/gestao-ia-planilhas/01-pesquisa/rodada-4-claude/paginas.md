# R4 — Análise de páginas de venda reais (planilhas, templates, cursos de IA/Excel, kits de gestão)

Data: 2026-09-13. Método: busca de URLs via WebSearch, abertura em Chromium headless (Playwright) com viewport
390×844 (iPhone), UA mobile, locale pt-BR, scroll completo para lazy-load, extração de h1/h2/h3, CTAs, preços,
sinais (timer, garantia, FAQ, CNPJ/termos), links de checkout e screenshot de página inteira.
Screenshots em `r4-shots/<nome>.png`, dados brutos em `r4-shots/<nome>.json`, recorte do herói em `r4-shots/hero/<nome>.png`.

Observações de método (importantes para ler a tabela):
- O egresso do proxy é nos EUA. Hotmart e Kiwify geolocalizam o checkout e as páginas de marketplace: preços saíram
  em USD (`$12.00`, `$20.00`) e o checkout abriu em inglês. Para os checkouts, rodei um script que clica em
  "Alterar país → Brasil"; para as páginas de marketplace da Hotmart, os preços em BRL não foram capturados.
- "Altura" é `scrollHeight` em px na largura 390. Páginas acima de 30.000 px teriam screenshot só do viewport (nenhuma passou).
- "CTAs" = quantidade de botões/links com verbo de compra (comprar, quero, garantir, acessar, adquirir, buy, get...).
- Falhas registradas: Etsy (403 anti-bot, 2 listagens), planilhasprofissionais.com e construindosonhos.adm.br (túnel do
  proxy recusado), lp.gruponinja.com.br (HTTP/2 + TLS incompatível), gumroad.com/a/... (afiliado, túnel recusado),
  pay.kiwify.com.br/DAXRCCx (produto indisponível). **planilhas.vc** hoje redireciona para um site de cassino vietnamita
  (domínio expirado/sequestrado) — não usar como referência.
- Páginas abertas que se revelaram artigos de blog/SEO, não páginas de venda (descartadas da análise): dasckup.com
  (curso de ChatGPT), hashtagtreinamentos.com (curso básico de ChatGPT), estagiotrainee.com/excel (comparativo).

**Total analisado com sucesso: 19 páginas brasileiras + 3 checkouts (1 Hotmart BR, 2 Kiwify) + 11 internacionais = 33.**

---

## 1. Tabela — páginas brasileiras

| # | URL | Produto | Preço visível | Faixa | Herói | CTAs | Altura (px) | Timer | Garantia | FAQ | CNPJ/Termos | Checkout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B1 | tomazzonitreinamentos.com.br/ticius-pro/ | Tícius — planilha de gestão p/ advogados ("sem mensalidade") | De R$397/597 por 12x R$20,67 ou **R$197** à vista (2 opções: suporte e-mail / WhatsApp) | 197–297 | Vídeo YouTube embutido sobre fundo preto | 6 | 13.022 | não | 7 dias | sim | CNPJ sim / termos sim | Hubla (pay.hub.la) |
| B2 | planilhasessenciais.com.br/planilha-essencial-do-advogado/ | Planilha Essencial do Advogado 2.0 PRO | De R$227 por 10x R$15,26 ou **R$127** à vista | 97–197 | Mockup notebook + thumb de vídeo "clique e assista" + estrelas | 5 | 15.505 | não | 7 dias incondicional | sim (objeções em formato FAQ) | CNPJ sim / termos sim | Hotmart (2 ofertas) |
| B3 | notioncel.com.br/legal-hub-notion-para-advogados/ | Legal Hub — template Notion p/ advogados | De R$297 por 12x R$19,78 ou **R$197** à vista; bônus "CRMaster de R$97 por R$0" | 197–297 | Logo + headline + mockup 3D "papel desenrolando" (sem vídeo) | 7 | 12.297 | não ("oferta por tempo limitado" só no texto) | 7 dias | sim | CNPJ não / termos não | Kiwify |
| B4 | samurailab.com.br/prompts-de-ia-para-advogados/ | Prompts de IA para Advogados — guia PDF | De R$197 (âncora R$297) por **R$17** | 17–47 | Capa 3D do e-book (robô vermelho) sobre fundo preto | 4 (mesmo botão repetido) | 7.252 | não ("Última chamada!" no h2) | 7 dias incondicional | sim | CNPJ não / termos não | Kiwify (link hoje "produto indisponível") |
| B5 | loja.guiadoexcel.com.br/produto/planilha-de-gestao-financeira-empresarial-excel/ | Planilha de Gestão Financeira Empresarial | De R$129 por **R$89** ou 10x R$8,90 | 47–97 | Ficha de produto e-commerce: título, estrelas 4,5 (730 avaliações), 1.930 clientes, preço, screenshot do dashboard | 11 (inclui menu) | 22.806 | não ("oferta por tempo limitado" no selo) | sim | sim | CNPJ não / termos sim | Loja própria (WooCommerce): Pix, Visa, Elo, Boleto, PayPal |
| B6 | henriquestuart.com.br/pfo1/ | Painel Financeiro Otimizado (template Notion finanças pessoais) | De R$297 por **12x R$14,76/ano** (assinatura anual) | 97–197 | Headline + mockup flutuante + vídeo lateral | 5 (todos "QUERO...") | 12.648 | não | 7 dias incondicional | sim | CNPJ não / termos não (tem aviso legal Kiwify) | Kiwify |
| B7 | smartplanilhas.com.br/produto/planilha-odontologico-dentista/ | Planilha p/ consultório odontológico | **R$249** (licença usuário único / múltiplos) | 197–297 | Ficha de produto + vídeo YouTube demonstrativo | 0 (botão "Adicionar ao carrinho" não pegou no regex) | 6.818 | não | 7 dias | não | CNPJ sim / termos não | Carrinho próprio, parcela 10x |
| B8 | planilhasprontas.com.br/baixar/planilha-clinicas-consultorios-excel/ | Planilha p/ clínicas e consultórios | De R$159 por **R$79,50** | 47–97 | Galeria de screenshots + "Ver vídeo" | 4 | 8.724 | não | 7 dias | sim | CNPJ sim / termos não | Carrinho próprio, 12x |
| B9 | excelcoaching.com.br/produto/planilha-para-advogados-... | Planilha p/ advogados (processos + financeiro) | **R$99** | 97 | Ficha WooCommerce padrão + 3 vídeos | 1 | 8.482 | não | não | sim | CNPJ sim / termos sim | Carrinho WooCommerce |
| B10 | eplanilhas.com.br | Pacote 4.000 planilhas prontas | De R$299,80 por **R$149,90** ou 12x R$15,19; "50% off válido hoje: domingo, 13/09/2026" | 97–197 | Headline + grid de ícones/categorias | 7 | 12.354 | não (data dinâmica = escassez falsa) | não | sim | CNPJ sim / termos não | Checkout próprio |
| B11 | souza.xyz/produto/kit-planilhas-gestao-empresarial/ | Kit 5 planilhas gestão (PDCA, GUT, 5W2H, projetos) + cursos | De R$406,96 por **R$199,15** | 197–297 | Ficha WooCommerce, texto longo "SEO" | 2 | 13.416 | não | não | não | CNPJ não / termos sim | WooCommerce |
| B12 | lojadasplanilhas.com.br | Loja Shopify de planilhas (home) | R$29,90–59,90 por planilha, pacotes | 27–97 | Slideshow "mais de 90 modelos" | 8 | 7.439 | não | não | sim | CNPJ sim / termos sim | Shopify (cupom 10% no topo) |
| B13 | luz.vc/produtos/planilha-de-gestao-financeira-completa-em-excel-4-0 | LUZ Prime — planilha de gestão financeira 6.0 (dentro de assinatura) | sem preço na página ("precisa ter um plano ativo") | assinatura | Texto + screenshots de abas; vídeo tutorial mais abaixo | 4 | 14.628 | não | não | sim | CNPJ sim / termos não | Assinatura LUZ Prime |
| B14 | experttcursos.com.br/excel | Curso de Excel (básico ao avançado, certificado) | De R$297 por 12x R$10,03 ou **R$97** à vista | 97 | Ícone Excel + headline + vídeo YouTube | 2 | 23.995 | não | sim (7 dias) | sim (accordion, triplicado no DOM) | CNPJ sim / termos sim | não identificado (botão âncora) |
| B15 | mestreacademy.com/curso/curso-chatgpt | Curso ChatGPT + 1 ano Mestre Academy Pro | **R$397** ou 12x R$39,62 (âncora "R$3.000" de valor) | 297–497 | Headline + vídeo + dado de mercado (RD Station) | 2 | 11.440 | não | 7 dias | não | CNPJ não / termos sim | plataforma própria |
| B16 | hotmart.com/.../planilhas-profissionais-excel/W34213923F | 15 planilhas de gestão (marketplace Hotmart) | $12 (USD geolocalizado) | ~27–67 | Layout padrão marketplace | 3 | 2.653 | não | não | sim (padrão Hotmart) | termos Hotmart | Hotmart |
| B17 | hotmart.com/.../chat-gpt-para-advogados-30-comandos-.../W95605448G | ChatGPT p/ Advogados — 30 comandos (6 aulas) | **Produto indisponível** (form "tenho interesse") | — | Marketplace | 5 | 3.574 | não | sim | sim | termos Hotmart | Hotmart |
| B18 | hotmart.com/.../200-prompts-de-comandos-para-advogados-.../F84291491X | 200 prompts p/ advogados (e-book) | $2 (USD) | ~9–27 | Marketplace | 3 | 3.454 | não | sim | sim | termos Hotmart | Hotmart — **nota 1,9/5 (12 avaliações)** |
| B19 | hotmart.com/.../curso-de-power-bi-s8gjp/K66093186H | Curso de Power BI — Expert Cursos | $20 (USD) | ~97 | Marketplace | 4 | 5.000 | não | não | sim | termos Hotmart | Hotmart — 4,8 (11 aval.), "85.000 alunos" |

### Checkouts abertos (modo Brasil)

| Checkout | URL | O que aparece, em ordem | Pix | Order bump | Timer |
|---|---|---|---|---|---|
| Hotmart | pay.hotmart.com/L82564123A?off=6ynt71cj (Planilha Essencial do Advogado) | Selo do país; thumb + nome + autor + "10x de R$15,26 / R$127 à vista"; **Dados pessoais**: e-mail, confirmar e-mail, nome completo, **CPF/CNPJ**, celular (+55), **CEP**; cupom; **Forma de pagamento**: cartão (select de parcelas 1–10x "com acréscimo"), **Pix**, PayPal, Cartão Virtual Caixa; **"Buy together"** (order bump: Planilha Essencial Financeira 3.0, com desconto 39%); resumo; botão "Comprar agora"; texto legal Hotmart | sim | 1 bump com % de desconto | banner "Complete o formulário no prazo" com contador de 15–17 min quando geolocalizado nos EUA; no modo BR não apareceu |
| Kiwify | pay.kiwify.com.br/kCvCLiU (Legal Hub) | Faixa laranja "Oferta por tempo limitado" com contador (14:53 no modo EUA); logo + mockup + nome; nome, e-mail, confirmar e-mail, **CPF/CNPJ**, telefone; "Lembrar-me nesse dispositivo"; cartão (número, mês, ano, CVC, parcelas, salvar cartão); **3 order bumps** em sequência ("SIM, EU ACEITO ESSA OFERTA ESPECIAL!": pack de 30 planilhas R$47, curso Notion, template Rotina Otimizada 70% off); resumo; botão "Pagar" com texto legal Kiwify; "Denunciar este produto". No modo BR aparece antes um **modal de oferta** ("Sim, eu quero meu template e os bônus" / "Continuar") | abas Pix/boleto não capturadas no render (esqueleto de carregamento); padrão Kiwify tem cartão/Pix/boleto | 3 bumps empilhados | sim, contador regressivo no topo |
| Kiwify | pay.kiwify.com.br/Hzuixxp (PFO) | Mesmo padrão; modal "Oferta por tempo limitado" bloqueia a página até clicar "Continuar" | idem | — | sim |

---

## 2. Tabela — páginas internacionais

| # | URL | Produto | Preço | Herói | CTAs | Altura | Timer | Garantia | FAQ | Termos | Checkout | Prova social |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | thomasjfrank.com/brain/ | Ultimate Brain (Notion, 2ª cérebro) | $129 (Plus $228 / Pro $278; cupom $50 off no topo) | Barra de cupom + headline "Your Second Brain, ENTIRELY in Notion" + botão + avatares "+40.000" + vídeo YouTube | 11 | 24.291 | não | sim (FAQ "Can I get a refund?") | sim | sim | Lemon Squeezy (shop.thomasjfrank.com) | "40.000+ people use", citação de Tiago Forte, depoimentos de criadores com nº de inscritos |
| I2 | notion.com/templates/ultimate-brain | Ultimate Brain (marketplace Notion) | $129 (código SPRING50) | Layout marketplace: galeria + "Purchase template for $129" fixo | 7 | 6.623 | não | não | não | sim | Notion | 4,9 (54 ratings) com reviews datadas |
| I3 | easlo.gumroad.com/l/brain | Second Brain (Notion) | $79 | Layout Gumroad: capa + preço + "I want this!" | 0 (botão nativo) | 3.157 | não | não | não | Gumroad | Gumroad | **7.070 vendas**, 4,9 (269 ratings), selo "Top creator" |
| I4 | easlo.gumroad.com/l/freelanceos | Freelance OS (Notion) | $79 individual / $199 teams ("0 left") | Gumroad | 0 | 2.239 | não | não | não | Gumroad | Gumroad | 858 vendas, 4,9 (48 ratings) |
| I5 | imaginationlabs.gumroad.com/l/business | Business OS (Notion) | $0 free / **$85** (âncora "$300 de valor"; tiers $49/$29/$19 por módulo) | Gumroad + copy longa com valor empilhado | 2 | 2.832 | não | **30 dias reembolso** | sim (Q+A) | Gumroad | Gumroad | 86 ratings 4,8; "+100 businesses" |
| I6 | godofprompt.ai/complete-ai-bundle | Complete AI Bundle (prompts + GPTs + automações) | $400 → **$199** lifetime ("save 50%, limited time"; âncora "$10.000") | Headline + ilustração 3D de caixa + 6 cards do que contém + botão amarelo + link Trustpilot | 4 (mesmo "Get Lifetime Access") | 12.228 | não | sim | sim | sim | próprio (Stripe-like) | "5.000+ business owners", reviews Trustpilot com nome |
| I7 | promptshq.co | Packs de prompts p/ advogados, analistas, compliance | $0 starter / **$49 Legal / $97 Finance / $249 Pro bundle** (âncora $1 no "from") | Headline serifada "Stop writing prompts. Start getting results." + 2 botões (free pack / see all) + grid de 4 números | 6 | 9.295 | não | não | sim | sim | Gumroad (4 links) | zero números reais (85% "time saved" sem fonte); depoimento único |
| I8 | vertex42.com/ExcelTemplates/money-management-template.html | Money Management Template (Excel/Sheets) | grátis (modelo de negócio: ads + versões pro) | Título + screenshot + botão DOWNLOAD por versão | 28 (menu + downloads) | 12.281 | não | "garantia" só em texto | não | sim | — | "Over 750.000 downloads" / "250.000 downloads" |
| I9 | someka.net/products/finance-kpi-dashboard-excel-template/ | Finance KPI Dashboard (Excel) | **$39,95** single / $79,95 multi; suporte +$19,95; customização +$250; membership $99/mês (400+ templates) | Ficha e-commerce: nota 4,56 (9 reviews), "Download Free Demo" + seletor de licença + "Add to cart" | 11 | 13.915 | não | não | sim (aba) | sim | WooCommerce | 9 reviews; demo grátis funciona como prova |
| I10 | spreadsheet123.com/ExcelTemplates/excel-purchase-order.html (via WebFetch) | Purchase Order template | grátis | Screenshot grande do template + 2 versões | download | — | não | não | não | sim | — | nenhuma |
| I11 | learn.justinwelsh.me/the-content-operating-system-kajabi-template | The Content OS (curso/sistema) | "Product no longer available" (histórico $150) | Headline + subtítulo + vídeo; depoimentos de nomes conhecidos logo abaixo | 0 | 11.122 | não | sim | sim (8 perguntas, incl. "quem NÃO deve comprar") | não | Kajabi | Depoimentos nomeados (Dan Koe, Dickie Bush, Nicolas Cole) |
| — | etsy.com/listing/1303887481 (Annual Budget Spreadsheet) | não abriu (403) | ~US$ 5–15 (snippet) | — | — | — | — | — | — | — | Etsy | snippet de busca: 4,8★ com 5,9 mil avaliações — não verificado |

---

## 3. Ordem das seções (a partir dos h2 e do texto)

**B1 Tícius (197):** headline "Organize seu escritório" → vídeo → bullets (sem mensalidade, offline, vitalício) → "Os 12.410 advogados que usam, recomendam" (prints de depoimentos) → "Para quem é" (4 perfis) → funcionalidades (10 cards) → "feito por advogados para advogados" → 2 opções de preço (suporte e-mail vs WhatsApp, mesma parcela) → garantia 7 dias → FAQ → rodapé com CNPJ.

**B2 Planilha Essencial do Advogado (127):** barra fixa "SUPER OFERTA 2026 + Acesso Vitalício / QUERO ADQUIRIR" → headline "organização de um software jurídico sem mensalidades eternas" → box de vídeo com mockup + "junte-se a mais de 5000 advogados" → CTA → "compra 100% segura, 7 dias" → 3 cards (pagamento único, acesso imediato, treinamento) → dor (❌ perde prazo? post-its?) → "você não precisa de um sistema de R$200/mês" → depoimentos → **objeções em formato de perguntas** ("não tenho tempo pra aprender", "parece caro por uma planilha") → funcionalidades (7 + 4 PRO) → preço de/por → "você não tem nada a perder" → ATENÇÃO (escassez) → FAQ → WhatsApp.

**B3 Legal Hub (197):** logo → headline → CTA → mockup → "o que você vai conseguir" (5 itens) → "me fala tudo sobre o template" → "e mais" → "veja com seus próprios olhos" (prints) → dado "1.450.000 advogados regulados" → bônus (com bônus "de R$97 por R$0") → "Aprovado e testado" (depoimentos) → investimento de/por → garantia/segurança/Kiwify → sobre a Notioncel ("1000 clientes") → FAQ → "antes que você ache bobagem, lembre-se de 2 coisas".

**B4 Samurai Lab (17):** headline em caixa alta de dor+medo → subtítulo → capa 3D → CTA → carta "Caro(a) colega advogado(a)" → dor → "Apresentando" → contraste "continuar sobrecarregado... OU desbloquear" → "O que você vai descobrir (entregáveis claros)" → "para você se..." → quem é o autor (90 escritórios) → preço de R$197 por R$17 → garantia → "Última chamada!" → FAQ → rodapé sem CNPJ.

**B5 Guia do Excel (89):** ficha com estrelas/clientes/preço/parcelas → "mais vendido" no screenshot → formas de pagamento (ícones) → 4 selos (download imediato, atualizações, sem mensalidade, suporte WhatsApp) → "Sobre o produto" → "Tudo que você precisa em um só lugar" (abas) → "Veja em ação" (imagens) → texto SEO longo ("como utilizar em 2027", rotina recomendada) → "O que nossos clientes dizem" → FAQ → "Você também pode gostar".

**B6 PFO (12x 14,76/ano):** headline → CTA → 3 selos → "dê o primeiro passo" + vídeo → bullets do que faz → CTA → "é impossível prosperar sem gestão" → "resultados dos alunos" (prints) → "para quem é" → "o que você vai ter acesso" (13 itens) → bônus (4) → preço (de R$297) → garantia 7 dias → "Quem é Henrique Stuart" → FAQ → aviso legal Kiwify.

**B14 Expert Cursos Excel (97):** logo → ícone do Excel → headline com "acesso vitalício e certificado" → vídeo → 4 selos (30h, certificado, básico ao avançado, suporte) → "Ganhe destaque no mercado" → módulos → certificado (imagem) → depoimentos em vídeo (5 vídeos) → preço de/por 12x → 4 selos → FAQ → rodapé com CNPJ. Página muito longa (24k px) por repetir blocos no DOM.

**I1 Thomas Frank (129):** cupom → header com "Buy" fixo → headline → "New: 3.0" → CTA + avatares 40k → vídeo → 8 blocos de benefício com emoji e GIF cada → "Start simple, move faster" → "World-class tutorials and support" → **tabela de preço com 3 tiers** → "What people are saying" → FAQ (updates, support, refund).

**I6 God of Prompt (199):** headline → ilustração → 6 cards do conteúdo → CTA + Trustpilot → "5.000+ business owners turned prompts into profits" (reviews com nome) → "Automate repetitive tasks" → "One bundle. Locked in for life" → lista de todos os produtos com nomes (15+) → "Ready to act in AI?" → "Will you be the next success story?" → newsletter → FAQ → "Everything you need. One payment." → preço $400→$199.

**I7 PromptsHQ (49–249):** headline → 2 CTAs (free first) → "works with ChatGPT · Claude · Gemini..." → grid de 4 números → "The problem" (3 parágrafos numerados) → "Four packs. One clear upgrade path" (tabela de preços) → "Used by professionals who bill by the hour" → "From purchase to productive in under 10 minutes" (3 passos) → FAQ → CTA final.

**Gumroad (I3–I5):** capa → preço → "I want this!" → descrição curta → "What's included?" (lista) → tiers → contadores nativos (vendas, ratings, distribuição de estrelas) → reviews. A plataforma faz a prova social; o vendedor só escreve 200 palavras.

---

## 4. Prova social — tipo e quantidade

| Página | Tipo | Quantidade / verificabilidade |
|---|---|---|
| Tícius | Número na headline + prints de WhatsApp/Instagram | "12.410 advogados" (não verificável) |
| Planilha Essencial Adv. | Número no box do vídeo + prints | "mais de 5000 advogados"; estrelas decorativas |
| Legal Hub | Depoimentos + número institucional | "1000 clientes ativos"; dado de mercado (1,45 mi advogados OAB) usado como contexto |
| Samurai Lab | Autoridade do autor | "ajudamos mais de 90 escritórios"; nenhum depoimento |
| Guia do Excel | **Avaliações nativas da loja** | 4,5★ em 730 avaliações + 1.930 clientes (mais crível do conjunto BR) |
| PFO | Prints de "resultados dos alunos" | quantidade não visível (carrossel) |
| Smart Planilhas | Selo "200 pessoas baixaram nos últimos dias" | avaliações do produto = 0 |
| Planilhas Prontas | Contador de compras + avaliações | 88 compras; **2,0/5 em 3 avaliações** exibido sem filtro (prova negativa) |
| ePlanilhas | "Palavras dos nossos clientes" | genérico, sem nomes completos |
| Expert Cursos | Vídeos de alunos + "85.000 alunos" | 5 vídeos; número institucional |
| Mestre Academy | Dado de mercado (RD Station) + "alunos te contam" | sem número |
| Hotmart marketplace | Nota + nº de avaliações nativo | 1,9 (12) / 5,0 (1) / 4,8 (11) — expõe produtos ruins |
| Thomas Frank | Número + avatares + citação de autoridade (Tiago Forte) + depoimentos com credencial | 40.000+ usuários |
| Easlo | Contadores nativos Gumroad | 7.070 vendas / 269 ratings (o mais forte, pois é gerado pela plataforma) |
| God of Prompt | Trustpilot + reviews nomeadas | "5.000+ business owners" |
| PromptsHQ | Nenhuma verificável | 4 números de marketing sem fonte |
| Vertex42 | Contador de downloads | 750.000 downloads |
| Someka | Reviews nativos + demo grátis | 4,56 (9) — pouco, mas real |

---

## 5. Forte e fraco, página a página (resumo)

| Página | Forte | Fraco |
|---|---|---|
| B1 Tícius | Promessa concreta ("cálculo automático de prazos", "offline"), 4 perfis de "para quem é", 2 opções de preço com mesmo valor à vista (só muda o suporte), CNPJ e termos | Vídeo YouTube como herói (sai da página), fundo preto genérico, sem Pix declarado, checkout Hubla menos conhecido |
| B2 Planilha Essencial | Melhor estrutura BR: barra fixa com CTA, comparação com "software de R$200/mês", objeções respondidas em formato pergunta, 2 ofertas no Hotmart, CNPJ | "SUPER OFERTA 2026" e "ATENÇÃO!" soam feira; estrelas decorativas sem nota; página de 15k px |
| B3 Legal Hub | Marca própria (logo, paleta cobre), mockup 3D bonito, bônus "de R$97 por R$0", integração Google Forms como diferencial | Sem CNPJ/termos; "oferta por tempo limitado" sem prazo real; 3 order bumps no checkout cansam |
| B4 Samurai | Copy PAS clara, entregáveis listados, preço R$17 remove fricção, autor com posicionamento (marketing jurídico) | Headline em caixa alta com medo ("antes que a concorrência o faça"), capa de robô = visual de guru, sem depoimento, sem CNPJ, checkout hoje quebrado |
| B5 Guia do Excel | Ficha de produto com 730 avaliações reais, formas de pagamento com ícones, WhatsApp de suporte no topo, atualização grátis | Texto SEO de 22k px enterra o CTA; cookie banner bloqueia o herói no mobile; "oferta por tempo limitado" sem prazo |
| B6 PFO | Muitos CTAs com benefício ("QUERO TER DINHEIRO NA CONTA"), 13 entregáveis, 4 bônus | **Assinatura anual disfarçada** de "12x R$14,76/ano" ao lado de "acesso vitalício" (contradição que gera reembolso e denúncia); sem CNPJ |
| B7 Smart Planilhas | Licença por usuário (upsell natural), vídeo demonstrativo, parcelamento 10x, WhatsApp | R$249 para uma planilha sem nenhuma avaliação; "200 baixaram nos últimos dias" é claim vazio |
| B8 Planilhas Prontas | Preço ancorado, garantia 7 dias, 6 meses de suporte declarado | Nota 2,0/5 exibida; layout WooCommerce sem persuasão |
| B10 ePlanilhas | Oferta simples (pacote gigante), checkout próprio | "50% válido hoje: <data de hoje>" = escassez falsa (viola CDC/política Meta); 4.000 planilhas = commodity |
| B14 Expert Cursos | Certificado e carga horária no herói, 5 depoimentos em vídeo, CNPJ | Herói é vídeo do YouTube; page de 24k px com blocos triplicados; CTA de compra só no fim |
| B15 Mestre Academy | Dado de mercado citado com fonte; garantia bem explicada; empilha 1 ano de "Pro" | R$397 sem mostrar aula; cross-sell de agência polui a página de ChatGPT |
| I1 Thomas Frank | Vídeo próprio (não YouTube) com o autor, tabela de 3 tiers, cupom no topo, FAQ que responde reembolso, benefícios com GIF | 24k px; muitos links de navegação competem com a compra |
| I3/I4 Easlo | Zero fricção: preço, botão, contadores reais; escassez real ("0 left" no tier teams) | Copy de 100 palavras — só funciona com audiência prévia |
| I5 Business OS | Valor empilhado por módulo ($49+$49+...=$300 por $85), reembolso 30 dias, versão grátis com 4 seções (lead magnet no mesmo produto) | Design padrão Gumroad; "+100 businesses" fraco |
| I6 God of Prompt | Design de produto (não de guru): caixa 3D, cards, Trustpilot, lista nomeada de tudo que entra, lifetime | Âncora "$10.000" exagerada; "limited time" permanente |
| I7 PromptsHQ | Posicionamento por profissão (advogados/finanças), tipografia editorial, free pack como entrada, escada $0→$49→$97→$249 | Nenhuma prova real; 85% "tempo economizado" sem fonte |
| I9 Someka | Demo grátis + seletor de licença + serviços adicionais (suporte, customização) + assinatura | Página pesada, poucos reviews |

---

## 6. Padrões nas páginas brasileiras de alta venda

1. **Promessa "sem mensalidade / pagamento único / acesso vitalício" é o gancho nº 1** em planilhas e templates (Tícius, Planilha Essencial, Legal Hub, Smart Planilhas, Souza, ePlanilhas, Guia do Excel). A comparação explícita com "software de R$200/mês" (Planilha Essencial) é o argumento de preço mais forte.
2. **Preço sempre ancorado "De R$X por R$Y"** com parcela em 10–12x logo abaixo e valor à vista. Parcela < R$20 aparece em 5 de 6 LPs dedicadas (R$20,67 / R$15,26 / R$19,78 / R$14,76 / R$10,03).
3. **Garantia de 7 dias em 100% das LPs dedicadas** (é o mínimo do CDC para compra online; todas apresentam como diferencial). Reembolso de 30 dias não apareceu em nenhuma BR.
4. **Herói**: vídeo do YouTube embutido (Tícius, Expert Cursos, Smart) ou mockup de notebook/celular com "clique e assista" (Planilha Essencial, Legal Hub, PFO). Nenhuma das 19 usa VSL sem controles (vturb/panda) — VSL não é padrão nesse nicho de planilhas/templates.
5. **Fundo escuro + botão verde/limão** domina as LPs de advogado (Planilha Essencial, Legal Hub, Tícius, Samurai). Lojas de planilha (Guia do Excel, Loja das Planilhas) usam branco + azul e-commerce.
6. **CTAs em primeira pessoa** com benefício: "QUERO ORGANIZAR MEU ESCRITÓRIO AGORA", "QUERO TER DINHEIRO NA CONTA NO FINAL DO MÊS". 4–7 CTAs por página, sempre o mesmo destino.
7. **Bloco "Para quem é"** com 3–4 perfis (Tícius, PFO, Legal Hub) e **funcionalidades em cards** (7–13 itens, um por aba da planilha).
8. **Prova social é fraca e não verificável** na maioria ("12.410 advogados", "mais de 5000", "200 baixaram nos últimos dias"). Onde há avaliações nativas (Guia do Excel: 730; Hotmart marketplace) elas são o elemento mais crível — e também expõem produtos ruins (1,9/5).
9. **Timer regressivo não aparece nas LPs**, só nos checkouts (Hotmart 15 min, Kiwify 15 min). A escassez nas LPs é textual ("oferta por tempo limitado", "última chamada", "válido hoje: <data automática>") — a última é escassez falsa.
10. **Order bump é padrão no checkout**: 1 bump na Hotmart (39% off), 3 bumps na Kiwify. Bump típico: pack de planilhas complementares por R$47 ou curso curto.
11. **Checkout**: Hotmart pede CPF/CNPJ + celular + CEP; Kiwify pede CPF/CNPJ + telefone e tem "lembrar neste dispositivo". Pix, cartão parcelado com juros ("*valor parcelado possui acréscimo") e PayPal na Hotmart.
12. **Altura**: LPs dedicadas de 7k a 16k px no mobile; lojas com texto SEO chegam a 23–24k. Páginas curtas (Samurai, 7,2k) vendem produto de R$17; as de R$127–197 têm 12–15k.
13. **CNPJ/termos**: 50% das LPs dedicadas não têm CNPJ nem termos (Legal Hub, Samurai, PFO, Mestre). As lojas de planilha (WooCommerce/Shopify) têm sempre.
14. **Plataforma**: Kiwify e Hotmart para LPs de infoproduto; WooCommerce/Shopify para "lojas de planilha" com dezenas de SKUs; Hubla apareceu em 1 caso.

## 7. Padrões nas páginas internacionais

1. **A plataforma faz a prova**: Gumroad mostra vendas (7.070), distribuição de estrelas e "Top creator"; Notion Marketplace mostra reviews datadas; Someka/Trustpilot idem. O vendedor escreve pouco.
2. **Tiers de preço em vez de "de/por"**: Ultimate Brain $129/$228/$278; Freelance OS $79/$199; PromptsHQ $0/$49/$97/$249; Someka single/multi + add-ons. A âncora vem do tier superior, não de um preço riscado.
3. **Versão grátis ou demo do próprio produto** como entrada (Business OS "free version 4 sections", PromptsHQ "free pack", Someka "download free demo", Vertex42 100% grátis). Isso substitui o "bônus de R$97 por R$0" brasileiro.
4. **Valor empilhado por módulo** ("Order Manager $49 + Finance $49 + ... = $300 → $85") e **lifetime** como palavra-chave (God of Prompt, Business OS, Easlo "Lifetime updates included").
5. **Reembolso de 30 dias** (Business OS) ou política clara em FAQ (Thomas Frank). Sem timer em nenhuma; escassez só quando real ("0 left").
6. **Herói de produto**: mockup/ilustração 3D ou vídeo próprio com o autor; headlines curtas de 4–7 palavras ("Your Second Brain, ENTIRELY in Notion", "Stop writing prompts. Start getting results."). Nada em caixa alta.
7. **Design com identidade** (tipografia serifada no PromptsHQ, amarelo/preto no God of Prompt, roxo no Thomas Frank) vs. template de construtor de página.
8. **Páginas mais curtas** para o mesmo ticket: Gumroad 2–3k px; LPs próprias 9–12k; só Thomas Frank passa de 20k (e é o de maior ticket, $129–278).
9. **Cupom/desconto no topo** (SUMMER50) em vez de preço riscado, o que mantém o preço de lista íntegro.
10. **FAQ que inclui "quem NÃO deve comprar"** (Justin Welsh) e "posso pedir reembolso?" (Thomas Frank) — reduz reembolso depois.

## 8. O que parece "curso de guru" vs. profissional

**Sinais de guru (evitar):**
- Headline em caixa alta com medo/urgência ("ANTES QUE A CONCORRÊNCIA O FAÇA", "ÚLTIMA CHAMADA!", "ATENÇÃO!") — Samurai, Planilha Essencial.
- Capa 3D de e-book com robô/raio/fogo, fundo preto e botão vermelho/limão brilhante.
- Preço riscado com múltiplas âncoras ("de R$597 / de R$397 por R$197"), "bônus de R$97 por R$0", "valor de R$3.000" / "$10.000".
- Data automática "válido hoje: domingo, 13 de setembro" e "oferta por tempo limitado" sem prazo (ePlanilhas, Legal Hub, Guia do Excel).
- Números de prova não verificáveis ("12.410 advogados", "200 baixaram nos últimos dias").
- Ausência de CNPJ, termos, política e canal de suporte (Legal Hub, Samurai, PFO).
- Contradição vitalício vs. assinatura (PFO), 3 order bumps empilhados no checkout.

**Sinais de profissional (copiar):**
- Avaliações nativas com número (Guia do Excel 730; Easlo 269; Notion 54) e depoimentos com nome + credencial (Thomas Frank).
- Demo/versão grátis ou vídeo mostrando o produto por dentro (Someka, Business OS, Smart Planilhas).
- Tiers claros com o que cada um inclui; licença por usuário; serviços adicionais opcionais.
- Comparação honesta com a alternativa ("software de R$200/mês" vs. pagamento único) e "para quem é / para quem não é".
- Garantia explicada em FAQ, CNPJ, termos, WhatsApp/suporte visível no topo (Guia do Excel).
- Marca própria (logo, paleta, tipografia) e headline curta de benefício; screenshot real do dashboard no herói.
- Formas de pagamento com ícones (Pix, cartões, boleto) já na ficha do produto.

## 9. Referências por faixa de preço (5 por tipo)

### R$ 27–47 (guia, pack de prompts, planilha única)
1. **easlo.gumroad.com/l/brain** — estrutura mínima: capa, preço, botão, "what's included", contadores. Para ticket baixo, quanto menos fricção melhor.
2. **samurailab.com.br/prompts-de-ia-para-advogados/** — copiar a estrutura PAS + "entregáveis claros" + "para você se..."; NÃO copiar caixa alta, robô e ausência de CNPJ.
3. **promptshq.co** — escada $0 → pago com free pack no herói; segmentação por profissão; grid de números (usar só números reais).
4. **loja.guiadoexcel.com.br (ficha de produto)** — formas de pagamento com ícones, 4 selos (download imediato, atualizações, sem mensalidade, suporte), avaliações nativas.
5. **imaginationlabs.gumroad.com/l/business** — valor empilhado por módulo e versão grátis do mesmo produto como isca; reembolso 30 dias como diferencial.

### R$ 197–297 (planilha/sistema completo, template de gestão)
1. **planilhasessenciais.com.br/planilha-essencial-do-advogado/** — melhor esqueleto BR: barra fixa com CTA, comparação com software mensal, objeções em formato de pergunta, cards de funcionalidades, 2 ofertas no checkout. Trocar "SUPER OFERTA" por linguagem sóbria.
2. **tomazzonitreinamentos.com.br/ticius-pro/** — "para quem é" em 4 perfis, funcionalidades = abas, 2 opções que diferem só no suporte (upsell de serviço sem mudar o produto).
3. **notioncel.com.br/legal-hub-notion-para-advogados/** — identidade visual própria e mockup 3D; diferencial técnico (integração Google Forms) como argumento; adicionar CNPJ/termos.
4. **someka.net (Finance KPI Dashboard)** — demo grátis + licença single/multi + suporte e customização como add-ons: modelo de escada de valor para planilha B2B.
5. **imaginationlabs.gumroad.com/l/business** — reaproveitar a matemática de valor empilhado ($49+$49+$29+$19 = $300 por $85) para kit de planilhas.

### R$ 497–697 (curso + planilhas, sistema com treinamento e suporte)
1. **thomasjfrank.com/brain/** — tabela de 3 tiers (produto / + cursos / + suporte), vídeo próprio com o autor, benefícios com GIF, FAQ com reembolso, cupom no topo. É a página de maior ticket com estrutura mais limpa.
2. **godofprompt.ai/complete-ai-bundle** — lista nomeada de TUDO que entra (15+ itens), cards do conteúdo no herói, Trustpilot, "lifetime" como promessa. Reduzir âncora exagerada.
3. **learn.justinwelsh.me/the-content-operating-system** — depoimentos de pares com credencial logo após o herói, FAQ com "quem NÃO deve comprar" e "qual a diferença para o outro produto" (útil quando houver escada de ofertas).
4. **mestreacademy.com/curso/curso-chatgpt** — como empilhar 1 ano de comunidade/plataforma para justificar R$397+; garantia explicada em parágrafo próprio. Evitar cross-sell que desvia do produto.
5. **experttcursos.com.br/excel** — para o componente "curso": certificado + carga horária no herói, módulos listados, depoimentos em vídeo, CNPJ no rodapé. Substituir YouTube por player próprio e cortar a página pela metade.

## 10. Implicações diretas para o pipeline deste laboratório

- Página BR de planilha/kit de gestão: alvo de **10–14k px no mobile**, herói com mockup real do dashboard + vídeo próprio curto (não YouTube), promessa "pagamento único, sem mensalidade", comparação com software mensal, 3–4 perfis "para quem é", funcionalidades = abas, preço de/por com parcela < R$20, garantia 7 dias explicada em FAQ, CNPJ + termos + WhatsApp visíveis. 4–5 CTAs iguais.
- Prova social: coletar avaliações reais desde a primeira venda (widget nativo ou prints com nome/cidade/profissão). Não usar contadores inventados.
- Escassez: só real (lote, data de reajuste registrada em DECISOES.md). Nunca data automática do dia.
- Checkout: Kiwify ou Hotmart com **1 order bump** (pack complementar a R$47), não 3. Verificar que Pix aparece como aba padrão. Se o produto for vitalício, nunca configurar como assinatura.
- Escada de preço internacional adaptável: versão grátis/demo → produto R$97–197 → tier com suporte/treinamento R$297–497 (modelo Someka/Thomas Frank), em vez de "bônus de R$97 por R$0".

---

## Anexo A — Ordens de seção adicionais

**B7 Smart Planilhas (249):** ficha (título, licença, preço, "adicionar ao carrinho") → "200 pessoas baixaram nos últimos dias" → selos (10x, download rápido, tutorial, 7 dias, WhatsApp) → descrição → abas do produto (Guia Comercial, Cadastro, Financeiro) → "Avaliações (0)" → vídeo → produtos relacionados.

**B10 ePlanilhas (149,90):** barra "50% de desconto válido hoje: <data>" → "Baixe agora, mais de 4000 planilhas" → "Conheça a solução" → "São mais de 4000 planilhas em dezenas de categorias" (lista) → "As melhores planilhas prontas e editáveis" → "Palavras dos nossos clientes" → "E tem mais..." → "Baixe agora o pacote completo" (preço de/por, 12x) → FAQ → "Fale conosco" → dicas (blog).

**B11 Souza Sistemas (199,15):** ficha WooCommerce (preço riscado) → "Descrição" (texto corporativo longo) → "O ecossistema definitivo..." → "O que está incluso" (5 planilhas + curso cada) → "Diferenciais técnicos" → "Avaliações" → produtos relacionados. Sem CTA intermediário: só "Comprar agora" no topo.

**B13 LUZ Prime:** breadcrumb → "faz parte do LUZ Prime: +250 planilhas, +150 apresentações, prompts de IA" → "COMEÇAR A USAR AGORA" → texto educativo sobre gestão financeira → "Para quem é" → "Tudo sobre a planilha" (16 abas em h3) → "Como funciona" → "Mais modelos" → vídeo tutorial → artigos SEO ("O que é gestão financeira?", "5 dicas") → "Seja Prime" → formulário de cadastro. A página de produto virou porta de entrada da assinatura.

**I8 Vertex42 (grátis):** título → "Money Management Template 2.1" com botão DOWNLOAD (Excel / Google Sheets) e "Over 250.000 downloads" → descrição → versão anterior com "Over 750.000 downloads" → "How to use" (8 subseções com screenshots) → "Related templates" → redes sociais. Página de conteúdo que vende confiança e leva a versões premium/anúncios.

**I9 Someka (39,95):** ficha (nota 4,56, "Download Free Demo", seletor de licença, add-ons, "Add to cart" ou "Become member $99/mo") → abas (Product Info, Video, FAQ, Examples, Comments) → "Template description" → "Features" → "Features summary" → "Product video" → "User reviews" (9) → "Related templates".

**B12 Loja das Planilhas (Shopify):** cookie/termos → cupom 10% no topo → slideshow (90 modelos / 20 pacotes) → "Mais vendidos" (preço de/por + 4x) → "Coleções" → "Últimos lançamentos" → "Pacotes em destaque" → "Opinião de quem confia" → rodapé com CNPJ e políticas.

## Anexo B — Índice de arquivos gerados

| Arquivo (em `r4-shots/`) | Página |
|---|---|
| ticius-tomazzoni.png/.json | B1 Tícius |
| planilhasessenciais-adv.png/.json | B2 Planilha Essencial do Advogado |
| notioncel-legalhub.png/.json | B3 Legal Hub |
| samurai-prompts.png/.json | B4 Samurai Lab |
| guiadoexcel-gestao.png/.json | B5 Guia do Excel |
| henriquestuart-pfo.png/.json | B6 PFO |
| smart-dentista.png/.json | B7 Smart Planilhas |
| planilhasprontas-clinica.png/.json | B8 Planilhas Prontas |
| excelcoaching-advogados.png/.json | B9 Excel Coaching |
| eplanilhas-advogado.png/.json | B10 ePlanilhas |
| souza-kit-gestao.png/.json | B11 Souza Sistemas |
| lojadasplanilhas.png/.json | B12 Loja das Planilhas |
| luz-gestao.png/.json | B13 LUZ Prime |
| expertt-excel.png/.json | B14 Expert Cursos |
| mestreacademy-chatgpt.png/.json | B15 Mestre Academy |
| hotmart-dnl-planilhas / hotmart-30comandos / hotmart-200prompts / hotmart-powerbi-expert (.png/.json) | B16–B19 marketplace Hotmart |
| hotmart-checkout-br.png/.json | Checkout Hotmart (modo Brasil) |
| hotmart-checkout-excel / hotmart-checkout-powerbi (.png/.json) | Checkout Hotmart (modo EUA, com timer) |
| kiwify-checkout-br.png/.json, kiwify-checkout-legalhub.png/.json, kiwify-checkout-pfo.png/.json | Checkout Kiwify (BR e EUA) |
| thomasfrank-brain, notion-ultimatebrain, easlo-brain, easlo-freelanceos, gumroad-businessos, godofprompt-bundle, promptshq, vertex42-money, someka-finance-kpi, justinwelsh-contentos (.png/.json) | I1–I11 |
| hero/*.png | recorte 780×2200 do topo de 20 páginas (herói + primeira dobra) |
| dasckup-chatgpt, hashtag-chatgpt, estagiotrainee-excel, planilhas-vc-loja (.png/.json) | abertas e descartadas (blog/comparativo/domínio sequestrado) |
| etsy-budget, etsy-legal-prompts, planilhasprofissionais-fluxo, construindosonhos-kiwify, ninja-excel-lp, notion-vic-businessos, spreadsheet123-po (.json) | falhas registradas (403 / túnel / TLS) |

Scripts: `r4-scan.js` (varredura padrão), `r4-hotmart-br.js` (checkout forçando país Brasil), `r4-kiwify2.js` (fecha modal Kiwify),
`r4-crop.js` (recorte do herói), `r4-sum.js` e `r4-grep.js` (leitura dos JSON), `r4-batch.sh` + `r4-list1..6.txt` (lotes).
