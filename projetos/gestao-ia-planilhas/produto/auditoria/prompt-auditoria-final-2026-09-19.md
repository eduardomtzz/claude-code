Auditoria FINAL das 53 planilhas do Seu Sócio Gestor. Em anexo, seu-socio-gestor-auditoria-final.zip:
os 53 arquivos atuais (depois de nove rodadas), INVENTARIO.md, TRAVAS.md, MUDANCAS-RODADA-9.md e a
pasta referencia/ (triagem completa das nove rodadas, convenções, números de referência e as ofertas).

Esta rodada é diferente das anteriores: não é confirmar uma correção. É a última passada antes da
venda. Quero que você trate o pacote como se nunca o tivesse visto, abra os 53 arquivos e faça a
auditoria mais completa que conseguir, com o rigor das rodadas 3 a 9. Leia LEIA-ME.md e
referencia/TRIAGEM-COMPLETA.md antes, para não reabrir o que está fechado, mas trabalhe nos arquivos,
não nos documentos.

FORMATO DO ACHADO (um por linha, sem elogio, "Nada" quando a seção não tiver achado):
GRAVIDADE | arquivo | aba!célula | reprodução (entrada e saída) | consequência para o cliente | correção sugerida
GRAVE = número errado, dado perdido, arquivo que não abre, instrução que leva a decisão errada de dinheiro,
prazo legal ou atendimento. MÉDIO = funciona mas confunde, quebra em borda previsível ou contradiz outra
parte. LEVE = acabamento. Conte por causa, não por arquivo (uma fórmula repetida em três kits é UM achado).
Se discordar de uma decisão fechada, mostre a fórmula e o teste; sem isso, não conta.

PARTE 1 · ARQUIVO POR ARQUIVO, OS 53
Para cada arquivo, nesta ordem, e diga por escrito o que testou mesmo quando o resultado for "Nada":
a) Fórmulas: referência deslocada (linha ou coluna), intervalo mais curto que a capacidade declarada,
   fixo × relativo errado, divisão por zero, vazio virando zero, texto virando número, data virando
   número, condição invertida, IFERROR escondendo erro real, LOOKUP/OFFSET/SUMPRODUCT fora do previsto.
b) Painel: reconstrua CADA número do painel a partir das abas de lançamento e de Config, com o mês
   escolhido em Config e com pelo menos um outro mês (inclusive um mês sem lançamento e a virada de ano).
c) Bordas: célula vazia, zero digitado, texto colado, negativo, data futura, capacidade cheia (última
   linha da aba de lançamento) e uma linha além da capacidade. Diferencie sempre "vazio" de "zero".
d) Entradas: toda célula amarela desbloqueada e toda fórmula bloqueada; toda lista com a origem certa e
   com bloqueio de erro, salvo as duas deliberadas (regra F); validações customizadas com digitação válida,
   inválida e limite.
e) Regras condicionais: predicado, faixa, prioridade e conflito de cor; INDIRECT resolvendo para a
   referência certa; regra que nunca dispara ou dispara sempre.
f) Gráficos: séries, categorias e títulos apontando para as células certas; o que acontece com texto
   ("Faltam dados", "cadastro incompleto") na série.
g) Textos: "Como usar", notas e rodapés contra o comportamento real (números citados, capacidade,
   instrução de troca de data, o que o caixa registra, o que cada aviso significa). Texto que promete o
   que a fórmula não faz é achado.
h) Impressão e leitura: coluna auxiliar oculta que devia estar oculta, largura que corta número,
   título e nota cobrindo a largura certa, painel abrindo na célula certa.

