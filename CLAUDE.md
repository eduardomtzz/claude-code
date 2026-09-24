# Laboratório de Produtos Digitais

Este repositório é a base de operação de um laboratório de produtos digitais: pesquisar nichos,
desenhar ofertas, produzir o produto, criar marca, página de vendas, checkout, rastreamento
(Pixel + Conversions API) e operar Meta Ads em busca de ROAS positivo. Claude executa;
o dono do projeto (Eduardo) dá direcionais, referências, aprova gastos e fornece credenciais.

Idioma de trabalho: português do Brasil. Mercado alvo padrão: Brasil (moeda BRL, Pix, LGPD, CDC).

## Pipeline (ordem obrigatória)

| Etapa | Skill | Saída em `projetos/<slug>/` |
|---|---|---|
| 1. Pesquisa de nicho | `pesquisa-nicho` | `01-pesquisa.md` |
| 2. Oferta | `oferta-produto-digital` | `02-oferta.md` |
| 3. Produto | `producao-produto` | `produto/` |
| 4. Marca | `identidade-marca` | `03-marca/` (logo.svg, tokens.css, guia.md) |
| 5. Copy | `copy-vendas` | `04-copy.md` |
| 6. Página | `pagina-vendas` | `site/` |
| 7. Checkout | `checkout-pagamento` | `05-checkout.md` + código em `site/` |
| 8. Rastreamento | `meta-pixel-capi` | `06-tracking.md` + código |
| 9. Criativos | `criativos-anuncios` | `07-criativos/` |
| 10. Tráfego | `meta-ads-operacao` | `08-ads/` (plano, matriz de testes, relatórios) |

Cada etapa lê as anteriores. Nunca pule a etapa 1 e 2: copy, marca e anúncios sem avatar e
oferta definidos viram retrabalho.

## Convenções

- Um projeto = uma pasta em `projetos/<slug-do-nicho>/`. O `README.md` da pasta tem o status
  atual de cada etapa (não iniciado / em andamento / aprovado).
- Decisões que dependem do Eduardo (nicho escolhido, preço, orçamento, aprovação de marca)
  ficam registradas em `projetos/<slug>/DECISOES.md` com data.
- Quando o ChatGPT puder ajudar (imagens, deep research, segunda opinião), use a skill
  `gpt-handoff`: entregue o prompt pronto para copiar e diga onde colar a resposta.
- Nunca inventar dados de mercado. Toda afirmação numérica na pesquisa cita a fonte ou é
  marcada como estimativa.

## Guardrails de dinheiro e compliance

- Nenhuma campanha é criada ou tem orçamento alterado acima dos tetos definidos em
  `projetos/<slug>/08-ads/limites.json` sem aprovação explícita registrada em `DECISOES.md`.
- Credenciais (token Meta, chaves de checkout) nunca entram no repositório. Vêm por variáveis
  de ambiente: `META_ACCESS_TOKEN`, `META_AD_ACCOUNT_ID`, `META_PIXEL_ID`, `META_PAGE_ID`,
  `META_IG_ACCOUNT_ID`, mais as do provedor de checkout.
- Copy e criativos respeitam as políticas de anúncios da Meta e o Código de Defesa do
  Consumidor: sem promessa de resultado garantido, sem "antes e depois" enganoso, sem
  escassez falsa. Toda página tem Termos, Política de Privacidade e canal de suporte.

## Skills e plugins do projeto

Skills próprias em `.claude/skills/` (uma por etapa do pipeline, mais `gpt-handoff`).
Plugins locais ativados em `.claude/settings.json`: `frontend-design` (páginas e marca sem
visual genérico), `security-guidance` (alerta em código de checkout e webhooks),
`commit-commands`, `feature-dev`.
Plugins do marketplace claude.ai recomendados (instalação pelo Eduardo na interface):
`adspirer-ads-agent` (Meta Ads via MCP), `marketing`, `brand-voice`, `searchfit-seo`.
Skills nativas usadas na produção: `anthropic-skills:pdf`, `docx`, `xlsx`, `pptx`,
`design`, `dataviz`, `artifact-design`.
