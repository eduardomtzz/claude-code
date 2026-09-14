#!/usr/bin/env python3
"""Planilha 17 do Kit de Gestão para Advogados: Painel do Escritório. Gera 17-painel-do-escritorio.xlsx
Uma tela com prazos, horas, caixa, recebíveis e propostas. Os números vêm da aba Dados (copiados toda sexta das
planilhas 01, 09, 13, 14, 15 e 16); o Histórico guarda uma linha por mês.
Exemplo alinhado às outras planilhas do kit: entradas de jan–ago iguais aos lançamentos da 09 (setembro = mês fechado, estimado),
a receber e casos ativos da 13, vencido e inadimplência da 14, propostas da 15, horas de agosto da 16, prazos da 01.
Os totais mensais (entrou, saiu, a receber, vencido...) são os mesmos das planilhas 18 e 20."""
from ssg import *
import dados
from openpyxl.chart import BarChart, LineChart, Reference

# ---------- exemplo compartilhado (jan..set/2026; mesmos números em build_18 e build_20) ----------
RECEITA=[33660,14000,19560,20900,19200,25970,30170,26660,29400]           # entrou no mês: jan–ago = lançamentos da 09; set = mês fechado (estimado)
CUSTOS=sum(v for n,v in dados.CUSTOS_FIXOS)                                  # 6.500/mês, mesmas linhas da 05 e da 09
PRO_LABORE=sum(c for n,p,c,h in dados.PESSOAS if p.startswith("Sóci"))     # 12.000
IMPOSTO=0.06                                                                 # provisão (planilha 10 e 18)
SAIDAS=[CUSTOS+PRO_LABORE+round(RECEITA[i]*IMPOSTO) for i in range(9)]
PRAZOS_SEMANA=[9,11,8,12,10,14,9,11,14]; ATRASADOS=[3,2,4,1,5,6,4,5,7]      # set: 01 mostra hoje 3 + próximos 7 dias 11
HORAS=[262,274,301,288,312,296,283,298,318]; FATURAVEIS=[171,183,208,196,224,209,195,232,226]   # ago = 16 (298 h, 77,9%)
A_RECEBER=[96400,101800,108300,112900,117600,121400,119800,124500,128280]; VENCIDO=[14200,15900,17800,19300,22400,21100,23600,24900,26590]
INAD=[0.148,0.156,0.164,0.171,0.190,0.174,0.197,0.171,0.174]                 # vencido ÷ parcelas em aberto, como na 14
PROP_N=[3,4,3,5,4,6,5,6,8]; PROP_V=[22500,31000,24800,39500,30200,47300,41000,51300,68400]; CASOS_ATIVOS=[27,27,28,29,30,32,31,30,30]
# coerência com dados.py (painel de 14/09/2026)
c=dados.CASOS
assert ATRASADOS[-1]==sum(1 for x in c if x["proximo_prazo_dias"] is not None and x["proximo_prazo_dias"]<0)
assert A_RECEBER[-1]==sum(x["valor_contratado"]-x["recebido"] for x in c)
assert CASOS_ATIVOS[-1]==sum(1 for x in c if x["fase"]!="Encerrado")
assert sum(RECEITA)<=sum(x["recebido"] for x in c)

wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche.",merge_to="E")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Mês do painel"; cfg["B5"]="Setembro"
cfg["A6"]="Ano"; cfg["B6"]=2026
cfg["A7"]="Data de referência (hoje)"; cfg["B7"]="=TODAY()"
cfg["A8"]="Número do mês"; cfg["B8"]="=MATCH(B5,$D$5:$D$16,0)"
cfg["A9"]="Mês anterior"; cfg["B9"]='=IF(B8>1,INDEX($D$5:$D$16,B8-1),"")'
for r in range(4,10): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"]); inp(cfg["B6"]); inp(cfg["B7"],DATA); calc(cfg["B8"]); calc(cfg["B9"])
cfg["D4"]="Meses"; rotulo(cfg["D4"])
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=4,value=m).font=F(size=10,color=TINTA)
dv=lista("=Config!$D$5:$D$16",allow_blank=False); dv.add("B5"); cfg.add_data_validation(dv)
cfg["A11"]="Use a mesma planilha o ano inteiro: troque o mês aqui e, no fim de cada mês, copie a linha de Dados para o Histórico."; nota(cfg["A11"])
widths(cfg,(28,40,4,14)); cfg.sheet_view.showGridLines=False

