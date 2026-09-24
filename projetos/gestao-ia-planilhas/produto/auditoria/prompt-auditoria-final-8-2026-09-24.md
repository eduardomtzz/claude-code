Rodada de confirmação 8 da auditoria final das 53 planilhas do Seu Sócio Gestor. Em anexo,
seu-socio-gestor-auditoria-final-8.zip: os 53 arquivos depois do seu parecer "AUDITORIA FINAL-7 —
CONFIRMAÇÃO", MUDANCAS-AUDITORIA-FINAL-7.md, a pasta varredura/ (VARREDURA.md, resultados .json e o
código), CENARIOS.md, HASHES.md, DURACOES-AULAS.md, INVENTARIO.md, TRAVAS.md e referencia/.

Mesmo método do seu último parecer, com recálculo forçado dos controles; nada presumido a partir do
meu registro.

O que peço, nesta ordem:

1. CONFIRMAR OU DERRUBAR os dois achados do seu parecer, com os seus contraexemplos:
   F7-G01 · 04/06 I5 = 0 e L5 = 0 na Consulta (esperado T5 = −130,67, E25 = 14, E26 = 130,67);
        04/08 H8 = 0 e I8 = 0 (esperado O8 = 3, E5 = 14 e vermelho em I8). A exceção agora vale só
        para a linha chamada "Retorno": confira que o Retorno do exemplo continua fora da contagem e
        que renomear a linha do Retorno faz a tabela 0 dela contar. Diga se aceita a identificação
        pelo nome do procedimento.
   F7-M01 · 03/05 E5 = 10 e F5 = 110 (aviso na linha, ocupação não publicada, Painel "cadastro
        incompleto"); E5 = F5 = 110 (100 %, sem aviso); E5 = 160 (68,75 %).
   E também a precisão do apêndice I: as regras de cor da 04/08 (Tabela!I8:M19) agora são
   IF(ISNUMBER(...), teste, FALSE) e não avaliam multiplicação de texto.

2. A VARREDURA. Leia varredura/VARREDURA.md e o código. Novidades: zero e ×10 em cada entrada
   numérica (dado válido, contam só erro e regra violada) e regras de negócio conferidas fora da
   planilha em todo modo (ocupação ≤ 100 %, mínimo ≤ máximo, prejuízo do convênio recalculado).
   Diga se as regras escolhidas cobrem as classes que você achou e quais invariantes faltam.

3. REGRESSÃO. Os 23 números do seu apêndice A. Comparação célula a célula com o final-7 (MUDANCAS
   lista os arquivos). HASHES.md etapa 2 contra os arquivos recebidos.

4. ACHADOS NOVOS, se houver: uma linha por causa, com gravidade, arquivo, célula, reprodução,
   consequência e correção proposta. Não conte homologação nativa pendente nem decisões fechadas.

5. VEREDITO POR KIT, na mesma escala, separando: (a) bloqueio do GERADOR ainda aberto e (b)
   pendência de HOMOLOGAÇÃO nativa (Excel 2016 pt-BR e Google Sheets). E só o que MUDA no roteiro
   nativo.

Formato: o mesmo do seu último parecer, com os apêndices.
