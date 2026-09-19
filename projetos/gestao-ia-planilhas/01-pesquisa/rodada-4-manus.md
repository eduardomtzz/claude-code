# Relatório da Quarta Rodada — Página de Vendas, Checkout e Pós-compra

| **[F] Metadado** [2] | **[F] Valor** [2] |
|---|---|
| **[F] Marca** [1] | **[F] Seu Sócio Gestor.** [1] |
| **[F] Data de corte** [1] | **[F] 12/09/2026.** [1] |
| **[F] Escopo** [1] | **[F] Página de vendas, prova, mídia, UX mobile, preço, conformidade, checkout, pagamentos, recuperação e pós-compra para três ofertas digitais autoguiadas.** [1] |
| **[F] Base documental** [2] | **[F] Briefing e todos os dossiês `research/`, `platforms/` e `references/` da rodada, confrontados com fontes primárias citadas.** [2] [3] [4] |

## Resumo executivo

**[F]** O portfólio contém três faixas: **R$ 27–47**, **R$ 197–297** e **R$ 497–697**; a aquisição prevista é majoritariamente móvel via Meta Ads e Google, a entrega é automática e os vídeos devem ser faceless, com demonstração de tela ou infográfico, narração por IA e legenda. [1]

**[F]** Não existe evidência pública que determine um comprimento vencedor por faixa de preço: páginas longas e curtas venceram em contextos distintos, e os testes publicados alteraram frequentemente mais de um componente. [16] [17] **[E]** A primeira versão deve crescer em densidade de explicação conforme preço, complexidade e objeções, mas essa progressão é hipótese a testar, não regra causal. [16]

**[F]** O lançamento não possui depoimentos. [1] **[E]** A prova inicial deve vir de telas reais, amostra funcional, inventário verificável, demonstração completa e identificação do fornecedor; beta, contadores de uso e avaliações só entram quando houver dado real, definição auditável e autorização. [18] [7]

**[F]** A operação precisa exibir preço e adicionais, forma e prazo de disponibilização, identificação e contato do fornecedor, resumo contratual e meio claro para arrependimento; o CDC prevê **7 dias** nas contratações fora do estabelecimento. [7] [8] [9] **[F]** A LGPD e a orientação da ANPD exigem finalidade, necessidade, transparência, escolha real, rejeição fácil de cookies não necessários e revogação facilitada. [11] [12]

**[F]** As políticas da Meta alcançam anúncio e destino e vedam práticas comerciais enganosas. [13] [14] **[E]** Preço, promessa, prazo, bônus, empresa e produto devem coincidir entre criativo, landing page e checkout; aprovação do anúncio não valida uma alegação. [13] [14]

**[F]** As sete opções auditadas são **Kiwify, Hotmart, Cakto, Ticto, Eduzz, Stripe e Mercado Pago**, com Stripe e Mercado Pago tratados separadamente. [58] [59] [60] [61] [62] [63] [64] **[E]** Para uma operação autoguiada que quer área de membros e pós-compra prontos, Kiwify, Hotmart, Cakto, Ticto ou Eduzz reduzem integrações; Stripe e Mercado Pago exigem LMS, afiliados e parte da automação fora do gateway. [58] [59] [60] [61] [62] [63] [64]

**[ND]** Não há benchmark público confiável de conversão, abandono, aprovação, recuperação, aceite de bump, upsell ou reembolso simultaneamente por **ticket, método e produto digital brasileiro**. [19] **[F]** Os números internacionais e de comércio eletrônico geral deste relatório são rotulados como não equivalentes e não se tornam metas do negócio. [19]

## Método de auditoria e legenda

| **[F] Rótulo** [2] | **[F] Definição aplicada** [2] |
|---|---|
| **[F] F** [2] | **[F] Fato diretamente sustentado por fonte primária, documento oficial, página observada ou artefato reproduzível citado.** [2] [3] [4] |
| **[F] E** [2] | **[F] Estimativa, cálculo, hipótese, recomendação ou transferência limitada de evidência, sempre identificada como tal.** [2] [3] [4] |
| **[F] ND** [2] | **[F] Não divulgado, não determinável publicamente ou conflitante sem resolução oficial; lacunas não foram preenchidas por analogia.** [2] [3] [4] |

**[F]** Foram abertas por `curl` **28 URLs** de uma amostra priorizada de leis, políticas, taxas e estudos; todas responderam com status HTTP abaixo de 400 na verificação de **12/09/2026**, sem que isso garanta permanência futura do conteúdo. [5] **[F]** Os percentuais de taxas e cenários A/B foram recalculados por script, com arredondamento e limitações documentados. [6]

# PARTE 1. ANATOMIA DA PÁGINA DE VENDAS

## 1.1. Estrutura, primeira dobra e comprimento por faixa

**[F]** Um estudo de atenção em desktop registrou **57%** do tempo acima da dobra e **74%** nos dois primeiros screenfuls, sem medir compra nem reproduzir o contexto móvel brasileiro. [16] **[F]** Em teste de usabilidade, **6 de 8** participantes não perceberam a rolagem quando o hero pareceu uma página completa; a amostra é diagnóstica, não um benchmark de conversão. [20]

**[F]** Em testes publicados, uma página longa da Highrise elevou cadastros líquidos em **37,5%** com mais de **42 mil visitantes**, enquanto uma versão mais curta do TruckersReport elevou opt-ins em **21,5%** com confiança declarada de **99,6%**; os contextos, métricas e mudanças não são equivalentes. [21] [17]

| **[F] Faixa** [2] | **[E] Primeira versão** [2] | **[E] Ordem proposta** [2] | **[ND] Limite da evidência** [2] |
|---|---|---|---|
| **[F] R$ 27–47.** [1] | **[E] Concisa, suficiente para entender produto, entrega e risco.** [16] | **[E] Hero → demonstração → itens → situações de uso → adequação → preço/7 dias → FAQ → rodapé.** [16] | **[ND] Não há número ideal de palavras, pixels ou seções para o ticket.** [16] |
| **[F] R$ 197–297.** [1] | **[E] Intermediária, com mecanismo, demonstração e objeções.** [16] | **[E] Hero → problema operacional → fluxo → demo → inventário → adequação → preço/7 dias → FAQ → rodapé.** [16] | **[ND] A relação entre preço e comprimento não foi isolada em experimento brasileiro.** [16] |
| **[F] R$ 497–697.** [1] | **[E] Explicativa e escaneável, com inventário e limites completos.** [16] | **[E] Hero vertical → prova → cinco núcleos → demos → vinte planilhas → manual/prompts → adequação → objeções → preço/7 dias → FAQ.** [1] [16] | **[ND] Mais preço não prova causalmente que mais texto converterá melhor.** [16] |

**[E]** O hero deve mostrar marca, tarefa, entregável, público, imagem/poster leve e uma ação; o início do próximo bloco deve permanecer visível para evitar “falso fim”. [16] [20] **[E]** O CTA no hero deve ser testado contra uma âncora para conteúdo, porque CTA acima e abaixo da dobra já venceram em contextos diferentes. [16] [22]

## 1.2. Headline e subheadline

**[F]** Páginas reais de templates frequentemente colocam tarefa, utilidade e formato antes da tecnologia. [65] [66] **[E]** A fórmula inicial é **verbo de uso + objeto gerencial + artefato pronto + fricção removida**, seguida de subheadline com conteúdo, compatibilidade, acesso e limite. [23]

| **[F] Oferta** [2] | **[E] Headline de controle** [2] | **[E] Subheadline de controle** [2] |
|---|---|---|
| **[F] Kit IA no Trabalho, R$ 27–47.** [1] | **[E] “Organize tarefas recorrentes com prompts e planilhas prontas para adaptar.”** [1] [23] | **[E] “Receba três planilhas e um kit de prompts, com acesso automático e uso autoguiado.”** [1] |
| **[F] IA no Trabalho, R$ 197–297.** [1] | **[E] “Preencha os dados e acompanhe o trabalho em planilhas, relatórios e apresentações.”** [1] [23] | **[E] “São dez planilhas, prompts e aulas curtas, com exemplos de entrada e saída.”** [1] |
| **[F] Kit vertical, R$ 497–697.** [1] | **[E] “Um sistema de gestão em planilhas para a rotina de [profissão].”** [1] | **[E] “Vinte planilhas em cinco núcleos, manual, demonstrações e prompts de IA; produto autoguiado.”** [1] |

**[ND]** A afirmação “na metade do tempo” aparece no nome da oferta intermediária, mas o briefing não apresenta ensaio que comprove redução de **50%**. [1] **[E]** Até existir medição reproduzível, a copy deve mostrar o mecanismo e evitar quantificar economia de tempo. [7]

**[F]** Exemplos reais úteis incluem “Quanto cobrar por pessoa sem descobrir o prejuízo depois do retiro”, em português, e “Keeps track of your customers and clients”, em inglês; são referências de clareza, não provas de conversão. [67] [68]

## 1.3. Mídia do hero: mockup, loop, vídeo e tour