# ---------- Dados (entrada semanal) ----------
d=wb.create_sheet("Dados")
titulo(d,"Dados da semana","Toda sexta, copie os totais das outras planilhas do kit para as células amarelas. Limites e metas também são seus. O resto é calculado.",merge_to="G")
hdr(d,4,["Indicador","Valor desta sexta","Limite ou meta","Sentido","Copie de (planilha do kit)","Situação"])
R0=5
# (chave, rótulo, valor do exemplo ou fórmula, limite, sentido, fonte, formato)
LINHAS=[
 ("prazos","Prazos de hoje e dos próximos 7 dias",PRAZOS_SEMANA[-1],None,"","01 · Agenda de prazos (Painel: Hoje + Próximos 7 dias)","#,##0"),
 ("atras","Prazos atrasados",ATRASADOS[-1],0,"Menor é melhor","01 · Agenda de prazos (Painel)","#,##0"),
 ("horas","Horas registradas no mês",HORAS[-1],300,"Maior é melhor","16 · Horas por caso e por pessoa (Painel)","#,##0"),
 ("fatur","Horas faturáveis no mês",FATURAVEIS[-1],200,"Maior é melhor","16 · Horas por caso e por pessoa (Painel)","#,##0"),
 ("pfat","% de horas faturáveis","=IF(OR(B7=\"\",B7=0,B8=\"\"),\"\",B8/B7)",0.70,"Maior é melhor","calculado aqui",PCT),
 ("entrou","Entrou no mês (recebimentos)",RECEITA[-1],30000,"Maior é melhor","09 · Caixa do escritório (Painel)",BRL0),
 ("saiu","Saiu no mês (custos, pró-labore e provisão de impostos)",SAIDAS[-1],20500,"Menor é melhor","09 · Caixa do escritório (Painel)",BRL0),
 ("sobrou","Sobrou no mês","=IF(OR(B10=\"\",B11=\"\"),\"\",B10-B11)",9500,"Maior é melhor","calculado aqui",BRL0),
 ("areceb","A receber (carteira)",A_RECEBER[-1],120000,"Menor é melhor","13 · Carteira de clientes e casos (Painel)",BRL0),
 ("venc","Vencido (parcelas em atraso)",VENCIDO[-1],15000,"Menor é melhor","14 · Parcelas e inadimplência (Painel)",BRL0),
 ("inad","Inadimplência (vencido ÷ parcelas em aberto)",INAD[-1],0.10,"Menor é melhor","14 · Parcelas e inadimplência (Painel)",PCT),
 ("propn","Propostas abertas (quantidade)",PROP_N[-1],None,"","15 · Propostas enviadas × fechadas (Painel)","#,##0"),
 ("propv","Propostas abertas (valor)",PROP_V[-1],40000,"Maior é melhor","15 · Propostas enviadas × fechadas (Painel)",BRL0),
 ("casos","Casos ativos",CASOS_ATIVOS[-1],32,"Maior é melhor","13 · Carteira de clientes e casos (Painel)","#,##0"),
]
ROW={k:R0+i for i,(k,*_) in enumerate(LINHAS)}
RN=R0+len(LINHAS)-1
for i,(k,rot,val,lim,sent,fonte,fmt) in enumerate(LINHAS):
    r=R0+i
    d.cell(row=r,column=1,value=rot); rotulo(d.cell(row=r,column=1),bold=False); d.cell(row=r,column=1).border=borda
    b=d.cell(row=r,column=2,value=val)
    if isinstance(val,str) and val.startswith("="): calc(b,fmt)
    else: inp(b,fmt,center=True)
    inp(d.cell(row=r,column=3,value=lim),fmt,center=True); inp(d.cell(row=r,column=4,value=sent),center=True)
    d.cell(row=r,column=5,value=fonte); nota(d.cell(row=r,column=5)); d.cell(row=r,column=5).border=borda
    d.cell(row=r,column=6,value=(f'=IF(OR(B{r}="",C{r}=""),"Informativo",IF(D{r}="Menor é melhor",IF(B{r}<=C{r},"No alvo",IF(B{r}<=C{r}*1.1,"Perto","Fora")),'
                                 f'IF(B{r}>=C{r},"No alvo",IF(B{r}>=C{r}*0.9,"Perto","Fora"))))')); calc(d.cell(row=r,column=6))
