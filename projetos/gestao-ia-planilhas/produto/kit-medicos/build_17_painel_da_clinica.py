#!/usr/bin/env python3
"""Planilha 17 do Kit de Gestão para Médicos: Painel da Clínica. Gera 17-painel-da-clinica.xlsx
Uma tela com agenda, faltas, caixa, convênios, parcelas e orçamentos. Os números vêm da aba Dados (copiados toda sexta das
planilhas 01, 02, 09, 13, 14 e 15); o Histórico guarda uma linha por mês.
Exemplo: sexta 11/09/2026 (setembro em andamento), números copiados exatamente dos painéis de origem; Histórico jan–ago (dados.HISTORICO)."""
from ssg import *
import dados
from openpyxl.chart import BarChart, LineChart, Reference

AG=dados.resumo_agenda(9); E=dados.estado(dados.HOJE); T9=dados.TOTAIS[9]; HIST=dados.HISTORICO; F9=dados.faltas(9)
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche.",merge_to="E")
cfg["A4"]="Clínica"; cfg["B4"]=f"{dados.CLINICA} (exemplo fictício)"
cfg["A5"]="Mês do painel"; cfg["B5"]="Setembro"
cfg["A6"]="Ano"; cfg["B6"]=2026
cfg["A7"]="Data de referência (hoje)"; cfg["B7"]="=TODAY()"
cfg["A8"]="Número do mês"; cfg["B8"]="=MATCH(B5,$D$5:$D$16,0)"
cfg["A9"]="Mês anterior"; cfg["B9"]='=IF(B8>1,INDEX($D$5:$D$16,B8-1),"")'
cfg["A10"]="Mês do painel já fechou? (Sim/Não)"; cfg["B10"]="Não"
for r in range(4,11): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"]); inp(cfg["B6"]); inp(cfg["B7"],DATA); calc(cfg["B8"]); calc(cfg["B9"]); inp(cfg["B10"])
dvf=lista('"Sim,Não"',allow_blank=False); dvf.add("B10"); cfg.add_data_validation(dvf)
cfg["D4"]="Meses"; rotulo(cfg["D4"])
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=4,value=m).font=F(size=10,color=TINTA)
dv=lista("=Config!$D$5:$D$16",allow_blank=False); dv.add("B5"); cfg.add_data_validation(dv)
cfg["A11"]="Use a mesma planilha o ano inteiro: troque o mês aqui e, no fim de cada mês, copie a linha de Dados para o Histórico. Enquanto o mês não fecha, agenda e caixa são parciais e o Painel não os compara com o mês anterior (marque Sim no fechamento)."; nota(cfg["A11"])
cfg["A12"]="Esta planilha só guarda totais: são 12 linhas de Dados e 12 de Histórico por ano, e nada envelhece. As planilhas de lançamento (01, 02, 09, 13, 14, 15, 16) têm um número fixo de linhas — cada \"Como usar\" diz quantas e como estender ou virar o ano."; nota(cfg["A12"])
widths(cfg,(28,40,4,14)); cfg.sheet_view.showGridLines=False

