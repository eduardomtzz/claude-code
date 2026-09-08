# Guia do projeto: do zero até o jogo no ar

Este guia é para quem nunca configurou um projeto web. Siga na ordem.

## 1. Ferramentas no seu computador

| Ferramenta | Para quê | Como instalar |
| --- | --- | --- |
| Git | versionar e enviar o código ao GitHub | https://git-scm.com/downloads |
| Node.js (LTS, 20 ou 22) | rodar o Vite e o build | https://nodejs.org (instale a versão LTS) |
| VS Code | editar o código | https://code.visualstudio.com |
| Claude Code | seu par de programação | veja `GUIA-CLAUDE-CODE.md` |

Confira no terminal:

```bash
git --version
node --version
npm --version
```

## 2. Baixar o repositório

```bash
git clone https://github.com/eduardomtzz/claude-code.git
cd claude-code
git checkout claude/ai-platforms-rpg-game-rhrvno
cd game
npm install
npm run dev
```

Abra o endereço mostrado no navegador. Deixe esse terminal aberto enquanto desenvolve: o Vite recarrega a página a cada arquivo salvo.

## 3. Testar no celular

1. Computador e celular na mesma rede Wi-Fi.
2. `npm run dev` já usa `--host`, então o terminal mostra uma linha `Network: http://192.168.x.x:5173`.
3. Abra esse endereço no navegador do celular.
4. Para instalar como app: no Chrome Android, menu ⋮ → "Adicionar à tela inicial". No Safari iOS, botão compartilhar → "Adicionar à Tela de Início". O PWA só é oferecido em HTTPS ou localhost, então no Wi-Fi local ele funciona como site normal. Depois de publicado no GitHub Pages (HTTPS), a instalação aparece.

## 4. Fluxo de trabalho com Git

Este repositório é um fork do `anthropics/claude-code`. O jogo mora na pasta `game/`, isolado do resto. Recomendação: quando o protótipo estiver estável, mova para um repositório só dele (`git subtree split` ou copiar a pasta). Enquanto isso:

```bash
git status                 # o que mudou
git add game               # prepara os arquivos do jogo
git commit -m "feat: ..."  # salva localmente
git push                   # envia ao GitHub
```

Padrão de mensagens de commit: `feat:` (funcionalidade), `fix:` (correção), `content:` (mudança nos JSONs), `docs:` (guias), `chore:` (configuração).

## 5. Publicar no GitHub Pages

1. No GitHub, abra o repositório → **Settings** → **Pages**.
2. Em **Build and deployment**, escolha **Source: GitHub Actions**.
3. O arquivo `.github/workflows/deploy-game.yml` já está no repositório. Ele roda quando a branch `main` recebe mudanças em `game/`. Você também pode dispará-lo manualmente em **Actions** → **Deploy game** → **Run workflow** (funciona em qualquer branch).
4. O endereço final fica `https://<seu-usuario>.github.io/<nome-do-repo>/`.

Se o jogo estiver num fork, o Pages pode vir desativado por padrão. Ative em Settings → Pages. Em repositórios privados, o Pages exige plano pago; torne o repositório público ou use outra hospedagem.

Alternativas gratuitas com HTTPS e domínio próprio: Netlify, Vercel e Cloudflare Pages. Em todas, aponte para a pasta `game`, comando de build `npm run build`, pasta de saída `dist`.

## 6. Atualizar o conteúdo periodicamente

As plataformas mudam todo mês. Rotina sugerida (mensal):

1. Abra o Claude Code na pasta `game/` e rode `/refresh-content claude` (ou `openai`, `manus`).
2. Revise o diff dos JSONs: nomes de funcionalidades, datas em `updatedAt`, links em `sources`.
3. `npm run validate:content` e `npm run dev` para jogar uma batalha do reino alterado.
4. Commit com prefixo `content:` e push. O deploy é automático.

## 7. Problemas comuns

| Sintoma | Causa provável | Solução |
| --- | --- | --- |
| Tela escura com "Erro ao carregar conteúdo" | JSON inválido ou arquivo faltando em `public/content` | `npm run validate:content` |
| Joystick não aparece | toque começou na metade direita da tela | arraste a partir da metade esquerda |
| Jogo pequeno demais ou grande demais | zoom automático por tamanho de tela | ajuste o `14` em `applyZoom()` em `WorldScene.ts` |
| Personagem atravessa parede | tile novo sem colisão | adicione o índice em `COLLIDES` em `world.ts` |
| Alterações não aparecem no celular após deploy | cache do service worker | feche todas as abas do jogo e abra de novo; o PWA atualiza sozinho na próxima carga |
