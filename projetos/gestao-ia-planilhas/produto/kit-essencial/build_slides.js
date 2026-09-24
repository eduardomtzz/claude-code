// Bônus do Kit IA no Trabalho · Essencial: modelo de apresentação de 8 slides (relatório mensal)
const pptxgen = require('pptxgenjs');
const UVA='3B1F5E', SOL='FFC83D', LILAS='7A5AA8', LILC='B89BE0', LAV='F3EEFB', TINTA='1F1235', BR='FFFFFF', CINZA='5A4A78';
const pres = new pptxgen(); pres.layout='LAYOUT_16x9'; pres.author='Seu Sócio Gestor'; pres.title='Relatório mensal · modelo de 8 slides';
const H='Arial';
function simbolo(s, x, y, k, dark){ // três degraus + ponto (marca), k = escala em polegadas
  const c1= dark? LILC : LILAS, c2= dark? BR : UVA;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:x, y:y+0.40*k, w:0.42*k, h:0.14*k, fill:{color:c1}, rectRadius:0.06*k, line:{color:c1}});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:x+0.10*k, y:y+0.22*k, w:0.42*k, h:0.14*k, fill:{color:c2}, rectRadius:0.06*k, line:{color:c2}});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:x+0.20*k, y:y+0.04*k, w:0.42*k, h:0.14*k, fill:{color:c2}, rectRadius:0.06*k, line:{color:c2}});
  s.addShape(pres.shapes.OVAL,{x:x+0.62*k, y:y+0.44*k, w:0.13*k, h:0.13*k, fill:{color:SOL}, line:{color:SOL}});
}
function rodape(s, dark){
  s.addText('Kit IA no Trabalho · modelo v1.0 · set/2026',{x:0.5,y:5.24,w:7.5,h:0.22,fontFace:H,fontSize:7,color:dark?LILAS:LILC,isTextBox:true,margin:0});
  simbolo(s, 9.0, 5.05, 0.55, dark);
}
function titulo(s, txt, sub){
  s.addText(txt,{x:0.5,y:0.35,w:9,h:0.8,fontFace:H,fontSize:26,bold:true,color:UVA,isTextBox:true,margin:0,valign:'top',fit:'shrink'});
  if(sub) s.addText(sub,{x:0.5,y:1.12,w:9,h:0.35,fontFace:H,fontSize:12,color:CINZA,isTextBox:true,margin:0});
}
// 1 · Capa
let s=pres.addSlide(); s.background={color:UVA};
simbolo(s,0.5,0.5,1.0,true);
s.addText('Relatório de setembro',{x:0.5,y:1.9,w:9,h:0.9,fontFace:H,fontSize:40,bold:true,color:BR,isTextBox:true,margin:0});
s.addText('Prisma Comunicação · apresentado à diretoria · 5 de outubro de 2026',{x:0.5,y:2.85,w:9,h:0.4,fontFace:H,fontSize:16,color:LILC,isTextBox:true,margin:0});
s.addText('Em uma frase: receita e resultado cresceram; conversão de leads e despesas pedem atenção.',{x:0.5,y:3.6,w:8.5,h:0.7,fontFace:H,fontSize:14,color:BR,italic:true,isTextBox:true,margin:0});
rodape(s,true);
s.addNotes('Modelo do Seu Sócio Gestor: troque os textos e mantenha a estrutura. Capa. Troque mês, empresa, público e data. A frase em itálico é a conclusão do mês em uma linha: escreva por último.');
// 2 · Resumo do mês
s=pres.addSlide(); s.background={color:BR};
titulo(s,'Setembro fechou com R$ 41 mil de resultado, 11% acima de agosto','Três números que resumem o mês. Os demais estão no relatório completo.');
const kp=[['R$ 131 mil','Receita','+5% vs. agosto · meta R$ 120 mil'],['R$ 89,8 mil','Despesas','+3% vs. agosto · acima da meta'],['R$ 41,4 mil','Resultado','+11% vs. agosto · meta R$ 35 mil']];
kp.forEach((k,i)=>{const x=0.5+i*3.1; s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:x,y:1.75,w:2.9,h:2.4,fill:{color:i==2?SOL:LAV},line:{color:i==2?SOL:LAV},rectRadius:0.12});
  s.addText(k[0],{x:x+0.25,y:1.95,w:2.5,h:0.9,fontFace:H,fontSize:30,bold:true,color:UVA,isTextBox:true,margin:0,fit:'shrink'});
  s.addText(k[1],{x:x+0.25,y:2.85,w:2.5,h:0.4,fontFace:H,fontSize:14,bold:true,color:UVA,isTextBox:true,margin:0});
  s.addText(k[2],{x:x+0.25,y:3.25,w:2.5,h:0.7,fontFace:H,fontSize:11,color:CINZA,isTextBox:true,margin:0,valign:'top'});});
