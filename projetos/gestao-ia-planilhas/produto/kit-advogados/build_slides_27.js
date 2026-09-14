// Modelo 27: resultado do mês para os sócios, 8 slides. Números: dados.py (casos) e painel 17 (histórico de setembro/2026).
const path=require('path');
const {C,H,ROD,novo,rodape,titulo,cards,lista,tabela,capa,fecho}=require('./slides_base');
const p=novo('Resultado do mês para os sócios · modelo de 8 slides');
const NOTA0='Modelo do Kit de Gestão para Advogados: troque os textos e mantenha a estrutura. ';
// 1 capa
let s=capa(p,'Resultado de setembro de 2026','Ferraz & Lima Advocacia (exemplo fictício) · reunião dos sócios · 2 de outubro de 2026',
 'Em uma frase: melhor caixa do ano (sobrou R$ 9,2 mil), mas 7 prazos atrasados e R$ 21,6 mil vencidos pedem ação esta semana.',ROD);
s.addNotes(NOTA0+'Capa. A frase em itálico é a conclusão do mês em uma linha: escreva por último, depois de montar os outros slides. Os números vêm do Painel do escritório (planilha 17, aba Histórico), do Caixa (09) e da Carteira (13). O prompt "Explicar o mês" ajuda a escrever a frase.');
// 2 resumo
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O mês em três números','Fonte: Painel do escritório (17), Caixa (09) e Carteira de clientes e casos (13).');
cards(p,s,[['R$ 29,4 mil','Receita (entrou no mês)','R$ 27,9 mil em agosto (+5%). Honorários por hora e fixos puxaram; nenhum êxito recebido.'],
 ['R$ 9,2 mil','Resultado (sobrou)','depois de R$ 6,4 mil de custo fixo, R$ 12 mil de pró-labore e R$ 1,8 mil de impostos. Agosto: R$ 7,8 mil.'],
 ['R$ 128,3 mil','A receber','R$ 21,6 mil já vencidos (16,8%). R$ 36 mil são honorários de êxito, que só entram no fim dos casos.']],1.65,2.5,1);
