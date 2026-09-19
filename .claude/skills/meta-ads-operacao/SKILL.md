---
name: meta-ads-operacao
description: Planejamento, criação via Marketing API, teste e otimização contínua de campanhas de Meta Ads (Facebook e Instagram) para produto digital, com matriz de testes de público, criativo e copy, regras de pausa e escala, limites de gasto, rotina diária automatizada e relatórios. Use quando o usuário pedir "criar campanhas", "rodar tráfego", "otimizar anúncios", "escalar", "relatório de ads", "testar públicos" ou "automatizar Meta Ads".
---

# Operação de Meta Ads

Pré-requisitos: `06-tracking.md` verificado, `07-criativos/` com pelo menos 6 criativos,
`02-oferta.md` com CPA máximo e ROAS de equilíbrio, e `08-ads/limites.json` aprovado em
`DECISOES.md`.

## Credenciais e acesso

Variáveis: `META_ACCESS_TOKEN` (usuário do sistema com `ads_management`,
`ads_read`, `business_management`), `META_AD_ACCOUNT_ID` (`act_...`), `META_PAGE_ID`,
`META_IG_ACCOUNT_ID`, `META_PIXEL_ID`. Use o SDK `facebook-business` (Python) e a
versão de API mais recente estável. Nunca commitar tokens.

## Estrutura de conta

- Nomenclatura: `[PROJ]-[FASE]-[OBJETIVO]-[DATA]` para campanha,
  `[PUBLICO]-[LOCAL]-[IDADE]` para conjunto, `[ANGULO]-[FORMATO]-[HOOK]-[v1]` para
  anúncio. A nomenclatura alimenta os UTMs e os relatórios.
- Fase 1 Teste (7 a 14 dias): campanha de Vendas, otimização por Purchase, ABO com 4 a
  6 conjuntos (broad, 2 de interesses, 1 lookalike se houver lista, 1 retargeting) e 3
  a 4 anúncios por conjunto. Orçamento por conjunto = CPA máximo × 1 a 2 por dia.
- Fase 2 Consolidação: mover vencedores para CBO ou Advantage+ Shopping, 3 a 5
  anúncios vencedores, retargeting separado (visitantes 7 dias sem compra).
- Fase 3 Escala: aumentar orçamento 20% a cada 48 a 72h enquanto ROAS acima do alvo;
  duplicar conjunto vencedor com novos criativos; expandir públicos e regiões.

## Matriz de testes

Uma variável por vez, em ordem: (1) criativo, (2) ângulo/copy, (3) público, (4)
página. Cada célula precisa de gasto mínimo = 1,5 × CPA máximo antes de julgar.
Registre em `08-ads/matriz.csv`: id, variável, hipótese, início, gasto, resultado,
decisão.

## Regras de decisão (rotina diária)

Executar uma vez por dia, no mesmo horário, após 24h de dados. Usar janela de 3 dias
para decisões e 7 dias para tendência.

Pausar anúncio quando:
- gasto ≥ 1,5 × CPA máximo e zero compras; ou
- CTR (link) < 0,8% e CPM acima da média da conta após 2.000 impressões; ou
- CPA 3 dias > 1,5 × CPA máximo com ≥ 3 compras.

Pausar conjunto quando todos os anúncios pausados ou ROAS 7 dias < 60% do alvo com
gasto ≥ 3 × CPA máximo.

Escalar quando ROAS 3 dias e 7 dias ≥ alvo e ≥ 5 compras: +20% no orçamento (nunca
mais, para não resetar o aprendizado). Duplicar em vez de aumentar quando já subiu 3
vezes.

Renovar criativo quando frequência > 2,5 em 7 dias ou CTR caiu 30% vs. primeira
semana.

Nunca: alterar mais de 20% do orçamento por dia, editar segmentação de conjunto ativo
(duplique), mexer em conjunto em aprendizado com menos de 48h, ultrapassar
`limites.json`.

## Limites (`08-ads/limites.json`)

```json
{"orcamento_diario_max": 0, "gasto_total_max": 0, "cpa_max": 0, "roas_alvo": 0,
 "pausar_tudo_se_gasto_sem_venda": 0, "aprovacao_necessaria_acima_de": 0}
```
Qualquer ação que ultrapasse esses valores é registrada como "pendente de aprovação" e
não executada.

## Automação (`08-ads/automacao/`)

- `criar_campanha.py`: lê `plano.yaml` (públicos, criativos, copies, orçamentos) e cria
  campanha, conjuntos e anúncios em estado PAUSED; ativa só após revisão.
- `otimizar.py`: puxa insights (3 e 7 dias, nível de anúncio), aplica as regras acima,
  grava ações em `log/AAAA-MM-DD.json`, executa as permitidas, lista as pendentes.
- `relatorio.py`: gera `relatorios/semana-N.md` com gasto, compras, CPA, ROAS, vencedores,
  perdedores, próximos testes.
- Agendamento: rotina diária via `create_trigger` (sessão nova) chamando `otimizar.py`
  e, às segundas, `relatorio.py`. Modo `--dry-run` obrigatório na primeira semana.

## Relatório semanal

Resumo em 5 linhas, tabela por campanha/conjunto/anúncio, o que aprendemos sobre
público, criativo e copy, decisões tomadas, orçamento da próxima semana, pedidos ao
Eduardo (novos criativos, fotos, aprovação de escala).
