#!/usr/bin/env python3
"""Planilha 2 do Kit IA no Trabalho: Relatório Mensal Pronto. Gera 02-relatorio-mensal-pronto.xlsx"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule, Rule
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.styles.numbers import NumberFormat
from openpyxl.chart import LineChart, BarChart, Reference
from openpyxl.utils import get_column_letter as L

UVA="3B1F5E"; SOL="FFC83D"; LILAS="7A5AA8"; LAVANDA="F3EEFB"; TINTA="1F1235"; AMARELO="FFF4CC"; BRANCO="FFFFFF"
F=lambda **k: Font(name="Arial", **k); fill=lambda c: PatternFill("solid", fgColor=c)
thin=Side(style="thin", color="DCD2EC"); borda=Border(left=thin,right=thin,top=thin,bottom=thin)
MESES=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
NI=12; R0=5; RN=R0+NI-1   # indicadores nas linhas 5..16
def hdr(ws,row,cols,vals,widths=None):
    for i,(c,v) in enumerate(zip(cols,vals)):
        cell=ws.cell(row=row,column=c,value=v); cell.font=F(bold=True,color=BRANCO,size=10); cell.fill=fill(UVA); cell.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); cell.border=borda
def inp(cell,fmt=None):
    cell.fill=fill(AMARELO); cell.protection=Protection(locked=False); cell.border=borda; cell.font=F(color=TINTA,size=10)
    if fmt: cell.number_format=fmt
def calc(cell,fmt=None,center=True):
    cell.border=borda; cell.font=F(color=TINTA,size=10)
    if center: cell.alignment=Alignment(horizontal="center")
    if fmt: cell.number_format=fmt

wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
cfg["A1"]="Configurações"; cfg["A1"].font=F(bold=True,size=16,color=UVA)
cfg["A2"]="Células amarelas: você preenche."; cfg["A2"].font=F(italic=True,size=10,color=LILAS)
cfg["A4"]="Nome da empresa ou área"; cfg["B4"]="Prisma Comunicação (exemplo fictício)"
cfg["A5"]="Ano"; cfg["B5"]=2026
cfg["A6"]="Mês do relatório"; cfg["B6"]="Setembro"
cfg["A7"]="Número do mês"; cfg["B7"]="=MATCH(B6,Config!$D$5:$D$16,0)"
cfg["A8"]="Mês anterior"; cfg["B8"]='=IF(B7>1,INDEX($D$5:$D$16,B7-1),"")'
cfg["D4"]="Meses"; cfg["D4"].font=F(bold=True,color=UVA)
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=4,value=m).font=F(size=10,color=TINTA)
for c in ("A4","A5","A6","A7","A8"): cfg[c].font=F(bold=True,color=UVA)
for c in ("B4","B5","B6"): inp(cfg[c])
for c in ("B7","B8"): calc(cfg[c],center=False)
dv_mes=DataValidation(type="list",formula1="=Config!$D$5:$D$16",allow_blank=False,showErrorMessage=True); dv_mes.add("B6"); cfg.add_data_validation(dv_mes)
cfg["A10"]="Use a mesma planilha o ano inteiro: só troque o mês do relatório."; cfg["A10"].font=F(size=10,color=LILAS)
cfg.column_dimensions["A"].width=26; cfg.column_dimensions["B"].width=40; cfg.column_dimensions["D"].width=14; cfg.sheet_view.showGridLines=False

# ---------- Indicadores ----------
ind=wb.create_sheet("Indicadores")
ind["A1"]="Indicadores do ano"; ind["A1"].font=F(bold=True,size=16,color=UVA)
ind["A2"]="Preencha o nome, a unidade, a meta mensal, se maior é melhor, e o valor de cada mês. Deixe em branco o que ainda não aconteceu."; ind["A2"].font=F(italic=True,size=10,color=LILAS); ind.merge_cells("A2:R2")
cols=["Indicador","Unidade","Casas decimais","Meta mensal","Maior é melhor?"]+[m[:3] for m in MESES]+["Acumulado","Média","Como acumular"]
hdr(ind,4,range(1,len(cols)+1),cols)
ind.row_dimensions[4].height=30
# ACUM: como o Acumulado trata o indicador. "Média" para razão (ticket médio, custo por
# lead, taxa, nota); "Soma" para estoque e fluxo (receita, despesa, quantidade, horas).
ACUM={"Taxa de conversão de leads":"Média","Ticket médio":"Média","Inadimplência":"Média",
      "NPS":"Média","Custo por lead":"Média"}
ex=[("Receita","R$",0,120000,"Sim",[98500,101200,112400,109800,118300,121900,115700,124600,131200]),
    ("Despesas","R$",0,85000,"Não",[80200,81900,84100,86500,83700,88200,84900,87300,89800]),
    ("Resultado (receita - despesas)","R$",0,35000,"Sim",[18300,19300,28300,23300,34600,33700,30800,37300,41400]),
    ("Novos clientes","un",0,6,"Sim",[3,4,5,4,6,5,4,7,6]),
    ("Leads recebidos","un",0,120,"Sim",[88,95,110,102,131,118,109,142,137]),
    ("Taxa de conversão de leads","%",1,5,"Sim",[3.4,4.2,4.5,3.9,4.6,4.2,3.7,4.9,4.4]),
    ("Ticket médio","R$",0,9000,"Sim",[8200,8400,8900,8700,9100,9300,9000,9400,9700]),
    ("Inadimplência","%",1,3,"Não",[4.1,3.8,3.2,3.5,2.9,3.1,3.4,2.6,2.4]),
    ("Atendimentos realizados","un",0,60,"Sim",[52,55,61,58,64,60,57,66,63]),
    ("NPS","pts",0,70,"Sim",[64,66,69,67,71,70,68,73,72]),
    ("Horas extras da equipe","h",0,20,"Não",[26,24,18,22,15,19,23,14,12]),
    ("Custo por lead","R$",2,45,"Não",[52.3,49.8,44.1,47.5,41.2,43.9,46.8,39.5,40.7])]
for i in range(NI):
    r=R0+i
    for c in range(1,6): inp(ind.cell(row=r,column=c))
    for c in range(6,18): inp(ind.cell(row=r,column=c),"#,##0.00")
    ind.cell(row=r,column=1).alignment=Alignment(horizontal="left")
    ind.cell(row=r,column=18,value=f'=IF(COUNT(F{r}:Q{r})=0,"",IF(T{r}="Média",AVERAGE(F{r}:Q{r}),SUM(F{r}:Q{r})))'); calc(ind.cell(row=r,column=18),"#,##0.00")
    ind.cell(row=r,column=19,value=f'=IF(COUNT(F{r}:Q{r})=0,"",AVERAGE(F{r}:Q{r}))'); calc(ind.cell(row=r,column=19),"#,##0.00")
    inp(ind.cell(row=r,column=20))      # Como acumular: Soma ou Média
    if i<len(ex):
        nome,un,casas,meta,mb,vals=ex[i]
        ind.cell(row=r,column=1,value=nome); ind.cell(row=r,column=2,value=un); ind.cell(row=r,column=3,value=casas); ind.cell(row=r,column=4,value=meta); ind.cell(row=r,column=5,value=mb)
        ind.cell(row=r,column=20,value=ACUM.get(nome,"Soma"))
        for j,v in enumerate(vals): ind.cell(row=r,column=6+j,value=v)
dv_sn=DataValidation(type="list",formula1='"Sim,Não"',allow_blank=True,showErrorMessage=True); dv_sn.add(f"E{R0}:E{RN}"); ind.add_data_validation(dv_sn)
dv_cd=DataValidation(type="list",formula1='"0,1,2"',allow_blank=True,showErrorMessage=True); dv_cd.add(f"C{R0}:C{RN}"); ind.add_data_validation(dv_cd)
dv_un=DataValidation(type="list",formula1='"R$,%,un,h,pts"',allow_blank=True,showErrorMessage=True); dv_un.add(f"B{R0}:B{RN}"); ind.add_data_validation(dv_un)
dv_ac=DataValidation(type="list",formula1='"Soma,Média"',allow_blank=False,showErrorMessage=True,
                    errorTitle="Como acumular",error="Escolha Soma (empilha) ou Média (razão).")
dv_ac.add(f"T{R0}:T{RN}"); ind.add_data_validation(dv_ac)
ind.cell(row=RN+2,column=1,value='"Como acumular" decide o que o Acumulado mostra: Soma para o que se empilha (receita, despesa, quantidade, horas) e Média para razão (ticket médio, custo por lead, taxa, nota). Somar razão não significa nada: doze meses de ticket médio somados não são o ticket do ano. "Média" é sempre a média dos meses preenchidos. Para indicadores em %, digite 4,5 (não 0,045).').font=F(size=10,color=LILAS)
ind.merge_cells(start_row=RN+2,start_column=1,end_row=RN+2,end_column=20)
for c,w in zip(range(1,20),[30,8,9,12,10]+[10]*12+[16,10]): ind.column_dimensions[L(c)].width=w
ind.freeze_panes="B5"; ind.sheet_view.showGridLines=False

# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
p["A1"]='=Config!B4&" · Relatório de "&Config!B6&" de "&Config!B5'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:I1")
p["A2"]="Nada para digitar aqui, exceto o indicador do gráfico em B18. Escolha o mês em Config; os números vêm de Indicadores."; p["A2"].font=F(italic=True,size=10,color=LILAS); p.merge_cells("A2:I2")
hdr(p,4,range(1,10),["Indicador","Mês","Mês anterior","Variação","Meta","Vs. meta","Situação","Acumulado (soma; média p/ % e pts)","Unidade"])
p.row_dimensions[4].height=28
m="Config!$B$7"
for i in range(NI):
    r=R0+i; s=R0+i  # mesma linha em Indicadores
    p.cell(row=r,column=1,value=f'=IF(Indicadores!A{s}="","",Indicadores!A{s})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF(Indicadores!A{s}="","",IF(INDEX(Indicadores!$F{s}:$Q{s},{m})="","",INDEX(Indicadores!$F{s}:$Q{s},{m})))'); calc(p.cell(row=r,column=2),"#,##0.00")
    p.cell(row=r,column=3,value=f'=IF(OR(Indicadores!A{s}="",{m}=1),"",IF(INDEX(Indicadores!$F{s}:$Q{s},{m}-1)="","",INDEX(Indicadores!$F{s}:$Q{s},{m}-1)))'); calc(p.cell(row=r,column=3),"#,##0.00")
    p.cell(row=r,column=4,value=f'=IF(OR(B{r}="",C{r}="",C{r}=0),"",(B{r}-C{r})/ABS(C{r}))'); calc(p.cell(row=r,column=4),"+0.0%;-0.0%;0.0%")
    p.cell(row=r,column=5,value=f'=IF(OR(Indicadores!A{s}="",Indicadores!D{s}=""),"",Indicadores!D{s})'); calc(p.cell(row=r,column=5),"#,##0.00")
    p.cell(row=r,column=6,value=f'=IF(OR(B{r}="",E{r}="",E{r}=0),"",(B{r}-E{r})/ABS(E{r}))'); calc(p.cell(row=r,column=6),"+0.0%;-0.0%;0.0%")
    p.cell(row=r,column=7,value=f'=IF(OR(B{r}="",E{r}=""),"",IF(Indicadores!E{s}="Não",IF(B{r}<=E{r},"No alvo","Acima da meta"),IF(B{r}>=E{r},"No alvo","Abaixo da meta")))'); calc(p.cell(row=r,column=7))
    p.cell(row=r,column=8,value=f'=IF(Indicadores!A{s}="","",Indicadores!R{s})'); calc(p.cell(row=r,column=8),"#,##0.00")
    p.cell(row=r,column=9,value=f'=IF(Indicadores!A{s}="","",Indicadores!B{s})'); calc(p.cell(row=r,column=9))
    # N: casas decimais (para o formato condicional). O: quanto o indicador está fora da meta, só se fora do alvo,
    # sempre positivo (sinal invertido quando "Maior é melhor?" = Não).
    p.cell(row=r,column=14,value=f'=IF(Indicadores!C{s}="",2,Indicadores!C{s})'); p.cell(row=r,column=14).font=F(size=9,color="B0A6C4")
    p.cell(row=r,column=15,value=f'=IF(OR(F{r}="",G{r}="",G{r}="No alvo"),"",IF(Indicadores!E{s}="Não",F{r},-F{r}))'); p.cell(row=r,column=15).font=F(size=9,color="B0A6C4")
rng=f"A{R0}:I{RN}"
p.conditional_formatting.add(rng, FormulaRule(formula=[f'OR($G{R0}="Abaixo da meta",$G{R0}="Acima da meta")'], fill=fill("FBE4E4"), font=Font(name="Arial",color="7A1F1F",size=10)))
p.conditional_formatting.add(rng, FormulaRule(formula=[f'$G{R0}="No alvo"'], fill=fill("DDF3E7")))
# casas decimais de Indicadores!C aplicadas a Mês, Mês anterior, Meta e Acumulado (formato base: 2 casas)
for cols_,fmt,fid,casas in ((f"B{R0}:C{RN} E{R0}:E{RN} H{R0}:H{RN}","#,##0",3,0),(f"B{R0}:C{RN} E{R0}:E{RN} H{R0}:H{RN}","#,##0.0",201,1)):
    p.conditional_formatting.add(cols_, Rule(type="expression",formula=[f'$N{R0}={casas}'],dxf=DifferentialStyle(numFmt=NumberFormat(numFmtId=fid,formatCode=fmt))))
# helper para gráfico de linha: indicador escolhido
p.cell(row=RN+2,column=1,value="Indicador do gráfico").font=F(bold=True,color=UVA)
# valor literal, não fórmula: célula amarela é para digitar, e fórmula em célula de
# entrada é apagada na primeira digitação
p.cell(row=RN+2,column=2,value=ex[0][0]); inp(p.cell(row=RN+2,column=2)); p.merge_cells(start_row=RN+2,start_column=2,end_row=RN+2,end_column=4)
dv_ind=DataValidation(type="list",formula1=f"=OFFSET(Indicadores!$A${R0},0,0,MAX(1,COUNTA(Indicadores!$A${R0}:$A${RN})),1)",allow_blank=False,showErrorMessage=True); dv_ind.add(f"B{RN+2}"); p.add_data_validation(dv_ind)
HR=RN+22  # linhas auxiliares do gráfico ficam abaixo dele (gráficos ignoram linhas ocultas)
p.cell(row=HR,column=1,value="Mês").font=F(size=9,color=BRANCO)
p.cell(row=HR+1,column=1,value="Valor").font=F(size=9,color=BRANCO)
p.cell(row=HR+2,column=1,value="Meta").font=F(size=9,color=BRANCO)
for j in range(12):
    c=2+j
    p.cell(row=HR,column=c,value=MESES[j][:3]).font=F(size=9,color=BRANCO)
    idx=f'MATCH($B${RN+2},Indicadores!$A${R0}:$A${RN},0)'
    p.cell(row=HR+1,column=c,value=f'=IFERROR(IF(INDEX(Indicadores!$F${R0}:$Q${RN},{idx},{j+1})="",NA(),INDEX(Indicadores!$F${R0}:$Q${RN},{idx},{j+1})),NA())').font=F(size=9,color=BRANCO)
    p.cell(row=HR+2,column=c,value=f'=IFERROR(INDEX(Indicadores!$D${R0}:$D${RN},{idx}),NA())').font=F(size=9,color=BRANCO)
lc=LineChart(); lc.title=None; lc.height=7.5; lc.width=18; lc.style=2
lc.add_data(Reference(p,min_col=1,max_col=13,min_row=HR+1,max_row=HR+2),from_rows=True,titles_from_data=True)
lc.set_categories(Reference(p,min_col=2,max_col=13,min_row=HR))
lc.series[0].graphicalProperties.line.solidFill=UVA; lc.series[0].graphicalProperties.line.width=28000
lc.series[1].graphicalProperties.line.solidFill=SOL; lc.series[1].graphicalProperties.line.dashStyle="dash"
lc.y_axis.majorGridlines=None; lc.legend.position="b"; lc.dispBlanksAs="gap"
for sr in lc.series: sr.smooth=False
p.add_chart(lc,f"A{RN+5}")
p.column_dimensions["N"].hidden=True; p.column_dimensions["O"].hidden=True  # fora de B:M, para o gráfico não pular mês oculto
p.cell(row=HR-1,column=1,value=f"Dados do gráfico ficam nas linhas {HR} a {HR+2}, em fonte branca, de propósito: meses sem valor dão #N/D para o gráfico deixar a lacuna em vez de cair a zero.").font=F(size=9,color="B0A6C4")
p.cell(row=RN+4,column=1,value="Evolução no ano do indicador escolhido (linha cheia) e sua meta (tracejada).").font=F(size=9,color=LILAS)
for c,w in zip(range(1,14),[30,12,12,10,12,10,15,16,9,9,9,9,9]): p.column_dimensions[L(c)].width=w
p.freeze_panes="A5"; p.sheet_view.showGridLines=False

# ---------- Resumo ----------
rs=wb.create_sheet("Resumo",1)
rs["A1"]="Resumo do mês, pronto para a IA"; rs["A1"].font=F(bold=True,size=16,color=UVA)
rs["A2"]="Copie o bloco abaixo e cole no prompt \"Escrever 01: relatório executivo\" ou \"Apresentar 01: roteiro de 8 slides\" da biblioteca do kit."; rs["A2"].font=F(italic=True,size=10,color=LILAS); rs.merge_cells("A2:D2")
rs["A4"]='="Relatório de "&Config!B6&" de "&Config!B5&" · "&Config!B4'; rs["A4"].font=F(bold=True,color=UVA); rs.merge_cells("A4:D4")
def frase(i):
    r=R0+i; s=R0+i
    v=f"Painel!B{r}"; a=f"Painel!C{r}"; var=f"Painel!D{r}"; meta=f"Painel!E{r}"; st=f"Painel!G{r}"; un=f"Indicadores!B{s}"; cd=f"Indicadores!C{s}"; nome=f"Indicadores!A{s}"
    num=lambda x: f'IF({un}="R$","R$ ","")&FIXED({x},IF({cd}="",0,{cd}))&IF(OR({un}="R$",{un}=""),""," "&{un})'
    return (f'=IF(OR({nome}="",{v}=""),"",'
            f'"• "&{nome}&": "&{num(v)}'
            # Três casos, como nas planilhas 20 dos outros kits: mês anterior vazio (não
            # comenta), mês anterior ZERO (diz que não há base) e variação calculável.
            # Antes, com C=0 a condição a<>"" era verdadeira e a frase tentava
            # FIXED(""*100,0) — achado da auditoria de 18/09.
            f'&IF({a}="","",IF(AND({a}=0,{v}<>0)," (sem base de comparação: "&Config!$B$8&" foi zero)",'
            f'IF({var}="","",IF({var}>=0," (+"," (")&FIXED({var}*100,0)&"% em relação a "&Config!$B$8&")")))'
            f'&IF({meta}<>"","; meta "&{num(meta)}&", "&LOWER({st}),"")&".")')
for i in range(NI):
    rs.cell(row=6+i,column=1,value=frase(i)).font=F(size=10,color=TINTA); rs.merge_cells(start_row=6+i,start_column=1,end_row=6+i,end_column=4)
    rs.cell(row=6+i,column=1).alignment=Alignment(wrap_text=True,vertical="top")
D0=6+NI+1
rs.cell(row=D0,column=1,value="Destaques automáticos").font=F(bold=True,color=UVA)
VR=f"Painel!$D${R0}:$D${RN}"; NR=f"Painel!$A${R0}:$A${RN}"; MR=f"Painel!$F${R0}:$F${RN}"
rs.cell(row=D0+1,column=1,value=f'=IFERROR("• Maior alta contra o mês anterior: "&INDEX({NR},MATCH(MAX({VR}),{VR},0))&" ("&IF(MAX({VR})>=0,"+","")&FIXED(MAX({VR})*100,0)&"%).","• Maior alta: preencha ao menos dois meses.")')
rs.cell(row=D0+2,column=1,value=f'=IFERROR("• Maior queda contra o mês anterior: "&INDEX({NR},MATCH(MIN({VR}),{VR},0))&" ("&FIXED(MIN({VR})*100,0)&"%).","")')
AR=f"Painel!$O${R0}:$O${RN}"; SR=f"Painel!$G${R0}:$G${RN}"
_fora=f'(COUNTIF({SR},"Acima da meta")+COUNTIF({SR},"Abaixo da meta"))'
rs.cell(row=D0+3,column=1,value=f'=IF({_fora}=0,"• Nenhum indicador fora da meta.",'
    f'IF(COUNT({AR})=0,"• "&{_fora}&" indicador(es) fora da meta (sem percentual: a meta é zero).",'
    f'IFERROR("• Mais longe da meta: "&INDEX({NR},MATCH(MAX({AR}),{AR},0))&" ("&IF(INDEX({MR},MATCH(MAX({AR}),{AR},0))>=0,"+","")&FIXED(INDEX({MR},MATCH(MAX({AR}),{AR},0))*100,0)&"% da meta, "&LOWER(INDEX({SR},MATCH(MAX({AR}),{AR},0)))&").","")))')
rs.cell(row=D0+4,column=1,value=f'=IFERROR("• Indicadores no alvo: "&COUNTIF(Painel!$G${R0}:$G${RN},"No alvo")&" de "&COUNTIF(Painel!$G${R0}:$G${RN},"<>")&".","")')
for k in range(1,5):
    rs.cell(row=D0+k,column=1).font=F(size=10,color=TINTA); rs.merge_cells(start_row=D0+k,start_column=1,end_row=D0+k,end_column=4); rs.cell(row=D0+k,column=1).alignment=Alignment(wrap_text=True,vertical="top")
T0=D0+6
rs.cell(row=T0,column=1,value="Bloco único para copiar").font=F(bold=True,color=UVA)
partes=" & ".join([f'IF(A{6+i}="","",A{6+i}&CHAR(10))' for i in range(NI)])
rs.cell(row=T0+1,column=1,value=f'=A4&CHAR(10)&{partes}&CHAR(10)&A{D0+1}&CHAR(10)&A{D0+2}&CHAR(10)&A{D0+3}&CHAR(10)&A{D0+4}')
rs.merge_cells(start_row=T0+1,start_column=1,end_row=T0+1,end_column=4); rs.cell(row=T0+1,column=1).alignment=Alignment(wrap_text=True,vertical="top"); rs.cell(row=T0+1,column=1).font=F(size=10,color=TINTA); rs.cell(row=T0+1,column=1).fill=fill(LAVANDA)
rs.row_dimensions[T0+1].height=300
rs.cell(row=T0+3,column=1,value="Os textos são gerados por fórmula. Revise antes de enviar; a IA precisa dos seus comentários sobre o porquê dos números.").font=F(size=9,color=LILAS)
rs.merge_cells(start_row=T0+3,start_column=1,end_row=T0+3,end_column=4)
for c,w in zip("ABCD",(40,30,30,30)): rs.column_dimensions[c].width=w
rs.sheet_view.showGridLines=False

# ---------- Como usar ----------
u=wb.create_sheet("Como usar",0)
u["A1"]="Relatório Mensal Pronto"; u["A1"].font=F(bold=True,size=20,color=UVA)
u["A2"]="Kit IA no Trabalho · Seu Sócio Gestor · versão 1.0 (setembro de 2026)"; u["A2"].font=F(size=10,color=LILAS)
linhas=[
("O que esta planilha faz","Você digita até 12 indicadores por mês; ela calcula variação contra o mês anterior, comparação com a meta, acumulado, média, monta o painel e escreve as frases-base do relatório para você colar na IA."),
("Como acumular","Cada indicador tem a sua regra, escolhida na última coluna da aba Indicadores: \"Soma\" para o que se empilha (receita, despesa, quantidade, horas) e \"Média\" para razão (ticket médio, custo por lead, taxa de conversão, inadimplência, NPS) — inclusive quando a razão está em reais. Somar razão não significa nada: doze meses de ticket médio somados não são o ticket do ano. A Média usa só os meses preenchidos; um mês com zero digitado ENTRA na conta, um mês em branco não."),
("Passo 1","Em Config, preencha o nome da empresa ou área, o ano e escolha o mês do relatório."),
("Passo 2","Em Indicadores, troque os exemplos pelos seus (de cima para baixo, sem pular linha): nome, unidade (R$, %, un, h, pts), casas decimais, meta mensal e se maior é melhor. Depois, o valor de cada mês. Em %, digite 4,5 e não 0,045."),
("Passo 3","Abra Painel: cada indicador com mês, mês anterior, variação, meta e situação (verde no alvo, vermelho fora). Escolha um indicador para o gráfico de evolução."),
("Passo 4","Abra Resumo: as frases do mês já estão escritas. Copie o bloco único e cole no prompt \"Escrever 01\" (relatório executivo) ou \"Apresentar 01\" (roteiro de 8 slides) da biblioteca do kit, junto com os seus comentários sobre o porquê dos números."),
("Todo mês","Digite os valores do novo mês em Indicadores e troque o mês em Config. O resto se refaz sozinho."),
("Legenda","Células amarelas: você preenche. Células brancas: calculadas. Verde: no alvo. Vermelho: fora da meta."),
("Proteção","Fórmulas protegidas sem senha. Para editar: Revisar > Desproteger planilha (Excel) ou Dados > Proteger intervalos (Google Sheets)."),
("Google Sheets","Faça upload no Google Drive e abra com o Google Sheets. Fórmulas, listas, cores e gráfico funcionam."),
("Exemplos","A Prisma Comunicação é uma empresa fictícia. Os números são inventados. Apague-os antes de começar. A planilha Ganhos e Gastos do kit usa outro exemplo, de uma autônoma, porque ela serve também para o dinheiro pessoal — não é descuido, é o uso previsto."),
("Suporte","suporte@seusociogestor.com.br · resposta em até 5 dias úteis · reembolso em até 7 dias pelo mesmo canal."),
]
for i,(a,b) in enumerate(linhas,start=4):
    u.cell(row=i,column=1,value=a).font=F(bold=True,color=UVA); u.cell(row=i,column=2,value=b).font=F(color=TINTA)
    u.cell(row=i,column=2).alignment=Alignment(wrap_text=True,vertical="top"); u.cell(row=i,column=1).alignment=Alignment(vertical="top"); u.row_dimensions[i].height=46
u.column_dimensions["A"].width=20; u.column_dimensions["B"].width=95; u.sheet_view.showGridLines=False

for ws in (cfg,ind,p,rs,u):
    ws.protection.sheet=True; ws.protection.formatColumns=False; ws.protection.formatRows=False; ws.protection.selectLockedCells=False
wb.properties.creator="Seu Sócio Gestor"; wb.properties.title="Relatório Mensal Pronto · Kit IA no Trabalho"
wb.save("02-relatorio-mensal-pronto.xlsx"); print("salvo")
