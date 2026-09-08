---
name: refresh-content
description: Atualiza o pacote de conteúdo de uma plataforma (openai, claude ou manus) pesquisando os sites oficiais e vídeos recentes do YouTube. Use quando o usuário pedir para atualizar, revisar ou refrescar o conteúdo do jogo.
---

# Atualizar conteúdo de uma plataforma

Argumento: `$ARGUMENTS` = `openai`, `claude` ou `manus`. Sem argumento, pergunte qual.

## Passos

1. Leia `public/content/<plataforma>.json` inteiro e o esquema em `README.md` (seção "Atualizar o conteúdo").
2. Pesquise as fontes oficiais com WebSearch e WebFetch:
   - openai: openai.com (news, product), help.openai.com, platform.openai.com/docs, developers.openai.com
   - claude: anthropic.com/news, claude.com, support.claude.com, code.claude.com/docs, platform.claude.com/docs
   - manus: manus.im (blog, docs em manus.im/docs), help.manus.im
   Busque também no YouTube por vídeos dos últimos 3 meses sobre a plataforma (em inglês e português) e extraia dicas das descrições. Não invente URLs de vídeo: confirme cada um.
3. Compare com o JSON atual. Para cada feature: ainda existe? mudou de nome, plano ou limite? há feature nova relevante? Prefira **editar** entradas existentes a criar novas, para manter os `id`s estáveis (o progresso salvo dos jogadores usa esses ids).
4. Atualize `summary`, `tips`, `sources` (com `date` real) e `questions`. Toda feature nova precisa de 2+ perguntas. Se uma feature foi descontinuada, remova a feature e as perguntas dela.
5. Atualize `updatedAt` para a data de hoje.
6. Rode `npm run validate:content`. Corrija até passar sem erros.
7. Mostre ao usuário um resumo em pt-BR: features adicionadas, alteradas, removidas, e o que não conseguiu verificar. Não faça commit sem o usuário pedir.

## Regras

- Só inclua o que foi verificado numa página realmente fetchada. Na dúvida, deixe fora.
- Perguntas: 4 opções, índice correto variado, `explanation` de 1-2 frases, dificuldade 1-3 misturada.
- Texto em pt-BR, claro para quem não é programador.
