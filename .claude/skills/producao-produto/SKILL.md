---
name: producao-produto
description: Produção do produto digital em si (ebook em PDF/DOCX, planilhas, templates, roteiros de aulas, área de membros) e sua entrega automática após a compra. Use quando o usuário pedir para "criar o ebook", "produzir o curso", "montar a planilha", "escrever o produto" ou "configurar a entrega".
---

# Produção do produto digital

Leia `02-oferta.md`: o sumário do produto e os bônus já estão definidos lá.

## Formatos e ferramentas

| Formato | Como produzir | Skill de apoio |
|---|---|---|
| Ebook / guia | Escrever em Markdown por capítulo, converter com a skill de PDF ou DOCX, capa em SVG com a marca | `anthropic-skills:pdf`, `anthropic-skills:docx` |
| Planilha / calculadora | Construir com fórmulas reais e instruções na primeira aba | `anthropic-skills:xlsx` |
| Templates, checklists, prompts | Markdown, PDF e versão Notion (texto colável) | `anthropic-skills:pdf` |
| Curso em vídeo | Roteiro por aula (gancho, conteúdo, tarefa), slides em PPTX; gravação é do Eduardo | `anthropic-skills:pptx` |
| Área de membros | Hotmart Club, Kiwify Members ou página estática protegida por link único | `checkout-pagamento` |

## Padrão de qualidade

- Cada capítulo ou aula termina com uma ação concreta de 10 minutos.
- Nada de enchimento: se um capítulo não muda o que o leitor faz, corte.
- Linguagem do avatar (use as citações de `01-pesquisa.md`).
- Nome do arquivo e capa com a identidade de `03-marca/`.
- Versão 1 completa antes de polir: entregue o rascunho inteiro, depois revise.

## Entrega automática

- Provedor de checkout entrega o arquivo ou libera a área de membros no evento de compra
  aprovada (webhook). Documente em `05-checkout.md`.
- Email de boas-vindas: assunto, link de acesso, como pedir suporte, lembrete da garantia.
- Teste o fluxo completo com uma compra de R$ 1 (ou modo sandbox) antes do tráfego.

## Saída: `projetos/<slug>/produto/`

`sumario.md`, `capitulos/*.md` ou `aulas/*.md`, arquivos finais (`*.pdf`, `*.xlsx`,
`*.pptx`), `entrega.md` (fluxo, email, links).