# ---------- Dados ----------
d=wb.create_sheet("Dados")
titulo(d,"Dados da semana","Toda sexta, copie os totais das outras planilhas do kit para as células amarelas. Limites e metas também são seus. O resto é calculado.",merge_to="G")
hdr(d,4,["Indicador","Valor desta sexta","Limite ou meta","Sentido","Copie de (planilha do kit)","Situação"])
R0=5
r1=lambda x: round(x,4)
LINHAS=[
 ("ocup","Ocupação da agenda no mês (horas atendidas ÷ disponíveis)",r1(AG["ocupacao"]),0.75,"Maior é melhor","01 · Agenda e ocupação (Painel: Ocupação)",PCT),
 ("atend","Horas atendidas no mês",round(AG["atendidas"],1),None,"","01 · Agenda e ocupação (Painel: Horas atendidas)","#,##0.0"),
 ("vazias","Horas vazias no mês",round(AG["vazias"],1),None,"","01 · Agenda e ocupação (Painel: Horas vazias)","#,##0.0"),
 ("falta","Taxa de falta no mês (faltas ÷ (faltas + realizados))",r1(F9[2]),0.06,"Menor é melhor","02 · Faltas e retornos (Painel: Taxa de falta)","0.0%"),
 ("retorno","Pacientes na lista de retorno",dados.lista_retorno(),8,"Menor é melhor","02 · Faltas e retornos (Painel: Na lista de retorno)","#,##0"),
 ("entrou","Entrou no mês (recebimentos)",T9["ent"],None,"","09 · Caixa da clínica (Painel: Entrou no mês)",BRL0),
 ("saiu","Saiu no mês (tudo o que saiu do caixa)",T9["sai_total"],None,"","09 · Caixa da clínica (Painel: Saiu no mês)",BRL0),
 ("sobrou","Sobrou no mês","=IF(OR(B10=\"\",B11=\"\"),\"\",B10-B11)",None,"","calculado aqui",BRL0),
 ("conv","Convênio a receber (lotes enviados e não pagos)",E["convenio_a_receber"],None,"","13 · Convênios a receber (Painel: A receber)",BRL0),
 ("atras","Convênio atrasado (previsão vencida)",E["convenio_atrasado"],0,"Menor é melhor","13 · Convênios a receber (Painel: Atrasado)",BRL0),
 ("glosa","Glosa no ano (glosa ÷ (pago + glosa))",r1(dados.glosa_ano()),0.04,"Menor é melhor","13 · Convênios a receber (Painel: Glosa no ano %)","0.0%"),
 ("venc","Vencido (parcelas a prazo em atraso)",E["vencido"],4000,"Menor é melhor","14 · Parcelas e inadimplência (Painel: Vencido)",BRL0),
 ("inad","Inadimplência a prazo (vencido ÷ (pago + vencido))",r1(E["inadimplencia"]),0.08,"Menor é melhor","14 · Parcelas e inadimplência (Painel: Inadimplência)","0.0%"),
 ("orcn","Orçamentos em aberto (quantidade)",E["orcamentos_n"],None,"","15 · Orçamentos (Painel: Apresentado + Em análise)","#,##0"),
 ("orcv","Orçamentos em aberto (valor)",E["orcamentos_valor"],None,"","15 · Orçamentos (Painel: Em aberto)",BRL0),
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
    d.cell(row=r,column=6,value=(f'=IF(OR(B{r}="",C{r}=""),"Informativo",IF(D{r}="Menor é melhor",IF(B{r}<C{r},"No alvo",IF(B{r}<=C{r}*1.1+(C{r}=0)*0.0001,"Perto","Fora")),'
                                 f'IF(B{r}>C{r},"No alvo",IF(B{r}>=C{r}*0.9,"Perto","Fora"))))')); calc(d.cell(row=r,column=6))
dvs=lista('"Maior é melhor,Menor é melhor"'); dvs.add(f"D{R0}:D{RN}"); d.add_data_validation(dvs)
for cor,txt,fnt in ((VERDE,"No alvo",VERDE_T),(AMARELO,"Perto","7A5200"),(VERM,"Fora",VERM_T)):
    d.conditional_formatting.add(f"F{R0}:F{RN}", FormulaRule(formula=[f'F{R0}="{txt}"'], fill=fill(cor), font=F(color=fnt,size=10,bold=(txt=="Fora"))))
d.cell(row=RN+2,column=1,value="Linha sem limite fica \"Informativo\". \"Perto\" é o limite exato ou até 10% além dele. Inadimplência = vencido ÷ (pago + vencido), a mesma conta da planilha 14. Convênio a receber é o que foi enviado e ainda está no prazo: informativo; o problema é o atrasado. Orçamentos em aberto também são informativos: pouco orçamento pendente pode ser bom (fechou tudo) ou ruim (a recepção parou de apresentar) — quem diz é a taxa de aprovação da planilha 15, não o valor parado. Os valores desta sexta valem para o mês escolhido em Config; no fim do mês, copie a coluna B para a linha do mês em Histórico.").font=F(size=9,color=LILAS)
d.merge_cells(start_row=RN+2,start_column=1,end_row=RN+2,end_column=6)
d.cell(row=RN+3,column=1,value="As planilhas indicadas em \"Copie de\" são as do próprio kit. Se ainda não usa alguma, deixe a linha em branco: o painel mostra \"—\". No exemplo (sexta 11/09/2026) agenda e caixa são do mês em andamento: a comparação com agosto só aparece no fechamento.").font=F(size=9,color=LILAS)
d.merge_cells(start_row=RN+3,start_column=1,end_row=RN+3,end_column=6)
for r in (RN+2,RN+3): d.cell(row=r,column=1).alignment=Alignment(wrap_text=True,vertical="top"); d.row_dimensions[r].height=30
widths(d,(52,16,14,16,52,12)); d.freeze_panes="B5"; d.sheet_view.showGridLines=False

# ---------- Histórico ----------
h=wb.create_sheet("Histórico")
titulo(h,"Histórico mensal","No fim de cada mês, copie os valores da aba Dados para a linha do mês. Colunas brancas são calculadas; deixe em branco os meses que ainda não aconteceram.",merge_to="P")
HCOLS=[("ocup","Ocupação",PCT),("atend","Horas atendidas","#,##0.0"),("vazias","Horas vazias","#,##0.0"),("falta","Taxa de falta","0.0%"),("retorno","Lista de retorno","#,##0"),
       ("entrou","Entrou",BRL0),("saiu","Saiu",BRL0),("sobrou","Sobrou",BRL0),("conv","Convênio a receber",BRL0),("atras","Convênio atrasado",BRL0),("glosa","Glosa no mês (%)","0.0%"),
       ("venc","Vencido",BRL0),("inad","Inadimplência","0.0%"),("orcn","Orçamentos abertos","#,##0"),("orcv","Valor dos orçamentos",BRL0)]
HCOL={k:2+i for i,(k,*_) in enumerate(HCOLS)}
hdr(h,4,["Mês"]+[t for _,t,_ in HCOLS],height=32)
def hv(k,m):
    x=HIST[m]
    return {"ocup":x["ocupacao"],"atend":x["atendidas"],"vazias":(dados.horas_disponiveis(m,ate=min(dados.fim_mes(m),dados.HOJE-__import__("datetime").timedelta(days=1)))-x["atendidas"]) if x["atendidas"] is not None else None,
            "falta":x["taxa_falta"],"retorno":x["retorno"],"entrou":x["entrou"],"saiu":x["saiu"],"conv":x["convenio"],"atras":x["atrasado"],"glosa":x["glosa_pct"],
            "venc":x["vencido"],"inad":x["inadimplencia"],"orcn":x["orcamentos_n"],"orcv":x["orcamentos_valor"]}[k]
for m in range(12):
    r=5+m
    h.cell(row=r,column=1,value=MESES[m]); rotulo(h.cell(row=r,column=1),bold=False); h.cell(row=r,column=1).border=borda
    for k,t,fmt in HCOLS:
        col=HCOL[k]; cell=h.cell(row=r,column=col)
        if k=="sobrou": cell.value=f'=IF(OR({L(HCOL["entrou"])}{r}="",{L(HCOL["saiu"])}{r}=""),"",{L(HCOL["entrou"])}{r}-{L(HCOL["saiu"])}{r})'; calc(cell,fmt)
        else:
            inp(cell,fmt,center=True)
            if m<9:
                v=hv(k,m+1)
                if v is not None: cell.value=round(v,4) if isinstance(v,float) else v
h.conditional_formatting.add("A5:A16", FormulaRule(formula=['ROW()-4=Config!$B$8'], fill=fill(SOL), font=F(color=UVA,size=10,bold=True)))
h.cell(row=18,column=1,value="A linha do mês escolhido em Config fica destacada. Setembro repete os valores da aba Dados (mês em andamento, até 11/09). Entrou e Saiu = Painel mensal da planilha 09 (caixa real). Agenda: o registro na planilha 01 começou em junho; antes fica em branco. Orçamentos: o funil (15) começou em junho. Convênio, vencido e inadimplência: o que a clínica copiou no fim de cada mês. Glosa no mês = dos lotes pagos naquele mês (no Dados, o acumulado do ano).").font=F(size=9,color=LILAS)
h.merge_cells("A18:P18"); h["A18"].alignment=Alignment(wrap_text=True,vertical="top"); h.row_dimensions[18].height=44
def serie_cols(k1,k2): return Reference(h,min_col=HCOL[k1],max_col=HCOL[k2],min_row=4,max_row=16)
cats=Reference(h,min_col=1,max_col=1,min_row=5,max_row=16)
bc=BarChart(); bc.type="col"; bc.grouping="clustered"; bc.title="Caixa do mês: entrou, saiu, sobrou"; bc.height=8; bc.width=22; bc.style=2
bc.add_data(serie_cols("entrou","sobrou"),titles_from_data=True); bc.set_categories(cats)
for sr,cor in zip(bc.series,(UVA,LILAS,SOL)): sr.graphicalProperties.solidFill=cor; sr.graphicalProperties.line.solidFill=cor
bc.y_axis.majorGridlines=None; bc.legend.position="b"; bc.y_axis.number_format='"R$" #,##0'; bc.dispBlanksAs="gap"
h.add_chart(bc,"A20")
lc=LineChart(); lc.title="Ocupação e taxa de falta"; lc.height=8; lc.width=22; lc.style=2
lc.add_data(serie_cols("ocup","ocup"),titles_from_data=True); lc.add_data(serie_cols("falta","falta"),titles_from_data=True); lc.set_categories(cats)
lc.series[0].graphicalProperties.line.solidFill=UVA; lc.series[0].graphicalProperties.line.width=28000
lc.series[1].graphicalProperties.line.solidFill="C0392B"; lc.series[1].graphicalProperties.line.width=28000
for sr in lc.series: sr.smooth=False
lc.y_axis.majorGridlines=None; lc.legend.position="b"; lc.dispBlanksAs="gap"; lc.y_axis.number_format='0%'
h.add_chart(lc,"A38")
widths(h,[12]+[12]*15); h.freeze_panes="B5"; h.sheet_view.showGridLines=False

# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
p["A1"]='=Config!B4&" · Painel da clínica · "&Config!B5&" de "&Config!B6'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:J1")
p["A2"]='="Nada para digitar aqui. Os números vêm da aba Dados (atualizada toda sexta) e o mês anterior vem do Histórico. Referência: "&TEXT(Config!B7,"dd/mm/yyyy")&"."'; nota(p["A2"]); p.merge_cells("A2:J2")
def dv_(k): return f"Dados!$B${ROW[k]}"
def val(k): return f'=IF({dv_(k)}="","—",{dv_(k)})'
tiles=[(4,[("ocup","Ocupação da agenda",PCT),("atend","Horas atendidas","#,##0.0"),("vazias","Horas vazias","#,##0.0"),("falta","Taxa de falta","0.0%"),("retorno","Lista de retorno","#,##0")]),
       (7,[("entrou","Entrou no mês",BRL0),("saiu","Saiu no mês",BRL0),("sobrou","Sobrou no mês",BRL0),("conv","Convênio a receber",BRL0),("atras","Convênio atrasado",BRL0)]),
       (10,[("glosa","Glosa no ano","0.0%"),("venc","Vencido (a prazo)",BRL0),("inad","Inadimplência a prazo","0.0%"),("orcn","Orçamentos abertos","#,##0"),("orcv","Valor dos orçamentos",BRL0)])]
for row,items in tiles:
    for j,(k,rot,fmt) in enumerate(items):
        col=1+2*j; kpi(p,row,col,rot,val(k),LAVANDA,UVA,fmt=fmt)
        ref=f"Dados!$F${ROW[k]}"; cell=f"{L(col)}{row+1}"
        p.conditional_formatting.add(cell, FormulaRule(formula=[f'{ref}="Fora"'], fill=fill(VERM), font=F(size=16,bold=True,color=VERM_T)))
        p.conditional_formatting.add(cell, FormulaRule(formula=[f'{ref}="Perto"'], fill=fill(AMARELO), font=F(size=16,bold=True,color="7A5200")))
        p.conditional_formatting.add(cell, FormulaRule(formula=[f'{ref}="No alvo"'], fill=fill(VERDE), font=F(size=16,bold=True,color=VERDE_T)))
p["A13"]="Cores dos cartões: verde no alvo · amarelo perto do limite · vermelho fora · lilás informativo"; nota(p["A13"]); p.merge_cells("A13:J13")
p["A14"]="Semáforos da semana e comparação com o mês anterior"; p["A14"].font=F(bold=True,size=13,color=UVA); p.merge_cells("A14:G14")
hdr(p,15,["Indicador","","Esta sexta","Limite ou meta","Situação","Mês anterior (Histórico)","Variação"]); p.merge_cells("A15:B15")
T0=16
for i,(k,rot,val_,lim,sent,fonte,fmt) in enumerate(LINHAS):
    r=T0+i; s=ROW[k]
    p.cell(row=r,column=1,value=f"=Dados!A{s}"); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2)
    p.cell(row=r,column=3,value=f'=IF(Dados!B{s}="","—",Dados!B{s})'); calc(p.cell(row=r,column=3),fmt)
    p.cell(row=r,column=4,value=f'=IF(Dados!C{s}="","—",Dados!C{s})'); calc(p.cell(row=r,column=4),fmt)
    p.cell(row=r,column=5,value=f"=Dados!F{s}"); calc(p.cell(row=r,column=5))
    hc=L(HCOL[k])
    p.cell(row=r,column=6,value=f'=IF(Config!$B$8<=1,"—",IF(INDEX(Histórico!${hc}$5:${hc}$16,Config!$B$8-1)="","—",INDEX(Histórico!${hc}$5:${hc}$16,Config!$B$8-1)))'); calc(p.cell(row=r,column=6),fmt)
    parcial='IF(Config!$B$10<>"Sim","no fechamento",' if k in ("ocup","atend","vazias","falta","entrou","saiu","sobrou") else '('
    if fmt in (PCT,"0.0%"):
        p.cell(row=r,column=7,value=f'={parcial}IF(OR(C{r}="—",F{r}="—"),"—",(C{r}-F{r})*100))'); calc(p.cell(row=r,column=7),'+0.0" p.p.";-0.0" p.p.";0.0" p.p."')
    else:
        p.cell(row=r,column=7,value=f'={parcial}IF(OR(C{r}="—",F{r}="—",F{r}=0),"—",(C{r}-F{r})/ABS(F{r})))'); calc(p.cell(row=r,column=7),"+0.0%;-0.0%;0.0%")