dvs=lista('"Maior é melhor,Menor é melhor"'); dvs.add(f"D{R0}:D{RN}"); d.add_data_validation(dvs)
for cor,txt,fnt in ((VERDE,"No alvo",VERDE_T),(AMARELO,"Perto","7A5200"),(VERM,"Fora",VERM_T)):
    d.conditional_formatting.add(f"F{R0}:F{RN}", FormulaRule(formula=[f'F{R0}="{txt}"'], fill=fill(cor), font=F(color=fnt,size=10,bold=(txt=="Fora"))))
d.cell(row=RN+2,column=1,value="Linha sem limite fica \"Informativo\". \"Perto\" é até 10% do limite. Inadimplência vem da planilha 14 (vencido ÷ parcelas em aberto). Os valores desta sexta valem para o mês escolhido em Config; no fim do mês, copie a coluna B para a linha do mês em Histórico.").font=F(size=9,color=LILAS)
d.merge_cells(start_row=RN+2,start_column=1,end_row=RN+2,end_column=6)
d.cell(row=RN+3,column=1,value="As planilhas indicadas em \"Copie de\" são as do próprio kit. Se ainda não usa alguma, deixe a linha em branco: o painel mostra \"—\".").font=F(size=9,color=LILAS)
d.merge_cells(start_row=RN+3,start_column=1,end_row=RN+3,end_column=6)
widths(d,(50,16,14,16,42,12)); d.freeze_panes="B5"; d.sheet_view.showGridLines=False

# ---------- Histórico ----------
h=wb.create_sheet("Histórico")
titulo(h,"Histórico mensal","No fim de cada mês, copie os valores da aba Dados para a linha do mês. Colunas brancas são calculadas; deixe em branco os meses que ainda não aconteceram.",merge_to="O")
HCOLS=[("prazos","Prazos hoje + 7 dias","#,##0"),("atras","Atrasados","#,##0"),("horas","Horas do mês","#,##0"),("fatur","Faturáveis","#,##0"),("pfat","% faturável",PCT),
       ("entrou","Entrou",BRL0),("saiu","Saiu",BRL0),("sobrou","Sobrou",BRL0),("areceb","A receber",BRL0),("venc","Vencido",BRL0),("inad","Inadimplência",PCT),
       ("propn","Propostas abertas","#,##0"),("propv","Valor das propostas",BRL0),("casos","Casos ativos","#,##0")]
HCOL={k:2+i for i,(k,*_) in enumerate(HCOLS)}
hdr(h,4,["Mês"]+[t for _,t,_ in HCOLS],height=32)
EX={"prazos":PRAZOS_SEMANA,"atras":ATRASADOS,"horas":HORAS,"fatur":FATURAVEIS,"entrou":RECEITA,"saiu":SAIDAS,"areceb":A_RECEBER,"venc":VENCIDO,"inad":INAD,"propn":PROP_N,"propv":PROP_V,"casos":CASOS_ATIVOS}
for m in range(12):
    r=5+m
    h.cell(row=r,column=1,value=MESES[m]); rotulo(h.cell(row=r,column=1),bold=False); h.cell(row=r,column=1).border=borda
    for k,t,fmt in HCOLS:
        col=HCOL[k]; cell=h.cell(row=r,column=col)
        if k=="pfat": cell.value=f'=IF(OR({L(HCOL["horas"])}{r}="",{L(HCOL["horas"])}{r}=0,{L(HCOL["fatur"])}{r}=""),"",{L(HCOL["fatur"])}{r}/{L(HCOL["horas"])}{r})'; calc(cell,fmt)
        elif k=="sobrou": cell.value=f'=IF(OR({L(HCOL["entrou"])}{r}="",{L(HCOL["saiu"])}{r}=""),"",{L(HCOL["entrou"])}{r}-{L(HCOL["saiu"])}{r})'; calc(cell,fmt)
        else:
            inp(cell,fmt,center=True)
            if m<9: cell.value=EX[k][m]