s.addText('10 dos 12 indicadores no alvo. Fora da meta: despesas e taxa de conversão de leads.',{x:0.5,y:4.4,w:9,h:0.5,fontFace:H,fontSize:13,color:TINTA,isTextBox:true,margin:0});
rodape(s,false); s.addNotes('Resumo do mês. Use os três números que mais importam para quem ouve. O texto abaixo dos cards vem da aba Resumo da planilha Relatório Mensal Pronto.');
// 3 · Destaque positivo 1 (gráfico)
s=pres.addSlide(); s.background={color:BR};
titulo(s,'Receita cresceu pelo segundo mês seguido e passou a meta','Receita mensal (R$ mil) e meta. Fonte: planilha Relatório Mensal Pronto.');
const mesesRec=['Abr','Mai','Jun','Jul','Ago','Set'];
s.addChart([
 {type:pres.charts.BAR,data:[{name:'Receita',labels:mesesRec,values:[109.8,118.3,121.9,115.7,124.6,131.2]}],options:{barDir:'col',chartColors:[UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:10,dataLabelColor:TINTA,dataLabelFormatCode:'0.0'}},
 {type:pres.charts.LINE,data:[{name:'Meta (R$ 120 mil)',labels:mesesRec,values:[120,120,120,120,120,120]}],options:{chartColors:[SOL],lineSize:2,lineDash:'dash',lineDataSymbol:'none',showValue:false}}],
 {x:0.5,y:1.6,w:5.6,h:3.4,catAxisLabelColor:CINZA,valAxisLabelColor:CINZA,valGridLine:{color:'E6DFF2',size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:10,valAxisMinVal:0,valAxisMaxVal:150,valAxisMajorUnit:30,showTitle:false});
s.addText([{text:'O que puxou',options:{bold:true,color:UVA,breakLine:true}},{text:'Ticket médio subiu para R$ 9,7 mil (+3%).',options:{bullet:true,breakLine:true}},{text:'Sete novos clientes em agosto renderam em setembro.',options:{bullet:true,breakLine:true}},{text:'Contratos mensais seguraram a base; dois projetos grandes fecharam o mês.',options:{bullet:true}}],
 {x:6.4,y:1.7,w:3.1,h:3.2,fontFace:H,fontSize:12,color:TINTA,isTextBox:true,margin:0,valign:'top',paraSpaceAfter:6});
rodape(s,false); s.addNotes('Destaque positivo com gráfico. Clique no gráfico > Editar dados para trocar os valores; a meta é a série tracejada, troque os 120 pelo seu número.');
// 4 · Destaque positivo 2 (número grande)
s=pres.addSlide(); s.background={color:BR};
titulo(s,'Inadimplência caiu para 2,4%, o menor nível do ano','Meta: 3,0%. Quanto menor, melhor.');
s.addShape(pres.shapes.OVAL,{x:0.7,y:1.8,w:2.9,h:2.9,fill:{color:LAV},line:{color:LAV}});
s.addText('2,4%',{x:0.7,y:2.55,w:2.9,h:1.0,fontFace:H,fontSize:48,bold:true,color:UVA,align:'center',isTextBox:true,margin:0});
s.addText('era 4,1% em janeiro',{x:0.7,y:3.5,w:2.9,h:0.4,fontFace:H,fontSize:11,color:CINZA,align:'center',isTextBox:true,margin:0});
s.addText([{text:'Por quê',options:{bold:true,color:UVA,breakLine:true}},{text:'Cobrança automática no 3º dia de atraso desde maio.',options:{bullet:true,breakLine:true}},{text:'Pix passou a ser a forma padrão nas propostas.',options:{bullet:true,breakLine:true}},{text:'Dois clientes recorrentes migraram para pagamento adiantado.',options:{bullet:true,breakLine:true}},{text:'O que manter',options:{bold:true,color:UVA,breakLine:true}},{text:'Régua de cobrança e Pix como padrão.',options:{bullet:true}}],
 {x:4.1,y:1.8,w:5.4,h:3.1,fontFace:H,fontSize:13,color:TINTA,isTextBox:true,margin:0,valign:'top',paraSpaceAfter:6});
rodape(s,false); s.addNotes('Destaque com número grande. Um número, uma causa, uma ação. Troque a unidade se não for percentual.');
// 5 · Ponto de atenção 1 (colunas)
s=pres.addSlide(); s.background={color:BR};
titulo(s,'Despesas passaram a meta pelo segundo mês: R$ 89,8 mil contra R$ 85 mil','Ponto de atenção. O que aconteceu, a causa e o que fazemos.');
const cols=[['O que aconteceu','Despesas +3% contra agosto e 6% acima da meta de R$ 85 mil. Freelancers, mídia paga e softwares subiram.'],['Causa provável','Freelancers extras na campanha de um cliente grande e um teste novo de anúncios. Parte é pontual; as assinaturas novas ficam.'],['Ação proposta','Congelar assinaturas novas até dezembro; mídia só com meta de conversão; revisar a meta para R$ 88 mil.']];
cols.forEach((c,i)=>{const x=0.5+i*3.1; s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:x,y:1.7,w:2.9,h:3.1,fill:{color:i==2?LAV:BR},line:{color:'DCD2EC',width:1},rectRadius:0.12});
  s.addText(c[0],{x:x+0.25,y:1.9,w:2.5,h:0.4,fontFace:H,fontSize:13,bold:true,color:UVA,isTextBox:true,margin:0});
  s.addText(c[1],{x:x+0.25,y:2.35,w:2.5,h:2.3,fontFace:H,fontSize:12,color:TINTA,isTextBox:true,margin:0,valign:'top'});});
