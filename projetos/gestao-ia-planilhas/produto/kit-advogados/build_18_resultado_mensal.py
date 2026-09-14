#!/usr/bin/env python3
"""Planilha 18 do Kit de Gestão para Advogados: Resultado Mensal (DRE simplificada do escritório). Gera 18-resultado-mensal.xlsx
Receita por modalidade de honorário, custos fixos (linhas de dados.CUSTOS_FIXOS), pró-labore, impostos provisionados
como % da receita, resultado e margem, mês a mês. Compara com o mês anterior e com o previsto.
Os totais mensais do exemplo (receita, saídas) são os mesmos das planilhas 17 e 20."""
from ssg import *
import dados
from openpyxl.chart import BarChart, Reference

# ---------- exemplo compartilhado (jan..set/2026; mesmos números em build_17 e build_20) ----------
RECEITA=[33660,14000,19560,20900,19200,25970,30170,26660,29400]   # jan–ago = lançamentos da 09; set = mês fechado (estimado)
CONSULTIVO=[3000,3000,4500,4500,4500,4500,4500,6000,7200]      # recorrente (objetivo 1 da planilha 19)
IMPOSTO=0.06
def modalidades(i):
    """Receita do mês dividida em fixo, hora, êxito e consultivo mensal (soma fecha em RECEITA[i])."""
    resto=RECEITA[i]-CONSULTIVO[i]
    hora=int(resto*0.27/100)*100; exito=int(resto*0.30/100)*100; fixo=resto-hora-exito
    return [fixo,hora,exito,CONSULTIVO[i]]
MODAL=["Honorários fixos (por caso)","Honorários por hora","Honorários de êxito","Consultivo mensal (recorrente)"]
SOCIOS=[(n,c) for n,p,c,h in dados.PESSOAS if p.startswith("Sóci")]  # Marina 6.000, Rafael 6.000
def custos_mes(i): return [v for n,v in dados.CUSTOS_FIXOS]   # mesmas linhas e valores da 05 e da 09 (6.500/mês)
SAIDAS=[sum(custos_mes(i))+sum(c for _,c in SOCIOS)+round(RECEITA[i]*IMPOSTO) for i in range(9)]
assert SAIDAS[-1]==20264 and SAIDAS[-2]==20100, SAIDAS  # iguais à planilha 17
PREV_RECEITA=[24000,24000,24000,24000,25000,25000,26000,26000,27000,27000,28000,28000]

wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche.",merge_to="E")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Ano"; cfg["B5"]=2026
cfg["A6"]="Mês de análise"; cfg["B6"]="Setembro"
cfg["A7"]="Impostos provisionados (% da receita)"; cfg["B7"]=IMPOSTO
cfg["A8"]="Número do mês"; cfg["B8"]="=MATCH(B6,$D$5:$D$16,0)"
cfg["A9"]="Mês anterior"; cfg["B9"]='=IF(B8>1,INDEX($D$5:$D$16,B8-1),"")'
for r in range(4,10): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"]); inp(cfg["B6"]); inp(cfg["B7"],"0.0%"); calc(cfg["B8"]); calc(cfg["B9"])
cfg["C7"]="Use a alíquota efetiva que o contador informar (Simples, ISS + IR ou lucro presumido). A provisão sai todo mês, mesmo que o imposto seja pago depois."; nota(cfg["C7"])
cfg["D4"]="Meses"; rotulo(cfg["D4"])
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=4,value=m).font=F(size=10,color=TINTA)
dv=lista("=Config!$D$5:$D$16",allow_blank=False); dv.add("B6"); cfg.add_data_validation(dv)
widths(cfg,(36,18,4,14)); cfg.sheet_view.showGridLines=False

