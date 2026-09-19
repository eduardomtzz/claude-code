#!/usr/bin/env python3
"""Planilha 5 do Kit Completo: Ata e Pendências. Gera 05-ata-e-pendencias.xlsx"""
from ssg import *
from datetime import date
NR=100; NP=300; R0=5; RR=R0+NR-1; RP=R0+NP-1
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche.",merge_to="F")
cfg["A4"]="Equipe ou empresa"; cfg["B4"]="Prisma Comunicação (exemplo fictício)"
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]=date(2026,9,14)
cfg["C5"]="O exemplo está congelado em 14/09/2026, para os arquivos do kit mostrarem a mesma foto. Ao usar com os seus dados, troque por =HOJE()."; nota(cfg["C5"])
cfg["A6"]="Reunião selecionada (para o Resumo)"; cfg["B6"]="R-004"
for c in ("A4","A5","A6"): rotulo(cfg[c])
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],center=True)
cfg["C6"]="Escolha o código da reunião na lista; a aba Resumo monta o texto dela."; nota(cfg["C6"])
cfg["A8"]="Pessoas (até 12)"; rotulo(cfg["A8"])
for i in range(12): inp(cfg.cell(row=9+i,column=1))
widths(cfg,(36,30,50)); cfg.sheet_view.showGridLines=False
# ---------- Reuniões ----------
re_=wb.create_sheet("Reuniões")
titulo(re_,"Reuniões","Uma linha por reunião. O código é automático. Escreva as decisões em frases curtas, separadas por ponto e vírgula.",merge_to="G")
hdr(re_,4,["Código","Data","Assunto","Participantes","Decisões","Pendências abertas","Pendências atrasadas"])
HOJE="Config!$B$5"
for r in range(R0,RR+1):
    re_.cell(row=r,column=1,value=f'=IF(C{r}="","","R-"&TEXT(ROW()-{R0-1},"000"))'); calc(re_.cell(row=r,column=1))
    for c in (2,3,4,5): inp(re_.cell(row=r,column=c))
    re_.cell(row=r,column=2).number_format=DATA; re_.cell(row=r,column=2).alignment=Alignment(horizontal="center")
    re_.cell(row=r,column=5).alignment=Alignment(wrap_text=True,vertical="top")
    re_.cell(row=r,column=6,value=f'=IF(C{r}="","",COUNTIFS(Pendências!$A${R0}:$A${RP},A{r},Pendências!$F${R0}:$F${RP},"<>Feito"))'); calc(re_.cell(row=r,column=6))
    re_.cell(row=r,column=7,value=f'=IF(C{r}="","",COUNTIFS(Pendências!$A${R0}:$A${RP},A{r},Pendências!$H${R0}:$H${RP},"Atrasada"))'); calc(re_.cell(row=r,column=7))
dvd=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True); dvd.add(f"B{R0}:B{RR}"); re_.add_data_validation(dvd)
re_.conditional_formatting.add(f"G{R0}:G{RR}", FormulaRule(formula=[f'AND(ISNUMBER(G{R0}),G{R0}>0)'], font=F(color="C8402E",size=10,bold=True)))
widths(re_,(9,11,32,26,60,11,11)); re_.freeze_panes="C5"; re_.sheet_view.showGridLines=False; re_.auto_filter.ref=f"A4:G{RR}"
# ---------- Pendências ----------
pe=wb.create_sheet("Pendências")
titulo(pe,"Pendências","Uma linha por pendência. Reunião e dono vêm de listas; situação e dias são calculados. Ao concluir, mude o status para Feito.",merge_to="J")
hdr(pe,4,["Reunião","Pendência","Dono","Prazo","Prioridade","Status","Concluída em","Situação","Dias","Chave"])
for r in range(R0,RP+1):
    for c in (1,2,3,4,5,6,7): inp(pe.cell(row=r,column=c))
    for c in (1,3,4,5,6,7): pe.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    pe.cell(row=r,column=4).number_format=DATA; pe.cell(row=r,column=7).number_format=DATA
    pe.cell(row=r,column=8,value=f'=IF(B{r}="","",IF(F{r}="Feito","Feita",IF(D{r}="","Sem prazo",IF(D{r}<{HOJE},"Atrasada",IF(D{r}={HOJE},"Hoje",IF(D{r}-{HOJE}<=7,"Esta semana","No prazo"))))))'); calc(pe.cell(row=r,column=8))
    pe.cell(row=r,column=9,value=f'=IF(OR(B{r}="",F{r}="Feito",D{r}=""),"",D{r}-{HOJE})'); calc(pe.cell(row=r,column=9),"0")
    pe.cell(row=r,column=10,value=f'=IF(OR(B{r}="",F{r}="Feito"),0,IF(H{r}="Atrasada",3000+MIN({HOJE}-D{r},60),IF(H{r}="Hoje",2500,IF(H{r}="Esta semana",2000-(D{r}-{HOJE}),IF(H{r}="Sem prazo",500,1000-MIN(D{r}-{HOJE},900)))))+IF(E{r}="Alta",200,IF(E{r}="Média",100,0))-ROW()/100000)'); pe.cell(row=r,column=10).font=F(color=CINZA,size=9)
