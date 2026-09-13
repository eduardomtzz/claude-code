// Modelo: resultado do trimestre, 12 slides
const {C,H,novo,rodape,titulo,cards,lista,capa,fecho}=require('./slides_base');
const ROD='Kit IA no Trabalho · Completo · modelo do Seu Sócio Gestor. Troque os textos; mantenha a estrutura.';
const p=novo('Resultado do trimestre · modelo de 12 slides');
let s=capa(p,'Resultado do 3º trimestre','Prisma Comunicação · reunião de diretoria · 6 de outubro de 2026','Em uma frase: receita recorrente cresceu 52% e a meta de contratos foi batida; entrega no prazo e retrabalho ficaram para trás.',ROD);
s.addNotes('Capa. A frase em itálico é a conclusão do trimestre em uma linha. Escreva por último.');
// 2 resumo
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O trimestre em três números','Dados da planilha Metas do Trimestre e do Relatório Mensal Pronto.');
cards(p,s,[['R$ 27,4 mil','Receita recorrente mensal','de R$ 18 mil em julho para R$ 27,4 mil em setembro (meta: R$ 30 mil)'],['24','Propostas enviadas','meta batida em setembro; conversão de 57% nas fechadas'],['3 de 9','Metas em risco','entrega no prazo, retrabalho e horas extras: veja os slides 7 a 9']],1.7,2.6,0);
s.addText('Nove resultados-chave: 1 atingido, 5 no ritmo ou em atenção, 3 em risco.',{x:0.5,y:4.5,w:9,h:0.4,fontFace:H,fontSize:13,color:C.TINTA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Resumo. Três números, o melhor, o que bateu meta e o que preocupa. Sem esconder o terceiro.');
// 3 metas painel
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Onde cada objetivo chegou','Progresso médio por objetivo contra 100% do trimestre. Fonte: Metas do Trimestre, aba Painel.');
s.addChart(p.charts.BAR,[{name:'Progresso',labels:['Crescer receita recorrente','Entregar no prazo','Reduzir retrabalho','Organizar a casa'],values:[81,53,57,71]}],
 {x:0.5,y:1.6,w:6,h:3.4,barDir:'bar',chartColors:[C.UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:10,dataLabelColor:C.TINTA,dataLabelFormatCode:'0"%"',catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valGridLine:{color:'E6DFF2',size:0.5},catGridLine:{style:'none'},showLegend:false,valAxisMinVal:0,valAxisMaxVal:100,showTitle:false});
lista(s,['#Leitura','Receita: quase lá; falta um contrato mensal.','Prazo e retrabalho: o gargalo é o mesmo, aprovação do cliente.','Casa: relatório mensal saiu no dia 5 em dois dos três meses.'],6.8,1.7,2.8,3.2,11.5);
rodape(p,s,false,ROD); s.addNotes('Gráfico de barras horizontais por objetivo. Clique no gráfico > Editar dados. Barra é a % média dos resultados-chave.');
// 4 objetivo 1
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Receita recorrente subiu de R$ 18 mil para R$ 27,4 mil por mês','Objetivo 1 · Crescer a receita recorrente · 3 resultados-chave.');
s.addChart(p.charts.LINE,[{name:'Receita recorrente (R$ mil)',labels:['Jul','Ago','Set'],values:[18,22.5,27.4]},{name:'Meta',labels:['Jul','Ago','Set'],values:[30,30,30]}],
 {x:0.5,y:1.6,w:5.4,h:3.4,chartColors:[C.UVA,C.SOL],lineSize:3,lineDataSymbol:'circle',lineDataSymbolSize:7,showValue:true,dataLabelPosition:'t',dataLabelFontSize:9,catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valGridLine:{color:'E6DFF2',size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:10,valAxisMinVal:0,valAxisMaxVal:35,showTitle:false});
lista(s,['#Resultados-chave','2 de 3 contratos mensais novos (Clínica Bem-Estar e Café Central).','24 propostas enviadas: meta batida.','R$ 27,4 mil de R$ 30 mil: 78% do caminho.','#Próximo trimestre','Fechar o terceiro contrato (Escola Nova Era, em negociação).'],6.2,1.7,3.4,3.3,11.5);
rodape(p,s,false,ROD); s.addNotes('Um slide por objetivo: gráfico do resultado-chave principal à esquerda, os outros em lista à direita.');
// 5 objetivo 2
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Entrega no prazo melhorou, mas as etapas atrasadas ainda são 3 por semana','Objetivo 2 · Entregar no prazo.');
cards(p,s,[['82%','Projetos entregues na data','de 60% para 82%; meta 90%'],['3,0','Etapas atrasadas por semana','de 4 para 3; meta 1 (em risco)']],1.65,1.95,-1);
lista(s,['#O que travou','Aprovação do cliente demora 5 a 8 dias nas campanhas.','Uma pessoa concentra 60% das etapas atrasadas (Linha do tempo).','#Ação','Prazo de aprovação de 3 dias no contrato; redistribuir etapas na semana 1 de outubro.'],0.5,3.75,9,1.4,11);
rodape(p,s,false,ROD); s.addNotes('Dois cards de número grande e uma leitura curta. A ação vem da planilha Projetos e Prazos.');
// 6 objetivo 3
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Retrabalho: peças aprovadas de primeira subiram para 60%','Objetivo 3 · Reduzir retrabalho.');
s.addChart(p.charts.BAR,[{name:'Aprovadas de primeira (%)',labels:['Jul','Ago','Set'],values:[40,52,60]}],
 {x:0.5,y:1.6,w:4.6,h:3.3,barDir:'col',chartColors:[C.LILAS],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:10,dataLabelFormatCode:'0"%"',catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valGridLine:{color:'E6DFF2',size:0.5},catGridLine:{style:'none'},showLegend:false,valAxisMinVal:0,valAxisMaxVal:80,showTitle:false});
lista(s,['#Resultados-chave','Rodadas de revisão por peça: 2,8 (meta 2,0), em risco.','Aprovação de primeira: 60% (meta 65%), no ritmo.','#Causa','Briefing incompleto em 4 dos 6 projetos com mais revisão.','#Ação','Checklist de briefing obrigatório antes da primeira peça (prompt Estruturar 08).'],5.4,1.7,4.2,3.3,11.5);
rodape(p,s,false,ROD); s.addNotes('Objetivo 3. Gráfico de colunas simples. Diga a causa como hipótese e a ação com dono.');
// 7 objetivo 4
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Organizar a casa: relatório no dia 5 em dois meses; horas extras ainda altas','Objetivo 4 · Organizar a casa.');
cards(p,s,[['2 de 3','Relatórios enviados até o dia 5','meta 3; em setembro saiu dia 7'],['14 h','Horas extras da equipe no mês','de 20 h para 14 h; meta 8 h (em risco)']],1.65,1.95,-1);
lista(s,['#Leitura','As horas extras concentram-se na última semana do mês, junto do fechamento.','#Ação','Antecipar o fechamento financeiro para o dia 28 e usar a rotina da planilha Orçamento.'],0.5,3.75,9,1.4,11);
rodape(p,s,false,ROD); s.addNotes('Objetivo 4. Mesma estrutura do slide 5.');
// 8 financeiro
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Financeiro: receita 1% acima do previsto, despesa 4% acima','Orçamento Previsto × Realizado, julho a setembro (R$ mil).');
s.addChart(p.charts.BAR,[{name:'Previsto',labels:['Receita','Despesa','Resultado'],values:[276,229.4,46.6]},{name:'Realizado',labels:['Receita','Despesa','Resultado'],values:[271.5,240.6,30.9]}],
 {x:0.5,y:1.6,w:5.6,h:3.4,barDir:'col',chartColors:[C.LILC,C.UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:9,dataLabelFormatCode:'0',catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valGridLine:{color:'E6DFF2',size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:10,showTitle:false});
lista(s,['#O que estourou','Freelancers: +19% (campanha do Bistrô).','Marketing e mídia: +30% (teste de anúncios).','Softwares: +16% (duas assinaturas novas).','#O que fazer','Congelar assinaturas; mídia só com meta de conversão.'],6.4,1.7,3.2,3.3,11.5);
rodape(p,s,false,ROD); s.addNotes('Financeiro do trimestre. Os três números vêm da aba "O ano, mês a mês" somando os três meses.');
// 9 funil
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Comercial: R$ 87,5 mil ganhos, R$ 125 mil em aberto, conversão de 57%','Funil de Propostas em 30/09. Previsão ponderada: R$ 55 mil.');
s.addChart(p.charts.BAR,[{name:'Valor (R$ mil)',labels:['Contato','Reunião feita','Proposta enviada','Negociação'],values:[16.3,31,49.5,28.2]}],
 {x:0.5,y:1.6,w:5,h:3.3,barDir:'bar',chartColors:[C.UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:10,dataLabelFormatCode:'0.0',catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valGridLine:{color:'E6DFF2',size:0.5},catGridLine:{style:'none'},showLegend:false,showTitle:false});
lista(s,['#Onde ganhamos','Indicação converte 100%; Instagram, 50%; site, ainda zero.','#Por que perdemos','Preço (1), concorrente (1), sem resposta (1).','#Ação','Retomar 2 propostas paradas (Construtora Vale, Studio Yoga) esta semana.'],5.8,1.7,3.8,3.3,11.5);
rodape(p,s,false,ROD); s.addNotes('Comercial. Funil por etapa em barras horizontais e três leituras.');
// 10 riscos
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O que pode dar errado no próximo trimestre','Três riscos, a chance de cada um e o que fazemos se acontecer.');
const riscos=[['Cliente grande atrasar aprovação de novo','Provável','Cláusula de prazo e reunião de aprovação marcada no kickoff'],['Terceiro contrato mensal não fechar','Possível','Duas propostas de reserva em negociação; meta cai para R$ 27 mil'],['Equipe no limite em novembro (campanhas)','Provável','Freela contratado até 15/10; férias só em janeiro']];
riscos.forEach((r,i)=>{const y=1.7+i*1.05; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.9,fill:{color:C.LAV},line:{color:C.LAV},rectRadius:0.1});
  s.addText(r[0],{x:0.7,y:y+0.12,w:4.3,h:0.7,fontFace:H,fontSize:12,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(r[1],{x:5.1,y:y+0.12,w:1.2,h:0.7,fontFace:H,fontSize:11,color:r[1]==='Provável'?C.VERM_T:C.CINZA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(r[2],{x:6.4,y:y+0.12,w:3,h:0.7,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'middle'});});
rodape(p,s,false,ROD); s.addNotes('Riscos. Apresentar antes das decisões mostra que você pensou no que pode dar errado. Use o prompt Produzir 20.');
// 11 metas próximas
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Metas do 4º trimestre','Quatro objetivos, nove resultados-chave. Detalhe na planilha Metas do Trimestre.');
const mt=[['Crescer receita recorrente','R$ 35 mil/mês · 4 contratos novos','Ana'],['Entregar no prazo','90% na data · 1 etapa atrasada/semana','Bruno'],['Reduzir retrabalho','2 rodadas/peça · 70% aprovadas de primeira','Carla'],['Organizar a casa','Relatório dia 5 em 3 de 3 · 8 h extras/mês','Ana']];
mt.forEach((m,i)=>{const y=1.65+i*0.82; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.7,fill:{color:i%2?C.BR:C.LAV},line:{color:'DCD2EC',width:0.75},rectRadius:0.08});
  s.addText(m[0],{x:0.7,y:y+0.08,w:3.2,h:0.55,fontFace:H,fontSize:12,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(m[1],{x:4.0,y:y+0.08,w:4.2,h:0.55,fontFace:H,fontSize:11,color:C.TINTA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(m[2],{x:8.3,y:y+0.08,w:1.1,h:0.55,fontFace:H,fontSize:11,color:C.CINZA,isTextBox:true,margin:0,valign:'middle',align:'right'});});
rodape(p,s,false,ROD); s.addNotes('Metas do próximo trimestre com dono. Copie da planilha; não invente meta na hora.');
// 12 decisões
s=fecho(p,'Três decisões que precisamos hoje',['Aprovar a cláusula de prazo de aprovação (3 dias) nos contratos novos.','Aprovar a contratação do freela de motion até 15/10 (R$ 6 mil/mês por 3 meses).','Aprovar o congelamento de assinaturas novas até janeiro.'],ROD);
s.addText('Obrigado. Dúvidas e números completos: planilhas Metas, Orçamento e Funil.',{x:0.5,y:4.5,w:9,h:0.4,fontFace:H,fontSize:12,color:C.LILC,isTextBox:true,margin:0});
s.addNotes('Fechamento: só decisões, com valor e prazo. Peça o sim ou o não antes de encerrar.');
p.writeFile({fileName:'entrega/16-modelo-resultado-do-trimestre-12-slides.pptx'}).then(f=>console.log('ok',f));
