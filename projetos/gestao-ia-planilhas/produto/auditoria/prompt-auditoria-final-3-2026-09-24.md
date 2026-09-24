Rodada de confirmação 3 da auditoria final das 53 planilhas do Seu Sócio Gestor. Em anexo,
seu-socio-gestor-auditoria-final-3.zip: os 53 arquivos depois do seu parecer "AUDITORIA FINAL-2 —
CONFIRMAÇÃO", MUDANCAS-AUDITORIA-FINAL-2.md (causa reproduzida, o que mudou e o número que prova),
CENARIOS.md (saída literal dos meus cenários), INVENTARIO.md, TRAVAS.md e referencia/.

Mesmo método do seu último parecer: exemplo restaurado antes de cada cenário, contas independentes
onde der, e "validação FALSE" separado de "o aplicativo bloqueou". Não presuma correção a partir do
registro de mudanças nem dos meus cenários: eles são o que eu afirmo, não prova.

O que peço, nesta ordem:

1. CONFIRMAR OU DERRUBAR os cinco achados do seu parecer:
   G01 · 04/06 Config!B7 vazio → Precificação!E22:E26 dizem "falta o custo-hora em Config" (nada de
        0, "0 de 7" ou prejuízo zero). 03/06 Simulador!B11 vazio → C29 "falta o custo-hora".
        Zero digitado continua zero: 04/06 B7 = 0 → E22 = 0 e F5 = 4; 03/06 B11 = 0 → C29 = 0.
   G02 · o predicado único de cada arquivo ("… conferem?" na Config: 03/05 B10, 04/05 B11, 03/06 B13,
        04/06 B13, 04/08 B15; dentro da hora mínima em 03/08 B12:B13 e 04/07 B14) tem as mesmas
        condições da validação e começa por ISNUMBER. Teste nos SETE arquivos de preço (03/05, 03/06,
        03/08, 04/05, 04/06, 04/07, 04/08), em cada célula de imposto, margem e folga: válido, zero,
        soma = 100 %, soma > 100 %, texto, branco, negativo. Na 04/06 e na 04/08, separadamente:
        B9 = B10 = 90 %; só B10 = 90 %; B9 = 60 % e B10 = 30 %; B9 = −30 %. Falha = qualquer hora
        mínima, preço, margem, situação, risco, recomendação, resumo, KPI ou total com número, "No
        alvo" ou "Entre mínimo e alvo" a partir de Config fora do domínio; ou #VALUE! em qualquer aba.
        Confira em especial E23 e K5/B40 da 04/06, os KPIs e a faixa por área da 03/08, os totais do
        mix da 04/07 e O/N/KPIs da 04/08.
   M01 · referencia/numeros-03-advogados.md §13: a linha do checklist é gerada do Checklist da 04 e
        não diz mais que Fernanda Castro pende parcela.
   N01 · referencia/oferta-02-completo.md: as oito descrições da tabela "As 10 planilhas" voltaram;
        a tabela das aulas tem a duração medida (2:25 a 2:56). Se tiver acesso aos vídeos, confira
        as durações; se não tiver, diga NÃO TESTADO.
   L01 · Hoje!A2 das duas cópias de Semana Organizada sem TEXT com código de data; varredura dos 53
        com zero TEXT com código de data. Refaça a contagem por conta própria.

2. OS TRÊS ARQUIVOS NOVOS NO ESCOPO. 03/08 (Tabela de referência), 04/07 (Simulador convênio ×
   particular) e 04/08 (Tabela de preços) tinham a mesma causa de G01/G02 e não estavam no seu
   parecer. Procure neles o que você achou na 04/06: custo-hora em branco apresentado como
   resultado, subtotal ou contagem sobre linhas suspensas, classificação com parâmetro fora do
   domínio, regra de cor que acende com aviso em texto.

3. REGRESSÃO DO EXEMPLO. Com o exemplo intacto, estes números não podem ter mudado:
   03/05 hora mínima 106,5668 → 110; 03/06 B15 120,2612, C29 3.501,7842, D40 3.951,7842,
   recomendação "Hora"; 03/08 hora mínima com folga 127,8801, alvo com folga 168,6929, casos abaixo
   do mínimo "10 de 38"; 04/05 338,9831 → 340; 04/06 E23 338,9831, E24 "0 de 7", E25 14,
   E26 60,4333; 04/07 hora mínima 338,9831, líquido do mês 26.866,58, custo cheio 16.986,67;
   04/08 hora mínima 338,9831, 14 tabelas abaixo do custo cheio + imposto. Compare também, célula a
   célula, os arquivos que o MUDANCAS diz que não mudaram de fórmula nem de dado.

4. CONTROLES NOVOS DO INVENTÁRIO. "TEXT com data" e "Entrega ≠ gerado" foram criados porque L01
   passou pela rodada anterior: o gerador estava certo e a cópia para a entrega não foi feita.
   Diga se a contagem de TEXT com data do inventário bate com a sua.

5. ACHADOS NOVOS, se houver: uma linha por causa, com gravidade (GRAVE / MÉDIO / LEVE), arquivo,
   célula, reprodução, consequência e correção proposta. Não conte homologação nativa pendente nem
   decisões fechadas como defeito.

6. VEREDITO POR KIT, na mesma escala do seu último parecer, e só o que MUDA no roteiro nativo
   (Excel 2016 pt-BR e Google Sheets), incluindo os três arquivos novos no passo de G02.

Formato: o mesmo do seu último parecer (resultado e método; achados abertos em uma linha por causa;
confirmação item a item; regressões; fórmulas exatas das discordâncias; veredito; roteiro; fora do
alcance; hashes dos arquivos recebidos).
