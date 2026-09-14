// Modelo 27: resultado do mês para os sócios, 8 slides. Agosto de 2026 fechado, apresentado na reunião de sócios de 14/09/2026.
// Números: NUMEROS.md (18 Resultado mensal, 09 Caixa, 01 Agenda, 07 Simulador, 08 Tabela, 13 Convênios, 14 Parcelas, 15 Orçamentos, 12 Reserva, 05 Custo da hora).
// Só totais e nomes da equipe: nenhum nome de paciente, nada clínico.
const path=require('path');
const {C,H,NOTA0,novo,slide,titulo,cards,lista,tabela,capa,fecho}=require('./slides_base');
const p=novo('Resultado do mês para os sócios · modelo de 8 slides');
// 1 capa
let s=capa(p,'Resultado de agosto de 2026','Clínica Vida Plena (exemplo fictício) · reunião dos sócios · segunda-feira, 14 de setembro de 2026',
 'Em uma frase: agosto deu resultado de R$ 9.640 (margem de 19,2 %), abaixo de julho; a ocupação de 70 % e os R$ 4.550 vencidos hoje pedem ação esta semana.');
s.addNotes(NOTA0+'Capa. A frase em itálico é a conclusão do mês em uma linha: escreva por último, depois de montar os outros slides. Os números vêm do Resultado mensal (18, Config = Agosto), do Caixa (09), da Agenda (01), do Simulador (07) e dos Convênios (13); a posição de parcelas e orçamentos é a de hoje (14 e 15). O prompt "Painel 01 · Explicar o mês ao sócio" ajuda a escrever a frase. Nenhum nome de paciente entra nesta apresentação.');
// 2 resumo
s=slide(p); titulo(s,'O mês em três números','Fonte: Resultado mensal (18) e Caixa da clínica (09), agosto fechado; Convênios (13) e Parcelas (14) na posição de sexta, 11/09.');
cards(p,s,[['R$ 50.336','Receita (entrou no mês)','R$ 53.101 em julho (−5,2 %). Particular à vista R$ 33.860, a prazo R$ 5.315, convênios R$ 11.161 (Saúde Total R$ 7.320, MediPlan R$ 2.130, Vida Care R$ 1.711).'],
 ['R$ 9.640','Resultado (margem 19,2 %)','depois de R$ 10.000 de custos fixos, R$ 7.159 de despesas variáveis (materiais, cartão, repasse, manutenção), R$ 18.000 de pró-labore e R$ 5.537 de impostos provisionados (11 %). Julho: R$ 12.598 (23,7 %).'],
 ['R$ 15.758','Convênio a receber','lotes enviados e não pagos, posição de 11/09; R$ 1.727 atrasados (lote de junho do Vida Care). Particulares: R$ 4.550 vencidos em 16 parcelas (inadimplência a prazo 10,4 %).']],1.65,2.5,1);
s.addText('Agenda de agosto: 168 horas disponíveis, 118,3 atendidas (70,4 %), 23 faltas (8,4 %), produção R$ 48.631.',{x:0.5,y:4.4,w:9,h:0.4,fontFace:H,fontSize:13,color:C.TINTA,isTextBox:true,margin:0});
s.addNotes('Resumo. Três números: o que entrou, o que sobrou e o que ainda vai entrar. O card destacado é o resultado. Diga o número ruim junto com o bom. O resultado da DRE (18) não é o que sobrou no caixa (09: R$ 8.716): a DRE provisiona 11 % de impostos em vez da guia paga (R$ 5.841) e deixa fora a despesa pessoal a acertar (R$ 620, na 11).');
// 3 agenda
s=slide(p); titulo(s,'Agenda de agosto: ocupação, faltas e o que produziu','Agenda e ocupação (01) e Faltas e retornos (02), Config = Agosto. Produção = valor de tabela dos atendimentos realizados, antes de glosa e impostos.');
cards(p,s,[['70,4 %','Ocupação','118,3 h de 168; julho 71,7 %'],['8,4 %','Taxa de falta','23 faltas; julho 8,8 %; meta 6 %'],['R$ 48.631','Produção do mês','R$ 410,97 por hora atendida']],1.55,1.55,0);
tabela(s,['Procedimento','Realizados','Produção','Valor médio','Contra o preço mínimo'],
 [['Consulta',130,'R$ 30.730','R$ 236,38','+7 %'],['Avaliação endócrina',30,'R$ 10.380','R$ 346,00','+24 %'],['Holter',10,'R$ 2.490','R$ 249,00','+74 %'],['Teste ergométrico',8,'R$ 2.270','R$ 283,75','+6 %'],['ECG',18,'R$ 1.416','R$ 78,67','−38 %'],['MAPA',8,'R$ 1.345','R$ 168,12','+21 %']],0.5,3.2,[2.6,1.2,1.4,1.4,2.0],9,0.24);
