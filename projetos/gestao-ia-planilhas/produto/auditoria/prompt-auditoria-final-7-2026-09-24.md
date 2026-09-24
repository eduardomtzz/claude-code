Rodada de confirmação 7 da auditoria final das 53 planilhas do Seu Sócio Gestor. Em anexo,
seu-socio-gestor-auditoria-final-7.zip: os 53 arquivos depois do seu parecer "AUDITORIA FINAL-6 —
REVISÃO AMPLIADA", MUDANCAS-AUDITORIA-FINAL-6.md, a pasta varredura/ (VARREDURA.md, resultados .json
e o código), CENARIOS.md, HASHES.md, DURACOES-AULAS.md, INVENTARIO.md, TRAVAS.md e referencia/.

Mesmo método do seu último parecer, com recálculo forçado dos controles; nada presumido a partir do
meu registro.

O que peço, nesta ordem:

1. CONFIRMAR OU DERRUBAR os sete achados do seu parecer, com os seus contraexemplos:
   F6-G01 · custo-hora −1: 03/06 Simulador!B11; Config!B7 nas 03/08, 04/06 e 04/08; 04/07 Config!B5.
        Esperado: "falta o custo-hora", nada de custo, preço mínimo, margem ou recomendação; zero
        digitado continua valendo; a célula rejeita negativo ao digitar.
   F6-G02 · 03/05 A5 vazio + C5 "abc"; 04/05 A5 vazio + D5 "abc"; 04/07 Config!A11 vazio com tabela
        120 e 25 atendimentos (G5/J5 não podem anunciar vencedor).
   F6-G03 · 03/06 B34 vazio mantendo "Deslocamentos" e "Não" (B39); despesa nova A37/C37 = "Não" sem
        valor; C34 vazio com valor conhecido (B39 soma, D39 avisa).
   F6-G04 · 04/06 L5 = 0 (E25 = 14, E26 = 130,67); 04/08 I8 = 0 (O8 = 3, E5 = 14). Leia a exceção
        do retorno (particular 0 e convênio 0 na mesma linha não é prejuízo) e diga se aceita.
   F6-G05 · 04/07 Config!D19 = −1 e B19 = −1 (C31:G36 suspensos); D19 = 0 continua valendo.
   F6-M01 · 04/06 I5 vazio (K5 e E24); 04/08 H8 vazio (N8 e C5). Particular agora é obrigatório.
   F6-M02 · 03/08 Referência!C9 = 8, D9 = 3 (F9:I9).

2. A VARREDURA NOVA. Leia varredura/VARREDURA.md e o código. Ela agora testa todas as entradas
   preenchidas (sem amostragem), acusa célula calculada que passa de vazia a número, preenche a
   primeira linha vazia de cada coluna de tabela, e as decisões de produto liberam só as saídas
   listadas (erro de fórmula nunca é pulado). Diga se ainda há ponto cego e se alguma exclusão
   esconde defeito. Se puder, rode-a ou reproduza por amostragem, incluindo DUAS entradas inválidas
   ao mesmo tempo, que ela ainda não cobre.

3. REGRESSÃO. Os 23 números do seu apêndice A. Comparação célula a célula com o final-6 (MUDANCAS
   lista os arquivos). HASHES.md etapa 2 contra os arquivos recebidos.

4. ACHADOS NOVOS, se houver: uma linha por causa, com gravidade, arquivo, célula, reprodução,
   consequência e correção proposta. Não conte homologação nativa pendente nem decisões fechadas.

5. VEREDITO POR KIT, na mesma escala, separando: (a) bloqueio do GERADOR ainda aberto e (b)
   pendência de HOMOLOGAÇÃO nativa (Excel 2016 pt-BR e Google Sheets). E só o que MUDA no roteiro
   nativo.

Formato: o mesmo do seu último parecer, com os apêndices.
