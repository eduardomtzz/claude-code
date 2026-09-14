// Modelo 28: proposta de honorários para um cliente, 10 slides. Exemplo = proposta nº 2026-023 (Roberto Almeida) das planilhas 06/07/15,
// em NUMEROS.md. Texto genérico e editável; sem tese jurídica (só escopo, etapas, equipe, valores). Nada de custo-hora, margem ou
// planilha interna: o cliente vê horas estimadas por etapa e valor por etapa.
const path=require('path');
const {C,H,NOTA0,novo,slide,titulo,cards,lista,tabela,capa,fecho}=require('./slides_base');
const p=novo('Proposta de honorários · modelo de 10 slides');
// 1 capa
let s=capa(p,'Proposta de honorários','[Nome do cliente] · discussão sobre contrato de prestação de serviços · 14 de setembro de 2026','Preparada por Ferraz & Lima Advocacia (exemplo fictício). Proposta nº 2026-023, válida por 15 dias, até 29 de setembro de 2026.');
s.addNotes(NOTA0+'Capa. O título diz o que o cliente contrata, em linguagem dele, não o nome da área. Validade sempre na capa. Os valores e as horas por etapa vêm da Proposta de honorários (07); a conta interna (Simulador 06, custo-hora 05) fica no escritório e não aparece em nenhum slide.');
// 2 entendimento
s=slide(p); titulo(s,'O que entendemos do seu caso','Só o escopo, com as palavras usadas na reunião. Sem opinião sobre o mérito nesta proposta.');
lista(s,['[Nome do cliente] tem uma divergência com [a outra parte] sobre um contrato de prestação de serviços; os documentos já estão reunidos.',
 'O que se quer: [tentar primeiro um acordo e, se não houver, seguir com a discussão até a decisão].',
 'O que importa para você: previsibilidade de custo, retorno periódico sobre o andamento e alguém que fale com a outra parte no seu lugar.',
 'Fora deste escopo: [outros contratos e assuntos] (proposta à parte, se quiser).'],0.5,1.7,9,3.2,13.5);
s.addNotes('Entendimento. Se o cliente ler e pensar "é isso mesmo", a proposta já está meio aceita. Escopo, não tese: a análise do caso fica para o trabalho contratado.');
// 3 etapas e prazos
s=slide(p); titulo(s,'Etapas e prazos estimados','Quatro etapas, as mesmas da proposta em PDF. Os prazos dependem da outra parte e do andamento: são estimativas.');
const et=[['Análise inicial e planejamento','até 15 dias','reunião, leitura dos documentos e definição da estratégia'],['Fase inicial','até 60 dias','redação e protocolo do pedido, acompanhamento das primeiras respostas'],['Acompanhamento até a decisão','durante o caso','manifestações, audiências e reuniões com você'],['Encerramento','ao fim do caso','prestação de contas e organização dos documentos finais']];
et.forEach((e,i)=>{const x=0.5+i*2.3; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x,y:1.75,w:2.1,h:2.75,fill:{color:i==2?C.SOL:C.LAV},line:{color:i==2?C.SOL:C.LAV},rectRadius:0.12});
  s.addText(String(i+1),{x:x+0.2,y:1.9,w:0.6,h:0.5,fontFace:H,fontSize:22,bold:true,color:C.LILAS,isTextBox:true,margin:0});
  s.addText(e[0],{x:x+0.2,y:2.45,w:1.8,h:0.6,fontFace:H,fontSize:13,bold:true,color:C.UVA,isTextBox:true,margin:0,fit:'shrink',valign:'top'});
  s.addText(e[1],{x:x+0.2,y:3.05,w:1.8,h:0.35,fontFace:H,fontSize:9.5,color:C.CINZA,isTextBox:true,margin:0,valign:'top'});
  s.addText(e[2],{x:x+0.2,y:3.4,w:1.8,h:1.05,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'top'});});
s.addText('A etapa destacada é a mais longa. Se houver acordo antes, o trabalho termina ali e a prestação de contas é feita na etapa 4.',{x:0.5,y:4.6,w:9,h:0.4,fontFace:H,fontSize:10.5,color:C.CINZA,isTextBox:true,margin:0});
s.addNotes('Etapas. Descreva o caminho em linguagem de gestão (o que acontece, quando, com que frequência), não em linguagem processual. Prazos sempre com "estimativa". As quatro etapas são as linhas da aba Proposta da planilha 07.');
// 4 equipe
s=slide(p); titulo(s,'Quem cuida do caso','Uma responsável, um sócio de apoio e uma estagiária. Você sempre sabe com quem falar.');
const eq=[['Marina Ferraz','Sócia responsável · cível e empresarial','Conduz o caso, as reuniões com você e a conversa com a outra parte. Estimativa: 30 horas.'],
 ['Rafael Lima','Sócio de apoio','Revisa o que sai do escritório e substitui a Marina em audiências e reuniões quando preciso. Estimativa: 8 horas.'],
 ['Júlia Prado','Estagiária','Organiza documentos, agenda e o relatório de andamento, sob supervisão da Marina. Estimativa: 15 horas.']];