h.conditional_formatting.add("A5:A16", FormulaRule(formula=['ROW()-4=Config!$B$8'], fill=fill(SOL), font=F(color=UVA,size=10,bold=True)))
h.cell(row=18,column=1,value="A linha do mês escolhido em Config fica destacada. Setembro repete os valores da aba Dados (exemplo).").font=F(size=9,color=LILAS)
# gráficos apontam direto para as colunas de entrada: mês ainda vazio fica sem barra/ponto (sem NA(), sem linha auxiliar)
def serie_cols(k1,k2): return Reference(h,min_col=HCOL[k1],max_col=HCOL[k2],min_row=4,max_row=16)
cats=Reference(h,min_col=1,max_col=1,min_row=5,max_row=16)
bc=BarChart(); bc.type="col"; bc.grouping="clustered"; bc.title="Caixa do mês: entrou, saiu, sobrou"; bc.height=8; bc.width=22; bc.style=2
bc.add_data(serie_cols("entrou","sobrou"),titles_from_data=True); bc.set_categories(cats)  # mês vazio = barra de altura zero (invisível)
for sr,cor in zip(bc.series,(UVA,LILAS,SOL)): sr.graphicalProperties.solidFill=cor; sr.graphicalProperties.line.solidFill=cor
bc.y_axis.majorGridlines=None; bc.legend.position="b"; bc.y_axis.number_format='"R$" #,##0'; bc.dispBlanksAs="gap"
h.add_chart(bc,"A20")
lc=LineChart(); lc.title="Recebíveis: a receber e vencido"; lc.height=8; lc.width=22; lc.style=2
lc.add_data(serie_cols("areceb","venc"),titles_from_data=True); lc.set_categories(cats)
lc.series[0].graphicalProperties.line.solidFill=UVA; lc.series[0].graphicalProperties.line.width=28000
lc.series[1].graphicalProperties.line.solidFill="C0392B"; lc.series[1].graphicalProperties.line.width=28000
for sr in lc.series: sr.smooth=False
lc.y_axis.majorGridlines=None; lc.legend.position="b"; lc.dispBlanksAs="gap"; lc.y_axis.number_format='"R$" #,##0'
h.add_chart(lc,"A38")
widths(h,[12]+[12]*14); h.freeze_panes="B5"; h.sheet_view.showGridLines=False

# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
p["A1"]='=Config!B4&" · Painel do escritório · "&Config!B5&" de "&Config!B6'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:J1")
p["A2"]='="Nada para digitar aqui. Os números vêm da aba Dados (atualizada toda sexta) e o mês anterior vem do Histórico. Referência: "&TEXT(Config!B7,"dd/mm/yyyy")&"."'; nota(p["A2"]); p.merge_cells("A2:J2")
def dv_(k): return f"Dados!$B${ROW[k]}"
def val(k): return f'=IF({dv_(k)}="","—",{dv_(k)})'
tiles=[(4,[("prazos","Prazos hoje + 7 dias","#,##0"),("atras","Prazos atrasados","#,##0"),("horas","Horas do mês","#,##0"),("fatur","Horas faturáveis","#,##0"),("casos","Casos ativos","#,##0")]),
       (7,[("entrou","Entrou no mês",BRL0),("saiu","Saiu no mês",BRL0),("sobrou","Sobrou no mês",BRL0),("areceb","A receber",BRL0),("venc","Vencido",BRL0)]),
       (10,[("propn","Propostas abertas","#,##0"),("propv","Valor das propostas",BRL0),("pfat","% de horas faturáveis",PCT),("inad","Inadimplência",PCT)])]
for row,items in tiles:
    for j,(k,rot,fmt) in enumerate(items):
        col=1+2*j; kpi(p,row,col,rot,val(k),LAVANDA,UVA,fmt=fmt)
        ref=f"Dados!$F${ROW[k]}"; cell=f"{L(col)}{row+1}"
        p.conditional_formatting.add(cell, FormulaRule(formula=[f'{ref}="Fora"'], fill=fill(VERM), font=F(size=16,bold=True,color=VERM_T)))
        p.conditional_formatting.add(cell, FormulaRule(formula=[f'{ref}="Perto"'], fill=fill(AMARELO), font=F(size=16,bold=True,color="7A5200")))
        p.conditional_formatting.add(cell, FormulaRule(formula=[f'{ref}="No alvo"'], fill=fill(VERDE), font=F(size=16,bold=True,color=VERDE_T)))
