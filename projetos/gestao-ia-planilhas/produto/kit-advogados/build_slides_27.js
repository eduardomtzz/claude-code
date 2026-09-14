// Modelo 27: resultado do mês para os sócios, 8 slides. Agosto de 2026 fechado, apresentado na reunião de sócios de 14/09/2026.
// Números: NUMEROS.md (18 Resultado mensal, 09 Caixa, 16 Horas, 01 Agenda, 13 Carteira, 14 Parcelas, 12 Reserva, 05 Custo-hora).
const path=require('path');
const {C,H,NOTA0,novo,slide,titulo,cards,lista,tabela,capa,fecho}=require('./slides_base');
const p=novo('Resultado do mês para os sócios · modelo de 8 slides');
// 1 capa
let s=capa(p,'Resultado de agosto de 2026','Ferraz & Lima Advocacia (exemplo fictício) · reunião dos sócios · segunda-feira, 14 de setembro de 2026',
 'Em uma frase: agosto deu resultado de R$ 5.688 (margem de 21 %), abaixo de julho; mas 7 prazos atrasados e R$ 14.480 vencidos hoje pedem ação esta semana.');
s.addNotes(NOTA0+'Capa. A frase em itálico é a conclusão do mês em uma linha: escreva por último, depois de montar os outros slides. Os números vêm do Resultado mensal (18, Config = Agosto), do Caixa (09), das Horas (16) e da Carteira (13); a posição de prazos e parcelas é a de hoje (01 e 14). O prompt "Painel 01 · Explicar o mês ao sócio" ajuda a escrever a frase.');
// 2 resumo
s=slide(p); titulo(s,'O mês em três números','Fonte: Resultado mensal (18) e Caixa do escritório (09), agosto fechado; Carteira (13) e Parcelas (14) na posição de 11/09.');
cards(p,s,[['R$ 26.900','Receita (entrou no mês)','R$ 29.460 em julho (−8,7 %). Honorários fixos R$ 15.300 e consultoria e pareceres R$ 11.290; nenhum êxito nem hora em agosto.'],
 ['R$ 5.688','Resultado (margem 21,1 %)','depois de R$ 6.500 de custo fixo, R$ 560 de despesas de casos, R$ 12.000 de pró-labore e R$ 2.152 de impostos provisionados (8 %). Julho: R$ 8.293 (28,2 %).'],
 ['R$ 111.990','A receber','R$ 14.480 já vencidos em 8 parcelas (inadimplência 5,1 %). R$ 30 mil são êxito puro de 5 casos, que só entra no fim.']],1.65,2.5,1);
s.addText('Trinta casos ativos com 18 clientes; 304 horas registradas em agosto, 248 faturáveis (81,6 %).',{x:0.5,y:4.4,w:9,h:0.4,fontFace:H,fontSize:13,color:C.TINTA,isTextBox:true,margin:0});
s.addNotes('Resumo. Três números: o que entrou, o que sobrou e o que ainda vai entrar. O card destacado é o resultado. Diga o número ruim junto com o bom. O resultado da DRE (18) não é o que sobrou no caixa (09: R$ 5.003): a DRE provisiona 8 % de impostos em vez da guia paga e deixa fora as despesas pessoais dos sócios (11).');
// 3 prazos e casos
s=slide(p); titulo(s,'Prazos da semana e casos ativos','Agenda de prazos (01), semáforo de hoje, 14/09. Atrasado é prazo cujo registro na agenda venceu sem baixa.');
cards(p,s,[['14','Prazos de hoje e dos próximos 7 dias'],['7','Prazos atrasados'],['30','Casos ativos']],1.6,1.35,1);
tabela(s,['Responsável','Prazos abertos','Atrasados','Hoje','Em alerta (7 dias)','Horas em agosto'],
 [['Marina Ferraz',15,3,2,4,'111,5'],['Rafael Lima',16,3,1,5,'112,0'],['Júlia Prado (estagiária)',5,1,0,2,'80,5'],['!Escritório','!36','!7','!3','!11','!304,0']],0.5,3.15,[2.6,1.3,1.2,1.0,1.5,1.4],11,0.36);