# ---------- Resultado (DRE) ----------
rs=wb.create_sheet("Resultado")
titulo(rs,"Resultado mensal do escritório","Preencha as linhas amarelas de cada mês com os totais do caixa (planilha 09). Totais, impostos provisionados, resultado e margem são calculados. Meses futuros ficam em branco.",merge_to="O")
hdr(rs,4,["Linha"]+[m[:3] for m in MESES]+["Total do ano","Média dos meses preenchidos"],height=30)
NC=len(dados.CUSTOS_FIXOS); NS=len(SOCIOS)
R_REC0=6; R_RECT=R_REC0+len(MODAL)             # 6..9 modalidades, 10 receita total
R_CF0=R_RECT+2; R_CFT=R_CF0+NC                  # 12..19 custos, 20 total custos
R_PL0=R_CFT+2; R_PLT=R_PL0+NS                   # 22..23 sócios, 24 total pró-labore
R_IMP=R_PLT+1; R_SAI=R_IMP+1; R_RES=R_SAI+1; R_MAR=R_RES+1   # 25 impostos, 26 saídas, 27 resultado, 28 margem
def secao(r,txt): c=rs.cell(row=r,column=1,value=txt); c.font=F(bold=True,size=11,color=UVA); c.fill=fill(LAVANDA); [setattr(rs.cell(row=r,column=k),"fill",fill(LAVANDA)) for k in range(2,16)]
def linha_total(r,txt,fn,fmt=BRL0,bold=True):
    rs.cell(row=r,column=1,value=txt); rotulo(rs.cell(row=r,column=1),bold=bold); rs.cell(row=r,column=1).border=borda
    for m in range(12):
        col=L(2+m); cell=rs.cell(row=r,column=2+m,value=fn(col)); calc(cell,fmt)
        if bold: cell.font=F(bold=True,color=UVA,size=10)
secao(R_REC0-1,"Receita (o que entrou no mês, por modalidade de honorário)")
for j,nome in enumerate(MODAL):
    r=R_REC0+j; rs.cell(row=r,column=1,value=nome); rotulo(rs.cell(row=r,column=1),bold=False); rs.cell(row=r,column=1).border=borda
    for m in range(12):
        cell=rs.cell(row=r,column=2+m); inp(cell,BRL0,center=True)
        if m<9: cell.value=modalidades(m)[j]
PREENCH=lambda col: f'COUNT({col}${R_REC0}:{col}${R_RECT-1},{col}${R_CF0}:{col}${R_CFT-1},{col}${R_PL0}:{col}${R_PLT-1})=0'
linha_total(R_RECT,"Receita total",lambda col: f'=IF({PREENCH(col)},"",SUM({col}{R_REC0}:{col}{R_RECT-1}))')
secao(R_CF0-1,"Custos fixos")
for j,(nome,v) in enumerate(dados.CUSTOS_FIXOS):
    r=R_CF0+j; rs.cell(row=r,column=1,value=nome); rotulo(rs.cell(row=r,column=1),bold=False); rs.cell(row=r,column=1).border=borda
    for m in range(12):
        cell=rs.cell(row=r,column=2+m); inp(cell,BRL0,center=True)
        if m<9: cell.value=custos_mes(m)[j]
linha_total(R_CFT,"Total de custos fixos",lambda col: f'=IF({PREENCH(col)},"",SUM({col}{R_CF0}:{col}{R_CFT-1}))')
secao(R_PL0-1,"Pró-labore dos sócios")
for j,(nome,v) in enumerate(SOCIOS):
    r=R_PL0+j; rs.cell(row=r,column=1,value=nome); rotulo(rs.cell(row=r,column=1),bold=False); rs.cell(row=r,column=1).border=borda
    for m in range(12):
        cell=rs.cell(row=r,column=2+m); inp(cell,BRL0,center=True)
        if m<9: cell.value=v
