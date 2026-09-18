#!/usr/bin/env python3
"""Planilha 15 do Kit de Gestão para Médicos: Orçamentos apresentados × aprovados (funil da recepção).
Gera 15-orcamentos.xlsx (Como usar, Painel, Config, Orçamentos). Exemplo: dados.ORCAMENTOS (junho a setembro; aprovados viraram atendimentos na 01)."""
from ssg import *
import dados
from openpyxl.chart import BarChart, Reference

N=300; R0=5; RN=R0+N-1
NL=10; L0=18; L1=L0+NL-1           # listas da Config: linhas 18..27
E0=10; E1=14                       # etapas: linhas 10..14
ETAPAS=[("Apresentado",0.30),("Em análise",0.50),("Aprovado",1.0),("Recusado",0.0),("Sem retorno",0.0)]
def off(sheet,col,r0,r1): return f"=OFFSET({sheet}!${col}${r0},0,0,MAX(1,COUNTA({sheet}!${col}${r0}:${col}${r1})),1)"
def dstr(ref): return f'TEXT(DAY({ref}),"00")&"/"&TEXT(MONTH({ref}),"00")&"/"&YEAR({ref})'
NOME=f"{dados.CLINICA} (exemplo fictício)"
HOJE="Config!$B$5"; META="Config!$B$6"; PAR="Config!$B$7"

wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. As probabilidades por etapa alimentam a previsão ponderada.",merge_to="J")
cfg["A4"]="Clínica"; cfg["B4"]=NOME
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]=dados.HOJE
cfg["A6"]="Meta de orçamentos aprovados no trimestre (R$)"; cfg["B6"]=dados.META_APROVADO_TRI
cfg["A7"]="Orçamento parado há mais de (dias)"; cfg["B7"]=7
for r in range(4,8): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],BRL0); inp(cfg["B7"],center=True)
hdr(cfg,9,["Etapa","Probabilidade de aprovar"])
for i,(e,pb) in enumerate(ETAPAS):
    r=E0+i; cfg.cell(row=r,column=1,value=e).font=F(size=10,color=TINTA); cfg.cell(row=r,column=1).border=borda
    inp(cfg.cell(row=r,column=2),PCT,center=True); cfg.cell(row=r,column=2).value=pb
cfg["A15"]="Etapas fixas: apresentado → em análise → aprovado, recusado ou sem retorno. Ajuste só as probabilidades, pela sua experiência."; nota(cfg["A15"])
for col,nome in ((1,"Tipos de orçamento"),(3,"Motivos de recusa"),(5,"Profissionais"),(7,"Itens mais comuns")): hdr(cfg,L0-1,[nome],start=col)
for r in range(L0,L1+1):
    for c in (1,3,5,7): inp(cfg.cell(row=r,column=c))
cfg.cell(row=L1+2,column=1,value="Preencha cada lista de cima para baixo, sem pular linha: as listas suspensas de Orçamentos param na primeira célula vazia. Até 10 itens por lista. Itens é texto livre; a lista só sugere.").font=F(size=9,color=LILAS)
cfg.cell(row=L1+3,column=1,value="Orçamento aqui é o valor apresentado ao paciente para exames e pacotes particulares (nome administrativo; sem indicação clínica). Aprovado vira horário na agenda (01).").font=F(size=9,color=LILAS)
widths(cfg,(44,20,3,26,3,24,3,44,3,3)); cfg.sheet_view.showGridLines=False
TIPO_L=off("Config","A",L0,L1); MOT_L=off("Config","C",L0,L1); RESP_L=off("Config","E",L0,L1); ITEM_L=off("Config","G",L0,L1)

