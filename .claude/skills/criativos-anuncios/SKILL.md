---
name: criativos-anuncios
description: Produção de criativos para Meta Ads (estáticos, carrossel, roteiros de vídeo e UGC, hooks, ângulos e variações nomeadas), nas especificações corretas, com prompts para gerar imagens no ChatGPT. Use quando o usuário pedir "criar criativos", "anúncios em imagem", "roteiro de vídeo para ads", "hooks", "variações de anúncio" ou antes de subir campanhas.
---

# Criativos de anúncio

Leia `04-copy.md` (ângulos) e `03-marca/`. Objetivo por rodada: 6 a 12 criativos que
cubram pelo menos 3 ângulos e 2 formatos.

## Ângulos (escolha 3 por rodada)

Dor direta, desejo/resultado, mecanismo único, prova/história, objeção invertida
("não é mais um curso"), comparação com o jeito antigo, curiosidade/segredo,
identificação ("se você é X que...").

## Formatos e especificações

| Formato | Tamanho | Uso |
|---|---|---|
| Estático feed | 1080×1080 | teste inicial, mais barato de produzir |
| Estático vertical | 1080×1350 e 1080×1920 | feed e stories/reels |
| Carrossel | 1080×1080, 3 a 5 cartões | mecanismo em passos, módulos, antes/depois de processo |
| Vídeo curto | 9:16, 15 a 45 s, legenda embutida | reels e stories, melhor CPM |
| UGC/fala para câmera | 9:16, 30 a 60 s | gravado pelo Eduardo ou creator |

Texto na imagem: no máximo uma ideia, fonte da marca, contraste alto, sem miniaturas
ilegíveis. Botão de CTA desenhado na imagem aumenta cliques.

## Estrutura de vídeo

Hook 0 a 3 s (padrão visual ou frase que interrompe), problema 3 a 10 s, mecanismo 10
a 30 s, prova, oferta e CTA. Escreva o roteiro com coluna de fala e coluna de
imagem/texto na tela.

## Produção

- Estáticos e carrosséis: HTML/SVG com `tokens.css`, renderizados em PNG via Chromium
  local (`site/tools/render.js`). Um arquivo por variação.
- Imagens fotográficas ou ilustradas: delegue ao ChatGPT com
  `gpt-handoff/prompts/imagem-anuncio.md` e integre o PNG recebido.
- Vídeo: entregue roteiro, texto na tela e briefing de gravação; edição em CapCut ou
  ferramenta do Eduardo.

## Nomenclatura

`[ANGULO]-[FORMATO]-[HOOK]-v[N]` (ex.: `dor-est1080-semtempo-v2`). Mesmo nome no
arquivo, no anúncio e na matriz de testes.

## Saída: `projetos/<slug>/07-criativos/`

`briefing.md` (ângulos, hooks, copies pareadas), `estaticos/*.html` e `*.png`,
`carrosseis/`, `videos/roteiro-*.md`, `prompts-gpt/*.md`, `indice.csv` (nome, ângulo,
formato, copy primária, headline, status).
