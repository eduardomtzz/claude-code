#!/usr/bin/env python3
"""Planilha 12 do Kit de Gestão para Advogados: Reserva de três meses e metas de caixa. Gera 12-reserva-e-metas-de-caixa.xlsx
Exemplo alimentado pelos totais mensais da planilha 09 (build_09_caixa_do_escritorio)."""
from ssg import *
import dados
from openpyxl.chart import LineChart, Reference
import build_09_caixa_do_escritorio as caixa

NPROJ=24; NM=3
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Custo fixo, saldo e reserva vêm do Painel da planilha 09; o resto é decisão do escritório.",merge_to="H")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Data de referência"; cfg["B5"]="=TODAY()"
cfg["A6"]="Mês de início da projeção"; cfg["B6"]="Outubro"
cfg["A7"]="Ano de início da projeção"; cfg["B7"]=2026
cfg["A8"]="Meta de reserva (meses de custo fixo)"; cfg["B8"]=3
cfg["A9"]="Aporte mensal planejado para a reserva"; cfg["B9"]=3000
for r in range(4,10): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); calc(cfg["B5"],DATA); inp(cfg["B6"],center=True); inp(cfg["B7"],center=True); inp(cfg["B8"],"0",center=True); inp(cfg["B9"],BRL)
cfg["D8"]="Três meses de custo fixo é a meta usual para um escritório pequeno; ajuste conforme a variação das entradas."; nota(cfg["D8"])
cfg["H4"]="Meses"; rotulo(cfg["H4"])
for i,m_ in enumerate(MESES): cfg.cell(row=5+i,column=8,value=m_).font=F(size=10,color=TINTA)
dv=lista("=Config!$H$5:$H$16"); dv.add("B6"); cfg.add_data_validation(dv)
cfg["A11"]="Custo fixo dos últimos 3 meses (com pró-labore fixo)"; rotulo(cfg["A11"])
hdr(cfg,12,["Mês","Custo fixo do mês"])
for i in range(NM):
    inp(cfg.cell(row=13+i,column=1),center=True); inp(cfg.cell(row=13+i,column=2),BRL)
cfg["A16"]="Custo fixo médio"; cfg["B16"]="=IFERROR(AVERAGE(B13:B15),0)"
rotulo(cfg["A16"]); calc(cfg["B16"],BRL); cfg["B16"].font=F(bold=True,color=UVA,size=10)
cfg["D13"]="Copie de \"Para onde foi o dinheiro\" (Painel da planilha 09): aluguel, contador, sistemas, equipe, pró-labore fixo e o resto que se repete todo mês. Impostos e custas ficam fora."; nota(cfg["D13"]); cfg["D13"].alignment=Alignment(wrap_text=True,vertical="top"); cfg.merge_cells("D13:F15")
cfg["A18"]="Situação hoje"; rotulo(cfg["A18"])
cfg["A19"]="Saldo em caixa do escritório (conta corrente)"; cfg["B19"]=40795
cfg["A20"]="Compromissos já lançados e ainda não pagos"; cfg["B20"]=14733
cfg["A21"]="Caixa livre"; cfg["B21"]="=B19-B20"
cfg["A22"]="Reserva já guardada (conta separada)"; cfg["B22"]=12000
for r in (19,20,21,22): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B19"],BRL); inp(cfg["B20"],BRL); calc(cfg["B21"],BRL); inp(cfg["B22"],BRL)
cfg["D19"]="Saldo acumulado e A pagar do Painel da planilha 09."; nota(cfg["D19"])
cfg["D22"]="O que já está numa conta separada só para a reserva. Se ainda não separou, deixe 0."; nota(cfg["D22"])
cfg["A24"]="Metas de caixa do trimestre (3)"; rotulo(cfg["A24"])
hdr(cfg,25,["Meta","Valor alvo","Valor atual","Prazo"])
for i in range(3):
    r=26+i; inp(cfg.cell(row=r,column=1)); inp(cfg.cell(row=r,column=2),BRL); inp(cfg.cell(row=r,column=3),BRL); inp(cfg.cell(row=r,column=4),DATA,center=True)
dvd=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True); dvd.add("D26:D28"); cfg.add_data_validation(dvd)
cfg["A30"]="Metas que se medem em reais e crescem até o alvo (reserva, recebimentos, provisão separada). Atualize o valor atual toda sexta. Datas de prazo do exemplo são relativas a hoje."; nota(cfg["A30"])
widths(cfg,(44,18,3,30,12,12,3,12)); cfg.sheet_view.showGridLines=False
# exemplo
tot=caixa.totais_mensais()
for i,m in enumerate((6,7,8)): cfg.cell(row=13+i,column=1,value=MESES[m-1]); cfg.cell(row=13+i,column=2,value=tot[m]["fixo"])
rec_tri=sum(tot[m]["ent"]-tot[m]["devol"] for m in (7,8,9))
metas=[("Reserva com 1 mês de custo fixo",tot[8]["fixo"],12000,dados.prazo_formula(108)),
       ("Receber R$ 65.000 no trimestre",65000,rec_tri,dados.prazo_formula(16)),
       ("Conta de provisão de impostos com o saldo da planilha 10",11750,9400,dados.prazo_formula(16))]