# ---------- Orçamentos ----------
o=wb.create_sheet("Orçamentos")
titulo(o,"Orçamentos","Uma linha por orçamento apresentado. Atualize a etapa conforme a resposta; ao decidir, marque Aprovado, Recusado ou Sem retorno, a data e, se recusado, o motivo.",merge_to="P")
hdr(o,4,["Data","Paciente","Profissional","Tipo","Itens","Valor (R$)","Etapa","Data da decisão","Motivo (se recusado)","Observação","Probabilidade","Valor ponderado","Dias em aberto","Dias até decidir","Situação","Mês"],height=32)
for r in range(R0,RN+1):
    for c in range(1,11): inp(o.cell(row=r,column=c))
    for c in (1,3,4,6,7,8,9): o.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    for c in (1,8): o.cell(row=r,column=c).number_format=DATA
    o.cell(row=r,column=6).number_format=BRL0
    o.cell(row=r,column=11,value=f'=IF(G{r}="","",IFERROR(INDEX(Config!$B${E0}:$B${E1},MATCH(G{r},Config!$A${E0}:$A${E1},0)),0))'); calc(o.cell(row=r,column=11),PCT)
    o.cell(row=r,column=12,value=f'=IF(OR(G{r}="",F{r}=""),"",F{r}*K{r})'); calc(o.cell(row=r,column=12),BRL0)
    o.cell(row=r,column=13,value=f'=IF(OR(G{r}="",G{r}="Aprovado",G{r}="Recusado",G{r}="Sem retorno",A{r}=""),"",{HOJE}-A{r})'); calc(o.cell(row=r,column=13),"0")
    o.cell(row=r,column=14,value=f'=IF(AND(OR(G{r}="Aprovado",G{r}="Recusado"),H{r}<>"",A{r}<>"",H{r}>=A{r}),H{r}-A{r},"")'); calc(o.cell(row=r,column=14),"0")
    o.cell(row=r,column=15,value=f'=IF(G{r}="","",IF(OR(G{r}="Aprovado",G{r}="Recusado",G{r}="Sem retorno"),G{r},IF(AND(M{r}<>"",M{r}>{PAR}),"Parado","Ativo")))'); calc(o.cell(row=r,column=15))
    o.cell(row=r,column=16,value=f'=IF(A{r}="","",DATE(YEAR(A{r}),MONTH(A{r}),1))'); calc(o.cell(row=r,column=16),"mm/yyyy")
    # chave INTEIRA (ver o comentário igual na 16): a soma de valor/1E+6 com ROW()/1E+5
    # colidia com R$ 10 de diferença em linhas vizinhas.
    # chave inteira: situação · dias (teto 500) · valor em CENTAVOS (teto R$ 999.999,99) · linha.
    # Máximo 3,5E+15, abaixo de 2^53. ROUND(valor,0) empatava 380,00 com 379,99 (rodada 4).
    o.cell(row=r,column=17,value=f'=IF(OR(G{r}="",O{r}="Aprovado",O{r}="Recusado",O{r}="Sem retorno"),0,IF(O{r}="Parado",2,1)*1E+15+MIN(N(M{r}),500)*1E+12+MIN(ROUND(N(F{r})*100,0),99999999)*1E+4+({RN}+1-ROW()))'); o.cell(row=r,column=17).font=F(color=CINZA,size=9)
o.column_dimensions["Q"].hidden=True
dvs=[lista(RESP_L), lista(TIPO_L), lista(ITEM_L,strict=True), lista(f"=Config!$A${E0}:$A${E1}"), lista(MOT_L,strict=True),
     DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True), DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True,showErrorMessage=True)]
