// Modelo: proposta comercial, 10 slides
const {C,H,novo,rodape,titulo,cards,lista,capa,fecho}=require('./slides_base');
const ROD='Kit IA no Trabalho · modelo v1.0 · set/2026';
const p=novo('Proposta comercial · modelo de 10 slides');
let s=capa(p,'Proposta: site e captação de matrículas','Para Escola Nova Era · preparada por Prisma Comunicação · 15 de setembro de 2026','Válida até 30 de setembro de 2026.',ROD);
s.addNotes('Modelo do Seu Sócio Gestor: troque os textos e mantenha a estrutura. Capa. Título é o que o cliente compra, não o nome do serviço. Validade sempre na capa.');
// 2 entendimento
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O que entendemos do seu momento','Três frases sobre o problema, com as palavras que vocês usaram na reunião.');
lista(s,['A escola cresceu para 320 alunos e o site atual não mostra a proposta pedagógica nem recebe matrícula.','As matrículas chegam por WhatsApp e se perdem: em 2026, 40 famílias interessadas não tiveram resposta em 48 horas.','A meta para 2027 é 380 alunos, com campanha em outubro e novembro.'],0.5,1.7,9,3.2,14);
rodape(p,s,false,ROD); s.addNotes('Entendimento. Se o cliente ler e pensar "é isso mesmo", a proposta já está meio vendida.');
// 3 objetivo
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Objetivo: 60 matrículas novas até dezembro, com resposta em até 24 horas','Como vamos medir: formulário de interesse, painel semanal, matrículas fechadas.');
cards(p,s,[['60','Matrículas novas','meta combinada para outubro a dezembro'],['24 h','Tempo de resposta','automação de e-mail e WhatsApp na hora do interesse'],['1 site','Que explica e converte','proposta pedagógica, tour, formulário e agenda de visita']],1.7,2.4,0);
rodape(p,s,false,ROD); s.addNotes('Objetivo em números. Combine a meta antes de escrever; se não houver número, use uma medida qualitativa clara.');
// 4 entregas
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O que será entregue','Seis entregas verificáveis. O que não está aqui, não está no escopo.');
const ent=[['1','Site institucional com 6 páginas','home, proposta pedagógica, séries, estrutura, matrícula, contato'],['2','Formulário de interesse com automação','e-mail e WhatsApp automáticos em até 5 minutos'],['3','Página de campanha de matrículas','uma por período; 3 variações de anúncio'],['4','Painel semanal de interessados','planilha compartilhada, atualizada toda sexta'],['5','Sessão de fotos e vídeo curto','meio período na escola; 40 fotos e 1 vídeo de 60 s'],['6','Treinamento da secretaria','1 hora, gravada, sobre o fluxo de resposta']];
ent.forEach((e,i)=>{const col=i%2, row=Math.floor(i/2); const x=0.5+col*4.6, y=1.65+row*1.1;
  s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x,y:y,w:4.4,h:0.95,fill:{color:C.LAV},line:{color:C.LAV},rectRadius:0.1});
  s.addShape(p.shapes.OVAL,{x:x+0.15,y:y+0.22,w:0.5,h:0.5,fill:{color:C.SOL},line:{color:C.SOL}});
  s.addText(e[0],{x:x+0.15,y:y+0.22,w:0.5,h:0.5,fontFace:H,fontSize:13,bold:true,color:C.UVA,align:'center',valign:'middle',isTextBox:true,margin:0});
  s.addText(e[1],{x:x+0.8,y:y+0.1,w:3.5,h:0.35,fontFace:H,fontSize:11.5,bold:true,color:C.UVA,isTextBox:true,margin:0});
  s.addText(e[2],{x:x+0.8,y:y+0.45,w:3.5,h:0.45,fontFace:H,fontSize:9.5,color:C.CINZA,isTextBox:true,margin:0,valign:'top'});});
rodape(p,s,false,ROD); s.addNotes('Entregas. Cada uma precisa ser verificável: o cliente sabe quando foi entregue.');
// 5 não incluído
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'O que não está incluído','Para não ter surpresa. Pode ser contratado à parte.');
lista(s,['Verba de anúncios (paga diretamente pela escola às plataformas; sugerimos R$ 3 mil/mês).','Hospedagem e domínio após o primeiro ano (R$ 40/mês, contratados em nome da escola).','Produção de conteúdo contínuo para redes sociais (proposta separada, mensal).','Sistema de gestão escolar ou integração com o sistema atual.'],0.5,1.7,9,3.2,14);
rodape(p,s,false,ROD); s.addNotes('Não incluído. É o slide que evita retrabalho e desgaste. Nunca pule.');
// 6 método
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Como trabalhamos','Quatro etapas, cada uma com uma aprovação sua.');
const et=[['Descobrir','semana 1','entrevistas, referências, mapa do site'],['Desenhar','semanas 2 e 3','layout das páginas e roteiro do vídeo'],['Produzir','semanas 4 a 6','site, fotos, vídeo, automações'],['Lançar','semana 7','publicação, treinamento, campanha']];
et.forEach((e,i)=>{const x=0.5+i*2.3; s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:x,y:1.8,w:2.1,h:2.6,fill:{color:i==3?C.SOL:C.LAV},line:{color:i==3?C.SOL:C.LAV},rectRadius:0.12});
  s.addText(String(i+1),{x:x+0.2,y:1.95,w:0.6,h:0.5,fontFace:H,fontSize:22,bold:true,color:C.LILAS,isTextBox:true,margin:0});
  s.addText(e[0],{x:x+0.2,y:2.5,w:1.8,h:0.4,fontFace:H,fontSize:15,bold:true,color:C.UVA,isTextBox:true,margin:0});
  s.addText(e[1],{x:x+0.2,y:2.9,w:1.8,h:0.3,fontFace:H,fontSize:10,color:C.CINZA,isTextBox:true,margin:0});
  s.addText(e[2],{x:x+0.2,y:3.25,w:1.8,h:1.0,fontFace:H,fontSize:10.5,color:C.TINTA,isTextBox:true,margin:0,valign:'top'});});
