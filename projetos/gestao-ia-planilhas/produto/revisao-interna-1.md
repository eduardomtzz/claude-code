# Revisão interna 1 · Kits Essencial e Completo (13/09/2026)

Dois revisores independentes (agentes Claude) abriram cada arquivo da entrega como cliente, sem alterar nada.
Este arquivo guarda os relatórios na íntegra e a triagem. Correções aplicadas ficam marcadas em `## Triagem`.

## Relatório A · Kit Essencial

Testes: recalc 01 (1.661 fórmulas, 0 erros), 02 (190 fórmulas, 3 × #N/A propositais em Painel!K39:M39), 03 (1.193, 0 erros).
PDFs 04: 13 p.; 05: 11 p.; 07: 1 p. Sem caracteres quebrados, sem TODO. 40 prompts numerados (5+8+10+6+6+5), iguais no PDF e no TXT.
PPTX validado, 8 slides, nada fora do slide. Vídeos 1280×720 com áudio, 57,4 / 54,0 / 56,3 s; SRT sincronizados. LEIA-ME lista exatamente os 10 arquivos + videos/.

### GRAVE
1. 04-biblioteca-de-prompts × página/oferta: página promete "quando usar, prompt, exemplo e o que conferir"; "Exemplo" só em 1 de 40; "Quando usar" falta em 11 (Revisar 01–06, Aprender 01–05); "Confira" falta em 2 (Aprender 01 e 04).

### MÉDIO
2. 05-mini-manual p. 6: captura é PDF do LibreOffice ("Sheet 3: Resumo", área branca, gráfico caindo a zero em Out–Dez).
3. Vídeos 01 (16–25 s), 02 (18–30 s), 03 (28–45 s): telas são renders de página do LibreOffice (branco, coluna interna "Ordem", planilha ilegível).
4. Página diz "mini-manual de 13 páginas"; o PDF tem 11.
5. Manual p. 5, 6, 8: diagramação solta (80 % de branco; título + captura sozinhos).
6. 06-modelo-apresentacao slides 3, 5, 7: dados da Rafa Design no deck da Prisma; título "terceiro mês seguido" contradito pelo gráfico (Jun→Jul caiu).
7. 02 Painel!K39:M39: #N/A visíveis em roxo.
8. 02 Resumo!A22 "Mais longe da meta": MAX(ABS) ignora o sentido; escolhe o melhor indicador.
9. 02 Painel!H5:H16 "Acumulado": soma sem sentido para taxa/média/pts.
10. 01 Config!B4 = HOJE() com exemplo fixo em set/2026: em outubro tudo vira "Atrasada".
11. 03 Painel Reserva: categoria Reserva entra como despesa; meses de reserva errado.
12. 06 pptx rodapé "modelo do Seu Sócio Gestor. Troque os textos" em todos os slides.

### LEVE
13. Manual p. 2: "3 min cada" (vídeos têm ~1 min).
14. LEIA-ME: "05-mini-manual.pdf … este guia"; não explica os .srt.
15. 02 Painel!A2 "Nada para preencher" × B18 amarela editável.
16. 02 Painel!B5:C16 formato fixo "#,##0.00" ignora casas decimais de Indicadores!C.
17. 02 Indicadores!B5:B16 Unidade sem lista.
18. 03 Lançamentos!C5:C504 lista com células "" no meio (Config!J9:J16); mesmo padrão em 01 (Config!B9:B16, F9:F16).
19. 01 Config!D9:D12 amarelas mas bloqueadas.
20. 01 Hoje!A10:G21 mostra 12 de 17 sem dizer que é recorte.
21. 06 pptx slide 3: eixo começa em 90; rótulo "meta" encosta no 118,3.
22. videos/*.srt não gravadas no vídeo; legenda 2 do vídeo 02 com 230 caracteres.
23. PDFs 04 e 05 p. 1: viúvas "IA" / "15 minutos" com sublinhado quebrando.
24. Manual p. 3 × "Como usar": "Proteger páginas e intervalos" vs "Proteger intervalos".
25. Página kit.html bônus: "PowerPoint e Google Slides" sugere dois arquivos.

Não verificado: Excel/Sheets reais; FIXED() no locale pt-BR; transcrição da narração.

## Relatório B · Kit Completo

Recalc: 0 erros em 9 planilhas; 3 #N/A intencionais em 02. 80 prompts (40+40); dicionário 60; 4 checklists; slides 8/12/10; durações batem com config.json; áudio ok; SRT ok.

### GRAVE — nenhum.

### MÉDIO
1. 16.pptx slide 8: "receita 1% acima do previsto"; dados 276 × 271,5 (−1,6 %), abaixo. Despesa 240,6/229,4 = +4,9 %.
2. 16.pptx slide 3: "Organizar a casa" 71 % × Painel!C12 = 58 %.
3. 16.pptx slide 2: "veja os slides 7 a 9"; em risco estão 5, 6, 7.
4. aula-01 e aula-04 srt/narração: "Esta aula tem seis minutos" / "Seis minutos, e você nunca mais usa pizza"; vídeos têm 2:25 e 1:59.
5. Legendas (8 .srt): cues de até 320 caracteres e 18,7 s.
6. Prints nos vídeos (aula 4, 5, 8) e manual (p. 5, 8, 10, 12, 13) em formato numérico dos EUA ("R$ 95,559", "131,200.00").
7. 14-manual: (a) sete páginas meio vazias por print na página seguinte; (b) rótulos "Sheet 3: Resumo", "Sheet 5: Resumo", "Sheet 3: Config"; (c) gráfico de 02 caindo a zero.
8. Manual p. 2 "Excel 2016 ou mais novo" × MINIFS/MAXIFS/TEXTJOIN exigem 2019+/365. FAQ da página cita só MÍNIMOSES/MÁXIMOSES; falta UNIRTEXTO.
9. 11-a.txt (texto puro, maiúsculas, só prompts) × 11-b.txt (Markdown completo).
10. 11-a.pdf: capa/rodapé/metadado "Essencial", título sem "Biblioteca A".
11. 06-metas Semanas!C5:O24 vazia no exemplo; página promete histórico; slide 4 do 16 usa Jul/Ago/Set que não existem.
12. 13-checklists p. 2 com 5 linhas.

### LEVE
13. 09-horas: lançamentos desde 01/07 em projetos que começam em ago/set (04 Config, 08 Propostas); "Redes sociais · Clínica" em andamento em 09 mas proposta aberta em 08.
14. 15.pptx slide 5: categorias da Rafa Design; rodapé "Essencial".
15. 01, 02, 03 (Como usar A2) e 15.pptx trazem "Essencial".
16. 13-checklists "5 perguntas (Produzir 20)" × Produzir 20 gera 8; checklist Relatório 7 itens × aula 7 diz 6.
17. 16.pptx slide 11: "nove resultados-chave", lista 8.
18. LEIA-ME e manual p. 2: "40 minutos de leitura" (são ~15).
19. 12-dicionário p. 3–4: coluna "O que faz" estreita.
20. 10-base Como usar!B8 cita verificações que o Checklist não tem.
21. 02 Painel!K39:M39 #N/A visíveis.
22. aula-04 dura 1:59 (promessa "2 a 3 minutos").
23. "PowerPoint e Google Slides" e "versão e data de revisão": só .pptx, sem versão nos modelos.
24. Sobreposição: Aprender 02 ≈ Produzir 06; Analisar 07 ≈ Estruturar 06; Apresentar 03 ≈ Produzir 20.

## Triagem
Tudo será corrigido, exceto: B22 (1 s) e B24 (sobreposição declarada por nota). Ordem: planilhas → telas em pt-BR → PDFs, slides, vídeos → pacote → site.