s.addText('Trinta casos ativos com 18 clientes; 318 horas registradas no mês, 226 faturáveis (71%).',{x:0.5,y:4.4,w:9,h:0.4,fontFace:H,fontSize:13,color:C.TINTA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Resumo. Três números: o que entrou, o que sobrou e o que ainda vai entrar. O card destacado é o resultado. Diga o número ruim junto com o bom.');
// 3 prazos e casos
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Prazos da semana e casos ativos','Agenda de prazos (01), semáforo de 2/10. Atrasado é prazo cujo registro na agenda venceu sem baixa.');
cards(p,s,[['13','Prazos nos próximos 7 dias'],['7','Prazos atrasados'],['30','Casos ativos']],1.6,1.35,1);
tabela(s,['Responsável','Prazos na semana','Atrasados','Casos ativos','Horas no mês'],
 [['Marina Ferraz',7,5,19,128],['Rafael Lima',6,2,11,118],['!Escritório','!13','!7','!30','!318']],0.5,3.15,[2.6,1.7,1.5,1.6,1.6],11,0.38);
s.addText('Das 318 horas, 72 são da estagiária. Casos ativos por fase: 6 iniciais, 1 em instrução, 4 em sentença, 5 em recurso, 2 em execução, 8 em acordo e 4 consultivos.',{x:0.5,y:4.55,w:9,h:0.45,fontFace:H,fontSize:11,color:C.CINZA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Prazos. Sete atrasados é o pior número do ano (o histórico do painel mostra 3, 2, 4, 1, 5, 6, 4, 5, 7). Não discuta caso a caso aqui: a lista com número do processo está na Agenda de prazos. Aqui a pergunta é: o que muda na rotina de segunda?');
// 4 horas x faturado
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Horas × faturado por sócio','Receita do mês por hora faturável, comparada ao custo-hora do escritório (planilha 05).');
s.addChart(p.charts.BAR,[{name:'R$ por hora faturável',labels:['Marina Ferraz','Rafael Lima','Custo-hora do escritório'],values:[199,117,73]}],
 {x:0.5,y:1.6,w:4.3,h:3.3,barDir:'col',chartColors:[C.UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:10,dataLabelColor:C.TINTA,dataLabelFormatCode:'"R$ "0',
  catAxisLabelColor:C.CINZA,catAxisLabelFontSize:9,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:false,valAxisMinVal:0,valAxisMaxVal:240,showTitle:false});
tabela(s,['Pessoa','Horas','Faturáveis','Entrou','R$/h'],
 [['Marina Ferraz',128,96,'19.100',199],['Rafael Lima',118,88,'10.300',117],['Júlia Prado',72,42,'—','—'],['!Total','!318','!226','!29.400','!130']],5.0,1.65,[1.5,0.65,0.85,0.85,0.65],9.5,[0.4,0.36,0.36,0.36,0.36]);
lista(s,['#Leitura','12 casos ativos já passaram das horas estimadas (8 da Marina, 4 do Rafael): candidatos a revisão de honorário ou aditivo.','Custo-hora dos sócios de R$ 73, calculado na planilha 05 (custo direto + rateio dos fixos ÷ horas faturáveis).'],5.0,3.6,4.5,1.4,10.5);
rodape(p,s,false,ROD); s.addNotes('Horas por pessoa vêm da planilha 16 (Horas por caso e por pessoa); o "entrou" por sócio, do Caixa (09) filtrado por responsável do caso. Clique no gráfico > Editar dados para trocar os valores. A estagiária não fatura direto, por isso os traços.');
// 5 caixa
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Caixa: entrou × saiu nos últimos três meses','Caixa do escritório (09), aba Painel. Saiu inclui custo fixo, pró-labore e impostos do mês.');
s.addChart(p.charts.BAR,[{name:'Entrou',labels:['Julho','Agosto','Setembro'],values:[23800,27900,29400]},{name:'Saiu',labels:['Julho','Agosto','Setembro'],values:[19888,20064,20179]}],
 {x:0.5,y:1.6,w:5.4,h:3.35,barDir:'col',chartColors:[C.UVA,C.LILC],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:9,dataLabelColor:C.TINTA,dataLabelFormatCode:'#,##0',
  catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valAxisLabelFormatCode:'#,##0',valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:10,valAxisMinVal:0,valAxisMaxVal:35000,showTitle:false});
lista(s,['#Setembro','Entrou R$ 29.400, saiu R$ 20.179, sobrou R$ 9.221 (agosto: R$ 7.836; julho: R$ 3.912).','#Saídas do mês','Custo fixo R$ 6.415 · pró-labore R$ 12.000 · impostos R$ 1.764 (6% da receita, alíquota efetiva combinada com o contador).','#No ano','Sobrou R$ 40,7 mil de janeiro a setembro. Reserva alvo (3 meses de custo fixo com pró-labore): R$ 55,2 mil.'],6.2,1.65,3.4,3.3,10.5);
rodape(p,s,false,ROD); s.addNotes('Caixa. Gráfico de colunas nativo: Entrou e Saiu por mês; a diferença é o que sobrou. Os três meses vêm da aba Histórico do painel. Se o mês fechou negativo, diga primeiro e explique por quê.');
// 6 recebíveis
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Recebíveis e inadimplência','Carteira de clientes e casos (13) e Parcelas e inadimplência (14), posição de 2/10.');
cards(p,s,[['R$ 128,3 mil','A receber','contratado menos recebido, nos 38 casos'],['R$ 21,6 mil','Vencido (16,8%)','R$ 20,9 mil em agosto; R$ 23,6 mil em julho'],['R$ 36,0 mil','Êxito pendente','4 casos; só entra no fim, não conta como atraso']],1.6,1.85,1);
lista(s,['#Por sócio','Marina: R$ 102,8 mil a receber (R$ 26,1 mil de êxito). Rafael: R$ 25,5 mil (R$ 9,9 mil de êxito). Sem êxito: R$ 92,3 mil em 15 casos com parcelas datadas.','#Cobrança','Régua da planilha 14: lembrete no vencimento, mensagem em 7 dias, ligação em 15, reunião em 30. Os modelos de mensagem do kit evitam o constrangimento.'],0.5,3.65,9,1.4,11);
rodape(p,s,false,ROD); s.addNotes('Recebíveis. Separe sempre o que está vencido do que é êxito: êxito sem data não é inadimplência. Se quiser, acrescente a lista dos cinco maiores vencidos da planilha 14.');
// 7 decisões
s=fecho(p,'Três decisões para hoje',['Separar R$ 4.000 do resultado de setembro para a reserva do escritório, todo mês, até chegar a três meses de custo fixo (R$ 55,2 mil).',
 'Casos novos só em modalidade fixa, por hora ou mista: a parte fixa precisa cobrir as horas estimadas. Hoje R$ 36 mil estão parados em quatro casos de êxito.',
 'Contratar mais 20 horas por mês da estagiária (R$ 700) para prazos e cobrança, ou redistribuir os 12 casos acima das horas estimadas? Decidir hoje.'],ROD);
s.addText('Registre a resposta (sim, não, adiado) na ata da reunião antes de passar ao próximo slide.',{x:0.5,y:4.55,w:9,h:0.4,fontFace:H,fontSize:12,color:C.LILC,isTextBox:true,margin:0});
s.addNotes('Decisões. Só o que precisa de sim ou não dos sócios, com valor e prazo. No máximo três: mais que isso vira discussão sem fim.');
// 8 próximos passos
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Próximos passos','Cada linha tem um responsável e uma data. Sem dono, não entra na lista.');
tabela(s,['O que','Quem','Prazo'],
 [['Zerar os 7 prazos atrasados e registrar a baixa na Agenda de prazos (01)','Marina (5) e Rafael (2)','9/10/2026'],
  ['Enviar lembrete de cobrança a todas as parcelas vencidas (modelos do kit)','Júlia Prado','9/10/2026'],
  ['Ligar para os clientes com parcela vencida há mais de 30 dias','Marina e Rafael','16/10/2026'],
  ['Revisar honorário dos 12 casos acima das horas estimadas (planilhas 16 e 06)','Marina Ferraz','23/10/2026'],
  ['Transferir R$ 4.000 para a reserva e registrar na planilha 12','Rafael Lima','28/10/2026'],
  ['Fechar o painel de outubro e enviar o resumo ao contador (planilha 20)','Rafael Lima','5/11/2026']],0.5,1.6,[5.6,2.1,1.3],10.5,[0.38,0.42,0.42,0.42,0.42,0.42,0.42],['l','l','r']);
s.addText('Próxima reunião de resultado: 6 de novembro de 2026, com o fechamento de outubro.',{x:0.5,y:4.65,w:9,h:0.35,fontFace:H,fontSize:11,color:C.CINZA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Próximos passos. Copie para a rotina da semana (planilha 03) e confira na próxima reunião o que foi feito. Não termine com "obrigado": termine com a data da próxima reunião.');
p.writeFile({fileName:path.join(__dirname,'27-modelo-resultado-do-mes-8-slides.pptx')}).then(f=>console.log('ok',f));