dvs=[lista(f"=Reuniões!$A${R0}:$A${RR}",strict=True), lista("=Config!$A$9:$A$20",strict=True), lista('"Alta,Média,Baixa"'), lista('"A fazer,Fazendo,Feito"'),
     DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True)]
for dv,rng in zip(dvs,[f"A{R0}:A{RP}",f"C{R0}:C{RP}",f"E{R0}:E{RP}",f"F{R0}:F{RP}",f"D{R0}:D{RP}"]): dv.add(rng); pe.add_data_validation(dv)
dvs[4].add(f"G{R0}:G{RP}")
pe.conditional_formatting.add(f"A{R0}:I{RP}", FormulaRule(formula=[f'$H{R0}="Atrasada"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
pe.conditional_formatting.add(f"A{R0}:I{RP}", FormulaRule(formula=[f'$H{R0}="Hoje"'], fill=fill("FFF4CC")))
pe.conditional_formatting.add(f"A{R0}:I{RP}", FormulaRule(formula=[f'$H{R0}="Feita"'], font=F(color="8A86A0",size=10)))
widths(pe,(10,44,14,11,11,10,12,13,7,6)); pe.column_dimensions["J"].hidden=True
pe.freeze_panes="C5"; pe.sheet_view.showGridLines=False; pe.auto_filter.ref=f"A4:I{RP}"
# exemplos
for i,v in enumerate(["Ana","Bruno","Carla","Diego","Marina (cliente)"]): cfg.cell(row=9+i,column=1,value=v)
reun=[(date(2026,8,24),"Semanal da equipe","Ana; Bruno; Carla; Diego","Priorizar o site da Loja Verde; Bruno assume o layout; contratar freela de motion só se a campanha do Bistrô for aprovada"),
      (date(2026,8,31),"Semanal da equipe","Ana; Bruno; Carla","Adiar a newsletter para outubro; Carla escreve os textos do site até 12/09"),
      (date(2026,9,3),"Kickoff · Relatório anual Horizonte","Ana; Marina (cliente)","Relatório em PDF de 24 páginas; entrega em 30/09; Marina manda os números até 12/09; uma rodada de revisão"),
      (date(2026,9,10),"Semanal da equipe","Ana; Bruno; Carla; Diego","Manual da Padaria atrasou: Carla fecha até 15/09; Diego prepara o servidor do site; reunião com o Bistrô na quarta")]
for i,(d,a,p_,dec) in enumerate(reun):
    for c,v in zip((2,3,4,5),(d,a,p_,dec)): re_.cell(row=R0+i,column=c,value=v)
pend=[("R-001","Enviar proposta de motion para o Bistrô","Ana",date(2026,8,28),"Média","Feito",date(2026,8,27)),
      ("R-001","Definir paleta do site da Loja Verde","Bruno",date(2026,8,29),"Alta","Feito",date(2026,8,29)),
      ("R-002","Escrever os textos das 5 páginas do site","Carla",date(2026,9,12),"Alta","Fazendo",None),
      ("R-002","Avisar a lista que a newsletter volta em outubro","Ana",date(2026,9,5),"Baixa","Feito",date(2026,9,4)),
      ("R-003","Enviar os números do ano para o relatório","Marina (cliente)",date(2026,9,12),"Alta","Feito",date(2026,9,12)),
      ("R-003","Montar a estrutura do relatório (sumário)","Ana",date(2026,9,9),"Alta","Feito",date(2026,9,9)),
      ("R-003","Enviar 3 referências de diagramação","Bruno",date(2026,9,16),"Média","A fazer",None),
      ("R-004","Fechar o manual da marca da Padaria","Carla",date(2026,9,15),"Alta","Fazendo",None),
      ("R-004","Preparar o servidor e o domínio do site","Diego",date(2026,9,18),"Média","A fazer",None),
      ("R-004","Confirmar a reunião de quarta com o Bistrô","Ana",date(2026,9,11),"Média","A fazer",None),
      ("R-004","Levantar custo do freela de motion","Ana",date(2026,9,13),"Baixa","A fazer",None),
      ("R-004","Revisar a proposta comercial da Aurora","Ana",None,"Média","A fazer",None)]
for i,row in enumerate(pend):
    for c,v in enumerate(row,start=1):
        if v is not None: pe.cell(row=R0+i,column=c,value=v)
# ---------- Em aberto ----------
p=wb.create_sheet("Em aberto",0)
p["A1"]='=Config!B4&" · pendências em "&TEXT(DAY(Config!B5),"00")&"/"&TEXT(MONTH(Config!B5),"00")&"/"&YEAR(Config!B5)'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:H1")
p["A2"]="Nada para preencher aqui: tudo vem de Reuniões e Pendências."; nota(p["A2"]); p.merge_cells("A2:H2")
PA=f"Pendências!$A${R0}:$A${RP}"; PB=f"Pendências!$B${R0}:$B${RP}"; PC=f"Pendências!$C${R0}:$C${RP}"; PD=f"Pendências!$D${R0}:$D${RP}"; PE_=f"Pendências!$E${R0}:$E${RP}"; PF=f"Pendências!$F${R0}:$F${RP}"; PH=f"Pendências!$H${R0}:$H${RP}"; PI=f"Pendências!$I${R0}:$I${RP}"; PJ=f"Pendências!$J${R0}:$J${RP}"
kpi(p,4,1,"Abertas",f'=COUNTIFS({PB},"<>",{PF},"<>Feito")',LAVANDA,UVA)
kpi(p,4,3,"Atrasadas",f'=COUNTIFS({PH},"Atrasada")',VERM,VERM_T)
kpi(p,4,5,"Para hoje",f'=COUNTIFS({PH},"Hoje")',SOL,UVA)
kpi(p,4,7,"Feitas no total",f'=COUNTIFS({PF},"Feito")',VERDE,VERDE_T)
p["A7"]="O que cobrar primeiro"; p["A7"].font=F(bold=True,size=13,color=UVA)
p["A8"]="Ordem: atrasadas, hoje, esta semana; dentro de cada grupo, prioridade alta primeiro."; nota(p["A8"])
hdr(p,9,["#","Pendência","Dono","Prazo","Situação","Prioridade","Reunião","Dias"])
TOP=15
for k in range(1,TOP+1):
    r=9+k; m=f'MATCH(LARGE({PJ},{k}),{PJ},0)'; g=f'LARGE({PJ},{k})>0'
    p.cell(row=r,column=1,value=k)
    for col,rng in zip((2,3,4,5,6,7,8),(PB,PC,PD,PH,PE_,PA,PI)):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},IF(INDEX({rng},{m})="","",INDEX({rng},{m})),""),"")')
    for col in range(1,9): calc(p.cell(row=r,column=col),center=(col!=2))
    p.cell(row=r,column=4).number_format=DATA; p.cell(row=r,column=8).number_format="0"