linha_total(R_PLT,"Total de pró-labore",lambda col: f'=IF({PREENCH(col)},"",SUM({col}{R_PL0}:{col}{R_PLT-1}))')
linha_total(R_IMP,"Impostos provisionados (% da receita, Config)",lambda col: f'=IF({col}{R_RECT}="","",ROUND({col}{R_RECT}*Config!$B$7,0))',bold=False)
linha_total(R_SAI,"Total de saídas (custos + pró-labore + impostos)",lambda col: f'=IF({col}{R_RECT}="","",{col}{R_CFT}+{col}{R_PLT}+{col}{R_IMP})')
linha_total(R_RES,"Resultado do mês (receita - saídas)",lambda col: f'=IF({col}{R_RECT}="","",{col}{R_RECT}-{col}{R_SAI})')
linha_total(R_MAR,"Margem (resultado ÷ receita)",lambda col: f'=IF(OR({col}{R_RECT}="",{col}{R_RECT}=0),"",{col}{R_RES}/{col}{R_RECT})',fmt="0.0%")
# Total do ano e média (colunas N e O)
for r in list(range(R_REC0,R_RECT+1))+list(range(R_CF0,R_CFT+1))+list(range(R_PL0,R_PLT+1))+[R_IMP,R_SAI,R_RES]:
    rs.cell(row=r,column=14,value=f'=IF(COUNT(B{r}:M{r})=0,"",SUM(B{r}:M{r}))'); calc(rs.cell(row=r,column=14),BRL0)
    rs.cell(row=r,column=15,value=f'=IF(COUNT(B{r}:M{r})=0,"",AVERAGE(B{r}:M{r}))'); calc(rs.cell(row=r,column=15),BRL0)
    if r in (R_RECT,R_CFT,R_PLT,R_SAI,R_RES):
        for k in (14,15): rs.cell(row=r,column=k).font=F(bold=True,color=UVA,size=10)
