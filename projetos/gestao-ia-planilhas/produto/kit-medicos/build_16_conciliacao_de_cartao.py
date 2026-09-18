#!/usr/bin/env python3
"""Planilha 16 do Kit de Gestão para Médicos: Conciliação de cartão e taxas (crédito, débito, Pix, antecipação). Gera 16-conciliacao-de-cartao.xlsx
Vendas = atendimentos particulares realizados pagos por Pix ou cartão desde 01/07/2026 (Agenda da 01). Taxas do exemplo: débito 1,5 %, crédito 3,2 %,
crédito parcelado 3,9 %, Pix 0 %. A saída "Taxas de cartão" do caixa (09) no fim de cada mês é o total desta planilha para as vendas do mês."""
from ssg import *
import dados
from openpyxl.chart import BarChart, Reference

N=2000; R0=5; RN=R0+N-1            # ≈ 100 pagamentos por mês no Pix e no cartão → mais de um ano por arquivo
TIPOS=["Pix","Cartão de débito","Cartão de crédito"]
NOME=f"{dados.CLINICA} (exemplo fictício)"
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Taxas e prazos da sua operadora (o contrato da maquininha diz; confira no extrato).",merge_to="F")
cfg["A4"]="Clínica"; cfg["B4"]=NOME
cfg["A5"]="Ano do painel"; cfg["B5"]=2026
cfg["A6"]="Mês do painel"; cfg["B6"]="Agosto"
cfg["A7"]="Número do mês"; cfg["B7"]="=MATCH(B6,$H$5:$H$16,0)"
cfg["A8"]="Data de referência (hoje)"; cfg["B8"]=dados.HOJE
cfg["A9"]="Preço da consulta particular (para a comparação)"; cfg["B9"]=dados.preco("Consulta","Particular")
for r in range(4,10): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"],center=True); inp(cfg["B6"],center=True); calc(cfg["B7"]); inp(cfg["B8"],DATA); inp(cfg["B9"],BRL0)
cfg["H4"]="Meses"; rotulo(cfg["H4"])
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=8,value=m).font=F(size=10,color=TINTA)
dv=lista("=Config!$H$5:$H$16",allow_blank=False); dv.add("B6"); cfg.add_data_validation(dv)
hdr(cfg,11,["Tipo","Taxa (%)","Cai na conta em (dias)","Observação"],height=30)
T0=12
taxas=[("Pix",dados.TAXAS["Pix"],0,"Pix na conta PJ: no exemplo, sem taxa (alguns bancos cobram por recebimento)."),
       ("Cartão de débito",dados.TAXAS["Cartão de débito"],dados.DIAS_CREDITO["Cartão de débito"],"Débito costuma cair no dia útil seguinte."),
       ("Cartão de crédito",dados.TAXAS["Cartão de crédito"],dados.DIAS_CREDITO["Cartão de crédito"],"Crédito à vista cai em 30 dias."),
       ("Cartão de crédito parcelado",dados.TAXAS["Cartão de crédito parcelado"],dados.DIAS_CREDITO["Cartão de crédito"],"Parcelado: cada parcela cai 30 dias depois da anterior; a taxa é maior.")]
for i,(t,tx,d,obs) in enumerate(taxas):
    r=T0+i; cfg.cell(row=r,column=1,value=t); calc(cfg.cell(row=r,column=1),center=False); inp(cfg.cell(row=r,column=2),"0.00%",center=True); cfg.cell(row=r,column=2).value=tx
    inp(cfg.cell(row=r,column=3),"0",center=True); cfg.cell(row=r,column=3).value=d; cfg.cell(row=r,column=4,value=obs); nota(cfg.cell(row=r,column=4))