for dv,rng in zip(dvs,[f"C{R0}:C{RN}",f"D{R0}:D{RN}",f"E{R0}:E{RN}",f"G{R0}:G{RN}",f"I{R0}:I{RN}",f"A{R0}:A{RN}",f"F{R0}:F{RN}"]): dv.add(rng); o.add_data_validation(dv)
dvh=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True); dvh.add(f"H{R0}:H{RN}"); o.add_data_validation(dvh)
o.conditional_formatting.add(f"A{R0}:O{RN}", FormulaRule(formula=[f'$O{R0}="Parado"'], fill=fill("FFF4CC")))
o.conditional_formatting.add(f"A{R0}:O{RN}", FormulaRule(formula=[f'$O{R0}="Aprovado"'], font=F(color=VERDE_T,size=10,bold=True)))
o.conditional_formatting.add(f"A{R0}:O{RN}", FormulaRule(formula=[f'OR($O{R0}="Recusado",$O{R0}="Sem retorno")'], font=F(color="8A86A0",size=10)))
o.conditional_formatting.add(f"I{R0}:I{RN}", FormulaRule(formula=[f'AND($G{R0}="Recusado",$I{R0}="")'], fill=fill(VERM)))
o.cell(row=RN+2,column=1,value="Amarelo: parado há mais dias que o limite da Config. Verde: aprovado. Cinza: recusado ou sem retorno. Motivo em vermelho: recusado sem motivo (preencha, é o que ensina). Datas de orçamentos ainda abertos no exemplo são relativas a hoje.").font=F(size=9,color=LILAS)
o.cell(row=RN+3,column=1,value="A data da decisão nunca é anterior à da apresentação: um orçamento aprovado hoje para um exame marcado para a semana que vem tem apresentação e decisão no passado e o agendamento no futuro (a observação guarda a data marcada). Se \"Dias até decidir\" ficar vazio numa linha decidida, é sinal de que as duas datas estão trocadas.").font=F(size=9,color=LILAS)
o.cell(row=RN+4,column=1,value="Orçamento aprovado a prazo: só para quem não tem parcela vencida em aberto na planilha 14. Com parcela em atraso, o combinado é à vista — a mesma regra da régua de cobrança.").font=F(size=9,color=LILAS)
widths(o,(11,26,22,20,36,12,13,12,24,30,11,13,9,9,12,9)); o.freeze_panes="C5"; o.sheet_view.showGridLines=False; o.auto_filter.ref=f"A4:P{RN}"

# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,f'=Config!$B$4&" · Orçamentos apresentados × aprovados · "&{dstr(HOJE)}',"Nada para digitar aqui: tudo vem de Orçamentos e Config.",merge_to="L")
p.merge_cells("A1:L1")
OA=f"Orçamentos!$A${R0}:$A${RN}"; OB=f"Orçamentos!$B${R0}:$B${RN}"; OC=f"Orçamentos!$C${R0}:$C${RN}"; OD=f"Orçamentos!$D${R0}:$D${RN}"; OE=f"Orçamentos!$E${R0}:$E${RN}"
OF=f"Orçamentos!$F${R0}:$F${RN}"; OG=f"Orçamentos!$G${R0}:$G${RN}"; OH=f"Orçamentos!$H${R0}:$H${RN}"; OI=f"Orçamentos!$I${R0}:$I${RN}"; OL=f"Orçamentos!$L${R0}:$L${RN}"
OM=f"Orçamentos!$M${R0}:$M${RN}"; ON=f"Orçamentos!$N${R0}:$N${RN}"; OO=f"Orçamentos!$O${R0}:$O${RN}"; OQ=f"Orçamentos!$Q${R0}:$Q${RN}"
ABERTO=f'{OG},"<>Aprovado",{OG},"<>Recusado",{OG},"<>Sem retorno",{OG},"<>"'
TRI=f'DATE(YEAR({HOJE}),3*INT((MONTH({HOJE})-1)/3)+1,1)'
# Limite SUPERIOR do trimestre: sem ele, fechamento de trimestre posterior entrava
# no total do trimestre consultado.
TRI_FIM=f'DATE(YEAR({HOJE})+(3*INT((MONTH({HOJE})-1)/3)+4>12),IF(3*INT((MONTH({HOJE})-1)/3)+4>12,1,3*INT((MONTH({HOJE})-1)/3)+4),1)'
DECID=f'(COUNTIFS({OG},"Aprovado")+COUNTIFS({OG},"Recusado")+COUNTIFS({OG},"Sem retorno"))'
kpi(p,4,1,"Em aberto (R$)",f'=SUMIFS({OF},{ABERTO})',LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Previsão ponderada",f'=SUMIFS({OL},{ABERTO})',SOL,UVA,fmt=BRL0)
kpi(p,4,5,"Aprovado no trimestre",f'=SUMIFS({OF},{OG},"Aprovado",{OH},">="&{TRI},{OH},"<"&{TRI_FIM})',VERDE,VERDE_T,fmt=BRL0)
kpi(p,4,7,"% da meta",f'=IFERROR(E5/{META},0)',VERDE,VERDE_T,fmt=PCT)
kpi(p,4,9,"Taxa de aprovação",f'=IFERROR(COUNTIFS({OG},"Aprovado")/{DECID},0)',LAVANDA,UVA,fmt=PCT)
kpi(p,4,11,"Dias até decidir (média)",f'=IFERROR(AVERAGEIFS({ON},{OG},"Aprovado"),0)',LAVANDA,UVA,fmt="0")
p["A7"]="Taxa de aprovação = aprovados ÷ (aprovados + recusados + sem retorno). Dias até decidir = da apresentação à decisão, média dos aprovados. Aprovado no trimestre soma pela data da decisão."; nota(p["A7"]); p.merge_cells("A7:L7")
p["A9"]="Funil por etapa"; p["A9"].font=F(bold=True,size=13,color=UVA)
hdr(p,10,["Etapa","Orçamentos","Valor (R$)","Ponderado (R$)","Barra"]); p.merge_cells("E10:H10")
for i,(e,pb) in enumerate(ETAPAS[:2]):
    r=11+i
    p.cell(row=r,column=1,value=f'=Config!$A${E0+i}'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=COUNTIFS({OG},A{r})'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=SUMIFS({OF},{OG},A{r})'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f'=SUMIFS({OL},{OG},A{r})'); calc(p.cell(row=r,column=4),BRL0)
    p.cell(row=r,column=5,value=f'=REPT("█",ROUND(IFERROR(C{r}/MAX($C$11:$C$15),0)*30,0))'); p.cell(row=r,column=5).font=F(size=10,color=LILAS); p.cell(row=r,column=5).border=borda; p.merge_cells(start_row=r,start_column=5,end_row=r,end_column=8)
for i,e in enumerate(("Aprovado","Recusado","Sem retorno")):
    r=13+i
    p.cell(row=r,column=1,value=e+" (total)"); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=COUNTIFS({OG},"{e}")'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=SUMIFS({OF},{OG},"{e}")'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=5,value=f'=REPT("█",ROUND(IFERROR(C{r}/MAX($C$11:$C$15),0)*30,0))'); p.cell(row=r,column=5).font=F(size=10,color=LILAS if e=="Aprovado" else "B0A6C4"); p.cell(row=r,column=5).border=borda; p.merge_cells(start_row=r,start_column=5,end_row=r,end_column=8)
p.cell(row=16,column=1,value="Valor médio dos aprovados"); calc(p.cell(row=16,column=1),center=False); p.cell(row=16,column=2,value='=IFERROR(C13/B13,0)'); calc(p.cell(row=16,column=2),BRL0)
p["A18"]="Retomar contato primeiro"; p["A18"].font=F(bold=True,size=13,color=UVA)
p["A19"]="Orçamentos abertos parados há mais tempo; os de maior valor primeiro. Sem insistência: uma mensagem educada perguntando se ficou alguma dúvida."; nota(p["A19"]); p.merge_cells("A19:L19")
hdr(p,20,["#","Paciente","Itens","Etapa","Valor (R$)","Dias em aberto","Situação","Profissional"])
TOP=8
for k in range(1,TOP+1):
    r=20+k; m=f'MATCH(LARGE({OQ},{k}),{OQ},0)'; g=f'LARGE({OQ},{k})>0'
    p.cell(row=r,column=1,value=k); calc(p.cell(row=r,column=1))
    for col,src in zip((2,3,4,5,6,7,8),("B","E","G","F","M","O","C")):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},INDEX(Orçamentos!${src}${R0}:${src}${RN},{m}),""),"")'); calc(p.cell(row=r,column=col),center=(col not in (2,3,8)))
    p.cell(row=r,column=5).number_format=BRL0; p.cell(row=r,column=6).number_format="0"