TN=T0+len(LINHAS)-1
for cor,txt,fnt in ((VERDE,"No alvo",VERDE_T),(AMARELO,"Perto","7A5200"),(VERM,"Fora",VERM_T)):
    p.conditional_formatting.add(f"E{T0}:E{TN}", FormulaRule(formula=[f'E{T0}="{txt}"'], fill=fill(cor), font=F(color=fnt,size=10,bold=(txt=="Fora"))))
p.cell(row=TN+2,column=1,value="Fora do alvo primeiro: convênio atrasado, vencido e lista de retorno pedem ação na segunda-feira (planilhas 13, 14 e 02). Variação de indicadores em % é em pontos percentuais (p.p.). No meio do mês, agenda e caixa ainda estão parciais: a variação deles só aparece quando Config diz que o mês fechou. Glosa no ano compara com a glosa do mês anterior no Histórico. A planilha avisa; a decisão é da clínica.").font=F(size=9,color=LILAS)
p.cell(row=TN+2,column=1).alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[TN+2].height=42
p.merge_cells(start_row=TN+2,start_column=1,end_row=TN+2,end_column=10)
p.cell(row=TN+3,column=1,value='Para transformar esta tela em texto para o sócio ou o contador, use a planilha 20 · Resumo do mês e o prompt "Painel 01 · Explicar o mês ao sócio".').font=F(size=9,color=LILAS)
p.merge_cells(start_row=TN+3,start_column=1,end_row=TN+3,end_column=10)
widths(p,(22,22,14,14,14,18,12,12,12,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False

como_usar(wb,"Painel da Clínica",[
 ("O que esta planilha faz","Reúne em uma tela os números que já estão nas outras planilhas do kit: ocupação da agenda, horas atendidas e vazias, taxa de falta e lista de retorno, o que entrou, saiu e sobrou, convênio a receber e atrasado, glosa, vencido e inadimplência a prazo, orçamentos abertos. Cada número ganha um semáforo contra o limite que você definir e a comparação com o mês anterior."),
 ("Toda sexta (3 minutos)","Abra as planilhas 01 (agenda), 02 (faltas), 09 (caixa), 13 (convênios), 14 (parcelas) e 15 (orçamentos), copie os totais do Painel de cada uma para a coluna B da aba Dados. Pronto: o Painel se refaz. No exemplo, a sexta é 11/09/2026 e cada número é exatamente o que está no Painel da planilha de origem."),
 ("Limites e metas","Na aba Dados, coluna C, escreva o limite de cada indicador (ex.: ocupação de 75 %, taxa de falta de 6 %, glosa de 4 %, inadimplência de 8 %) e diga se maior ou menor é melhor. Linha sem limite fica informativa — é o caso de convênio a receber e dos orçamentos em aberto, que sozinhos não dizem se a clínica vai bem ou mal."),
 ("Fim do mês","Copie a coluna B da aba Dados para a linha do mês em Histórico. Os gráficos de caixa e de agenda usam essa aba; o Painel busca ali o mês anterior."),
 ("Config","Escolha o mês do painel e mantenha a data de referência em =HOJE(). O título do Painel se ajusta."),
 ("Com a IA","O Painel é a tela da rotina de sexta. Para o texto do mês (sócio, contador), use a planilha 20 · Resumo do mês e o prompt \"Painel 01 · Explicar o mês ao sócio\" da biblioteca."),
])
proteger(wb); salvar(wb,"17-painel-da-clinica.xlsx","Painel da Clínica · Kit de Gestão para Médicos")
