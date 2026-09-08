# AI Quest — RPG 2D para aprender OpenAI, Claude e Manus

Jogo web (roda no navegador do celular e do computador) em que você explora três reinos, um por plataforma de IA, conversa com mentores que ensinam funcionalidades reais e vence batalhas de perguntas para ganhar XP.

Todo o conhecimento vem de arquivos JSON em `public/content/`. O código do jogo não sabe nada sobre as plataformas: trocar ou atualizar uma lição é editar um JSON.

## Rodar localmente

Pré-requisito: Node.js 18 ou mais novo.

```bash
cd game
npm install
npm run dev
```

Abra o endereço que o Vite mostrar (normalmente `http://localhost:5173`). Para testar no celular na mesma rede Wi-Fi, use o endereço `Network:` que aparece no terminal.

Outros comandos:

| Comando | O que faz |
| --- | --- |
| `npm run build` | Checa tipos e gera a versão final em `dist/` |
| `npm run preview` | Serve a pasta `dist/` para testar o build |
| `npm run validate:content` | Valida os JSONs de conteúdo (ids, opções, fontes) |
| `node scripts/make-icons.mjs` | Regera os ícones do PWA |

## Como jogar

- **Mover:** arraste o dedo na metade esquerda da tela (joystick virtual) ou use setas / WASD.
- **Interagir:** botão roxo "A" no canto inferior direito, ou tecla E / Espaço.
- **Mentores** têm um "!" sobre a cabeça. Conversar com um abre a lição (resumo, dicas e fontes) e oferece uma batalha de 4 perguntas sobre aquele tema.
- **Batalha:** acertar causa dano no inimigo (sequências de acertos dão bônus). Errar tira vida sua e mostra a explicação.
- **Chefe** de cada reino libera quando todas as lições do reino estiverem marcadas com ✓. São 8 perguntas misturadas do reino.
- **Progresso** é salvo automaticamente no navegador (localStorage). O botão ☰ no topo abre o menu.

## Estrutura

```
game/
├── index.html              # casca HTML; canvas do Phaser + overlay de UI
├── vite.config.ts          # Vite + PWA (manifest, service worker)
├── public/
│   ├── content/            # PACOTES DE CONTEÚDO (openai, claude, manus, youtube)
│   └── icons/              # ícones do PWA
├── scripts/
│   ├── validate-content.mjs
│   └── make-icons.mjs
└── src/
    ├── main.ts             # configuração do Phaser
    ├── data/world.ts       # mapa, reinos, posições dos NPCs e chefes
    ├── scenes/
    │   ├── BootScene.ts    # gera texturas, carrega conteúdo, tela inicial
    │   ├── WorldScene.ts   # mundo, movimento, interações, chefes
    │   └── HudScene.ts     # joystick virtual e botão de ação
    ├── systems/
    │   ├── content.ts      # tipos e carregamento dos JSONs
    │   ├── save.ts         # progresso em localStorage, XP e níveis
    │   └── textures.ts     # arte gerada em tempo de execução (sem assets binários)
    └── ui/                 # overlay HTML: diálogo, batalha, título, HUD
```

## Atualizar o conteúdo (o coração do projeto)

Cada plataforma tem um arquivo `public/content/<plataforma>.json` com esta forma:

```jsonc
{
  "platform": "claude",
  "name": "Claude (Anthropic)",
  "updatedAt": "2026-09-08",
  "sources": [{ "id": "src-1", "title": "...", "url": "https://...", "type": "docs", "date": "2026-08-01" }],
  "features": [
    { "id": "projects", "name": "Projetos", "category": "chat", "summary": "...", "tips": ["..."], "sourceIds": ["src-1"] }
  ],
  "questions": [
    { "id": "q-projects-1", "featureId": "projects", "type": "multiple_choice", "prompt": "...",
      "options": ["A", "B", "C", "D"], "answer": 2, "explanation": "...", "difficulty": 1 }
  ]
}
```

Regras que o jogo assume:

- As **primeiras 8 funcionalidades** de cada arquivo viram mentores no mapa (há 8 vagas por reino em `src/data/world.ts`). As demais ficam disponíveis só como perguntas de chefe. Para mais mentores, adicione vagas em `npcSlots`.
- Cada funcionalidade precisa de **pelo menos 2 perguntas**. As batalhas completam com perguntas do `youtube.json` da mesma plataforma.
- `answer` é o índice (0 a 3) da opção correta. Varie o índice.
- Rode `npm run validate:content` depois de editar. O build falha se o JSON estiver quebrado.

O arquivo `youtube.json` guarda vídeos (título, canal, URL, dicas extraídas) e perguntas derivadas deles, com `platform` para o jogo saber em qual reino usar.

Para refazer a pesquisa com o Claude Code, use o comando `/refresh-content` descrito em `docs/GUIA-CLAUDE-CODE.md`.

## Publicar (GitHub Pages)

O workflow `.github/workflows/deploy-game.yml` na raiz do repositório faz o build e publica em GitHub Pages toda vez que algo em `game/` chega na branch principal. Veja `docs/GUIA-PROJETO.md` para os passos de ativação.

## Roadmap sugerido

1. Trocar a arte gerada por sprites CC0 (Kenney, OpenGameArt) em `src/systems/textures.ts`.
2. Missões práticas além de quiz (ordenar passos de um fluxo, montar um prompt com peças).
3. Árvore de habilidades ligada às categorias (`category`) das funcionalidades.
4. Som e música (Howler ou o áudio do próprio Phaser).
5. Ranking online (precisa de backend, por exemplo Supabase).
