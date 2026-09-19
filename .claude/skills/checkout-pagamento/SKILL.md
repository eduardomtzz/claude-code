---
name: checkout-pagamento
description: Escolha e integração do checkout para produto digital no Brasil (Kiwify, Hotmart, Eduzz, Stripe, Mercado Pago), com Pix e cartão, order bump, upsell em um clique, webhooks de entrega e evento Purchase deduplicado. Use quando o usuário pedir "configurar checkout", "integrar pagamento", "order bump", "upsell", "webhook de compra" ou "entrega automática".
---

# Checkout e pagamento

Leia `02-oferta.md` (escada de valor e preços) e `producao-produto/entrega.md`.

## Decisão de plataforma

| Opção | Quando usar | Prós | Contras |
|---|---|---|---|
| Kiwify | Padrão para infoproduto BR | Pix, cartão, order bump, upsell 1 clique, área de membros, pixel e CAPI nativos, saque rápido | Taxa por venda |
| Hotmart | Quer afiliados e marketplace | Maior rede de afiliados, Club | Taxa maior, checkout menos flexível |
| Eduzz / Monetizze | Alternativa com afiliados | Similar à Hotmart | Menos integrações |
| Stripe | Produto global ou SaaS | Controle total via API, assinaturas | Sem Pix nativo simples no BR, exige código, sem afiliados |
| Mercado Pago | Checkout próprio no Brasil | Pix e cartão, API boa, taxas competitivas | Você constrói order bump, upsell e entrega |

Recomendação padrão: Kiwify no início (velocidade). Migrar para checkout próprio
(Mercado Pago ou Stripe) só quando o volume justificar a economia de taxa. Registre a
escolha em `DECISOES.md`.

## Configuração (plataforma pronta)

1. Produto principal, order bump e upsell criados com nomes e preços de `02-oferta.md`.
2. Checkout com a cor de ação da marca, logo, selo de garantia, Pix e cartão em até
   12x, campo de telefone (recuperação por WhatsApp).
3. Página de obrigado apontando para `site/obrigado.html` com os parâmetros da venda.
4. Pixel e CAPI configurados na plataforma **ou** no site, nunca nos dois sem
   `event_id` compartilhado (ver `meta-pixel-capi`).
5. Webhook de "compra aprovada", "reembolso" e "carrinho abandonado" apontando para um
   endpoint seu (Cloudflare Worker ou Vercel Function) que: entrega o produto, envia o
   email, registra a venda em `vendas.csv`/planilha, e dispara Purchase via CAPI se a
   plataforma não fizer.
6. Recuperação de carrinho: sequência de emails de `04-copy.md` e mensagem de WhatsApp
   (manual ou via API oficial).

## Checkout próprio (quando escolhido)

- Backend mínimo: função serverless que cria a cobrança (Pix com QR e copia-e-cola;
  cartão tokenizado), recebe o webhook do provedor, valida assinatura, idempotência por
  `payment_id`, entrega e dispara CAPI.
- Order bump: checkbox no formulário que altera o valor antes de criar a cobrança.
- Upsell: página pós-compra com cobrança em um clique usando o cartão tokenizado
  (Stripe) ou novo Pix (Mercado Pago).
- Nunca armazenar dados de cartão. Logs sem dados pessoais além do necessário (LGPD).

## Testes obrigatórios antes do tráfego

Compra real de valor mínimo com Pix e com cartão; reembolso; conferir entrega, email,
evento Purchase no Gerenciador de Eventos com valor e moeda corretos e deduplicado.

## Saída: `projetos/<slug>/05-checkout.md` e código em `site/api/`

Documento com plataforma, IDs, links de checkout por produto, fluxo do webhook,
variáveis de ambiente necessárias e resultado dos testes.
