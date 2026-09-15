---
name: oferta-produto-digital
description: Desenho de oferta para produto digital (formato, promessa, preço, bônus, garantia, escada de valor com order bump e upsell). Use quando o usuário pedir para "criar a oferta", "definir o produto", "precificar", "montar bônus" ou após a pesquisa de nicho. Produz 02-oferta.md.
---

# Oferta de produto digital

A oferta é o que se vende; o produto é só uma parte dela. Copy, página e anúncio derivam
daqui. Leia `01-pesquisa.md` antes.

## Processo

1. **Resultado prometido.** Uma frase: "de [situação atual] para [resultado] em [prazo]
   sem [maior objeção]". Deve ser específico, crível e verificável.
2. **Mecanismo único.** Nome próprio para o método (ex.: "Protocolo 3x7"). Explica por
   que funciona quando o resto falhou. Anote a lógica em 3 passos.
3. **Formato do produto** (escolha pelo que o avatar consome, não pelo mais fácil):
   - Ebook/guia em PDF: baixo ticket (R$ 27 a 97), produção rápida.
   - Curso em vídeo curto ou área de membros: ticket médio (R$ 97 a 497).
   - Planilhas, templates, prompts, checklists: ótimo como front-end ou bônus.
   - Comunidade/mentoria: alto ticket, exige presença do Eduardo.
4. **Equação de valor.** Aumente resultado percebido e probabilidade de sucesso; reduza
   tempo até o resultado e esforço. Cada bônus deve matar uma objeção específica.
5. **Escada de valor:**
   - Front-end (produto principal, ticket de entrada).
   - Order bump (complemento impulsivo, 20 a 40% do preço principal).
   - Upsell 1 (versão acelerada ou feito-para-você, 2 a 4x o principal).
   - Downsell opcional.
6. **Preço.** Ancore no custo da alternativa (curso caro, consultor, tempo perdido).
   Defina preço cheio, preço de lançamento e parcelamento. Calcule ticket médio esperado
   com taxas de order bump e upsell conservadoras (15% e 10%).
7. **Garantia.** 7 dias é obrigatório no Brasil (CDC, art. 49). Ofereça 7, 15 ou 30 dias
   e explique como pedir reembolso.
8. **Economia do funil.** Com preço, ticket médio e margem, calcule o CPA máximo
   aceitável e o ROAS de equilíbrio. Isso alimenta `meta-ads-operacao`.

## Saída: `projetos/<slug>/02-oferta.md`

Seções: Promessa, Mecanismo único, Avatar (resumo), Produto (formato e sumário),
Bônus (nome, objeção que resolve, valor percebido), Escada de valor (tabela), Preços,
Garantia, Economia do funil (tabela: preço, ticket médio, margem, CPA máximo, ROAS de
equilíbrio), Nome provisório da oferta, Perguntas abertas para o Eduardo.

## Regras

- Nenhuma promessa de resultado garantido, renda ou cura.
- Todo bônus listado precisa existir antes do lançamento (ver `producao-produto`).
- Preço final é decisão do Eduardo: registre em `DECISOES.md`.
