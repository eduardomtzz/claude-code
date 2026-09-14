// Modelo 29: carteira e caixa do mês para o contador, 8 slides. Números: dados.py (custos fixos, pessoas, casos) e painel 17 (setembro/2026).
const path=require('path');
const {C,H,ROD,novo,rodape,titulo,cards,lista,tabela,capa,fecho}=require('./slides_base');
const p=novo('Carteira e caixa para o contador · modelo de 8 slides');
const NOTA0='Modelo do Kit de Gestão para Advogados: troque os textos e mantenha a estrutura. ';
// 1 capa
let s=capa(p,'Carteira e caixa de setembro de 2026','Ferraz & Lima Advocacia (exemplo fictício) · reunião mensal com o contador · 6 de outubro de 2026','Entrou R$ 29,4 mil, saiu R$ 20,2 mil, a receber R$ 128,3 mil. Oito dúvidas no slide 7.',ROD);
s.addNotes(NOTA0+'Capa. Reunião de 30 minutos: os números vêm prontos das planilhas 09 (Caixa), 10 (Provisão), 11 (Pró-labore), 13 (Carteira) e 14 (Inadimplência); o contador recebe os arquivos do slide 8 antes da reunião. O roteiro da reunião está no bônus do kit.');
// 2 receita por modalidade
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Receita do mês por modalidade','Recebimentos de setembro (regime de caixa), Caixa do escritório (09), aba Painel. Total: R$ 29.400.');
s.addChart(p.charts.BAR,[{name:'Recebido em setembro (R$)',labels:['Consultoria e pareceres','Honorários mistos (parte fixa)','Honorários de êxito','Honorários por hora','Honorários fixos'],values:[2600,4400,4000,9600,8800]}],
 {x:0.5,y:1.6,w:5.6,h:3.35,barDir:'bar',chartColors:[C.UVA],showValue:true,dataLabelPosition:'outEnd',dataLabelFontSize:9.5,dataLabelColor:C.TINTA,dataLabelFormatCode:'#,##0',
  catAxisLabelColor:C.CINZA,catAxisLabelFontSize:9.5,valAxisLabelColor:C.CINZA,valAxisLabelFontSize:9,valAxisLabelFormatCode:'#,##0',valGridLine:{color:C.GRADE,size:0.5},catGridLine:{style:'none'},showLegend:false,valAxisMinVal:0,valAxisMaxVal:12000,showTitle:false});
lista(s,['#Leitura','Agosto: R$ 27.900. Setembro é o maior mês do ano.','Cada recebimento está lançado por cliente, caso e forma de pagamento (Pix, transferência ou boleto).','Reembolso de custas: R$ 0 em setembro. Quando houver, vai em categoria própria, fora da receita (dúvida 4).','A receber já emitido e não pago no mês: R$ 7.500 (parcela final de um caso e um parecer).'],6.4,1.65,3.2,3.3,10.5);
rodape(p,s,false,ROD); s.addNotes('Receita por modalidade. Barras horizontais, uma série. Clique no gráfico > Editar dados. O contador precisa saber o que é honorário, o que é consultoria e o que é reembolso, porque o tratamento é diferente.');
// 3 saídas por categoria
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Saídas do mês por categoria','Caixa do escritório (09), aba Painel. Total pago ou provisionado em setembro: R$ 20.179.');
tabela(s,['Categoria','Setembro (R$)'],
 [['Pró-labore dos sócios (2 × R$ 6.000)','12.000'],['Aluguel e condomínio','2.800'],['Impostos e taxas (6% da receita)','1.764'],['Estagiária (bolsa)','1.400'],['Contador','600'],['Sistemas e assinaturas','450'],['Marketing e site','400'],['Material, correio e outros','395'],['Telefone e internet','220'],['Anuidades OAB e cursos','150'],['!Total','!20.179']],0.5,1.6,[3.5,1.4],9.5,0.28);
