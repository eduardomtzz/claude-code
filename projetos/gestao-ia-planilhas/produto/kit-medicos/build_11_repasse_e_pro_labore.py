#!/usr/bin/env python3
"""Planilha 11 do Kit de Gestão para Médicos: Repasse aos médicos parceiros e pró-labore dos sócios (PF × clínica). Gera 11-repasse-e-pro-labore.xlsx
Repasse = % da produção do mês da médica parceira (Painel da 01, por profissional), pago dia 10 do mês seguinte (saída no caixa 09).
Pró-labore fixo, retiradas extras, despesas pessoais e distribuição de lucro por trimestre: os mesmos lançamentos da 09."""
from ssg import *
import dados

NS=6; NPAR=4; N=400; R0=5; RN=R0+N-1; NREP=36; RP0=5; RPN=RP0+NREP-1
TIPOS=["Pró-labore","Retirada extra","Despesa pessoal paga pela clínica","Devolução à clínica","Distribuição de lucro"]
TRIMS=["1º trimestre","2º trimestre","3º trimestre","4º trimestre"]
SOCIOS=dados.PRO_LABORE
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Sócios, pró-labore combinado, médicos parceiros com % de repasse e a regra de distribuição de lucro ficam aqui.",merge_to="J")
cfg["A4"]="Clínica"; cfg["B4"]=f"{dados.CLINICA} (exemplo fictício)"
cfg["A5"]="Ano"; cfg["B5"]=2026
cfg["A6"]="Mês do painel"; cfg["B6"]="Setembro"
cfg["A7"]="Número do mês"; cfg["B7"]="=MATCH(B6,$H$5:$H$16,0)"
cfg["A8"]="Trimestre do painel"; cfg["B8"]="=ROUNDUP(B7/3,0)"
cfg["A9"]="Parte do lucro do trimestre distribuída aos sócios"; cfg["B9"]=dados.DISTRIB
cfg["A10"]="Lucro mínimo do trimestre para haver distribuição"; cfg["B10"]=dados.LUCRO_MINIMO
cfg["A11"]="Custo indireto por hora (planilha 05; informativo)"; cfg["B11"]=dados.CUSTO_INDIRETO_HORA
# Data de referência: sem ela o 4º trimestre nunca fecharia, porque o mês do painel
# não passa de 12 e o trimestre só termina no ano seguinte.
cfg["A12"]="Data de referência"; cfg["B12"]=dados.HOJE
for r in range(4,12): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"],center=True); inp(cfg["B6"],center=True); calc(cfg["B7"]); calc(cfg["B8"]); inp(cfg["B9"],PCT,center=True); inp(cfg["B10"],BRL); inp(cfg["B11"],BRL); inp(cfg["B12"],DATA)
cfg["D9"]="Regra combinada entre os sócios: o restante do lucro fica na clínica (reserva e provisões). Trimestre com lucro abaixo do mínimo não distribui."
cfg["D10"]="A distribuição é calculada só para trimestres já fechados (os três meses lançados em Resultado mensal e anteriores ao mês do painel)."
cfg["D11"]="Quanto vale a hora de sala, recepção e estrutura (custos fixos ÷ horas de atendimento: R$ 71,43 no exemplo). Serve só para MOSTRAR o tamanho da estrutura que o parceiro usa: esse custo NÃO é descontado da margem da parceria, porque a estrutura já está inteira dentro do custo-hora dos sócios na planilha 05 (10.000 de custo fixo ÷ 140 h) e o pró-labore dos dois sócios já cobre o mês. Descontar de novo cobraria a mesma estrutura duas vezes. A margem da parceria desconta só o que o parceiro consome de verdade: material e insumo."
for r in (9,10,11): nota(cfg.cell(row=r,column=4)); cfg.cell(row=r,column=4).alignment=Alignment(wrap_text=True,vertical="top"); cfg.merge_cells(start_row=r,start_column=4,end_row=r,end_column=6); cfg.row_dimensions[r].height=32
cfg["H4"]="Meses"; cfg["J4"]="Tipos de movimento"; rotulo(cfg["H4"]); rotulo(cfg["J4"])
for i,m_ in enumerate(MESES): cfg.cell(row=5+i,column=8,value=m_).font=F(size=10,color=TINTA)
for i,t in enumerate(TIPOS): cfg.cell(row=5+i,column=10,value=t).font=F(size=10,color=TINTA)
dv=lista("=Config!$H$5:$H$16"); dv.add("B6"); cfg.add_data_validation(dv)
cfg["A13"]="Sócios (até 6)"; rotulo(cfg["A13"])
hdr(cfg,14,["Sócio","Participação no lucro","Pró-labore fixo mensal"])
S0=15; SN=S0+NS-1
for i in range(NS):
    r=S0+i; inp(cfg.cell(row=r,column=1)); inp(cfg.cell(row=r,column=2),PCT,center=True); inp(cfg.cell(row=r,column=3),BRL)