s.addNotes('Agenda. Hoje, 14/09: setembro está em 81 % de ocupação, com a Sala 2 em 66 % (8,2 horas vazias) e 4 das 6 faltas do mês na agenda do Dr. Paulo; a taxa de falta caiu de 10,9 % (fim de julho) para 5,3 % depois da confirmação de véspera; os 48 retornos de agosto não têm cobrança. Os cartões vêm do Painel da 01 com Config = Agosto; a tabela, da Tabela de preços (08) com o volume de agosto. O ECG é o único procedimento com valor médio abaixo do mínimo: 13 dos 18 foram por convênio. Não discuta paciente nem atendimento aqui: só horas, faltas e valores.');
// 4 preço e mix
s=slide(p); titulo(s,'Consulta: o que cada pagador deixou em agosto','Simulador convênio × particular (07), quadro 4: as 130 consultas realizadas em agosto, líquido após glosa, custo do dinheiro e impostos, contra o custo cheio de R$ 130,67.');
s.addChart(p.charts.BAR,[{name:'Resultado das consultas de agosto (R$)',labels:['Particular','Saúde Total','MediPlan','Vida Care'],values:[12867,-720,-1474,-793]}],
 {x:0.5,y:1.6,w:4.4,h:3.3,barDir:'col',chartColors:[C.UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:9,dataLabelColor:C.TINTA,dataLabelFormatCode:'#,##0',
  catAxisLabelColor:C.CINZA,catAxisLabelFontSize:9,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valAxisLabelFormatCode:'#,##0',valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:false,valAxisMinVal:-3000,valAxisMaxVal:15000,showTitle:false});
tabela(s,['Pagador','Consultas','Líquido','Custo cheio','Resultado'],
 [['Particular',62,'R$ 20.968','R$ 8.101','R$ 12.867'],['Saúde Total',25,'R$ 2.546','R$ 3.267','−R$ 720'],['MediPlan',30,'R$ 2.446','R$ 3.920','−R$ 1.474'],['Vida Care',13,'R$ 906','R$ 1.699','−R$ 793'],['!Total','!130','!R$ 26.867','!R$ 16.987','!R$ 9.880']],5.1,1.65,[1.3,0.8,0.95,0.95,0.9],9.5,[0.4,0.34,0.34,0.34,0.34,0.34]);
lista(s,['#Leitura','Custo da hora de atendimento R$ 200 (R$ 28.000 ÷ 140 h) e hora mínima R$ 340 (planilha 05). A consulta particular deixa R$ 534 por hora; nenhum convênio cobre o custo cheio.','Com agenda vazia, o convênio ainda contribui (Saúde Total: R$ 97,85 por consulta). Com agenda cheia, toma o lugar de um particular. A decisão é por sala e turno, não geral.'],5.1,3.85,4.4,1.3,9.5);
s.addNotes('Preço e mix. Gráfico de colunas nativo: clique > Editar dados. Os números vêm do quadro 4 do Simulador (07). Não é argumento para descredenciar: é argumento para renegociar tabela e prazo (prompt Preço 06) e para olhar onde há hora vazia (planilha 01). Nada de divulgar preço sem revisar pelas regras do CFM.');
// 5 caixa
s=slide(p); titulo(s,'Caixa: entrou × saiu nos últimos três meses','Caixa da clínica (09), aba Painel. Saiu inclui custos fixos, pró-labore, repasse à médica parceira, guia de impostos, materiais e taxas de cartão.');
s.addChart(p.charts.BAR,[{name:'Entrou',labels:['Junho','Julho','Agosto'],values:[43855,53101,50336]},{name:'Saiu',labels:['Junho','Julho','Agosto'],values:[41534,43427,41620]}],
 {x:0.5,y:1.6,w:5.4,h:3.35,barDir:'col',chartColors:[C.UVA,C.LILC],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:9,dataLabelColor:C.TINTA,dataLabelFormatCode:'#,##0',
  catAxisLabelColor:C.CINZA,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valAxisLabelFormatCode:'#,##0',valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:true,legendPos:'b',legendFontSize:10,valAxisMinVal:0,valAxisMaxVal:60000,showTitle:false});
lista(s,['#Agosto','Entrou R$ 50.336, saiu R$ 41.620, sobrou R$ 8.716 (julho: R$ 9.674; junho: R$ 2.321).','#Saídas de agosto','Pró-labore R$ 18.000 · custos fixos R$ 10.000 · guia de impostos R$ 5.841 (11 % das entradas de julho) · repasse à Dra. Renata R$ 4.845 · materiais R$ 1.380 · taxas de cartão R$ 484 · manutenção R$ 450 · despesa pessoal a acertar R$ 620.','#No ano','Sobrou R$ 18.311 de janeiro a agosto; saldo em caixa R$ 52.251 hoje, com R$ 25.997 a pagar até o fim de setembro. Provisão guardada: R$ 17.602 ao fim de agosto. Reserva: R$ 14.000 de R$ 84.000 (meio mês de custo fixo).'],6.2,1.65,3.4,3.4,9.5);
s.addNotes('Caixa. Gráfico de colunas nativo: Entrou e Saiu por mês; a diferença é o que sobrou. Os três meses vêm do Painel mensal do Caixa (09) ou da aba Histórico do Painel da clínica (17). Se o mês fechou negativo, diga primeiro e explique por quê. Julho teve a distribuição do 2º trimestre (R$ 3.591); agosto, a manutenção.');
// 6 recebíveis
s=slide(p); titulo(s,'Convênios, parcelas e orçamentos','Convênios a receber (13), Parcelas e inadimplência (14) e Orçamentos (15), posição de sexta, 11/09. Só totais.');
cards(p,s,[['R$ 15.758','Convênio a receber','R$ 1.727 atrasados (Vida Care, lote de junho, 10 dias); R$ 240 em recurso'],['5,6 %','Glosa dos lotes pagos em agosto','5,5 % no ano: Saúde Total 3,3 %, MediPlan 7,5 %, Vida Care 11,3 % (meta 4 %)'],['R$ 4.550','Vencido a prazo (10,4 %)','16 parcelas; fim de agosto R$ 4.040 (9,8 %); julho R$ 3.380 (9,6 %); meta 8 %']],1.6,1.85,2);
lista(s,['#Cobrar primeiro (14)','Onze parcelas há 30 dias ou mais somam R$ 3.190: mensagem já não resolve; é o degrau 4 da régua (conversa do médico ou da administração e plano por escrito). As outras cinco (R$ 1.360) estão nos degraus 1 a 3, com a recepção.','#Régua da planilha 14','1 dia: lembrete gentil por WhatsApp · 7 dias: mensagem da recepção com nova data · 15 dias: ligação da recepção com o demonstrativo · 30 dias: conversa e plano por escrito. Sem ameaça, sem constrangimento; os modelos do bônus 22 seguem a régua.','#Orçamentos (15)','Aprovado no trimestre R$ 8.510 (47 % da meta de R$ 18.000); 6 em aberto somando R$ 3.460; taxa de aprovação 72 %; "vai pensar / sem retorno" é o maior motivo de perda.'],0.5,3.65,9,1.5,9.5);
s.addNotes('Recebíveis. Separe sempre convênio (lote enviado, prazo, glosa) de particular a prazo (parcela, régua). Inadimplência = vencido ÷ (pago + vencido), a mesma conta em todo o kit; glosa = glosa ÷ (pago + glosa) dos lotes pagos. A lista "Cobrar primeiro" da planilha 14 ordena por valor × dias de atraso; os nomes ficam na planilha, não no slide.');
// 7 decisões
s=fecho(p,'Três decisões para hoje',['Separar R$ 3.000 por mês para a reserva da clínica, a partir de setembro, até chegar a três meses de custo fixo (R$ 84.000; hoje R$ 14.000, meta em setembro de 2028 pela planilha 12). Ou R$ 5.000, pela sobra média dos últimos três meses?',
 'Vida Care: 11,3 % de glosa, 61 dias de prazo real e R$ 110 por hora na consulta. Pedir a conversa de tabela e prazo (prompt Preço 06) antes da renovação, ou reduzir os horários de terça à tarde? Decidir o pedido hoje.',
 'Sala 2 com 8,2 horas vazias em setembro (66 % de ocupação). Abrir as tardes de segunda e quarta para um segundo médico parceiro por repasse (modelo 28), ou um turno a mais do Dr. Paulo? Decidir se a conversa começa.'],13);
s.addText('Registre a resposta (sim, não, adiado) na ata da reunião antes de passar ao próximo slide.',{x:0.5,y:4.7,w:9,h:0.4,fontFace:H,fontSize:12,color:C.LILC,isTextBox:true,margin:0});
s.addNotes('Decisões. Só o que precisa de sim ou não dos sócios, com valor e prazo. No máximo três: mais que isso vira discussão sem fim. Descredenciamento e contrato de parceria têm regra própria: a decisão aqui é começar a conversa, não redigir nada.');
// 8 próximos passos
s=slide(p); titulo(s,'Próximos passos','Cada linha tem um responsável e uma data. Sem dono, não entra na lista.');
tabela(s,['O que','Quem','Prazo'],
 [['Recorrer das duas guias glosadas de julho (Saúde Total, R$ 170) com o texto administrativo do Recebíveis 03','Bruna Carvalho','18/09/2026'],
  ['Cobrar por escrito o lote de junho do Vida Care (R$ 1.727, 10 dias de atraso; Recebíveis 08)','Bruna Carvalho','16/09/2026'],
  ['Enviar a mensagem da régua para as 16 parcelas vencidas (modelos 09 a 12 do bônus 22) e registrar na planilha 14','Bruna Carvalho','16/09/2026'],
  ['Conversar com os 11 pacientes com parcela há mais de 30 dias e registrar o plano por escrito','Dra. Carolina Mendes','25/09/2026'],
  ['Transferir R$ 3.000 para a reserva e registrar na planilha 12','Dr. Paulo Andrade','28/09/2026'],
  ['Fechar setembro e enviar o resumo ao contador, só totais (planilhas 18 e 20; bônus 24)','Dra. Carolina Mendes','05/10/2026']],0.5,1.6,[5.6,2.2,1.2],10,[0.38,0.46,0.42,0.42,0.42,0.38,0.42],['l','l','r']);
s.addText('Próxima reunião de resultado: 5 de outubro de 2026, com o fechamento de setembro.',{x:0.5,y:4.75,w:9,h:0.35,fontFace:H,fontSize:11,color:C.CINZA,isTextBox:true,margin:0});
s.addNotes('Próximos passos. Copie para a rotina da semana (planilha 03) e confira na próxima reunião o que foi feito. Não termine com "obrigado": termine com a data da próxima reunião.');
p.writeFile({fileName:path.join(__dirname,'27-modelo-resultado-do-mes-8-slides.pptx')}).then(f=>console.log('ok',f));