eq.forEach((e,i)=>{const y=1.65+i*0.98; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.85,fill:{color:C.LAV},line:{color:C.LAV},rectRadius:0.1});
  s.addText(e[0],{x:0.7,y:y+0.1,w:2.2,h:0.65,fontFace:H,fontSize:13,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[1],{x:2.95,y:y+0.1,w:2.3,h:0.65,fontFace:H,fontSize:10.5,color:C.CINZA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[2],{x:5.35,y:y+0.1,w:3.95,h:0.65,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'middle'});});
s.addText('53 horas estimadas no total, distribuídas nas quatro etapas da próxima página.',{x:0.5,y:4.65,w:9,h:0.35,fontFace:H,fontSize:10.5,color:C.CINZA,isTextBox:true,margin:0});
s.addNotes('Equipe. Nome, papel e o que cada um faz neste caso. As horas por pessoa somam as horas por etapa da proposta (07); a conta de custo dessas horas é interna (05 e 06) e não entra aqui.');
// 5 modalidade e valores
s=slide(p); titulo(s,'Modalidade e valores','Duas opções para as mesmas quatro etapas. Valores de exemplo, para editar.');
tabela(s,['Modalidade','Valor fixo','Parcela de êxito','Horas estimadas','Como paga'],
 [['Opção A · Honorário fixo','R$ 7.000','não há','53 h','40 % na aceitação + 3 parcelas mensais'],
  ['!Opção B · Misto (recomendada)','!R$ 4.500','!15 % do valor recebido ou economizado, ao final','!53 h','!40 % na aceitação + 3 parcelas; êxito ao final']],0.5,1.6,[2.3,1.2,2.4,1.2,1.9],10,[0.4,0.5,0.62],['l','r','l','r','l']);
lista(s,['#Como chegamos ao valor','Pelas horas estimadas em cada etapa e pelo valor de cada uma: análise inicial 8 h (R$ 900), fase inicial 18 h (R$ 1.800), acompanhamento até a decisão 22 h (R$ 1.200), encerramento 5 h (R$ 600). O êxito da opção B só existe se houver resultado para você.','#Por que recomendamos a opção mista','Entrada menor e o escritório participa do resultado. Se nada for recebido ou economizado, não há parcela de êxito.','#Não incluído no valor','Custas e despesas de terceiros (perícia, certidões, deslocamento), reembolsadas com comprovante.'],0.5,3.25,9,1.8,10.5);
s.addNotes('Valores. Tabela nativa: clique e edite. Mostre no máximo duas opções e diga qual recomenda. O que o cliente vê: horas por etapa e valor por etapa (aba Proposta da 07). O que fica no escritório: custo-hora, margem e a comparação das modalidades (05, 06 e 08). Nunca cole essas contas aqui: é o item do checklist "Antes de enviar a proposta".');
// 6 condições de pagamento
s=slide(p); titulo(s,'Condições de pagamento e parcelas','Entrada de 40 % na aceitação da proposta e três parcelas mensais, por Pix. Datas contadas da proposta (14/09/2026).');
tabela(s,['Parcela','Vencimento','Opção A · Fixo','Opção B · Misto'],
 [['Entrada (40 %)','na aceitação','R$ 2.800','R$ 1.800'],['1ª parcela','14/10/2026','R$ 1.400','R$ 900'],['2ª parcela','13/11/2026','R$ 1.400','R$ 900'],['3ª parcela','13/12/2026','R$ 1.400','R$ 900'],['!Total','!—','!R$ 7.000','!R$ 4.500 + êxito']],0.5,1.6,[2.6,2.0,2.2,2.2],10.5,[0.38,0.36,0.36,0.36,0.36,0.36],['l','l','r','r']);
s.addText('Êxito da opção B: apurado e pago em até 30 dias depois de você receber (ou deixar de pagar) o valor. Despesas de terceiros: previsão de até R$ 1.250 (custas R$ 800, deslocamentos R$ 300, cópias e certidões R$ 150), sempre autorizadas antes. Atraso: aviso em 7 dias; condições de reajuste e de rescisão ficam no contrato.',{x:0.5,y:4.15,w:9,h:0.85,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'top'});
s.addNotes('Condições. Parcelas com data e valor: são as do cronograma de pagamento da planilha 07 (entrada 40 % = R$ 1.800; restante R$ 2.700 em 3 × R$ 900). A soma tem de bater com o valor total do slide anterior.');
// 7 incluído e não incluído
s=slide(p); titulo(s,'O que está incluído e o que não está','Para não haver surpresa. O que não está aqui pode ser contratado à parte.');
[[0.5,C.VERDE,C.VERDE_T,'Incluído',['As quatro etapas do slide 3, até o encerramento do caso.','Conversa com a outra parte em seu nome, na tentativa de acordo.','Até duas reuniões por mês com você (presenciais ou por vídeo).','Relatório de andamento por e-mail a cada 30 dias e atendimento em horário comercial.','Organização e guarda dos documentos do caso.']],
 [5.1,C.VERM,C.VERM_T,'Não incluído',['Custas e despesas de terceiros (reembolsadas com comprovante).','Recursos a instâncias superiores: proposta específica, se chegar lá.','Outros contratos ou assuntos.','Viagens fora da cidade (reembolso combinado antes).','Serviços de contabilidade, perícia ou tradução.']]
].forEach(b=>{ s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:b[0],y:1.6,w:4.4,h:3.35,fill:{color:b[1]},line:{color:b[1]},rectRadius:0.12});
  s.addText(b[3],{x:b[0]+0.25,y:1.75,w:3.9,h:0.35,fontFace:H,fontSize:14,bold:true,color:b[2],isTextBox:true,margin:0});
  lista(s,b[4],b[0]+0.25,2.2,3.9,2.65,11); });
