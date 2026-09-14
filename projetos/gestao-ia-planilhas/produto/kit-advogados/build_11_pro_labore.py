#!/usr/bin/env python3
"""Planilha 11 do Kit de Gestão para Advogados: Pró-labore e separação pessoa física × escritório. Gera 11-pro-labore.xlsx
Exemplo alimentado pelos lançamentos da planilha 09 (build_09_caixa_do_escritorio)."""
from ssg import *
import dados

NS=6; N=400; R0=5; RN=R0+N-1
TIPOS=["Pró-labore","Retirada extra","Despesa pessoal paga pelo escritório","Devolução ao escritório","Distribuição de lucro"]
TRIMS=["1º trimestre","2º trimestre","3º trimestre","4º trimestre"]
SOCIOS=[(n,v) for n,p,v,_ in dados.PESSOAS if p.startswith("Sóci")]
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Sócios, pró-labore combinado e a regra de distribuição de lucro ficam aqui.",merge_to="J")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Ano"; cfg["B5"]=2026
cfg["A6"]="Mês do painel"; cfg["B6"]="Setembro"
cfg["A7"]="Número do mês"; cfg["B7"]="=MATCH(B6,$H$5:$H$16,0)"
cfg["A8"]="Trimestre do painel"; cfg["B8"]="=ROUNDUP(B7/3,0)"
cfg["A9"]="Parte do lucro do trimestre distribuída aos sócios"; cfg["B9"]=dados.DISTRIB
cfg["A10"]="Lucro mínimo do trimestre para haver distribuição"; cfg["B10"]=dados.LUCRO_MINIMO
for r in range(4,11): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"],center=True); inp(cfg["B6"],center=True); calc(cfg["B7"]); calc(cfg["B8"]); inp(cfg["B9"],PCT,center=True); inp(cfg["B10"],BRL)
cfg["D9"]="Regra combinada entre os sócios: o restante do lucro fica no escritório (reserva e provisões). Trimestre com lucro abaixo do mínimo não distribui."
cfg["D10"]="A distribuição é calculada só para trimestres já fechados (os três meses lançados em Resultado mensal e anteriores ao mês do painel)."
for r in (9,10): nota(cfg.cell(row=r,column=4)); cfg.cell(row=r,column=4).alignment=Alignment(wrap_text=True,vertical="top"); cfg.merge_cells(start_row=r,start_column=4,end_row=r,end_column=6); cfg.row_dimensions[r].height=32
cfg["H4"]="Meses"; cfg["J4"]="Tipos de movimento"; rotulo(cfg["H4"]); rotulo(cfg["J4"])
for i,m_ in enumerate(MESES): cfg.cell(row=5+i,column=8,value=m_).font=F(size=10,color=TINTA)
for i,t in enumerate(TIPOS): cfg.cell(row=5+i,column=10,value=t).font=F(size=10,color=TINTA)
dv=lista("=Config!$H$5:$H$16"); dv.add("B6"); cfg.add_data_validation(dv)
cfg["A12"]="Sócios (até 6)"; rotulo(cfg["A12"])
hdr(cfg,13,["Sócio","Participação no lucro","Pró-labore fixo mensal"])
S0=14; SN=S0+NS-1
for i in range(NS):
    r=S0+i; inp(cfg.cell(row=r,column=1)); inp(cfg.cell(row=r,column=2),PCT,center=True); inp(cfg.cell(row=r,column=3),BRL)
cfg.cell(row=SN+1,column=1,value="Total"); cfg.cell(row=SN+1,column=2,value=f"=SUM(B{S0}:B{SN})"); cfg.cell(row=SN+1,column=3,value=f"=SUM(C{S0}:C{SN})")
for c in (1,2,3): cfg.cell(row=SN+1,column=c).font=F(bold=True,color=UVA,size=10); cfg.cell(row=SN+1,column=c).border=borda
cfg.cell(row=SN+1,column=2).number_format=PCT; cfg.cell(row=SN+1,column=3).number_format=BRL; cfg.cell(row=SN+1,column=2).alignment=Alignment(horizontal="center")
cfg.cell(row=SN+1,column=4,value=f'=IF(ROUND(B{SN+1},4)=1,"","A participação deve somar 100 %")'); cfg.cell(row=SN+1,column=4).font=F(color=VERM_T,size=10,bold=True)
cfg.cell(row=SN+3,column=1,value="Preencha os sócios de cima para baixo, sem pular linha: a lista suspensa de Retiradas para na última linha preenchida."); nota(cfg.cell(row=SN+3,column=1))
cfg.cell(row=SN+4,column=1,value="Pró-labore fixo: o valor combinado que cada sócio retira todo mês. Retirada extra e despesa pessoal paga pelo escritório são o que passou do combinado."); nota(cfg.cell(row=SN+4,column=1))
for i,(n_,v) in enumerate(SOCIOS):
    cfg.cell(row=S0+i,column=1,value=n_); cfg.cell(row=S0+i,column=2,value=1/len(SOCIOS)); cfg.cell(row=S0+i,column=3,value=v)