cfg.cell(row=SN+1,column=1,value="Total"); cfg.cell(row=SN+1,column=2,value=f"=SUM(B{S0}:B{SN})"); cfg.cell(row=SN+1,column=3,value=f"=SUM(C{S0}:C{SN})")
for c in (1,2,3): cfg.cell(row=SN+1,column=c).font=F(bold=True,color=UVA,size=10); cfg.cell(row=SN+1,column=c).border=borda
cfg.cell(row=SN+1,column=2).number_format=PCT; cfg.cell(row=SN+1,column=3).number_format=BRL; cfg.cell(row=SN+1,column=2).alignment=Alignment(horizontal="center")
cfg.cell(row=SN+1,column=4,value=f'=IF(ROUND(B{SN+1},4)=1,"","A participação deve somar 100 %")'); cfg.cell(row=SN+1,column=4).font=F(color=VERM_T,size=10,bold=True)
for i,(n_,v) in enumerate(SOCIOS):
    cfg.cell(row=S0+i,column=1,value=n_); cfg.cell(row=S0+i,column=2,value=1/len(SOCIOS)); cfg.cell(row=S0+i,column=3,value=v)
P0=SN+5; PN=P0+NPAR-1
cfg.cell(row=P0-2,column=1,value="Médicos parceiros por repasse (até 4)"); rotulo(cfg.cell(row=P0-2,column=1))
hdr(cfg,P0-1,["Parceiro","% de repasse (parte do parceiro)","Sobre","Pago no dia"])
for i in range(NPAR):
    r=P0+i; inp(cfg.cell(row=r,column=1)); inp(cfg.cell(row=r,column=2),PCT,center=True); inp(cfg.cell(row=r,column=3),center=True); inp(cfg.cell(row=r,column=4),"0",center=True)
cfg.cell(row=P0,column=1,value=dados.REN); cfg.cell(row=P0,column=2,value=dados.REPASSE); cfg.cell(row=P0,column=3,value="Produção do mês"); cfg.cell(row=P0,column=4,value=10)
dvs=lista('"Produção do mês,Recebido no mês"'); dvs.add(f"C{P0}:C{PN}"); cfg.add_data_validation(dvs)
cfg.cell(row=PN+1,column=1,value="Preencha de cima para baixo, sem pular linha. Repasse sobre a produção: o parceiro recebe pelo que atendeu, e a glosa do convênio fica com a clínica; a planilha usa a coluna \"Produção do mês\" da aba Repasse. Sobre o recebido: o parceiro espera o convênio pagar, e aí você precisa preencher a coluna \"Recebido no mês\" da aba Repasse — é ela que a planilha usa nesse caso. Combine por escrito; a planilha só calcula.").font=F(size=9,color=LILAS)
cfg.cell(row=PN+2,column=1,value="Pró-labore fixo: o valor combinado que cada sócio retira todo mês. Retirada extra e despesa pessoal paga pela clínica são o que passou do combinado.").font=F(size=9,color=LILAS)
widths(cfg,(46,20,22,3,3,3,3,12,3,34)); cfg.sheet_view.showGridLines=False
LSOC=f"OFFSET(Config!$A${S0},0,0,MAX(1,COUNTA(Config!$A${S0}:$A${SN})),1)"; LPAR=f"OFFSET(Config!$A${P0},0,0,MAX(1,COUNTA(Config!$A${P0}:$A${PN})),1)"
CH="Config!$B$11"
# ---------- Repasse ----------
rp=wb.create_sheet("Repasse")
titulo(rp,"Repasse aos médicos parceiros","Uma linha por parceiro e mês. Amarelo: produção e horas atendidas (Painel da 01, por profissional, com o mês escolhido em Config) e o que foi pago. O resto é calculado.",merge_to="M")
hdr(rp,4,["Mês","Ano","Parceiro","Produção do mês (R$)","Horas atendidas","% de repasse","Repasse devido (R$)","Pago em","Valor pago (R$)","Diferença (R$)","Fica com a clínica (R$)","Material e insumo do parceiro (R$)","Margem da parceria (R$)","Custo indireto das horas (informativo, R$)","Recebido no mês (R$) · só se o acordo for sobre o recebido"],height=52)
for r in range(RP0,RPN+1):
    inp(rp.cell(row=r,column=1),center=True); inp(rp.cell(row=r,column=2),center=True); inp(rp.cell(row=r,column=3)); inp(rp.cell(row=r,column=4),BRL0,center=True); inp(rp.cell(row=r,column=5),"#,##0.0",center=True); inp(rp.cell(row=r,column=15),BRL0,center=True)
    rp.cell(row=r,column=6,value=f'=IF(C{r}="","",IFERROR(INDEX(Config!$B${P0}:$B${PN},MATCH(C{r},Config!$A${P0}:$A${PN},0)),""))'); calc(rp.cell(row=r,column=6),PCT)
    # a base do repasse segue o acordo escolhido em Config (coluna "Sobre"): produção
    # do mês (coluna D) ou o que a clínica recebeu no mês (coluna O). Antes a opção
    # "Recebido no mês" não mudava fórmula nenhuma e o parceiro era pago pela base errada.
    base=(f'IF(IFERROR(INDEX(Config!$C${P0}:$C${PN},MATCH(C{r},Config!$A${P0}:$A${PN},0)),"Produção do mês")'
          f'="Recebido no mês",N(O{r}),N(D{r}))')
    rp.cell(row=r,column=7,value=f'=IF(OR(C{r}="",F{r}=""),"",IF({base}=0,"",ROUND({base}*F{r},0)))'); calc(rp.cell(row=r,column=7),BRL0)
    inp(rp.cell(row=r,column=8),DATA,center=True); inp(rp.cell(row=r,column=9),BRL0,center=True)
    rp.cell(row=r,column=10,value=f'=IF(G{r}="","",IF(I{r}="",G{r},G{r}-I{r}))'); calc(rp.cell(row=r,column=10),BRL0)
    rp.cell(row=r,column=11,value=f'=IF(G{r}="","",D{r}-G{r})'); calc(rp.cell(row=r,column=11),BRL0)
    inp(rp.cell(row=r,column=12),BRL0,center=True)
    rp.cell(row=r,column=13,value=f'=IF(G{r}="","",K{r}-N(L{r}))'); calc(rp.cell(row=r,column=13),BRL0)
    rp.cell(row=r,column=14,value=f'=IF(OR(G{r}="",E{r}=""),"",E{r}*{CH})'); calc(rp.cell(row=r,column=14),BRL0); rp.cell(row=r,column=14).font=F(color=LILAS,size=10)
    # P: auxiliar do número do mês (oculta). Ficava em O, sobre a entrada de "Recebido
    # no mês": o acordo sobre o recebido pagava o número do mês × % (agosto, R$ 4).
    rp.cell(row=r,column=16,value=f'=IF(A{r}="","",MATCH(A{r},Config!$H$5:$H$16,0))'); rp.cell(row=r,column=16).font=F(color=CINZA,size=9)
    rp.cell(row=r,column=17,value=f'=IF(OR(C{r}="",F{r}=""),0,IF(AND(IFERROR(INDEX(Config!$C${P0}:$C${PN},MATCH(C{r},Config!$A${P0}:$A${PN},0)),"Produção do mês")="Recebido no mês",O{r}=""),1,0))'); rp.cell(row=r,column=17).font=F(color=CINZA,size=9)