s.addText('Casos ativos por fase (02): 7 consultivos, 8 iniciais, 4 em instrução, 3 em sentença, 3 em recurso, 3 em execução e 2 em acordo. Quatro parados há mais de 30 dias.',{x:0.5,y:4.98,w:8.4,h:0.5,fontFace:H,fontSize:10,color:C.CINZA,isTextBox:true,margin:0,valign:'top'});
s.addNotes('Prazos. Sete atrasados, quatro deles vencidos entre sexta e domingo: o que a rotina de sexta deixou passar. Não discuta caso a caso aqui: a lista com número do processo está na Agenda de prazos. A pergunta é: o que muda na rotina de segunda? A Júlia responde pelas juntadas de documentos; os casos continuam com o sócio.');
// 4 horas x custo-hora
s=slide(p); titulo(s,'Horas de agosto contra a meta e o custo-hora','Horas por caso e por pessoa (16) e Custo-hora do escritório (05).');
s.addChart(p.charts.BAR,[{name:'Horas faturáveis em agosto',labels:['Marina Ferraz','Rafael Lima','Júlia Prado'],values:[101.5,88,58.5]},{name:'Meta de faturáveis por mês',labels:['Marina Ferraz','Rafael Lima','Júlia Prado'],values:[110,110,60]}],
 {x:0.5,y:1.6,w:4.4,h:3.3,barDir:'col',chartColors:[C.UVA,C.LILC],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:9,dataLabelColor:C.TINTA,dataLabelFormatCode:'0',
  catAxisLabelColor:C.CINZA,catAxisLabelFontSize:9,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:9,valAxisMinVal:0,valAxisMaxVal:130,showTitle:false});
tabela(s,['Pessoa','Horas','Faturáveis','% fat.','Custo-hora'],
 [['Marina Ferraz','111,5','101,5','91 %','R$ 72,76'],['Rafael Lima','112,0','88,0','79 %','R$ 72,76'],['Júlia Prado','80,5','58,5','73 %','R$ 41,55'],['!Escritório','!304,0','!248,0','!82 %','!R$ 66,07']],5.1,1.65,[1.45,0.7,0.85,0.65,0.85],9.5,[0.4,0.36,0.36,0.36,0.36]);
lista(s,['#Leitura','Custo-hora do escritório R$ 66,07 (R$ 18.500 ÷ 280 h faturáveis) e hora mínima a cobrar R$ 110 (planilha 05).','Dois casos ativos já passaram das horas estimadas (16): Bistrô 42, 50 h para 45, êxito sem nada recebido; Escola Aurora, 100 h para 90.'],5.1,3.6,4.4,1.5,10);
s.addNotes('Horas por pessoa vêm da planilha 16 (Painel, Config = Agosto); custo-hora e hora mínima, da 05. Clique no gráfico > Editar dados para trocar os valores. Os sócios ficaram perto ou acima da meta de 110 h faturáveis: o gargalo é agenda, não demanda.');
// 5 caixa
s=slide(p); titulo(s,'Caixa: entrou × saiu nos últimos três meses','Caixa do escritório (09), aba Painel. Saiu inclui custo fixo, pró-labore, guia de impostos e despesas de casos.');
s.addChart(p.charts.BAR,[{name:'Entrou',labels:['Junho','Julho','Agosto'],values:[27420,29460,26900]},{name:'Saiu',labels:['Junho','Julho','Agosto'],values:[23085,28898,21897]}],
 {x:0.5,y:1.6,w:5.4,h:3.35,barDir:'col',chartColors:[C.UVA,C.LILC],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:9,dataLabelColor:C.TINTA,dataLabelFormatCode:'#,##0',
  catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valAxisLabelFormatCode:'#,##0',valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:10,valAxisMinVal:0,valAxisMaxVal:35000,showTitle:false});
