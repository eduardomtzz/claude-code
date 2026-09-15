# Plano de anúncios inicial · Kit Essencial e Kit Completo

Data: 14/09/2026. Estado: **pronto para ligar no dia em que existirem conta de anúncios, Pixel verificado
(`06-tracking.md`) e checkout da Kiwify.** Tetos em `limites.json` (pendentes de aprovação em `DECISOES.md`).

## 1. Economia de cada produto (de `02-oferta/`)

| | Essencial (R$ 37) | Completo (R$ 197) |
|---|---|---|
| Margem líquida por venda (após Kiwify e impostos, estimativa) | ~R$ 28 | ~R$ 157 |
| CPA máximo (100 % da margem) | R$ 28 | R$ 157 |
| CPA alvo (70 %) | R$ 20 | R$ 110 |
| ROAS de equilíbrio | 1,3 | 1,25 |
| ROAS alvo | 1,3 (o Essencial é porta de entrada; empata) | 1,8 |
| Conversão de equilíbrio com clique a R$ 1,50 | 5,4 % | 0,96 % |

Leitura: o Essencial não foi feito para dar lucro em tráfego pago; ele paga o clique e cria a lista de
compradores para o Completo. O Completo é quem precisa de ROAS. Por isso a verba inicial vai
majoritariamente para o Completo, e o Essencial roda como campanha de aquisição barata.

## 2. Estrutura de conta (fase 1 · teste, 14 dias)

Nomenclatura: campanha `SSG-TESTE-VENDAS-2026-09`, conjunto `[PUBLICO]-BR-[IDADE]`, anúncio
`[ANGULO]-[FORMATO]-[HOOK]-v1`. UTMs iguais aos nomes.

**Campanha A · Completo (R$ 197)** · objetivo Vendas · otimização Purchase · ABO

| Conjunto | Público | Orçamento/dia |
|---|---|---|
| `BROAD-BR-25-55` | Brasil, 25 a 55, sem interesse (Advantage+ público) | R$ 60 |
| `INT-PLANILHA-BR-25-55` | interesses: Microsoft Excel, Google Planilhas, Planilhas eletrônicas | R$ 50 |
| `INT-IA-BR-25-55` | interesses: ChatGPT, Inteligência artificial, Produtividade | R$ 50 |
| `INT-GESTAO-BR-25-55` | interesses: Gestão de projetos, Administração de empresas, Empreendedorismo | R$ 40 |

**Campanha B · Essencial (R$ 37)** · objetivo Vendas · otimização Purchase · ABO

| Conjunto | Público | Orçamento/dia |
|---|---|---|
| `BROAD-BR-25-55` | Brasil, 25 a 55, sem interesse | R$ 40 |
| `INT-PLANILHA-IA-BR-25-55` | Excel + Google Planilhas + ChatGPT | R$ 40 |

**Campanha C · Retargeting** (liga a partir do dia 4, quando houver público)

| Conjunto | Público | Orçamento/dia |
|---|---|---|
| `RT-VISITANTES-7D` | visitou /kit/ ou /completo/ nos últimos 7 dias e não comprou | R$ 20 |

Total: R$ 300/dia = teto de `limites.json`. Retargeting entra dentro do teto reduzindo R$ 10 de cada
BROAD.

Regras fixas: Brasil inteiro; posicionamentos automáticos (Advantage+); sem exclusão por atributo pessoal;
página de destino sempre a do produto, nunca a home; Pix e cartão no checkout.

## 3. Criativos por conjunto (3 a 4 por conjunto)

Já existem (`08-ads/criativos/`):

| Arquivo | Uso |
|---|---|
| `essencial-venda-9x16.mp4` | vídeo de vendas 9:16 (dor → custo → 3 passos → prova → preço) |
| `completo-venda-9x16.mp4` | vídeo de vendas 9:16 do Completo (4 passos) |
| `essencial-nao-comece-do-zero-9x16.mp4` | demonstração de tela; retargeting |
| `essencial-produto-1080x1920.png`, `-1080x1080.png` | estáticos com notebook + celular |
| `completo-produto-1080x1920.png`, `-1080x1080.png` | idem, Completo |

Faltam para completar a matriz (produzir na semana 1, sem apresentador, sem narração humana):
- 1 vídeo curto 9:16 (15 s) por produto com hook em texto nos 2 primeiros segundos.
- 1 carrossel por produto (5 cartões: problema, tela 1, tela 2, o que vem, preço).
- 1 estático "prova": tela real + legenda "Tela real. Dados fictícios." + preço.

Copy: os 3 ângulos de `04-copy/kit-essencial.md` e `04-copy/kit-completo.md` (primária curta e média,
5 headlines). Regras: gancho nas 3 primeiras palavras, sem "você" acusatório, sem promessa de renda ou
resultado, sem urgência falsa, preço sempre visível.