rs.cell(row=R_MAR,column=14,value=f'=IF(OR(N{R_RECT}="",N{R_RECT}=0),"",N{R_RES}/N{R_RECT})'); calc(rs.cell(row=R_MAR,column=14),"0.0%")
rs.cell(row=R_MAR,column=15,value=f'=IF(COUNT(B{R_MAR}:M{R_MAR})=0,"",AVERAGE(B{R_MAR}:M{R_MAR}))'); calc(rs.cell(row=R_MAR,column=15),"0.0%")
rs.conditional_formatting.add(f"B{R_RES}:O{R_RES}", FormulaRule(formula=[f'AND(ISNUMBER(B{R_RES}),B{R_RES}<0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
rs.conditional_formatting.add(f"B{R_RES}:O{R_RES}", FormulaRule(formula=[f'AND(ISNUMBER(B{R_RES}),B{R_RES}>=0)'], fill=fill(VERDE), font=F(color=VERDE_T,size=10,bold=True)))
rs.conditional_formatting.add("B4:M4", FormulaRule(formula=['COLUMN()-1=Config!$B$8'], fill=fill(SOL), font=F(color=UVA,size=10,bold=True)))
rs.cell(row=R_MAR+2,column=1,value="Honorário misto: lance a parte fixa em \"fixos\" e a parte de êxito em \"êxito\" quando cada uma entrar. Impostos são provisão (o que separar), não o pagamento da guia. Resultado negativo fica vermelho.").font=F(size=9,color=LILAS)
rs.merge_cells(start_row=R_MAR+2,start_column=1,end_row=R_MAR+2,end_column=15)
rs.cell(row=R_MAR+3,column=1,value="Os valores de exemplo (janeiro a setembro de 2026) batem com o Caixa (09), o Painel do escritório (17) e o Resumo do mês (20). Aqui os impostos são provisão; no caixa aparece a guia paga.").font=F(size=9,color=LILAS)
rs.merge_cells(start_row=R_MAR+3,start_column=1,end_row=R_MAR+3,end_column=15)
widths(rs,[44]+[11]*12+[14,16]); rs.freeze_panes="B5"; rs.sheet_view.showGridLines=False

# ---------- Previsto ----------
pv=wb.create_sheet("Previsto")
titulo(pv,"Previsto para o ano","Preencha o que espera de receita, custos fixos e pró-labore em cada mês. O Painel compara o realizado com este previsto.",merge_to="N")
hdr(pv,4,["Linha"]+[m[:3] for m in MESES]+["Total do ano"],height=30)
PV=["Receita prevista","Custos fixos previstos","Pró-labore previsto","Impostos previstos (% da receita, Config)","Saídas previstas","Resultado previsto","Margem prevista"]
PV_EX=[PREV_RECEITA,[sum(v for _,v in dados.CUSTOS_FIXOS)]*12,[sum(c for _,c in SOCIOS)]*12]
for j,nome in enumerate(PV):
    r=5+j; pv.cell(row=r,column=1,value=nome); rotulo(pv.cell(row=r,column=1),bold=(j>=4)); pv.cell(row=r,column=1).border=borda
    for m in range(12):
        col=L(2+m); cell=pv.cell(row=r,column=2+m)
        if j<3: inp(cell,BRL0,center=True); cell.value=PV_EX[j][m]
        elif j==3: cell.value=f'=IF({col}5="","",ROUND({col}5*Config!$B$7,0))'; calc(cell,BRL0)
        elif j==4: cell.value=f'=IF({col}5="","",N({col}6)+N({col}7)+{col}8)'; calc(cell,BRL0)
        elif j==5: cell.value=f'=IF({col}5="","",{col}5-{col}9)'; calc(cell,BRL0)
        else: cell.value=f'=IF(OR({col}5="",{col}5=0),"",{col}10/{col}5)'; calc(cell,"0.0%")
    if j<6: pv.cell(row=r,column=14,value=f'=IF(COUNT(B{r}:M{r})=0,"",SUM(B{r}:M{r}))'); calc(pv.cell(row=r,column=14),BRL0)
    else: pv.cell(row=r,column=14,value='=IF(OR(N5="",N5=0),"",N10/N5)'); calc(pv.cell(row=r,column=14),"0.0%")
pv.cell(row=13,column=1,value="Uma boa previsão de custos fixos é a média dos últimos três meses; de receita, o que já está contratado para o mês mais o que costuma fechar.").font=F(size=9,color=LILAS)
pv.merge_cells("A13:N13")
widths(pv,[40]+[11]*12+[14]); pv.freeze_panes="B5"; pv.sheet_view.showGridLines=False

# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
p["A1"]='=Config!B4&" · Resultado mensal · "&Config!B6&" de "&Config!B5'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:H1")
p["A2"]="Nada para digitar aqui. Escolha o mês em Config; os números vêm de Resultado e de Previsto."; nota(p["A2"]); p.merge_cells("A2:H2")
M="Config!$B$8"
def mes(r,off=0):  # valor da linha r de Resultado no mês (ou mês anterior)
    idx=f"{M}-{off}" if off else M
    return f'INDEX(Resultado!$B${r}:$M${r},{idx})'
def val(r,fmt_blank='"—"'): return f'=IF({mes(r)}="",{fmt_blank},{mes(r)})'
kpi(p,4,1,"Receita do mês",val(R_RECT),LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Saídas do mês",val(R_SAI),LAVANDA,UVA,fmt=BRL0)
kpi(p,4,5,"Resultado",val(R_RES),VERDE,VERDE_T,fmt=BRL0)
kpi(p,4,7,"Margem",val(R_MAR),SOL,UVA,fmt="0.0%")
p.conditional_formatting.add("E5", FormulaRule(formula=['AND(ISNUMBER(E5),E5<0)'], fill=fill(VERM), font=F(size=16,bold=True,color=VERM_T)))
p["A7"]="Comparação com o mês anterior e com o previsto"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Linha","","Mês","Mês anterior","Variação","Previsto","Vs. previsto","Situação"]); p.merge_cells("A8:B8")
COMP=[("Receita total",R_RECT,5,"Maior é melhor"),("Custos fixos",R_CFT,6,"Menor é melhor"),("Pró-labore",R_PLT,7,""),("Impostos provisionados",R_IMP,8,""),
      ("Total de saídas",R_SAI,9,"Menor é melhor"),("Resultado do mês",R_RES,10,"Maior é melhor"),("Margem",R_MAR,11,"Maior é melhor")]
for i,(nome,r,pr,sent) in enumerate(COMP):
    rr=9+i; pct=(r==R_MAR); fmt="0.0%" if pct else BRL0
    p.cell(row=rr,column=1,value=nome); rotulo(p.cell(row=rr,column=1),bold=(r in (R_RECT,R_SAI,R_RES))); p.cell(row=rr,column=1).border=borda; p.merge_cells(start_row=rr,start_column=1,end_row=rr,end_column=2)
    p.cell(row=rr,column=3,value=val(r)); calc(p.cell(row=rr,column=3),fmt)
    p.cell(row=rr,column=4,value=f'=IF({M}<=1,"—",IF({mes(r,1)}="","—",{mes(r,1)}))'); calc(p.cell(row=rr,column=4),fmt)
    if pct:
        p.cell(row=rr,column=5,value=f'=IF(OR(C{rr}="—",D{rr}="—"),"—",(C{rr}-D{rr})*100)'); calc(p.cell(row=rr,column=5),'+0.0" p.p.";-0.0" p.p.";0.0" p.p."')
    else:
        p.cell(row=rr,column=5,value=f'=IF(OR(C{rr}="—",D{rr}="—",D{rr}=0),"—",(C{rr}-D{rr})/ABS(D{rr}))'); calc(p.cell(row=rr,column=5),"+0.0%;-0.0%;0.0%")
    p.cell(row=rr,column=6,value=f'=IF(INDEX(Previsto!$B${pr}:$M${pr},{M})="","—",INDEX(Previsto!$B${pr}:$M${pr},{M}))'); calc(p.cell(row=rr,column=6),fmt)
    if pct:
        p.cell(row=rr,column=7,value=f'=IF(OR(C{rr}="—",F{rr}="—"),"—",(C{rr}-F{rr})*100)'); calc(p.cell(row=rr,column=7),'+0.0" p.p.";-0.0" p.p.";0.0" p.p."')
    else:
        p.cell(row=rr,column=7,value=f'=IF(OR(C{rr}="—",F{rr}="—",F{rr}=0),"—",(C{rr}-F{rr})/ABS(F{rr}))'); calc(p.cell(row=rr,column=7),"+0.0%;-0.0%;0.0%")
    if sent:
        cond=f'C{rr}<=F{rr}' if sent=="Menor é melhor" else f'C{rr}>=F{rr}'
        p.cell(row=rr,column=8,value=f'=IF(OR(C{rr}="—",F{rr}="—"),"—",IF({cond},"Dentro do previsto",IF({"C"+str(rr)+"<=F"+str(rr)+"*1.05" if sent=="Menor é melhor" else "C"+str(rr)+">=F"+str(rr)+"*0.95"},"Perto","Fora do previsto")))')
    else:
        p.cell(row=rr,column=8,value="Informativo")
    calc(p.cell(row=rr,column=8))
for cor,txt,fnt in ((VERDE,"Dentro do previsto",VERDE_T),(AMARELO,"Perto","7A5200"),(VERM,"Fora do previsto",VERM_T)):
    p.conditional_formatting.add("H9:H15", FormulaRule(formula=[f'H9="{txt}"'], fill=fill(cor), font=F(color=fnt,size=10,bold=(txt=="Fora do previsto"))))
p["A17"]="Receita do mês por modalidade"; p["A17"].font=F(bold=True,size=13,color=UVA)
hdr(p,18,["Modalidade","","Mês","Mês anterior","Variação","% da receita"]); p.merge_cells("A18:B18")
for j,nome in enumerate(MODAL):
    rr=19+j; r=R_REC0+j
    p.cell(row=rr,column=1,value=nome); rotulo(p.cell(row=rr,column=1),bold=False); p.cell(row=rr,column=1).border=borda; p.merge_cells(start_row=rr,start_column=1,end_row=rr,end_column=2)
    p.cell(row=rr,column=3,value=val(r)); calc(p.cell(row=rr,column=3),BRL0)
    p.cell(row=rr,column=4,value=f'=IF({M}<=1,"—",IF({mes(r,1)}="","—",{mes(r,1)}))'); calc(p.cell(row=rr,column=4),BRL0)
    p.cell(row=rr,column=5,value=f'=IF(OR(C{rr}="—",D{rr}="—",D{rr}=0),"—",(C{rr}-D{rr})/ABS(D{rr}))'); calc(p.cell(row=rr,column=5),"+0.0%;-0.0%;0.0%")
    p.cell(row=rr,column=6,value=f'=IF(OR(C{rr}="—",C9="—",C9=0),"—",C{rr}/C9)'); calc(p.cell(row=rr,column=6),PCT)
p["A24"]="Receita, saídas e resultado no ano (meses em branco não aparecem)"; nota(p["A24"])
bc=BarChart(); bc.type="col"; bc.grouping="clustered"; bc.title=None; bc.height=8.5; bc.width=24; bc.style=2
for r,cor in ((R_RECT,UVA),(R_SAI,LILAS),(R_RES,SOL)):
    bc.add_data(Reference(rs,min_col=1,max_col=13,min_row=r,max_row=r),from_rows=True,titles_from_data=True)
for sr,cor in zip(bc.series,(UVA,LILAS,SOL)): sr.graphicalProperties.solidFill=cor; sr.graphicalProperties.line.solidFill=cor
bc.set_categories(Reference(rs,min_col=2,max_col=13,min_row=4,max_row=4))
bc.y_axis.majorGridlines=None; bc.legend.position="b"; bc.y_axis.number_format='"R$" #,##0'
p.add_chart(bc,"A25")
p.cell(row=43,column=1,value='Para explicar o resultado ao sócio ou ao contador, use a planilha 20 · Resumo do mês e o prompt "Explicar o mês".').font=F(size=9,color=LILAS)
p.merge_cells("A43:H43")
widths(p,(24,16,14,14,13,14,13,18)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False

como_usar(wb,"Resultado Mensal",[
 ("O que esta planilha faz","Uma DRE simplificada do escritório: receita por modalidade de honorário, custos fixos, pró-labore, impostos provisionados como % da receita, resultado e margem, mês a mês. Compara o mês com o anterior e com o que você previu."),
 ("Passo 1","Em Config, informe o ano, o mês de análise e a % de impostos a provisionar (peça ao contador a alíquota efetiva)."),
 ("Passo 2","Em Resultado, preencha por mês o que entrou em cada modalidade e o que saiu em cada linha de custo fixo e de pró-labore. Os totais do mês estão no Painel da planilha 09 · Caixa do escritório."),
 ("Passo 3","Em Previsto, escreva o que espera de receita, custos fixos e pró-labore para cada mês. Pode ser o mesmo valor o ano inteiro."),
 ("Passo 4","Abra Painel: receita, saídas, resultado e margem do mês, comparação com o mês anterior e com o previsto, receita por modalidade e o gráfico do ano."),
 ("Fim do mês","Depois de fechar o caixa, lance o mês aqui e troque o mês em Config. Leva 10 minutos."),
 ("Com a IA","Copie a tabela do Painel para o prompt \"Explicar o mês\" ou \"Preparar a reunião com o contador\" da biblioteca do kit. A planilha 20 · Resumo do mês já escreve o texto-base."),
])
proteger(wb); salvar(wb,"18-resultado-mensal.xlsx","Resultado Mensal · Kit de Gestão para Advogados")