cfg["A17"]="Antecipar o crédito? (Sim/Não)"; cfg["B17"]="Não"; cfg["A18"]="Taxa de antecipação (% ao mês)"; cfg["B18"]=0.018
rotulo(cfg["A17"]); rotulo(cfg["A18"]); inp(cfg["B17"],center=True); inp(cfg["B18"],"0.0%",center=True)
dvs=lista('"Sim,Não"'); dvs.add("B17"); cfg.add_data_validation(dvs)
cfg["D17"]="Com antecipação, o crédito cai em 1 dia e a operadora cobra a taxa de antecipação sobre o valor pelo prazo antecipado. No exemplo, a clínica não antecipa."; nota(cfg["D17"])
cfg["A20"]="As taxas do exemplo são ilustrativas. Pegue as suas no contrato da maquininha ou no extrato da operadora; elas mudam por bandeira e por volume."; nota(cfg["A20"])
widths(cfg,(44,14,20,70,3,3,3,12)); cfg.sheet_view.showGridLines=False
TX=f"Config!$B${T0}:$B${T0+3}"; DD=f"Config!$C${T0}:$C${T0+3}"; TT=f"Config!$A${T0}:$A${T0+3}"; ANT="Config!$B$17"; TXA="Config!$B$18"; HOJE="Config!$B$8"
# ---------- Vendas ----------
v=wb.create_sheet("Vendas")
titulo(v,"Vendas no cartão e no Pix","Uma linha por pagamento (copie da Agenda da planilha 01: atendimentos particulares realizados com Pix ou cartão). Amarelo: data, paciente, procedimento, tipo, parcelas, valor bruto e a conferência no extrato.",merge_to="O")
hdr(v,4,["Data da venda","Paciente","Procedimento","Tipo","Parcelas","Valor bruto (R$)","Parcelas já conferidas","Taxa (%)","Taxa (R$)","Valor líquido (R$)","Líquido por parcela (R$)","1ª parcela cai em","Última parcela cai em","Já previsto até hoje (R$)","Ainda vai cair (R$)","Mês","Ano","Situação"],height=44)
for r in range(R0,RN+1):
    for c in range(1,8): inp(v.cell(row=r,column=c),center=(c not in (2,3)))
    v.cell(row=r,column=1).number_format=DATA; v.cell(row=r,column=6).number_format=BRL0
    tipo=f'IF(AND(D{r}="Cartão de crédito",N(E{r})>1),"Cartão de crédito parcelado",D{r})'
    NP_=f'MAX(1,N(E{r}))'
    v.cell(row=r,column=8,value=f'=IF(D{r}="","",IFERROR(INDEX({TX},MATCH({tipo},{TT},0)),0)+IF(AND({ANT}="Sim",LEFT(D{r},17)="Cartão de crédito"),{TXA}*IFERROR(INDEX({DD},MATCH({tipo},{TT},0)),0)/30*MAX(1,N(E{r})),0))'); calc(v.cell(row=r,column=8),"0.00%")
    v.cell(row=r,column=9,value=f'=IF(OR(D{r}="",F{r}=""),"",ROUND(F{r}*H{r},2))'); calc(v.cell(row=r,column=9),BRL)
    v.cell(row=r,column=10,value=f'=IF(I{r}="","",F{r}-I{r})'); calc(v.cell(row=r,column=10),BRL)
    # NEF = liquidações FINANCEIRAS efetivas (coluna V, oculta). Com antecipação integral
    # o líquido inteiro cai em D+1: é UMA liquidação, embora a taxa use o n comercial de
    # parcelas. Sem essa separação, L e M mostravam 11/09 nos dois e K/N/O continuavam
    # dividindo por 2, dizendo que metade ainda ia cair (achado G-20 da auditoria de 18/09).
    NEF=f'MAX(1,N($V{r}))'
    v.cell(row=r,column=11,value=f'=IF(J{r}="","",J{r}/{NEF})'); calc(v.cell(row=r,column=11),BRL)
    v.cell(row=r,column=12,value=f'=IF(OR(D{r}="",A{r}=""),"",A{r}+IF(AND({ANT}="Sim",LEFT(D{r},17)="Cartão de crédito"),1,IFERROR(INDEX({DD},MATCH({tipo},{TT},0)),0)))'); calc(v.cell(row=r,column=12),DATA)
    # Com antecipação integral todo o líquido cai em D+1, então a última parcela é a
    # primeira. Antes só a 1ª ia para D+1 e as demais seguiam de 30 em 30, contradizendo
    # o texto da Config.
    v.cell(row=r,column=13,value=f'=IF(L{r}="","",L{r}+30*({NEF}-1))'); calc(v.cell(row=r,column=13),DATA)
    v.cell(row=r,column=14,value=f'=IF(OR(L{r}="",K{r}=""),"",K{r}*MIN({NEF},MAX(0,INT(({HOJE}-L{r})/30)+1)))'); calc(v.cell(row=r,column=14),BRL)
    v.cell(row=r,column=15,value=f'=IF(J{r}="","",J{r}-N(N{r}))'); calc(v.cell(row=r,column=15),BRL)
    v.cell(row=r,column=16,value=f'=IF(A{r}="","",MONTH(A{r}))'); calc(v.cell(row=r,column=16))
    v.cell(row=r,column=17,value=f'=IF(A{r}="","",YEAR(A{r}))'); calc(v.cell(row=r,column=17))
    # parcelas que já venceram até a data de referência
    venc=f'MIN({NEF},MAX(0,INT(({HOJE}-L{r})/30)+1))'
    v.cell(row=r,column=18,value=f'=IF(L{r}="","",IF(L{r}>{HOJE},"A cair",'
        f'IF(N(G{r})>={venc},IF(N(G{r})>={NEF},"Conferido","Conferido até aqui"),'
        f'"A conferir")))'); calc(v.cell(row=r,column=18))
    v.cell(row=r,column=19,value=f'=IF(R{r}="A conferir",({HOJE}-L{r})*1E+10+MIN(ROUND(N(F{r}),0),99999)*1E+5+({RN}+1-ROW()),0)'); v.cell(row=r,column=19).font=F(color=CINZA,size=9)
    # Pendência = só as parcelas VENCIDAS e ainda NÃO conferidas. Somar N (todo o
    # liquidado) fazia o painel pedir reconferência de dinheiro já conciliado: R$ 5.652,71
    # em vez de R$ 4.758,98 no exemplo, R$ 893,73 a mais em cinco linhas (regressão da
    # auditoria de 18/09). Quando todas venceram, usa J-K*G para fechar o centavo da última.
    v.cell(row=r,column=20,value=f'=IF(R{r}<>"A conferir",0,IF({venc}>={NEF},J{r}-K{r}*N(G{r}),K{r}*({venc}-N(G{r}))))'); v.cell(row=r,column=20).font=F(color=CINZA,size=9)
    v.cell(row=r,column=21,value=f'=IF(L{r}="",0,L{r})'); v.cell(row=r,column=21).font=F(color=CINZA,size=9)
    v.cell(row=r,column=22,value=f'=IF(L{r}="",0,IF(AND({ANT}="Sim",LEFT(D{r},17)="Cartão de crédito"),1,{NP_}))'); v.cell(row=r,column=22).font=F(color=CINZA,size=9)
    v.cell(row=r,column=23,value=f'=IF(K{r}="",0,K{r})'); v.cell(row=r,column=23).font=F(color=CINZA,size=9)
    # taxa de cada liquidação: o caixa (09) paga a taxa quando o dinheiro cai, não no dia da venda
    v.cell(row=r,column=24,value=f'=IF(OR(I{r}="",L{r}=""),0,I{r}/{NEF})'); v.cell(row=r,column=24).font=F(color=CINZA,size=9)