for col in ("P","Q"): rp.column_dimensions[col].hidden=True
rp.conditional_formatting.add(f"O{RP0}:O{RPN}", FormulaRule(formula=[f'$Q{RP0}=1'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
for dv,rng_ in [(lista("=Config!$H$5:$H$16"),f"A{RP0}:A{RPN}"),(lista(f"={LPAR}",strict=True),f"C{RP0}:C{RPN}"),(DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True),f"H{RP0}:H{RPN}")]:
    dv.add(rng_); rp.add_data_validation(dv)
rp.conditional_formatting.add(f"J{RP0}:J{RPN}", FormulaRule(formula=[f'AND(ISNUMBER(J{RP0}),J{RP0}>0)'], fill=fill(AMARELO), font=F(color=UVA,size=10,bold=True)))
rp.conditional_formatting.add(f"J{RP0}:J{RPN}", FormulaRule(formula=[f'AND(ISNUMBER(J{RP0}),J{RP0}<0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
rp.conditional_formatting.add(f"M{RP0}:M{RPN}", FormulaRule(formula=[f'AND(ISNUMBER(M{RP0}),M{RP0}<0)'], font=F(color="C8402E",size=10,bold=True)))
rp.cell(row=RPN+2,column=1,value="Diferença em amarelo: repasse devido e ainda não pago (ou pago a menos). Margem da parceria = o que fica com a clínica − material e insumo que o parceiro consome (o custo direto da parceria). O custo indireto das horas é só informativo: a estrutura já está paga dentro do custo-hora dos sócios (05), e descontá-la aqui cobraria a mesma sala duas vezes. Margem negativa em vermelho: o repasse combinado não cobre nem o material; reveja o % ou a tabela.").font=F(size=9,color=LILAS)
rp.merge_cells(start_row=RPN+2,start_column=1,end_row=RPN+2,end_column=13); rp.cell(row=RPN+2,column=1).alignment=Alignment(wrap_text=True,vertical="top"); rp.row_dimensions[RPN+2].height=30
rp.cell(row=RPN+4,column=1,value="A coluna \"Recebido no mês\" só é usada quando o acordo do parceiro, em Config, for \"Recebido no mês\": aí o repasse sai do que a clínica efetivamente recebeu (convênio já pago), não da produção. Com o acordo sobre a produção, deixe-a vazia.").font=F(size=9,color=LILAS)
rp.cell(row=RPN+3,column=1,value="No exemplo, a produção de janeiro a junho veio do fechamento do dia (a agenda na planilha 01 começou em julho); julho e agosto são o Painel da 01 por profissional; setembro está em andamento (até 11/09), sem repasse pago ainda.").font=F(size=9,color=LILAS)
widths(rp,(11,7,24,15,11,10,14,12,13,12,14,15,14,17,22)); rp.freeze_panes="D5"; rp.sheet_view.showGridLines=False
# exemplo: produção da parceira jan-set (dados.AGENDA_TODA); pagamentos = lançamentos "Repasse" da 09
rep_pagos={}
for d,t,c,quem,ref,desc,v,f,pago in dados.LANCAMENTOS:
    if c=="Repasse à médica parceira" and pago=="Sim": rep_pagos[d.month]=(d,v)
for i,m in enumerate(range(1,10)):
    r=RP0+i; prod=dados.producao(dados.REN,m); horas=dados.horas_atendidas(m,prof=dados.REN)
    rp.cell(row=r,column=1,value=MESES[m-1]); rp.cell(row=r,column=2,value=2026); rp.cell(row=r,column=3,value=dados.REN); rp.cell(row=r,column=4,value=prod); rp.cell(row=r,column=5,value=round(horas,1))
    rp.cell(row=r,column=12,value=dados.material(dados.REN,m))
    if m+1 in rep_pagos:
        d,v=rep_pagos[m+1]; rp.cell(row=r,column=8,value=d); rp.cell(row=r,column=9,value=v)
        assert v==round(prod*dados.REPASSE),(m,v,prod)
# ---------- Resultado mensal ----------
rm=wb.create_sheet("Resultado mensal")
titulo(rm,"Resultado mensal da clínica","Amarelo: entradas e saídas de cada mês, sem nada dos sócios (copie do Painel da planilha 09). O resto é calculado.",merge_to="H")
hdr(rm,4,["Mês","Entradas recebidas","Saídas da clínica (sem sócios)","Pró-labore fixo combinado","Resultado após pró-labore","Trimestre"],height=40)
for i in range(12):
    r=5+i
    rm.cell(row=r,column=1,value=MESES[i]); calc(rm.cell(row=r,column=1),center=False)
    inp(rm.cell(row=r,column=2),BRL); inp(rm.cell(row=r,column=3),BRL)
    rm.cell(row=r,column=4,value=f'=IF(AND(B{r}="",C{r}=""),0,Config!$C${SN+1})'); calc(rm.cell(row=r,column=4),BRL)
    rm.cell(row=r,column=5,value=f"=B{r}-C{r}-D{r}"); calc(rm.cell(row=r,column=5),BRL)
    rm.cell(row=r,column=6,value=TRIMS[i//3]); calc(rm.cell(row=r,column=6))
rm.conditional_formatting.add("E5:E16", FormulaRule(formula=['E5<0'], font=F(color="C8402E",size=10,bold=True)))
rm["A18"]="Entradas = Entrou no mês (Painel da planilha 09) menos devoluções dos sócios (Outras entradas). Saídas sem sócios = Saiu no mês menos pró-labore, retiradas extras, distribuição de lucro e despesas pessoais dos sócios (o repasse à parceira fica dentro). Meses não fechados ficam em branco (setembro: até 11/09)."; nota(rm["A18"])
widths(rm,(14,18,22,20,20,14)); rm.sheet_view.showGridLines=False
tot=dados.TOTAIS
for m in range(1,10):
    rm.cell(row=4+m,column=2,value=tot[m]["ent_sem_devol"]); rm.cell(row=4+m,column=3,value=tot[m]["sai"]-tot[m]["pessoal"])
# ---------- Retiradas ----------
re_=wb.create_sheet("Retiradas")
titulo(re_,"Retiradas e movimentos sócio × clínica","Uma linha por movimento entre a conta da clínica e a pessoa física de cada sócio. Preencha o amarelo; mês e ano são calculados.",merge_to="H")
hdr(re_,4,["Data","Sócio","Tipo","Descrição","Valor","Trimestre de referência (só distribuição)","Mês","Ano"],height=40)
for r in range(R0,RN+1):
    for c in range(1,7): inp(re_.cell(row=r,column=c))
    re_.cell(row=r,column=1).number_format=DATA; re_.cell(row=r,column=5).number_format=BRL
    for c in (1,2,3,6): re_.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    re_.cell(row=r,column=7,value=f'=IF(A{r}="","",MONTH(A{r}))'); calc(re_.cell(row=r,column=7))
    re_.cell(row=r,column=8,value=f'=IF(A{r}="","",YEAR(A{r}))'); calc(re_.cell(row=r,column=8))
for dv,rng_ in [(lista(f"={LSOC}",strict=True),f"B{R0}:B{RN}"),(lista("=Config!$J$5:$J$9"),f"C{R0}:C{RN}"),
                (lista('"'+",".join(TRIMS)+'"'),f"F{R0}:F{RN}"),(DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True),f"A{R0}:A{RN}"),
                (DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True,showErrorMessage=True),f"E{R0}:E{RN}")]:
    dv.add(rng_); re_.add_data_validation(dv)
re_.conditional_formatting.add(f"A{R0}:H{RN}", FormulaRule(formula=[f'$C{R0}="Despesa pessoal paga pela clínica"'], fill=fill(VERM)))
re_.conditional_formatting.add(f"A{R0}:H{RN}", FormulaRule(formula=[f'$C{R0}="Devolução à clínica"'], font=F(color=VERDE_T,size=10)))
widths(re_,(12,24,34,44,14,22,6,7)); re_.freeze_panes="A5"; re_.sheet_view.showGridLines=False; re_.auto_filter.ref=f"A4:H{RN}"
pref={"Pró-labore ·":"Pró-labore","Retirada extra ·":"Retirada extra","Despesa pessoal ·":"Despesa pessoal paga pela clínica","Devolução de despesa pessoal ·":"Devolução à clínica","Distribuição de lucro ·":"Distribuição de lucro"}
rows=[]
for d,t,c,quem,ref,desc,v,f,pago in dados.LANCAMENTOS:
    if pago!="Sim": continue
    for pr,tipo in pref.items():
        if desc.startswith(pr):
            soc=next(n for n,_ in SOCIOS if n in desc)
            partes=[x.strip() for x in desc.split("·")]; refq=""
            if tipo=="Distribuição de lucro": refq=partes[1]; txt="Distribuição de lucro · "+refq
            elif tipo=="Pró-labore": txt="Pró-labore de "+MESES[d.month-1].lower()
            elif tipo=="Devolução à clínica": txt="Devolução da despesa pessoal (plano de saúde)"
            else: txt=partes[-1].replace(" (a acertar)","").capitalize()
            rows.append((d,soc,tipo,txt,v,refq))
for i,row in enumerate(rows):
    for c,v in enumerate(row,start=1): re_.cell(row=R0+i,column=c,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!B4&" · Repasse e pró-labore · "&Config!B6&" de "&Config!B5',"Nada para digitar aqui. Parceiros e sócios vêm de Config; repasses, de Repasse; movimentos, de Retiradas; lucro, de Resultado mensal.",merge_to="J")
M="Config!$B$7"; Y="Config!$B$5"; Q="Config!$B$8"
RB=f"Retiradas!$B${R0}:$B${RN}"; RC=f"Retiradas!$C${R0}:$C${RN}"; RE=f"Retiradas!$E${R0}:$E${RN}"; RF=f"Retiradas!$F${R0}:$F${RN}"; RG=f"Retiradas!$G${R0}:$G${RN}"; RH=f"Retiradas!$H${R0}:$H${RN}"
PB=f"Repasse!$B${RP0}:$B${RPN}"; PC_=f"Repasse!$C${RP0}:$C${RPN}"; PD=f"Repasse!$D${RP0}:$D${RPN}"; PE=f"Repasse!$E${RP0}:$E${RPN}"; PG=f"Repasse!$G${RP0}:$G${RPN}"; PI=f"Repasse!$I${RP0}:$I${RPN}"
PJ=f"Repasse!$J${RP0}:$J${RPN}"; PK=f"Repasse!$K${RP0}:$K${RPN}"; PL=f"Repasse!$L${RP0}:$L${RPN}"; PM=f"Repasse!$M${RP0}:$M${RPN}"; AVISO=9+NPAR; NOTA=10+NPAR       # aviso do recebido em branco e a nota da tabela de parceiros
SM=NOTA+2; SA=SM+11; TQ=SA+12    # "Sócios no mês", "Sócios no ano" e os trimestres
PCUSTO=f"Repasse!$N${RP0}:$N${RPN}"; PN_=f"Repasse!$P${RP0}:$P${RPN}"   # P = número do mês (auxiliar)
PQ_=f"Repasse!$Q${RP0}:$Q${RPN}"   # 1 = acordo sobre o recebido, recebido em branco
def smes(tipo,soc): return f'SUMIFS({RE},{RB},{soc},{RC},"{tipo}",{RG},{M},{RH},{Y})'
def sano(tipo,soc): return f'SUMIFS({RE},{RB},{soc},{RC},"{tipo}",{RG},"<="&{M},{RH},{Y})'
# parceiros
p["A7"]="Médicos parceiros: no mês do painel e no ano"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Parceiro","Produção no mês","Repasse devido no mês","Produção no ano","Repasse no ano","Pago no ano","A pagar","Fica com a clínica (ano)","Material e insumo (ano)","Margem da parceria (ano)","Custo indireto das horas (ano, informativo)"],height=52)
for i in range(NPAR):
    r=9+i; src=f"Config!$A${P0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",SUMIFS({PD},{PC_},{src},{PN_},{M},{PB},{Y}))')
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({PG},{PC_},{src},{PN_},{M},{PB},{Y}))')
    p.cell(row=r,column=4,value=f'=IF({src}="","",SUMIFS({PD},{PC_},{src},{PB},{Y},{PN_},"<="&{M}))')
    p.cell(row=r,column=5,value=f'=IF({src}="","",SUMIFS({PG},{PC_},{src},{PB},{Y},{PN_},"<="&{M}))')
    p.cell(row=r,column=6,value=f'=IF({src}="","",SUMIFS({PI},{PC_},{src},{PB},{Y},{PN_},"<="&{M}))')
    p.cell(row=r,column=7,value=f'=IF({src}="","",E{r}-F{r})')
    p.cell(row=r,column=8,value=f'=IF({src}="","",D{r}-E{r})')
    p.cell(row=r,column=9,value=f'=IF({src}="","",SUMIFS({PL},{PC_},{src},{PB},{Y},{PN_},"<="&{M}))')
    p.cell(row=r,column=10,value=f'=IF({src}="","",H{r}-I{r})')
    p.cell(row=r,column=11,value=f'=IF({src}="","",SUMIFS({PCUSTO},{PC_},{src},{PB},{Y},{PN_},"<="&{M}))')
    for c in range(2,12): calc(p.cell(row=r,column=c),BRL0)
    p.cell(row=r,column=7).font=F(bold=True,color=UVA,size=10); p.cell(row=r,column=10).font=F(bold=True,color=UVA,size=10)
    p.cell(row=r,column=11).font=F(color=LILAS,size=10)
p.conditional_formatting.add(f"G9:G{8+NPAR}", FormulaRule(formula=['AND(ISNUMBER(G9),G9>0)'], fill=fill(AMARELO), font=F(color=UVA,size=10,bold=True)))
p.conditional_formatting.add(f"J9:J{8+NPAR}", FormulaRule(formula=['AND(ISNUMBER(J9),J9<0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
# aviso do acordo sobre o recebido sem valor preenchido: sem ele o repasse do mês
# simplesmente não aparece e o "A pagar" do ano fica negativo, sem explicação
p.cell(row=AVISO,column=1,value=f'=IF(SUM({PQ_})=0,"",SUM({PQ_})&" mês(es) com acordo sobre o recebido e a coluna \'Recebido no mês\' em branco na aba Repasse (em vermelho lá): o repasse desses meses não foi calculado. Preencha o valor que a clínica recebeu, ou volte o acordo para produção em Config.")')
p.cell(row=AVISO,column=1).font=F(size=10,bold=True,color=VERM_T)
p.merge_cells(start_row=AVISO,start_column=1,end_row=AVISO,end_column=11)
p.cell(row=AVISO,column=1).alignment=Alignment(wrap_text=True,vertical="top")
p.cell(row=NOTA,column=1,value="A pagar = repasse devido e ainda não pago (no exemplo, o de setembro, que sai dia 10 de outubro). Margem da parceria = o que fica com a clínica − material e insumo do parceiro. O custo indireto das horas (última coluna) é informativo: mostra quanto vale a estrutura que o parceiro ocupa, mas ela já está paga dentro do custo-hora dos sócios (05) — descontá-la de novo cobraria a mesma sala duas vezes."); nota(p.cell(row=NOTA,column=1))
p.merge_cells(start_row=NOTA,start_column=1,end_row=NOTA,end_column=11); p.cell(row=NOTA,column=1).alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[NOTA].height=30
# trimestres
p.cell(row=TQ-2,column=1,value="Lucro e distribuição por trimestre").font=F(bold=True,size=13,color=UVA)
hdr(p,TQ-1,["Trimestre","Entradas","Saídas (sem sócios)","Pró-labore fixo","Resultado após pró-labore","Fechado?","Distribuível aos sócios","Já distribuído","Falta distribuir"],height=40)
for q in range(4):
    r=TQ+q; a=5+q*3; b=7+q*3
    p.cell(row=r,column=1,value=TRIMS[q]); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f"=SUM('Resultado mensal'!B{a}:B{b})"); p.cell(row=r,column=3,value=f"=SUM('Resultado mensal'!C{a}:C{b})")
    p.cell(row=r,column=4,value=f"=SUM('Resultado mensal'!D{a}:D{b})"); p.cell(row=r,column=5,value=f"=SUM('Resultado mensal'!E{a}:E{b})")
    # O trimestre fecha quando a data de referência já passou do último dia dele, e só
    # conta como fechado se os três meses tiverem resultado lançado: trimestre com mês
    # em branco distribui lucro a menos. Antes o teste era mês do painel > 3*(q+1), que
    # para o 4º trimestre exigia mês 13 — condição impossível.
    ano_seg = 'Config!$B$5+1' if q == 3 else 'Config!$B$5'
    mes_seg = 1 if q == 3 else 3*(q+1)+1
    fim_tri = f'DATE({ano_seg},{mes_seg},1)'
    # os TRÊS meses precisam estar lançados nas três colunas: entradas, saídas e
    # pró-labore. Contar só as entradas fechava o trimestre com as despesas em branco e
    # liberava lucro que não existe (achado G-9 da auditoria de 18/09).
    tres = (f"AND(COUNT('Resultado mensal'!B{a}:B{b})>=3,COUNT('Resultado mensal'!C{a}:C{b})>=3,"
            f"COUNT('Resultado mensal'!D{a}:D{b})>=3)")
    p.cell(row=r,column=6,value=f'=IF(AND(Config!$B$12>={fim_tri},{tres}),"Sim","Em andamento")')
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
kpi(p,4,1,"Repasse devido no mês",f"=SUM(C9:C{8+NPAR})",SOL,UVA,fmt=BRL0)
kpi(p,4,3,"Repasse a pagar (ano)",f"=SUM(G9:G{8+NPAR})",LAVANDA,UVA,fmt=BRL0)
kpi(p,4,5,"Pró-labore combinado (mês)",f"=Config!$C${SN+1}",LAVANDA,UVA,fmt=BRL0)
kpi(p,4,7,"Fora do combinado (mês)",f"=SUM(I{SM+2}:I{SM+1+NS})",VERM,VERM_T,fmt=BRL0)
kpi(p,4,9,"A acertar com a clínica (ano)",f"=SUM(G{SA+2}:G{SA+1+NS})",VERM,VERM_T,fmt=BRL0)
# no mês por sócio
p.cell(row=SM,column=1,value="Sócios no mês").font=F(bold=True,size=13,color=UVA)
hdr(p,SM+1,["Sócio","Pró-labore combinado","Pró-labore pago","Retiradas extras","Despesas pessoais pela clínica","Devoluções","Distribuição de lucro","Total retirado","Fora do combinado","Situação"],height=40)
for i in range(NS):
    r=SM+2+i; src=f"Config!$A${S0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",Config!$C${S0+i})')
    p.cell(row=r,column=3,value=f'=IF({src}="","",{smes("Pró-labore",src)})')
    p.cell(row=r,column=4,value=f'=IF({src}="","",{smes("Retirada extra",src)})')
    p.cell(row=r,column=5,value=f'=IF({src}="","",{smes("Despesa pessoal paga pela clínica",src)})')
    p.cell(row=r,column=6,value=f'=IF({src}="","",{smes("Devolução à clínica",src)})')
    p.cell(row=r,column=7,value=f'=IF({src}="","",{smes("Distribuição de lucro",src)})')
    p.cell(row=r,column=8,value=f'=IF({src}="","",C{r}+D{r}+E{r}-F{r}+G{r})')
    p.cell(row=r,column=9,value=f'=IF({src}="","",D{r}+E{r}-F{r})')
    p.cell(row=r,column=10,value=f'=IF({src}="","",IF(I{r}>0,"Acima do combinado",IF(C{r}<B{r},"Pró-labore ainda não pago por completo","Conforme o combinado")))')
    for c in range(2,10): calc(p.cell(row=r,column=c),BRL0)
    calc(p.cell(row=r,column=10)); p.cell(row=r,column=8).font=F(bold=True,color=UVA,size=10)
p.conditional_formatting.add(f"J{SM+2}:J{SM+1+NS}", FormulaRule(formula=[f'J{SM+2}="Acima do combinado"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"J{SM+2}:J{SM+1+NS}", FormulaRule(formula=[f'J{SM+2}="Conforme o combinado"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
p.conditional_formatting.add(f"J{SM+2}:J{SM+1+NS}", FormulaRule(formula=[f'J{SM+2}="Pró-labore ainda não pago por completo"'], fill=fill(AMARELO)))
p.cell(row=SM+2+NS,column=1,value="Fora do combinado = retiradas extras + despesas pessoais pagas pela clínica − devoluções. Distribuição de lucro segue a regra de Config e não conta como \"fora\"."); nota(p.cell(row=SM+2+NS,column=1))
# no ano por sócio
p.cell(row=SA,column=1,value="Sócios no ano, até o mês do painel").font=F(bold=True,size=13,color=UVA)
hdr(p,SA+1,["Sócio","Pró-labore combinado até o mês","Pró-labore pago","Retiradas extras","Despesas pessoais pela clínica","Devoluções","A acertar com a clínica","Distribuição devida (trimestres fechados)","Distribuição recebida","Distribuição a receber"],height=52)
for i in range(NS):
    r=SA+2+i; src=f"Config!$A${S0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",Config!$C${S0+i}*{M})')
    p.cell(row=r,column=3,value=f'=IF({src}="","",{sano("Pró-labore",src)})')
    p.cell(row=r,column=4,value=f'=IF({src}="","",{sano("Retirada extra",src)})')
    p.cell(row=r,column=5,value=f'=IF({src}="","",{sano("Despesa pessoal paga pela clínica",src)})')
    p.cell(row=r,column=6,value=f'=IF({src}="","",{sano("Devolução à clínica",src)})')
    p.cell(row=r,column=7,value=f'=IF({src}="","",D{r}+E{r}-F{r})')
    p.cell(row=r,column=8,value=f'=IF({src}="","",{GDIST}*Config!$B${S0+i})')
    p.cell(row=r,column=9,value=f'=IF({src}="","",{sano("Distribuição de lucro",src)})')
    p.cell(row=r,column=10,value=f'=IF({src}="","",IF(ABS(H{r}-I{r})<1,0,H{r}-I{r}))')
    for c in range(2,11): calc(p.cell(row=r,column=c),BRL0)
    p.cell(row=r,column=7).font=F(bold=True,color=UVA,size=10); p.cell(row=r,column=10).font=F(bold=True,color=UVA,size=10)
p.conditional_formatting.add(f"G{SA+2}:G{SA+1+NS}", FormulaRule(formula=[f'AND(G{SA+2}<>"",G{SA+2}>0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"J{SA+2}:J{SA+1+NS}", FormulaRule(formula=[f'AND(J{SA+2}<>"",J{SA+2}>0)'], fill=fill(AMARELO), font=F(color=UVA,size=10,bold=True)))
p.cell(row=SA+2+NS,column=1,value="A acertar com a clínica: o sócio devolve ou desconta da próxima distribuição de lucro. Distribuição devida = distribuível dos trimestres fechados × participação. Pró-labore, retiradas, repasse e distribuição têm tratamento tributário próprio: combine o formato com o contador."); nota(p.cell(row=SA+2+NS,column=1))
widths(p,(24,14,15,13,14,12,13,14,14,15,17)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
como_usar(wb,"Repasse aos médicos parceiros e pró-labore dos sócios",[
 ("O que esta planilha faz","Separa três dinheiros que costumam se misturar: o repasse dos médicos parceiros (% da produção do mês), o pró-labore fixo dos sócios e o que passou do combinado (retirada extra, despesa pessoal paga pela clínica). Mostra se a parceria paga a sala que usa e distribui o lucro de cada trimestre fechado por uma regra clara."),
 ("Passo 1","Em Config, cadastre os sócios (participação no lucro, pró-labore fixo), os parceiros (% de repasse, sobre produção ou recebido, dia de pagamento), a regra de distribuição e o custo indireto por hora (Painel da 05) — que entra só como informação, para mostrar o tamanho da estrutura que o parceiro usa."),
 ("Passo 2","Em Repasse, uma linha por parceiro e mês: produção e horas atendidas (Painel da 01, por profissional, com o mês escolhido em Config), o material e insumo que os atendimentos dele consumiram e, quando pagar, a data e o valor. O repasse pago é a mesma saída do caixa (09)."),
 ("Passo 3","Em Resultado mensal, entradas e saídas da clínica sem nada dos sócios (Painel da 09). Em Retiradas, uma linha por movimento entre clínica e sócio: pró-labore, retirada extra, despesa pessoal, devolução e distribuição de lucro."),
 ("Passo 4","Em Painel, escolha o mês em Config: repasse devido e a pagar, margem da parceria, o que cada sócio retirou × o combinado no mês e no ano, o saldo a acertar e o lucro distribuível dos trimestres fechados contra o que já foi pago."),
 ("Rotina","Dia 10: pagar o repasse do mês anterior e lançar. Dia 28: pagar o pró-labore e lançar. No fechamento do mês: lançar despesas pessoais que passaram pela conta da clínica e combinar como zerar. No fim de cada trimestre: distribuir o lucro pela regra, não pelo humor do caixa."),
 ("Com a IA","Copie \"Médicos parceiros\" e \"Sócios no ano\" e use o prompt \"Caixa 06 · Separar o que é da clínica e o que é pessoal\" ou \"Caixa 07 · Conversa sobre o repasse com o médico parceiro\" da biblioteca do kit."),
])
proteger(wb); salvar(wb,"11-repasse-e-pro-labore.xlsx","Repasse e pró-labore · Kit de Gestão para Médicos")