for i,row in enumerate(metas):
    for c,v in enumerate(row,start=1): cfg.cell(row=26+i,column=c,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!B4&" · Reserva e metas de caixa · "&TEXT(DAY(Config!B5),"00")&"/"&TEXT(MONTH(Config!B5),"00")&"/"&YEAR(Config!B5)',"Nada para digitar aqui. Meta, custo fixo, saldo e aporte vêm de Config.",merge_to="J")
META="Config!$B$8*Config!$B$16"; MED="Config!$B$16"; RES="Config!$B$22"; APORTE="Config!$B$9"; HOJE="Config!$B$5"
P0=10; PN=P0+NPROJ-1
kpi(p,4,1,"Meta de reserva",f"={META}",LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Reserva hoje",f"={RES}",VERDE,VERDE_T,fmt=BRL0)
kpi(p,4,5,"Falta guardar",f"=MAX(0,A5-C5)",VERM,VERM_T,fmt=BRL0)
kpi(p,4,7,"Meses de custo fixo cobertos",f"=IF({MED}=0,0,C5/{MED})",SOL,UVA,fmt='0.0')
kpi(p,4,9,"Meta prevista para",f'=IF(C5>=A5,"Já atingida",IFERROR(INDEX(A{P0}:A{PN},MATCH("Meta atingida",F{P0}:F{PN},0)),"Depois de 24 meses"))',LAVANDA,UVA,fmt="General")
p["I5"].font=F(size=13,bold=True,color=UVA)
p["A7"]="Semáforo"; rotulo(p["A7"])
p["B7"]=f'=IF(G5<1,"Vermelho: menos de 1 mês de custo fixo guardado",IF(G5<Config!$B$8,"Amarelo: abaixo da meta",IF(G5<Config!$B$8+1,"Verde: meta atingida","Verde: acima da meta")))'
p["B7"].font=F(bold=True,size=11,color=UVA); p.merge_cells("B7:F7")
p.conditional_formatting.add("B7", FormulaRule(formula=['LEFT(B7,8)="Vermelho"'], fill=fill(VERM), font=F(color=VERM_T,size=11,bold=True)))
p.conditional_formatting.add("B7", FormulaRule(formula=['LEFT(B7,7)="Amarelo"'], fill=fill(AMARELO), font=F(color=UVA,size=11,bold=True)))
p.conditional_formatting.add("B7", FormulaRule(formula=['LEFT(B7,5)="Verde"'], fill=fill(VERDE), font=F(color=VERDE_T,size=11,bold=True)))
p["G7"]=f'="Contando o caixa livre (R$ "&ROUND(Config!$B$21,0)&"): "&ROUND(IF({MED}=0,0,(C5+Config!$B$21)/{MED}),1)&" meses"'; nota(p["G7"]); p.merge_cells("G7:J7")
p.cell(row=P0-2,column=1,value="Projeção da reserva, mês a mês").font=F(bold=True,size=13,color=UVA)
hdr(p,P0-1,["Mês","Saldo no início","Aporte","Saldo no fim","% da meta","Atingiu?","Barra","Meta"]); p.merge_cells(start_row=P0-1,start_column=7,end_row=P0-1,end_column=9)
M0="MATCH(Config!$B$6,Config!$H$5:$H$16,0)"
for i in range(NPROJ):
    r=P0+i
    p.cell(row=r,column=1,value=f'=INDEX(Config!$H$5:$H$16,MOD({M0}+{i}-1,12)+1)&"/"&(Config!$B$7+INT(({M0}+{i}-1)/12))'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f"={RES}" if i==0 else f"=D{r-1}"); calc(p.cell(row=r,column=2),BRL0)
    p.cell(row=r,column=3,value=f"={APORTE}"); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f"=B{r}+C{r}"); calc(p.cell(row=r,column=4),BRL0); p.cell(row=r,column=4).font=F(bold=True,color=UVA,size=10)
    p.cell(row=r,column=5,value=f'=IF($A$5=0,"",D{r}/$A$5)'); calc(p.cell(row=r,column=5),PCT)
    p.cell(row=r,column=6,value=f'=IF(D{r}>=$A$5,IF(B{r}<$A$5,"Meta atingida","Acima da meta"),"")'); calc(p.cell(row=r,column=6))
    p.cell(row=r,column=7,value=f'=IF(E{r}="","",REPT("█",ROUND(MIN(1,E{r})*30,0)))'); p.cell(row=r,column=7).font=F(size=10,color=LILAS); p.cell(row=r,column=7).border=borda
    p.merge_cells(start_row=r,start_column=7,end_row=r,end_column=9)
    p.cell(row=r,column=10,value=f"=$A$5"); calc(p.cell(row=r,column=10),BRL0); p.cell(row=r,column=10).font=F(size=9,color=CINZA)
p.conditional_formatting.add(f"A{P0}:F{PN}", FormulaRule(formula=[f'$F{P0}="Meta atingida"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10,bold=True)))
p.cell(row=PN+1,column=1,value="Aporte igual todo mês, sem rendimento. Quando a reserva bater a meta, decida com o sócio o que fazer com o aporte: manter, reduzir ou virar distribuição."); nota(p.cell(row=PN+1,column=1))
lc=LineChart(); lc.height=7.5; lc.width=18; lc.title="Reserva projetada × meta"; lc.style=2
lc.add_data(Reference(p,min_col=4,min_row=P0-1,max_row=PN),titles_from_data=True); lc.add_data(Reference(p,min_col=10,min_row=P0-1,max_row=PN),titles_from_data=True)
lc.set_categories(Reference(p,min_col=1,min_row=P0,max_row=PN))
lc.series[0].graphicalProperties.line.solidFill=UVA; lc.series[0].graphicalProperties.line.width=28000; lc.series[1].graphicalProperties.line.solidFill=SOL; lc.series[1].graphicalProperties.line.dashStyle="dash"
lc.legend.position="b"; lc.y_axis.majorGridlines=None
p.add_chart(lc,f"K{P0-2}")
# metas do trimestre
G0=PN+4
p.cell(row=G0-2,column=1,value="Metas de caixa do trimestre").font=F(bold=True,size=13,color=UVA)
hdr(p,G0-1,["Meta","Valor alvo","Valor atual","Progresso","Barra","Prazo","Dias restantes","Situação"])
for i in range(3):
    r=G0+i; src=f"Config!$A${26+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",Config!$B${26+i})'); calc(p.cell(row=r,column=2),BRL0)
    p.cell(row=r,column=3,value=f'=IF({src}="","",Config!$C${26+i})'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f'=IF(OR({src}="",B{r}=0),"",MIN(1,C{r}/B{r}))'); calc(p.cell(row=r,column=4),PCT)
    p.cell(row=r,column=5,value=f'=IF(D{r}="","",REPT("█",ROUND(D{r}*20,0)))'); p.cell(row=r,column=5).font=F(size=10,color=LILAS); p.cell(row=r,column=5).border=borda
    p.cell(row=r,column=6,value=f'=IF(OR({src}="",Config!$D${26+i}=""),"",Config!$D${26+i})'); calc(p.cell(row=r,column=6),DATA)
    p.cell(row=r,column=7,value=f'=IF(OR({src}="",F{r}="",H{r}="Concluída"),"",F{r}-{HOJE})'); calc(p.cell(row=r,column=7),"0")
    p.cell(row=r,column=8,value=f'=IF({src}="","",IF(AND(B{r}>0,C{r}>=B{r}),"Concluída",IF(AND(F{r}<>"",F{r}<{HOJE}),"Prazo vencido","Em andamento")))'); calc(p.cell(row=r,column=8))
    p.row_dimensions[r].height=30; p.cell(row=r,column=1).alignment=Alignment(wrap_text=True,vertical="center")
p.conditional_formatting.add(f"H{G0}:H{G0+2}", FormulaRule(formula=[f'H{G0}="Concluída"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10,bold=True)))
p.conditional_formatting.add(f"H{G0}:H{G0+2}", FormulaRule(formula=[f'H{G0}="Prazo vencido"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"H{G0}:H{G0+2}", FormulaRule(formula=[f'H{G0}="Em andamento"'], fill=fill(LAVANDA)))
p.cell(row=G0+3,column=1,value="Atualize o valor atual das metas em Config toda sexta. Prazo vencido não é fracasso: é sinal para renegociar a meta ou o aporte com o sócio."); nota(p.cell(row=G0+3,column=1))
widths(p,(34,15,13,15,11,15,13,10,10,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
como_usar(wb,"Reserva de três meses e metas de caixa",[
 ("O que esta planilha faz","Calcula a reserva que o escritório precisa (meses de custo fixo), mostra quanto já tem, quantos meses cobre hoje, quando chega à meta com o aporte planejado (mês a mês, com gráfico) e acompanha três metas de caixa do trimestre com barra de progresso."),
 ("Passo 1","Em Config, digite a meta em meses de custo fixo (3 é um bom começo), o custo fixo dos últimos 3 meses com pró-labore (copie do Painel da planilha 09), o saldo em caixa, os compromissos ainda não pagos, o que já está guardado numa conta separada e o aporte mensal que cabe."),
 ("Passo 2","Ainda em Config, escreva as três metas de caixa do trimestre: nome, valor alvo, valor atual e prazo. Metas que se medem em reais e crescem até o alvo."),
 ("Passo 3","Em Painel: meta, reserva, falta, meses cobertos, semáforo e o mês em que a meta é atingida. A projeção mostra 24 meses; a linha verde é o mês da virada."),
 ("Rotina","Toda sexta, 5 minutos: atualizar o valor atual das metas. No fechamento do mês: transferir o aporte para a conta da reserva e atualizar o saldo e o custo fixo em Config."),
 ("Com a IA","Copie o Painel e use o prompt \"Explicar o mês ao sócio\" da biblioteca do kit para decidir aporte e metas do próximo trimestre com o sócio."),
])
proteger(wb); salvar(wb,"12-reserva-e-metas-de-caixa.xlsx","Reserva de três meses e metas de caixa · Kit de Gestão para Advogados")