| **[F] Formato** [2] | **[E] Papel recomendado** [2] | **[F] Evidência e limite** [2] |
|---|---|---|
| **[F] Mockup/poster.** [23] | **[E] Fallback leve que mostra o conjunto; deve ser seguido de tela legível.** [23] | **[F] É estável e previsível; [ND] não prova fluxo nem atualização.** [23] |
| **[F] Loop WebM/MP4.** [24] | **[E] Mostrar uma entrada e uma reação curta, com pausa e poster.** [24] | **[F] Um exemplo técnico caiu de 3,7 MB em GIF para 551 KB em MP4 e 341 KB em WebM; [ND] não é média universal.** [24] |
| **[F] Vídeo por toque.** [25] | **[E] Prova central com resultado, três passos e CTA, sempre legendada.** [25] | **[ND] Não há duração vencedora para planilhas brasileiras; testar versões de 35–55 s e 3–6 min como faixas experimentais.** [25] |
| **[F] Tour interativo.** [26] | **[E] Segunda camada opcional, curta e sem gate inicial.** [26] | **[F] O relatório do fornecedor analisou mais de 28 mil demos, mas seleciona o próprio ecossistema e não é randomizado.** [26] |

**[F]** A Meta recomenda compreensão sem som, e o W3C exige legendas sincronizadas em mídia pré-gravada com áudio, salvo exceção de alternativa textual equivalente. [27] [28] **[E]** A narração por IA deve ter revisão humana, pronúncia testada e legenda integral; vídeos reais analisados não validaram voz sintética como superior. [23]

## 1.4. Como mostrar planilhas e prompts

| **[E] Bloco** [2] | **[E] Execução** [2] | **[E] Controle de integridade** [2] |
|---|---|---|
| **[E] Resultado primeiro.** [23] | **[E] Abrir com painel preenchido e alterar uma entrada.** [23] | **[E] Manter a reação na tela; não mostrar somente o estado final.** [23] |
| **[E] Uma ação por cena.** [23] | **[E] Recortar campo, clique e saída; usar cursor, zoom e legenda.** [23] | **[E] Não reduzir uma captura desktop inteira a 9:16.** [23] |
| **[E] Inventário.** [65] [66] | **[E] Nomear cada arquivo, tarefa, entrada, saída, formato e compatibilidade.** [65] [66] | **[E] Não esconder limitações em miniaturas ilegíveis.** [7] |
| **[E] Prompt.** [23] | **[E] Mostrar contexto, comando e saída rotulada como exemplo.** [23] | **[E] Informar que saídas de IA variam e exigem revisão.** [23] |
| **[E] Antes/depois organizacional.** [1] | **[E] Comparar informação dispersa com estrutura organizada.** [1] | **[E] Não converter organização em promessa de renda, saúde ou desempenho profissional.** [1] [7] |