PARTE 2 · COERÊNCIA DE CADA KIT (o exemplo é um só por kit)
Completo (Prisma Comunicação): projetos da 04 × horas da 09 × propostas da 08 × orçamento 07 ×
relatório 02 (receita, despesa e resultado dos nove meses fecham entre 02 e 07); metas 06 × semanas ×
meses; base 10 × listas.
Advogados: agenda 01 × andamento 02 × carteira 13 × parcelas 14 × caixa 09 × resultado 18 × painel 17
× resumo 20 × metas 19; os 29 casos (cronograma = contrato no fixo, entre fixo e contratado no misto);
proposta 07 × simulador 06 × tabela 08 × custo-hora 05; funil 15 × horas 16.
Médicos: agenda 01 × faltas 02 × cartão 16 × caixa 09 (calendário de liquidação: junho 455,87, julho
346,61, agosto 681,60 de taxa; bruto liquidado 30.490 / 26.720 / 38.010; saldo do painel 38.605,81) ×
convênios 13 × parcelas 14 × repasse 11 × provisão 10 × resultado 18 × painel 17 × resumo 20 × metas 19;
tabela de preços 08 como fonte única (06, 07 e Config da 01 copiam de lá); custo-hora 05 × precificação 06.
Essencial: os três arquivos são idênticos aos do Completo (confira o hash) e a 01 tem datas relativas de
propósito.

PARTE 3 · REGRESSÃO DE TUDO QUE FOI FECHADO NAS NOVE RODADAS
Use referencia/TRIAGEM-COMPLETA.md como lista. Repita pelo menos: G-1 do 03-ganhos (caixa só com
Pago = Sim: 4.173,90 / 4.011,23); 09 do Completo com Config!B11 vazio ("cadastro incompleto" em C5,
F10, H10, J10, F25); 16 dos Médicos com G = 1,5 / 3 / −1 / "Sim" (T = 365,18), a venda de 100 em 3×
(32,03 / 32,03 / 32,04), a identidade bruto = líquido + taxa em 01/08 e 11/08, o calendário de agosto e
setembro; 01 dos Médicos com L906/M906 vazios e com M906 = 0; 11 dos dois kits com trimestre fechado
por data e pelos três meses; 06 dos Advogados sem horas estimadas; 07 dos Advogados com parcela zero;
as cinco chaves de ranking com 379,99 e 380,00; as três metas com os 16 casos de borda, K vazio, todos
os atuais vazios, G6/F6/E6 vazios e zerados, e C6 vazio; as 120 regras com INDIRECT; os 146 TODAY()
restritos às três exceções; o checklist da 10 em B2:B1001.

PARTE 4 · COMPATIBILIDADE EXCEL 2016 E GOOGLE SHEETS, POR LEITURA
Liste toda função usada e marque qualquer uma fora do Excel 2007+; matriz dentro de SUMPRODUCT que o
Excel 2016 avalie diferente do LibreOffice; IF dentro de SUMPRODUCT; N() ou ISNUMBER() sobre intervalo;
INDIRECT com nome de aba com espaço ou acento; OFFSET com COUNTA; FIXED e TEXT com código de formato
(o TEXT só pode ter "dd/mm/yyyy" e "0%"); formato de número e de data dependentes de locale; fórmulas
acima de 8.192 caracteres; validação customizada com referência relativa; regra condicional com
INDIRECT que o Sheets importa; proteção sem senha; gráfico com série de texto. Diga o que você
consegue afirmar por leitura e o que só o teste nativo prova.

PARTE 5 · REFERÊNCIAS E TEXTOS DO PRODUTO
numeros-03 e numeros-04 contra os arquivos: todo número da referência tem de estar no arquivo (o
contrário do que já aconteceu, quando a referência mentia). Convenções A-F: procure uma violação em
qualquer arquivo. Ofertas: cada promessa da oferta (quantidade de planilhas, o que cada uma faz,
capacidade, rotina em minutos) corresponde ao que o arquivo entrega?

PARTE 6 · VEREDITO E ROTEIRO
a) Por kit: pode vender com a promessa "Excel 2016 e Google Sheets"? Separe o que depende do gerador
   (com o achado) do que depende de homologação nativa.
b) Roteiro de homologação nativa para o dono do produto, passo a passo, na ordem de risco: arquivo,
   aba, o que digitar, o que tem de aparecer, o que seria falha. Ele vai executar esse roteiro em
   Excel 2016 e no Google Sheets e me devolver o resultado.
c) Lista de tudo que ficou fora do seu alcance nesta rodada, sem eufemismo.

APÊNDICES: os 53 hashes SHA-256 de entrada; tabela de cobertura (arquivo × itens a-h da parte 1, com
"testado" ou "não testado"); fórmulas exatas de cada achado.
