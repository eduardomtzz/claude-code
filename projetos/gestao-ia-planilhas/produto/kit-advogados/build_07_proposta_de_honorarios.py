#!/usr/bin/env python3
"""Planilha 7 do Kit de Gestão para Advogados: Proposta de honorários. Gera 07-proposta-de-honorarios.xlsx"""
from ssg import *
from openpyxl.worksheet.page import PageMargins
from datetime import date
import dados
NS=8; NPAR=12; NR=100; R0=9; RN=R0+NR-1     # serviços na proposta, parcelas, linhas do registro
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Os dados do escritório aparecem no cabeçalho da proposta: antes da primeira proposta real, troque o nome (tire o \"(exemplo fictício)\"), telefone, e-mail e endereço.",merge_to="J")
campos=[("Nome do escritório",f"{dados.ESCRITORIO} (exemplo fictício)"),("Mês de referência","Setembro de 2026"),("Data de referência",dados.HOJE),
 ("Telefone e WhatsApp","(11) 0000-0000"),("E-mail","contato@exemplo.com.br"),("Endereço","Rua Exemplo, 100 · São Paulo · SP"),("Responsável pela proposta",dados.PESSOAS[0][0])]
for i,(a,v) in enumerate(campos):
    r=4+i; cfg.cell(row=r,column=1,value=a); rotulo(cfg.cell(row=r,column=1)); cfg.cell(row=r,column=2,value=v)
    if r==6: calc(cfg.cell(row=r,column=2),DATA)
    else: inp(cfg.cell(row=r,column=2))
cfg["A11"]="O nome acima sai impresso no cabeçalho e na assinatura da proposta. Apague o \"(exemplo fictício)\" antes de enviar a primeira proposta."; nota(cfg["A11"])
cfg["A12"]="Listas (preencha de cima para baixo, sem pular linha)"; rotulo(cfg["A12"])
listas={4:("Áreas",dados.AREAS),6:("Modalidades",dados.TIPOS_HON),8:("Formas de pagamento",["Pix","Transferência","Boleto","Cartão"]),10:("Situações",["Enviada","Fechada","Perdida"])}
for col,(nome,vals) in listas.items():
    cfg.cell(row=13,column=col,value=nome); rotulo(cfg.cell(row=13,column=col))
    for i in range(20): inp(cfg.cell(row=14+i,column=col))
    for i,v in enumerate(vals): cfg.cell(row=14+i,column=col,value=v)
def LST(col): return f"=OFFSET(Config!${col}$14,0,0,MAX(1,COUNTA(Config!${col}$14:${col}$33)),1)"
widths(cfg,(30,44,3,18,3,14,3,20,3,14)); cfg.sheet_view.showGridLines=False
# ---------- Proposta ----------
p=wb.create_sheet("Proposta",0)
DT="$E$4"
titulo(p,'=Config!$B$4&" · Proposta de honorários · "&TEXT(DAY($E$4),"00")&"/"&TEXT(MONTH($E$4),"00")&"/"&YEAR($E$4)',
       "Preencha o amarelo. A tabela abaixo sai pronta para imprimir em A4 (Arquivo > Imprimir) ou salvar em PDF e enviar ao cliente.",merge_to="E")
p["A3"]='=Config!$B$7&" · "&Config!$B$8&" · "&Config!$B$9'; nota(p["A3"]); p.merge_cells("A3:E3")
cab=[("Proposta nº",dados.PROP_NUM_ATUAL,None,"Data",'=TODAY()',DATA),("Cliente",dados.CLIENTES[7][0],None,"Válida por (dias)",15,"0"),
     ("Contato do cliente","roberto@exemplo.com.br",None,"Válida até","=E4+E5",DATA),("Área","Cível",None,"Modalidade","Misto",None)]
for i,(a,v,fa,d,e,fe) in enumerate(cab):
    r=4+i
    p.cell(row=r,column=1,value=a); rotulo(p.cell(row=r,column=1)); p.cell(row=r,column=2,value=v); inp(p.cell(row=r,column=2),fa)
    p.cell(row=r,column=4,value=d); rotulo(p.cell(row=r,column=4)); p.cell(row=r,column=5,value=e)
    if r==6: calc(p.cell(row=r,column=5),fe)
    else: inp(p.cell(row=r,column=5),fe,center=True)