widths(cfg,(44,20,22,3,3,3,3,12,3,34)); cfg.sheet_view.showGridLines=False
LSOC=f"OFFSET(Config!$A${S0},0,0,MAX(1,COUNTA(Config!$A${S0}:$A${SN})),1)"
# ---------- Resultado mensal ----------
rm=wb.create_sheet("Resultado mensal")
titulo(rm,"Resultado mensal do escritório","Amarelo: entradas e saídas de cada mês, sem nada dos sócios (copie do Painel da planilha 09). O resto é calculado.",merge_to="H")
hdr(rm,4,["Mês","Entradas recebidas","Saídas do escritório (sem sócios)","Pró-labore fixo combinado","Resultado após pró-labore","Trimestre"],height=40)
for i in range(12):
    r=5+i
    rm.cell(row=r,column=1,value=MESES[i]); calc(rm.cell(row=r,column=1),center=False)
    inp(rm.cell(row=r,column=2),BRL); inp(rm.cell(row=r,column=3),BRL)
    rm.cell(row=r,column=4,value=f'=IF(AND(B{r}="",C{r}=""),0,Config!$C${SN+1})'); calc(rm.cell(row=r,column=4),BRL)
    rm.cell(row=r,column=5,value=f"=B{r}-C{r}-D{r}"); calc(rm.cell(row=r,column=5),BRL)
    rm.cell(row=r,column=6,value=TRIMS[i//3]); calc(rm.cell(row=r,column=6))
rm.conditional_formatting.add("E5:E16", FormulaRule(formula=['E5<0'], font=F(color="C8402E",size=10,bold=True)))
rm["A18"]="Entradas = Entrou no mês (Painel da planilha 09) menos devoluções dos sócios (Outras entradas). Saídas sem sócios = Saiu no mês menos pró-labore, retiradas extras, distribuição de lucro e despesas pessoais dos sócios. Meses não fechados ficam em branco (setembro: até 11/09)."; nota(rm["A18"])
widths(rm,(14,18,22,20,20,14)); rm.sheet_view.showGridLines=False
tot=dados.TOTAIS
for m in range(1,10):
    rm.cell(row=4+m,column=2,value=tot[m]["ent_sem_devol"]); rm.cell(row=4+m,column=3,value=tot[m]["sai"]-tot[m]["pessoal"])
# ---------- Retiradas ----------
re_=wb.create_sheet("Retiradas")
titulo(re_,"Retiradas e movimentos sócio × escritório","Uma linha por movimento entre a conta do escritório e a pessoa física de cada sócio. Preencha o amarelo; mês e ano são calculados.",merge_to="H")
hdr(re_,4,["Data","Sócio","Tipo","Descrição","Valor","Trimestre de referência (só distribuição)","Mês","Ano"],height=40)
for r in range(R0,RN+1):
    for c in range(1,7): inp(re_.cell(row=r,column=c))
    re_.cell(row=r,column=1).number_format=DATA; re_.cell(row=r,column=5).number_format=BRL
    for c in (1,2,3,6): re_.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    re_.cell(row=r,column=7,value=f'=IF(A{r}="","",MONTH(A{r}))'); calc(re_.cell(row=r,column=7))
    re_.cell(row=r,column=8,value=f'=IF(A{r}="","",YEAR(A{r}))'); calc(re_.cell(row=r,column=8))
for dv,rng_ in [(lista(f"={LSOC}",strict=False),f"B{R0}:B{RN}"),(lista("=Config!$J$5:$J$9"),f"C{R0}:C{RN}"),
                (lista('"'+",".join(TRIMS)+'"'),f"F{R0}:F{RN}"),(DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True),f"A{R0}:A{RN}"),
                (DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True),f"E{R0}:E{RN}")]:
    dv.add(rng_); re_.add_data_validation(dv)
