# Rastreamento · Pixel da Meta + API de Conversões (CAPI)

Estado em 13/09/2026: código pronto e testado em sintaxe; **falta o ID do Pixel e o token** (só existem
depois de o Eduardo criar a conta de anúncios e o Business Manager). Nada disso entra no repositório.

## Decisão de arquitetura

| Evento | Onde dispara | Como | Dedup |
|---|---|---|---|
| PageView | todas as páginas do site | navegador (Pixel) + servidor (`/api/capi`) | `event_id` igual nos dois |
| ViewContent | `/kit/` e `/completo/` | idem, com `content_ids`, `value`, `currency: BRL` | idem |
| InitiateCheckout | clique em qualquer botão `data-checkout` | idem | idem |
| Purchase | **checkout da Kiwify** (Pixel da Kiwify na página de checkout + API de Conversões nativa da Kiwify no webhook de aprovação) | configurado dentro da Kiwify, com o mesmo Pixel | a própria Kiwify envia o mesmo `event_id` nos dois lados |

O site **não** dispara Purchase. Motivo: a página de obrigado pode ser aberta sem compra (link reenviado,
Pix pendente) e o Purchase só é confiável no evento de pagamento aprovado, que só a Kiwify conhece.
Assim o valor, o `order_id` e o e-mail com hash vêm do servidor da Kiwify, com melhor qualidade de
correspondência (EMQ).

## Onde está o código

- `site/public/assets/js/site.js`: consentimento (ANPD) e a função `SSG.track(nome, params)`. O Pixel só
  carrega depois do aceite de "publicidade". Cada evento gera um `event_id` (UUID), dispara `fbq` com
  `eventID` e envia o espelho para `/api/capi` (sendBeacon). Grava o cookie `_fbc` a partir do `fbclid`.
- `site/functions/api/capi.js`: Cloudflare Pages Function. Valida o evento (só PageView, ViewContent,
  InitiateCheckout, Lead), monta `user_data` com IP, user agent, `fbp`, `fbc` (e e-mail em SHA-256, se um dia
  houver formulário) e envia para `graph.facebook.com/v21.0/{PIXEL_ID}/events`. Sem credenciais, responde
  204 e não faz nada.
- `site/build.py`: o ID do Pixel entra no HTML pela variável de ambiente `META_PIXEL_ID` no momento do build
  (Cloudflare Pages → Settings → Environment variables). `config.json` continua com o campo vazio.
- Página de vendas: `window.SSG.viewContent` define nome, id e valor do produto (`kit.html`, `completo.html`).

## Variáveis de ambiente (Cloudflare Pages, produção e preview)

| Variável | Uso | Onde obter |
|---|---|---|
| `META_PIXEL_ID` | build (HTML) e Function | Gerenciador de Eventos → Fontes de dados → o Pixel |
| `META_CAPI_TOKEN` | só a Function | Gerenciador de Eventos → Configurações → API de Conversões → Gerar token |
| `META_TEST_EVENT_CODE` | só durante o teste | Gerenciador de Eventos → Testar eventos (apagar depois) |

## Configuração na Kiwify (Eduardo)

1. Produto → Pixels → Facebook: informar o **mesmo** `META_PIXEL_ID`; ativar "API de Conversões" e colar o
   token gerado no Gerenciador de Eventos; marcar Purchase (compra aprovada) e, se disponível, InitiateCheckout
   no checkout. Não marcar eventos duplicados com o site (o site já envia ViewContent/InitiateCheckout na
   página de vendas; na página de checkout quem envia é a Kiwify).
2. Domínio `seusociogestor.com.br` verificado no Business Manager (registro DNS ou meta-tag; a meta-tag entra
   em `src/layout.html` quando existir).
3. Configuração de eventos agregados (iOS): Purchase como prioridade 1, InitiateCheckout 2, ViewContent 3.

## Roteiro de verificação (antes de ligar anúncios)

1. Publicar o site com `META_PIXEL_ID`, `META_CAPI_TOKEN` e `META_TEST_EVENT_CODE` definidos.
2. Abrir `/kit/` no celular, aceitar o banner: no Gerenciador de Eventos → Testar eventos devem aparecer
   PageView e ViewContent com origem "Navegador" e "Servidor" e status **"Deduplicado"**.
3. Clicar em Comprar: InitiateCheckout com as duas origens. Fazer uma compra de teste (Pix de R$ 1 se a
   Kiwify permitir, ou cupom): Purchase deve aparecer vindo da Kiwify, com valor e moeda certos, uma vez só.
4. Recusar o banner em outro navegador: nenhum evento pode aparecer, nem do servidor.
5. Extensão Meta Pixel Helper: zero erros, um disparo por evento.
6. EMQ do Purchase ≥ 6 depois das primeiras compras reais. Se ficar abaixo, conferir se a Kiwify está enviando
   e-mail/telefone com hash.
7. Remover `META_TEST_EVENT_CODE` e registrar aqui a data da verificação e as capturas.

## LGPD

- Banner simétrico (aceitar/rejeitar/configurar); Pixel e CAPI só com "publicidade" aceito; sem consentimento,
  nem o servidor recebe evento (o `track` não roda).
- Política de privacidade, item 3 e tabela de fornecedores, já cita Meta, Pixel e API de Conversões e o que
  não é enviado (CPF, telefone em claro, dados de clientes/pacientes).
- `/cookies/` permite mudar a escolha a qualquer momento.

## Pendências

- [ ] Criar conta de anúncios, Business Manager e Pixel; gerar token CAPI (Eduardo).
- [ ] Definir as variáveis no Cloudflare Pages e publicar.
- [ ] Configurar Pixel + CAPI na Kiwify.
- [ ] Rodar o roteiro de verificação e anotar EMQ, data e capturas aqui.