p["A8"]="Objeto (resumo do serviço)"; rotulo(p["A8"]); p["B8"]="Acompanhamento da discussão sobre contrato de prestação de serviços, da análise inicial ao encerramento."
inp(p["B8"]); p.merge_cells("B8:E8"); p["B8"].alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[8].height=32
for dv,cell in ((lista(LST("D")),"B7"),(lista(LST("F")),"E7")): dv.add(cell); p.add_data_validation(dv)
# serviços
S0=11; SN=S0+NS-1; ST=SN+1
p.cell(row=S0-1,column=1,value="Serviços e etapas").font=F(bold=True,size=12,color=UVA)
hdr(p,S0,["Etapa ou serviço","O que inclui","Prazo previsto","Horas previstas","Valor (R$)"])
for r in range(S0+1,SN+2):
    for c in (1,2,3): inp(p.cell(row=r,column=c))
    p.cell(row=r,column=2).alignment=Alignment(wrap_text=True,vertical="top")
    inp(p.cell(row=r,column=4),"0",center=True); inp(p.cell(row=r,column=5),BRL,center=True)
ST=SN+2
p.cell(row=ST,column=1,value="Total dos honorários fixos"); rotulo(p.cell(row=ST,column=1)); p.cell(row=ST,column=1).border=borda
p.cell(row=ST,column=4,value=f"=SUM(D{S0+1}:D{SN+1})"); calc(p.cell(row=ST,column=4),"0")
p.cell(row=ST,column=5,value=f"=SUM(E{S0+1}:E{SN+1})"); calc(p.cell(row=ST,column=5),BRL); p.cell(row=ST,column=5).font=F(bold=True,color=UVA,size=10)
p.cell(row=ST+1,column=1,value="Honorários de êxito (% sobre o resultado)"); rotulo(p.cell(row=ST+1,column=1)); p.cell(row=ST+1,column=1).border=borda
p.cell(row=ST+1,column=5,value=0.15); inp(p.cell(row=ST+1,column=5),PCT,center=True)
p.cell(row=ST+1,column=2,value="Sobre o valor efetivamente recebido ou economizado pelo cliente ao fim do caso. Deixe 0% se não houver."); inp(p.cell(row=ST+1,column=2)); p.merge_cells(start_row=ST+1,start_column=2,end_row=ST+1,end_column=4)
TOT=f"$E${ST}"
# condições
Q0=ST+4
p.cell(row=Q0-1,column=1,value="Condições de pagamento").font=F(bold=True,size=12,color=UVA)
# Auditoria final (G05): entrada e parcela arredondadas ao centavo e a última parcela fecha a
# diferença; 4.500 com 40 % em 7× dava 7 × 385,71 = 4.499,97 com "confere: Sim".
cond=[("Entrada (% do valor fixo)",0.40,PCT,"Entrada (R$)",f"=ROUND({TOT}*B{Q0},2)",BRL),
      ("Parcelas do restante (1 a 12)",3,"0","Restante (R$)",f'=IF(AND(B{Q0+1}=0,{TOT}-E{Q0}>0),"ATENÇÃO: "&FIXED({TOT}-E{Q0},2)&" sem parcelas",{TOT}-E{Q0})',BRL),
      ("Primeira parcela (dias após a entrada)",30,"0","Valor da parcela (R$; a última fecha o centavo)",f'=IF(B{Q0+1}=0,0,ROUND(E{Q0+1}/B{Q0+1},2))',BRL),
      ("Intervalo entre parcelas (dias)",30,"0","Forma de pagamento","Pix",None)]
for i,(a,v,fa,d,e,fe) in enumerate(cond):
    r=Q0+i
    p.cell(row=r,column=1,value=a); rotulo(p.cell(row=r,column=1)); p.cell(row=r,column=2,value=v); inp(p.cell(row=r,column=2),fa,center=True)
    p.cell(row=r,column=4,value=d); rotulo(p.cell(row=r,column=4)); p.cell(row=r,column=5,value=e)
    if i==3: inp(p.cell(row=r,column=5),center=True)
    else: calc(p.cell(row=r,column=5),fe)
# Zero só é aceitável quando a entrada quita 100 %: senão sobra saldo sem cronograma.
dvn=DataValidation(type="custom",
                   formula1=f'=AND(B{Q0+1}=INT(B{Q0+1}),B{Q0+1}>=0,B{Q0+1}<={NPAR},OR(B{Q0+1}>0,ROUND({TOT}-E{Q0},2)<=0))',
                   allow_blank=False,showErrorMessage=True,
                   errorTitle="Parcelas do restante",
                   error=f"Digite um número inteiro de 1 a {NPAR}. Zero só é aceito quando a entrada quita o valor todo; com saldo em aberto, a proposta precisa de cronograma.")