re_.conditional_formatting.add(f"A{R0}:H{RN}", FormulaRule(formula=[f'$C{R0}="Despesa pessoal paga pelo escritório"'], fill=fill(VERM)))
re_.conditional_formatting.add(f"A{R0}:H{RN}", FormulaRule(formula=[f'$C{R0}="Devolução ao escritório"'], font=F(color=VERDE_T,size=10)))
widths(re_,(12,20,34,44,14,22,6,7)); re_.freeze_panes="A5"; re_.sheet_view.showGridLines=False; re_.auto_filter.ref=f"A4:H{RN}"
# exemplo: movimentos dos sócios extraídos dos lançamentos da planilha 09
pref={"Pró-labore ·":"Pró-labore","Retirada extra ·":"Retirada extra","Despesa pessoal ·":"Despesa pessoal paga pelo escritório","Devolução de despesa pessoal ·":"Devolução ao escritório","Distribuição de lucro ·":"Distribuição de lucro"}
rows=[]
for d,t,c,cli,caso,desc,v,f,pago in dados.LANCAMENTOS:
    if pago!="Sim": continue
    for pr,tipo in pref.items():
        if desc.startswith(pr):
            soc=next(n for n,_ in SOCIOS if n in desc)
            partes=[x.strip() for x in desc.split("·")]; ref=""
            if tipo=="Distribuição de lucro": ref=partes[1]; txt="Distribuição de lucro · "+ref
            elif tipo=="Pró-labore": txt="Pró-labore de "+MESES[d.month-1].lower()
            elif tipo=="Devolução ao escritório": txt="Devolução da despesa pessoal (plano de saúde)"
            else: txt=partes[-1].replace(" (a acertar)","").capitalize()
            rows.append((d,soc,tipo,txt,v,ref))
for i,row in enumerate(rows):
    for c,v in enumerate(row,start=1): re_.cell(row=R0+i,column=c,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!B4&" · Pró-labore e retiradas · "&Config!B6&" de "&Config!B5',"Nada para digitar aqui. Sócios e regra vêm de Config; movimentos, de Retiradas; lucro, de Resultado mensal.",merge_to="J")
M="Config!$B$7"; Y="Config!$B$5"; Q="Config!$B$8"
RB=f"Retiradas!$B${R0}:$B${RN}"; RC=f"Retiradas!$C${R0}:$C${RN}"; RE=f"Retiradas!$E${R0}:$E${RN}"; RF=f"Retiradas!$F${R0}:$F${RN}"; RG=f"Retiradas!$G${R0}:$G${RN}"; RH=f"Retiradas!$H${R0}:$H${RN}"
def smes(tipo,soc): return f'SUMIFS({RE},{RB},{soc},{RC},"{tipo}",{RG},{M},{RH},{Y})'
def sano(tipo,soc): return f'SUMIFS({RE},{RB},{soc},{RC},"{tipo}",{RG},"<="&{M},{RH},{Y})'
# trimestres (calculados antes para os KPIs referenciarem)
TQ=32
p.cell(row=TQ-2,column=1,value="Lucro e distribuição por trimestre").font=F(bold=True,size=13,color=UVA)
hdr(p,TQ-1,["Trimestre","Entradas","Saídas (sem sócios)","Pró-labore fixo","Resultado após pró-labore","Fechado?","Distribuível aos sócios","Já distribuído","Falta distribuir"],height=40)
for q in range(4):
    r=TQ+q; a=5+q*3; b=7+q*3
    p.cell(row=r,column=1,value=TRIMS[q]); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f"=SUM('Resultado mensal'!B{a}:B{b})"); p.cell(row=r,column=3,value=f"=SUM('Resultado mensal'!C{a}:C{b})")
    p.cell(row=r,column=4,value=f"=SUM('Resultado mensal'!D{a}:D{b})"); p.cell(row=r,column=5,value=f"=SUM('Resultado mensal'!E{a}:E{b})")
    p.cell(row=r,column=6,value=f'=IF({M}>{3*(q+1)},"Sim","Em andamento")')
    p.cell(row=r,column=7,value=f'=IF(AND(F{r}="Sim",E{r}>=Config!$B$10),E{r}*Config!$B$9,0)')
    p.cell(row=r,column=8,value=f'=SUMIFS({RE},{RC},"Distribuição de lucro",{RF},A{r},{RH},{Y})')
    p.cell(row=r,column=9,value=f"=IF(ABS(G{r}-H{r})<1,0,G{r}-H{r})")
    for c in (2,3,4,5,7,8,9): calc(p.cell(row=r,column=c),BRL0)
    calc(p.cell(row=r,column=6)); p.cell(row=r,column=7).font=F(bold=True,color=UVA,size=10)
