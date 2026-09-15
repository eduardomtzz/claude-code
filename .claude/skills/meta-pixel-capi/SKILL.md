---
name: meta-pixel-capi
description: Instalação e verificação do Pixel da Meta e da Conversions API (CAPI) em páginas de vendas e checkouts, com eventos padrão, parâmetros, deduplicação por event_id, dados avançados com hash, teste no Gerenciador de Eventos e consentimento LGPD. Use quando o usuário pedir "instalar o pixel", "configurar CAPI", "rastrear conversões", "evento Purchase" ou "Gerenciador de Eventos".
---

# Pixel da Meta e Conversions API

Sem rastreamento correto, a otimização de anúncios é cega. Esta etapa é bloqueante para
`meta-ads-operacao`.

## Variáveis

`META_PIXEL_ID`, `META_CAPI_TOKEN` (token do Gerenciador de Eventos, nunca no cliente),
`META_TEST_EVENT_CODE` (só durante testes).

## Eventos e onde disparam

| Evento | Onde | Parâmetros |
|---|---|---|
| PageView | todas as páginas | automático |
| ViewContent | página de vendas | `content_name`, `content_ids`, `value`, `currency: BRL` |
| InitiateCheckout | clique no botão de compra | `value`, `currency`, `content_ids` |
| AddPaymentInfo | checkout (se próprio) | idem |
| Purchase | obrigado ou webhook (CAPI) | `value` (líquido de order bump/upsell somados), `currency`, `content_ids`, `order_id` |
| Lead | captura de email (se houver) | `content_name` |

## Deduplicação

Gere um `event_id` único por evento no navegador (`crypto.randomUUID()`), envie no
pixel e no CAPI com o mesmo `event_name`. Purchase: se o checkout é de terceiro (Kiwify,
Hotmart), ative o CAPI nativo deles e **não** dispare Purchase no site; se dispara no
site, use `order_id` como `event_id` nos dois lados.

## Implementação no site

- Snippet base do pixel no `<head>` com `fbq('init', PIXEL_ID)` e `fbq('track',
  'PageView')` só após consentimento (ver LGPD abaixo).
- Eventos customizados via função `track(name, params)` em `site/js/tracking.js` que
  chama `fbq` e envia POST para `/api/capi` com `event_id`, `event_source_url`,
  `fbp`, `fbc`, `client_user_agent`.
- Endpoint `/api/capi` (Worker/Function): monta `user_data` com `em`, `ph`, `fn`, `ln`
  em SHA-256 quando disponíveis, `client_ip_address`, `fbp`, `fbc`; envia para
  `https://graph.facebook.com/v21.0/{PIXEL_ID}/events` com `access_token`.
- Advanced Matching automático ligado no Gerenciador de Eventos.

## Verificação (obrigatória)

1. Extensão Meta Pixel Helper: sem erros, um disparo por evento.
2. Gerenciador de Eventos, aba "Testar eventos" com `test_event_code`: cada evento
   aparece com "Navegador" e "Servidor" e status "Deduplicado".
3. Qualidade da correspondência de eventos (EMQ) do Purchase: alvo 6 ou mais.
4. Domínio verificado no Business Manager e evento Purchase priorizado na
   configuração de eventos agregados.

## LGPD

Pixel só após consentimento no banner; antes disso, nada dispara (ou use
`fbq('consent','revoke')` e `grant` após aceite). Política de privacidade cita Meta,
pixel, CAPI e finalidade.

## Saída: `projetos/<slug>/06-tracking.md`

IDs, mapa de eventos, onde cada um dispara, capturas do "Testar eventos", EMQ, data da
verificação. Código em `site/js/tracking.js` e `site/api/capi.*`.