**[F]** O benchmark de quinze páginas reais na Parte 7 mostra uso recorrente de previews, demos, screenshots e inventários, mas nenhuma publica teste que prove conversão do layout. [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [79]

## 1.5. Preço, âncora, Pix, parcelamento e planos

**[F]** A oferta deve mostrar preço total à vista; em pagamento parcelado, deve informar quantidade, periodicidade, valor, juros/acréscimos e total aplicável. [7] [9] **[F]** Preço diferente por instrumento de pagamento é permitido, desde que o desconto seja informado de forma visível. [10]

| **[E] Ordem no bloco** [2] | **[E] Conteúdo** [2] | **[F] Regra** [2] |
|---:|---|---|
| **[E] 1.** [8] | **[E] Nome da oferta e “compra única” ou recorrência real.** [8] | **[F] Características e condições integram a oferta.** [7] [8] |
| **[E] 2.** [9] | **[E] Preço total à vista como informação primária.** [9] | **[F] Informar só a parcela é insuficiente.** [9] |
| **[E] 3.** [10] | **[E] Total no Pix e desconto exato, se real.** [10] | **[F] A diferenciação por método deve ser visível.** [10] |
| **[E] 4.** [7] [9] | **[E] Parcelas, juros e total parcelado.** [7] [9] | **[F] O consumidor não deve precisar calcular o total.** [9] |
| **[E] 5.** [8] | **[E] CTA, forma e prazo de disponibilização.** [8] | **[F] Disponibilidade e entrega devem ser informadas.** [8] |
| **[E] 6.** [7] [8] | **[E] Direito de arrependimento de 7 dias e canal.** [7] [8] | **[F] A confirmação do pedido de cancelamento deve ser imediata.** [8] |

**[F]** Preço riscado enganoso ou omissão capaz de induzir erro é publicidade enganosa, e o anunciante deve provar a correção da mensagem. [7] **[E]** Só use “de/por” com histórico defensável por data, canal e vigência; sem histórico, use preço atual ou condição de lançamento com término real. [7] [29]

**[F]** Um estudo de parcelamento com **391 participantes** encontrou gasto médio de **US$ 89,42** em quatro parcelas contra **US$ 77,46** em pagamento integral adiado, com _p_=0,001 e _d_=0,33; o país da amostra não foi informado no trecho e o resultado não é benchmark brasileiro. [29] **[E]** Parcela pode ganhar saliência, mas o total deve permanecer explícito. [9]

**[E]** Só compare planos materialmente distintos; em mobile, apresente até duas opções simultâneas ou cartões seletáveis. [30] **[ND]** “Três planos” e “mais escolhido” não têm efeito garantido, e o segundo rótulo exige dado auditável. [30] [7]

## 1.6. Garantia, FAQ, adequação, bônus, selo, CNPJ e contato

**[F]** O CDC prevê **7 dias** para desistência em contratação fora do estabelecimento, e o Decreto nº 7.962/2013 exige meio claro, eficaz e disponível pela mesma ferramenta da contratação. [7] [8] **[E]** A página deve chamar o bloco de “Direito de arrependimento de 7 dias”, sem vender o mínimo legal como privilégio excepcional. [7] [8]

**[E]** O FAQ deve responder compra única/assinatura, conteúdo e exclusões, compatibilidade, pré-requisitos, entrega, suporte, Pix/parcelas e arrependimento; condições materiais ficam visíveis também fora do acordeão. [7] [8]

**[E]** “Para quem é” descreve situação e autonomia de uso; “para quem não é” afasta quem espera serviço feito, contato humano, personalização ou resultado garantido. [1] [7] **[E]** Bônus deve ser distinto, real e elegível; valor monetário só quando houver preço separadamente praticado. [7] [29]

**[F]** O comércio eletrônico deve exibir nome empresarial, CPF/CNPJ quando aplicável, endereço físico e eletrônico e meios de contato. [8] **[E]** Selos só podem representar emissor, escopo e validade reais; HTTPS, processador identificado e microcopy verdadeira são preferíveis a “paredes” de ícones. [31] [7]

## 1.7. Urgência e escassez legítimas

| **[E] Tática** [2] | **[E] Condição legítima** [2] | **[E] Evidência a guardar** [2] | **[E] Não fazer** [2] |
|---|---|---|---|
| **[E] Preço de lançamento.** [7] | **[E] Data/hora e preço posterior reais.** [7] | **[E] Regra de sistema, fuso, versão e histórico.** [7] | **[E] Reiniciar contador ou manter a oferta igual.** [14] [32] |
| **[E] Bônus por prazo.** [8] | **[E] O bônus deixa de ser incluído após a data.** [8] | **[E] Inventário antes/depois e elegibilidade.** [8] | **[E] Prorrogar silenciosamente.** [14] |
| **[E] Lote/capacidade.** [7] | **[E] Há limite humano ou técnico mensurável.** [7] | **[E] Capacidade sincronizada e motivo operacional.** [7] | **[E] Alegar vagas limitadas para entrega ilimitada.** [14] |
| **[E] Fechamento.** [8] | **[E] O checkout realmente deixa de aceitar compras.** [8] | **[E] Data, hora, fuso e log de fechamento.** [8] | **[E] Reabrir imediatamente como padrão perene.** [32] |

**[F]** Em experimento mobile chinês com **22.084 usuários** randomizados, incentivo e escassez tiveram efeitos diferentes conforme existência de carrinho; o estudo tratou varejo físico e SMS, não produto digital brasileiro. [32] **[E]** O achado sustenta testar eventos reais por estágio, não fabricar estoque. [32] [14]

# PARTE 2. PROVA SOCIAL SEM CLIENTES

## 2.1. Estratégias éticas no lançamento

| **[E] Estratégia** [2] | **[E] Execução inicial** [2] | **[F] Evidência e limite** [2] |
|---|---|---|
| **[E] Demonstração pública.** [18] | **[E] Rota sem cadastro com tarefa completa, saída concreta e limitações.** [18] | **[ND] Não há uplift brasileiro isolado; amostras digitais podem ajudar em outros contextos.** [18] |
| **[E] Beta documentado.** [18] | **[E] Informar N, período, critério, versão e ajustes; incentivo independe da nota.** [18] | **[ND] Não há A/B que isole o rótulo beta.** [18] |
| **[E] Prova de uso.** [18] | **[E] Publicar somente eventos reais com unidade, período, deduplicação e atualização.** [18] | **[F] Contagens alteraram escolhas em experimentos, mas não provaram aumento líquido de vendas.** [18] |
| **[E] Autoridade documental.** [18] | **[E] Citar fonte, data, população e limite junto da alegação.** [18] | **[ND] Não há efeito causal de citações em checkout mobile.** [18] |
| **[E] Avaliação verificada.** [18] | **[E] Associar internamente a compra, exibir data/versão e autorização.** [18] | **[F] A Hotmart oferece pesquisa e componente de avaliações; [ND] não publica uplift.** [33] [34] |

**[E]** A escada de evidência é: existência do produto → utilidade observável → beta → uso real → avaliações verificadas. [18] **[ND]** Os percentuais internacionais de reviews ou trial não devem ser tratados como meta brasileira. [18]

## 2.2. Coleta automática, consentimento e LGPD

**[F]** A Hotmart documenta Hotmart Ask e avaliações na página de pagamento. [33] [34] **[F]** A Kiwify documenta integrações por evento com ActiveCampaign/Mailchimp e webhooks, mas não confirma coletor nativo público de avaliações no checkout. [35] [36]

| **[E] Etapa** [2] | **[E] Regra operacional** [2] | **[F] Base** [2] |
|---:|---|---|
| **[E] 1. Elegibilidade.** [35] | **[E] Compra aprovada, não reembolsada e uso mínimo definido antes do convite.** [35] | **[F] Eventos de compra podem alimentar automações.** [35] [36] |
| **[E] 2. Convite.** [11] | **[E] Um convite relacionado à experiência, com opt-out; newsletter e upsell ficam separados.** [11] | **[F] Finalidade, necessidade e transparência são princípios da LGPD.** [11] |
| **[E] 3. Formulário.** [11] | **[E] Separar avaliação privada, autorização de texto, nome público, foto/voz, canais e revogação.** [11] | **[F] Consentimento deve ser livre, informado, inequívoco e para finalidade determinada.** [11] |
| **[E] 4. Publicação.** [18] | **[E] Guardar original, recorte aprovado, versão, data, incentivo e status de revogação.** [18] | **[F] Testemunhal publicitário deve ser genuíno e comprovável.** [37] |
| **[E] 5. Retirada.** [11] | **[E] Canal simples e SLA interno para retirar vitrine e mídia futura.** [11] | **[F] O consentimento pode ser revogado por procedimento gratuito e facilitado.** [11] |

**[E]** Texto operacional: “Autorizo opcionalmente a publicação do meu comentário, identificado como [opção], nos canais [lista], sem alteração de sentido; posso revogar em [contato].” [11] [37]

## 2.3. O que não fazer e casos brasileiros

**[F]** Depoimento inventado, modelo apresentado como cliente, número sem fonte, edição que muda sentido, endosso inexistente e resultado improvável entram em conflito com CDC, CONAR ou políticas de anúncio. [7] [37] [14]

| **[F] Caso** [2] | **[F] Conduta/medida documentada** [2] | **[E] Aplicação** [2] |
|---|---|---|
| **[F] Diletto/Senacon, 2019.** [38] | **[F] História de origem inverídica apresentada como real; multa definitiva de R$ 100.000,00, reduzida para R$ 92.039,25 após dedução registrada.** [38] | **[E] Não fabricar fundador, tradição, personagem ou história “real”.** [38] |
| **[F] Empiricus/Bettina/Procon-SP, 2019.** [39] | **[F] A representação registrou omissão de aportes e falta de comprovação; a fonte consultada não prova decisão criminal final nem multa final.** [39] | **[E] Um número verdadeiro pode enganar quando omite base, aportes ou causalidade.** [39] |
| **[F] Curso online/TJSP, 2025.** [40] | **[F] Promessa de rendimento mínimo diário; ressarcimento de R$ 829 e dano moral de R$ 5.000.** [40] | **[E] Reembolso não neutraliza promessa de resultado.** [40] |

**[ND]** Não foi localizado precedente primário aberto que usasse exatamente a expressão “foto de banco apresentada como cliente”; isso não cria permissão, porque testemunhal falso e uso comercial de imagem sem autorização já são vedados. [37] [41]

# PARTE 3. UX, UI E PERFORMANCE MOBILE

## 3.1. UX que reduz fricção

**[E]** A interface deve funcionar em **320 CSS px**, zoom de **200%**, ordem DOM coerente, teclado e leitor de tela. [42] **[F]** WCAG 2.2 AA exige contraste de **4,5:1** para texto normal e **3:1** para texto grande; o mínimo de alvo do critério 2.5.8 é **24 × 24 CSS px**, enquanto **48 × 48 px** é recomendação prática mais confortável. [42]

**[F]** Uma revisão de **33** experimentos com elementos fixos encontrou **9** vencedores, **6** perdedores e **18** inconclusivos; amostras e efeitos por teste não foram publicados. [43] **[F]** Em um A/B mobile de **14 dias** com mais de **3.000 pedidos por variante**, o painel inferior elevou pedidos em **5,2%**, enquanto apenas rolar até a área de compra não mudou significativamente a conversão. [44] **[E]** CTA fixa é hipótese, não padrão obrigatório. [43] [44]

**[E]** Use uma coluna, texto escaneável, mesma ação nas CTAs repetidas, âncoras descritivas em páginas longas, poster e play explícito, vídeo mudo por padrão e controles que não cubram conteúdo. [42] **[ND]** Não há frequência universal de CTA, largura vencedora, fonte vencedora nem uplift brasileiro desses componentes. [42]

## 3.2. Core Web Vitals, conversão e mídia paga

| **[F] Métrica** [2] | **[F] Bom no p75** [2] | **[F] Precisa melhorar** [2] | **[F] Ruim** [2] |
|---|---:|---:|---:|
| **[F] LCP.** [45] | **[F] ≤ 2,5 s.** [45] | **[F] > 2,5 s e ≤ 4,0 s.** [45] | **[F] > 4,0 s.** [45] |
| **[F] INP.** [45] | **[F] ≤ 200 ms.** [45] | **[F] > 200 ms e ≤ 500 ms.** [45] | **[F] > 500 ms.** [45] |
| **[F] CLS.** [45] | **[F] ≤ 0,1.** [45] | **[F] > 0,1 e ≤ 0,25.** [45] | **[F] > 0,25.** [45] |

**[F]** Em A/B da Vodafone, uma versão com LCP **31%** melhor registrou **8%** mais vendas; o caso não publica duração nem intervalos de confiança e não é brasileiro. [46] **[F]** Em A/B de um mês da Rakuten 24, várias métricas melhoraram e a conversão subiu **33,13%**, mas o volume absoluto não foi publicado e não se isola um único vital. [47]

**[F]** A Meta define visualização de página de destino como clique seguido de carregamento bem-sucedido; não publica limiar de LCP que determine CPM ou custo. [15] **[F]** O Google considera experiência de destino no diagnóstico, mas o Índice de qualidade não é KPI nem entrada direta do leilão. [48] **[ND]** Não existe fórmula pública que converta LCP em CPA da Meta ou CPC do Google. [15] [48]

**[E]** Priorize resposta HTML, recurso LCP descobrível e sem lazy load, redução de JavaScript, dimensões reservadas e lazy loading apenas fora da dobra; valide em RUM e use laboratório para diagnóstico. [45]

## 3.3. Cookies, LGPD, Pixel, CAPI e Consent Mode

| **[F] Estado** [2] | **[E] Pixel/CAPI** [2] | **[E] Google tags** [2] | **[E] Relatório** [2] |
|---|---|---|---|
| **[F] Sem resposta.** [12] | **[E] Manter Pixel revogado e não enviar evento publicitário por CAPI.** [49] | **[E] Básico bloqueado; avançado só após avaliação jurídica e transparência sobre pings.** [50] | **[E] Registrar apenas CMP e telemetria estritamente necessária; omissão não é aceite.** [12] |
| **[F] Rejeitou.** [12] | **[E] Manter revogado e não usar servidor como bypass.** [49] | **[E] Estados pertinentes em `denied`; separar modelado de observado.** [50] | **[E] Backend transacional continua sendo fonte de verdade da compra.** [49] |
| **[F] Aceitou publicidade.** [12] | **[E] Conceder, minimizar e deduplicar `event_name`/`event_id`.** [49] | **[E] Atualizar os quatro estados pertinentes.** [50] | **[E] Conciliar observado, modelado e backend.** [50] |
| **[F] Revogou.** [11] | **[E] Revogar e interromper envios futuros da finalidade.** [11] [49] | **[E] Atualizar imediatamente para `denied`.** [50] | **[E] Guardar trilha de revogação.** [11] |

**[F]** A ANPD recomenda no primeiro nível aceitar, rejeitar cookies não necessários e gerenciar preferências com visibilidade comparável; cookies baseados em consentimento devem iniciar desligados. [12] **[F]** Em estudo alemão com **82.890 visitantes**, posição e nudges alteraram fortemente a interação; em outro estudo, ocultar “rejeitar todos” elevou aceite em cerca de **22–23 pontos percentuais**, um efeito de dark pattern, não meta legítima. [51] [52]

**[F]** A CAPI não foi criada para contornar privacidade, e Pixel/CAPI exigem deduplicação quando enviam o mesmo evento. [49] **[F]** O Consent Mode avançado envia pings sem cookies quando negado; “sem cookies” não significa “sem tratamento de dados”. [50]

## 3.4. Padrão visual profissional versus estética de “guru”

| **[E] Preferir** [2] | **[E] Evitar** [2] |
|---|---|
| **[E] Tela real, inventário, navegação por tarefa, tipografia sóbria, informação de escopo e prova junto da alegação.** [65] [69] [70] | **[E] Mockup ilegível, superlativo sem fonte, bônus inflado, múltiplos contadores, brilho sem função e depoimento cenográfico.** [7] [37] |
| **[E] Um CTA principal, preço total, documentação e contato visíveis.** [8] [9] | **[E] Muitas rotas concorrentes, condição material escondida e urgência perene.** [14] [32] |
| **[E] Identidade adequada à vertical e demonstração de dados fictícios identificados.** [1] | **[E] Simular prontuário, processo ou cliente real sem base e autorização.** [11] [37] |

**[ND]** “Profissional” e “guru” são categorias editoriais, não classes de desempenho validadas; o que pode ser auditado é clareza, legibilidade, veracidade, consistência e adequação. [2] [3]

# PARTE 4. CHECKOUT E PÓS-COMPRA

## 4.1. Sete opções de pagamento/plataforma

**[F]** Todas as taxas abaixo foram consultadas em **12/09/2026**; a data editorial é indicada quando a fonte a publica. [58] [59] [60] [61] [62] [63] [64] **[E]** Valores negociados, condições por conta, parcelamento, antecipação, saque, afiliados, fiscal, reembolso e chargeback devem permanecer separados da taxa-base. [58] [59] [60] [61] [62] [63] [64]

| **[F] Opção** [2] | **[F] Taxa pública e data** [2] | **[F] Pagamentos e liquidação** [2] | **[F] Produto, checkout e pós-compra** [2] | **[E] Leitura para o caso** [2] |
|---|---|---|---|---|
| **[F] Kiwify.** [58] | **[F] 8,99% + R$ 2,49 por venda aprovada; R$ 3,67 por saque; página de taxas atualizada em 23/01/2025, acesso em 12/09/2026.** [58] | **[F] Cartão D+15; Pix/boleto D+2; D+2 no cartão adiciona 2% e eleva reserva para 10%.** [58] | **[F] Checkout hospedado, bump, one-click upsell, área de membros, afiliados e recuperação por WhatsApp; [ND] embed geral por iframe.** [58] | **[E] Funcionalmente completa; a parcela fixa pesa no low ticket.** [58] [6] |
| **[F] Hotmart.** [59] | **[F] Central: 9,9% + R$ 1,00 em 12/09/2026 e mudança para R$ 2,49 em 21/09/2026; página comercial/política já mostravam R$ 2,49; aplicabilidade contratual é ND.** [59] | **[F] Cartão D+30; Pix/boleto D+2; parcelamento 3,49% a.m.; antecipações separadas.** [59] | **[F] Checkout hospedado, overlay/embutido, bump, upsell, Club, recuperação, afiliados e eNotas.** [59] | **[E] Cobertura ampla, mas exigir captura do painel por conflito oficial e considerar Player vigente na data.** [59] |
| **[F] Cakto.** [60] | **[F] Pix 0% + R$ 2,49; cartão 4,99% + R$ 2,49; páginas acessadas em 12/09/2026; [ND] boleto, saque e prazos têm divergências oficiais.** [60] | **[ND] Pix “instantâneo” versus D+1; [F] cartão até D+15; antecipação existe, preço ND.** [60] | **[F] Checkout hospedado e API própria, bump, one-click cartão, Members e afiliados; recuperação/fiscal dependem de integrações.** [60] | **[E] Pix é econômico, mas contratação deve resolver conflitos por escrito.** [60] [6] |
| **[F] Ticto.** [61] | **[F] Política de 03/07/2026: 6,99% + R$ 2,49; Termos conflitantes citam 9,9% + R$ 2,49; acesso em 12/09/2026.** [61] | **[F] Pix D0, boleto D+2 após compensação, cartão D+30; parcelamento 3,49% a.m.; antecipação 5,49% por período e reserva de 40%.** [61] | **[F] Hospedado, bump, upsell, Mozart, recuperação/Magic Link, afiliados e integrações fiscais; [ND] embed.** [61] | **[E] Aderente, inclusive campanha low ticket até R$ 50, mas taxa efetiva exige confirmação contratual.** [61] |
| **[F] Eduzz.** [62] | **[F] Básico 4,9% + R$ 2,49; até R$ 30,00 a regra principal isenta 4,9%; artigo atualizado em 14/04/2026; saque conflita entre R$ 1,99 e R$ 9,00.** [62] | **[F] Pix/boleto D+2; cartão D+30; parcelamento 3,49% a.m.; antecipação 2,99% + 0,1% por dia.** [62] | **[F] Hospedado e Elements embutido, bump, one-click cartão, Nutror, recuperação, afiliados e Smart Notas; SafeVideo pode cobrar R$ 3,99 por aluno/plataforma.** [62] | **[E] Taxa de entrada favorável em R$ 27, mas vídeo e saque precisam entrar na unit economics.** [62] [6] |
| **[F] Stripe.** [63] | **[F] Cartão nacional 3,99% + R$ 0,39; Pix 1,19%; boleto R$ 3,45; página sem data editorial, acesso em 12/09/2026.** [63] | **[F] Cartão doméstico D+30; Pix/boleto D+2; Pix “somente por convite”; antecipação por parceiro e taxa ND.** [63] | **[F] Hospedado/embutido/Elements, Link e um cross-sell; [ND] upsell pós-compra, área de membros e afiliados nativos.** [63] | **[E] Checkout componível e barato, mas exige LMS, fiscal e automações externas.** [63] |
| **[F] Mercado Pago.** [64] | **[F] Cartão 4,98% D0, 4,49% D14 ou 3,98% D30; Pix 0,99%; boleto R$ 3,49; página sem data editorial, acesso em 12/09/2026.** [64] | **[F] Pix D0; boleto até 3 dias; parcelamento até 12x no Transparente e 18x no Link; antecipação tem preço ND no app.** [64] | **[F] Pro redirecionado e Bricks/Transparente embutido; [ND] bump, upsell, área de membros e afiliados nativos; NFS-e por R$ 79/mês ou grátis acima de R$ 10 mil/mês.** [64] | **[E] Forte para Pix/liquidez, mas cursos e intangíveis não têm Proteção ao Vendedor e o LMS é externo.** [64] |

**[E]** Nos cálculos auditáveis de R$ 27, a taxa-base efetiva é **18,21%** na Kiwify, **13,60%** na Hotmart pela regra temporal de corte, **9,22%** no Pix Cakto, **14,21%** no cartão Cakto, **16,21%** na Ticto, **9,22%** na Eduzz, **5,43%** no cartão Stripe e **3,98%** no cartão D30 Mercado Pago. [6] [58] [59] [60] [61] [62] [63] [64] **[E]** Esses exemplos excluem parcelamento, antecipação, saque, afiliados, fiscal, reembolso, chargeback e ferramentas externas. [6]

## 4.2. Campos, meios, cupom, timer, resumo e benchmarks

**[F]** Em benchmark internacional da Baymard, o checkout médio tinha **11,3 campos** e **5,1 etapas**, enquanto os testes de usabilidade indicavam que muitos fluxos físicos poderiam operar com **7–8 campos**; isso não é norma para produto digital brasileiro. [53]

**[E]** Use um campo de nome completo, e-mail cedo para recibo/acesso e campos progressivos por método; CPF, telefone e endereço só entram com finalidade e exigência documentadas. [19] [11] **[E]** Pix e cartão podem iniciar expostos e boleto recolhido, mas a ordem final deve vir dos dados da conta por ticket e origem. [19]

| **[F] Indicador** [2] | **[F] Brasil** [2] | **[F] Internacional** [2] | **[E] Uso correto** [2] |
|---|---|---|---|
| **[F] Mix de valor.** [19] | **[F] E-commerce geral de 2023: cartão nacional 39%, internacional 10%, Pix 33% e boleto 9%.** [19] | **[ND] Não necessário para interpretar o mix brasileiro.** [19] | **[E] Confirma relevância dos meios; não mede conversão nem aprovação.** [19] |
| **[F] Abandono.** [19] | **[ND] Produto digital por ticket/método: não publicado.** [19] | **[F] Média simples de 70,22% em 50 estudos heterogêneos.** [54] | **[E] Contexto amplo, não baseline operacional.** [54] |
| **[F] Recuperação por e-mail.** [19] | **[ND] Produto digital por ticket/método: não publicado.** [19] | **[F] Klaviyo: mais de 143 mil fluxos; 3,33% de pedido atribuído em média.** [55] | **[E] Fonte de plataforma e varejo; medir incrementalidade por holdout.** [55] |
| **[F] Métodos adicionais.** [56] | **[ND] Pix/Brasil isolado: não divulgado.** [56] | **[F] Holdback Stripe: conversão +7,4% e receita +12% quando ao menos um método relevante adicional era exibido.** [56] | **[E] Testar método local; não importar o lift.** [56] |

**[E]** Cupom deve ficar recolhido, resumo e total acessíveis, erro corrigível sem reinício, CTA específico por método e timer somente para expiração real. [19] **[ND]** Conversão e recuperação por faixa/método permanecem ND. [19]

## 4.3. Order bump e upsell

**[F]** Hotmart, Kiwify, Cakto, Ticto e Eduzz documentam bump e/ou upsell, enquanto Stripe confirma cross-sell no checkout e Mercado Pago não publicou componente nativo equivalente nas páginas auditadas. [58] [59] [60] [61] [62] [63] [64]

**[E]** O controle inicial deve ser sem adicional; a variante usa um único complemento não pré-selecionado, com descrição, preço e novo total. [19] **[E]** Para tickets superiores, teste primeiro o upsell após aprovação para não colocar nova decisão antes do pagamento principal. [19]

**[ND]** Não existe taxa pública confiável de aceite por faixa no produto digital brasileiro. [19] **[E]** A métrica é receita líquida por sessão, com conversão principal, ativação, reembolso, chargeback e suporte como guardrails. [19]

## 4.4. Página de obrigado e primeiros 7 dias

| **[F] Estado** [2] | **[E] Página/e-mail** [2] | **[E] Onboarding** [2] |
|---|---|---|
| **[F] Cartão/Pix aprovado.** [19] | **[E] Confirmar pedido, item, total, método, recibo, acesso, suporte e arrependimento.** [8] [19] | **[E] Um CTA dominante para a primeira ação útil.** [19] |
| **[F] Pix pendente.** [19] | **[E] Mostrar “pagamento ainda não confirmado”, QR, copia-e-cola, valor, validade e atualização automática.** [19] | **[E] Não liberar conteúdo pago antes da aprovação.** [19] |
| **[F] Boleto pendente.** [19] | **[E] Mostrar linha, vencimento e prazo de compensação; não chamar de compra aprovada.** [19] | **[E] Liberar após webhook de aprovação.** [19] |
| **[F] Falha.** [19] | **[E] Erro acionável, dados não sensíveis preservados e alternativa de método.** [19] | **[E] Não criar acesso nem prometer entrega.** [8] |

**[F]** O Decreto nº 7.962/2013 exige confirmação imediata da aceitação e contrato conservável e reproduzível. [8] **[E]** Nos **7 dias** iniciais, envie recibo/acesso após aprovação, lembrete por ausência de acesso, ajuda após acesso sem primeira ação e suporte/reembolso antes do fim da janela, sem criar obstáculo ao direito. [7] [8] [19]

## 4.5. Recuperação por estado

| **[F] Estado** [2] | **[E] Mensagem** [2] | **[E] Regra de parada** [2] |
|---|---|---|
| **[F] Abandono sem ordem.** [19] | **[E] “Continue de onde parou”, sem dizer que há pagamento pendente.** [19] | **[E] Compra, oposição ou fim da elegibilidade.** [11] [19] |
| **[F] Pix não pago.** [19] | **[E] Link vigente, código, valor e validade real.** [19] | **[E] Aprovação, expiração, cancelamento ou oposição.** [19] |
| **[F] Boleto não pago.** [19] | **[E] Linha digitável, vencimento e compensação.** [19] | **[E] Aprovação, vencimento, cancelamento ou oposição.** [19] |
| **[F] Cartão recusado.** [19] | **[E] Próximo passo acionável e alternativa de cartão/Pix sem reiniciar.** [19] | **[E] Aprovação, desistência ou oposição.** [19] |

**[E]** A cadência inicial pode testar imediato/10 min, 2–4 h, 24 h e até 48 h, mas esses momentos vêm de configuração de plataforma e benchmark internacional, não de causalidade brasileira; cada disparo consulta o estado atual. [19] **[E]** Use holdout para separar recuperação incremental de compra espontânea. [56]

# PARTE 5. ANÚNCIO ↔ PÁGINA

## 5.1. Message match

**[F]** O Google recomenda correspondência entre anúncio, palavra-chave, CTA e conteúdo de destino; a Meta mede visualização somente quando o destino carrega. [48] [15] **[E]** Replique problema, nome do produto, preview e condição comercial do criativo no hero, sem mudar promessa ou preço no checkout. [13] [14]

**[E]** Instrumente `ad_click → landing_page_view → view_offer → checkout_started → payment_approved`, preservando UTMs e evitando redirecionamentos em cadeia. [15] [45] **[ND]** Não há uplift brasileiro isolado de message match para estas ofertas. [48]

## 5.2. Destinos penalizáveis pela Meta

**[F]** A Meta pode revisar anúncio e destino e proíbe práticas comerciais enganosas, incluindo preço enganoso. [13] [14] **[E]** A página deve evitar promessa improvável, renda/resultado garantido, clickbait, falso botão, escassez falsa, preço oculto, endosso inexistente, discrepância de marca/produto e coleta opaca. [13] [14] [7]

**[E]** Para reduzir risco de reprovação e fricção, identifique fornecedor, produto, preço, condições, entrega, contato, privacidade e arrependimento; mantenha página funcional e mobile. [8] [13] **[ND]** Aprovação e custo menor não podem ser prometidos, pois leilão, conta, criativo, público, evento e destino interagem e não existe fórmula pública de CPA. [15]

## 5.3. Advertorial/pré-venda versus página direta

**[E]** Use página direta como controle quando o criativo já demonstra problema e produto; teste pré-venda transparente quando categoria, mecanismo ou adequação exigem educação antes da oferta. [16] **[E]** Compare compra e receita por clique de anúncio no funil completo, não a taxa isolada da última página. [16]

**[F]** Testes de páginas longas e curtas produziram resultados conflitantes e geralmente mudaram pacotes inteiros. [16] [17] **[ND]** Não há estudo que determine, por **R$ 197–297** ou **R$ 497–697**, quando advertorial vence no tráfego frio brasileiro. [16] **[E]** A pré-venda deve declarar natureza comercial e não esconder preço, responsável ou oferta. [7] [8]

# PARTE 6. TESTES E MÉTRICAS

## 6.1. Dez testes A/B ordenados

**[E]** A ordem prioriza integridade de medição, velocidade, clareza, demonstração e checkout antes de persuasão adicional; é uma priorização operacional, não ranking causal universal. [45] [19]

| **[E] Ordem** [2] | **[E] Hipótese isolada** [2] | **[E] Controle × variação** [2] | **[E] Métrica primária** [2] | **[E] Guardrails** [2] |
|---:|---|---|---|---|
| **[E] 1.** [45] | **[E] Melhor desempenho aumenta compras.** [46] | **[E] Mesmo conteúdo; pacote atual × HTML/LCP/JS otimizado.** [45] | **[E] Compra por sessão elegível.** [46] | **[E] LCP, INP, CLS, erros e cobertura.** [45] |
| **[E] 2.** [23] | **[E] Hero específico reduz ambiguidade.** [23] | **[E] Headline genérica × tarefa, entregável e público.** [23] | **[E] Compra por sessão.** [17] | **[E] Início de checkout, rejeição e reembolso.** [17] |
| **[E] 3.** [23] | **[E] Tela real explica melhor que mockup.** [23] | **[E] Mockup × loop/demo legendada do mesmo fluxo.** [23] | **[E] Compra por sessão.** [23] | **[E] LCP, play, compreensão e bytes.** [24] |
| **[E] 4.** [16] | **[E] Contexto antes da compra ajuda tráfego frio.** [22] | **[E] CTA de compra no hero × âncora e CTA após entregáveis.** [22] | **[E] Compra por sessão mobile.** [16] | **[E] Receita, checkout e scroll como diagnóstico.** [16] |
| **[E] 5.** [16] | **[E] Densidade adequada depende da oferta.** [16] | **[E] Página concisa × expandida por objeções, sem mudar preço/CTA.** [16] | **[E] Compra por sessão.** [16] | **[E] Receita, reembolso e suporte.** [16] |
| **[E] 6.** [44] | **[E] CTA fixa contextual reduz esforço.** [44] | **[E] Sem barra × painel inferior após CTA sair da tela.** [44] | **[E] Compra mobile.** [44] | **[E] Cliques acidentais, CLS e INP.** [42] |
| **[E] 7.** [29] | **[E] Bloco de preço completo reduz dúvida.** [29] | **[E] Preço/CTA × total, Pix, parcelas, entrega e 7 dias.** [7] [9] | **[E] Compra por visualização do preço.** [29] | **[E] Dúvida de cobrança, reembolso e margem.** [29] |
| **[E] 8.** [19] | **[E] Campos progressivos elevam aprovação.** [19] | **[E] CPF/telefone universais × mínimos por método.** [11] [19] | **[E] Pagamento aprovado por checkout.** [19] | **[E] Fiscal, fraude, erro e entrega.** [19] |
| **[E] 9.** [56] | **[E] Ordem de meios relevante ajuda conclusão.** [56] | **[E] Ordem atual × Pix/cartão visíveis e boleto recolhido.** [19] | **[E] Aprovação por checkout.** [19] | **[E] Mix, taxa, margem e tempo.** [58] [59] [60] [61] [62] [63] [64] |
| **[E] 10.** [19] | **[E] Recuperação por estado supera mensagem única.** [19] | **[E] Sequência única × fluxos separados com holdout.** [19] | **[E] Aprovação incremental por elegível.** [56] | **[E] Descadastro, reclamação, desconto e atribuição.** [11] [19] |

**[E]** Para duas proporções, o cálculo foi reproduzido com teste bilateral, **α=0,05**, poder **80%**, alocação igual e aproximação normal. [6] **[E]** Um lift relativo de **20%** requer aproximadamente **42.693**, **21.109**, **13.914** ou **8.158** sessões por braço quando a baseline é, respectivamente, **1%**, **2%**, **3%** ou **5%**. [6] **[E]** Esses números são cenários matemáticos, não recomendação automática; perdas, atrasos, reembolsos, multiplicidade e unidade de randomização exigem ajuste. [6]

## 6.2. Métricas de referência

| **[F] Camada** [2] | **[E] Métrica própria** [2] | **[F] Referência externa** [2] | **[E] Regra de decisão** [2] |
|---|---|---|---|
| **[F] Aquisição.** [15] | **[E] Clique → visualização de destino.** [15] | **[ND] Sem limiar Meta por LCP ou ticket.** [15] | **[E] Diagnosticar perda por URL, aparelho e consentimento.** [15] |
| **[F] Página.** [16] | **[E] Compra/sessão, receita/sessão, `view_offer`, CTA e seção.** [16] | **[F] Unbounce reúne 41 mil páginas, mas mistura setores e tipos de conversão.** [57] | **[E] Baseline própria; não usar mediana ampla como meta de compra.** [57] |
| **[F] Checkout.** [19] | **[E] Aprovação por início, método, ticket e dispositivo.** [19] | **[ND] Brasil/produto digital por ticket e método.** [19] | **[E] Comparar taxas e margem por método.** [58] [59] [60] [61] [62] [63] [64] |
| **[F] Pós-compra.** [19] | **[E] Primeiro acesso, primeira ação, suporte, reembolso e chargeback.** [19] | **[ND] Benchmark brasileiro por faixa não publicado.** [19] | **[E] Não otimizar compra à custa de ativação ou qualidade.** [19] |
| **[F] Técnica.** [45] | **[E] LCP, INP, CLS no p75 por variante.** [45] | **[F] LCP ≤2,5 s, INP ≤200 ms, CLS ≤0,1.** [45] | **[E] Requisito técnico e diagnóstico, não previsão de receita.** [45] |

**[ND]** Tempo na página e chegada ao preço não possuem taxa “boa” universal; maior tempo pode significar interesse ou confusão. [16] **[E]** Defina sucesso por compra, receita líquida, aprovação, ativação e pós-venda; use cliques e scroll apenas para diagnóstico. [16] [19]

# PARTE 7. BLUEPRINTS FINAIS

## Blueprint A — R$ 27–47

| **[E] Ordem** [2] | **[E] Seção e objetivo** [2] | **[E] Mídia/prova** [2] |
|---:|---|---|
| **[E] 1.** [1] | **[E] Hero: confirmar tarefa, três planilhas, prompts, preço e acesso.** [1] | **[E] Poster/tela real e CTA de compra ou demo.** [23] |
| **[E] 2.** [23] | **[E] Demonstração: uma entrada e uma saída em até 55 s como hipótese.** [23] | **[E] Loop/MP4 legendado com dados fictícios identificados.** [23] |
| **[E] 3.** [1] | **[E] Conteúdo: nome, função e compatibilidade das três planilhas e categorias de prompts.** [1] | **[E] Capturas ampliadas e exemplo de prompt.** [23] |
| **[E] 4.** [7] | **[E] Adequação: para quem é/não é e limites de autosserviço.** [7] | **[E] Antes/depois apenas organizacional.** [1] |
| **[E] 5.** [9] | **[E] Oferta: total, Pix, parcelas se houver, entrega e 7 dias.** [7] [9] | **[E] Condição real, CNPJ e processador identificados.** [8] |
| **[E] 6.** [8] | **[E] FAQ/rodapé: acesso, arquivos, suporte, privacidade e arrependimento.** [8] | **[E] Links literais e contato testado.** [8] |

| **[E] Decisão** [2] | **[E] Prescrição** [2] |
|---|---|
| **[E] Preço.** [1] | **[E] Compra única dentro de R$ 27–47; sem âncora fictícia.** [1] [7] |
| **[E] Urgência.** [32] | **[E] Nenhuma no controle; variante apenas com data real e mudança automática.** [32] |
| **[E] Checkout.** [19] | **[E] Mobile, campos mínimos por método, Pix/cartão visíveis, sem bump no controle.** [19] |
| **[E] Três primeiros testes.** [23] | **[E] Performance; headline específica; mockup versus demo.** [45] [23] |

### Cinco páginas reais para referência do Blueprint A

| **[F] Página** [2] | **[F] Preço observado em 12/09/2026** [2] | **[E] Por que usar** [2] |
|---|---:|---|
| **[F] [Controle Financeiro Pessoal](https://controlecer.company/).** [65] | **[F] R$ 47.** [65] | **[E] Hero, mockup, card de oferta e CTA; não copiar contador sem lastro.** [65] |
| **[F] [Planilha Financeira para Retiro](https://chacaradaserra.net/planilha-planejamento-financeiro-do-retiro/).** [67] | **[F] R$ 37.** [67] | **[E] Problema específico, sete abas e venda sem pressão aparente.** [67] |
| **[F] [+200 Prompts Secretos](https://isarego.com.br/teste.html).** [69] | **[F] R$ 47.** [69] | **[E] Objeção → módulos → autoridade → preço; alegações acadêmicas precisam ser reescritas.** [69] |
| **[F] [Spreadsheets Bundle](https://karaexploresmoney.podia.com/budget-spreadsheets).** [66] | **[F] US$ 7.** [66] | **[E] Screenshot real, lista curta e checkout curto; não importar ausência de reembolso sem revisão.** [66] |
| **[F] [CRM Template](https://www.easlo.co/templates/crm).** [68] | **[F] US$ 9.** [68] | **[E] Layout mínimo, CTA dominante e preview grande do template.** [68] |

**[ND]** Nenhuma das cinco páginas publica teste controlado da própria landing page; o uso é visual e estrutural. [65] [66] [67] [68] [69]

## Blueprint B — R$ 197–297

| **[E] Ordem** [2] | **[E] Seção e objetivo** [2] | **[E] Mídia/prova** [2] |
|---:|---|---|
| **[E] 1.** [1] | **[E] Hero: ligar problema operacional a dez planilhas, prompts e aulas.** [1] | **[E] Resultado visível, CTA e continuação da página.** [20] [23] |
| **[E] 2.** [23] | **[E] Fluxo: explicar como planilha, prompt e aula se conectam.** [23] | **[E] Diagrama curto e demo entrada → saída.** [23] |
| **[E] 3.** [1] | **[E] Inventário: tornar as dez planilhas e aulas auditáveis.** [1] | **[E] Galeria, índice e amostras ampliadas.** [70] [72] |
| **[E] 4.** [7] | **[E] Aplicações e adequação: uso por conta própria, pré-requisitos e exclusões.** [7] | **[E] Demos e documentação, sem economia temporal garantida.** [1] |
| **[E] 5.** [9] | **[E] Oferta: total, Pix, parcelas, entrega, suporte e 7 dias.** [7] [9] | **[E] Um único preço consistente e identificação do fornecedor.** [8] |
| **[E] 6.** [8] | **[E] FAQ/rodapé: implantação, acesso, atualização, privacidade e arrependimento.** [8] | **[E] Links literais e canal funcional.** [8] |

| **[E] Decisão** [2] | **[E] Prescrição** [2] |
|---|---|
| **[E] Preço.** [1] | **[E] Compra única dentro de R$ 197–297, total parcelado junto da parcela.** [1] [9] |
| **[E] Urgência.** [32] | **[E] Controle sem urgência; variante apenas com prazo comercial material.** [32] |
| **[E] Checkout.** [19] | **[E] Pix e cartão expostos, boleto secundário, resumo persistente e campos progressivos.** [19] |
| **[E] Três primeiros testes.** [45] | **[E] Performance; headline de fluxo; inventário antes versus depois da demonstração.** [45] [23] |

### Cinco páginas reais para referência do Blueprint B

| **[F] Página** [2] | **[F] Preço observado em 12/09/2026** [2] | **[E] Por que usar** [2] |
|---|---:|---|
| **[F] [Pack Site Fácil](https://packsitefacil.com.br/).** [70] | **[F] R$ 197.** [70] | **[E] Galeria visual, segmentação, stack e bloco comercial; claims “validados” não têm teste publicado.** [70] |
| **[F] [Pack Páginas Lucrativas](https://cristianefaria.com/produtos/pack-paginas-lucrativas/).** [71] | **[F] R$ 197,70 no bloco de oferta, com conflito de R$ 147 no topo.** [71] | **[E] Mecanismo, implantação e bônus; corrigir a inconsistência de preço em qualquer adaptação.** [71] |
| **[F] [Kit Página de Vendas + Captura + Obrigado](https://templates.descomplicandosites.com.br/produto/kit-pagina-de-vendas-captura/).** [72] | **[F] R$ 197.** [72] | **[E] Ficha compacta, demos, tutorial, FAQ e parcelamento explícito.** [72] |
| **[F] [The Systems Course](https://www.riskology.co/courses/systems-course/).** [73] | **[F] US$ 49.** [73] | **[E] Mecanismo nomeado, currículo completo e prova distribuída.** [73] |
| **[F] [Productivity Power Hour](https://thesweetsetup.com/productivity-power-hour/).** [74] | **[F] US$ 39 no HTML público.** [74] | **[E] Workshop curto, duração explícita e framework de quatro passos.** [74] |

**[ND]** Nenhuma das cinco páginas publica experimento da própria página com variante, amostra, duração e intervalo de confiança. [70] [71] [72] [73] [74]

## Blueprint C — R$ 497–697 vertical profissional

| **[E] Ordem** [2] | **[E] Seção e objetivo** [2] | **[E] Mídia/prova** [2] |
|---:|---|---|
| **[E] 1.** [1] | **[E] Hero vertical: profissão, vinte planilhas, cinco núcleos, escopo e acesso.** [1] | **[E] Tela real, CTA e índice dos núcleos.** [23] |
| **[E] 2.** [1] | **[E] Prova e mapa: tornar arquitetura e profundidade visíveis.** [1] | **[E] Galeria dos cinco núcleos e caso fictício identificado.** [77] |
| **[E] 3.** [23] | **[E] Demonstrações: uma tarefa por núcleo, com capítulos.** [23] | **[E] Cinco clipes ou VSL segmentada, narração IA e legenda.** [23] |
| **[E] 4.** [1] | **[E] Inventário: nome, entrada, saída e limite das vinte planilhas.** [1] | **[E] Previews legíveis e filtros por núcleo.** [79] |
| **[E] 5.** [1] | **[E] Implantação: manual, prompts, compatibilidade e segurança operacional.** [1] | **[E] Sumário do manual e exemplos de prompts.** [23] |
| **[E] 6.** [7] | **[E] Adequação/objeções: autosserviço, atualização, suporte, confidencialidade e exclusões.** [7] | **[E] Documentação; nenhuma promessa jurídica, clínica ou financeira.** [7] |
| **[E] 7.** [9] | **[E] Oferta: total, parcelas, Pix, entrega e 7 dias.** [7] [9] | **[E] Condição real, CNPJ, contato e processador.** [8] |
| **[E] 8.** [8] | **[E] FAQ/rodapé: compra, acesso, dados, suporte, privacidade e arrependimento.** [8] [11] | **[E] Links literais e canal testado.** [8] |

| **[E] Decisão** [2] | **[E] Prescrição** [2] |
|---|---|
| **[E] Preço.** [1] | **[E] Compra única dentro de R$ 497–697; parcelas e total no mesmo bloco.** [1] [9] |
| **[E] Urgência.** [32] | **[E] Só lançamento, fechamento ou bônus com consequência automática e comprovável.** [32] |
| **[E] Checkout.** [19] | **[E] Resumo completo, Pix/cartão visíveis, boleto alternativo e teste de upsell somente após aprovação.** [19] |
| **[E] Três primeiros testes.** [45] | **[E] Performance; hero por profissão versus cinco núcleos; vídeo único versus capítulos.** [45] [23] |

### Cinco páginas reais para referência do Blueprint C

| **[F] Página** [2] | **[F] Preço observado em 12/09/2026** [2] | **[E] Por que usar** [2] |
|---|---:|---|
| **[F] [Escola de Efeitos Especiais](https://escoladeefeitosespeciais.com.br/curso_online_de_edicao_animacao_efeitos_visuais_profissional/).** [75] | **[F] R$ 597.** [75] | **[E] Arquitetura longa, currículo, demonstração, professor, garantia e preço repetido.** [75] |
| **[F] [Espetacular Curso de Carrossel](https://millenanbg.com.br/carrossel-v3/).** [76] | **[F] R$ 397 atual e R$ 497 riscado.** [76] | **[E] Direção visual, prova cedo e método numerado; não é benchmark direto do ticket atual.** [76] |
| **[F] [Landing Pages ABS](https://designerabs.com.br/landing-pages-abs/).** [77] | **[F] Plano anual de R$ 597.** [77] | **[E] Galeria de projetos, feedbacks, stack e comparação de planos.** [77] |
| **[F] [Reels That Convert](https://socialtemplates.co/course).** [78] | **[F] US$ 97.** [78] | **[E] Página concisa, nicho explícito, escopo de uma hora e bullets operacionais.** [78] |
| **[F] [SMM 8 Template Bundle](https://alfie-studio.com/bundle).** [79] | **[F] US$ 149.** [79] | **[E] Previews por item, valor empilhado e antes/depois operacional.** [79] |

**[ND]** Nenhuma das cinco páginas prova desempenho causal do layout, e a página de carrossel tem preço atual abaixo da faixa; as referências são de arquitetura e direção visual. [75] [76] [77] [78] [79]

# NUNCA FAZER

| **[E] Proibição** [2] | **[F] Base** [2] |
|---|---|
| **[E] Inventar depoimento, cliente, foto, avaliação, contador, número de uso ou selo.** [7] [37] | **[F] Publicidade objetiva e testemunhal precisam ser verdadeiros e comprováveis.** [7] [37] |
| **[E] Prometer renda, resultado profissional, saúde ou economia temporal determinada sem ensaio pertinente.** [1] [7] | **[F] O briefing veda essas promessas, e omissão ou afirmação capaz de induzir erro é enganosa.** [1] [7] |
| **[E] Usar escassez falsa, timer reiniciável, vaga ilimitada ou bônus permanente “só hoje”.** [14] [32] | **[F] A Meta veda práticas enganosas, e autoridades descrevem timers falsos como dark pattern.** [14] [32] |
| **[E] Riscar preço não praticado ou esconder total, juros, adicionais e recorrência.** [7] [9] | **[F] Preço e condições devem ser claros, precisos e ostensivos.** [7] [9] |
| **[E] Chamar mínimo legal de 7 dias de benefício exclusivo ou dificultar o arrependimento.** [7] [8] | **[F] O direito e seu canal são obrigatórios no comércio eletrônico.** [7] [8] |
| **[E] Exigir CPF, telefone ou endereço só para enriquecer CRM.** [11] [19] | **[F] Finalidade, necessidade e transparência limitam a coleta.** [11] |
| **[E] Pré-selecionar bump, esconder recusa de upsell ou bloquear acesso atrás de nova oferta.** [19] | **[E] Adicional deve ser inequívoco e subordinado à compra e ao onboarding.** [19] |
| **[E] Liberar conteúdo ou enviar recibo de aprovado quando Pix/boleto está pendente.** [19] | **[F] Pendente e aprovado são estados diferentes do processador.** [19] |
| **[E] Continuar recuperação após pagamento, expiração, reembolso ou oposição.** [11] [19] | **[E] A automação deve consultar o estado vigente e respeitar direitos do titular.** [11] [19] |
| **[E] Usar CAPI como bypass do consentimento ou contar Pixel e servidor em duplicidade.** [49] | **[F] A Meta rejeita contorno de privacidade e exige deduplicação.** [49] |
| **[E] Declarar vitória por clique, play, scroll ou significância observada cedo.** [16] [6] | **[E] A decisão exige plano prévio, compra/receita, incerteza e guardrails.** [16] [6] |
| **[E] Tratar benchmark internacional, de varejo ou SaaS como taxa típica brasileira.** [16] [19] | **[F] País, produto, método, métrica e desenho limitam a transferência.** [16] [19] |
| **[E] Publicar taxa de plataforma sem data, método, prazo, plano e custos separados.** [58] [59] [60] [61] [62] [63] [64] | **[F] As próprias páginas têm conflitos, condições por conta e custos adicionais.** [58] [59] [60] [61] [62] [63] [64] |

# Limitações e decisão de lançamento

**[F]** As páginas de benchmark foram inspecionadas em **12/09/2026** e podem mudar; nenhuma compra foi concluída, nenhum arquivo entregue foi validado e nenhuma taxa de conversão das páginas foi auditada. [4] **[F]** A checagem de URL confirma disponibilidade HTTP na amostra, não veracidade de todo o conteúdo nem permanência futura. [5]

**[F]** Existem conflitos oficiais materiais nas taxas ou prazos de Hotmart, Cakto, Ticto e Eduzz; nesses pontos, a informação foi mantida como **ND** até confirmação no painel ou contrato. [59] [60] [61] [62] **[E]** Antes do go-live, arquive capturas de taxas, termos, reserva, saque, reembolso e recursos da conta escolhida. [58] [59] [60] [61] [62] [63] [64]

**[ND]** Não há benchmark público diretamente comparável que forneça taxa de compra por faixa e fonte, aceite de bump, recuperação, aprovação ou reembolso para estas ofertas brasileiras. [19] **[E]** A decisão deve vir de baseline própria, testes pré-planejados e conciliação do backend com mídia e plataforma. [6] [49] [50]

**[E]** A primeira versão recomendada combina: hero compacto com demonstração real; copy factual; oferta com total e 7 dias; checkout progressivo; página por estado; onboarding antes de monetização; recuperação com holdout; Core Web Vitals no p75; consentimento simétrico; e trilha documental de cada alegação. [16] [19] [45] [7] [12]

# Referências
[1]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/oidfsbhAfFTTlamY.txt "Briefing da quarta rodada"
[2]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/tcbnxBzdEryawsCk.md "Manifesto público dos dossiês e artefatos de suporte da quarta rodada"
[3]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/tcbnxBzdEryawsCk.md "Manifesto público dos dossiês e artefatos de suporte da quarta rodada"
[4]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/tcbnxBzdEryawsCk.md "Manifesto público dos dossiês e artefatos de suporte da quarta rodada"
[5]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/RbMijuZeMgSHaytm.tsv "Auditoria HTTP de 28 URLs em 12/09/2026"
[6]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/gDykWQfQpumlwIaa.json "Cálculos reproduzíveis de amostra A/B, taxas e percentuais"
[7]: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm "Lei nº 8.078/1990 — Código de Defesa do Consumidor"
[8]: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm "Decreto nº 7.962/2013 — Comércio eletrônico"
[9]: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/decreto/d5903.htm "Decreto nº 5.903/2006 — Informação de preços"
[10]: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13455.htm "Lei nº 13.455/2017 — Diferenciação de preços"
[11]: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm "Lei nº 13.709/2018 — LGPD"
[12]: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf/@@display-file/file "ANPD — Guia orientativo de cookies"
[13]: https://transparency.meta.com/policies/ad-standards/ "Meta Advertising Standards"
[14]: https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/ "Meta — Prohibited Commercial Practices"
[15]: https://www.facebook.com/business/help/417293491972212 "Meta — Landing page view optimization"
[16]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/BACZoqwjUCkAmKWq.md "T01 — Anatomia e comprimento da página mobile"
[17]: https://cxl.com/blog/case-study-how-we-improved-landing-page-conversion/ "CXL — TruckersReport case study"
[18]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/neFNbHOnVayiGdpo.md "T04 — Prova social ética no lançamento"
[19]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/cQihATJRPPSuiHox.md "T06 — Otimização do checkout e pós-compra"
[20]: https://www.nngroup.com/articles/illusion-of-completeness/ "NN/g — The Illusion of Completeness"
[21]: https://signalvnoise.com/posts/2977-behind-the-scenes-highrise-marketing-site-ab-testing-part-1 "Highrise long-form test"
[22]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/BACZoqwjUCkAmKWq.md "T01 — Evidência conflitante sobre posição da CTA"
[23]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/RKEdusqdXBepoqAH.md "T02 — Copy, mídia hero e demonstração"
[24]: https://web.dev/articles/replace-gifs-with-videos "web.dev — Replace animated GIFs with video"
[25]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/RKEdusqdXBepoqAH.md "T02 — Duração experimental de VSL"
[26]: https://www.navattic.com/report/state-of-the-interactive-product-demo-2025 "Navattic — State of the Interactive Product Demo 2025"
[27]: https://www.facebook.com/business/help/1675722002698686 "Meta — Add captions to your video ad"
[28]: https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html "W3C — Captions prerecorded"
[29]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/iKSssKSqUVVBCpbv.md "T03 — Preço, garantia e urgência"
[30]: https://www.nngroup.com/articles/comparison-tables/ "NN/g — Comparison Tables"
[31]: https://baymard.com/blog/perceived-security-of-payment-form "Baymard — Perceived security of payment forms"
[32]: https://pubsonline.informs.org/doi/abs/10.1287/isre.2019.0859 "Cart targeting, scarcity and price incentives"
[33]: https://help.hotmart.com/pt-br/article/360030387292/como-configurar-o-hotmart-ask- "Hotmart Ask"
[34]: https://help.hotmart.com/pt-br/article/115003134331/como-customizar-minha-aparencia-da-pagina-de-pagamento "Hotmart — Aparência da página de pagamento"
[35]: https://ajuda.kiwify.com.br/pt-br/article/como-integrar-com-o-activecampaign-mu2gmp/ "Kiwify — ActiveCampaign"
[36]: https://ajuda.kiwify.com.br/pt-br/article/como-funcionam-os-webhooks-2ydtgl/ "Kiwify — Webhooks"
[37]: https://conar.wpenginepowered.com/wp-content/uploads/2026/08/Codigo_CONAR_2026.pdf "Código CONAR 2026"
[38]: https://www.gov.br/mj/pt-br/assuntos/seus-direitos/consumidor/notas-tecnicas/nota-tecnica-224.pdf "Senacon — Nota Técnica nº 224/2019, Diletto"
[39]: https://www.procon.sp.gov.br/wp-content/uploads/files/Representacao_DPPC_Empiricus.pdf "Procon-SP — Representação Empiricus"
[40]: https://www.tjsp.jus.br/Noticias/Noticia?codigoNoticia=96153 "TJSP — Influenciadora indenizará seguidora por propaganda enganosa"
[41]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/neFNbHOnVayiGdpo.md "T04 — Casos de direito de imagem e testemunhal"
[42]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/pCvlgEqqMLCnKilQ.md "T05 — UX mobile, acessibilidade e consentimento"
[43]: https://www.onlinedialogue.nl/en/blogs/sticky-cta-guaranteed-conversion-uplift/ "Online Dialogue — revisão de sticky CTA"
[44]: https://growthrock.co/sticky-add-to-cart-button-example/ "Growth Rock — Sticky add-to-cart A/B tests"
[45]: https://web.dev/articles/vitals "web.dev — Core Web Vitals"
[46]: https://web.dev/case-studies/vodafone "web.dev — Vodafone case study"
[47]: https://web.dev/case-studies/rakuten "web.dev — Rakuten 24 case study"
[48]: https://support.google.com/google-ads/answer/7543502?hl=pt-BR "Google Ads — Experiência na página de destino"
[49]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/pCvlgEqqMLCnKilQ.md "T05 — Meta Pixel, CAPI e deduplicação"
[50]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/pCvlgEqqMLCnKilQ.md "T05 — Google Consent Mode"
[51]: https://arxiv.org/abs/1909.02638 "Utz et al. — (Un)informed Consent"
[52]: https://arxiv.org/abs/2001.02479 "Nouwens et al. — Dark Patterns after the GDPR"
[53]: https://baymard.com/blog/checkout-flow-average-form-fields "Baymard — Checkout form fields"
[54]: https://baymard.com/lists/cart-abandonment-rate "Baymard — Cart abandonment rate"
[55]: https://www.klaviyo.com/blog/abandoned-cart-benchmarks "Klaviyo — Abandoned cart benchmarks"
[56]: https://stripe.com/blog/testing-the-conversion-impact-of-50-plus-global-payment-methods "Stripe — Global payment-method holdback"
[57]: https://unbounce.com/conversion-benchmark-report/ "Unbounce — 2024 Conversion Benchmark Report"
[58]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/YVJeQJgFedPbeCRn.md "Auditoria Kiwify; taxas oficiais e acesso em 12/09/2026"
[59]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/feMeucvtkwxYLbSg.md "Auditoria Hotmart; taxas oficiais e acesso em 12/09/2026"
[60]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/yBqFKnkawtSgKcxh.md "Auditoria Cakto; taxas oficiais e acesso em 12/09/2026"
[61]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/tFTrlAajBaCCpMaN.md "Auditoria Ticto; taxas oficiais e acesso em 12/09/2026"
[62]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/gNOvsTDopytQaKBH.md "Auditoria Eduzz; taxas oficiais e acesso em 12/09/2026"
[63]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/CFxyrWDuKoMhWzcb.md "Auditoria Stripe separada; taxas oficiais e acesso em 12/09/2026"
[64]: https://files.manuscdn.com/user_upload_by_module/session_file/310419663031032655/CFxyrWDuKoMhWzcb.md "Auditoria Mercado Pago separada; taxas oficiais e acesso em 12/09/2026"
[65]: https://controlecer.company/ "Controle Financeiro Pessoal — verificado em 12/09/2026"
[66]: https://karaexploresmoney.podia.com/budget-spreadsheets "Spreadsheets Bundle — verificado em 12/09/2026"
[67]: https://chacaradaserra.net/planilha-planejamento-financeiro-do-retiro/ "Planilha Financeira para Retiro — verificada em 12/09/2026"
[68]: https://www.easlo.co/templates/crm "CRM Template — verificado em 12/09/2026"
[69]: https://isarego.com.br/teste.html "+200 Prompts Secretos — verificado em 12/09/2026"
[70]: https://packsitefacil.com.br/ "Pack Site Fácil — verificado em 12/09/2026"
[71]: https://cristianefaria.com/produtos/pack-paginas-lucrativas/ "Pack Páginas Lucrativas — verificado em 12/09/2026"
[72]: https://templates.descomplicandosites.com.br/produto/kit-pagina-de-vendas-captura/ "Kit Página de Vendas + Captura + Obrigado — verificado em 12/09/2026"
[73]: https://www.riskology.co/courses/systems-course/ "The Systems Course — verificado em 12/09/2026"
[74]: https://thesweetsetup.com/productivity-power-hour/ "Productivity Power Hour — verificado em 12/09/2026"
[75]: https://escoladeefeitosespeciais.com.br/curso_online_de_edicao_animacao_efeitos_visuais_profissional/ "Escola de Efeitos Especiais — verificada em 12/09/2026"
[76]: https://millenanbg.com.br/carrossel-v3/ "Espetacular Curso de Carrossel — verificado em 12/09/2026"
[77]: https://designerabs.com.br/landing-pages-abs/ "Landing Pages ABS — verificada em 12/09/2026"
[78]: https://socialtemplates.co/course "Reels That Convert — verificado em 12/09/2026"
[79]: https://alfie-studio.com/bundle "SMM 8 Template Bundle — verificado em 12/09/2026"