p.conditional_formatting.add(f"E{TQ}:E{TQ+3}", FormulaRule(formula=[f'E{TQ}<0'], font=F(color="C8402E",size=10,bold=True)))
p.conditional_formatting.add(f"I{TQ}:I{TQ+3}", FormulaRule(formula=[f'I{TQ}>0'], fill=fill(AMARELO), font=F(color=UVA,size=10,bold=True)))
p.conditional_formatting.add(f"I{TQ}:I{TQ+3}", FormulaRule(formula=[f'I{TQ}<0'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"A{TQ}:I{TQ+3}", FormulaRule(formula=[f'ROW()-{TQ}+1={Q}'], fill=fill(LAVANDA)))
p.cell(row=TQ+4,column=1,value="Falta distribuir em amarelo: lucro do trimestre fechado ainda não pago aos sócios. Em vermelho: distribuiu mais do que a regra permite (ou o trimestre ainda não fechou). Diferenças de centavos são ignoradas."); nota(p.cell(row=TQ+4,column=1))
GDIST=f"SUM($G${TQ}:$G${TQ+3})"
# KPIs
kpi(p,4,1,"Pró-labore combinado (mês)",f"=Config!$C${SN+1}",LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Retirado pelos sócios (mês)",f"=SUM(H9:H{8+NS})",SOL,UVA,fmt=BRL0)
kpi(p,4,5,"Fora do combinado (mês)",f"=SUM(I9:I{8+NS})",VERM,VERM_T,fmt=BRL0)
kpi(p,4,7,"A acertar com o escritório (ano)",f"=SUM(G{20}:G{19+NS})",VERM,VERM_T,fmt=BRL0)
kpi(p,4,9,"Distribuição a pagar (ano)",f"=SUM(J{20}:J{19+NS})",VERDE,VERDE_T,fmt=BRL0)
# no mês por sócio
p["A7"]="No mês, por sócio"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Sócio","Pró-labore combinado","Pró-labore pago","Retiradas extras","Despesas pessoais pelo escritório","Devoluções","Distribuição de lucro","Total retirado","Fora do combinado","Situação"],height=40)
for i in range(NS):
    r=9+i; src=f"Config!$A${S0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",Config!$C${S0+i})')
    p.cell(row=r,column=3,value=f'=IF({src}="","",{smes("Pró-labore",src)})')
    p.cell(row=r,column=4,value=f'=IF({src}="","",{smes("Retirada extra",src)})')
    p.cell(row=r,column=5,value=f'=IF({src}="","",{smes("Despesa pessoal paga pelo escritório",src)})')
    p.cell(row=r,column=6,value=f'=IF({src}="","",{smes("Devolução ao escritório",src)})')
    p.cell(row=r,column=7,value=f'=IF({src}="","",{smes("Distribuição de lucro",src)})')
    p.cell(row=r,column=8,value=f'=IF({src}="","",C{r}+D{r}+E{r}-F{r}+G{r})')
    p.cell(row=r,column=9,value=f'=IF({src}="","",D{r}+E{r}-F{r})')
    p.cell(row=r,column=10,value=f'=IF({src}="","",IF(I{r}>0,"Acima do combinado",IF(C{r}<B{r},"Pró-labore ainda não pago por completo","Conforme o combinado")))')
    for c in range(2,10): calc(p.cell(row=r,column=c),BRL0)
    calc(p.cell(row=r,column=10)); p.cell(row=r,column=8).font=F(bold=True,color=UVA,size=10)
p.conditional_formatting.add(f"J9:J{8+NS}", FormulaRule(formula=['J9="Acima do combinado"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"J9:J{8+NS}", FormulaRule(formula=['J9="Conforme o combinado"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
p.conditional_formatting.add(f"J9:J{8+NS}", FormulaRule(formula=['J9="Pró-labore ainda não pago por completo"'], fill=fill(AMARELO)))
p.cell(row=9+NS,column=1,value="Fora do combinado = retiradas extras + despesas pessoais pagas pelo escritório − devoluções. Distribuição de lucro segue a regra de Config e não conta como \"fora\"."); nota(p.cell(row=9+NS,column=1))
# no ano por sócio
p["A18"]="No ano, até o mês do painel, por sócio"; p["A18"].font=F(bold=True,size=13,color=UVA)
hdr(p,19,["Sócio","Pró-labore combinado até o mês","Pró-labore pago","Retiradas extras","Despesas pessoais pelo escritório","Devoluções","A acertar com o escritório","Distribuição devida (trimestres fechados)","Distribuição recebida","Distribuição a receber"],height=52)
for i in range(NS):
    r=20+i; src=f"Config!$A${S0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",Config!$C${S0+i}*{M})')
    p.cell(row=r,column=3,value=f'=IF({src}="","",{sano("Pró-labore",src)})')
    p.cell(row=r,column=4,value=f'=IF({src}="","",{sano("Retirada extra",src)})')
    p.cell(row=r,column=5,value=f'=IF({src}="","",{sano("Despesa pessoal paga pelo escritório",src)})')
    p.cell(row=r,column=6,value=f'=IF({src}="","",{sano("Devolução ao escritório",src)})')
    p.cell(row=r,column=7,value=f'=IF({src}="","",D{r}+E{r}-F{r})')
    p.cell(row=r,column=8,value=f'=IF({src}="","",{GDIST}*Config!$B${S0+i})')
    p.cell(row=r,column=9,value=f'=IF({src}="","",{sano("Distribuição de lucro",src)})')
    p.cell(row=r,column=10,value=f'=IF({src}="","",IF(ABS(H{r}-I{r})<1,0,H{r}-I{r}))')
    for c in range(2,11): calc(p.cell(row=r,column=c),BRL0)
    p.cell(row=r,column=7).font=F(bold=True,color=UVA,size=10); p.cell(row=r,column=10).font=F(bold=True,color=UVA,size=10)
p.conditional_formatting.add(f"G20:G{19+NS}", FormulaRule(formula=['AND(G20<>"",G20>0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"J20:J{19+NS}", FormulaRule(formula=['AND(J20<>"",J20>0)'], fill=fill(AMARELO), font=F(color=UVA,size=10,bold=True)))
p.cell(row=20+NS,column=1,value="A acertar com o escritório: o sócio devolve ou desconta da próxima distribuição de lucro, para a conta do escritório voltar a zero. Distribuição devida = distribuível dos trimestres fechados × participação."); nota(p.cell(row=20+NS,column=1))
p.cell(row=21+NS,column=1,value="Pró-labore, retiradas e distribuição de lucro têm tratamento tributário próprio: combine o formato com o contador. A planilha só organiza o que saiu para cada sócio."); nota(p.cell(row=21+NS,column=1))
widths(p,(26,16,16,14,18,13,16,14,16,30)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
como_usar(wb,"Pró-labore e separação pessoa física × escritório",[
 ("O que esta planilha faz","Separa o dinheiro dos sócios do dinheiro do escritório. Cada sócio tem um pró-labore fixo combinado; tudo o que passar disso (retirada extra, despesa pessoal paga pela conta do escritório) aparece como \"fora do combinado\" e como saldo a acertar. O lucro de cada trimestre fechado é distribuído por uma regra clara."),
 ("Passo 1","Em Config, cadastre os sócios com participação no lucro (soma 100 %) e o pró-labore fixo mensal. Defina a parte do lucro do trimestre que vai para os sócios e o lucro mínimo para distribuir."),
 ("Passo 2","Em Resultado mensal, uma linha por mês: entradas e saídas do escritório sem nada dos sócios (copie do Painel da planilha 09). O resultado após pró-labore e o trimestre são calculados."),
 ("Passo 3","Em Retiradas, uma linha por movimento entre escritório e sócio: pró-labore pago, retirada extra, despesa pessoal paga pelo escritório, devolução e distribuição de lucro (com o trimestre de referência)."),
 ("Passo 4","Em Painel, escolha o mês em Config: o que cada sócio retirou × o combinado no mês e no ano, o saldo a acertar e o lucro distribuível dos trimestres fechados contra o que já foi pago."),
 ("Rotina","Todo dia 28: pagar o pró-labore e lançar. No fechamento do mês: lançar despesas pessoais que passaram pela conta do escritório e combinar como zerar. No fim de cada trimestre: distribuir o lucro pela regra, não pelo humor do caixa."),
 ("Com a IA","Copie \"No ano, por sócio\" e \"Lucro e distribuição por trimestre\" e use o prompt \"Caixa 06 · Separar o que é do escritório e o que é pessoal\" da biblioteca do kit para preparar a conversa entre os sócios."),
])
proteger(wb); salvar(wb,"11-pro-labore.xlsx","Pró-labore e separação pessoa física × escritório · Kit de Gestão para Advogados")