lista(s,['#Custo fixo','Sem pró-labore: R$ 6.415. Com pró-labore: R$ 18.415 por mês.','Custo-hora do escritório: R$ 84 (custo fixo com pró-labore ÷ 220 horas faturáveis dos sócios).','#Fora da tabela','Custas adiantadas para clientes: R$ 70 em setembro, a reembolsar (categoria própria, não é despesa do escritório).','Anuidade da OAB: paga em janeiro (R$ 1.100); R$ 150 por mês é a média com cursos.'],6.2,1.65,3.4,3.3,10.5);
rodape(p,s,false,ROD); s.addNotes('Saídas por categoria. As linhas são as mesmas da aba Config do Caixa (09): se mudar uma categoria lá, mude aqui. Pró-labore separado das demais, sempre.');
// 4 provisões
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Provisão de impostos, 13º e férias','Planilha Provisão (10). Separado no fechamento do mês e transferido para a conta reserva no dia 28.');
tabela(s,['Provisão','Base de cálculo','Setembro (R$)','Janeiro a setembro (R$)'],
 [['Impostos e taxas','6% da receita do mês (alíquota efetiva combinada com o contador)','1.764','13.236'],['13º dos sócios','1/12 do pró-labore (R$ 12.000 ÷ 12)','1.000','9.000'],['Recesso de janeiro','1/12 do custo fixo sem pró-labore (R$ 6.415 ÷ 12)','535','4.815'],['!Total provisionado','','!3.299','!27.051']],0.5,1.6,[2.2,3.6,1.5,1.7],10.5,[0.38,0.45,0.45,0.45,0.4],['l','l','r','r']);
lista(s,['#Regra do escritório','Impostos pagos no dia 20 do mês seguinte (regime de caixa); 13º e recesso pagos em dezembro e janeiro com o provisionado, sem usar o caixa do mês.','#Reserva','Alvo: três meses de custo fixo com pró-labore (R$ 55,2 mil). Aporte aprovado pelos sócios: R$ 4.000 por mês a partir de outubro (planilha 12).'],0.5,3.85,9,1.2,10.5);
rodape(p,s,false,ROD); s.addNotes('Provisões. A alíquota de 6% é do exemplo: o contador confirma a de cada mês (dúvida 1). Sem funcionário CLT no exemplo; se houver, acrescente 13º, férias e encargos como linha própria.');
// 5 recebíveis e vencidos
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Recebíveis e vencidos','Carteira de clientes e casos (13) e Parcelas e inadimplência (14), posição de 30/9.');
cards(p,s,[['R$ 128,3 mil','A receber','contratado menos recebido nos 38 casos'],['R$ 21,6 mil','Vencido (16,8%)','julho R$ 23,6 mil · agosto R$ 20,9 mil'],['R$ 36,0 mil','Êxito sem data','4 casos; entra só no fim, não é atraso']],1.6,1.85,1);
lista(s,['#O que o contador precisa saber','Com parcelas datadas (fixo, hora e misto): R$ 92,3 mil em 15 casos. Sem data (êxito): R$ 36 mil em 4 casos.','Nenhuma parcela foi dada como perdida em 2026; a régua de cobrança está em andamento nos R$ 21,6 mil vencidos.','Recebido de janeiro a setembro: R$ 220,6 mil, contra R$ 374,2 mil contratados na carteira.'],0.5,3.65,9,1.4,11);
rodape(p,s,false,ROD); s.addNotes('Recebíveis. O contador não cobra ninguém, mas precisa da posição para o balanço e para responder às dúvidas 3 e 6. Se houver parcela a dar baixa, traga o número.');
// 6 pró-labore e retiradas
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Pró-labore e retiradas por sócio','Pró-labore e separação pessoa física × escritório (11). Pagamento no dia 28, sempre da conta do escritório.');
tabela(s,['Pessoa','Pró-labore mensal','Janeiro a setembro','Retiradas extras','Distribuição proposta (out.)'],
 [['Marina Ferraz','R$ 6.000','R$ 54.000','R$ 0','R$ 6.000'],['Rafael Lima','R$ 6.000','R$ 54.000','R$ 0','R$ 6.000'],['Júlia Prado (bolsa de estágio)','R$ 1.400','R$ 12.600','—','—'],['!Total','!R$ 13.400','!R$ 120.600','!R$ 0','!R$ 12.000']],0.5,1.6,[2.6,1.5,1.6,1.5,1.8],10.5,[0.45,0.38,0.38,0.38,0.38],['l','r','r','r','r']);