p.conditional_formatting.add(f"A10:H{9+TOP}", FormulaRule(formula=['$E10="Atrasada"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
p.conditional_formatting.add(f"A10:H{9+TOP}", FormulaRule(formula=['$E10="Hoje"'], fill=fill("FFF4CC")))
r0=11+TOP
p.cell(row=r0,column=1,value="Por pessoa").font=F(bold=True,size=13,color=UVA)
hdr(p,r0+1,["Pessoa","Abertas","Atrasadas","Esta semana","Feitas","Próximo prazo"])
for i in range(12):
    r=r0+2+i; src=f"Config!$A${9+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({PC},{src},{PB},"<>",{PF},"<>Feito"))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({PC},{src},{PH},"Atrasada"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({PC},{src},{PH},"Esta semana")+COUNTIFS({PC},{src},{PH},"Hoje"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({PC},{src},{PF},"Feito"))'); calc(p.cell(row=r,column=5))
    # Menor prazo com condição sem MINIFS: 1E+10 nas linhas que não casam.
    cond=f'({PC}={src})*({PF}<>"Feito")*({PB}<>"")*({PD}<>"")'
    mf=f'SUMPRODUCT(MIN({cond}*{PD}+(1-{cond})*1E+10))'
    p.cell(row=r,column=6,value=f'=IF({src}="","",IFERROR(IF(OR({mf}=0,{mf}>=1E+10),"",{mf}),""))'); calc(p.cell(row=r,column=6),DATA)
p.conditional_formatting.add(f"C{r0+2}:C{r0+13}", FormulaRule(formula=[f'AND(ISNUMBER(C{r0+2}),C{r0+2}>0)'], font=F(color="C8402E",size=10,bold=True)))
widths(p,(6,46,16,12,13,11,10,8)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Resumo para a IA ----------
s=wb.create_sheet("Resumo",1)
s["A1"]='="Resumo da reunião "&Config!B6&" · "&IFERROR(INDEX(Reuniões!$C$5:$C$104,MATCH(Config!B6,Reuniões!$A$5:$A$104,0)),"")'; s["A1"].font=F(bold=True,size=16,color=UVA); s.merge_cells("A1:F1")
s["A2"]="Escolha a reunião em Config. Copie o bloco abaixo e cole no prompt \"Escrever 07: resumo de reunião para quem não foi\" ou \"Escrever 02: e-mail curto que pede algo\"."; nota(s["A2"]); s.merge_cells("A2:F2")
SEL="Config!$B$6"; RA=f"Reuniões!$A${R0}:$A${RR}"
def campo(col): return f'IFERROR(INDEX(Reuniões!${col}${R0}:${col}${RR},MATCH({SEL},{RA},0)),"")'
s["A4"]="Data"; s["B4"]=f'={campo("B")}'; s["B4"].number_format=DATA
s["A5"]="Assunto"; s["B5"]=f'={campo("C")}'
s["A6"]="Participantes"; s["B6"]=f'={campo("D")}'
s["A7"]="Decisões"; s["B7"]=f'={campo("E")}'
for r in (4,5,6,7): rotulo(s.cell(row=r,column=1)); s.cell(row=r,column=2).font=F(size=10,color=TINTA); s.cell(row=r,column=2).alignment=Alignment(wrap_text=True,vertical="top",horizontal="left"); s.merge_cells(start_row=r,start_column=2,end_row=r,end_column=6)
s.row_dimensions[7].height=48
s["A9"]="Pendências desta reunião"; s["A9"].font=F(bold=True,size=13,color=UVA)
hdr(s,10,["#","Pendência","Dono","Prazo","Status","Situação"])
for k in range(1,21):
    r=10+k
    m=f'SMALL(IF({PA}={SEL},ROW({PA})-{R0-1}),{k})'
    # sem fórmula matricial: usamos a coluna auxiliar de ordem
    s.cell(row=r,column=1,value=k)
    for col,letter in zip((2,3,4,5,6),("B","C","D","F","H")):
        ix=f'INDEX(Pendências!${letter}${R0}:${letter}${RP},MATCH({k},Pendências!$K${R0}:$K${RP},0))'
        s.cell(row=r,column=col,value=f'=IFERROR(IF({ix}="","",{ix}),"")')
    for col in range(1,7): calc(s.cell(row=r,column=col),center=(col!=2))
    s.cell(row=r,column=4).number_format=DATA
# coluna auxiliar K em Pendências: ordem dentro da reunião selecionada
for r in range(R0,RP+1):
    pe.cell(row=r,column=11,value=f'=IF(AND(B{r}<>"",A{r}={SEL}),COUNTIFS($A${R0}:A{r},{SEL},$B${R0}:B{r},"<>"),"")'); pe.cell(row=r,column=11).font=F(color=CINZA,size=9)
pe.column_dimensions["K"].hidden=True
s["A32"]="Bloco único para copiar"; s["A32"].font=F(bold=True,size=13,color=UVA)
# Concatenação das pendências sem TEXTJOIN (que exige Excel > 2016 perpétuo):
# coluna H oculta, cumulativa linha a linha, e no fim se corta o separador sobrando.
for k in range(1,21):
    r=10+k
    item=(f'IF(B{r}="","",B{r}&" (dono: "&C{r}&"; prazo: "&IF(D{r}="","sem prazo",TEXT(DAY(D{r}),"00")&"/"&TEXT(MONTH(D{r}),"00"))'
          f'&IF(F{r}="Sem prazo","","; "&LOWER(F{r}))&") | ")')
    ant=f'H{r-1}' if k>1 else '""'
    s.cell(row=r,column=8,value=f'={ant}&{item}').font=F(color=CINZA,size=9)
s.column_dimensions["H"].hidden=True
pend='IF(LEN(H30)>3,LEFT(H30,LEN(H30)-3),"nenhuma")'
s["A33"]=f'="Reunião: "&B5&" · "&TEXT(DAY(B4),"00")&"/"&TEXT(MONTH(B4),"00")&"/"&YEAR(B4)&CHAR(10)&"Participantes: "&B6&CHAR(10)&"Decisões: "&B7&CHAR(10)&"Pendências: "&{pend}'
s["A33"].font=F(size=10,color=TINTA); s["A33"].alignment=Alignment(wrap_text=True,vertical="top"); s.merge_cells("A33:F40"); s["A33"].border=borda
widths(s,(6,46,16,12,10,13)); s.sheet_view.showGridLines=False
dvsel=lista(f"=Reuniões!$A${R0}:$A${RR}",strict=True); dvsel.add("B6"); cfg.add_data_validation(dvsel)
como_usar(wb,"Ata e Pendências",[
 ("O que esta planilha faz","Registra cada reunião (data, assunto, participantes, decisões) e cada pendência com dono e prazo. Mostra o que cobrar primeiro, a carga por pessoa e monta o resumo pronto para a IA transformar em e-mail ou ata."),
 ("Passo 1","Em Config, preencha o nome da equipe e as pessoas. Troque a data de referência por =HOJE() (no exemplo ela está congelada em 14/09/2026)."),
 ("Passo 2","Em Reuniões, uma linha por reunião. Escreva as decisões em frases curtas separadas por ponto e vírgula. O código (R-001, R-002...) é automático."),
 ("Passo 3","Em Pendências, uma linha por tarefa que saiu da reunião: reunião (lista), pendência, dono (lista), prazo, prioridade e status. Ao concluir, mude o status para Feito."),
 ("Passo 4","Em Em aberto, veja o que cobrar primeiro e a carga por pessoa. Em Resumo, escolha a reunião em Config e copie o bloco único."),
 ("Rotina","Logo depois da reunião, 5 minutos para registrar. Segunda de manhã, olhe Em aberto e cobre por e-mail com o prompt \"Escrever 02\"."),
 ("Com a IA","Bloco único da aba Resumo + prompt \"Escrever 07: resumo de reunião para quem não foi\". Para cobrar uma pendência atrasada: \"Escrever 10: mensagem de cobrança educada\"."),
])
proteger(wb); salvar(wb,"05-ata-e-pendencias.xlsx","Ata e Pendências · Kit IA no Trabalho Completo")
