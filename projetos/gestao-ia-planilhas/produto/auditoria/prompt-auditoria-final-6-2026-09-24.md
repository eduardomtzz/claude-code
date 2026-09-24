Rodada de confirmação 6 da auditoria final das 53 planilhas do Seu Sócio Gestor. Em anexo,
seu-socio-gestor-auditoria-final-6.zip: os 53 arquivos depois do seu parecer "AUDITORIA FINAL-5 —
CONFIRMAÇÃO", MUDANCAS-AUDITORIA-FINAL-5.md, a pasta varredura/ (VARREDURA.md, resultados .json e o
código), CENARIOS.md, HASHES.md, DURACOES-AULAS.md, INVENTARIO.md, TRAVAS.md e referencia/.

Mesmo método do seu último parecer, com recálculo forçado dos controles; nada presumido a partir do
meu registro.

O que peço, nesta ordem:

1. CONFIRMAR OU DERRUBAR os dois achados do seu parecer, com os seus contraexemplos:
   F5-G01 · 03/05 e 04/05 Config!B9 vazio e "abc"; 04/05 Config!B10 vazio; sensibilidade B42 "abc";
        03/06 B34 vazio mantendo "Deslocamentos" e "Não"; C33 vazio com B33 = 800; B19 = −1; etapa
        com nome e sem horas. Esperado: aviso específico, nada de hora arredondada 0, custo do
        horário vazio 0, #VALUE! ou recomendação com despesa ou hora suposta.
   F5-G02 · 03/08 G5 e F5 "abc" (I5, C57:F57), A5 vazio; 04/08 Q8 vazio com P8 = 130 (G5), Q8 = 0
        (G5 = 17.901 legítimo), A8 vazio com dados na linha; 04/07 glosa C11 vazia (G5/J5), prazo
        B11 = 0 com juros vazio (Saúde Total 103,596), pagador A10 vazio com atendimentos.

2. A VARREDURA. Leia varredura/VARREDURA.md e o código. Diga se o método cobre a causa (uma entrada
   inválida produzindo número ou rótulo sem aviso) e se alguma exclusão da triagem esconde defeito.
   Se puder, rode-a ou reproduza por amostragem, e procure o que ela NÃO cobre: duas entradas
   inválidas ao mesmo tempo, linhas do meio das tabelas longas, células vazias do exemplo que
   recebem dado. Avalie as decisões de "branco = não se aplica" das convenções: aceitar, ou dizer
   por que são defeito.

3. REGRESSÃO. Os 23 números do seu apêndice A. Comparação célula a célula com o final-5 (MUDANCAS
   lista os sete arquivos). HASHES.md etapa 2 contra os arquivos recebidos.

4. ACHADOS NOVOS, se houver: uma linha por causa, com gravidade, arquivo, célula, reprodução,
   consequência e correção proposta. Não conte homologação nativa pendente nem decisões fechadas.

5. VEREDITO POR KIT, na mesma escala, separando com clareza: (a) bloqueio do GERADOR ainda aberto,
   e (b) pendência de HOMOLOGAÇÃO nativa (Excel 2016 pt-BR e Google Sheets). E só o que MUDA no
   roteiro nativo.

Formato: o mesmo do seu último parecer, com os apêndices.
