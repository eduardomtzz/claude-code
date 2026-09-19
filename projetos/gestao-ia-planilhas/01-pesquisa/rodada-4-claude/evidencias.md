# R4 — Evidências de CRO para páginas de venda de produto digital (Seu Sócio Gestor)

Data da pesquisa: 13/09/2026. Contexto: kits de planilhas + prompts de IA, R$ 27 a R$ 697, páginas HTML próprias, tráfego frio de Meta Ads, comprador no celular, sem fundador em vídeo, sem depoimentos no lançamento.

Legenda: **F** = fato com link para fonte primária ou relatório original; **E** = estimativa ou opinião fundamentada (fonte secundária, dado sem metodologia aberta, ou leitura minha); **ND** = procurado e não encontrado.

Avisos gerais:
- Quase nenhuma fonte é específica de infoproduto brasileiro. Os benchmarks são internacionais e majoritariamente B2B/e-commerce; onde há dado brasileiro, está sinalizado.
- Estudos de caso de fornecedores (Unbounce, Vidyard, VWO, Wistia) têm viés de publicação: só os ganhos viram artigo. Trate os percentuais como "ordem de grandeza", não como previsão.

---

## 1. Estrutura da página de vendas

### Acima da dobra e atenção por rolagem
- Em eyetracking com 120 participantes e 130 mil fixações, 57% do tempo de visualização fica no primeiro screenful, 74% nos dois primeiros e 81% nos três primeiros (NN/g, 2018). Em 2010 eram 80% na primeira tela; as pessoas rolam mais, mas a queda de atenção após a dobra continua íngreme (F) [NN/g – Scrolling and Attention](https://www.nngroup.com/articles/scrolling-and-attention/)
- Mais de 42% do tempo de visualização cai nos 20% superiores da página e 65% nos 40% superiores (F) [NN/g](https://www.nngroup.com/articles/scrolling-and-attention/)
- NN/g recomenda: prioridade máxima no topo, evitar "falsos fins de página" (false floors) e usar sinais de continuidade (texto cortado, seta) para induzir rolagem (F) [NN/g](https://www.nngroup.com/articles/scrolling-and-attention/)

### Página longa vs. curta
- CXL: copy curta ganha quando risco, custo e compromisso percebidos são baixos e a motivação é impulsiva; copy longa ganha quando a decisão é racional/analítica e o preço é alto ("uma foto e uma descrição curta funcionam para um relógio, não para um software de US$ 2.000") (E, síntese da CXL sem teste controlado por preço) [CXL – Long form or short form](https://cxl.com/blog/long-form-or-short-form/)
- Casos citados pela CXL nos dois sentidos: Crazy Egg aumentou conversão em 30% ao alongar a página ~20x; edX/Unbounce e Flare (3,53% → 5,85%, +65%) ganharam encurtando (E, estudos de caso de fornecedor) [CXL](https://cxl.com/blog/long-form-or-short-form/), [CXL – short home pages](https://cxl.com/blog/4-cases-where-short-home-pages-outperformed-long-home-pages/)
- Não existe estudo publicado que cruze comprimento da página com faixa de preço de infoproduto de forma controlada (ND).

### Taxas de conversão por setor — Unbounce Conversion Benchmark Report (edição com dados de Q4/2024, publicada em março/2025; 41 mil páginas, 464 milhões de visitas, 57 milhões de conversões)
- Mediana geral: 6,6% (F) [Unbounce – average conversion rates](https://unbounce.com/average-conversion-rates-landing-pages/)
- Nota: as conversões medidas são majoritariamente leads/cadastros, não compras. Não use 6,6% como meta de venda.

| Setor (Unbounce) | Mediana | "Boa" (top 25%) |
|---|---|---|
| E-commerce | 4,2% | 11,4% |
| SaaS | 3,8% | 11,6% |
| Serviços profissionais | 6,1% | 14,1% |
| Serviços financeiros | 8,3% | 26,1% |
| Viagens e hospitalidade | 4,8% | 15,6% |
| Jurídico | 6,3% | 13,1% |
| Educação | 8,4% | 20,0% |
| Eventos e entretenimento | 12,3% | 40,8% |

Fonte da tabela (F): [Unbounce – What's a good conversion rate](https://unbounce.com/landing-pages/whats-a-good-conversion-rate/)

- Outros achados do mesmo relatório: 83% das visitas a landing pages são mobile; páginas escritas em nível de leitura de 5ª–7ª série convertem 11,1%, 56% acima de textos de 8ª–9ª série (F) [Unbounce](https://unbounce.com/landing-pages/whats-a-good-conversion-rate/)

### Ordem de seções recomendada por plataformas brasileiras
- Hotmart e Kiwify publicam guias de estrutura (headline, vídeo/demonstração, benefícios, conteúdo, prova, garantia, preço, FAQ), mas sem dados de teste que sustentem a ordem (E). O blog da Hotmart não respondeu durante a pesquisa (timeout); a página existe em [hotmart.com/pt-br/blog/pagina-de-vendas](https://hotmart.com/pt-br/blog/pagina-de-vendas). Nenhum benchmark numérico de conversão por faixa de preço foi encontrado na Hotmart ou Kiwify (ND).

---

## 2. Mídia do herói

### Vídeo em landing page
- Teste Vidyard/Unbounce (2011, explainer animado): sem vídeo 6,5%; vídeo embutido 11% (+69%); vídeo em lightbox 13% (+100%). Amostra não divulgada (E, estudo de caso do próprio fornecedor de vídeo) [Unbounce – case study Vidyard](https://unbounce.com/conversion-rate-optimization/case-study-using-video-to-lift-landing-page-conversion-rate-by-100/)
- O "vídeo aumenta conversão em 80–86%" (EyeView Digital) vem de um único teste pré-2020 (TutorVista) e circula sem metodologia pública (E, evite citar como regra) [Vbout resumo](https://www.vbout.com/blog/impact-of-video-content-on-landing-page-conversion-rates/)
- Wistia State of Video 2026 (13 milhões de vídeos, 79 milhões de horas): quanto mais curto o vídeo, maior a taxa de engajamento; vídeos abaixo de 1 minuto têm ~52% de engajamento médio; as maiores taxas de play ocorrem em home, galerias e páginas de produto (F) [Wistia – State of Video](https://wistia.com/learn/marketing/video-marketing-statistics)
- Não há estudo controlado comparando imagem estática vs. GIF vs. vídeo curto vs. VSL longa na mesma página de infoproduto (ND). O que existe são casos isolados de fornecedores.

### Sem apresentador: screencast e narração
- Revisão de estudos educacionais: talking head (rosto do instrutor) aumenta satisfação e aprendizado percebido, mas não melhora retenção e pode piorar recall factual; screencast é preferível para explicar processos. Sondermann & Merkt (2023, N=112): efeito negativo do talking head sobre recall, embora participantes o preferissem (F, contexto educacional, não comercial) [Science of Learning – resumo com referências](https://scienceoflearning.substack.com/p/should-instructional-videos-include), [Systematic review – Computers & Education Open](https://www.sciencedirect.com/science/article/pii/S2666557321000306)
- Leitura: para "planilha + prompt", demonstração de tela com narração é o formato mais alinhado à evidência; o rosto do fundador não é requisito para o vídeo funcionar (E).

### Voz de IA
- Estudo WPP Media / amp / MediaScience (2025, 55 participantes em laboratório, EUA): só 42% identificaram voz de IA em frases e 47% em anúncios completos; anúncios com voz sintética igualaram os humanos em engajamento neurológico e intenção de compra; vozes que o público *acreditava* serem humanas foram avaliadas como mais emocionais e "relacionáveis" (F, amostra pequena) [WPP Media](https://www.wppmedia.com/news/ai-voices-audio-ads)
- Pesquisas de sentimento de fornecedores de locução humana apontam menor confiança em anúncios "100% IA" (13%) versus "humano com apoio de IA" (48%) (E, fonte com conflito de interesse) [RealVOTalent](https://www.realvotalent.com/ai-voice-sentiment)
- Não há estudo de retenção ou conversão de VSL com voz de IA em página de vendas (ND).

### Som desligado e legendas (relevante para o herói em mobile)
- Teste interno do Facebook (2016): legendas aumentam o tempo de visualização de anúncios em vídeo em 12% em média; 80% reagem negativamente quando o vídeo toca com som inesperadamente (F) [3Play Media resumo do anúncio do Facebook](https://www.3playmedia.com/blog/captions-increase-viewership-for-facebook-video-ads/)
- Publishers reportam que até 85% dos views de vídeo no Facebook são sem som (E, dado de publishers, 2016) [Digiday](https://digiday.com/media/silent-world-facebook-video/)
- Verizon Media/Publicis (2019): 69% assistem vídeo sem som em locais públicos; 80% dizem ter mais chance de assistir até o fim com legenda (F, pesquisa declarada) [Forbes – Verizon Media](https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/)

| Formato do herói | Evidência de efeito | Nível |
|---|---|---|
| Imagem estática / mockup | Baseline; sem estudo comparativo direto | ND |
| GIF/loop de demonstração muda | Sem estudo; equivale a "vídeo autoplay sem som" na prática | E |
| Vídeo curto (<60 s) com legenda | Maior engajamento por duração (Wistia); +12% tempo com legenda (Facebook) | F/E |
| VSL longa com voz de IA | Sem dados publicados de conversão | ND |
| Vídeo em lightbox (clique para abrir) | +100% num caso Vidyard (2011) | E |

---

## 3. Bloco de preço

### Ancoragem e isca (decoy)
- Tversky & Kahneman (1974): roleta viciada em 10 ou 65 deslocou a estimativa mediana de "% de países africanos na ONU" de 25% para 45% (F) [Simply Psychology – resumo com referência ao paper](https://www.simplypsychology.org/what-is-the-anchoring-bias.html)
- Ariely, *Predictably Irrational* (cap. 1), assinatura da The Economist: com a opção-isca (impresso US$ 125), 16% escolheram online, 0% impresso, 84% impresso+online; sem a isca, 68% online e 32% impresso+online (F) [Wikipedia – Decoy effect, com referência ao livro](https://en.wikipedia.org/wiki/Decoy_effect)

### Preço riscado ("de/por")
- Análise de 22 experimentos em grandes marcas de assinatura (DoWhatWorks): preço riscado "tende a perder"; num teste da Spotify com 5 variações, todas as versões com preço riscado perderam (E, metodologia proprietária) [DoWhatWorks](https://www.dowhatworks.io/blog/do-strikethrough-prices-work)
- Claims de "+20–30% de intenção de compra" para preço riscado circulam em blogs de ferramentas de desconto sem estudo citável (E, fraco) [Voucherify](https://www.voucherify.io/blog/strikethrough-pricing-why-a-single-line-still-drives-conversions)
- Leitura: para produto novo sem histórico de preço, o "de/por" é juridicamente frágil (ver abaixo) e a evidência de conversão é mista; ancore por comparação de valor (o que custaria montar sozinho, consultoria, tempo), não por preço anterior inexistente (E).

### Bom/melhor/ótimo
- HBR (Mohammed, 2018) defende três níveis: "Good" atrai sensíveis a preço, "Better" mantém a base, "Best" extrai mais dos que querem mais; o artigo completo está atrás de paywall e não traz percentuais abertos (E) [HBR – Good-Better-Best](https://hbr.org/2018/09/the-good-better-best-approach-to-pricing)
- Combinado com Ariely: a opção do meio tende a capturar a maioria quando a "ótima" serve de âncora (E).

### Parcelamento e Pix no Brasil
- Nuvemshop (jun–ago/2026): Pix já supera cartão em número de pedidos; ticket médio Pix R$ 233,80 vs. cartão R$ 339,97; compras em parcela única caíram de 60,7% para 57,2% do faturamento; faturamento em 10x cresceu 54%; 52% dos lojistas oferecem desconto no Pix (F, dados de uma plataforma) [E-Commerce Brasil / Nuvemshop](https://www.ecommercebrasil.com.br/noticias/pix-ou-cartao-dados-mostram-como-o-brasileiro-paga-no-comercio-eletronico)
- Gmattos (via CNN/PagBrasil): 47% das lojas online oferecem desconto no Pix, tipicamente 4–12% (até 15% na Black Friday). Caso Scarf Me: após desconto no Pix, participação do Pix subiu de 32% para 45% em dois meses (E, caso de fornecedor de pagamento; mede mix, não conversão total) [PagBrasil](https://www.pagbrasil.com/pt-br/blog/pix/desconto-para-metodo-de-pagamento-pix/)
- Efeito do desconto Pix sobre a taxa de conversão total da página: não há estudo publicado (ND). O que se mede é migração de meio de pagamento e economia de taxa/chargeback.
- Lei 13.455/2017 autoriza preço diferente por meio/prazo de pagamento, desde que o desconto seja informado "em local e formato visíveis ao consumidor" (F) [Planalto – Lei 13.455](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13455.htm)

### Regras brasileiras para exibir preço
- Lei 10.962/2004 dispõe sobre a oferta e as formas de afixação de preços (F) [Planalto – Lei 10.962](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.962.htm)
- Decreto 5.903/2006, art. 2º: preço deve ter correção, clareza, precisão, ostensividade e legibilidade; art. 3º: informar o **total à vista** e, em venda a prazo, o total com financiamento, número/periodicidade/valor das parcelas, taxa de juros e acréscimos (F) [Justia – Decreto 5.903](http://brasil.justia.com/nacionales/decretos/5-903-de-20-9-2006/gdoc/)
- Decreto 5.903/2006, art. 9º, inciso IV: é infração "informar preços apenas em parcelas, obrigando o consumidor ao cálculo do total"; inciso II: cores de letra e fundo idênticas ou semelhantes; inciso I: letras de tamanho não uniforme que dificultem a percepção (F) [Modelo Inicial – art. 9](https://modeloinicial.com.br/lei/DEC-5903-2006/decreto-5903/art-9)
- Implicação direta: "12x de R$ 19,90" só pode aparecer com o valor total à vista igualmente visível; e "parcelamento em destaque" não pode esconder o preço cheio (E, decorrente do art. 9º IV).
- Conar, art. 27 §3º(a): o anúncio deve ser claro quanto ao preço total; "alegada a sua redução, o Anunciante deverá poder comprová-la mediante anúncio ou documento que evidencie o preço anterior"; §3º(b): entrada, prestações e taxas em operações a prazo (F) [Código Conar – PDF Secom](https://www.gov.br/secom/pt-br/acesso-a-informacao/legislacao/ca2digobrasdeautoregulanovo.pdf)
- CDC art. 37 §1º: é enganosa a publicidade falsa ou capaz de induzir em erro sobre "preço e quaisquer outros dados"; §3º: enganosa por omissão quando omite dado essencial (F) [Jusbrasil – art. 37 CDC](https://www.jusbrasil.com.br/topicos/10603148/artigo-37-da-lei-n-8078-de-11-de-setembro-de-1990)
- "Portaria 6/2022" sobre preço de/por: não localizada. Não encontrei portaria federal específica que defina "preço de referência" para promoções (ND). O que rege é CDC art. 37 + Decreto 5.903 + Conar art. 27 §3º; Senacon e Procons tratam a "metade do dobro" (subir o preço antes para simular desconto) como publicidade enganosa (F) [Agência Brasil – Procon-SP Black Friday 2024](https://agenciabrasil.ebc.com.br/economia/noticia/2024-11/procon-sp-recebeu-no-ultimo-mes-2-mil-reclamacoes-relacionadas-bla), [InvestNews – Procon Black Friday 2025](https://investnews.com.br/financas/black-friday-2025-10-duvidas/)
- Procon-SP mantém lista pública de sites a evitar (81 em 2025) e recebeu 1.533 reclamações de Black Friday só em novembro/2025 (F) [Metrópoles](https://www.metropoles.com/negocios/procon-sp-tem-lista-de-78-sites-que-devem-ser-evitados-na-black-friday), [Terra](https://www.terra.com.br/especiais/black-friday/black-friday-2025-conheca-a-lista-do-procon-sp-com-sites-a-serem-evitados,b6b12d097223c1adbbb076965e230096co9dhsm0.html)
- Referência comparada útil para política interna: na UE (Diretiva Omnibus) o "de" deve ser o menor preço praticado nos 30 dias anteriores (F, não vale no Brasil, mas é um critério defensável) [Uniqodo – strikethrough](https://www.uniqodo.com/glossary/what-is-strikethrough-pricing)

| Elemento de preço | Evidência de conversão | Risco legal BR |
|---|---|---|
| Preço à vista em destaque | Obrigatório | Nenhum |
| "12x de R$ X" + total visível | Ticket sobe com parcelamento (Nuvemshop) | Baixo se total à vista visível |
| "12x de R$ X" sem total | — | Infração Decreto 5.903 art. 9º IV |
| Preço riscado de/por | Mista/negativa em assinaturas | Alto sem prova do preço anterior (Conar 27 §3º, CDC 37) |
| Desconto Pix | Migra mix para Pix; sem dado de conversão total | Baixo se informado antes do checkout (Lei 13.455) |
| Três planos (bom/melhor/ótimo) | Decoy/ancoragem robustos em laboratório | Nenhum |

---

## 4. Urgência e escassez

### Efeito medido
- CXL registra: countdown levou Cracku a +300% de conversões e MusicLawContracts (Marcus Taylor) a +147%; o próprio artigo alerta que quando o cronômetro zera a oferta precisa expirar de verdade (E, estudos de caso sem amostra) [CXL – Creating urgency](https://cxl.com/blog/creating-urgency/)
- Booking.com: +18% após widgets de prova social e +15–20% em propriedades com notas recentes fortes (E, dado citado pela CXL) [CXL](https://cxl.com/blog/creating-urgency/)
- Mathur et al. (Princeton, 2019), crawler em 11 mil sites de e-commerce: 393 countdowns em 437 sites, dos quais 157 instâncias em 140 sites eram enganosas (reiniciavam ao recarregar); dark patterns em pelo menos 11% dos sites (F) [Paper – Dark Patterns at Scale](https://arxiv.org/pdf/1907.07032), [UChicago resumo](https://cs.uchicago.edu/news/dark-patterns/)
- Meta-análise de "18 testes de countdown com mediana +9,1% para prazos reais e −3,2% para falsos" aparece só em blog de ferramenta, sem lista de testes (E, fraco) [LiquidBoost](https://liquidboost.app/blog/countdown-timer-conversion-data)
- Não há estudo controlado sobre "lotes" ou "bônus por prazo" em infoproduto (ND).

### O que a Meta proíbe ou penaliza
- Padrões de Publicidade – Práticas Comerciais Inaceitáveis: anúncios não podem promover produtos/ofertas usando práticas enganosas, incluindo preço enganoso, endossos não autorizados e promessas de retorno garantido (F) [Meta Transparency – Unacceptable Business Practices](https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/)
- Conteúdo de baixa qualidade ou perturbador (política de anúncios): linguagem sensacionalista, ocultar informação para induzir clique, pop-ups excessivos e páginas de destino que não correspondem ao anúncio (F, página oficial não renderizou; conteúdo confirmado por múltiplas fontes) [Meta Business Help 617541753336634](https://www.facebook.com/business/help/617541753336634), [Jon Loomer – Low-quality post-click](https://www.jonloomer.com/low-quality-ad-content-and-post-click-experiences/)
- Distribuição orgânica e paga: clickbait ("você não vai acreditar…") e engagement bait são rebaixados (F) [Meta – Clickbait links](https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/clickbait-links/), [Meta – Engagement bait](https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/engagement-bait/)
- A Meta não tem regra escrita que proíba "countdown" em si; o que pega é urgência falsa enquadrada como prática enganosa e a queda de quality ranking (E).

### CDC e Conar
- CDC art. 6º, III e IV: direito a informação adequada e clara e proteção contra publicidade enganosa e abusiva e métodos comerciais coercitivos ou desleais (F) [Modelo Inicial – art. 6 CDC](https://modeloinicial.com.br/lei/CDC/codigo-defesa-consumidor/art-6)
- CDC art. 37: proibida publicidade enganosa (falsa ou que induz em erro, inclusive por omissão) e abusiva (explora medo, se aproveita de deficiência de julgamento) (F) [Jusbrasil – art. 37](https://www.jusbrasil.com.br/topicos/10603148/artigo-37-da-lei-n-8078-de-11-de-setembro-de-1990)
- CDC art. 39, IV e X: prevalecer-se da fraqueza ou ignorância do consumidor para impor produtos; elevar preço sem justa causa (F) [Modelo Inicial – art. 39](https://modeloinicial.com.br/lei/CDC/codigo-defesa-consumidor/art-39,inc-X)
- Conar art. 27 §1º: descrições e alegações objetivas devem ser comprováveis; §5º: expressões vendedoras só se comprováveis (F) [Código Conar](https://www.gov.br/secom/pt-br/acesso-a-informacao/legislacao/ca2digobrasdeautoregulanovo.pdf)
- "Vagas limitadas" para produto digital de escala ilimitada é apontada por advogados como escassez falsa enquadrável no art. 37 (E, doutrina) [Walmar Andrade – publicidade enganosa de infoprodutos](https://walmarandrade.com.br/publicidade-enganosa-infoprodutos/)

### Casos brasileiros
- Procon-SP multou a Empiricus em R$ 40 mil (2019) pela campanha "Bettina" (patrimônio de R$ 1 milhão a partir de R$ 1,5 mil): promessa de resultado "enganosa e capaz de induzir o consumidor a erro" (F) [IstoÉ Dinheiro](https://istoedinheiro.com.br/procon-sp-multa-empiricus-por-propaganda-enganosa)
- Procon-MG multou a Estácio em R$ 931.728,96 por propaganda enganosa (F) [MPMG](https://www.mpmg.mp.br/portal/menu/comunicacao/noticias/procon-mg-multa-faculdade-estacio-de-sa-por-propaganda-enganosa.shtml)
- Procon-DF fechou empresa que vendia cursos com falsa garantia de emprego (F) [Agência Brasília](https://www.agenciabrasilia.df.gov.br/w/procon-fecha-empresa-que-vendia-cursos-com-falsa-garantia-de-emprego-a-jovens-do-df)
- TJ-SP condenou influenciadora a restituir consumidor por publicidade enganosa de curso online (F, fonte é escritório de advocacia) [Maia Yoshiyasu](https://mylaw.com.br/2024/02/26/influenciadora-e-condenada-por-publicidade-enganosa-em-curso-online-como-se-prevenir/)
- Conar 2025: sustações por alegações sem comprovação ("eleita a melhor do Brasil", "5x mais rápido", "melhores taxas do mercado" — Eisenbahn, Sonridor, Wellhub) (F) [Meio & Mensagem](https://www.meioemensagem.com.br/comunicacao/confira-os-anunciantes-mais-punidos-pelo-conar-em-2025)
- Caso Conar específico de "últimas vagas/só hoje" em infoproduto: não localizado (ND).

---

## 5. Prova social e confiança

### Efeito medido
- Spiegel Research Center (Northwestern, 2017): produto com 5 avaliações tem probabilidade de compra 270% maior que sem avaliações; efeito maior em produto caro (+380%) que em barato (+190%); benefício marginal cai rápido após 5 avaliações; pico de compra em notas 4,0–4,7 (não em 5,0); selo "comprador verificado" +15% (F) [Spiegel – How online reviews influence sales](https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/)
- WikiJob/VWO: três depoimentos "sóbrios" movidos para o topo da página elevaram compras em 34%; a mesma prova no rodapé não teve efeito (E, estudo de caso de fornecedor) [VWO – WikiJob](https://vwo.com/success-stories/wikijob/)
- BrightLocal 2026 (1.002 adultos, EUA, negócios locais): 97% leem avaliações; 31% só usam negócios com 4,5+ estrelas; 47% não consideram negócio com menos de 20 avaliações; 74% querem avaliações dos últimos 3 meses (F, contexto local/EUA) [Resumo BrightLocal 2026](https://gbppromote.com/local-consumer-review-survey/)
- Reclame AQUI (fev/2025, ~2.300 usuários): 81,54% leem reviews antes de comprar; 72,29% deixariam de comprar de marca que não se importa com a opinião do cliente (F, amostra da própria base) [Blog Reclame AQUI](https://blog.reclameaqui.com.br/varejo-consumidores-leem-reviews-antes-de-comprar/)
- Reclame AQUI/CX Trends 2024: 48% consultam o Reclame AQUI antes de comprar (E, pesquisa da própria plataforma) [Terra – reputação digital](https://www.terra.com.br/noticias/reputacao-digital-se-torna-decisiva-na-jornada-de-compra,04dca87fa63a1e53437dada8ab4f71efkaugmj4i.html)

### Selos e segurança
- Baymard (2025, 1.026 respondentes): 19% abandonaram um checkout nos últimos 3 meses por "não confiar no site com dados do cartão"; encapsular visualmente o bloco do cartão aumenta a segurança percebida; um selo "caseiro" superou selos SSL de fornecedores reais (exceto Norton), ou seja, a presença visual pesa mais que a legitimidade técnica (F) [Baymard – perceived security](https://baymard.com/blog/perceived-security-of-payment-form)
- Baymard, motivos de abandono 2025: custos extras 40%, entrega lenta 20%, desconfiança com cartão 19%, criar conta 18%, checkout longo 17%, erros do site 17%, poucos métodos de pagamento 9% (F) [Baymard – cart abandonment](https://baymard.com/lists/cart-abandonment-rate)
- CXL (2.100 + 1.037 respondentes, EUA): selos familiares (PayPal, Norton, Google, Visa/Mastercard) geram mais segurança percebida; "quanto mais familiar o símbolo, maior a segurança percebida" (F) [CXL – trust seals](https://cxl.com/research-study/trust-seals/)
- Garantia de devolução: nenhum teste A/B público e bem documentado isolando a garantia (ND). Baymard mostra "política de devolução insatisfatória" como motivo de 13% dos abandonos, o que sustenta exibir a garantia perto do preço (E).

### Lançar sem depoimentos
- Alternativas com respaldo: (a) demonstração de tela do produto real (evidência do item 2); (b) números verificáveis de uso do produto — não invente contagem de clientes; (c) garantia explícita e canal de suporte; (d) reputação da plataforma de checkout (Hotmart/Kiwify têm páginas no Reclame AQUI; a Kiwify aparece com nota 8,0–8,1 "Ótimo") (E) [Reclame AQUI – Kiwify](https://www.reclameaqui.com.br/empresa/kiwify/); (e) coletar avaliações desde a primeira venda para atingir o patamar de 5 avaliações do Spiegel (E)
- Hotmart: comprador avalia o produto de 1 a 5 estrelas após pagamento aprovado; a nota geral aparece na página do produto no marketplace (F) [Hotmart – indicador de satisfação](https://help.hotmart.com/pt-br/article/115006174067/o-que-e-o-indicador-de-satisfacao-no-mercado-), [Hotmart Ask](https://help.hotmart.com/pt-br/article/360030387292/hotmart-ask-o-que-e-e-como-configurar). Kiwify não tem avaliação pública de produto equivalente (ND).

### Regras para depoimentos
- Conar art. 27 §9º: só depoimentos personalizados e genuínos, ligados à experiência real; sempre comprováveis; modelos sem personalização só como "licença publicitária", nunca confundida com testemunhal (F) [Código Conar](https://www.gov.br/secom/pt-br/acesso-a-informacao/legislacao/ca2digobrasdeautoregulanovo.pdf)
- Conar Anexo Q, item 3: consumidor identificado deve ter nome e sobrenome verdadeiros; funcionários e modelos não podem se passar por consumidores; testemunho limitado à experiência pessoal; anunciante deve comprovar a veracidade quando solicitado (item 5.1) (F) [Código Conar](https://www.gov.br/secom/pt-br/acesso-a-informacao/legislacao/ca2digobrasdeautoregulanovo.pdf)
- Meta: endossos não autorizados e resultados que o usuário típico não obtém são práticas comerciais inaceitáveis (F) [Meta – Unacceptable Business Practices](https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/)

---

## 6. UX mobile e performance

### Velocidade
- Google/Deloitte "Milliseconds Make Millions" (2020, 37 marcas, 4 semanas, mobile): melhora de 0,1 s elevou conversão de varejo em 8,4% e ticket em 9,2%; viagens +10,1% de conversão; bounce em páginas de lead −8,3% (F) [Deloitte](https://www.deloitte.com/ie/en/services/consulting/research/milliseconds-make-millions.html), [web.dev](https://web.dev/case-studies/milliseconds-make-millions)
- Akamai/SOASTA (2017, ~10 bilhões de visitas): atraso de 100 ms reduz conversão em 7%; 2 s de atraso elevam bounce em 103%; 53% dos visitantes mobile abandonam página que leva mais de 3 s (F) [Akamai](https://www.akamai.com/newsroom/press-release/akamai-releases-spring-2017-state-of-online-retail-performance-report)
- Portent (dados 2019, atualizado 2022; 20 sites, 100 milhões de pageviews): e-commerce converte 3,05% a 1 s, 1,68% a 2 s, 1,12% a 3 s, 0,67% a 4 s; B2B 1 s converte 3x mais que 5 s. O próprio artigo admite não controlar variáveis de confusão e não define qual métrica de carregamento usou (F com ressalva) [Portent](https://portent.com/blog/analytics/research-site-speed-hurting-everyones-revenue.htm)
- Core Web Vitals "bom" no percentil 75: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 (F) [web.dev – thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds)

### Sticky CTA
- GrowthRock (e-commerce): botão fixo de compra +7,9% pedidos no desktop (99% sig., ~2.000 conversões/variação); no mobile, versão "drawer" +5,2% pedidos (98% sig.) e versão simples sem diferença (F, caso único) [GrowthRock](https://growthrock.co/sticky-add-to-cart-button-example/)
- Outros casos reportam +2,7% a +20% e um outlier de +252% (mobile); nem todo sticky ganha (E) [Convertibles](https://convertibles.dev/blogs/case-studies/homepage-sticky-cta-case-study), [Blend Commerce](https://blendcommerce.com/blogs/ab-tests-shopify/7-17-increase-in-conversion-rate)
- Leitura: em página longa mobile, CTA fixo no rodapé com preço é aposta de baixo risco; testar com e sem (E).

### Tipografia e leitura
- Linha ideal 50–75 caracteres; WCAG 1.4.8 recomenda no máximo 80; em mobile retrato o problema quase não ocorre (F) [Baymard – line length](https://baymard.com/blog/line-length-readability)
- NN/g (leitura de relance): tamanhos maiores, largura regular e maior peso venceram em legibilidade (F) [NN/g – glanceable fonts](https://www.nngroup.com/articles/glanceable-fonts/)
- Lighthouse aprova se ≥60% do texto tem ≥12 px; o limite foi reduzido de 16 px porque 80% das páginas falhavam; 16 px segue sendo o padrão de corpo dos navegadores (F) [Chrome Developers – font-size audit](https://developer.chrome.com/docs/lighthouse/seo/font-size), [Lighthouse PR #4550](https://github.com/googlechrome/lighthouse/pull/4550)
- Unbounce: texto em nível de 5ª–7ª série converte 56% melhor que 8ª–9ª (F) [Unbounce](https://unbounce.com/landing-pages/whats-a-good-conversion-rate/)

### Vídeo autoplay mudo com legenda
- Ver item 2: 80% reagem mal a som inesperado; legenda +12% de tempo de visualização (F) [3Play Media](https://www.3playmedia.com/blog/captions-increase-viewership-for-facebook-video-ads/)

### Formulários e checkout
- Checkout médio tem 11,3 campos (2024) quando ~8 bastam; Baymard historicamente aponta 23,48 elementos de formulário contra 12–14 ideais (E, dados de terceiros citando Baymard) [Frisbii](https://frisbii.com/blog/6-best-practices-to-increase-checkout-conversion-rates/)
- GoodUI: "sem campo de cupom" mediana +24% (3 testes); "menos campos" +13% (4 testes) (E, base pequena) [GoodUI](https://goodui.org/blog/better-experiments-prioritize-ab-tests-to-maximize-your-win-rate/)
- Abandono de carrinho médio 70,22% (50 estudos, até set/2025) (F) [Baymard](https://baymard.com/lists/cart-abandonment-rate)

### Banner de cookies e LGPD
- Bielova et al. (USENIX Security 2024): banner neutro 17% de rejeição; opção de rejeitar igualmente visível eleva rejeição a 34%; banner sem "recusar" 4% (F) [Lista de estudos – ignite.video](https://www.ignite.video/en/articles/basics/cookie-consent-studies)
- Análise longitudinal de CMPs (2024): com "Rejeitar tudo" no primeiro nível ~60% rejeitam; quando rejeitar exige vários cliques ~90% aceitam (F) [ignite.video](https://www.ignite.video/en/articles/basics/cookie-consent-studies)
- Advance Metrics (2024): 25,4% aceitam tudo diretamente; 68,9% fecham ou ignoram o banner (F) [ignite.video](https://www.ignite.video/en/articles/basics/cookie-consent-studies)
- Claims de "banner reduz conversão em 5–20%" vêm de blogs de fornecedores sem estudo aberto (E, fraco) [ClearAnalytics](https://clearanalytics.eu/blog/cookie-consent-banners-are-killing-your-conversion-rate)
- Guia ANPD (out/2022): botão para rejeitar todos os cookies não necessários, de fácil visualização, no primeiro e no segundo nível; três opções com o mesmo destaque ("aceitar todos", "rejeitar todos", "gerenciar"); cookies de consentimento desativados por padrão; práticas desaconselhadas: botão único "concordo", destaque só ao aceite, pré-marcação; consentimento é a base mais adequada para cookies de publicidade (Pixel), legítimo interesse "dificilmente" se aplica a publicidade (F) [ANPD – Guia de cookies PDF](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf/@@display-file/file)
- Implicação para o Pixel: com banner conforme, uma parcela relevante (34–60% nos estudos europeus) pode recusar; o CAPI server-side só pode disparar com a mesma base legal. Planeje a atribuição com perda de sinal (E).

| Métrica mobile | Meta | Fonte |
|---|---|---|
| LCP | ≤ 2,5 s (p75) | web.dev |
| INP | ≤ 200 ms | web.dev |
| CLS | ≤ 0,1 | web.dev |
| Fonte de corpo | ≥ 16 px (mínimo Lighthouse 12 px) | Chrome Developers |
| Linha | 50–75 caracteres | Baymard |
| Campos no checkout | ~8 | Baymard (via terceiros) |

---

## 7. Anúncio ↔ página

### Message match
- Unbounce define message match como o grau em que a página repete a promessa e a frase do anúncio; a justificativa é reduzir a sensação de "cheguei no lugar errado" (F, definição) [Unbounce – Message match](https://unbounce.com/conversion-glossary/definition/message-match/)
- "Dynamic text replacement dá 10–20% a mais" aparece em blog de ferramenta sem estudo (E, fraco) [Fibr](https://fibr.ai/blog/the-landing-page-puzzle-how-message-match-creates-the-perfect-fit)
- Analogia com Google Ads: a "experiência na página de destino" é um dos três componentes do Índice de Qualidade; na Meta, o equivalente são os diagnósticos de relevância abaixo (E).

### Diagnósticos de relevância da Meta
- Três rankings (qualidade, taxa de engajamento, taxa de conversão), cada um "acima da média / média / abaixo da média (35%, 20%, 10% inferiores)", exibidos a partir de 500 impressões; qualidade usa feedback de usuários e "atributos de baixa qualidade" como ocultar informação, linguagem sensacionalista, engagement bait e experiência pós-clique (F) [Meta – About Ad Relevance Diagnostics](https://www.facebook.com/business/help/403110480493160), [Meta – How to use](https://www.facebook.com/business/help/436113280262012), [Meta – Attributes to avoid](https://www.facebook.com/business/help/1767120243598011)
- Leitura oficial das combinações: qualidade e engajamento acima da média com conversão abaixo = problema de página/oferta, não de criativo (F, tabela do help center; texto oficial não renderizou, confirmado em fontes secundárias) [Chui – explicação](https://chui.substack.com/p/facebook-ads-quality-engagement-and)
- Política: produtos e promessas do anúncio devem bater com a página; cloaking e redirecionamento para esconder o destino são infrações de "burlar sistemas" (F) [Meta – Introduction to Advertising Standards](https://transparency.meta.com/policies/ad-standards/)

### Advertorial / pré-venda vs. página direta
- Advertorials convertem tráfego frio em 1–3% de clique para lead/venda, segundo praticantes; um caso de CAC −46% ao trocar página de produto por advertorial circula sem fonte primária (E, fraco) [Landerlab](https://landerlab.io/blog/advertorial-landing-page-3-examples), [Convertibles](https://convertibles.dev/blogs/optimization/examples-of-advertorials)
- Splitbase: advertorial faz sentido para produtos "que geram muitas perguntas" e exigem educação; Nik Sharma cita ~15% de clique do advertorial para a página de produto (E) [Splitbase](https://splitbase.com/blog/landing-page-types)
- Nenhum teste publicado com números auditáveis comparando advertorial vs. direto (ND).

---

## 8. Testes A/B e benchmarks

### Testes com maior retorno esperado em página nova
- GoodUI: padrões com histórico de vitórias têm 71% de taxa de acerto (36 de 51 previsões); maior efeito mediano em "sem campo de cupom" (+24%) e "menos campos" (+13%) (E, base de 115 testes) [GoodUI – previsibilidade](https://goodui.org/blog/can-winning-a-b-tests-be-predicted-with-past-results/), [GoodUI – priorização](https://goodui.org/blog/better-experiments-prioritize-ab-tests-to-maximize-your-win-rate/)
- Consenso CXL/VWO/Optimizely (sem meta-análise pública de win rate): headline/promessa, oferta/preço, posição da prova, CTA e comprimento do formulário são as alavancas de maior amplitude; cor de botão é de baixa amplitude (E) [Optimizely – 101 things to test](https://www.optimizely.com/insights/blog/101-things-to-ab-test/), [VWO – exemplos](https://vwo.com/blog/ab-testing-examples/)
- Evidência específica deste relatório: prova social no topo vs. rodapé (+34%, WikiJob); vídeo em lightbox vs. embutido (13% vs. 11%, Vidyard); sticky CTA mobile (+5%); página curta vs. longa (ganhos nos dois sentidos); preço riscado (tende a perder em assinaturas).

Ordem sugerida de testes para a página nova (E):
1. Headline + promessa do herói (mesma frase do anúncio vencedor).
2. Herói: demonstração em vídeo curto legendado vs. imagem/mockup estático.
3. Bloco de preço: à vista em destaque + parcelas vs. três planos com âncora.
4. Prova: bloco de garantia + demonstração acima da dobra vs. só no fim.
5. Sticky CTA com preço vs. sem.
6. Comprimento: versão enxuta (R$ 27) vs. longa (R$ 197/697).

### Tamanho de amostra
- Não existe número universal: depende da taxa base e do efeito mínimo detectável (MDE). Exemplo: com base 3%, detectar +5% relativo exige ~25.000 visitantes por variação; +10% exige ~6.500 (E, calculadora) [Atticus Li – guia](https://atticusli.com/blog/posts/ab-test-sample-size-guide/)
- Exemplo GuessTheTest: a 5% de significância, MDE 10% exige 2.922 conversões totais; MDE 5% exige 11.141 (F, cálculo da fonte) [GuessTheTest](https://guessthetest.com/calculating-sample-size-in-a-b-testing-everything-you-need-to-know/)
- Regras práticas usadas no mercado: nunca menos de 100 conversões por variação; ideal 300+; rodar semanas inteiras (ciclo de negócio completo) (E) [Invesp](https://www.invespcro.com/blog/calculating-sample-size-for-an-ab-test/), [ABTasty](https://www.abtasty.com/blog/sample-size-calculation/)
- Calculadoras: [Evan Miller – sample size](https://www.evanmiller.org/ab-testing/sample-size.html), [Evan Miller – sequencial](https://www.evanmiller.org/ab-testing/sequential.html), [CXL – calculadora](https://cxl.com/ab-test-calculator/) (F)
- Conta prática para este projeto (E): com 1% de conversão e MDE de 20% relativo (1,0% → 1,2%), são ~30 mil visitantes por variação. A R$ 1–2 por clique, um teste custa R$ 60–120 mil em mídia. Logo, na página de R$ 27, teste primeiro métricas de funil (clique no CTA, InitiateCheckout) com testes sequenciais; reserve testes em Purchase para mudanças grandes.

### Benchmarks visita → compra por fonte
- Unbounce (todas as indústrias, majoritariamente leads): mediana 6,6%; e-commerce 4,2%; educação 8,4% (F) [Unbounce](https://unbounce.com/landing-pages/whats-a-good-conversion-rate/)
- Meta Ads (WordStream 2026): CTR médio 1,49%, CPC US$ 0,77; campanhas de geração de leads convertem 7,72% em média, educação 10–13% (leads, não vendas) (F, dados de contas de agência nos EUA) [Superscale resumo WordStream 2026](https://superscale.ai/learn/meta-ads-benchmarks-by-industry/), [WordStream 2025](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025)
- Google Ads Search (WordStream 2026, 13 mil campanhas, abr/2025–mar/2026): conversão média 8,18%; educação 13,14% (F, leads e vendas misturados) [WordStream – Google Ads 2026](https://www.wordstream.com/blog/2026-google-ads-benchmarks)
- E-mail (Omnisend/Klaviyo, e-commerce): campanhas 0,08% de conversão por envio; automações 1,49%; fluxos de boas-vindas no top 10% convertem 12–18% (F, e-commerce internacional) [Omnisend benchmarks](https://www.omnisend.com/blog/email-marketing-benchmarks/), [Klaviyo benchmarks](https://www.klaviyo.com/products/email-marketing/benchmarks)
- Brasil, infoproduto, Meta frio: uma agência brasileira publica "venda direta de infoprodutos 0,8–2,5%" e "tráfego frio ~0,9%", sem fonte (E, fraco) [Trafius](https://trafius.com.br/blog/taxa-de-conversao-de-landing-page-pra-meta-ads-metas-realistas). Hotmart e Kiwify não publicam benchmark de conversão de página (ND).

| Fonte de tráfego | Benchmark disponível | Natureza | Nível |
|---|---|---|---|
| Meta frio → compra de infoproduto BR | ~0,5–1,5% | Estimativa de agências | E |
| Meta → lead | 7,7% média; educação 10–13% | WordStream 2026 | F |
| Google Search → conversão | 8,18% média; educação 13,1% | WordStream 2026 | F |
| E-mail campanha → compra | 0,08% por envio; 1,49% em automações | Omnisend 2025 | F |
| Landing page geral | mediana 6,6% (leads) | Unbounce Q4/2024 | F |

---

## Implicações para páginas de R$ 27, R$ 197 e R$ 697 (E)

Leitura minha, combinando as evidências acima com as restrições do projeto.

**Comum às três**
- Primeira tela decide: promessa igual à do anúncio, demonstração visual do produto (vídeo curto legendado, autoplay mudo, ou mockup), preço à vista visível e CTA. NN/g: 57% da atenção fica ali.
- Preço sempre com total à vista; parcelas como complemento, nunca sozinhas (Decreto 5.903, art. 9º IV). Sem "de/por" enquanto não houver preço anterior praticado e documentado (Conar 27 §3º). Ancore por valor (custo de fazer sozinho, tempo), não por desconto.
- Sem contador, sem "últimas vagas". Se houver prazo, que seja real e expire (Mathur 2019 mostra que timers falsos são o dark pattern mais comum, e a Meta enquadra urgência falsa como prática enganosa). Bônus por prazo é aceitável se o prazo for verdadeiro e registrado.
- Sem depoimentos: substituir por demonstração de tela do produto real, garantia de 7 dias (CDC art. 49 já obriga) ou maior, suporte visível, política clara e link para CNPJ/termos. Coletar avaliações desde a primeira venda; Spiegel mostra que o efeito satura em ~5 avaliações, então a meta inicial é pequena.
- Texto simples (nível 5ª–7ª série), 16 px, linhas de 50–75 caracteres, LCP < 2,5 s. Banner de cookies com "rejeitar" igual ao "aceitar" (ANPD); prever que 30–60% podem recusar o Pixel e usar CAPI com a mesma base legal.
- Sticky CTA no mobile com preço; testar.
- Todo texto de produto e anúncio deve ser comprovável (Conar 27 §1º); "resultados" só como funcionalidade ("calcula X"), nunca como promessa de ganho.

**R$ 27 (impulso, baixo risco)**
- Página curta: herói + 3–5 benefícios concretos + o que vem dentro (lista/prints) + preço + garantia + FAQ curto. A CXL enquadra este caso como "baixo custo, baixo compromisso, motivação de querer": copy curta tende a vencer.
- Herói: GIF/vídeo mudo de 15–30 s mostrando a planilha funcionando. Sem VSL.
- Preço à vista em destaque; Pix como padrão. Parcelamento pouco relevante no ticket.
- Testes: só métricas de funil (clique no CTA, InitiateCheckout); Purchase exige volume que este ticket não paga.

**R$ 197 (decisão ponderada)**
- Página média/longa: herói com demonstração narrada (60–120 s, legendada), problema → mecanismo → o que está incluído (tour por cada planilha/prompt) → para quem é/não é → garantia → preço com três opções (kit básico / kit completo / kit + prompts) usando a versão "ótima" como âncora → FAQ com objeções de compatibilidade (Excel/Google Sheets, celular) → suporte.
- Parcelamento em 12x visível ao lado do total à vista. Desconto Pix opcional, informado antes do checkout (Lei 13.455).
- Prova sem depoimento: números de uso verificáveis (quantidade de fórmulas, abas, horas economizadas *estimadas* com premissas expostas), reputação da plataforma de checkout, garantia estendida.
- Testes: herói vídeo vs. estático; bloco de preço 1 vs. 3 opções; prova acima vs. abaixo.

**R$ 697 (alto risco percebido para o avatar)**
- Página longa e "analítica" (CXL: decisão racional, alto custo). Estrutura: herói com demonstração + resumo do que está incluído; caso de uso completo em vídeo (demonstração passo a passo com voz de IA é aceitável — WPP: paridade de intenção de compra — mas revele que é narração sintética se perguntado e considere um trecho com voz humana para o momento emocional); comparação com alternativas (consultoria, montar do zero); tabela de conteúdo detalhada; garantia mais longa (14–30 dias) e condicional clara; preço com âncora de "ótimo" e plano intermediário; parcelamento 12x em destaque com total à vista; FAQ extenso; suporte humano nominal (e-mail, WhatsApp).
- Sem depoimentos, a confiança precisa vir de transparência: quem está por trás (CNPJ, nome do responsável, canais), amostra gratuita de uma planilha ou prompt (gera lead, alimenta e-mail, e a automação de e-mail converte 1,49% vs. 0,08% de campanha).
- Considere pré-venda (advertorial/conteúdo) antes da página para tráfego frio; a evidência é fraca, mas o racional (educar antes de pedir R$ 697) é o mesmo da CXL para produtos complexos. Trate como teste, não como certeza.
- Testes: aqui o volume de compras será pequeno; otimize por InitiateCheckout e leads da amostra grátis; mudanças em Purchase só com testes sequenciais e paciência de meses.

---

## Fontes

Estrutura e benchmarks
- Unbounce, average conversion rates (Q4/2024): https://unbounce.com/average-conversion-rates-landing-pages/
- Unbounce, What's a good conversion rate (tabela por setor): https://unbounce.com/landing-pages/whats-a-good-conversion-rate/
- NN/g, Scrolling and Attention (2018): https://www.nngroup.com/articles/scrolling-and-attention/
- CXL, Long form or short form: https://cxl.com/blog/long-form-or-short-form/
- CXL, 4 cases where short home pages outperformed: https://cxl.com/blog/4-cases-where-short-home-pages-outperformed-long-home-pages/
- Hotmart, página de vendas (não carregou na pesquisa): https://hotmart.com/pt-br/blog/pagina-de-vendas

Mídia do herói
- Unbounce/Vidyard case study: https://unbounce.com/conversion-rate-optimization/case-study-using-video-to-lift-landing-page-conversion-rate-by-100/
- Wistia, State of Video 2026: https://wistia.com/learn/marketing/video-marketing-statistics
- Vbout (resumo EyeView): https://www.vbout.com/blog/impact-of-video-content-on-landing-page-conversion-rates/
- Science of Learning, talking heads: https://scienceoflearning.substack.com/p/should-instructional-videos-include
- Systematic review, instructor presence: https://www.sciencedirect.com/science/article/pii/S2666557321000306
- WPP Media, AI voices in audio ads (2025): https://www.wppmedia.com/news/ai-voices-audio-ads
- RealVOTalent, AI voice sentiment: https://www.realvotalent.com/ai-voice-sentiment
- 3Play Media, Facebook captions +12%: https://www.3playmedia.com/blog/captions-increase-viewership-for-facebook-video-ads/
- Digiday, 85% sem som: https://digiday.com/media/silent-world-facebook-video/
- Forbes, Verizon Media 69%: https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/

Preço
- Simply Psychology, anchoring (Tversky & Kahneman 1974): https://www.simplypsychology.org/what-is-the-anchoring-bias.html
- Wikipedia, Decoy effect (Ariely/Economist): https://en.wikipedia.org/wiki/Decoy_effect
- DoWhatWorks, strikethrough prices: https://www.dowhatworks.io/blog/do-strikethrough-prices-work
- Voucherify, strikethrough pricing: https://www.voucherify.io/blog/strikethrough-pricing-why-a-single-line-still-drives-conversions
- Uniqodo, was/now pricing (Omnibus): https://www.uniqodo.com/glossary/what-is-strikethrough-pricing
- HBR, Good-Better-Best (2018): https://hbr.org/2018/09/the-good-better-best-approach-to-pricing
- E-Commerce Brasil / Nuvemshop, Pix ou cartão: https://www.ecommercebrasil.com.br/noticias/pix-ou-cartao-dados-mostram-como-o-brasileiro-paga-no-comercio-eletronico
- PagBrasil, desconto Pix: https://www.pagbrasil.com/pt-br/blog/pix/desconto-para-metodo-de-pagamento-pix/
- Planalto, Lei 13.455/2017: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13455.htm
- Planalto, Lei 10.962/2004: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.962.htm
- Justia, Decreto 5.903/2006: http://brasil.justia.com/nacionales/decretos/5-903-de-20-9-2006/gdoc/
- Modelo Inicial, Decreto 5.903 art. 9: https://modeloinicial.com.br/lei/DEC-5903-2006/decreto-5903/art-9
- Agência Brasil, Procon-SP Black Friday 2024: https://agenciabrasil.ebc.com.br/economia/noticia/2024-11/procon-sp-recebeu-no-ultimo-mes-2-mil-reclamacoes-relacionadas-bla
- InvestNews, Procon Black Friday 2025: https://investnews.com.br/financas/black-friday-2025-10-duvidas/
- Metrópoles, lista Procon-SP: https://www.metropoles.com/negocios/procon-sp-tem-lista-de-78-sites-que-devem-ser-evitados-na-black-friday
- Terra, lista Procon-SP 2025: https://www.terra.com.br/especiais/black-friday/black-friday-2025-conheca-a-lista-do-procon-sp-com-sites-a-serem-evitados,b6b12d097223c1adbbb076965e230096co9dhsm0.html

Urgência, CDC, Conar, Meta
- CXL, Creating urgency: https://cxl.com/blog/creating-urgency/
- Mathur et al., Dark Patterns at Scale (2019): https://arxiv.org/pdf/1907.07032
- UChicago, resumo do estudo: https://cs.uchicago.edu/news/dark-patterns/
- LiquidBoost, countdown data: https://liquidboost.app/blog/countdown-timer-conversion-data
- Meta, Unacceptable Business Practices: https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/
- Meta, Introduction to Advertising Standards: https://transparency.meta.com/policies/ad-standards/
- Meta, Low Quality or Disruptive Content (help): https://www.facebook.com/business/help/617541753336634
- Meta, Clickbait links: https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/clickbait-links/
- Meta, Engagement bait: https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/engagement-bait/
- Jon Loomer, low-quality post-click: https://www.jonloomer.com/low-quality-ad-content-and-post-click-experiences/
- Modelo Inicial, CDC art. 6: https://modeloinicial.com.br/lei/CDC/codigo-defesa-consumidor/art-6
- Jusbrasil, CDC art. 37: https://www.jusbrasil.com.br/topicos/10603148/artigo-37-da-lei-n-8078-de-11-de-setembro-de-1990
- Modelo Inicial, CDC art. 39: https://modeloinicial.com.br/lei/CDC/codigo-defesa-consumidor/art-39,inc-X
- Código Conar (PDF Secom): https://www.gov.br/secom/pt-br/acesso-a-informacao/legislacao/ca2digobrasdeautoregulanovo.pdf
- Conar, código online: http://www.conar.org.br/codigo/codigo.php
- Walmar Andrade, publicidade enganosa de infoprodutos: https://walmarandrade.com.br/publicidade-enganosa-infoprodutos/
- IstoÉ Dinheiro, Procon-SP x Empiricus: https://istoedinheiro.com.br/procon-sp-multa-empiricus-por-propaganda-enganosa
- MPMG, Procon-MG x Estácio: https://www.mpmg.mp.br/portal/menu/comunicacao/noticias/procon-mg-multa-faculdade-estacio-de-sa-por-propaganda-enganosa.shtml
- Agência Brasília, Procon-DF fecha empresa de cursos: https://www.agenciabrasilia.df.gov.br/w/procon-fecha-empresa-que-vendia-cursos-com-falsa-garantia-de-emprego-a-jovens-do-df
- Maia Yoshiyasu, influenciadora condenada: https://mylaw.com.br/2024/02/26/influenciadora-e-condenada-por-publicidade-enganosa-em-curso-online-como-se-prevenir/
- Meio & Mensagem, mais punidos pelo Conar em 2025: https://www.meioemensagem.com.br/comunicacao/confira-os-anunciantes-mais-punidos-pelo-conar-em-2025

Prova social e confiança
- Spiegel Research Center: https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/
- VWO, WikiJob: https://vwo.com/success-stories/wikijob/
- BrightLocal 2026 (resumo): https://gbppromote.com/local-consumer-review-survey/
- Reclame AQUI, 81,54% leem reviews: https://blog.reclameaqui.com.br/varejo-consumidores-leem-reviews-antes-de-comprar/
- Terra, reputação digital (CX Trends): https://www.terra.com.br/noticias/reputacao-digital-se-torna-decisiva-na-jornada-de-compra,04dca87fa63a1e53437dada8ab4f71efkaugmj4i.html
- Baymard, perceived security: https://baymard.com/blog/perceived-security-of-payment-form
- Baymard, cart abandonment rate: https://baymard.com/lists/cart-abandonment-rate
- CXL, trust seals research: https://cxl.com/research-study/trust-seals/
- Reclame AQUI, Kiwify: https://www.reclameaqui.com.br/empresa/kiwify/
- Hotmart, indicador de satisfação: https://help.hotmart.com/pt-br/article/115006174067/o-que-e-o-indicador-de-satisfacao-no-mercado-
- Hotmart Ask: https://help.hotmart.com/pt-br/article/360030387292/hotmart-ask-o-que-e-e-como-configurar

UX mobile e performance
- Deloitte, Milliseconds Make Millions: https://www.deloitte.com/ie/en/services/consulting/research/milliseconds-make-millions.html
- web.dev, Milliseconds make millions: https://web.dev/case-studies/milliseconds-make-millions
- Akamai, Spring 2017 report: https://www.akamai.com/newsroom/press-release/akamai-releases-spring-2017-state-of-online-retail-performance-report
- Portent, site speed: https://portent.com/blog/analytics/research-site-speed-hurting-everyones-revenue.htm
- web.dev, CWV thresholds: https://web.dev/articles/defining-core-web-vitals-thresholds
- GrowthRock, sticky add to cart: https://growthrock.co/sticky-add-to-cart-button-example/
- Convertibles, sticky CTA +20,4%: https://convertibles.dev/blogs/case-studies/homepage-sticky-cta-case-study
- Blend Commerce, sticky CTA +7,17%: https://blendcommerce.com/blogs/ab-tests-shopify/7-17-increase-in-conversion-rate
- Baymard, line length: https://baymard.com/blog/line-length-readability
- NN/g, glanceable fonts: https://www.nngroup.com/articles/glanceable-fonts/
- Chrome Developers, font-size audit: https://developer.chrome.com/docs/lighthouse/seo/font-size
- Lighthouse PR #4550: https://github.com/googlechrome/lighthouse/pull/4550
- Frisbii, checkout fields: https://frisbii.com/blog/6-best-practices-to-increase-checkout-conversion-rates/
- ignite.video, 29 estudos sobre cookie banners: https://www.ignite.video/en/articles/basics/cookie-consent-studies
- ClearAnalytics, cookie banners e conversão: https://clearanalytics.eu/blog/cookie-consent-banners-are-killing-your-conversion-rate
- ANPD, Guia de cookies (PDF): https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf/@@display-file/file

Anúncio ↔ página
- Unbounce, Message match: https://unbounce.com/conversion-glossary/definition/message-match/
- Fibr, message match: https://fibr.ai/blog/the-landing-page-puzzle-how-message-match-creates-the-perfect-fit
- Meta, About Ad Relevance Diagnostics: https://www.facebook.com/business/help/403110480493160
- Meta, How to use Ad Relevance Diagnostics: https://www.facebook.com/business/help/436113280262012
- Meta, Attributes to avoid: https://www.facebook.com/business/help/1767120243598011
- Chui, rankings explicados: https://chui.substack.com/p/facebook-ads-quality-engagement-and
- Landerlab, advertorials: https://landerlab.io/blog/advertorial-landing-page-3-examples
- Convertibles, advertorial examples: https://convertibles.dev/blogs/optimization/examples-of-advertorials
- Splitbase, landing page types: https://splitbase.com/blog/landing-page-types

Testes e benchmarks
- GoodUI, previsibilidade: https://goodui.org/blog/can-winning-a-b-tests-be-predicted-with-past-results/
- GoodUI, priorização: https://goodui.org/blog/better-experiments-prioritize-ab-tests-to-maximize-your-win-rate/
- Optimizely, 101 things to test: https://www.optimizely.com/insights/blog/101-things-to-ab-test/
- VWO, A/B testing examples: https://vwo.com/blog/ab-testing-examples/
- Evan Miller, sample size: https://www.evanmiller.org/ab-testing/sample-size.html
- Evan Miller, sequential: https://www.evanmiller.org/ab-testing/sequential.html
- CXL, A/B test calculator: https://cxl.com/ab-test-calculator/
- GuessTheTest, sample size: https://guessthetest.com/calculating-sample-size-in-a-b-testing-everything-you-need-to-know/
- Atticus Li, sample size guide: https://atticusli.com/blog/posts/ab-test-sample-size-guide/
- Invesp, sample size: https://www.invespcro.com/blog/calculating-sample-size-for-an-ab-test/
- ABTasty, sample size: https://www.abtasty.com/blog/sample-size-calculation/
- WordStream, Facebook Ads Benchmarks 2025: https://www.wordstream.com/blog/facebook-ads-benchmarks-2025
- Superscale, resumo WordStream 2026 (Meta): https://superscale.ai/learn/meta-ads-benchmarks-by-industry/
- WordStream, Google Ads Benchmarks 2026: https://www.wordstream.com/blog/2026-google-ads-benchmarks
- Omnisend, email benchmarks: https://www.omnisend.com/blog/email-marketing-benchmarks/
- Klaviyo, benchmarks: https://www.klaviyo.com/products/email-marketing/benchmarks
- Trafius, metas de conversão Meta Ads BR: https://trafius.com.br/blog/taxa-de-conversao-de-landing-page-pra-meta-ads-metas-realistas
