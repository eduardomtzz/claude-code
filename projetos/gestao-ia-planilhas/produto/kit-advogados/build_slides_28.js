// Modelo 28: proposta de honorários para um cliente, 10 slides. Texto genérico e editável; sem tese jurídica (só escopo, etapas, equipe, valores).
const path=require('path');
const {C,H,ROD,novo,rodape,titulo,cards,lista,tabela,capa,fecho}=require('./slides_base');
const p=novo('Proposta de honorários · modelo de 10 slides');
const NOTA0='Modelo do Kit de Gestão para Advogados: troque os textos e mantenha a estrutura. ';
// 1 capa
let s=capa(p,'Proposta de honorários','Loja Verde Comércio · demanda contratual com fornecedor · 15 de setembro de 2026','Preparada por Ferraz & Lima Advocacia (exemplo fictício). Válida até 30 de setembro de 2026.',ROD);
s.addNotes(NOTA0+'Capa. O título diz o que o cliente contrata, em linguagem dele, não o nome da área. Validade sempre na capa. Os valores vêm do Simulador de honorário (06) e da Proposta de honorários (07); a equipe e as horas, do Custo-hora (05).');
// 2 entendimento
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O que entendemos do seu caso','Só o escopo, com as palavras usadas na reunião. Sem opinião sobre o mérito nesta proposta.');
lista(s,['A Loja Verde tem uma divergência com um fornecedor sobre entregas e valores de um contrato de 2025; os documentos já estão reunidos pela empresa.',
 'A empresa quer tentar primeiro um acordo e, se não houver, seguir com a demanda.',
 'O que importa para vocês: previsibilidade de custo, um retorno mensal sobre o andamento e alguém que fale com o fornecedor no lugar da empresa.',
 'Fora deste escopo: outros contratos e a rotina societária da empresa (proposta à parte, se quiserem).'],0.5,1.7,9,3.2,13.5);
rodape(p,s,false,ROD); s.addNotes('Entendimento. Se o cliente ler e pensar "é isso mesmo", a proposta já está meio aceita. Escopo, não tese: a análise do caso fica para o trabalho contratado.');
// 3 etapas e prazos
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Etapas e prazos estimados','Quatro etapas. Os prazos dependem da outra parte e do andamento: são estimativas, revistas no relatório mensal.');
const et=[['Organizar','semanas 1 e 2','leitura dos documentos, reunião de alinhamento e plano de trabalho'],['Negociar','semanas 3 a 8','contato com o fornecedor, propostas de acordo e reuniões'],['Demanda','a partir do 3º mês, se não houver acordo','preparação, protocolo e acompanhamento de cada etapa'],['Acompanhar','12 a 18 meses (estimativa)','audiências, reuniões e relatório mensal até o encerramento']];
et.forEach((e,i)=>{const x=0.5+i*2.3; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x,y:1.75,w:2.1,h:2.75,fill:{color:i==1?C.SOL:C.LAV},line:{color:i==1?C.SOL:C.LAV},rectRadius:0.12});
  s.addText(String(i+1),{x:x+0.2,y:1.9,w:0.6,h:0.5,fontFace:H,fontSize:22,bold:true,color:C.LILAS,isTextBox:true,margin:0});
  s.addText(e[0],{x:x+0.2,y:2.45,w:1.8,h:0.4,fontFace:H,fontSize:14,bold:true,color:C.UVA,isTextBox:true,margin:0,fit:'shrink'});
  s.addText(e[1],{x:x+0.2,y:2.85,w:1.8,h:0.45,fontFace:H,fontSize:9.5,color:C.CINZA,isTextBox:true,margin:0,valign:'top'});
  s.addText(e[2],{x:x+0.2,y:3.3,w:1.8,h:1.1,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'top'});});
