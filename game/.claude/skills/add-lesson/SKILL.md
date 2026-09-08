---
name: add-lesson
description: Adiciona uma nova funcionalidade (lição) com perguntas ao pacote de conteúdo de uma plataforma do jogo, seguindo o esquema e validando o JSON.
---

# Adicionar uma lição

Argumentos: `$ARGUMENTS` = `<plataforma> "<nome da funcionalidade>"`.

1. Leia `public/content/<plataforma>.json` e o esquema em `README.md`.
2. Pesquise a funcionalidade nas fontes oficiais (WebSearch + WebFetch) e adicione uma `source` com URL e data reais.
3. Crie a `feature` com `id` em kebab-case, `category` válida, `summary` de 2-3 frases e 2-4 `tips` práticas.
4. Crie pelo menos 2 `questions` (4 opções, índice correto variado, `explanation`, dificuldades diferentes).
5. Decida a posição no array `features`: as primeiras 20 aparecem como mentores no mapa. Pergunte ao usuário se a nova lição deve entrar entre elas e em que posição.
6. Rode `npm run validate:content` e mostre o resultado.