p.conditional_formatting.add(f"A21:H{20+TOP}", FormulaRule(formula=['$G21="Parado"'], fill=fill("FFF4CC")))
ra=20+TOP+2
p.cell(row=ra,column=1,value="Por tipo").font=F(bold=True,size=13,color=UVA)
hdr(p,ra+1,["Tipo","Orçamentos","Aprovados","Recusados / sem retorno","Taxa de aprovação","Valor aprovado (R$)","Em aberto (R$)"],height=32)
for i in range(NL):
    r=ra+2+i; src=f"Config!$A${L0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({OD},{src}))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({OD},{src},{OG},"Aprovado"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({OD},{src},{OG},"Recusado")+COUNTIFS({OD},{src},{OG},"Sem retorno"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",IFERROR(C{r}/(C{r}+D{r}),0))'); calc(p.cell(row=r,column=5),PCT)
    p.cell(row=r,column=6,value=f'=IF({src}="","",SUMIFS({OF},{OD},{src},{OG},"Aprovado"))'); calc(p.cell(row=r,column=6),BRL0)
    p.cell(row=r,column=7,value=f'=IF({src}="","",SUMIFS({OF},{OD},{src},{ABERTO}))'); calc(p.cell(row=r,column=7),BRL0)
rm=ra+2+NL+1
p.cell(row=rm,column=1,value="Motivos de recusa").font=F(bold=True,size=13,color=UVA)
hdr(p,rm+1,["Motivo","Recusados","Valor (R$)","% dos recusados"])
for i in range(NL):
    r=rm+2+i; src=f"Config!$C${L0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({OI},{src},{OG},"Recusado")+COUNTIFS({OI},{src},{OG},"Sem retorno"))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({OF},{OI},{src},{OG},"Recusado")+SUMIFS({OF},{OI},{src},{OG},"Sem retorno"))'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f'=IF({src}="","",IFERROR(B{r}/($B$14+$B$15),0))'); calc(p.cell(row=r,column=4),PCT)
hdr(p,rm+1,["Profissional","Orçamentos","Aprovados","Taxa de aprovação","Valor aprovado (R$)"],start=6)
for i in range(NL):
    r=rm+2+i; src=f"Config!$E${L0+i}"
    p.cell(row=r,column=6,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=6),center=False)
    p.cell(row=r,column=7,value=f'=IF({src}="","",COUNTIFS({OC},{src}))'); calc(p.cell(row=r,column=7))
    p.cell(row=r,column=8,value=f'=IF({src}="","",COUNTIFS({OC},{src},{OG},"Aprovado"))'); calc(p.cell(row=r,column=8))
    p.cell(row=r,column=9,value=f'=IF({src}="","",IFERROR(H{r}/(H{r}+COUNTIFS({OC},{src},{OG},"Recusado")+COUNTIFS({OC},{src},{OG},"Sem retorno")),0))'); calc(p.cell(row=r,column=9),PCT)
    p.cell(row=r,column=10,value=f'=IF({src}="","",SUMIFS({OF},{OC},{src},{OG},"Aprovado"))'); calc(p.cell(row=r,column=10),BRL0)