dvn.add(f"B{Q0+1}"); p.add_data_validation(dvn)
dvf=lista(LST("H")); dvf.add(f"E{Q0+3}"); p.add_data_validation(dvf)
ENT=f"$B${Q0}"; NPA=f"$B${Q0+1}"; D1=f"$B${Q0+2}"; INT=f"$B${Q0+3}"; VENT=f"$E${Q0}"; VPAR=f"$E${Q0+2}"
# cronograma
K0=Q0+6
p.cell(row=K0-1,column=1,value="Cronograma de pagamento").font=F(bold=True,size=12,color=UVA)
hdr(p,K0,["Parcela","Vencimento","Valor (R$)"])
p.cell(row=K0+1,column=1,value=f'=IF({VENT}=0,"","Entrada")'); calc(p.cell(row=K0+1,column=1),center=False)
p.cell(row=K0+1,column=2,value=f'=IF({VENT}=0,"","Na aceitação da proposta")'); calc(p.cell(row=K0+1,column=2))
p.cell(row=K0+1,column=3,value=f'=IF({VENT}=0,"",{VENT})'); calc(p.cell(row=K0+1,column=3),BRL)
for n in range(1,NPAR+1):
    r=K0+1+n
    p.cell(row=r,column=1,value=f'=IF({n}>{NPA},"","Parcela {n} de "&{NPA})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({n}>{NPA},"",{DT}+{D1}+({n}-1)*{INT})'); calc(p.cell(row=r,column=2),DATA)
    p.cell(row=r,column=3,value=f'=IF({n}>{NPA},"",IF({n}={NPA},$E${Q0+1}-{VPAR}*({NPA}-1),{VPAR}))'); calc(p.cell(row=r,column=3),BRL)
KN=K0+1+NPAR
p.cell(row=KN+1,column=1,value="Total"); rotulo(p.cell(row=KN+1,column=1)); p.cell(row=KN+1,column=1).border=borda
p.cell(row=KN+1,column=3,value=f"=SUM(C{K0+1}:C{KN})"); calc(p.cell(row=KN+1,column=3),BRL); p.cell(row=KN+1,column=3).font=F(bold=True,color=UVA,size=10)
# conferência: o cronograma tem de somar o valor da proposta. Sem ela, entrada parcial com
# zero parcelas saía "válida" e o cliente recebia uma proposta sem vencimentos.
p.cell(row=KN+2,column=1,value="Confere com o valor da proposta?"); rotulo(p.cell(row=KN+2,column=1)); p.cell(row=KN+2,column=1).border=borda
p.cell(row=KN+2,column=3,value=f'=IF(ABS(C{KN+1}-{TOT})<0.01,"Sim","NÃO: faltam "&FIXED({TOT}-C{KN+1},2)&" sem vencimento. Ajuste a entrada ou o número de parcelas antes de enviar.")')
calc(p.cell(row=KN+2,column=3),center=False); p.cell(row=KN+2,column=3).font=F(bold=True,color=UVA,size=10)
p.merge_cells(start_row=KN+2,start_column=3,end_row=KN+2,end_column=6)
p.conditional_formatting.add(f"C{KN+2}", FormulaRule(formula=[f'LEFT(C{KN+2},3)="NÃO"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"C{KN+2}", FormulaRule(formula=[f'C{KN+2}="Sim"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10,bold=True)))
p.cell(row=K0,column=5,value="Datas contadas a partir da data da proposta. Se o aceite demorar, refaça a proposta com a data nova."); nota(p.cell(row=K0,column=5)); p.cell(row=K0,column=5).alignment=Alignment(wrap_text=True,vertical="top"); p.cell(row=K0,column=5).font=F(size=9,color=LILAS)
# condições gerais
G0=KN+4
p.cell(row=G0-1,column=1,value="Condições gerais").font=F(bold=True,size=12,color=UVA)
gerais=["Despesas do caso (taxas, deslocamentos, cópias, terceiros) são cobradas à parte, mediante comprovante.",
        "Os valores valem para as etapas descritas acima. Serviços fora deste escopo serão orçados separadamente.",
        "Os honorários de êxito, quando previstos, são calculados sobre o resultado efetivamente obtido, ao fim do caso."]
