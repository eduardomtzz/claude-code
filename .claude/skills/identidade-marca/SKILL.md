---
name: identidade-marca
description: Criação de nome, logo (SVG), paleta, tipografia e tom de voz para uma marca de produto digital, a partir de referências e direcionais do usuário. Use quando o usuário pedir "nome para a marca", "logo", "identidade visual", "paleta", "tom de voz" ou antes de construir a página de vendas. Produz 03-marca/.
---

# Identidade de marca

Leia `01-pesquisa.md` e `02-oferta.md`. A marca serve ao avatar, não ao gosto de quem faz.
Peça ao Eduardo referências (marcas que ele admira, prints, cores que gosta ou rejeita)
antes de propor. Se ele não tiver, proponha 3 direções contrastantes e peça escolha.

## Processo

1. **Território.** Três adjetivos que a marca deve transmitir e três que deve evitar.
   Liste 5 marcas de referência no nicho e o que cada uma faz de visual.
2. **Nome.** Gere 20 candidatos em 4 famílias: descritivo, evocativo, inventado,
   composto. Filtre por: pronúncia fácil em português, domínio `.com.br` ou `.com`
   livre (verifique com WebFetch em um registrador), Instagram livre, sem marca
   registrada óbvia no INPI (busca em `busca.inpi.gov.br`). Entregue 5 finalistas com
   justificativa.
3. **Logo.** Construa em SVG puro, sem fontes externas embutidas (converta texto em
   caminhos ou use fonte do Google Fonts com fallback). Entregue: principal,
   horizontal, símbolo isolado, monocromático, versão para fundo escuro. Teste em 32px
   (favicon) e em 1080px (Instagram).
4. **Paleta.** 1 cor primária, 1 de ação (CTA, contraste AA sobre branco e sobre
   escuro), 2 neutras, 1 de apoio. Hex e uso de cada uma.
5. **Tipografia.** Uma display e uma de texto, ambas no Google Fonts, com escala de
   tamanhos. Siga a skill `frontend-design` para evitar o visual genérico.
6. **Tom de voz.** Como a marca fala: 5 frases de exemplo, 5 palavras que usa, 5 que
   nunca usa. Alinhado ao avatar.
7. **Aplicações.** Mockup de avatar do Instagram, capa do ebook, banner 1080x1080 e
   1080x1920 em HTML/SVG. Se precisar de imagens fotográficas ou 3D, delegue ao ChatGPT
   com `gpt-handoff/prompts/imagem-marca.md`.

## Saída: `projetos/<slug>/03-marca/`

`guia.md` (nome, território, paleta, tipografia, tom de voz, regras de uso),
`logo.svg`, `logo-horizontal.svg`, `simbolo.svg`, `logo-mono.svg`, `logo-dark.svg`,
`tokens.css` (variáveis CSS usadas pela página), `aplicacoes/*.html`.

Registre a escolha de nome e direção em `DECISOES.md`.