rodape(s,false); s.addNotes('Ponto de atenção em três colunas. Nunca apresente um problema sem a ação proposta na terceira coluna.');
// 6 · Ponto de atenção 2 (linha)
s=pres.addSlide(); s.background={color:BR};
titulo(s,'Conversão de leads caiu para 4,4% e ficou abaixo da meta de 5%','Taxa de conversão (%) por mês. Fonte: planilha Relatório Mensal Pronto.');
s.addChart(pres.charts.LINE,[{name:'Conversão',labels:['Abr','Mai','Jun','Jul','Ago','Set'],values:[3.9,4.6,4.2,3.7,4.9,4.4]},{name:'Meta',labels:['Abr','Mai','Jun','Jul','Ago','Set'],values:[5,5,5,5,5,5]}],
 {x:0.5,y:1.6,w:5.6,h:3.4,chartColors:[UVA,SOL],lineSize:3,lineDataSymbol:'circle',lineDataSymbolSize:7,showValue:false,catAxisLabelColor:CINZA,valAxisLabelColor:CINZA,valGridLine:{color:'E6DFF2',size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:10,valAxisMinVal:3,valAxisMaxVal:6,showTitle:false});
s.addText([{text:'Leitura',options:{bold:true,color:UVA,breakLine:true}},{text:'Mais leads (137) e menos fechamentos: a qualidade caiu com o impulsionamento novo.',options:{bullet:true,breakLine:true}},{text:'Ação',options:{bold:true,color:UVA,breakLine:true}},{text:'Ajustar o público do anúncio e qualificar o lead no primeiro contato. Revisar em 30 dias.',options:{bullet:true}}],
 {x:6.4,y:1.7,w:3.1,h:3.2,fontFace:H,fontSize:12,color:TINTA,isTextBox:true,margin:0,valign:'top',paraSpaceAfter:6});
rodape(s,false); s.addNotes('Ponto de atenção com gráfico de linha e meta. Diga a causa provável como hipótese, não como certeza.');
// 7 · Próximos passos
s=pres.addSlide(); s.background={color:BR};
titulo(s,'Três ações para outubro','Cada uma com responsável e data. Sem responsável, não é ação.');
const acts=[['1','Renegociar os dois freelancers fixos e cancelar softwares sem uso','Ana · até 15/10'],['2','Ajustar público do anúncio e criar triagem de leads','Bruno · até 10/10'],['3','Revisar a meta de despesas e apresentar o novo orçamento','Ana · até 31/10']];
acts.forEach((a,i)=>{const y=1.7+i*1.05; s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.85,fill:{color:LAV},line:{color:LAV},rectRadius:0.1});
  s.addShape(pres.shapes.OVAL,{x:0.7,y:y+0.15,w:0.55,h:0.55,fill:{color:SOL},line:{color:SOL}});
  s.addText(a[0],{x:0.7,y:y+0.15,w:0.55,h:0.55,fontFace:H,fontSize:16,bold:true,color:UVA,align:'center',valign:'middle',isTextBox:true,margin:0});
  s.addText(a[1],{x:1.5,y:y+0.12,w:5.6,h:0.6,fontFace:H,fontSize:14,color:TINTA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(a[2],{x:7.2,y:y+0.12,w:2.1,h:0.6,fontFace:H,fontSize:12,bold:true,color:UVA,isTextBox:true,margin:0,valign:'middle',align:'right'});});
rodape(s,false); s.addNotes('Próximos passos. Três é o limite: mais que isso ninguém lembra.');
// 8 · Pedido
s=pres.addSlide(); s.background={color:UVA};
simbolo(s,0.5,0.5,1.0,true);
s.addText('O que preciso de vocês hoje',{x:0.5,y:1.8,w:9,h:0.7,fontFace:H,fontSize:30,bold:true,color:BR,isTextBox:true,margin:0});
s.addText('Aprovar a revisão da meta de despesas para R$ 88 mil e a verba de R$ 1.500 para o novo teste de anúncios em outubro.',{x:0.5,y:2.6,w:8.6,h:1.0,fontFace:H,fontSize:18,color:BR,isTextBox:true,margin:0});
s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:0.5,y:3.9,w:2.2,h:0.6,fill:{color:SOL},line:{color:SOL},rectRadius:0.3});
s.addText('Aprovado',{x:0.5,y:3.9,w:2.2,h:0.6,fontFace:H,fontSize:14,bold:true,color:UVA,align:'center',valign:'middle',isTextBox:true,margin:0});
s.addShape(pres.shapes.ROUNDED_RECTANGLE,{x:2.9,y:3.9,w:2.6,h:0.6,fill:{color:UVA},line:{color:LILC,width:1.5},rectRadius:0.3});
s.addText('Precisa de ajuste',{x:2.9,y:3.9,w:2.6,h:0.6,fontFace:H,fontSize:14,bold:true,color:BR,align:'center',valign:'middle',isTextBox:true,margin:0});
rodape(s,true); s.addNotes('Pedido ou decisão. Uma frase, um valor, um prazo. Termine a reunião com a resposta registrada.');
pres.writeFile({fileName:'entrega/06-modelo-apresentacao-8-slides.pptx'}).then(f=>console.log('ok',f));