p["I10"]="Cores dos cartões"; p["I10"].font=F(size=9,bold=True,color=UVA); p["I11"]="Verde: no alvo · Amarelo: perto do limite · Vermelho: fora · Lilás: informativo"; nota(p["I11"]); p["I11"].alignment=Alignment(wrap_text=True,vertical="top"); p.merge_cells("I11:J11")
p["A13"]="Semáforos da semana e comparação com o mês anterior"; p["A13"].font=F(bold=True,size=13,color=UVA)
hdr(p,14,["Indicador","","Esta sexta","Limite ou meta","Situação","Mês anterior (Histórico)","Variação"]); p.merge_cells("A14:B14")
T0=15
for i,(k,rot,val_,lim,sent,fonte,fmt) in enumerate(LINHAS):
    r=T0+i; s=ROW[k]
    p.cell(row=r,column=1,value=f"=Dados!A{s}"); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2)
    p.cell(row=r,column=3,value=f'=IF(Dados!B{s}="","—",Dados!B{s})'); calc(p.cell(row=r,column=3),fmt)
    p.cell(row=r,column=4,value=f'=IF(Dados!C{s}="","—",Dados!C{s})'); calc(p.cell(row=r,column=4),fmt)
    p.cell(row=r,column=5,value=f"=Dados!F{s}"); calc(p.cell(row=r,column=5))
    hc=L(HCOL[k])
    p.cell(row=r,column=6,value=f'=IF(Config!$B$8<=1,"—",IF(INDEX(Histórico!${hc}$5:${hc}$16,Config!$B$8-1)="","—",INDEX(Histórico!${hc}$5:${hc}$16,Config!$B$8-1)))'); calc(p.cell(row=r,column=6),fmt)
    p.cell(row=r,column=7,value=f'=IF(OR(C{r}="—",F{r}="—",F{r}=0),"—",(C{r}-F{r})/ABS(F{r}))'); calc(p.cell(row=r,column=7),"+0.0%;-0.0%;0.0%")
TN=T0+len(LINHAS)-1
for cor,txt,fnt in ((VERDE,"No alvo",VERDE_T),(AMARELO,"Perto","7A5200"),(VERM,"Fora",VERM_T)):
    p.conditional_formatting.add(f"E{T0}:E{TN}", FormulaRule(formula=[f'E{T0}="{txt}"'], fill=fill(cor), font=F(color=fnt,size=10,bold=(txt=="Fora"))))
p.cell(row=TN+2,column=1,value="Fora do alvo primeiro: prazos atrasados e vencido pedem ação na segunda-feira (planilhas 01 e 14). A planilha avisa; o controle é do escritório.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=TN+2,start_column=1,end_row=TN+2,end_column=10)
p.cell(row=TN+3,column=1,value='Para transformar esta tela em texto para o sócio ou o contador, use a planilha 20 · Resumo do mês e o prompt "Explicar o mês".').font=F(size=9,color=LILAS)
p.merge_cells(start_row=TN+3,start_column=1,end_row=TN+3,end_column=10)
widths(p,(22,22,14,14,14,18,12,12,12,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False

como_usar(wb,"Painel do Escritório",[
 ("O que esta planilha faz","Reúne em uma tela os números que já estão nas outras planilhas do kit: prazos da semana e atrasados, horas do mês e faturáveis, o que entrou, saiu e sobrou, a receber e vencido, propostas abertas e casos ativos. Cada número ganha um semáforo contra o limite que você definir e a comparação com o mês anterior."),
 ("Toda sexta (10 minutos)","Abra as planilhas 01 (prazos), 16 (horas), 09 (caixa), 13 (carteira), 14 (inadimplência) e 15 (propostas), copie os totais do Painel de cada uma para a coluna B da aba Dados. Pronto: o Painel se refaz."),
 ("Limites e metas","Na aba Dados, coluna C, escreva o limite de cada indicador (ex.: 0 prazos atrasados, 70% de horas faturáveis, inadimplência de 10%) e diga se maior ou menor é melhor. Linha sem limite fica informativa."),
 ("Fim do mês","Copie a coluna B da aba Dados para a linha do mês em Histórico. Os gráficos de caixa e de recebíveis usam essa aba; o Painel busca ali o mês anterior."),
 ("Config","Escolha o mês do painel e mantenha a data de referência em =HOJE(). O título do Painel se ajusta."),
 ("Com a IA","O Painel é a tela da rotina de sexta. Para o texto do mês (sócio, contador), use a planilha 20 · Resumo do mês e o prompt \"Explicar o mês\" da biblioteca."),
])
proteger(wb); salvar(wb,"17-painel-do-escritorio.xlsx","Painel do Escritório · Kit de Gestão para Advogados")
