---
name: pagina-vendas
description: Construção e publicação da página de vendas de produto digital (HTML estático rápido, mobile-first, com marca, copy, pixel, checkout, termos e LGPD), incluindo variantes A/B e checklist de conversão. Use quando o usuário pedir "criar a página de vendas", "landing page", "publicar o site", "página de obrigado" ou "melhorar a conversão da página".
---

# Página de vendas

Insumos obrigatórios: `03-marca/tokens.css`, `04-copy.md`, `02-oferta.md`. Siga a skill
`frontend-design` para não cair no visual genérico de IA.

## Stack padrão

- HTML + CSS + JS mínimo, sem framework. Um arquivo por página, CSS em `tokens.css` e
  `site.css`. Imagens em WebP, lazy loading, fontes do Google Fonts com `display=swap`.
- Hospedagem: Cloudflare Pages ou Vercel (gratuito, domínio próprio, HTTPS). Deploy por
  git push; documente o comando em `site/README.md`.
- Páginas: `index.html` (vendas), `obrigado.html` (pós-compra, dispara Purchase se o
  checkout não fizer), `termos.html`, `privacidade.html`, opcional `upsell.html`.

## Estrutura da página (ordem da copy)

Hero com headline, sub e CTA acima da dobra no celular; vídeo (VSL) opcional; seções
na ordem de `04-copy.md`; barra de CTA fixa no mobile após 30% de scroll; rodapé com
CNPJ ou nome do responsável, email de suporte, termos, privacidade e aviso de que o
site não é afiliado ao Facebook/Meta.

## Checklist de conversão

- LCP abaixo de 2,5 s no celular (teste com Lighthouse via Playwright/Chromium local).
- CTA visível a cada duas telas; mesmo verbo em todos.
- Preço aparece antes do FAQ; parcelamento em destaque.
- Botão de compra abre o checkout em nova aba com parâmetros UTM e `fbclid`
  preservados.
- Formulários mínimos; captura de email só se houver sequência pronta.
- Selo de garantia perto do preço; ícones de Pix e cartão.
- Depoimentos com foto e primeiro nome (autorizados).

## Rastreamento

Inclua o snippet de `meta-pixel-capi` no `<head>` de todas as páginas: `PageView` em
todas, `ViewContent` na página de vendas, `InitiateCheckout` no clique do botão,
`Purchase` na página de obrigado ou via webhook do checkout (nunca os dois sem
deduplicação). Parâmetros UTM padrão: `utm_source=meta&utm_medium=paid&utm_campaign=
{{campaign.name}}&utm_content={{ad.name}}`.

## Testes A/B

Use variantes por caminho (`/`, `/b/`) com split no anúncio (50/50 no nível de anúncio)
ou por JS com `localStorage` e evento customizado `Variant`. Só um elemento por teste:
headline, lead, preço exibido ou vídeo x texto. Mínimo de 100 cliques por variante
antes de qualquer conclusão.

## LGPD

Banner simples de cookies com opção de recusar (o pixel só dispara após consentimento
ou em modo de dados limitados), política de privacidade explicando pixel e CAPI, email
para exercício de direitos.

## Saída: `projetos/<slug>/site/`

Código completo, `README.md` com deploy e variáveis, `checklist.md` marcado, captura
de tela mobile e desktop em `site/screenshots/` gerada com Chromium local.
