#!/usr/bin/env python3
"""Planilha 3 do Kit IA no Trabalho: Ganhos e Gastos. Gera 03-ganhos-e-gastos.xlsx"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter as L
from datetime import date, timedelta
import random
UVA="3B1F5E"; SOL="FFC83D"; LILAS="7A5AA8"; LAVANDA="F3EEFB"; TINTA="1F1235"; AMARELO="FFF4CC"; BRANCO="FFFFFF"
F=lambda **k: Font(name="Arial", **k); fill=lambda c: PatternFill("solid", fgColor=c)
thin=Side(style="thin", color="DCD2EC"); borda=Border(left=thin,right=thin,top=thin,bottom=thin)
MESES=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
BRL='"R$" #,##0.00;[Red]-"R$" #,##0.00'
def hdr(ws,row,vals,start=1):
    for i,v in enumerate(vals):
        c=ws.cell(row=row,column=start+i,value=v); c.font=F(bold=True,color=BRANCO,size=10); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); c.border=borda
def inp(c,fmt=None):
    c.fill=fill(AMARELO); c.protection=Protection(locked=False); c.border=borda; c.font=F(color=TINTA,size=10)
    if fmt: c.number_format=fmt
def calc(c,fmt=None,center=True):
    c.border=borda; c.font=F(color=TINTA,size=10)
    if center: c.alignment=Alignment(horizontal="center")
    if fmt: c.number_format=fmt
N=500; R0=5; RN=R0+N-1
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
cfg["A1"]="Configurações"; cfg["A1"].font=F(bold=True,size=16,color=UVA)
cfg["A2"]="Células amarelas: você preenche."; cfg["A2"].font=F(italic=True,size=10,color=LILAS)
cfg["A4"]="Nome (pessoa ou negócio)"; cfg["B4"]="Rafa Design (exemplo fictício)"
cfg["A5"]="Ano do painel"; cfg["B5"]=2026
cfg["A6"]="Mês do painel"; cfg["B6"]="Setembro"
cfg["A7"]="Número do mês"; cfg["B7"]="=MATCH(B6,$H$5:$H$16,0)"
cfg["A8"]="Saldo inicial (antes do 1º lançamento)"; cfg["B8"]=2500
cfg["A9"]="Meta de reserva (meses de despesa)"; cfg["B9"]=3
cfg["A10"]="Categoria de reserva (guardado, não gasto)"; cfg["B10"]="Reserva"
for c in ("A4","A5","A6","A7","A8","A9","A10"): cfg[c].font=F(bold=True,color=UVA)
for c in ("B4","B5","B6","B9","B10"): inp(cfg[c])
inp(cfg["B8"],BRL); calc(cfg["B7"])
cfg["D4"]="Categorias de receita"; cfg["F4"]="Categorias de despesa"; cfg["H4"]="Meses"
for c in ("D4","F4","H4"): cfg[c].font=F(bold=True,color=UVA)
rec=["Serviços","Produtos","Comissões","Outras receitas"]
des=["Moradia","Alimentação","Transporte","Ferramentas e assinaturas","Impostos e taxas","Marketing","Equipamentos","Saúde","Lazer","Educação","Reserva","Outras despesas"]
for i,v in enumerate(rec): cfg.cell(row=5+i,column=4,value=v)
for i,v in enumerate(des): cfg.cell(row=5+i,column=6,value=v)
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=8,value=m).font=F(size=10,color=TINTA)
for r in range(5,17):
    inp(cfg.cell(row=r,column=4)); inp(cfg.cell(row=r,column=6))
cfg["A19"]="Até 12 categorias de receita e 12 de despesa. Mude os nomes à vontade; os lançamentos usam estas listas."; cfg["A19"].font=F(size=10,color=LILAS)
cfg["A20"]="Preencha as categorias de cima para baixo, sem pular linha: a lista suspensa de Lançamentos para na última linha preenchida."; cfg["A20"].font=F(size=10,color=LILAS)
cfg["A21"]="A categoria de reserva (B10) sai da conta, mas não é gasto: fica fora da média de despesas e soma ao cálculo de meses de reserva."; cfg["A21"].font=F(size=10,color=LILAS)
dv=DataValidation(type="list",formula1="=Config!$H$5:$H$16"); dv.add("B6"); cfg.add_data_validation(dv)
dv_res=DataValidation(type="list",formula1="=OFFSET(Config!$F$5,0,0,MAX(1,COUNTA(Config!$F$5:$F$16)),1)",allow_blank=True,showErrorMessage=False); dv_res.add("B10"); cfg.add_data_validation(dv_res)
for c,w in zip("ABCDEFGH",(34,30,3,24,3,26,3,12)): cfg.column_dimensions[c].width=w
cfg.sheet_view.showGridLines=False
# ---------- Lançamentos ----------
lan=wb.create_sheet("Lançamentos")
lan["A1"]="Lançamentos"; lan["A1"].font=F(bold=True,size=16,color=UVA)
lan["A2"]="Uma linha por entrada ou saída. Preencha as colunas amarelas; mês e ano são calculados. Apague os exemplos e comece o seu."; lan["A2"].font=F(italic=True,size=10,color=LILAS); lan.merge_cells("A2:J2")
hdr(lan,4,["Data","Tipo","Categoria","Descrição","Valor","Forma","Pago?","Observação","Mês","Ano"])
lan.row_dimensions[4].height=26
for r in range(R0,RN+1):
    for c in range(1,9): inp(lan.cell(row=r,column=c))
    lan.cell(row=r,column=1).number_format="dd/mm/yyyy"; lan.cell(row=r,column=5).number_format=BRL
    lan.cell(row=r,column=9,value=f'=IF(A{r}="","",MONTH(A{r}))'); calc(lan.cell(row=r,column=9))
    lan.cell(row=r,column=10,value=f'=IF(A{r}="","",YEAR(A{r}))'); calc(lan.cell(row=r,column=10))
    for c in (2,3,6,7): lan.cell(row=r,column=c).alignment=Alignment(horizontal="center")
dvs=[DataValidation(type="list",formula1='"Receita,Despesa"',allow_blank=True),
     DataValidation(type="list",formula1="=Config!$D$5:$D$16",allow_blank=True,showErrorMessage=False),
     DataValidation(type="list",formula1='"Pix,Cartão,Dinheiro,Boleto,Transferência"',allow_blank=True),
     DataValidation(type="list",formula1='"Sim,Não"',allow_blank=True),
     DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True),
     DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True)]
for dv,rng in zip(dvs,[f"B{R0}:B{RN}",f"C{R0}:C{RN}",f"F{R0}:F{RN}",f"G{R0}:G{RN}",f"A{R0}:A{RN}",f"E{R0}:E{RN}"]): dv.add(rng); lan.add_data_validation(dv)
# categoria: lista combinada receita+despesa exige nomes no mesmo intervalo; usamos coluna auxiliar em Config
cfg["J4"]="Todas as categorias (automático)"; cfg["J4"].font=F(bold=True,color=UVA)
# J fica contígua (receitas preenchidas, depois despesas preenchidas), para a lista suspensa não ter vazios no meio
NR_="COUNTA($D$5:$D$16)"; ND_="COUNTA($F$5:$F$16)"
for i in range(24):
    k=i+1
    cfg.cell(row=5+i,column=10,value=f'=IF({k}<={NR_},INDEX($D$5:$D$16,{k}),IF({k}<={NR_}+{ND_},INDEX($F$5:$F$16,{k}-{NR_}),""))').font=F(size=9,color="B0A6C4")
dvs[1].formula1="=OFFSET(Config!$J$5,0,0,MAX(1,COUNTA(Config!$D$5:$D$16)+COUNTA(Config!$F$5:$F$16)),1)"
cfg.column_dimensions["J"].width=26
lan.conditional_formatting.add(f"A{R0}:J{RN}", FormulaRule(formula=[f'$B{R0}="Receita"'], font=Font(name="Arial",color="155E3C",size=10)))
lan.conditional_formatting.add(f"A{R0}:J{RN}", FormulaRule(formula=[f'AND($B{R0}="Despesa",$G{R0}="Não")'], fill=fill("FBE4E4")))
for c,w in zip(range(1,11),(12,10,24,36,14,12,8,30,6,7)): lan.column_dimensions[L(c)].width=w
lan.freeze_panes="A5"; lan.sheet_view.showGridLines=False; lan.auto_filter.ref=f"A4:J{RN}"
# exemplos: Rafa, designer autônomo, jul-set 2026
random.seed(7)
ex=[]
def add(d,t,c,desc,v,f="Pix",p="Sim",o=""): ex.append((d,t,c,desc,v,f,p,o))
for m in (7,8,9):
    y=2026
    add(date(y,m,5),"Receita","Serviços","Identidade visual · Padaria do Sol",3200 if m!=9 else 3600,"Pix")
    add(date(y,m,12),"Receita","Serviços","Posts do mês · Clínica Bem-Estar",1800,"Transferência")
    add(date(y,m,20),"Receita","Serviços","Site · Loja Verde" if m==8 else "Cardápio · Bistrô 42",2400 if m==8 else 950,"Pix")
    if m==9: add(date(y,9,26),"Receita","Produtos","Venda de template no marketplace",320,"Transferência")
    add(date(y,m,1),"Despesa","Moradia","Aluguel",1400,"Boleto")
    add(date(y,m,3),"Despesa","Moradia","Luz e internet",260,"Boleto")
    add(date(y,m,7),"Despesa","Ferramentas e assinaturas","Adobe + Google One",189,"Cartão")
    add(date(y,m,10),"Despesa","Impostos e taxas","DAS MEI",80.9,"Boleto")
    add(date(y,m,8),"Despesa","Alimentação","Mercado",620+random.randint(-60,80),"Cartão")
    add(date(y,m,15),"Despesa","Alimentação","Almoços e lanches",310+random.randint(-40,40),"Cartão")
    add(date(y,m,16),"Despesa","Transporte","Uber e ônibus",180+random.randint(-30,30),"Cartão")
    add(date(y,m,18),"Despesa","Marketing","Impulsionamento no Instagram",150,"Cartão")
    add(date(y,m,22),"Despesa","Saúde","Plano de saúde",390,"Boleto")
    add(date(y,m,25),"Despesa","Lazer","Cinema e bar",140+random.randint(-30,60),"Cartão")
    add(date(y,m,28),"Despesa","Reserva","Transferência para a reserva",500,"Transferência")
    if m==8: add(date(y,8,14),"Despesa","Equipamentos","Mesa digitalizadora",890,"Cartão")
    if m==9: add(date(y,9,30),"Despesa","Educação","Curso de motion",297,"Cartão","Não","Vence dia 30")
    if m==9: add(date(y,9,29),"Despesa","Impostos e taxas","Taxa da prefeitura",65,"Boleto","Não","")
ex.sort(key=lambda x:x[0])
for i,row in enumerate(ex):
    for c,v in enumerate(row,start=1): lan.cell(row=R0+i,column=c,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
p["A1"]='=Config!B4&" · "&Config!B6&" de "&Config!B5'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:H1")
p["A2"]="Nada para preencher aqui. Escolha o mês em Config; tudo vem de Lançamentos."; p["A2"].font=F(italic=True,size=10,color=LILAS); p.merge_cells("A2:H2")
M="Config!$B$7"; Y="Config!$B$5"
LA=f"Lançamentos!$A${R0}:$A${RN}"; LB=f"Lançamentos!$B${R0}:$B${RN}"; LC=f"Lançamentos!$C${R0}:$C${RN}"; LE=f"Lançamentos!$E${R0}:$E${RN}"; LG=f"Lançamentos!$G${R0}:$G${RN}"; LI=f"Lançamentos!$I${R0}:$I${RN}"; LJ=f"Lançamentos!$J${R0}:$J${RN}"
# Painel de CAIXA: só entra o que está marcado Pago? = Sim. Sem esse filtro,
# "Entrou no mês" e "Saldo acumulado" incluíam conta que ainda não foi paga e o
# cliente lia como dinheiro disponível. O previsto tem quadro próprio ao lado.
def somames(tipo,m=M,y=Y,pago=True):
    filtro=f',{LG},"Sim"' if pago else ""
    return f'SUMIFS({LE},{LB},"{tipo}",{LI},{m},{LJ},{y}{filtro})'
def somaate(tipo,fim,pago=True):
    filtro=f',{LG},"Sim"' if pago else ""
    return f'SUMIFS({LE},{LB},"{tipo}",{LA},"<="&{fim}{filtro})'
kp=[("Entrou no mês",f"={somames('Receita')}","DDF3E7","155E3C"),
    ("Saiu no mês",f"={somames('Despesa')}","FBE4E4","7A1F1F"),
    ("Sobrou",f"=A5-C5",SOL,UVA),
    ("Saldo em caixa",f'=Config!$B$8+{somaate("Receita","DATE("+Y+","+M+"+1,0)")}-{somaate("Despesa","DATE("+Y+","+M+"+1,0)")}',LAVANDA,UVA),
    ("A receber (não recebido)",f'=SUMIFS({LE},{LB},"Receita",{LG},"Não")',LAVANDA,LILAS),
    ("A pagar (não pago)",f'=SUMIFS({LE},{LB},"Despesa",{LG},"Não")',LAVANDA,LILAS)]
for i,(lab,fml,bg,fg) in enumerate(kp):
    col=1+i*2
    a=p.cell(row=4,column=col,value=lab); a.font=F(size=9,bold=True,color=fg); a.fill=fill(bg); a.alignment=Alignment(horizontal="center")
    b=p.cell(row=5,column=col,value=fml); b.font=F(size=16,bold=True,color=fg); b.fill=fill(bg); b.alignment=Alignment(horizontal="center"); b.number_format='"R$" #,##0'
    p.merge_cells(start_row=4,start_column=col,end_row=4,end_column=col+1); p.merge_cells(start_row=5,start_column=col,end_row=5,end_column=col+1)
    p.cell(row=4,column=col+1).fill=fill(bg); p.cell(row=5,column=col+1).fill=fill(bg)
p.row_dimensions[5].height=30
# reserva (categoria definida em Config!B10: sai da conta, mas não é gasto)
RES="Config!$B$10"
fim=f'DATE({Y},{M}+1,0)'; ini=f'DATE({Y},{M}-2,1)'
p["A7"]="Reserva"; p["A7"].font=F(bold=True,size=13,color=UVA)
p["A8"]="Média de despesas dos últimos 3 meses (sem a reserva)"
p["C8"]=f'=IFERROR((SUMIFS({LE},{LB},"Despesa",{LA},">="&{ini},{LA},"<="&{fim})-SUMIFS({LE},{LB},"Despesa",{LC},{RES},{LA},">="&{ini},{LA},"<="&{fim}))/3,0)'
p["A9"]="Guardado na reserva até o mês (acumulado)"
p["C9"]=f'=SUMIFS({LE},{LB},"Despesa",{LC},{RES},{LA},"<="&{fim})'
p["A10"]="Saldo em caixa + reserva equivalem a"; p["C10"]='=IF(C8>0,(G5+C9)/C8,0)'; p["D10"]="meses de despesa"
p["A11"]="Meta de reserva"; p["C11"]="=Config!$B$9"; p["D11"]="meses"
p["A12"]="Situação"; p["C12"]='=IF(C10>=C11,"Meta de reserva atingida",IF(C10>=C11/2,"No caminho: metade da meta","Reserva baixa: priorize guardar"))'
for r in (8,9,10,11,12): p.cell(row=r,column=1).font=F(color=TINTA,size=10); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2)
p["C8"].number_format=BRL; p["C9"].number_format=BRL; p["C10"].number_format="0.0"; p["C11"].number_format="0"
for c in ("C8","C9","C10","C11","C12"): p[c].font=F(bold=True,color=UVA,size=10)
p.merge_cells("C12:F12"); p["D10"].font=F(size=10,color=LILAS); p["D11"].font=F(size=10,color=LILAS)
p["A13"]='="O que vai para a categoria "&'+RES+'&" sai da conta (entra em Saiu no mês), mas não é gasto: fica fora da média e soma ao cálculo de meses de reserva."'
p["A13"].font=F(size=9,color=LILAS); p.merge_cells("A13:H13")
# por categoria
S=2  # deslocamento das seções abaixo (bloco da reserva ganhou 2 linhas)
p.cell(row=13+S,column=1,value="Para onde foi o dinheiro").font=F(bold=True,size=13,color=UVA)
hdr(p,14+S,["Categoria de despesa","Valor no mês","% do total","Mês anterior","Barra"]); p.merge_cells(start_row=14+S,start_column=5,end_row=14+S,end_column=8)
for i in range(12):
    r=15+S+i; src=f"Config!$F${5+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",SUMIFS({LE},{LB},"Despesa",{LC},{src},{LI},{M},{LJ},{Y}))'); calc(p.cell(row=r,column=2),BRL)
    p.cell(row=r,column=3,value=f'=IF(OR({src}="",$C$5=0),"",B{r}/$C$5)'); calc(p.cell(row=r,column=3),"0%")
    p.cell(row=r,column=4,value=f'=IF({src}="","",IF({M}=1,SUMIFS({LE},{LB},"Despesa",{LC},{src},{LI},12,{LJ},{Y}-1),SUMIFS({LE},{LB},"Despesa",{LC},{src},{LI},{M}-1,{LJ},{Y})))'); calc(p.cell(row=r,column=4),BRL)
    p.cell(row=r,column=5,value=f'=IF(C{r}="","",REPT("█",ROUND(C{r}*40,0)))'); p.cell(row=r,column=5).font=F(size=10,color=LILAS); p.cell(row=r,column=5).border=borda
    p.merge_cells(start_row=r,start_column=5,end_row=r,end_column=8)
TOT=27+S
p.cell(row=TOT,column=1,value="Total"); p.cell(row=TOT,column=2,value=f"=SUM(B{15+S}:B{26+S})"); p.cell(row=TOT,column=4,value=f"=SUM(D{15+S}:D{26+S})")
for c in (1,2,4): p.cell(row=TOT,column=c).font=F(bold=True,color=UVA,size=10); p.cell(row=TOT,column=c).border=borda
p.cell(row=TOT,column=2).number_format=BRL; p.cell(row=TOT,column=4).number_format=BRL
p.cell(row=29+S,column=1,value="De onde veio o dinheiro").font=F(bold=True,size=13,color=UVA)
hdr(p,30+S,["Categoria de receita","Valor no mês","% do total","Mês anterior"])
for i in range(12):
    r=31+S+i; src=f"Config!$D${5+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",SUMIFS({LE},{LB},"Receita",{LC},{src},{LI},{M},{LJ},{Y}))'); calc(p.cell(row=r,column=2),BRL)
    p.cell(row=r,column=3,value=f'=IF(OR({src}="",$A$5=0),"",B{r}/$A$5)'); calc(p.cell(row=r,column=3),"0%")
    p.cell(row=r,column=4,value=f'=IF({src}="","",IF({M}=1,SUMIFS({LE},{LB},"Receita",{LC},{src},{LI},12,{LJ},{Y}-1),SUMIFS({LE},{LB},"Receita",{LC},{src},{LI},{M}-1,{LJ},{Y})))'); calc(p.cell(row=r,column=4),BRL)
# ano
A0=44+S
p.cell(row=A0,column=1,value="O ano, mês a mês").font=F(bold=True,size=13,color=UVA)
hdr(p,A0+1,["Mês","Entrou","Saiu","Sobrou","Saldo ao fim do mês"])
for i in range(12):
    r=A0+2+i
    p.cell(row=r,column=1,value=MESES[i]); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'={somames("Receita",i+1)}'); calc(p.cell(row=r,column=2),BRL)
    p.cell(row=r,column=3,value=f'={somames("Despesa",i+1)}'); calc(p.cell(row=r,column=3),BRL)
    p.cell(row=r,column=4,value=f'=B{r}-C{r}'); calc(p.cell(row=r,column=4),BRL)
    p.cell(row=r,column=5,value=f'=Config!$B$8+{somaate("Receita",f"DATE({Y},{i+2},0)")}-{somaate("Despesa",f"DATE({Y},{i+2},0)")}'); calc(p.cell(row=r,column=5),BRL)
p.conditional_formatting.add(f"D{A0+2}:D{A0+13}", FormulaRule(formula=[f'D{A0+2}<0'], font=Font(name="Arial",color="C8402E",size=10,bold=True)))
bc=BarChart(); bc.type="col"; bc.grouping="clustered"; bc.height=7.5; bc.width=18; bc.title=None; bc.style=2
bc.add_data(Reference(p,min_col=2,max_col=3,min_row=A0+1,max_row=A0+13),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=A0+2,max_row=A0+13))
bc.series[0].graphicalProperties.solidFill="7A5AA8"; bc.series[1].graphicalProperties.solidFill="3B1F5E"; bc.legend.position="b"; bc.y_axis.majorGridlines=None
p.add_chart(bc,f"G{A0}")
p.cell(row=A0+14,column=1,value="Meses sem lançamento aparecem zerados. Compare só os meses já fechados.").font=F(size=9,color=LILAS)
for c,w in zip(range(1,11),(30,16,12,16,12,12,12,12,4,4)): p.column_dimensions[L(c)].width=w
p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Como usar ----------
u=wb.create_sheet("Como usar",0)
u["A1"]="Ganhos e Gastos"; u["A1"].font=F(bold=True,size=20,color=UVA)
u["A2"]="Kit IA no Trabalho · Seu Sócio Gestor · versão 1.0 (setembro de 2026)"; u["A2"].font=F(size=10,color=LILAS)
linhas=[
("O que esta planilha faz","Você lança o que entra e o que sai; ela mostra quanto sobrou no mês, para onde o dinheiro foi, quanto falta pagar, o saldo acumulado e quantos meses de reserva você tem. Serve para pessoa, autônomo ou negócio pequeno."),
("Passo 1","Em Config, preencha o nome, o ano, o saldo que você tinha antes do primeiro lançamento, a meta de reserva (3 meses é um bom começo) e qual categoria é a sua reserva. Ajuste as categorias se quiser, de cima para baixo, sem pular linha."),
("Passo 2","Em Lançamentos, uma linha por entrada ou saída: data, tipo, categoria, descrição, valor, forma e se já foi pago. Apague os exemplos e comece o seu."),
("Passo 3","Em Painel, escolha o mês em Config e veja: entrou, saiu, sobrou, saldo, a pagar, reserva e as categorias com barra. O que você guarda na categoria de reserva sai da conta, mas não conta como gasto: fica fora da média de despesas e soma aos meses de reserva."),
("Rotina","Lance na hora ou uma vez por semana (10 minutos). No fim do mês, olhe o Painel antes de decidir qualquer gasto grande."),
("Com a IA","Copie a tabela \"Para onde foi o dinheiro\" e use o prompt \"Analisar 03: onde cortar\" da biblioteca do kit. Para explicar o mês a um cliente ou sócio, use \"Escrever 05\"."),
("Legenda","Células amarelas: você preenche. Brancas: calculadas. Linhas em verde: receitas. Linhas em vermelho claro: despesas ainda não pagas."),
("Proteção","Fórmulas protegidas sem senha. Para editar: Revisar > Desproteger planilha (Excel) ou Dados > Proteger intervalos (Google Sheets)."),
("Google Sheets","Faça upload no Google Drive e abra com o Google Sheets. Fórmulas, listas, cores e gráfico funcionam."),
("Exemplos","Rafa Design é uma pessoa fictícia. Os valores são inventados. Apague-os antes de começar."),
("Suporte","suporte@seusociogestor.com.br · resposta em até 5 dias úteis · reembolso em até 7 dias pelo mesmo canal."),
]
for i,(a,b) in enumerate(linhas,start=4):
    u.cell(row=i,column=1,value=a).font=F(bold=True,color=UVA); u.cell(row=i,column=2,value=b).font=F(color=TINTA)
    u.cell(row=i,column=2).alignment=Alignment(wrap_text=True,vertical="top"); u.cell(row=i,column=1).alignment=Alignment(vertical="top"); u.row_dimensions[i].height=46
u.column_dimensions["A"].width=20; u.column_dimensions["B"].width=95; u.sheet_view.showGridLines=False
for ws in (cfg,lan,p,u):
    ws.protection.sheet=True; ws.protection.formatColumns=False; ws.protection.formatRows=False; ws.protection.selectLockedCells=False; ws.protection.sort=False; ws.protection.autoFilter=False
wb.properties.creator="Seu Sócio Gestor"; wb.properties.title="Ganhos e Gastos · Kit IA no Trabalho"
wb.save("03-ganhos-e-gastos.xlsx"); print("salvo")