for i,t in enumerate(gerais):
    r=G0+i; p.cell(row=r,column=1,value=t); inp(p.cell(row=r,column=1)); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=5)
    p.cell(row=r,column=1).alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[r].height=28
r=G0+3
p.cell(row=r,column=1,value='="Forma de pagamento: "&$E$'+str(Q0+3)+'&". Esta proposta é válida até "&TEXT(DAY($E$6),"00")&"/"&TEXT(MONTH($E$6),"00")&"/"&YEAR($E$6)&"."'); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=5)
A0=r+3
p.cell(row=A0,column=1,value="De acordo:"); rotulo(p.cell(row=A0,column=1))
p.cell(row=A0+2,column=1,value="______________________________________"); p.cell(row=A0+2,column=4,value="______________________________________")
p.cell(row=A0+3,column=1,value="=$B$5"); p.cell(row=A0+3,column=4,value='=Config!$B$10&" · "&Config!$B$4')
for c in (1,4): p.cell(row=A0+3,column=c).font=F(size=10,color=TINTA)
p.cell(row=A0+5,column=1,value="A proposta não substitui o contrato de honorários do escritório; ela organiza o que foi combinado antes de formalizar.").font=F(size=9,color=LILAS)
widths(p,(34,44,22,14,16)); p.sheet_view.showGridLines=False
p.print_area=f"A1:E{A0+5}"; p.page_setup.paperSize=p.PAPERSIZE_A4; p.page_setup.orientation="portrait"
p.page_setup.fitToWidth=1; p.page_setup.fitToHeight=1; p.sheet_properties.pageSetUpPr.fitToPage=True
p.page_margins=PageMargins(left=0.6,right=0.6,top=0.6,bottom=0.6); p.print_options.horizontalCentered=True
servs=[("Análise inicial e planejamento","Reunião, leitura dos documentos e definição da estratégia","até 15 dias",8,900),
       ("Fase inicial","Redação e protocolo do pedido, acompanhamento das primeiras respostas","até 60 dias",18,1800),
       ("Acompanhamento até a decisão","Manifestações, audiências e reuniões com o cliente","durante o caso",22,1200),
       ("Encerramento","Prestação de contas e organização dos documentos finais","ao fim do caso",5,600)]
for i,row in enumerate(servs):
    for c,v in enumerate(row,start=1): p.cell(row=S0+1+i,column=c,value=v)
# ---------- Registro ----------
g=wb.create_sheet("Registro")
titulo(g,'=Config!$B$4&" · Registro de propostas · "&Config!$B$5',"Uma linha por proposta enviada. Atualize a situação quando o cliente responder; o alerta avisa validade vencida.",merge_to="M")
GJ=f"$J${R0}:$J${RN}"; GG=f"$G${R0}:$G${RN}"
kpi(g,4,1,"Aguardando resposta",f'=COUNTIF({GJ},"Enviada")',LAVANDA,UVA)
kpi(g,4,3,"Fechadas",f'=COUNTIF({GJ},"Fechada")',VERDE,VERDE_T)
kpi(g,4,5,"Perdidas",f'=COUNTIF({GJ},"Perdida")',VERM,VERM_T)
kpi(g,4,7,"Valor fechado",f'=SUMIFS({GG},{GJ},"Fechada")',SOL,UVA,fmt=BRL0)
kpi(g,4,9,"Taxa de fechamento",f'=IFERROR(C5/(C5+E5),0)',LAVANDA,UVA,fmt=PCT)
kpi(g,4,11,"Em aberto (R$)",f'=SUMIFS({GG},{GJ},"Enviada")',LAVANDA,UVA,fmt=BRL0)
hdr(g,R0-1,["Nº","Data de envio","Cliente","Área","Serviço","Modalidade","Valor proposto (R$)","Válida por (dias)","Válida até","Situação","Data da resposta","Alerta","Observação"],height=32)
for r in range(R0,RN+1):
    for c in (1,2,3,4,5,6,7,8,10,11,13): inp(g.cell(row=r,column=c))
    for c in (1,2,4,6,8,10,11): g.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    g.cell(row=r,column=2).number_format=DATA; g.cell(row=r,column=11).number_format=DATA; g.cell(row=r,column=7).number_format=BRL; g.cell(row=r,column=8).number_format="0"
    g.cell(row=r,column=9,value=f'=IF(OR(B{r}="",H{r}=""),"",B{r}+H{r})'); calc(g.cell(row=r,column=9),DATA)
    g.cell(row=r,column=12,value=f'=IF(A{r}="","",IF(J{r}<>"Enviada","",IF(I{r}="","",IF(I{r}<TODAY(),"Validade vencida · retomar contato",IF(I{r}-TODAY()<=3,"Vence em até 3 dias","")))))'); calc(g.cell(row=r,column=12),center=False)