s.addText('A etapa destacada é onde a maior parte dos casos como este se resolve. Se houver acordo, o trabalho termina na etapa 2.',{x:0.5,y:4.6,w:9,h:0.4,fontFace:H,fontSize:10.5,color:C.CINZA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Etapas. Descreva o caminho em linguagem de gestão (o que acontece, quando, com que frequência), não em linguagem processual. Prazos sempre com "estimativa".');
// 4 equipe
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Quem cuida do caso','Uma responsável, um sócio de apoio e uma estagiária. Você sempre sabe com quem falar.');
const eq=[['Marina Ferraz','Sócia responsável · cível e empresarial','Conduz o caso, as reuniões com a empresa e a negociação com o fornecedor. Estimativa: 70 horas.'],
 ['Rafael Lima','Sócio de apoio','Revisa o que sai do escritório e substitui a Marina em audiências e reuniões quando preciso. Estimativa: 15 horas.'],
 ['Júlia Prado','Estagiária','Organiza documentos, agenda e o relatório mensal, sob supervisão da Marina. Estimativa: 25 horas.']];
eq.forEach((e,i)=>{const y=1.65+i*0.98; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.85,fill:{color:C.LAV},line:{color:C.LAV},rectRadius:0.1});
  s.addText(e[0],{x:0.7,y:y+0.1,w:2.2,h:0.65,fontFace:H,fontSize:13,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[1],{x:2.95,y:y+0.1,w:2.3,h:0.65,fontFace:H,fontSize:10.5,color:C.CINZA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[2],{x:5.35,y:y+0.1,w:3.95,h:0.65,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'middle'});});
s.addText('110 horas estimadas no total, base do valor da próxima página (planilha Simulador de honorário, 06).',{x:0.5,y:4.65,w:9,h:0.35,fontFace:H,fontSize:10.5,color:C.CINZA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Equipe. Nome, papel e o que cada um faz neste caso. As horas por pessoa vêm do Simulador (06) e servem de base para o valor.');
// 5 modalidade e valores
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Modalidade e valores','Duas opções para as mesmas quatro etapas. Valores de exemplo, para editar.');
tabela(s,['Modalidade','Valor fixo','Parcela de êxito','Horas estimadas','Como paga'],
 [['Opção A · Honorário fixo','R$ 14.400','não há','110 h','30% na assinatura + 4 parcelas mensais'],
  ['!Opção B · Misto (recomendada)','!R$ 9.600','!10% do valor recuperado ou economizado, ao final','!110 h','!30% na assinatura + 4 parcelas; êxito ao final']],0.5,1.6,[2.3,1.2,2.4,1.2,1.9],10,[0.4,0.5,0.62],['l','r','l','r','l']);
lista(s,['#Como chegamos ao valor','Custo-hora do escritório × 110 horas estimadas + margem, conferido com a tabela interna de casos do mesmo tipo (planilha 08).','#Por que recomendamos a opção mista','Entrada menor para a empresa e o escritório participa do resultado. Se nada for recuperado ou economizado, não há parcela de êxito.','#Não incluído no valor','Custas e despesas de terceiros (perícia, certidões, deslocamento), reembolsadas com comprovante.'],0.5,3.25,9,1.75,11);
rodape(p,s,false,ROD); s.addNotes('Valores. Tabela nativa: clique e edite. Mostre no máximo duas opções e diga qual recomenda. O valor sai do Simulador de honorário (06); a coerência com outros casos, da Tabela de referência (08).');
// 6 condições de pagamento
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Condições de pagamento e parcelas','Entrada de 30% na assinatura do contrato e quatro parcelas mensais no dia 10, por Pix ou boleto.');
tabela(s,['Parcela','Vencimento','Opção A · Fixo','Opção B · Misto'],
 [['Entrada (30%)','na assinatura','R$ 4.320','R$ 2.880'],['1ª parcela','10/11/2026','R$ 2.520','R$ 1.680'],['2ª parcela','10/12/2026','R$ 2.520','R$ 1.680'],['3ª parcela','10/01/2027','R$ 2.520','R$ 1.680'],['4ª parcela','10/02/2027','R$ 2.520','R$ 1.680'],['!Total','!—','!R$ 14.400','!R$ 9.600 + êxito']],0.5,1.6,[2.6,2.0,2.2,2.2],10.5,[0.38,0.34,0.34,0.34,0.34,0.34,0.34],['l','l','r','r']);
s.addText('Êxito da opção B: apurado e pago em até 30 dias depois de a empresa receber o valor. Despesas de terceiros: previsão de até R$ 1.500 no primeiro ano, sempre autorizadas antes. Atraso: aviso em 7 dias; condições de reajuste e de rescisão ficam no contrato.',{x:0.5,y:4.42,w:9,h:0.6,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'top'});
rodape(p,s,false,ROD); s.addNotes('Condições. Parcelas com data e valor; a soma tem de bater com o valor total do slide anterior. As datas do exemplo partem da assinatura em outubro de 2026.');
// 7 incluído e não incluído
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O que está incluído e o que não está','Para não haver surpresa. O que não está aqui pode ser contratado à parte.');
[[0.5,C.VERDE,C.VERDE_T,'Incluído',['As quatro etapas do slide 3, até o encerramento do caso.','Negociação com o fornecedor em nome da empresa.','Até duas reuniões por mês com a empresa (presenciais ou por vídeo).','Relatório mensal por e-mail e atendimento em horário comercial.','Organização e guarda dos documentos do caso.']],
 [5.1,C.VERM,C.VERM_T,'Não incluído',['Custas e despesas de terceiros (reembolsadas com comprovante).','Recursos a instâncias superiores: proposta específica, se chegar lá.','Outros contratos ou demandas da empresa.','Viagens fora da cidade (reembolso combinado antes).','Serviços de contabilidade, perícia ou tradução.']]
].forEach(b=>{ s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:b[0],y:1.6,w:4.4,h:3.35,fill:{color:b[1]},line:{color:b[1]},rectRadius:0.12});
  s.addText(b[3],{x:b[0]+0.25,y:1.75,w:3.9,h:0.35,fontFace:H,fontSize:14,bold:true,color:b[2],isTextBox:true,margin:0});
  lista(s,b[4],b[0]+0.25,2.2,3.9,2.65,11); });
rodape(p,s,false,ROD); s.addNotes('Incluído e não incluído. É o slide que evita desgaste depois. Nunca pule. Se o cliente pedir algo da coluna direita, é proposta nova, não favor.');
// 8 comunicação e rotina
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Como vamos nos falar','Rotina combinada desde o início: você sabe quando terá notícia, sem precisar perguntar.');
cards(p,s,[['Mensal','Reunião de 30 min','primeira semana do mês, presencial ou por vídeo, com a Marina'],['E-mail','Relatório mensal','o que aconteceu, o que vem, custos e despesas do mês, em uma página'],['2 dias','Retorno','a e-mail e WhatsApp comercial, em até 2 dias úteis, de segunda a sexta, das 9h às 18h'],['No dia','Fato relevante','aviso de qualquer movimento que mude prazo, custo ou decisão, com o que muda para a empresa']],1.7,2.45,0);
s.addText('Tudo o que for combinado nas reuniões vai por e-mail no mesmo dia, para ficar registrado. Urgências: telefone dos sócios.',{x:0.5,y:4.35,w:9,h:0.5,fontFace:H,fontSize:11,color:C.TINTA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Comunicação. Quatro compromissos simples. Cumpri-los vale mais que qualquer adjetivo sobre o escritório.');
// 9 próximos passos
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Próximos passos','Quatro passos até o início do trabalho.');
const pp=[['Aprovação da proposta','por e-mail ou assinatura, com a escolha da opção A ou B','até 30/09/2026'],['Contrato de honorários e entrada','assinatura e pagamento dos 30%','até 7/10/2026'],['Reunião de abertura (1 hora)','entrega dos documentos e plano de trabalho','semana de 13/10/2026'],['Primeiro relatório mensal','com o resultado da etapa 1 e a agenda da negociação','5/11/2026']];
pp.forEach((e,i)=>{const y=1.65+i*0.82; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.7,fill:{color:i==0?C.SOL:C.LAV},line:{color:i==0?C.SOL:C.LAV},rectRadius:0.1});
  s.addShape(p.shapes.OVAL,{x:0.65,y:y+0.1,w:0.5,h:0.5,fill:{color:C.UVA},line:{color:C.UVA}});
  s.addText(String(i+1),{x:0.65,y:y+0.1,w:0.5,h:0.5,fontFace:H,fontSize:13,bold:true,color:C.BR,align:'center',valign:'middle',isTextBox:true,margin:0});
  s.addText(e[0],{x:1.35,y:y+0.08,w:3.1,h:0.55,fontFace:H,fontSize:12,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[1],{x:4.5,y:y+0.08,w:3.4,h:0.55,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[2],{x:8.0,y:y+0.08,w:1.35,h:0.55,fontFace:H,fontSize:10.5,bold:true,color:C.CINZA,isTextBox:true,margin:0,valign:'middle',align:'right'});});
rodape(p,s,false,ROD); s.addNotes('Próximos passos com data. O primeiro é a decisão do cliente; os outros mostram que o escritório já tem o caminho pronto.');
// 10 contato
s=fecho(p,'Contato',['Marina Ferraz · sócia responsável · marina@ferrazlima.exemplo · (11) 9 0000-0000','Rafael Lima · sócio · rafael@ferrazlima.exemplo · (11) 9 0000-0001','Ferraz & Lima Advocacia · Rua Exemplo, 100 · São Paulo · seg. a sex., 9h às 18h'],ROD);
s.addText('Dados fictícios. Esta apresentação acompanha a proposta; as condições finais ficam no contrato de honorários.',{x:0.5,y:4.5,w:9,h:0.4,fontFace:H,fontSize:11,color:C.LILC,isTextBox:true,margin:0});
s.addNotes('Fechamento: contato de quem responde, com horário. Não termine com "obrigado": termine com como falar com você.');
p.writeFile({fileName:path.join(__dirname,'28-modelo-proposta-de-honorarios-10-slides.pptx')}).then(f=>console.log('ok',f));