s.addNotes('Incluído e não incluído. É o slide que evita desgaste depois. Nunca pule. Se o cliente pedir algo da coluna direita, é proposta nova, não favor.');
// 8 comunicação e rotina
s=slide(p); titulo(s,'Como vamos nos falar','Rotina combinada desde o início: você sabe quando terá notícia, sem precisar perguntar.');
cards(p,s,[['Mensal','Reunião de 30 min','primeira semana do mês, presencial ou por vídeo, com a Marina'],['E-mail','Relatório de andamento','o que aconteceu, o que vem, custos e despesas do período, em uma página'],['2 dias','Retorno','a e-mail e WhatsApp do escritório, em até 2 dias úteis, de segunda a sexta, das 9h às 18h'],['No dia','Fato relevante','aviso de qualquer movimento que mude prazo, custo ou decisão, com o que muda para você']],1.7,2.45,0);
s.addText('Tudo o que for combinado nas reuniões vai por e-mail no mesmo dia, para ficar registrado. Urgências: telefone dos sócios.',{x:0.5,y:4.35,w:9,h:0.5,fontFace:H,fontSize:11,color:C.TINTA,isTextBox:true,margin:0});
s.addNotes('Comunicação. Quatro compromissos simples. Cumpri-los vale mais que qualquer adjetivo sobre o escritório.');
// 9 próximos passos
s=slide(p); titulo(s,'Próximos passos','Quatro passos até o início do trabalho.');
const pp=[['Aprovação da proposta','por e-mail ou assinatura, com a escolha da opção A ou B','até 29/09/2026'],['Contrato de honorários e entrada','assinatura e pagamento dos 40 % por Pix','até 06/10/2026'],['Reunião de abertura (1 hora)','entrega dos documentos e plano de trabalho','semana de 12/10/2026'],['Primeiro relatório de andamento','com o resultado da etapa 1 e o plano da etapa 2','até 30/10/2026']];
pp.forEach((e,i)=>{const y=1.65+i*0.82; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:0.5,y:y,w:9,h:0.7,fill:{color:i==0?C.SOL:C.LAV},line:{color:i==0?C.SOL:C.LAV},rectRadius:0.1});
  s.addShape(p.shapes.OVAL,{x:0.65,y:y+0.1,w:0.5,h:0.5,fill:{color:C.UVA},line:{color:C.UVA}});
  s.addText(String(i+1),{x:0.65,y:y+0.1,w:0.5,h:0.5,fontFace:H,fontSize:13,bold:true,color:C.BR,align:'center',valign:'middle',isTextBox:true,margin:0});
  s.addText(e[0],{x:1.35,y:y+0.08,w:3.1,h:0.55,fontFace:H,fontSize:12,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[1],{x:4.5,y:y+0.08,w:3.4,h:0.55,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'middle'});
  s.addText(e[2],{x:8.0,y:y+0.08,w:1.35,h:0.55,fontFace:H,fontSize:10.5,bold:true,color:C.CINZA,isTextBox:true,margin:0,valign:'middle',align:'right'});});
s.addNotes('Próximos passos com data. O primeiro é a decisão do cliente (a validade da proposta, 15 dias); os outros mostram que o escritório já tem o caminho pronto.');
// 10 contato
s=fecho(p,'Contato',['Marina Ferraz · sócia responsável · [e-mail] · [telefone]','Rafael Lima · sócio · [e-mail] · [telefone]','Ferraz & Lima Advocacia · [endereço] · seg. a sex., 9h às 18h']);
s.addText('Troque os colchetes pelos dados reais antes de enviar. Esta apresentação acompanha a proposta em PDF; as condições finais ficam no contrato de honorários.',{x:0.5,y:4.5,w:9,h:0.6,fontFace:H,fontSize:11,color:C.LILC,isTextBox:true,margin:0,valign:'top'});
s.addNotes('Fechamento: contato de quem responde, com horário. Preencha [e-mail], [telefone] e [endereço]: os colchetes existem para ninguém enviar contato de exemplo. Não termine com "obrigado": termine com como falar com você.');
p.writeFile({fileName:path.join(__dirname,'28-modelo-proposta-de-honorarios-10-slides.pptx')}).then(f=>console.log('ok',f));
