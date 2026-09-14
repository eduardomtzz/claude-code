// Modelo 28: proposta de parceria para um médico que vai atender na clínica por repasse, 10 slides. Exemplo = a parceria da Dra. Renata Sousa
// (planilhas 01 e 11, em NUMEROS.md), apresentada a um novo parceiro. Texto genérico e editável; sem custo-hora, margem da parceria ou
// qualquer conta interna da clínica (05, 11): o parceiro vê turnos, sala, o que cada lado fornece, o percentual de repasse e um exemplo real.
// Nada clínico e nenhuma peça de divulgação; contatos entre colchetes.
const path=require('path');
const {C,H,NOTA0,novo,slide,titulo,cards,lista,tabela,capa,fecho}=require('./slides_base');
const p=novo('Proposta de parceria · modelo de 10 slides');
// 1 capa
let s=capa(p,'Proposta de parceria','[Nome do médico] · [especialidade] · 14 de setembro de 2026','Preparada pela Clínica Vida Plena (exemplo fictício). Dois turnos por semana na Sala 2, por repasse sobre a produção. Proposta válida por 15 dias, até 29 de setembro de 2026.');
s.addNotes(NOTA0+'Capa. O título diz o que a clínica propõe, em linguagem do médico convidado. Validade sempre na capa. Turnos e sala vêm da Agenda (01, Config); o percentual de repasse, da planilha 11. O custo da hora (05), o custo da estrutura e a margem da parceria (11) ficam na clínica e não aparecem em nenhum slide.');
// 2 a clínica
s=slide(p); titulo(s,'A clínica hoje','Só o que o parceiro precisa saber para decidir: estrutura, equipe, pagadores e horário. Sem números internos.');
cards(p,s,[['2','Salas de atendimento','Sala 1 e Sala 2, com recepção e sala de espera compartilhadas'],['3','Médicos atendendo','dois sócios (clínica médica e cardiologia) e uma parceira (endocrinologia)'],['3 + particular','Pagadores','Saúde Total, MediPlan e Vida Care credenciados; particular à vista e a prazo'],['seg. a sex.','Horário','manhã (8h às 12h) e tarde (13h às 17h); recepção o dia inteiro']],1.7,2.45,1);
s.addText('Equipe: Dra. Carolina Mendes (sócia, clínica médica), Dr. Paulo Andrade (sócio, cardiologia), Dra. Renata Sousa (parceira, endocrinologia, dois turnos por semana) e Bruna Carvalho (recepção). Exames realizados na clínica: ECG, MAPA, Holter e teste ergométrico.',{x:0.5,y:4.35,w:9,h:0.7,fontFace:H,fontSize:11,color:C.TINTA,isTextBox:true,margin:0,valign:'top'});
s.addNotes('A clínica. Cartões com o que existe: salas, equipe, pagadores, horário. Corrija o texto do segundo cartão para a sua equipe. Nada de ocupação, faturamento ou custo aqui.');
// 3 o que propomos
s=slide(p); titulo(s,'O que propomos','Dois turnos fixos por semana, na mesma sala, com agenda aberta a particular e aos convênios que o parceiro aceitar.');
const tur=[['Segunda-feira','tarde · 13h às 17h','Sala 2 · 4 horas'],['Quarta-feira','tarde · 13h às 17h','Sala 2 · 4 horas']];
tur.forEach((t,i)=>{const x=0.5+i*4.6; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x,y:1.7,w:4.4,h:1.5,fill:{color:C.SOL},line:{color:C.SOL},rectRadius:0.12});
  s.addText(t[0],{x:x+0.25,y:1.8,w:3.9,h:0.5,fontFace:H,fontSize:18,bold:true,color:C.UVA,isTextBox:true,margin:0});
  s.addText(t[1],{x:x+0.25,y:2.3,w:3.9,h:0.4,fontFace:H,fontSize:13,color:C.UVA,isTextBox:true,margin:0});
  s.addText(t[2],{x:x+0.25,y:2.7,w:3.9,h:0.4,fontFace:H,fontSize:12,color:C.CINZA,isTextBox:true,margin:0});});
