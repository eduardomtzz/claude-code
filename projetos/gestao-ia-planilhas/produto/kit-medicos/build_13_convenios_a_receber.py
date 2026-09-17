#!/usr/bin/env python3
"""Planilha 13 do Kit de Gestão para Médicos: Convênios a receber (lotes enviados, pagos, glosados, recurso de glosa).
Gera 13-convenios-a-receber.xlsx (Como usar, Painel, Config, Lotes, Guias).
Lote = convênio × mês de competência, enviado no dia 5 do mês seguinte, pago no prazo do convênio menos a glosa (dados.LOTES).
Guias = uma por atendimento de convênio realizado desde 01/07/2026 (dados.GUIAS); as glosadas de um lote pago aparecem marcadas."""
from ssg import *
import dados
from openpyxl.chart import BarChart, Reference
from datetime import date

NL=150; R0=5; RNL=R0+NL-1          # Lotes: linhas 5..154
NG=1500; RNG=R0+NG-1               # Guias: linhas 5..1504
NCONV=6; C0=10; CN=C0+NCONV-1      # convênios na Config: linhas 10..15
TOP=12
def off(sheet,col,r0,r1): return f"=OFFSET({sheet}!${col}${r0},0,0,MAX(1,COUNTA({sheet}!${col}${r0}:${col}${r1})),1)"
def dstr(ref): return f'TEXT(DAY({ref}),"00")&"/"&TEXT(MONTH({ref}),"00")&"/"&YEAR({ref})'
NOME=f"{dados.CLINICA} (exemplo fictício)"
HOJE="Config!$B$5"; Y="Config!$B$6"; TOL="Config!$B$7"
CV=f"Config!$A${C0}:$A${CN}"; CP=f"Config!$B${C0}:$B${CN}"
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Cada convênio com o prazo contratual de pagamento (dias após o envio do lote) e o dia de envio.",merge_to="H")
cfg["A4"]="Clínica"; cfg["B4"]=NOME
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]=dados.HOJE
cfg["A6"]="Ano do painel"; cfg["B6"]=2026
cfg["A7"]="Tolerância de atraso antes de avisar (dias)"; cfg["B7"]=0
for r in (4,5,6,7): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],center=True); inp(cfg["B7"],"0",center=True)
hdr(cfg,C0-1,["Convênio","Prazo de pagamento (dias)","Dia de envio do lote","Glosa histórica (informativa)","Observação"],height=32)
for r in range(C0,CN+1):
    inp(cfg.cell(row=r,column=1)); inp(cfg.cell(row=r,column=2),"0",center=True); inp(cfg.cell(row=r,column=3),"0",center=True); inp(cfg.cell(row=r,column=4),"0.0%",center=True); inp(cfg.cell(row=r,column=5))
for i,(n,prazo,g) in enumerate(dados.CONVENIOS):
    r=C0+i; cfg.cell(row=r,column=1,value=n); cfg.cell(row=r,column=2,value=prazo); cfg.cell(row=r,column=3,value=dados.DIA_ENVIO_LOTE); cfg.cell(row=r,column=4,value=g); cfg.cell(row=r,column=5,value="Prazo contado do envio do lote (contrato)")