rodape(p,s,false,ROD); s.addNotes('Método em quatro etapas com semanas. Aprovação do cliente ao fim de cada uma.');
// 7 cronograma
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Cronograma: 7 semanas a partir da aprovação','Começando em 22/09, o site vai ao ar em 6/11, antes da campanha de novembro.');
const semanas=['S1','S2','S3','S4','S5','S6','S7']; const gx=2.6, gw=6.9/7;
semanas.forEach((w,i)=>s.addText(w,{x:gx+i*gw,y:1.7,w:gw,h:0.3,fontFace:H,fontSize:10,color:C.CINZA,align:'center',isTextBox:true,margin:0}));
const g=[['Descobrir',0,1],['Desenhar',1,2],['Produzir',3,3],['Lançar',6,1],['Aprovações suas',0,7]];
g.forEach((r,i)=>{const y=2.1+i*0.55; s.addText(r[0],{x:0.5,y:y,w:2.0,h:0.4,fontFace:H,fontSize:11,bold:true,color:C.UVA,isTextBox:true,margin:0,valign:'middle'});
  if(i<4) s.addShape(p.shapes.ROUNDED_RECTANGLE,{x:gx+r[1]*gw+0.05,y:y+0.05,w:r[2]*gw-0.1,h:0.3,fill:{color:i==3?C.SOL:C.LILAS},line:{color:i==3?C.SOL:C.LILAS},rectRadius:0.08});
  else [0,2,5,6].forEach(k=>s.addShape(p.shapes.OVAL,{x:gx+k*gw+gw/2-0.12,y:y+0.08,w:0.24,h:0.24,fill:{color:C.SOL},line:{color:C.UVA,width:1.5}}));});
s.addText('Bolinhas amarelas: reuniões de aprovação (30 minutos cada).',{x:0.5,y:4.9,w:9,h:0.3,fontFace:H,fontSize:10,color:C.CINZA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Cronograma em barras por semana. Copie da planilha Projetos e Prazos.');
// 8 investimento
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Investimento: R$ 31.000, em três parcelas','Valor fechado para as seis entregas. Sem custo extra dentro do escopo.');
cards(p,s,[['R$ 31.000','Valor total','à vista com 5% de desconto: R$ 29.450'],['3×','R$ 10.334','na aprovação, na entrega do layout e na publicação'],['7 dias','Para desistir','após a aprovação, antes de começar a produção']],1.7,2.4,0);
s.addText('Inclui hospedagem e domínio no primeiro ano, duas rodadas de revisão por etapa e 30 dias de ajustes após a publicação.',{x:0.5,y:4.35,w:9,h:0.6,fontFace:H,fontSize:12,color:C.TINTA,isTextBox:true,margin:0});
rodape(p,s,false,ROD); s.addNotes('Investimento. Valor total sempre visível, parcelas claras, o que está incluído no preço.');
// 9 por que nós
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Por que a Prisma','Três fatos verificáveis. Sem adjetivos.');
lista(s,['4 sites para escolas e cursos nos últimos 2 anos (Nova Era pode falar com a Escola do Vale e o Curso Ápice).','Time de 4 pessoas: estratégia, design, texto e tecnologia, sem terceirizar o essencial.','Painel semanal e prazo por etapa: você sabe onde o projeto está sem precisar perguntar.'],0.5,1.7,9,3.2,14);
rodape(p,s,false,ROD); s.addNotes('Prova. Só o que dá para verificar: clientes que podem ser contatados, equipe, processo.');
// 10 próximo passo
s=fecho(p,'Próximo passo',['Aprovação até 30/09 por e-mail ou assinatura da proposta.','Reunião de descoberta na semana de 22/09 (2 horas, na escola).','Site no ar em 6/11; campanha de matrículas a partir de 10/11.'],ROD);
s.addText('Ana Silva · ana@prisma.exemplo · (11) 9 0000-0000 (dados fictícios)',{x:0.5,y:4.5,w:9,h:0.4,fontFace:H,fontSize:12,color:C.LILC,isTextBox:true,margin:0});
s.addNotes('Fechamento: próximo passo com data e contato. Não termine com "obrigado".');
p.writeFile({fileName:'entrega/17-modelo-proposta-comercial-10-slides.pptx'}).then(f=>console.log('ok',f));