lista(s,['Dois turnos de 4 horas: 8 horas de agenda por semana, cerca de 32 horas por mês (feriados descontados); consultas de [30] minutos e retornos de [20], ou a duração que a especialidade pedir.','Agenda aberta a particular e aos convênios credenciados que o parceiro aceitar atender; a tabela particular da especialidade é combinada entre o parceiro e a clínica antes do primeiro turno.','Início previsto: [19/10/2026]. Revisão da parceria a cada seis meses (turnos, tabela, percentual).'],0.5,3.4,9,1.6,12);
s.addNotes('Proposta. Turnos, sala e horas: são as linhas de Config da Agenda (01). Deixe claro que o parceiro escolhe quais convênios atende. A tabela particular é combinada, não imposta; a divulgação de preços segue as regras do CFM.');
// 4 o que a clínica fornece
s=slide(p); titulo(s,'O que a clínica fornece','Tudo o que está fora da consulta. O parceiro chega, atende e vai embora sem pensar em agenda, guia ou cobrança.');
[[0.5,'Estrutura',['Sala equipada e higienizada, com material básico de consulta.','Recepção e sala de espera; sistema de agenda; energia, internet e telefone.','Equipamentos da clínica (ECG, MAPA, Holter) para exames indicados pelo parceiro, com agendamento pela recepção.']],
 [5.1,'Administração',['Agendamento, confirmação de véspera por mensagem e remarcação de faltas.','Cobrança do particular (à vista e a prazo), nota fiscal e conciliação de cartão.','Guias de convênio, envio dos lotes, acompanhamento do pagamento e recurso administrativo de glosa.']]
].forEach(b=>{ s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:b[0],y:1.6,w:4.4,h:3.4,fill:{color:C.LAV},line:{color:C.LAV},rectRadius:0.12});
  s.addText(b[1],{x:b[0]+0.25,y:1.75,w:3.9,h:0.35,fontFace:H,fontSize:14,bold:true,color:C.UVA,isTextBox:true,margin:0});
  lista(s,b[2],b[0]+0.25,2.2,3.9,2.7,11); });
s.addNotes('O que a clínica fornece. É o slide que justifica o percentual. Liste o que costuma ficar invisível: confirmação, cobrança, nota, guia, glosa. O recurso de glosa por motivo clínico é do médico (o prontuário é dele); o administrativo, da clínica.');
// 5 o que o parceiro fornece
s=slide(p); titulo(s,'O que o parceiro fornece','Responsabilidade profissional e presença nos turnos. O prontuário e a conduta são do médico; a clínica não interfere.');
lista(s,['Inscrição ativa no CRM e registro de especialidade [RQE], com cópia para o cadastro da clínica.','Presença nos dois turnos combinados; ausência avisada com [15] dias, para a recepção remarcar os pacientes.','Atendimento e prontuário sob a sua responsabilidade, no sistema da clínica ou no seu, conforme combinado, com sigilo e guarda pelas regras do CFM e da LGPD.','Instrumentos e materiais específicos da especialidade que a clínica não tenha: [liste].','Pessoa jurídica própria e nota fiscal para a clínica a cada repasse, no formato que o contador da clínica e o seu definirem (a formalização da parceria, contrato incluído, é combinada com o contador e com quem cuida do jurídico dos dois lados).','Qualquer material de divulgação com o nome da clínica ou do parceiro é aprovado pelos dois e segue a Resolução CFM 2.336/2023.'],0.5,1.7,9,3.3,12);
s.addNotes('O que o parceiro fornece. Seis itens administrativos; nenhum clínico. A frase sobre a formalização (PJ, nota, contrato) é para não prometer um formato que o contador ainda não confirmou: o kit não traz modelo de contrato.');
// 6 repasse
s=slide(p); titulo(s,'Repasse: como se calcula e quando é pago','Percentual sobre a produção do mês (valor de tabela dos atendimentos realizados), pago no dia 10 do mês seguinte, com demonstrativo.');
tabela(s,['Atendimento','Valor de tabela','Parceiro (50 %)','Clínica (50 %)'],
 [['Consulta particular','R$ 380','R$ 190','R$ 190'],['Retorno particular','R$ 0','R$ 0','R$ 0'],['Consulta pelo convênio Saúde Total','R$ 120','R$ 60','R$ 60'],['Avaliação endócrina particular (exemplo da especialidade)','R$ 400','R$ 200','R$ 200']],0.5,1.6,[3.9,1.7,1.7,1.7],10.5,[0.38,0.36,0.36,0.36,0.36],['l','r','r','r']);
