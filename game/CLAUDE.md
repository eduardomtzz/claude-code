# AI Quest (pasta `game/`)

RPG 2D web em Phaser 3 + TypeScript + Vite, otimizado para navegador mobile, que ensina as plataformas OpenAI, Claude e Manus. Idioma do jogo e dos JSONs: pt-BR.

## Comandos

- `npm run dev` — servidor local (Vite, `--host` para testar no celular)
- `npm run build` — typecheck + build em `dist/`
- `npm run validate:content` — valida `public/content/*.json`; rode sempre depois de editar conteúdo

## Arquitetura (o que importa)

- O código nunca contém fatos sobre as plataformas. Tudo vem de `public/content/{openai,claude,manus,youtube}.json`. Esquema documentado em `README.md`.
- `src/data/world.ts` gera o mapa e as posições. Cada reino tem 20 vagas de mentor (`NPC_SLOTS_PER_REGION`); as primeiras 20 `features` do JSON ocupam as vagas na ordem do arquivo. Reordene o JSON para mudar quem aparece.
- `src/scenes/WorldScene.ts` é o mundo; `src/ui/*.ts` é a interface em HTML por cima do canvas (diálogo, batalha, título). UI de texto fica em HTML, não em objetos Phaser.
- `src/systems/textures.ts` desenha toda a arte em runtime. Não há assets binários além dos ícones PWA.
- Progresso em `localStorage` via `src/systems/save.ts`. Ao mudar o formato, incremente `version` e migre.

## Regras

- Perguntas: exatamente 4 opções, `answer` é índice 0-3, variar o índice, mínimo 2 por feature, `explanation` obrigatória.
- Toda feature precisa de `sourceIds` que existam em `sources`, com URL real fetchada.
- Não invente funcionalidades. Se não conseguir verificar numa página oficial, deixe fora.
- Mobile primeiro: botões com no mínimo 48px de altura, nada depende de hover ou de teclado.
- Commits: `feat:`, `fix:`, `content:`, `docs:`, `chore:`.
