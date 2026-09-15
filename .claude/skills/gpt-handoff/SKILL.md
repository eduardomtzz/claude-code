---
name: gpt-handoff
description: Delegação de tarefas ao ChatGPT do usuário (geração de imagens, deep research, segunda opinião crítica) com prompt pronto para copiar e instruções de como devolver o resultado. Use quando uma tarefa exigir geração de imagem/foto/3D, pesquisa web extensa com muitas fontes, ou quando o usuário pedir "prompt para o GPT" ou "pede ajuda pro ChatGPT".
---

# Handoff para o ChatGPT

O Eduardo tem ChatGPT com geração de imagens e pesquisa profunda. Claude não gera
imagens fotográficas; use esta skill para essas lacunas e para uma segunda opinião
independente.

## Quando delegar

| Tarefa | Delegar? | Prompt base |
|---|---|---|
| Imagens fotográficas, ilustrações, mockups 3D de logo | Sim | `prompts/imagem-marca.md`, `prompts/imagem-anuncio.md` |
| Pesquisa ampla de nicho com dezenas de fontes | Sim, como complemento | `prompts/deep-research-nicho.md` |
| Crítica independente de oferta/copy/página | Sim | `prompts/critica-oferta.md`, `prompts/critica-copy.md` |
| Logo em SVG, código, página, copy, planilhas, automação | Não, é trabalho de Claude | |

## Formato de entrega ao usuário

Sempre entregue:
1. Uma linha dizendo por que delegar.
2. O prompt completo em bloco de código, pronto para colar, já com o contexto do
   projeto preenchido (avatar, marca, paleta, ângulo). Sem placeholders vazios.
3. Onde colar a resposta: caminho do arquivo em `projetos/<slug>/...` ou "cole aqui na
   conversa".
4. O que Claude fará com a resposta ao recebê-la.

## Ao receber a resposta

- Imagens: salvar em `07-criativos/imagens/` ou `03-marca/imagens/` com o nome da
  variação; conferir tamanho e recortar/redimensionar via script se preciso.
- Pesquisa: conferir 3 fontes ao acaso com WebFetch antes de incorporar; marcar o que
  não foi verificado.
- Crítica: listar cada ponto e decidir (aceitar, adaptar, rejeitar com motivo).
