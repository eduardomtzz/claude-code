# Rodada 4 (Claude): páginas de venda, checkout e conversão

Data: 2026-09-13. Três frentes rodadas em paralelo, com os relatórios completos em
`rodada-4-claude/`:

| Frente | Arquivo | O que tem |
|---|---|---|
| Checkout e benchmarks BR | `rodada-4-claude/checkout.md` | 9 plataformas comparadas, custo efetivo por ticket, Pix x cartão, order bump, reembolso, chargeback, nota fiscal e imposto |
| Evidências de conversão | `rodada-4-claude/evidencias.md` | ~100 fontes: estrutura, herói, preço e lei, urgência (Meta, CDC, Conar), prova social, mobile, anúncio↔página, testes A/B |
| Páginas reais | `rodada-4-claude/paginas.md` + `paginas-referencia/*.jpg` | 33 páginas abertas no navegador em modo celular (19 BR, 3 checkouts, 11 internacionais), ordem das seções, prova social, forte/fraco |

Conferi ao acaso quatro fontes primárias (taxas Cakto, Ticto e Kiwify; Decreto 5.903 art. 9º):
todas batem com o que está nos relatórios. Rótulos: F fato com fonte, E estimativa, ND não
encontrado. Quase nenhum benchmark é de infoproduto brasileiro; os números são ordem de grandeza.

## 1. Dez conclusões que mudam o que vamos construir

1. **A primeira tela decide.** 57% do tempo de atenção fica na primeira dobra e 81% nas três
   primeiras (NN/g, eyetracking). Promessa igual à do anúncio, demonstração visual do produto,
   preço à vista e botão precisam caber na primeira tela do celular.
2. **No nicho de planilhas e templates, ninguém usa VSL.** Das 19 páginas brasileiras, zero usam
   VSL sem controles. O herói é mockup do painel + vídeo curto. Isso favorece o nosso formato
   (demonstração de tela com narração por IA e legenda). Vídeos abaixo de 1 minuto têm o maior
   engajamento (Wistia); legendas somam 12% de tempo assistido e 80% reagem mal a som inesperado.
3. **O gancho número 1 do nicho é "pagamento único, sem mensalidade".** A comparação explícita
   com "software de R$ 200 por mês" é o argumento de preço mais forte observado. É exatamente a
   nossa âncora (Clinicorp, Astrea, Kiwify de SaaS).
4. **Preço: total à vista sempre visível; "de/por" é frágil.** Informar só parcelas é infração
   (Decreto 5.903, art. 9º IV). Preço riscado exige prova do preço anterior (Conar art. 27 §3º;
   CDC art. 37) e, em 22 testes de assinaturas, tendeu a perder. As páginas internacionais boas
   ancoram com três níveis (bom/melhor/ótimo) ou valor empilhado por módulo, não com risco.
5. **Urgência só real.** Pesquisa de Princeton achou timers falsos em 140 sites; a Meta enquadra
   urgência enganosa como prática comercial inaceitável e rebaixa a qualidade do anúncio. Uma
   página brasileira analisada usa "válido hoje: <data automática>": é o que nunca faremos.
   Preço de lançamento com data real registrada em `DECISOES.md` é permitido.