lista(s,['#Regras','A base é a produção realizada no mês, registrada na agenda da clínica; o demonstrativo acompanha o pagamento. Faltas e cancelamentos não geram repasse; retorno sem cobrança também não.','Glosa de convênio é por conta da clínica: o parceiro recebe pelo valor de tabela. Alternativa, se preferirem: [ ] % sobre o valor efetivamente recebido, com o prazo do convênio.','Pagamento no dia 10 do mês seguinte, por transferência, contra a nota fiscal do parceiro.'],0.5,3.55,9,1.5,10.5);
s.addNotes('Repasse. Tabela nativa: clique e edite. Mostre a conta com dois ou três atendimentos, não com a produção total da clínica. O percentual e a base (produção ou recebido) são os da Config da planilha 11. O que fica com a clínica paga sala, recepção, cobrança e glosa: não coloque aqui o custo da estrutura por hora nem a margem da parceria.');
// 7 simulação (por padrão; o caso real só com autorização por escrito do parceiro)
s=slide(p); titulo(s,'Como funciona na prática: oito meses simulados','Simulação com os números do exemplo do kit: um parceiro com dois turnos por semana, ao longo de oito meses. Não é o histórico de nenhum profissional identificado.');
s.addChart(p.charts.BAR,[{name:'Produção mensal (R$)',labels:['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago'],values:[7450,6510,12100,8770,10490,9440,9690,10380]}],
 {x:0.5,y:1.6,w:5.2,h:3.3,barDir:'col',chartColors:[C.UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:8,dataLabelColor:C.TINTA,dataLabelFormatCode:'#,##0',
  catAxisLabelColor:C.CINZA,catAxisLabelFontSize:9,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valAxisLabelFormatCode:'#,##0',valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:false,valAxisMinVal:0,valAxisMaxVal:14000,showTitle:false});
[['R$ 10.380','Produção de um mês cheio','30 atendimentos em 23,7 horas',1.6,false],['R$ 5.190','Repasse do mesmo mês','pago no dia 10, com demonstrativo',2.85,true]].forEach(k=>{
  s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:5.9,y:k[3],w:3.6,h:1.1,fill:{color:k[4]?C.SOL:C.LAV},line:{color:k[4]?C.SOL:C.LAV},rectRadius:0.12});
  s.addText(k[0],{x:6.1,y:k[3]+0.08,w:3.2,h:0.5,fontFace:H,fontSize:22,bold:true,color:C.UVA,isTextBox:true,margin:0});
  s.addText(k[1],{x:6.1,y:k[3]+0.55,w:3.2,h:0.28,fontFace:H,fontSize:12,bold:true,color:C.UVA,isTextBox:true,margin:0});
  s.addText(k[2],{x:6.1,y:k[3]+0.8,w:3.2,h:0.28,fontFace:H,fontSize:9.5,color:C.CINZA,isTextBox:true,margin:0});});
s.addText('Nos oito meses simulados: R$ 74.830 de produção e R$ 37.415 de repasse, sempre no dia 10, com a agenda em torno de 88 % de ocupação. [Para usar o caso de um parceiro real: só com autorização por escrito dele.]',{x:5.9,y:4.0,w:3.6,h:1.1,fontFace:H,fontSize:9.5,color:C.TINTA,isTextBox:true,margin:0,valign:'top'});
s.addNotes('Simulação. Por padrão este slide é simulação, com os números do exemplo do kit e sem nome de profissional: é o que se manda para um médico de fora. Para trocar pelo caso de um parceiro atual, com nome, é preciso autorização por escrito dele: produção, horas e repasse são dado de equipe identificado e não saem da clínica sem isso (bônus 23, seção 6). Mesmo com autorização, só produção, horas e repasse (planilhas 01 e 11): nenhum paciente, nenhum dado clínico, nenhum número interno da clínica. Gráfico nativo: clique > Editar dados.');
// 8 regras administrativas
s=slide(p); titulo(s,'Regras administrativas combinadas','Para não haver atrito depois. Tudo isto vai para o acordo escrito, no formato que o contador e o jurídico definirem.');
tabela(s,['Tema','Como fica'],
 [['Agenda','A recepção marca e confirma; o parceiro define a duração de cada procedimento e pode bloquear horários com [7] dias de aviso.'],
  ['Faltas e cancelamentos','Confirmação de véspera pela recepção; política de faltas da clínica vale para todos os profissionais.'],
  ['Convênios','O parceiro escolhe quais atende; guias preenchidas no dia; lote enviado pela clínica no dia 5; glosa administrativa recorrida pela clínica, glosa clínica pelo médico.'],
  ['Prontuário e sigilo','Do médico. Nenhum dado de paciente sai da clínica nem entra em ferramenta de IA pública; regras do guia LGPD da clínica.'],
  ['Divulgação','Qualquer material com o nome da clínica ou do parceiro é aprovado pelos dois e segue as regras do CFM e do CRM.'],
  ['Revisão','A cada seis meses: turnos, tabela, percentual, ocupação. Qualquer um dos lados encerra com [30] dias de aviso, cumprindo a agenda já marcada.']],0.5,1.6,[2.0,7.0],10,[0.36,0.5,0.42,0.6,0.5,0.5,0.55],['l','l']);