lista(s,['#Agosto','Entrou R$ 26.900, saiu R$ 21.897, sobrou R$ 5.003 (julho: R$ 562, com a distribuição do 2º trimestre; junho: R$ 4.335).','#Saídas de agosto','Custo fixo R$ 6.500 · pró-labore R$ 12.000 · guia de impostos R$ 2.357 (8 % das entradas de julho) · custas e deslocamento R$ 560 · despesa pessoal a acertar R$ 480.','#No ano','Sobrou R$ 21.783 de janeiro a agosto; saldo em caixa R$ 43.683. Reserva alvo (3 meses de custo fixo com pró-labore): R$ 55.500; guardado: R$ 12.000.'],6.2,1.65,3.4,3.4,10);
s.addNotes('Caixa. Gráfico de colunas nativo: Entrou e Saiu por mês; a diferença é o que sobrou. Os três meses vêm do Painel mensal do Caixa (09) ou da aba Histórico do painel (17). Se o mês fechou negativo, diga primeiro e explique por quê.');
// 6 recebíveis
s=slide(p); titulo(s,'Recebíveis e inadimplência','Carteira de clientes e casos (13) e Parcelas e inadimplência (14), posição de sexta, 11/09.');
cards(p,s,[['R$ 111.990','A receber','contratado menos recebido, nos 30 casos ativos'],['R$ 14.480','Vencido (5,1 %)','8 parcelas; R$ 12.500 (4,5 %) no fim de agosto; R$ 8.900 (3,6 %) em julho'],['R$ 30.000','Êxito pendente','5 casos de êxito puro; só entra no fim, não conta como atraso']],1.6,1.85,1);
lista(s,['#Cobrar primeiro (14)','Seis parcelas com mais de 30 dias: Bistrô 42 (2 × R$ 2.100, 150 e 180 dias), Fernanda Castro (R$ 1.400, caso encerrado), Oficina Mecânica Central (R$ 1.500), Patrícia Gomes (R$ 2.100) e Agência Prisma (R$ 1.800).','#Régua da planilha 14','1 dia: lembrete gentil · 7 dias: mensagem do responsável pelo caso · 15 dias: e-mail com demonstrativo e proposta de renegociação · 30 dias: ligação ou reunião e plano por escrito. Os modelos do bônus 22 seguem a régua.'],0.5,3.65,9,1.45,10.5);
s.addNotes('Recebíveis. Separe sempre o que está vencido do que é êxito: êxito sem data não é inadimplência. Inadimplência = vencido ÷ (pago + vencido), a mesma conta em todo o kit. A lista "Cobrar primeiro" da planilha 14 ordena por valor × dias de atraso.');
// 7 decisões
s=fecho(p,'Três decisões para hoje',['Separar R$ 3.000 por mês para a reserva do escritório, a partir de setembro, até chegar a três meses de custo fixo (R$ 55.500; hoje R$ 12.000, meta em dezembro de 2027 pela planilha 12).',
 'Casos novos só em modalidade fixa, por hora ou mista: a parte fixa precisa cobrir as horas estimadas. Hoje R$ 30 mil estão parados em cinco casos de êxito puro.',
 'Contratar mais 20 horas por mês da estagiária (R$ 467, na proporção da bolsa atual de R$ 1.400 por 60 h faturáveis) para juntadas e cobrança, ou redistribuir os prazos entre os sócios? Decidir hoje.']);
s.addText('Registre a resposta (sim, não, adiado) na ata da reunião antes de passar ao próximo slide.',{x:0.5,y:4.7,w:9,h:0.4,fontFace:H,fontSize:12,color:C.LILC,isTextBox:true,margin:0});
s.addNotes('Decisões. Só o que precisa de sim ou não dos sócios, com valor e prazo. No máximo três: mais que isso vira discussão sem fim.');
// 8 próximos passos
s=slide(p); titulo(s,'Próximos passos','Cada linha tem um responsável e uma data. Sem dono, não entra na lista.');
tabela(s,['O que','Quem','Prazo'],
 [['Zerar os 7 prazos atrasados e registrar a baixa na Agenda de prazos (01)','Marina (3), Rafael (3) e Júlia (1)','18/09/2026'],
  ['Enviar a mensagem da régua para as 8 parcelas vencidas (modelos 04 a 07 do bônus 22)','Júlia Prado','16/09/2026'],
  ['Ligar para os clientes com parcela vencida há mais de 30 dias e registrar o plano por escrito','Marina e Rafael','25/09/2026'],
  ['Revisar o honorário dos 2 casos acima das horas estimadas (planilhas 16 e 06)','Rafael (Bistrô 42) e Marina (Escola Aurora)','30/09/2026'],
  ['Transferir R$ 3.000 para a reserva e registrar na planilha 12','Rafael Lima','28/09/2026'],
  ['Fechar setembro e enviar o resumo ao contador (planilhas 18 e 20)','Rafael Lima','05/10/2026']],0.5,1.6,[5.4,2.4,1.2],10,[0.38,0.42,0.42,0.42,0.42,0.42,0.42],['l','l','r']);
s.addText('Próxima reunião de resultado: 5 de outubro de 2026, com o fechamento de setembro.',{x:0.5,y:4.75,w:9,h:0.35,fontFace:H,fontSize:11,color:C.CINZA,isTextBox:true,margin:0});
s.addNotes('Próximos passos. Copie para a rotina da semana (planilha 03) e confira na próxima reunião o que foi feito. Não termine com "obrigado": termine com a data da próxima reunião.');
p.writeFile({fileName:path.join(__dirname,'27-modelo-resultado-do-mes-8-slides.pptx')}).then(f=>console.log('ok',f));
