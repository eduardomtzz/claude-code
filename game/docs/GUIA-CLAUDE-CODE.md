# Guia: configurar o Claude Code para este projeto

O Claude Code é a ferramenta com que você vai evoluir o jogo e atualizar o conteúdo. Este guia cobre instalação, os arquivos de configuração que já estão no repositório e como usar cada um.

## 1. Instalar e entrar

```bash
# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

Depois:

```bash
cd caminho/para/claude-code/game
claude
```

Na primeira vez ele pede login. Use sua conta claude.ai (planos Pro, Max ou Team liberam o Claude Code) ou uma chave da API. Documentação oficial: https://code.claude.com/docs/en/setup

Também existe a extensão para VS Code e JetBrains (procure "Claude Code" no marketplace) e o modo web em https://claude.ai/code, que roda em um container na nuvem e abre PRs no seu GitHub. Esta sessão que criou o jogo é um exemplo do modo web.

## 2. O que já está configurado no repositório

| Arquivo | Para quê |
| --- | --- |
| `game/CLAUDE.md` | Memória do projeto. O Claude Code lê automaticamente ao abrir a pasta. Descreve arquitetura, regras de conteúdo e comandos. |
| `game/.claude/settings.json` | Permissões pré-aprovadas para os comandos rotineiros (npm run dev/build/validate). Evita pedir confirmação a cada vez. |
| `game/.claude/skills/refresh-content/SKILL.md` | Skill `/refresh-content <plataforma>`: pesquisa os sites oficiais e o YouTube e atualiza o JSON. |
| `game/.claude/skills/add-lesson/SKILL.md` | Skill `/add-lesson`: adiciona uma funcionalidade nova com perguntas seguindo o esquema. |
| `game/.claude/skills/playtest/SKILL.md` | Skill `/playtest`: sobe o jogo, abre no Chromium headless, tira screenshots de celular e checa erros no console. |

Abra o Claude Code sempre dentro de `game/` para que o `CLAUDE.md` certo seja carregado. Se abrir na raiz do repositório, o arquivo `game/CLAUDE.md` também é lido quando você mexe em arquivos dentro de `game/`.

## 3. Configurações pessoais (fora do repositório)

Ficam em `~/.claude/settings.json` e valem para todos os projetos. Exemplos úteis:

```json
{
  "permissions": {
    "allow": ["Bash(git status)", "Bash(git diff *)", "Bash(git log *)"]
  },
  "includeCoAuthoredBy": true
}
```

Comandos dentro do Claude Code que você vai usar:

| Comando | O que faz |
| --- | --- |
| `/init` | cria um CLAUDE.md inicial (já feito aqui) |
| `/memory` | edita o CLAUDE.md do projeto ou o seu pessoal (`~/.claude/CLAUDE.md`) |
| `/permissions` | vê e ajusta o que é permitido sem perguntar |
| `/model` | troca de modelo (Opus para tarefas grandes, Sonnet para rotina, Haiku para coisas simples) |
| `/compact` | resume a conversa quando o contexto ficar cheio |
| `/clear` | começa uma conversa nova |
| `/plan` ou Shift+Tab | modo plano: ele propõe antes de mexer |
| `/mcp` | gerencia servidores MCP conectados |
| `/hooks` | configura ganchos (ex.: rodar o validador antes de cada commit) |
| `/schedule` | cria rotinas agendadas (ex.: pesquisa mensal de conteúdo) |
| `/skills` | lista skills disponíveis, inclusive as deste projeto |

## 4. Fluxos recomendados

### Atualizar o conteúdo de uma plataforma

```
/refresh-content claude
```

O Claude vai pesquisar as fontes oficiais, comparar com o JSON atual, propor um diff e rodar `npm run validate:content`. Revise as mudanças antes de commitar. Faça uma plataforma por vez para o diff ficar legível.

### Adicionar uma lição à mão

```
/add-lesson openai "Modo de voz avançado"
```

### Mudar o jogo

Comece descrevendo o resultado esperado, não a implementação. Exemplo: "Quero que as batalhas de chefe tenham um cronômetro de 20 segundos por pergunta, com penalidade se estourar". Peça o modo plano para mudanças grandes.

### Rotina mensal automática (opcional)

Dentro do Claude Code:

```
/schedule
```

Crie uma rotina mensal com o prompt: "Rode /refresh-content para openai, claude e manus, valide, e abra um PR com as mudanças de conteúdo". A rotina roda na nuvem e você só revisa o PR.

## 5. Servidores MCP úteis para este projeto

MCP (Model Context Protocol) conecta o Claude Code a ferramentas externas. Adicione com `claude mcp add`. Candidatos úteis aqui:

- **GitHub** (já vem no modo web): abrir PRs, ler issues.
- **Playwright** (`npx @playwright/mcp`): navegar no jogo de verdade e tirar screenshots durante o desenvolvimento.
- **Fetch/Browser**: para a pesquisa de conteúdo quando o `WebFetch` embutido não bastar.

## 6. Hooks sugeridos

Em `game/.claude/settings.json` já existe um hook `PreToolUse` que roda `npm run validate:content` antes de qualquer `git commit`. Se o JSON estiver quebrado, o commit é bloqueado. Para desligar, remova o bloco `hooks`.

## 7. Boas práticas que os vídeos mais assistidos repetem

Estas dicas também estão dentro do jogo, no Reino Claude:

- Mantenha o `CLAUDE.md` curto e específico: comandos, convenções, o que não fazer.
- Use `@arquivo` para apontar exatamente o que ele deve ler.
- Peça plano antes de mudanças grandes; revise o plano; só então execute.
- `/compact` quando a conversa ficar longa; `/clear` ao trocar de assunto.
- Subagentes para pesquisa em paralelo, como foi feito para gerar este conteúdo.
- Hooks para regras que não podem falhar (lint, validação), em vez de confiar na memória do modelo.