p.cell(row=rm+2+NL+1,column=1,value="Fonte: aba Orçamentos. Um orçamento recusado com o motivo anotado vale mais que três sem: é o que mostra o que ajustar no preço, no prazo ou na forma de apresentar. Nunca prometa resultado ao paciente para fechar um orçamento.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=rm+2+NL+1,start_column=1,end_row=rm+2+NL+1,end_column=12)
bc=BarChart(); bc.type="bar"; bc.height=6; bc.width=13; bc.title="Valor por etapa (R$)"; bc.style=2
bc.add_data(Reference(p,min_col=3,min_row=10,max_row=15),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=11,max_row=15))
bc.series[0].graphicalProperties.solidFill="3B1F5E"; bc.legend=None; bc.x_axis.majorGridlines=None
p.add_chart(bc,"J9")
widths(p,(26,26,34,16,15,16,16,14,14,16,12,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False

# ---------- Exemplo ----------
for i,v in enumerate(dados.TIPOS_ORC): cfg.cell(row=L0+i,column=1,value=v)
for i,v in enumerate(dados.MOTIVOS_ORC): cfg.cell(row=L0+i,column=3,value=v)
for i,n in enumerate(dados.MEDICOS): cfg.cell(row=L0+i,column=5,value=n)
for i,v in enumerate(["Consulta + ECG + teste ergométrico","MAPA","Holter","MAPA + Holter","Teste ergométrico","Avaliação endócrina + retorno","Consulta + 2 retornos (acompanhamento)"]): cfg.cell(row=L0+i,column=7,value=v)
def _dt(x): return None if x is None else (dados.prazo_formula(x) if isinstance(x,int) else x)
for i,ob in enumerate(dados.ORCAMENTOS):
    r=R0+i
    for c,v in zip(range(1,11),(_dt(ob["data"]),ob["paciente"],ob["profissional"],ob["tipo"],ob["itens"],ob["valor"],ob["etapa"],_dt(ob["decisao"]),ob["motivo"],ob["obs"])):
        if v not in (None,""): o.cell(row=r,column=c,value=v)
print(len(dados.ORCAMENTOS),"orçamentos no exemplo")

como_usar(wb,"Orçamentos apresentados × aprovados",[
 ("O que esta planilha faz","O funil da recepção: cada orçamento de exame ou pacote particular apresentado ao paciente, com valor e etapa; a previsão ponderada, o aprovado no trimestre contra a meta, a taxa de aprovação, quem retomar primeiro, os resultados por tipo e profissional e os motivos de recusa."),
 ("Passo 1","Em Config, preencha a meta de orçamentos aprovados no trimestre, o limite de \"parado\" (7 dias é um bom padrão), os tipos, motivos de recusa, profissionais e itens mais comuns. Ajuste as probabilidades por etapa se a sua experiência for diferente."),
 ("Passo 2","Em Orçamentos, uma linha por orçamento: data, paciente, profissional, tipo, itens, valor e etapa. Sempre que o paciente responder, atualize a etapa."),
 ("Passo 3","Ao decidir, mude a etapa para Aprovado, Recusado ou Sem retorno e preencha a data — que é sempre igual ou posterior à da apresentação. Se recusado, anote o motivo: é a parte mais valiosa da planilha. Aprovado vira horário na agenda (01) e, se for a prazo, parcela na 14 — e a prazo só para quem não tem parcela vencida em aberto."),
 ("Passo 4","Em Painel, veja o funil, a previsão ponderada, a lista \"Retomar contato primeiro\", a taxa de aprovação por tipo e profissional e os motivos de recusa."),
 ("Rotina","Sexta-feira, 3 minutos (rotina da semana, planilha 03): atualizar as etapas e retomar os parados. Dia 1 do mês: comparar o aprovado com a meta e olhar os motivos de recusa. O Painel da clínica (17) copia \"Em aberto\" e \"Aprovado no mês\" daqui."),
 ("Com a IA","Copie \"Motivos de recusa\" e use o prompt \"Recebíveis 05 · Por que os orçamentos não fecham\" da biblioteca; para retomar um contato, \"Agenda 04 · Mensagem de retomada de orçamento\" (sem nome do paciente). Nenhum prompt do kit escreve promessa de resultado."),
 ("Exemplo","O funil traz os orçamentos de junho a setembro de 2026: os aprovados são exames realizados ou agendados na planilha 01 (mesmo paciente e data); os abertos têm datas relativas a hoje."),
])
proteger(wb); salvar(wb,"15-orcamentos.xlsx","Orçamentos apresentados × aprovados · Kit de Gestão para Médicos")