cfg.cell(row=CN+2,column=1,value="Preencha de cima para baixo, sem pular linha. Prazo: o que está no contrato (30, 45 ou 60 dias após o envio). A glosa histórica é só uma referência para o simulador (07); o Painel calcula a glosa real dos lotes pagos.").font=F(size=9,color=LILAS)
cfg.cell(row=CN+3,column=1,value="Recurso de glosa: administrativo (guia sem autorização, código errado, prazo). O texto do recurso é seu; o prompt \"Recebíveis 03 · Recurso de glosa em linguagem administrativa\" da biblioteca ajuda a redigir, sem conteúdo clínico.").font=F(size=9,color=LILAS)
widths(cfg,(40,18,14,18,44,3,3,3)); cfg.sheet_view.showGridLines=False
CONV_L=off("Config","A",C0,CN)
# ---------- Guias ----------
gu=wb.create_sheet("Guias")
titulo(gu,"Guias","Uma linha por atendimento de convênio realizado (copie da Agenda da planilha 01: data, paciente, pagador, procedimento, profissional, valor). Quando o convênio pagar o lote, marque as guias glosadas e o recurso.",merge_to="M")
hdr(gu,4,["Guia (nº)","Data do atendimento","Paciente","Convênio","Procedimento","Profissional","Valor (R$)","Glosada?","Recurso","Competência","Lote (chave)","Situação do lote","Valor glosado (R$)"],height=32)
LK=f"Lotes!$P${R0}:$P${RNL}"; LN=f"Lotes!$N${R0}:$N${RNL}"
for r in range(R0,RNG+1):
    for c in range(1,10): inp(gu.cell(row=r,column=c),center=(c not in (3,5,6)))
    gu.cell(row=r,column=2).number_format=DATA; gu.cell(row=r,column=7).number_format=BRL0
    gu.cell(row=r,column=10,value=f'=IF(B{r}="","",DATE(YEAR(B{r}),MONTH(B{r}),1))'); calc(gu.cell(row=r,column=10),"mm/yyyy")
    gu.cell(row=r,column=11,value=f'=IF(OR(B{r}="",D{r}=""),"",D{r}&"|"&TEXT(J{r},"yyyy-mm"))'); calc(gu.cell(row=r,column=11)); gu.cell(row=r,column=11).font=F(color=CINZA,size=9)
    gu.cell(row=r,column=12,value=f'=IF(K{r}="","",IFERROR(INDEX({LN},MATCH(K{r},{LK},0)),"Sem lote cadastrado"))'); calc(gu.cell(row=r,column=12))
    gu.cell(row=r,column=13,value=f'=IF(H{r}="Sim",G{r},0)'); calc(gu.cell(row=r,column=13),BRL0)
    gu.cell(row=r,column=14,value=f'=IF(AND(H{r}="Sim",I{r}<>"Aceito"),G{r}+ROW()/100000,0)'); gu.cell(row=r,column=14).font=F(color=CINZA,size=9)
gu.column_dimensions["N"].hidden=True
dvs=[(lista(CONV_L),f"D{R0}:D{RNG}"),(lista('"Sim"'),f"H{R0}:H{RNG}"),(lista('"Em recurso,Aceito,Negado"'),f"I{R0}:I{RNG}"),
     (DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True),f"B{R0}:B{RNG}"),(DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True),f"G{R0}:G{RNG}")]