lista(s,['#Regras da casa','Nenhuma despesa pessoal no cartão ou na conta do escritório; o que escapou foi lançado como retirada extra (zero em 2026).','#Proposta dos sócios','Sobrou R$ 40,7 mil de janeiro a setembro. Distribuir R$ 12 mil em outubro e manter o restante em reserva: depende da resposta à dúvida 2.'],0.5,3.75,9,1.3,11);
rodape(p,s,false,ROD); s.addNotes('Pró-labore. Pró-labore é custo fixo; distribuição de lucro é outra coisa e tem tratamento diferente: é exatamente o que se pergunta ao contador.');
// 7 dúvidas
s=p.addSlide(); s.background={color:C.BR}; titulo(s,'Dúvidas para o contador','Oito perguntas. As respostas vão para a aba Config das planilhas e para a ata da reunião.');
lista(s,['Alíquota efetiva de setembro e enquadramento: o faturamento dos últimos 12 meses muda alguma coisa?',
 'Distribuição de R$ 12 mil em outubro (R$ 6 mil por sócio): o que precisa estar apurado antes e como registrar?',
 'Honorários de êxito: nota e imposto no recebimento ou em outro momento? Como lançar os R$ 36 mil sem data?',
 'Reembolso de custas adiantadas para clientes: como lançar para não entrar como receita?',
 'Estagiária: bolsa, recesso e documentos que o escritório deve guardar.',
 'Parcela vencida há mais de 90 dias sem acordo: quando e como dar baixa?',
 '13º dos sócios: pró-labore extra em dezembro ou distribuição? Qual pesa menos?',
 'Calendário de guias e obrigações de outubro a dezembro, para entrar na Agenda do escritório.'],0.5,1.62,9,3.4,12,true);
rodape(p,s,false,ROD); s.addNotes('Dúvidas. Lista numerada para o contador responder por escrito. Perguntas de gestão e contabilidade; nada de consulta jurídica aqui. Guarde as respostas na aba Config das planilhas citadas.');
// 8 anexos
s=fecho(p,'Anexos enviados com este resumo',['09 · Caixa do escritório: aba Lançamentos filtrada em setembro e aba Painel.','10 · Provisão de impostos, 13º e férias: aba Painel.','11 · Pró-labore e separação pessoa física × escritório: aba Painel.','13 · Carteira de clientes e casos e 14 · Parcelas e inadimplência: abas Painel e Vencidos.','18 · Resultado mensal simplificado e 20 · Resumo do mês (texto gerado pelo prompt "Preparar a reunião com o contador").','Fora do kit: extratos bancários de setembro e guias pagas.'],ROD);
s.addText('Tudo em .xlsx, com as fórmulas; o contador não precisa alterar nada. Próxima reunião: 5 de novembro de 2026.',{x:0.5,y:4.6,w:9,h:0.4,fontFace:H,fontSize:11,color:C.LILC,isTextBox:true,margin:0});
s.addNotes('Anexos. Diga exatamente que arquivo e que aba o contador recebe. Envie três dias antes da reunião e termine com a data da próxima.');
p.writeFile({fileName:path.join(__dirname,'29-modelo-carteira-para-o-contador-8-slides.pptx')}).then(f=>console.log('ok',f));