for col in "STUVWX": v.column_dimensions[col].hidden=True
dvs=[(lista('"'+",".join(TIPOS)+'"'),f"D{R0}:D{RN}"),(DataValidation(type="custom",formula1=f'=AND(N(G{R0})=INT(N(G{R0})),N(G{R0})>=0,N(G{R0})<=MAX(1,N($V{R0})))',allow_blank=True,showErrorMessage=True,errorTitle="Parcelas já conferidas",error="Digite um número inteiro de 0 até a quantidade de parcelas que caem na conta (com antecipação integral, 1)."),f"G{R0}:G{RN}"),(DataValidation(type="whole",operator="between",formula1="1",formula2="12",allow_blank=True,showErrorMessage=True),f"E{R0}:E{RN}"),
     (DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True),f"A{R0}:A{RN}"),(DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True,showErrorMessage=True),f"F{R0}:F{RN}")]
for dv,rng in dvs: dv.add(rng); v.add_data_validation(dv)
v.conditional_formatting.add(f"A{R0}:R{RN}", FormulaRule(formula=[f'$R{R0}="A conferir"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
v.conditional_formatting.add(f"A{R0}:R{RN}", FormulaRule(formula=[f'LEFT($R{R0},9)="Conferido"'], font=F(color=VERDE_T,size=10)))
v.conditional_formatting.add(f"A{R0}:R{RN}", FormulaRule(formula=[f'$R{R0}="A cair"'], fill=fill(LAVANDA)))
v.cell(row=RN+2,column=1,value="Vermelho: a previsão da 1ª parcela passou e ninguém conferiu no extrato (ou não caiu). Lilás: ainda vai cair. Verde: conferido. Parcelado: a planilha divide o líquido pelo número de parcelas e cada uma cai de 30 em 30 dias a partir da 1ª — \"Já previsto até hoje\" soma só as parcelas que já venceram e \"Ainda vai cair\" é o resto. Por isso uma venda em 2× aparece com metade do valor em cada dia, e não com o valor inteiro no primeiro.").font=F(size=9,color=LILAS)
v.merge_cells(start_row=RN+2,start_column=1,end_row=RN+2,end_column=18); v.cell(row=RN+2,column=1).alignment=Alignment(wrap_text=True,vertical="top"); v.row_dimensions[RN+2].height=30
v.cell(row=RN+4,column=1,value=f"Esta aba tem {N} linhas ({R0} a {RN}): com cerca de 100 pagamentos por mês no Pix e no cartão, passa de um ano. Para estender, desproteja a aba, copie a última linha para baixo e ajuste o número final nas fórmulas do Painel; ou comece um arquivo por ano, junto com a agenda (01).").font=F(size=9,color=LILAS)
v.cell(row=RN+3,column=1,value="No exemplo, as vendas vêm da Agenda da 01 (01/07 a 11/09/2026); conferidas as que tinham previsão até 09/09. O caixa (09) registra o valor bruto no dia da venda e as taxas do mês numa saída única no fim do mês.").font=F(size=9,color=LILAS)
widths(v,(12,26,20,17,9,13,12,9,11,13,13,13,14,14,13,6,6,16)); v.freeze_panes="C5"; v.sheet_view.showGridLines=False; v.auto_filter.ref=f"A4:R{RN}"
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Conciliação de cartão e taxas · "&Config!$B$6&" de "&Config!$B$5',"Nada para digitar aqui. Escolha o mês em Config; tudo vem de Vendas. Taxas por mês da venda; a receber por previsão na conta.",merge_to="L")
D0=18   # primeira linha do quadro "dia a dia" (o A7 e a auxiliar N já dependem dela)
M="Config!$B$7"; Y="Config!$B$5"
V=lambda col: f"Vendas!${col}${R0}:${col}${RN}"
MES=f"{V('P')},{M},{V('Q')},{Y}"
kpi(p,4,1,"Vendas no mês (bruto)",f"=SUMIFS({V('F')},{MES})",LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Taxas no mês",f"=SUMIFS({V('I')},{MES})",VERM,VERM_T,fmt=BRL)
kpi(p,4,5,"Taxa média",'=IF(A5=0,"",C5/A5)',VERM,VERM_T,fmt="0.00%")
kpi(p,4,7,"Líquido no mês",'=A5-C5',VERDE,VERDE_T,fmt=BRL0)
kpi(p,4,9,"Ainda vai cair (todas as vendas)",f'=SUM({V("O")})',SOL,UVA,fmt=BRL0)
kpi(p,4,11,"A conferir",f'=SUM({V("T")})',VERM,VERM_T,fmt=BRL0)
# Taxa por DATA DE LIQUIDAÇÃO: é quando a operadora desconta. O A7 antigo mandava lançar
# no caixa o C5 (taxa das vendas do mês); em agosto isso dava R$ 484,12 contra R$ 681,61
# efetivamente descontados, R$ 197,49 de despesa a menos e saldo inflado (achado de 18/09).
p["N4"]="Taxas liquidadas no mês (auxiliar)"; p["N4"].font=F(size=9,color=CINZA)
p["N5"]=f"=SUM(N{D0+2}:N{D0+32})"; p["N5"].font=F(size=9,color=CINZA); p["N5"].number_format=BRL
p["A7"]='="As taxas das vendas do mês equivalem a "&FIXED(IF(Config!$B$9=0,0,C5/Config!$B$9),1)&" consultas particulares. Para o caixa (09), a saída \'Taxas de cartão\' do mês é "&"R$ "&FIXED($N$5,2)&": é a taxa das liquidações que caíram neste mês, e não a das vendas feitas nele."'; nota(p["A7"]); p.merge_cells("A7:L7")
p["A9"]="Por tipo de pagamento no mês"; p["A9"].font=F(bold=True,size=13,color=UVA)
hdr(p,10,["Tipo","Vendas","Bruto (R$)","Taxas (R$)","Taxa média","Líquido (R$)","% do bruto","Barra"]); p.merge_cells("H10:J10")
# crédito à vista = todo crédito menos o parcelado (parcelas em branco contam como à vista)
CRED=f'{V("D")},"Cartão de crédito"'; PARC=f'{V("D")},"Cartão de crédito",{V("E")},">1"'
linhas=[("Pix",f'{V("D")},"Pix"'),("Cartão de débito",f'{V("D")},"Cartão de débito"'),("Cartão de crédito à vista",None),("Cartão de crédito parcelado",PARC)]
for i,(nm,crit) in enumerate(linhas):
    r=11+i
    p.cell(row=r,column=1,value=nm); calc(p.cell(row=r,column=1),center=False)
    if crit is None:
        p.cell(row=r,column=2,value=f'=COUNTIFS({CRED},{MES})-COUNTIFS({PARC},{MES})'); calc(p.cell(row=r,column=2))
        p.cell(row=r,column=3,value=f'=SUMIFS({V("F")},{CRED},{MES})-SUMIFS({V("F")},{PARC},{MES})'); calc(p.cell(row=r,column=3),BRL0)
        p.cell(row=r,column=4,value=f'=SUMIFS({V("I")},{CRED},{MES})-SUMIFS({V("I")},{PARC},{MES})'); calc(p.cell(row=r,column=4),BRL)
    else:
        p.cell(row=r,column=2,value=f'=COUNTIFS({crit},{MES})'); calc(p.cell(row=r,column=2))
        p.cell(row=r,column=3,value=f'=SUMIFS({V("F")},{crit},{MES})'); calc(p.cell(row=r,column=3),BRL0)
        p.cell(row=r,column=4,value=f'=SUMIFS({V("I")},{crit},{MES})'); calc(p.cell(row=r,column=4),BRL)
    p.cell(row=r,column=5,value=f'=IF(C{r}=0,"",D{r}/C{r})'); calc(p.cell(row=r,column=5),"0.00%")
    p.cell(row=r,column=6,value=f'=C{r}-D{r}'); calc(p.cell(row=r,column=6),BRL0)
    p.cell(row=r,column=7,value=f'=IF($A$5=0,"",C{r}/$A$5)'); calc(p.cell(row=r,column=7),PCT)
    p.cell(row=r,column=8,value=f'=IF(G{r}="","",REPT("█",ROUND(G{r}*30,0)))'); p.cell(row=r,column=8).font=F(size=10,color=LILAS); p.cell(row=r,column=8).border=borda; p.merge_cells(start_row=r,start_column=8,end_row=r,end_column=10)
p.cell(row=15,column=1,value="Total"); p.cell(row=15,column=2,value="=SUM(B11:B14)"); p.cell(row=15,column=3,value="=SUM(C11:C14)"); p.cell(row=15,column=4,value="=SUM(D11:D14)"); p.cell(row=15,column=6,value="=SUM(F11:F14)")
for c in (1,2,3,4,6): p.cell(row=15,column=c).font=F(bold=True,color=UVA,size=10); p.cell(row=15,column=c).border=borda
p.cell(row=15,column=3).number_format=BRL0; p.cell(row=15,column=4).number_format=BRL; p.cell(row=15,column=6).number_format=BRL0
p.cell(row=16,column=1,value="Parcelado custa mais e demora mais. Se o parcelado pesa, vale oferecer desconto no Pix em vez de absorver a taxa; a decisão é da clínica.").font=F(size=9,color=LILAS)
# por semana do mês (dia a dia)
p.cell(row=D0,column=1,value="Dia a dia do mês: vendas, taxas e previsão de crédito").font=F(bold=True,size=13,color=UVA)
hdr(p,D0+1,["Dia","Data","Vendas","Bruto (R$)","Taxas (R$)","Líquido (R$)","Cai na conta neste dia (R$)","Conferido?"],height=32)
for i in range(31):
    r=D0+2+i
    p.cell(row=r,column=1,value=i+1); calc(p.cell(row=r,column=1))
    p.cell(row=r,column=2,value=f'=IF({i+1}>DAY(DATE({Y},{M}+1,0)),"",DATE({Y},{M},{i+1}))'); calc(p.cell(row=r,column=2),DATA)
    p.cell(row=r,column=3,value=f'=IF(B{r}="","",COUNTIFS({V("A")},B{r}))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF(B{r}="","",SUMIFS({V("F")},{V("A")},B{r}))'); calc(p.cell(row=r,column=4),BRL0)
    p.cell(row=r,column=5,value=f'=IF(B{r}="","",SUMIFS({V("I")},{V("A")},B{r}))'); calc(p.cell(row=r,column=5),BRL)
    p.cell(row=r,column=6,value=f'=IF(B{r}="","",D{r}-E{r})'); calc(p.cell(row=r,column=6),BRL0)
    p.cell(row=r,column=7,value=f'=IF(B{r}="","",SUMPRODUCT(({V("U")}>0)*({V("U")}<=B{r})*(MOD(B{r}-{V("U")},30)=0)*((B{r}-{V("U")})/30<{V("V")})*{V("W")}))'); calc(p.cell(row=r,column=7),BRL0)
    p.cell(row=r,column=8,value=f'=IF(OR(B{r}="",G{r}=0),"",IF(COUNTIFS({V("L")},B{r},{V("R")},"A conferir")>0,"Falta conferir",IF(B{r}>{HOJE},"A cair","Conferido")))'); calc(p.cell(row=r,column=8))
    # auxiliar oculta: taxa das liquidações deste dia. Mesmo predicado da coluna G, com a
    # taxa por liquidação (Vendas!X) no lugar do líquido.
    p.cell(row=r,column=14,value=f'=IF(B{r}="",0,SUMPRODUCT(({V("U")}>0)*({V("U")}<=B{r})*(MOD(B{r}-{V("U")},30)=0)*((B{r}-{V("U")})/30<{V("V")})*{V("X")}))'); p.cell(row=r,column=14).font=F(color=CINZA,size=9)
p.conditional_formatting.add(f"A{D0+2}:H{D0+32}", FormulaRule(formula=[f'$C{D0+2}=0'], font=F(color="B0A6C4",size=10)))
p.conditional_formatting.add(f"H{D0+2}:H{D0+32}", FormulaRule(formula=[f'H{D0+2}="Falta conferir"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"H{D0+2}:H{D0+32}", FormulaRule(formula=[f'H{D0+2}="Conferido"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
p.cell(row=D0+33,column=1,value="\"Cai na conta neste dia\" soma as parcelas que caem nesse dia (inclusive as de vendas de meses anteriores e as parcelas 2, 3… de vendas parceladas): é o número para bater com o extrato da conta. Uma venda em 2× aparece metade num dia e metade 30 dias depois.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=D0+33,start_column=1,end_row=D0+33,end_column=12); p.cell(row=D0+33,column=1).alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[D0+33].height=28
# a conferir
C0=D0+36
p.cell(row=C0,column=1,value="Falta conferir no extrato (previsão vencida)").font=F(bold=True,size=13,color=UVA)
hdr(p,C0+1,["#","Data da venda","Paciente","Procedimento","Tipo","Parcelas","Bruto (R$)","Líquido já previsto (R$)","1ª parcela caía em","Dias desde a previsão"],height=32)
# S = pontuação de pendência (dias vencidos, valor e linha como desempate). A coluna O
# é "ainda vai cair", dinheiro futuro: ordenar por ela priorizava o que não precisa de
# conferência, e por repetir valores fazia a mesma venda aparecer várias vezes.
KEY=V("S")
for k in range(1,11):
    r=C0+1+k; m=f'MATCH(LARGE({KEY},{k}),{KEY},0)'; g=f'LARGE({KEY},{k})>0'
    p.cell(row=r,column=1,value=k); calc(p.cell(row=r,column=1))
    for col,src in zip((2,3,4,5,6,7,8,9),("A","B","C","D","E","F","N","L")):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},INDEX({V(src)},{m}),""),"")'); calc(p.cell(row=r,column=col),center=(col not in (3,4)))
    p.cell(row=r,column=2).number_format=DATA; p.cell(row=r,column=9).number_format=DATA; p.cell(row=r,column=7).number_format=BRL0; p.cell(row=r,column=8).number_format=BRL
    p.cell(row=r,column=10,value=f'=IF(I{r}="","",{HOJE}-I{r})'); calc(p.cell(row=r,column=10),"0")
p.cell(row=C0+12,column=1,value="Venda que não caiu na conta na data prevista: confira o extrato da operadora (estorno, chargeback, erro de bandeira) antes de cobrar o paciente. A planilha aponta; a conferência é sua.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=C0+12,start_column=1,end_row=C0+12,end_column=12)
bc=BarChart(); bc.type="col"; bc.grouping="stacked"; bc.overlap=100; bc.height=6.5; bc.width=13; bc.title="Líquido × taxas por tipo (R$)"; bc.style=2
bc.add_data(Reference(p,min_col=6,min_row=10,max_row=14),titles_from_data=True); bc.add_data(Reference(p,min_col=4,min_row=10,max_row=14),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=11,max_row=14))
bc.series[0].graphicalProperties.solidFill=UVA; bc.series[1].graphicalProperties.solidFill="C0392B"; bc.legend.position="b"; bc.y_axis.majorGridlines=None
p.add_chart(bc,"K9")
widths(p,(24,13,12,13,13,13,16,14,13,12,12,12)); p.column_dimensions["N"].hidden=True; p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Exemplo ----------
vendas=[r for r in dados.AGENDA if r["situacao"]=="Realizado" and r["pagador"]=="Particular" and r["forma"] in TIPOS]
assert len(vendas)<=N
LIM=dados.SEXTA-__import__("datetime").timedelta(days=2)
for i,r_ in enumerate(vendas):
    r=R0+i
    v.cell(row=r,column=1,value=r_["data"]); v.cell(row=r,column=2,value=r_["paciente"]); v.cell(row=r,column=3,value=r_["procedimento"]); v.cell(row=r,column=4,value=r_["forma"])
    if r_["parcelas"]: v.cell(row=r,column=5,value=r_["parcelas"])
    v.cell(row=r,column=6,value=r_["valor"])
    prev=r_["data"]+__import__("datetime").timedelta(days=dados.DIAS_CREDITO.get(r_["forma"],0))
    # quantas parcelas já venceram até o corte do exemplo: é isso que a recepção teria
    # conferido no extrato até aqui
    if prev<=LIM:
        _np=r_["parcelas"] or 1
        _venc=min(_np, max(0,(LIM-prev).days//30+1))
        if _venc: v.cell(row=r,column=7,value=_venc)
print(len(vendas),"vendas no exemplo")
como_usar(wb,"Conciliação de cartão e taxas",[
 ("O que esta planilha faz","Cada pagamento no cartão ou no Pix com a taxa da operadora, o valor líquido e o dia em que cai na conta. Mostra quanto as taxas comem no mês (e a quantas consultas equivalem), o que ainda vai cair, o que já deveria ter caído e não foi conferido, e o dia a dia para bater com o extrato."),
 ("Passo 1","Em Config, digite as taxas e os prazos da sua operadora (contrato da maquininha ou extrato), se antecipa o crédito e o preço da consulta particular (só para a comparação)."),
 ("Passo 2","Em Vendas, uma linha por pagamento: data, paciente, procedimento, tipo, parcelas e valor bruto (copie da Agenda da 01, filtrando os particulares pagos com Pix ou cartão). A cada quinzena, escreva em \"Parcelas já conferidas\" quantas parcelas daquela venda você já achou no extrato: 1 para Pix, débito e crédito à vista; no parcelado vá somando conforme cada parcela cai. Assim a venda volta para \"A conferir\" quando a parcela seguinte vencer, em vez de ficar conferida para sempre depois da primeira."),
 ("Passo 3","Em Painel, escolha o mês em Config: vendas, taxas, líquido, por tipo, dia a dia e a lista \"Falta conferir\". No fechamento do mês, lance como saída \"Taxas de cartão\" no caixa (09) o valor que a nota abaixo dos quadros indica: a taxa das liquidações que caíram no mês, não a das vendas feitas nele."),
 ("Rotina","É uma planilha QUINZENAL, fora dos 30 minutos semanais da planilha 03: a cada 15 dias, 10 minutos para conferir o extrato da operadora contra \"Cai na conta neste dia\" e marcar as conferidas. No fechamento do mês, lance no caixa (09) a taxa das liquidações do mês, que a nota abaixo dos quadros mostra pronta. Uma vez por semestre: comparar a taxa média com outra operadora."),
 ("Limite e como estender","A aba Vendas tem 2.000 linhas (5 a 2004): mais de um ano com cerca de 100 pagamentos por mês. Perto do fim, desproteja a aba, copie a última linha para baixo e ajuste o número final nas fórmulas do Painel, ou comece um arquivo por ano."),
 ("Ligação com as outras planilhas","O caixa (09) registra o bruto na data em que cai na conta, usando as datas desta planilha; a taxa do mês é a saída do fim do mês em que o dinheiro caiu. Por isso a taxa desta tela (vendas de agosto) e a do caixa (recebimentos de agosto) são números diferentes de propósito. O resultado mensal (18) mostra as taxas como despesa variável. No exemplo o Painel está em agosto (mês fechado); setembro está em andamento."),
 ("Com a IA","Copie \"Por tipo de pagamento\" e use o prompt \"Caixa 09 · A taxa da maquininha está comendo a margem?\" da biblioteca do kit para decidir entre absorver a taxa, oferecer desconto no Pix ou trocar de operadora."),
])
proteger(wb); salvar(wb,"16-conciliacao-de-cartao.xlsx","Conciliação de cartão e taxas · Kit de Gestão para Médicos")