6. **Prova social sem clientes é possível e tem teto pequeno.** Cinco avaliações elevam a
   probabilidade de compra em 270% (380% em produto caro) e o efeito satura depois disso
   (Spiegel). Até lá: demonstração real do produto, garantia explicada, CNPJ, canal de suporte,
   reputação da plataforma de checkout e dado de mercado com fonte. Números inventados ("12.410
   advogados") são o padrão do nicho e são o que nos diferencia por não fazer.
7. **Pix converte mais e custa menos.** Conversão de carrinho acima de 90% no Pix contra ~70% no
   cartão (Gmattos). Abaixo de R$ 100 o Pix chega a 75% dos pagamentos; acima de R$ 500 o cartão
   parcelado lidera. Pix pré-selecionado no kit de entrada, 12x pré-selecionado nos verticais.
8. **Checkout: cinco campos, um order bump, cupom escondido.** Média do mercado é 11 campos;
   bastam nome, e-mail, CPF, telefone e pagamento. Order bump a 10–25% do preço converte 30–40%
   dos compradores (Hotmart/SamCart). Campo de cupom aberto faz o cliente sair para procurar
   cupom (Baymard). Três bumps empilhados (padrão Kiwify observado) cansam.
9. **A plataforma de checkout muda a margem em até 9 pontos.** No ticket de R$ 27 a Kiwify
   custa 18,2% e a Hotmart 19,1% (fixo sobe para R$ 2,49 em 21/09); Cakto no Pix custa 9,2%,
   Ticto 9,2% com isenção low ticket. Em R$ 697: Kiwify 9,3%, Cakto Pix 0,4%, cartão 5,3%.
10. **Testar compra exige volume que não teremos no começo.** Com 1% de conversão, detectar +20%
    pede ~30 mil visitas por variação. Testes iniciais medem clique no botão e início de
    checkout; a compra só valida mudanças grandes.

## 2. O que a Meta e a lei exigem da página (checklist fixo)

- Página coerente com o anúncio: mesma promessa na primeira dobra; sem cloaking; sem pop-up
  excessivo; sem linguagem sensacionalista (diagnósticos de relevância da Meta a partir de 500
  impressões).
- Preço total à vista, parcelas com juros informados (Decreto 5.903 art. 3º); desconto Pix
  informado antes do checkout (Lei 13.455/2017).
- Garantia de 7 dias (CDC art. 49) explicada em uma frase perto do preço e no FAQ.
- CNPJ, razão social, e-mail de suporte, termos e política de privacidade no rodapé. Metade das
  páginas brasileiras analisadas não tem: é vantagem de confiança barata.
- Depoimentos só reais, com nome e sobrenome, comprováveis (Conar Anexo Q). Funcionário não posa
  de cliente. Sem foto de banco de imagem como cliente.
- Banner de cookies com "rejeitar" tão visível quanto "aceitar" (guia ANPD). Nos estudos
  europeus 34–60% recusam nesse formato: planejar perda de sinal do Pixel; CAPI só com a mesma
  base legal.
- Velocidade: LCP até 2,5 s, INP até 200 ms, CLS até 0,1; 0,1 s a menos deu +8,4% de conversão
  no varejo (Google/Deloitte). Página em HTML estático, sem construtor pesado.
- Texto em nível de leitura simples (5ª a 7ª série converte 56% melhor, Unbounce), corpo 16 px,
  linha de 50–75 caracteres.

## 3. Blueprint por tipo de página

### Kit IA no Trabalho, R$ 27–47 (impulso, risco baixo)

| Seção | Objetivo | Conteúdo |
|---|---|---|
| Herói | Decidir em 5 s | Promessa do anúncio, GIF/vídeo mudo de 15–30 s da planilha funcionando, preço à vista, botão |
| O que vem dentro | Tornar concreto | Lista com print de cada item (3 planilhas + prompts), "abre no Excel, Google Sheets e celular" |
| Para quem é | Autoseleção | 3 perfis em uma linha cada |
| Preço e garantia | Remover risco | Preço à vista, Pix, 7 dias explicados, selo "pagamento pela [plataforma]" |
| FAQ curto | Objeções técnicas | 5 perguntas: compatibilidade, entrega, reembolso, atualização, suporte |
| Rodapé | Confiança | CNPJ, e-mail, termos, privacidade |

Altura alvo 5 a 8 mil px no celular. Sem VSL, sem três planos, sem bônus empilhado. Botão fixo
com preço. Testes: só clique no botão e início de checkout.

### IA no Trabalho, R$ 197–297 (decisão ponderada)

| Seção | Objetivo | Conteúdo |
|---|---|---|
| Herói | Promessa + prova visual | Headline curta de benefício, demonstração narrada de 60–90 s com legenda (autoplay mudo), preço à vista + 12x, botão |
| Problema e mecanismo | Explicar por que funciona | "Metade do tempo" = método em 3 passos, sem promessa de renda |
| Tour do que está incluído | Valor percebido | Card por planilha e por bloco de prompts, com print real; contagem verificável (abas, fórmulas, prompts) |
| Comparação | Ancorar | "Montar sozinho x curso longo x este kit", sem preço riscado |
| Para quem é / não é | Reduzir reembolso | 4 perfis sim, 2 não |
| Preço | Converter | Duas ou três opções (kit / kit + aulas / kit + aulas + prompts), a superior como âncora; total à vista, 12x e Pix |
| Garantia e confiança | Remover risco | 7 dias em texto claro, CNPJ, suporte, reputação da plataforma |
| FAQ | Objeções | 8 a 10 perguntas, inclui "preciso saber Excel?" e "funciona no celular?" |

Altura alvo 10 a 14 mil px. Testes: herói vídeo x estático; 1 x 3 opções; prova acima x abaixo.

### Verticais (advogados, médicos, dentistas), R$ 497–697 (risco alto para o avatar)

| Seção | Objetivo | Conteúdo |
|---|---|---|
| Herói | Reconhecimento | Dor na voz da profissão (falas da rodada 3), mockup do painel, demonstração de 60–90 s, preço à vista + 12x, botão |
| Regra de transparência | Expectativa certa | Linha obrigatória: kit de planilhas + manual + demonstrações + prompts; não é software, sem mensalidade, sem atendimento humano |
| Mecanismo | Credibilidade | Os 5 núcleos e o fechamento semanal de 30 min |
| Tour completo | Justificar o ticket | Uma seção por núcleo, com print real de cada planilha preenchida com a empresa fictícia; vídeo curto por núcleo |
| Comparação | Âncora | Tabela: software mensal (R$ 160–370/mês, fonte) x consultor x este kit; sem "de/por" |
| Amostra grátis | Prova e lead | Uma planilha do kit para baixar em troca de e-mail (automação de e-mail converte 1,49% contra 0,08% de campanha) |
| Para quem é / não é | Reduzir reembolso | Perfis por porte de clínica ou escritório |
| Bônus | Matar objeções | Cada bônus nomeia a objeção que resolve; valor estimado, não "de R$ 97 por R$ 0" |
| Preço | Converter | Kit (R$ 697) e Pro como âncora superior; 12x em destaque com total à vista; Pix |
| Garantia | Risco | 7 dias incondicional (avaliar 15 dias como diferencial: nenhuma página BR do nicho oferece mais que 7) |
| Confiança | Substituir depoimentos | Empresa por trás (Z2 Data Services, CNPJ), dados oficiais citados (CFO, OAB), regras de conselho respeitadas, LGPD |
| FAQ longo | Objeções | 12 a 15, inclui "é prontuário?" (não), "preciso de contador?", "e a LGPD?" |

Altura alvo 12 a 16 mil px. Considerar pré-página de conteúdo (advertorial) para tráfego frio
como teste, não como padrão. Testes: início de checkout e leads da amostra; compra só com
paciência de meses.

## 4. Blueprint do checkout

- Uma etapa; campos: nome, e-mail, CPF, telefone (necessário para recuperar Pix por WhatsApp:
  14,3% de Pix expirado recuperado, Appmax), pagamento.
- Pix pré-selecionado até R$ 100; cartão 12x pré-selecionado acima (Kiwify reporta até +30% de
  conversão com 12x pré-marcado).
- Um order bump no bloco de pagamento, 10–25% do preço, texto de duas frases, sem "só agora".
- Cupom escondido atrás de link. Sem timer. Resumo com total antes do botão.
- Upsell em um clique na página pós-compra (aceite típico 10–20% em digital).
- Página de obrigado com acesso imediato, vídeo "abra assim" de 3 min, e-mail D+1 e D+5. Reembolso
  aprovado sem atrito (limite de chargeback das plataformas é 0,9–1,5%; reembolso não tem limite).
- Nota fiscal por venda via eNotas/Notazz/Spedy, emitida após os 7 dias de garantia. Enquadramento
  provável: CNAE 8599-6/04, Anexo III (6% inicial) se Fator R ≥ 28%; confirmar com contador.

## 5. Plataforma de checkout: recomendação para decisão do Eduardo

| Opção | Custo em R$ 27 | Custo em R$ 697 | A favor | Contra |
|---|---|---|---|---|
| **Cakto** | 9,2% (Pix) / 14,2% (cartão) | 0,4% / 5,3% | Pix 0% + R$ 2,49; upsell 1 clique, área de membros, afiliados | Mais nova; recuperação nativa ND; juros do parcelamento não publicados |
| **Ticto** | 9,2% (isenção low ticket, sob contato) | 7,3% | Pix D0, recuperação de carrinho nativa, domínio próprio no checkout | Saque R$ 4,80–9,60; antecipação limitada |
| Kiwify | 18,2% | 9,3% | Ecossistema maduro, área de membros grátis, muito usada | Mais cara; checkout só em domínio da Kiwify |
| Hotmart | 19,1% | 10,3% | Checkout embutido, recuperador nativo, avaliação pública de produto | Mais cara; cartão em 30 dias |

Minha recomendação: **Cakto para o Kit e o IA no Trabalho**, com Ticto como alternativa se a
reputação da Cakto no Reclame Aqui não convencer na etapa 7. Kiwify só se as duas falharem em
estabilidade. Decisão fica registrada em `DECISOES.md` quando o Eduardo escolher.

## 6. Nunca fazer (lista fechada)

- Contador falso, data automática do dia, "últimas vagas" em produto digital.
- "De R$ X por R$ Y" sem preço anterior praticado e documentado.
- Só parcelas sem o total à vista.
- Números de clientes inventados; estrelas decorativas sem nota; foto de banco como cliente.
- Headline em caixa alta com medo; capa 3D de robô; múltiplas âncoras ("valor de R$ 3.000").
- Bônus "de R$ 97 por R$ 0".
- Três order bumps empilhados; modal que bloqueia o checkout.
- Vitalício vendido como assinatura.
- Página sem CNPJ, termos, privacidade e e-mail.
- Vídeo do YouTube como herói (leva o visitante para fora da página).
- Promessa de renda, resultado clínico ou jurídico.

## 7. Referências para copiar a estrutura (não o tom)

- R$ 27–47: Easlo (Gumroad, capa + preço + contadores reais), PromptsHQ (escada grátis→pago por
  profissão), Guia do Excel (ficha com formas de pagamento e 730 avaliações), Business OS (valor
  empilhado + reembolso 30 dias), Samurai Lab (estrutura PAS e entregáveis; não copiar o tom).
- R$ 197–297: Planilha Essencial do Advogado (melhor esqueleto BR: barra fixa, comparação com
  software mensal, objeções em pergunta), Tícius (para quem é em 4 perfis, funcionalidades =
  abas), Legal Hub (identidade própria, mockup), Someka (demo grátis + licenças), Business OS.
- R$ 497–697: Thomas Frank (3 níveis, vídeo próprio, FAQ com reembolso), God of Prompt (lista
  nomeada de tudo que entra), Justin Welsh (FAQ com "quem não deve comprar"), Mestre Academy
  (garantia explicada), Expert Cursos (certificado e módulos; cortar pela metade).

Prints da primeira dobra de 20 páginas em `rodada-4-claude/paginas-referencia/`.

## 8. Lacunas para o ChatGPT e o Manus fecharem

- Benchmark de conversão visita→compra de infoproduto no Brasil por faixa de preço (ND em todas
  as fontes públicas que achei).
- Taxa média de reembolso no Brasil por faixa de preço e formato.
- Percentual de Pix gerado e não pago em tráfego frio.
- Efeito medido de desconto Pix na conversão total (não só no mix).
- Teste publicado de advertorial x página direta com números auditáveis.
- Casos do Conar sobre "últimas vagas" e depoimento falso em infoproduto.
- Reputação atual de Cakto e Ticto (Reclame Aqui, estabilidade, casos de bloqueio de saldo).