for dv,rng in ((lista(LST("D"),strict=True),f"D{R0}:D{RN}"),(lista(LST("F")),f"F{R0}:F{RN}"),(lista(LST("J")),f"J{R0}:J{RN}"),
               (DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True),f"B{R0}:B{RN}")): dv.add(rng); g.add_data_validation(dv)
g.conditional_formatting.add(f"L{R0}:L{RN}", FormulaRule(formula=[f'LEFT($L{R0},8)="Validade"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
g.conditional_formatting.add(f"L{R0}:L{RN}", FormulaRule(formula=[f'LEFT($L{R0},5)="Vence"'], fill=fill(AMARELO)))
g.conditional_formatting.add(f"J{R0}:J{RN}", FormulaRule(formula=[f'$J{R0}="Fechada"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
g.conditional_formatting.add(f"J{R0}:J{RN}", FormulaRule(formula=[f'$J{R0}="Perdida"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
widths(g,(10,12,26,14,40,12,16,10,12,11,12,30,34)); g.freeze_panes=f"A{R0}"; g.sheet_view.showGridLines=False; g.auto_filter.ref=f"A{R0-1}:M{RN}"
# exemplo: as 10 propostas mais recentes já enviadas do funil da planilha 15 (mesmos clientes, valores e situação), da mais nova para a mais antiga
def _dt(x): return None if x is None else (dados.prazo_formula(x) if isinstance(x,int) else x)
for i,p in enumerate(dados.propostas_registro_07(NR if NR<10 else 10)):
    r=R0+i; sit=dados.SIT_07.get(p["etapa"],"Enviada")
    obs=p["obs"] if sit!="Perdida" else (p["motivo"]+(" · "+p["obs"] if p["obs"] else ""))
    for c,v in zip((1,2,3,4,5,6,7,8,10,11,13),(p["numero"],_dt(p["proposta"]),p["cliente"],p["area"],p["servico"],p["modalidade"],p["valor"],15,sit,_dt(p["fechamento"]),obs)):
        if v is not None: g.cell(row=r,column=c,value=v)
como_usar(wb,"Proposta de honorários",[
 ("O que esta planilha faz","Monta a proposta de honorários pronta para o cliente (etapas, valores, entrada, parcelas com datas, validade) e guarda o registro das propostas enviadas com situação e alerta de validade."),
 ("Passo 1","Em Config, dados do escritório (aparecem no cabeçalho) e as listas de áreas, modalidades, formas de pagamento e situações."),
 ("Passo 2","Em Proposta, preencha o amarelo: número, data, cliente, etapas com valor, percentual de êxito (se houver), entrada, parcelas e intervalo. O cronograma e a validade são calculados."),
 ("Passo 3","Imprima ou salve em PDF (Arquivo > Imprimir; já está ajustado para uma página A4) e envie. Depois anote a proposta na aba Registro."),
 ("Passo 4","Em Registro, atualize a situação quando o cliente responder. O topo mostra quantas estão aguardando, fechadas, perdidas e a taxa de fechamento. No exemplo, o Registro traz as 10 propostas mais recentes do funil da planilha 15 (as mesmas, com os mesmos valores); a 15 guarda o funil completo com etapas, origem e motivo de perda."),
 ("Rotina","Sexta-feira, 5 minutos: olhe os alertas do Registro e retome contato com quem está perto de vencer."),
 ("Com a IA","Copie a proposta e use o prompt \"Honorários 04 · Texto de apresentação da proposta\" da biblioteca do kit antes de enviar, ou \"Honorários 02 · Revisar a proposta pela margem\" para conferir o valor. Os valores vêm do Simulador (planilha 06)."),
])
proteger(wb); salvar(wb,"07-proposta-de-honorarios.xlsx","Proposta de honorários · Kit de Gestão para Advogados")