for dv,rng in dvs: dv.add(rng); gu.add_data_validation(dv)
gu.conditional_formatting.add(f"A{R0}:M{RNG}", FormulaRule(formula=[f'$H{R0}="Sim"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
gu.conditional_formatting.add(f"A{R0}:M{RNG}", FormulaRule(formula=[f'AND($H{R0}="Sim",$I{R0}="Aceito")'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
gu.conditional_formatting.add(f"L{R0}:L{RNG}", FormulaRule(formula=[f'L{R0}="Sem lote cadastrado"'], font=F(color="C8402E",size=10,bold=True)))
gu.cell(row=RNG+2,column=1,value="Vermelho: guia glosada. Verde: glosa recuperada por recurso aceito. \"Sem lote cadastrado\": a competência dessa guia ainda não tem linha na aba Lotes. Só dados administrativos: nada de diagnóstico ou código clínico aqui.").font=F(size=9,color=LILAS)
widths(gu,(12,12,26,14,18,22,11,9,11,11,16,16,12)); gu.freeze_panes="C5"; gu.sheet_view.showGridLines=False; gu.auto_filter.ref=f"A4:M{RNG}"
GD=f"Guias!$D${R0}:$D${RNG}"; GG=f"Guias!$G${R0}:$G${RNG}"; GK=f"Guias!$K${R0}:$K${RNG}"; GM=f"Guias!$M${R0}:$M${RNG}"; GH=f"Guias!$H${R0}:$H${RNG}"; GI=f"Guias!$I${R0}:$I${RNG}"; GN=f"Guias!$N${R0}:$N${RNG}"
# ---------- Lotes ----------
lo=wb.create_sheet("Lotes")
titulo(lo,"Lotes de convênio","Uma linha por convênio e mês de competência. Amarelo: guias e valor enviados, data de envio, pagamento recebido, recurso de glosa e valor recuperado. Branco: previsão, glosa, situação e atraso.",merge_to="R")
hdr(lo,4,["Convênio","Competência (mês)","Nº de guias","Valor enviado (R$)","Data de envio","Data do pagamento","Valor pago (R$)","Recurso de glosa","Valor recuperado (R$)","Data da recuperação","Prazo (dias)","Previsão de pagamento","Glosa (R$)","Situação","Dias de atraso","Chave","Guias na aba Guias (R$)","Diferença (R$)"],height=40)
for r in range(R0,RNL+1):
    for c in range(1,11): inp(lo.cell(row=r,column=c),center=(c!=1))
    lo.cell(row=r,column=2).number_format="mm/yyyy"; lo.cell(row=r,column=4).number_format=BRL0; lo.cell(row=r,column=7).number_format=BRL0; lo.cell(row=r,column=9).number_format=BRL0
    for c in (5,6,10): lo.cell(row=r,column=c).number_format=DATA
    lo.cell(row=r,column=11,value=f'=IF(A{r}="","",IFERROR(INDEX({CP},MATCH(A{r},{CV},0)),""))'); calc(lo.cell(row=r,column=11),"0")
    lo.cell(row=r,column=12,value=f'=IF(OR(A{r}="",E{r}="",K{r}=""),"",E{r}+K{r})'); calc(lo.cell(row=r,column=12),DATA)
    lo.cell(row=r,column=13,value=f'=IF(OR(A{r}="",F{r}=""),0,MAX(0,D{r}-G{r}))'); calc(lo.cell(row=r,column=13),BRL0)
    lo.cell(row=r,column=14,value=f'=IF(A{r}="","",IF(E{r}="","Em separação",IF(F{r}<>"",IF(H{r}="Em recurso","Em recurso",IF(M{r}>0,"Paga com glosa","Paga")),IF(L{r}+{TOL}<{HOJE},"Atrasada","Aguardando"))))'); calc(lo.cell(row=r,column=14))
    lo.cell(row=r,column=15,value=f'=IF(N{r}="Atrasada",{HOJE}-L{r},"")'); calc(lo.cell(row=r,column=15),"0")
    lo.cell(row=r,column=16,value=f'=IF(OR(A{r}="",B{r}=""),"",A{r}&"|"&TEXT(B{r},"yyyy-mm"))'); calc(lo.cell(row=r,column=16)); lo.cell(row=r,column=16).font=F(color=CINZA,size=9)
    lo.cell(row=r,column=17,value=f'=IF(P{r}="","",IF(COUNTIF({GK},P{r})=0,"",SUMIFS({GG},{GK},P{r})))'); calc(lo.cell(row=r,column=17),BRL0)
    lo.cell(row=r,column=18,value=f'=IF(Q{r}="","",D{r}-Q{r})'); calc(lo.cell(row=r,column=18),BRL0)
    lo.cell(row=r,column=19,value=f'=IF(OR(N{r}="Atrasada",N{r}="Aguardando"),IF(N{r}="Atrasada",100000+O{r},0)+D{r}/1000000+ROW()/100000000,0)'); lo.cell(row=r,column=19).font=F(color=CINZA,size=9)
    lo.cell(row=r,column=20,value=f'=IF(AND(F{r}<>"",E{r}<>""),F{r}-E{r},"")'); lo.cell(row=r,column=20).font=F(color=CINZA,size=9)
lo.column_dimensions["S"].hidden=True; lo.column_dimensions["T"].hidden=True
dvs=[(lista(CONV_L),f"A{R0}:A{RNL}"),(lista('"Em recurso,Aceito,Negado"'),f"H{R0}:H{RNL}"),
     (DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True),f"B{R0}:B{RNL}"),(DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True),f"E{R0}:F{RNL}"),
     (DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True),f"D{R0}:D{RNL}")]
for dv,rng in dvs: dv.add(rng); lo.add_data_validation(dv)
lo.conditional_formatting.add(f"A{R0}:R{RNL}", FormulaRule(formula=[f'$N{R0}="Atrasada"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
lo.conditional_formatting.add(f"A{R0}:R{RNL}", FormulaRule(formula=[f'$N{R0}="Em recurso"'], fill=fill("FFF4CC")))
lo.conditional_formatting.add(f"A{R0}:R{RNL}", FormulaRule(formula=[f'OR($N{R0}="Paga",$N{R0}="Paga com glosa")'], font=F(color=VERDE_T,size=10)))
lo.conditional_formatting.add(f"A{R0}:R{RNL}", FormulaRule(formula=[f'$N{R0}="Em separação"'], font=F(color="8A86A0",size=10)))
lo.conditional_formatting.add(f"R{R0}:R{RNL}", FormulaRule(formula=[f'AND(ISNUMBER(R{R0}),R{R0}<>0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
lo.cell(row=RNL+2,column=1,value="Vermelho: previsão de pagamento vencida sem pagamento. Amarelo: glosa em recurso. Verde: paga. Cinza: guias em separação (lote ainda não enviado). Diferença em vermelho: o valor enviado não bate com as guias cadastradas na aba Guias para essa competência.").font=F(size=9,color=LILAS)
lo.cell(row=RNL+3,column=1,value="Glosa = enviado − pago. Recurso aceito: digite o valor recuperado e a data (é uma entrada no caixa 09). No exemplo, os lotes de outubro/2025 a maio/2026 vêm dos registros anteriores à agenda; junho em diante bate com a aba Guias.").font=F(size=9,color=LILAS)
widths(lo,(14,12,9,13,12,12,13,12,12,12,8,13,11,14,9,16,13,12)); lo.freeze_panes="C5"; lo.sheet_view.showGridLines=False; lo.auto_filter.ref=f"A4:R{RNL}"
LA=f"Lotes!$A${R0}:$A${RNL}"; LB=f"Lotes!$B${R0}:$B${RNL}"; LC=f"Lotes!$C${R0}:$C${RNL}"; LD=f"Lotes!$D${R0}:$D${RNL}"; LE=f"Lotes!$E${R0}:$E${RNL}"; LF=f"Lotes!$F${R0}:$F${RNL}"
LG=f"Lotes!$G${R0}:$G${RNL}"; LH=f"Lotes!$H${R0}:$H${RNL}"; LI=f"Lotes!$I${R0}:$I${RNL}"; LJ=f"Lotes!$J${R0}:$J${RNL}"; LL=f"Lotes!$L${R0}:$L${RNL}"; LM=f"Lotes!$M${R0}:$M${RNL}"
LN_=f"Lotes!$N${R0}:$N${RNL}"; LO=f"Lotes!$O${R0}:$O${RNL}"; LS=f"Lotes!$S${R0}:$S${RNL}"; LT=f"Lotes!$T${R0}:$T${RNL}"
ANO_ENV=f'{LE},">="&DATE({Y},1,1),{LE},"<="&DATE({Y},12,31)'; ANO_PAG=f'{LF},">="&DATE({Y},1,1),{LF},"<="&DATE({Y},12,31)'
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,f'=Config!$B$4&" · Convênios a receber · "&{dstr(HOJE)}',"Nada para digitar aqui: tudo vem de Lotes, Guias e Config. A receber = lotes enviados e ainda não pagos (valor enviado).",merge_to="L")
p.merge_cells("A1:L1")
kpi(p,4,1,"A receber (lotes enviados)",f'=SUMIFS({LD},{LN_},"Aguardando")+SUMIFS({LD},{LN_},"Atrasada")',LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Atrasado",f'=SUMIFS({LD},{LN_},"Atrasada")',VERM,VERM_T,fmt=BRL0)
kpi(p,4,5,"Recebido no ano",f'=SUMIFS({LG},{ANO_PAG})+SUMIFS({LI},{LJ},">="&DATE({Y},1,1),{LJ},"<="&DATE({Y},12,31))',VERDE,VERDE_T,fmt=BRL0)
kpi(p,4,7,"Glosa no ano (R$)",f'=SUMIFS({LM},{ANO_PAG})',VERM,VERM_T,fmt=BRL0)
kpi(p,4,9,"Glosa no ano (%)",f'=IFERROR(G5/(SUMIFS({LG},{ANO_PAG})+G5),0)',VERM,VERM_T,fmt="0.0%")
kpi(p,4,11,"Em recurso (R$)",f'=SUMIFS({LM},{LH},"Em recurso")',SOL,UVA,fmt=BRL0)
p["A7"]="Glosa (%) = glosa ÷ (pago + glosa) dos lotes pagos no ano: de tudo o que o convênio decidiu, quanto ele não pagou. Recebido no ano inclui glosa recuperada por recurso. Em separação (mês corrente) não conta como a receber até o envio."; nota(p["A7"]); p.merge_cells("A7:L7"); p["A7"].alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[7].height=30
# por convênio
p["A9"]="Por convênio (lotes enviados no ano)"; p["A9"].font=F(bold=True,size=13,color=UVA)
hdr(p,10,["Convênio","Lotes","Enviado (R$)","Pago (R$)","Glosa (R$)","Glosa (%)","Recuperado (R$)","A receber (R$)","Atrasado (R$)","Prazo contratual","Prazo real (média, dias)","Barra da glosa"],height=32)
for i in range(NCONV):
    r=11+i; src=f"Config!$A${C0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({LA},{src},{ANO_ENV}))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({LD},{LA},{src},{ANO_ENV}))'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f'=IF({src}="","",SUMIFS({LG},{LA},{src},{ANO_PAG}))'); calc(p.cell(row=r,column=4),BRL0)
    p.cell(row=r,column=5,value=f'=IF({src}="","",SUMIFS({LM},{LA},{src},{ANO_PAG}))'); calc(p.cell(row=r,column=5),BRL0)
    p.cell(row=r,column=6,value=f'=IF({src}="","",IFERROR(E{r}/(D{r}+E{r}),0))'); calc(p.cell(row=r,column=6),"0.0%")
    p.cell(row=r,column=7,value=f'=IF({src}="","",SUMIFS({LI},{LA},{src},{LJ},">="&DATE({Y},1,1),{LJ},"<="&DATE({Y},12,31)))'); calc(p.cell(row=r,column=7),BRL0)
    p.cell(row=r,column=8,value=f'=IF({src}="","",SUMIFS({LD},{LA},{src},{LN_},"Aguardando")+SUMIFS({LD},{LA},{src},{LN_},"Atrasada"))'); calc(p.cell(row=r,column=8),BRL0)
    p.cell(row=r,column=9,value=f'=IF({src}="","",SUMIFS({LD},{LA},{src},{LN_},"Atrasada"))'); calc(p.cell(row=r,column=9),BRL0)
    p.cell(row=r,column=10,value=f'=IF({src}="","",Config!$B${C0+i})'); calc(p.cell(row=r,column=10),"0")
    p.cell(row=r,column=11,value=f'=IF({src}="","",IFERROR(AVERAGEIFS({LT},{LA},{src},{ANO_PAG}),"—"))'); calc(p.cell(row=r,column=11),"0")
    p.cell(row=r,column=12,value=f'=IF(F{r}="","",REPT("█",ROUND(MIN(1,F{r}/0.15)*20,0)))'); p.cell(row=r,column=12).font=F(size=10,color="C0392B"); p.cell(row=r,column=12).border=borda
p.conditional_formatting.add(f"F11:F{10+NCONV}", FormulaRule(formula=['AND(ISNUMBER(F11),F11>0.05)'], font=F(color="C8402E",size=10,bold=True)))
p.conditional_formatting.add(f"I11:I{10+NCONV}", FormulaRule(formula=['AND(ISNUMBER(I11),I11>0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"K11:K{10+NCONV}", FormulaRule(formula=['AND(ISNUMBER(K11),K11>J11)'], font=F(color="C8402E",size=10,bold=True)))
p.cell(row=11+NCONV,column=1,value="Glosa acima de 5 % e prazo real acima do contratual ficam em vermelho: são os dois argumentos da conversa com o convênio. A barra da glosa vai até 15 %.").font=F(size=9,color=LILAS)
# lotes em aberto
A0=11+NCONV+2
p.cell(row=A0,column=1,value="Lotes em aberto: atrasados primeiro, depois os maiores").font=F(bold=True,size=13,color=UVA)
hdr(p,A0+1,["#","Convênio","Competência","Nº de guias","Enviado (R$)","Data de envio","Previsão","Situação","Dias de atraso"])
for k in range(1,TOP+1):
    r=A0+1+k; m=f'MATCH(LARGE({LS},{k}),{LS},0)'; g=f'LARGE({LS},{k})>0'
    p.cell(row=r,column=1,value=k); calc(p.cell(row=r,column=1))
    for col,src in zip((2,3,4,5,6,7,8,9),("A","B","C","D","E","L","N","O")):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},INDEX(Lotes!${src}${R0}:${src}${RNL},{m}),""),"")'); calc(p.cell(row=r,column=col),center=(col!=2))
    p.cell(row=r,column=3).number_format="mm/yyyy"; p.cell(row=r,column=5).number_format=BRL0; p.cell(row=r,column=6).number_format=DATA; p.cell(row=r,column=7).number_format=DATA; p.cell(row=r,column=9).number_format="0"
p.conditional_formatting.add(f"A{A0+2}:I{A0+1+TOP}", FormulaRule(formula=[f'$H{A0+2}="Atrasada"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
# por mês de competência
M0=A0+1+TOP+3
p.cell(row=M0,column=1,value="Por mês de competência (ano do painel)").font=F(bold=True,size=13,color=UVA)
hdr(p,M0+1,["Mês","Lotes","Guias","Enviado (R$)","Pago (R$)","Glosa (R$)","Glosa (%)","A receber (R$)","Situação"])
for i in range(12):
    r=M0+2+i; c1=f'DATE({Y},{i+1},1)'
    p.cell(row=r,column=1,value=MESES[i]); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=COUNTIFS({LB},{c1},{LA},"<>")'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=SUMIFS({LC},{LB},{c1})'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=SUMIFS({LD},{LB},{c1})'); calc(p.cell(row=r,column=4),BRL0)
    p.cell(row=r,column=5,value=f'=SUMIFS({LG},{LB},{c1})'); calc(p.cell(row=r,column=5),BRL0)
    p.cell(row=r,column=6,value=f'=SUMIFS({LM},{LB},{c1})'); calc(p.cell(row=r,column=6),BRL0)
    p.cell(row=r,column=7,value=f'=IF(E{r}+F{r}=0,"",F{r}/(E{r}+F{r}))'); calc(p.cell(row=r,column=7),"0.0%")
    p.cell(row=r,column=8,value=f'=SUMIFS({LD},{LB},{c1},{LN_},"Aguardando")+SUMIFS({LD},{LB},{c1},{LN_},"Atrasada")'); calc(p.cell(row=r,column=8),BRL0)
    p.cell(row=r,column=9,value=f'=IF(B{r}=0,"",IF(COUNTIFS({LB},{c1},{LN_},"Atrasada")>0,"Com atraso",IF(COUNTIFS({LB},{c1},{LN_},"Em separação")>0,"Em separação",IF(H{r}>0,"Aguardando","Fechado"))))'); calc(p.cell(row=r,column=9))
p.conditional_formatting.add(f"A{M0+2}:I{M0+13}", FormulaRule(formula=[f'$B{M0+2}=0'], font=F(color="B0A6C4",size=10)))
p.conditional_formatting.add(f"I{M0+2}:I{M0+13}", FormulaRule(formula=[f'I{M0+2}="Com atraso"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
p.conditional_formatting.add(f"I{M0+2}:I{M0+13}", FormulaRule(formula=[f'I{M0+2}="Fechado"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
# guias glosadas
G0=M0+16
p.cell(row=G0,column=1,value="Guias glosadas para recorrer (maiores primeiro; recurso aceito sai da lista)").font=F(bold=True,size=13,color=UVA)
hdr(p,G0+1,["#","Guia","Data","Paciente","Convênio","Procedimento","Profissional","Valor (R$)","Recurso"])
for k in range(1,TOP+1):
    r=G0+1+k; m=f'MATCH(LARGE({GN},{k}),{GN},0)'; g=f'LARGE({GN},{k})>0'
    p.cell(row=r,column=1,value=k); calc(p.cell(row=r,column=1))
    for col,src in zip((2,3,4,5,6,7,8,9),("A","B","C","D","E","F","G","I")):
        idx=f'INDEX(Guias!${src}${R0}:${src}${RNG},{m})'
        # Recurso vazio: INDEX devolve 0; mostra "—" (= ainda não recorreu), como diz a nota abaixo da lista
        expr=f'IF({idx}=0,"—",{idx})' if col==9 else idx
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},{expr},""),"")'); calc(p.cell(row=r,column=col),center=(col not in (4,6,7)))
    p.cell(row=r,column=3).number_format=DATA; p.cell(row=r,column=8).number_format=BRL0
p.conditional_formatting.add(f"A{G0+2}:I{G0+1+TOP}", FormulaRule(formula=[f'$I{G0+2}="Em recurso"'], fill=fill("FFF4CC")))
p.conditional_formatting.add(f"A{G0+2}:I{G0+1+TOP}", FormulaRule(formula=[f'$I{G0+2}="Negado"'], font=F(color="8A86A0",size=10)))
p.conditional_formatting.add(f"I{G0+2}:I{G0+1+TOP}", FormulaRule(formula=[f'$I{G0+2}="—"'], font=F(color="B0A6C4",size=10)))
p.cell(row=G0+2+TOP,column=1,value="Recurso com \"—\" = ainda não recorreu. Prazo para recorrer varia por contrato: confira antes. A planilha lista; o recurso é administrativo e é seu.").font=F(size=9,color=LILAS)
bc=BarChart(); bc.type="bar"; bc.height=6; bc.width=12; bc.title="Glosa no ano por convênio (%)"; bc.style=2
bc.add_data(Reference(p,min_col=6,min_row=10,max_row=10+len(dados.CONVENIOS)),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=11,max_row=10+len(dados.CONVENIOS)))
bc.series[0].graphicalProperties.solidFill="7A1F1F"; bc.legend=None; bc.x_axis.majorGridlines=None; bc.x_axis.number_format="0%"
p.add_chart(bc,f"J{A0}")
widths(p,(16,14,13,13,12,12,14,13,13,12,14,22)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Exemplo ----------
for i,l in enumerate(dados.LOTES):
    r=R0+i
    lo.cell(row=r,column=1,value=l["convenio"]); lo.cell(row=r,column=2,value=l["competencia"]); lo.cell(row=r,column=3,value=l["n_guias"]); lo.cell(row=r,column=4,value=l["valor"])
    if l["envio"]: lo.cell(row=r,column=5,value=l["envio"])
    if l["pagamento"]: lo.cell(row=r,column=6,value=l["pagamento"]); lo.cell(row=r,column=7,value=l["pago"])
    if l["recurso"]: lo.cell(row=r,column=8,value=l["recurso"])
    if l["recuperado"]: lo.cell(row=r,column=9,value=l["recuperado"]); lo.cell(row=r,column=10,value=l["data_recuperacao"])
guias=[g for g in dados.GUIAS if g["data"]>=dados.INICIO_AGENDA]
assert len(guias)<=NG
for i,g in enumerate(guias):
    r=R0+i
    for c,k in ((1,"numero"),(2,"data"),(3,"paciente"),(4,"convenio"),(5,"procedimento"),(6,"profissional"),(7,"valor")): gu.cell(row=r,column=c,value=g[k])
    if g["glosada"]: gu.cell(row=r,column=8,value="Sim")
    if g["recurso"]: gu.cell(row=r,column=9,value=g["recurso"])
print(len(dados.LOTES),"lotes e",len(guias),"guias no exemplo")
como_usar(wb,"Convênios a receber",[
 ("O que esta planilha faz","Responde \"quanto o convênio deve e quanto ele não pagou?\": cada lote enviado (convênio × mês) com previsão de pagamento pelo prazo do contrato, o que foi pago, a glosa, o recurso e o que foi recuperado; por convênio, por mês e a lista de guias glosadas para recorrer."),
 ("Passo 1","Em Config, cadastre cada convênio com o prazo contratual de pagamento (dias após o envio) e o dia de envio do lote. Preencha de cima para baixo, sem pular linha."),
 ("Passo 2","Em Guias, uma linha por atendimento de convênio realizado (copie da Agenda da planilha 01: data, paciente, convênio, procedimento, profissional, valor). É a base do lote do mês."),
 ("Passo 3","Em Lotes, uma linha por convênio e mês: nº de guias, valor enviado e data de envio. Quando o pagamento cair, digite data e valor pago (a glosa é a diferença) e lance a entrada no caixa (09). Se recorrer, marque o recurso; se aceito, o valor recuperado e a data. Volte em Guias e marque as guias glosadas."),
 ("Passo 4","Em Painel: a receber, atrasado, glosa do ano (R$ e %), em recurso; por convênio (com prazo real × contratual), lotes em aberto, mês a mês e as guias glosadas para recorrer."),
 ("Rotina","Sexta, 3 minutos (rotina da semana, planilha 03): separar as guias da semana e conferir se todas estão na aba Guias. Dia 5: enviar o lote do mês anterior e registrar. No recebimento: pagamento, glosa e recurso. A planilha avisa o atraso; a cobrança ao convênio é sua."),
 ("Ligação com as outras planilhas","A receber e atrasado vão para o Painel da clínica (17); a glosa % por convênio alimenta o simulador (07); os lotes pagos são entradas do caixa (09). As metas do trimestre (19) acompanham glosa, atrasos e recuperado."),
 ("Com a IA","Copie \"Por convênio\" e use o prompt \"Recebíveis 01 · Resumir os convênios para o sócio\" da biblioteca do kit; para uma guia glosada, \"Recebíveis 03 · Recurso de glosa em linguagem administrativa\" (sem dados clínicos: só guia, procedimento, data e motivo administrativo)."),
])
proteger(wb); salvar(wb,"13-convenios-a-receber.xlsx","Convênios a receber · Kit de Gestão para Médicos")