s.addNotes('Regras. Seis temas administrativos, uma linha cada. Não são cláusulas: são os combinados que o contador e o jurídico vão transformar em acordo. Nada clínico entra aqui.');
// 9 próximos passos
s=slide(p); titulo(s,'Próximos passos','Quatro passos até o primeiro turno.');
const pp=[['Resposta à proposta','por e-mail ou mensagem, com os turnos e convênios que aceita','até 29/09/2026'],['Formalização com o contador','contrato de parceria, nota fiscal e formato do repasse definidos pelos dois lados','até 06/10/2026'],['Cadastro e visita','tabela da especialidade na agenda, cadastro no sistema, conhecer a recepção e a sala','semana de 12/10/2026'],['Primeiro turno','agenda aberta com duas semanas de antecedência; primeiro repasse em 10/11','19/10/2026']];
pp.forEach((e,i)=>{const y=1.65+i*0.82; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.7,fill:{color:i==0?C.SOL:C.LAV},line:{color:i==0?C.SOL:C.LAV},rectRadius:0.1});
  s.addShape(p.shapes.OVAL,{x:0.65,y:y+0.1,w:0.5,h:0.5,fill:{color:C.UVA},line:{color:C.UVA}});
  s.addText(String(i+1),{x:0.65,y:y+0.1,w:0.5,h:0.5,fontFace:H,fontSize:13,bold:true,color:C.BR,align:'center',valign:'middle',isTextBox:true,margin:0});
  s.addText(e[0],{x:1.35,y:y+0.08,w:2.6,h:0.55,fontFace:H,fontSize:12,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[1],{x:4.0,y:y+0.08,w:3.9,h:0.55,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[2],{x:8.0,y:y+0.08,w:1.35,h:0.55,fontFace:H,fontSize:10.5,bold:true,color:C.CINZA,isTextBox:true,margin:0,valign:'middle',align:'right'});});
s.addNotes('Próximos passos com data. O primeiro é a decisão do parceiro (validade da proposta, 15 dias); o segundo é a formalização, que depende do contador; os outros mostram que a clínica já tem o caminho pronto.');
// 10 contato
s=fecho(p,'Contato',['Dra. Carolina Mendes · sócia · [e-mail] · [telefone]','Dr. Paulo Andrade · sócio · [e-mail] · [telefone]','Clínica Vida Plena · [endereço] · seg. a sex., 8h às 17h · recepção: [telefone]']);
s.addText('Troque os colchetes pelos dados reais antes de enviar. Esta apresentação é uma proposta comercial entre profissionais; as condições finais ficam no acordo escrito. Não é material de divulgação ao público.',{x:0.5,y:4.5,w:9,h:0.6,fontFace:H,fontSize:11,color:C.LILC,isTextBox:true,margin:0,valign:'top'});
s.addNotes('Fechamento: contato de quem responde, com horário. Preencha [e-mail], [telefone] e [endereço]: os colchetes existem para ninguém enviar contato de exemplo. Não termine com "obrigado": termine com como falar com você.');
p.writeFile({fileName:path.join(__dirname,'28-modelo-proposta-de-parceria-10-slides.pptx')}).then(f=>console.log('ok',f));