## 4. Matriz de testes (uma variável por vez)

Ordem: (1) criativo, (2) ângulo/copy, (3) público, (4) página. Cada célula só é julgada com gasto ≥ 1,5 × CPA
máximo (Essencial R$ 42; Completo R$ 236). Registro em `matriz.csv`.

| Semana | Teste | Hipótese |
|---|---|---|
| 1 | vídeo de vendas × estático mockup × carrossel, no BROAD de cada produto | vídeo ganha em CPA; estático ganha em CTR |
| 1 | ângulo "não comece do zero" × "a IA que você já tem" no Completo | o ângulo IA converte melhor acima de R$ 100 |
| 2 | BROAD × interesses | BROAD empata em CPA com metade do CPM |
| 2 | página /completo/ atual × variante com vídeo da aula 5 no topo | vídeo no topo sobe conversão |

## 5. Regras diárias (executadas uma vez por dia, após 24 h de dados; janela de 3 dias para decidir, 7 para tendência)

Pausar anúncio: gasto ≥ 1,5 × CPA máximo sem compra; ou CTR de link < 0,8 % com CPM acima da média da
conta após 2.000 impressões; ou CPA de 3 dias > 1,5 × CPA máximo com ≥ 3 compras.
Pausar conjunto: todos os anúncios pausados, ou ROAS 7 dias < 60 % do alvo com gasto ≥ 3 × CPA máximo.
Escalar: ROAS 3 e 7 dias ≥ alvo com ≥ 5 compras → +20 % no orçamento (duplicar a partir da terceira subida).
Renovar criativo: frequência > 2,5 em 7 dias ou CTR caiu 30 % contra a primeira semana.
Parar tudo: gasto acumulado sem nenhuma venda ≥ R$ 450 (`pausar_tudo_se_gasto_sem_venda`).
Nunca: mais de 20 % de mudança de orçamento por dia; editar segmentação de conjunto ativo; mexer em
conjunto com menos de 48 h; passar dos tetos.

## 5b. Kit de Gestão para Advogados (R$ 497) · campanha D, liga quando o produto estiver no ar

Economia (de `02-oferta/advogados.md`): margem líquida ~R$ 402; CPA máximo R$ 402; CPA alvo R$ 281; ROAS alvo 1,77.
Conjuntos (ABO, otimização Purchase, Brasil, 27 a 55): `INT-OAB-BR` (interesses: OAB, Direito, advocacia, cargo advogado)
R$ 80/dia; `BROAD-BR-27-55` com criativo que se autosseleciona ("Você advoga o dia inteiro...") R$ 60/dia. Retargeting
7 dias entra no RT geral. Criativos: vídeo de vendas 9:16, estático mockup 9:16 e 1:1, carrossel dos 5 núcleos. Copy:
`04-copy/advogados.md`, 3 ângulos. Tetos: entram em `limites.json` como `kit-advogados` quando o Eduardo aprovar
(sugestão: `cpa_max` 402, `cpa_alvo` 281, `roas_alvo` 1.77; orçamento diário sobe de R$ 300 para R$ 440).

## 6. O que acontece depois da fase 1

- Vencedores de criativo e público vão para uma campanha CBO (ou Advantage+ Shopping) por produto.
- Compradores do Essencial viram público personalizado (lista da Kiwify) para o Completo, com oferta de
  upgrade abatendo os R$ 37 (mecânica de cupom a definir na Kiwify).
- Se o Completo fechar 14 dias com ROAS ≥ 1,8, proposta de subir para R$ 600/dia (nova aprovação).
- Se nenhum produto fizer 5 vendas em 14 dias com R$ 4.500 gastos, pausa geral e revisão de página e
  oferta antes de qualquer verba nova.

## 7. Relatório

Toda segunda: `08-ads/relatorios/semana-N.md` com gasto, compras, CPA, ROAS por campanha/conjunto/anúncio,
o que aprendemos, decisões, orçamento da semana e pedidos ao Eduardo.

## 8. Pendências para ligar

- [ ] Conta de anúncios, Business Manager, Pixel, token CAPI (Eduardo) → `06-tracking.md` verificado.
- [ ] Kiwify com os dois produtos e Pixel/CAPI configurados.
- [ ] Aprovação dos tetos de `limites.json` em `DECISOES.md`.
- [ ] Produzir os criativos que faltam (item 3).
- [ ] Credenciais `META_ACCESS_TOKEN`, `META_AD_ACCOUNT_ID`, `META_PAGE_ID`, `META_IG_ACCOUNT_ID` no ambiente;
      só então escrever e testar `automacao/criar_campanha.py` (cria tudo PAUSED) e `otimizar.py --dry-run`.
