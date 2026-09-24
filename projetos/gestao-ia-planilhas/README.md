# Seu Sócio Gestor

Empresa de produtos digitais 100% automáticos: sistemas de gestão em planilhas + ensino de IA
aplicada ao trabalho, com verticais por profissão liberal. Tudo produzido pelo Claude Code;
Eduardo é o gestor e aprovador.

## Status por etapa

| Etapa | Status | Observação |
|---|---|---|
| 1. Pesquisa de nicho | aprovado | 4 rodadas. Rodada 4 (conversão) consolidada em `01-pesquisa/resumo-rodada-4.md`: blueprint das páginas, checkout e pós-compra |
| 2. Oferta | em andamento | `02-oferta/kit-essencial.md`, `02-oferta/kit-completo.md`, `02-oferta/advogados.md` (produto 3, decisões pendentes em DECISOES.md); `02-oferta/dentistas.md` guardada para o produto 5 |
| 3. Produto | em andamento | Kit Essencial e Kit Completo v1 revisados (`produto/revisao-interna-1.md`). Kit para Advogados v1 revisado e corrigido (`produto/revisao-interna-2.md`). Kit para Médicos v1 em `produto/kit-medicos/` (20 planilhas em 5 núcleos, 41 prompts, manual de 4 semanas, 3 bônus, 3 modelos de slides, 8 aulas), revisado por 3 revisores e corrigido (`produto/revisao-interna-3.md`; `dados.py` fonte única, `verifica_coerencia.py` 677 OK, `NUMEROS.md`). Falta: auditoria no GPT, teste em Excel/Sheets reais, narração definitiva (Google TTS) |
| 4. Marca | aprovado | direção D, kit de marca em `03-marca/kit-de-marca/` |
| 5. Copy | em andamento | `04-copy/kit-essencial.md`, `04-copy/kit-completo.md`, `04-copy/advogados.md` (página, obrigado, e-mails, 3 ângulos de anúncio cada) |
| 6. Página | em andamento | base + `/kit/` + `/completo/` + `/advogados/` + `/obrigado/` (3 estados) em `site/`, heróis e inventários com mockup, imagem OG por produto, imagens otimizadas no build, revisadas em celular e desktop. Falta hospedar (Cloudflare Pages), links da Kiwify, e-mails, leitura final do Eduardo |
| 7. Checkout | em andamento | Kiwify decidida. E-mails de entrega e pós-compra prontos em `05-checkout/emails.md`, com checklist de configuração. Falta a conta e os links |
| 8. Rastreamento | em andamento | Código pronto: `site.js` (Pixel com consentimento e `event_id`), `site/functions/api/capi.js` (API de Conversões). Purchase vem da Kiwify. Plano e verificação em `06-tracking.md`. Falta o ID do Pixel e o token |
| 9. Criativos | em andamento | Em `08-ads/criativos/`: vídeo de vendas 9:16, vídeo de 15 s, carrossel de 6 cartões e estáticos com mockup dos três kits, demo do Essencial. Em `08-ads/instagram/`: 15 posts de feed + 15 Stories com legendas. Falta: narração definitiva |
| 10. Tráfego | em andamento | Plano de teste em `08-ads/plano.md`, tetos em `08-ads/limites.json` (pendentes de aprovação em `DECISOES.md`), `matriz.csv`. Liga quando existirem conta, Pixel e Kiwify |

## Escada de produtos e ordem de produção (aprovada em 2026-09-13)

| Ordem | Produto | Página | Preço |
|---|---|---|---|
| 0 | Base do site: home institucional mínima, termos, privacidade, suporte, checkout, Pixel + CAPI, e-mail de entrega | / | — |
| 1 | Kit IA no Trabalho · Essencial (entrada de tudo) | /kit | R$ 37 |
| 2 | Kit IA no Trabalho · Completo (10 planilhas, 80 prompts, 8 aulas curtas) | /completo | R$ 197 |
| 3 | Kit de Gestão para Advogados | /advogados | R$ 497 |
| 4 | Kit de Gestão para Médicos (núcleo de clínica, criado) | /medicos | R$ 697 |
| 5 | Kit de Gestão para Dentistas (clona o núcleo de clínica) | /dentistas | R$ 697 |
| 6 | Kit de Gestão para Entregadores (laboratório de afiliados e orgânico) | /entregadores | R$ 27 |
| 7 | Edição Estética (clone do núcleo de clínica) | /estetica | R$ 497 |
| Pro | Painéis Power BI + atualizações 12 meses (upsell das verticais) | — | R$ 497 |

Regras: um produto só começa a ser produzido depois que o anterior está no ar com ROAS medido.
Cada produto passa por oferta, produto, copy, página, criativos e lançamento. Área do cliente é a
área de membros do checkout; não construímos a nossa. Anúncio nunca cai na home.

Blueprint de páginas, checkout e pós-compra: `01-pesquisa/resumo-rodada-4.md` (entrada obrigatória das
etapas 6 a 8).

Ofertas ficam em `02-oferta/<produto>.md`; produto em `produto/<produto>/`.
