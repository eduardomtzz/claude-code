---
name: pesquisa-nicho
description: Pesquisa e avaliação de nichos para produtos digitais. Use quando o usuário pedir para "estudar nichos", "encontrar um nicho", "validar um mercado", "comparar nichos" ou antes de qualquer oferta nova. Produz 01-pesquisa.md com avatar, dores, concorrência, ofertas existentes e nota de viabilidade.
---

# Pesquisa de nicho

Objetivo: decidir se vale a pena entrar num nicho e com qual ângulo, com evidência, não opinião.

## Entradas

- Direcionais do Eduardo: nichos candidatos, interesses, restrições (ex.: "nada de saúde").
- Referências que ele passar (links, prints, concorrentes).
- Se nada foi passado, proponha 5 nichos candidatos e peça escolha antes de aprofundar.

## Processo

1. **Mapa do nicho.** Defina em uma frase: quem sofre, com o quê, e o que já tentou.
2. **Coleta de evidência** (use WebSearch/WebFetch; registre cada fonte):
   - Demanda: Google Trends (12 meses e 5 anos), volume de buscas das 10 palavras-chave
     principais, tendência subindo/estável/caindo.
   - Concorrência paga: Biblioteca de Anúncios da Meta (`facebook.com/ads/library`),
     filtrar Brasil. Liste 5 a 10 anunciantes ativos há mais de 30 dias: são os que dão
     lucro. Anote ângulo, formato, promessa e preço aparente.
   - Ofertas existentes: marketplaces Hotmart, Kiwify, Eduzz, Monetizze; Amazon (livros
     e avaliações); Udemy. Anote preço, formato, temperatura do produto.
   - Voz do cliente: comentários no YouTube, TikTok, Reddit (r/brasil e subs do tema),
     grupos e avaliações. Copie 15 a 30 frases literais de dor, desejo e objeção.
3. **Avatar.** Um parágrafo em primeira pessoa: situação, dor, tentativa fracassada,
   desejo, medo, o que precisaria acreditar para comprar.
4. **Pontuação (0 a 5 cada, some):**
   - Dor urgente e consciente
   - Poder e hábito de compra online
   - Concorrência ativa (sinal de dinheiro), mas com brecha de ângulo
   - Facilidade de produzir o produto digital
   - Tamanho de público no Brasil (estimativa de interesses na Meta)
   - Compliance simples (evitar saúde, dinheiro fácil, relacionamento agressivo)
   Nota abaixo de 20/30: descarte ou reposicione.
5. **Ângulos de entrada.** 3 ângulos possíveis (mecanismo único, subnicho, formato novo).

## Saída: `projetos/<slug>/01-pesquisa.md`

Seções: Resumo (5 linhas), Avatar, Evidência de demanda, Concorrentes pagos (tabela),
Ofertas existentes (tabela), Voz do cliente (citações), Pontuação, Ângulos, Riscos,
Recomendação, Fontes.

Ao final, atualize `projetos/<slug>/README.md` e proponha a decisão a registrar em
`DECISOES.md`.

## Delegar ao ChatGPT

Para uma segunda camada de pesquisa ampla, use `gpt-handoff` com
`prompts/deep-research-nicho.md`. Traga a resposta para `01-pesquisa.md` como seção
"Pesquisa complementar (GPT)", conferindo as fontes antes de aceitar números.
