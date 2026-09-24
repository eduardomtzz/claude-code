Rodada de confirmação 5 da auditoria final das 53 planilhas do Seu Sócio Gestor. Em anexo,
seu-socio-gestor-auditoria-final-5.zip: os 53 arquivos depois do seu parecer "AUDITORIA FINAL-4 —
CONFIRMAÇÃO", MUDANCAS-AUDITORIA-FINAL-4.md, CENARIOS.md, HASHES.md, DURACOES-AULAS.md,
INVENTARIO.md, TRAVAS.md e referencia/.

Mesmo método do seu último parecer: exemplo restaurado antes de cada cenário, contas independentes,
"validação FALSE" separado de "o aplicativo bloqueou", e nada presumido a partir do meu registro.

O que peço, nesta ordem:

1. CONFIRMAR OU DERRUBAR os dois achados do seu parecer:
   F4-G01 · dado obrigatório vazio ou em texto:
        03/06: Simulador!B16 ("Dados do caso conferem?") e cada modalidade exigindo só o que usa.
        Repita B45 "abc", B13 vazio, B12 "abc", B44:B48 vazio/texto/negativo/fora de 0–100 %, hora
        com texto no bloco 2 e despesa com texto no bloco 3. Esperado: nenhuma modalidade
        classificada com dado faltando; recomendação "Complete os dados do caso" ou "Corrija horas
        ou despesas"; zero digitado continua valendo.
        04/06 B5 vazio e 04/08 B8 vazio; também "gera retorno?" vazio, retorno da Config vazio,
        material vazio ou texto, preço particular e convênio em texto. Esperado: "faltam os
        minutos" (ou o dado certo), "Faltam dados da linha", resumo e KPIs "n linha(s) ou preço(s)
        incompletos"; nada de 30,67 / 51,98 / "No alvo".
        04/07: glosa, prazo, juros, minutos, retorno e material vazios; prazo zero dispensa juros.
        03/08: valor ou horas do caso em texto; horas típicas em texto.
        03/05 e 04/05: custo fixo em texto ou com nome e sem valor; "já está nos custos fixos?"
        vazio; horas de trabalho em texto.
   F4-G02 · totais sobre a mesma população:
        04/07: B20 vazio com 25 atendimentos → D49 e F49 "líquido incompleto", E49 16.986,67;
        B20 = 0 → F49 = D49 − E49. 04/08: P8 vazio com Q8 preenchido → I5 "volume incompleto",
        K5 vazio; nada de 911,83.

2. REGRESSÃO. Os 23 números do seu apêndice A não podem ter mudado. Compare célula a célula com o
   pacote final-4: o MUDANCAS lista os sete arquivos que mudaram; os outros 46 não podem ter mudado
   de fórmula, dado, validação ou regra. Confira que HASHES.md (etapa 2) bate com os arquivos.

3. MESMA CAUSA EM OUTRO LUGAR. Nos sete arquivos de preço, procure qualquer entrada que ainda vire
   zero, suma de um total ou receba classificação quando vazia ou em texto; e qualquer total ou
   média que some populações diferentes. Separe claramente o que é defeito do que é decisão de
   produto (por exemplo: linha sem nome é ignorada; zero digitado vale).

4. ACHADOS NOVOS, se houver: uma linha por causa, com gravidade (GRAVE / MÉDIO / LEVE), arquivo,
   célula, reprodução, consequência e correção proposta. Não conte homologação nativa pendente nem
   decisões fechadas.

5. VEREDITO POR KIT, na mesma escala, e só o que MUDA no roteiro nativo (Excel 2016 pt-BR e Google
   Sheets).

Formato: o mesmo do seu último parecer, com os apêndices (contas independentes, fórmulas exatas,
comparação contra o pacote anterior, matriz dos cenários e hashes).
