Rodada de confirmação 4 da auditoria final das 53 planilhas do Seu Sócio Gestor. Em anexo,
seu-socio-gestor-auditoria-final-4.zip: os 53 arquivos depois do seu parecer "AUDITORIA FINAL-3 —
CONFIRMAÇÃO", MUDANCAS-AUDITORIA-FINAL-3.md, CENARIOS.md, HASHES.md, DURACOES-AULAS.md, INVENTARIO.md,
TRAVAS.md e referencia/. Se eu anexar também seu-socio-gestor-aulas-completo.zip, são as oito aulas
do Completo.

Mesmo método do seu último parecer: exemplo restaurado antes de cada cenário, contas independentes,
"validação FALSE" separado de "o aplicativo bloqueou", e nada presumido a partir do meu registro.

O que peço, nesta ordem:

1. CONFIRMAR OU DERRUBAR os três achados do seu parecer:
   F3-G01 · 03/06: Config!B14 ("Regras de risco conferem?") exige B9:B11 numéricos de 0 a 100 % e B12
        Sim/Não. Repita B9 vazio, B10 "abc", B11 "abc", mais zero, negativo, 100 % e 110 % em cada um.
        Esperado: a modalidade que usa o parâmetro diz "Regra de risco inválida (Config)"; Hora não é
        afetada; A5 = "Corrija as regras de risco em Config"; C5 e E5 vazios; A6 pede a correção.
        Nenhuma classificação Alto/Médio/Baixo com parâmetro ausente ou inválido.
   F3-G02 · custo-hora ZERO: 03/06 com B11 = 0, B45 = 50, B47 = 1.000, B48 = 1 % → Fixo Baixo e
        recomendação Fixo (R$ 5.990); com 0,01 → Fixo, R$ 5.989,47. 03/08 B7 = 0, 04/07 B5 = 0,
        04/08 B7 = 0 → "sem base (mínimo zero)" nas comparações percentuais, zero #DIV/0!, zero 0 %
        falso. Confira também que as regras de risco reescritas (Fixo, Êxito, Misto, sem divisão)
        classificam igual às antigas quando os denominadores são positivos; e o êxito ou o valor em
        discussão zero.
   F3-M01 · 03/06 C11 sem #VALUE! e sem "R$ 0,0000" com B11 vazio, "abc" ou 0.

2. OS TRÊS NÃO TESTADOS DO SEU PARECER, agora com material:
   a) validações customizadas com texto: as 18 começam por IF(ISNUMBER(x);AND(...);FALSE); diga se
      "abc" dá FALSE em todas.
   b) entrega × gerado: HASHES.md traz o hash do gerado (antes do pacote) e o da cópia. Confira que
      a coluna da etapa 2 bate com os arquivos que você recebeu.
   c) durações: DURACOES-AULAS.md traz ffprobe, tamanho e SHA-256. Se o zip das aulas vier, meça; se
      não vier, diga NÃO TESTADO.

3. REGRESSÃO. Os 23 números do seu apêndice A não podem ter mudado. Compare célula a célula com o
   pacote final-3: o MUDANCAS lista os sete arquivos que mudaram e o que mudou em cada um; os outros
   46 não podem ter mudado de fórmula, dado, validação ou regra.

4. MESMA CAUSA EM OUTRO LUGAR. Procure nos sete arquivos de preço qualquer divisão, comparação ou
   IFERROR que ainda trate zero legítimo, ausência ou texto como resultado apurado.

5. ACHADOS NOVOS, se houver: uma linha por causa, com gravidade (GRAVE / MÉDIO / LEVE), arquivo,
   célula, reprodução, consequência e correção proposta. Não conte homologação nativa pendente nem
   decisões fechadas.

6. VEREDITO POR KIT, na mesma escala, e só o que MUDA no roteiro nativo (Excel 2016 pt-BR e Google
   Sheets).

Formato: o mesmo do seu último parecer, com os apêndices (contas independentes, fórmulas exatas,
comparação contra o pacote anterior, matriz dos cenários e hashes).
