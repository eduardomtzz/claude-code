---
name: playtest
description: Sobe o jogo localmente, abre em um navegador headless com viewport de celular, tira screenshots das telas principais e reporta erros de console. Use após mudanças visuais ou de gameplay.
---

# Playtest automatizado

1. Se `dist/` não existir ou estiver velho, rode `npm run build`.
2. Rode `npm run preview -- --port 4173` em background.
3. Use Playwright (via `npx playwright` ou o MCP do Playwright se estiver configurado) com viewport 390x844 (iPhone) e 360x800 (Android). Para cada um:
   - abra `http://localhost:4173/`, espere a tela de título, tire screenshot;
   - clique em "Começar aventura", espere 1s, tire screenshot do mundo;
   - simule teclado `ArrowUp` por 1s e `e` para falar com o Guia; screenshot do diálogo;
   - colete `console.error` e `pageerror`.
4. Reporte: screenshots (envie ao usuário), erros encontrados, e sugestões de ajuste de layout mobile.
5. Encerre o servidor de preview.
