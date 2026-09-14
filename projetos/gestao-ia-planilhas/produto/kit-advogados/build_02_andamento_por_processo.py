#!/usr/bin/env python3
"""Planilha 2 do Kit de Gestão para Advogados: Andamento por processo. Gera 02-andamento-por-processo.xlsx"""
from ssg import *
import dados
N=300; R0=5; RN=R0+N-1; NL=10; TOP=12
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Fases, áreas e responsáveis aparecem nas listas da aba Processos.",merge_to="H")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]="=TODAY()"
cfg["A6"]="Considerar parado após (dias sem atualização)"; cfg["B6"]=30
for c in ("A4","A5","A6"): rotulo(cfg[c])
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],center=True)
cfg["C5"]="Deixe =HOJE() para acompanhar o dia; troque por uma data para simular outro dia."; nota(cfg["C5"])
cfg["C6"]="Caso sem atualização há mais dias do que isso aparece como parado no Painel."; nota(cfg["C6"])
cfg["A9"]=f"Fases (até {NL})"; cfg["D9"]=f"Áreas (até {NL})"; cfg["F9"]=f"Responsáveis (até {NL})"
for c in ("A9","D9","F9"): rotulo(cfg[c])
for i in range(NL):
    for col in (2,4,6): inp(cfg.cell(row=10+i,column=col))
for i,v in enumerate(dados.FASES): cfg.cell(row=10+i,column=2,value=v)
for i,v in enumerate(dados.AREAS): cfg.cell(row=10+i,column=4,value=v)
for i,(n,_,_,_) in enumerate(dados.PESSOAS): cfg.cell(row=10+i,column=6,value=n)
cfg["A21"]="Preencha de cima para baixo, sem pular linha: as listas suspensas param na última linha preenchida."; nota(cfg["A21"])
cfg["A22"]="Mantenha a fase \"Encerrado\" com esse nome: é ela que tira o caso das contagens de ativos."; nota(cfg["A22"])
widths(cfg,(44,20,4,20,4,20,4,4)); cfg.sheet_view.showGridLines=False
# ---------- Processos ----------
ps=wb.create_sheet("Processos")
titulo(ps,"Processos","Uma linha por caso (copie o cadastro da planilha 13 · Carteira, aba Casos: a 13 é a fonte). Preencha as colunas amarelas; dias, situação e parado são calculados. A cada movimentação, atualize a fase, a próxima ação e a data da última atualização.",merge_to="N")
hdr(ps,4,["Número","Cliente","Área","Fase","Responsável","Próxima ação","Data da próxima ação","Última atualização","Observação","Dias para a ação","Situação","Dias sem atualizar","Parado?","Chave"])
HOJE="Config!$B$5"; PAR="Config!$B$6"
for r in range(R0,RN+1):
    for c in range(1,10): inp(ps.cell(row=r,column=c))
    for c in (3,4,5,7,8): ps.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    ps.cell(row=r,column=7).number_format=DATA; ps.cell(row=r,column=8).number_format=DATA
    ps.cell(row=r,column=11,value=f'=IF(A{r}="","",IF(D{r}="Encerrado","Encerrado",IF(G{r}="","Sem próxima ação",IF(G{r}<{HOJE},"Atrasado",IF(G{r}={HOJE},"Hoje",IF(G{r}-{HOJE}<=7,"Esta semana","Em dia"))))))'); calc(ps.cell(row=r,column=11))
    ps.cell(row=r,column=10,value=f'=IF(OR(K{r}="",K{r}="Encerrado",K{r}="Sem próxima ação"),"",G{r}-{HOJE})'); calc(ps.cell(row=r,column=10),"0")
    ps.cell(row=r,column=12,value=f'=IF(OR(A{r}="",D{r}="Encerrado",H{r}=""),"",{HOJE}-H{r})'); calc(ps.cell(row=r,column=12),"0")
    ps.cell(row=r,column=13,value=f'=IF(L{r}="","",IF(L{r}>{PAR},"Sim",""))'); calc(ps.cell(row=r,column=13))
    ps.cell(row=r,column=14,value=f'=IF(M{r}="Sim",L{r}-ROW()/100000,0)'); ps.cell(row=r,column=14).font=F(color=CINZA,size=9)
def off(col): return f"=OFFSET(Config!${col}$10,0,0,MAX(1,COUNTA(Config!${col}$10:${col}${9+NL})),1)"
dva=lista(off("D"),strict=False); dva.add(f"C{R0}:C{RN}")
dvf=lista(off("B"),strict=False); dvf.add(f"D{R0}:D{RN}")
dvr=lista(off("F"),strict=False); dvr.add(f"E{R0}:E{RN}")
dvd=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True); dvd.add(f"G{R0}:H{RN}")
for dv in (dva,dvf,dvr,dvd): ps.add_data_validation(dv)
ps.conditional_formatting.add(f"A{R0}:M{RN}", FormulaRule(formula=[f'$K{R0}="Atrasado"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
ps.conditional_formatting.add(f"A{R0}:M{RN}", FormulaRule(formula=[f'$K{R0}="Hoje"'], fill=fill(SOL), font=F(color=UVA,size=10,bold=True)))
ps.conditional_formatting.add(f"A{R0}:M{RN}", FormulaRule(formula=[f'$K{R0}="Esta semana"'], fill=fill("FFF4CC")))
ps.conditional_formatting.add(f"A{R0}:M{RN}", FormulaRule(formula=[f'$K{R0}="Encerrado"'], font=F(color="8A86A0",size=10)))
ps.conditional_formatting.add(f"M{R0}:M{RN}", FormulaRule(formula=[f'$M{R0}="Sim"'], font=F(color="C8402E",size=10,bold=True)))
widths(ps,(28,26,14,12,16,36,13,13,30,10,16,11,9,6)); ps.column_dimensions["N"].hidden=True
ps.freeze_panes="C5"; ps.sheet_view.showGridLines=False; ps.auto_filter.ref=f"A4:M{RN}"
# exemplos: os 38 casos de dados.py; a próxima ação é o prazo principal do caso (o mesmo da planilha 01), coerente com a fase
ACAO={"Audiência de conciliação":"Audiência de conciliação (confirmar presença do cliente)","Audiência de instrução":"Audiência de instrução (avisar testemunhas)",
      "Reunião com cliente":"Reunião com o cliente","Juntada de documentos":"Juntar documentos enviados pelo cliente","Entrega de parecer":"Entregar o parecer ao cliente",
      "Minuta de acordo":"Enviar a minuta de acordo","Homologação do acordo":"Acompanhar a homologação do acordo","Cumprimento de sentença":"Iniciar o cumprimento de sentença",
      "Manifestação sobre a penhora":"Manifestar sobre a penhora"}
for i,c in enumerate(dados.CASOS):
    r=R0+i; fase=c["fase"]; d=c["proximo_prazo_dias"]
    acao=""; dt=None; obs=dados.OBS_ANDAMENTO.get(c["chave"],"")
    if fase!="Encerrado":
        desc=c["descricao_prazo"]; acao=ACAO.get(desc,f"Protocolar: {desc.lower()}")
    if d is not None: dt=dados.prazo_formula(d)
    if fase=="Encerrado": ult=c["encerramento"]; obs=obs or "Encerrado; conferir checklist de encerramento"
    else: ult=dados.prazo_formula(-c["ultima_atualizacao_dias"])
    vals=(c["numero"],c["cliente"],c["area"],fase,c["responsavel"],acao,dt,ult,obs)
    for col,v in enumerate(vals,start=1):
        if v not in ("",None): ps.cell(row=r,column=col,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Andamento dos processos · "&TEXT(Config!$B$5,"dd/mm/yyyy")',"Nada para digitar aqui: tudo vem de Config e Processos.",merge_to="L")
PA=f"Processos!$A${R0}:$A${RN}"; PB=f"Processos!$B${R0}:$B${RN}"; PC=f"Processos!$C${R0}:$C${RN}"; PD=f"Processos!$D${R0}:$D${RN}"; PE_=f"Processos!$E${R0}:$E${RN}"
PF=f"Processos!$F${R0}:$F${RN}"; PG=f"Processos!$G${R0}:$G${RN}"; PH=f"Processos!$H${R0}:$H${RN}"; PK=f"Processos!$K${R0}:$K${RN}"; PL=f"Processos!$L${R0}:$L${RN}"; PM=f"Processos!$M${R0}:$M${RN}"; PN=f"Processos!$N${R0}:$N${RN}"
kpi(p,4,1,"Casos ativos",f'=COUNTIFS({PA},"<>",{PD},"<>Encerrado")',LAVANDA,UVA)
kpi(p,4,3,"Ação atrasada",f'=COUNTIFS({PK},"Atrasado")',VERM,VERM_T)
kpi(p,4,5,"Ação hoje ou esta semana",f'=COUNTIFS({PK},"Hoje")+COUNTIFS({PK},"Esta semana")',SOL,UVA)
kpi(p,4,7,"Sem próxima ação",f'=COUNTIFS({PK},"Sem próxima ação")',"FFE9A8",UVA)
kpi(p,4,9,f'="Parados há mais de "&{PAR}&" dias"',f'=COUNTIFS({PM},"Sim")',VERM,VERM_T)
kpi(p,4,11,"Encerrados",f'=COUNTIFS({PA},"<>",{PD},"Encerrado")',VERDE,VERDE_T)
p["A7"]="Por fase"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Fase","Casos","Ação atrasada","Esta semana","Sem próxima ação","Parados"])
for i in range(NL):
    r=9+i; src=f"Config!$B${10+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({PA},"<>",{PD},{src}))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({PD},{src},{PK},"Atrasado"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({PD},{src},{PK},"Hoje")+COUNTIFS({PD},{src},{PK},"Esta semana"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({PD},{src},{PK},"Sem próxima ação"))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF({src}="","",COUNTIFS({PD},{src},{PM},"Sim"))'); calc(p.cell(row=r,column=6))
p.conditional_formatting.add(f"C9:C{8+NL}", FormulaRule(formula=['AND(ISNUMBER(C9),C9>0)'], font=F(color="C8402E",size=10,bold=True)))
p.conditional_formatting.add(f"F9:F{8+NL}", FormulaRule(formula=['AND(ISNUMBER(F9),F9>0)'], font=F(color="C8402E",size=10,bold=True)))
# Por área (à direita)
p["H7"]="Por área"; p["H7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Área","Ativos","Encerrados","Ação atrasada","Parados"],start=8)
for i in range(NL):
    r=9+i; src=f"Config!$D${10+i}"
    p.cell(row=r,column=8,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=8),center=False)
    p.cell(row=r,column=9,value=f'=IF({src}="","",COUNTIFS({PA},"<>",{PC},{src},{PD},"<>Encerrado"))'); calc(p.cell(row=r,column=9))
    p.cell(row=r,column=10,value=f'=IF({src}="","",COUNTIFS({PC},{src},{PD},"Encerrado"))'); calc(p.cell(row=r,column=10))
    p.cell(row=r,column=11,value=f'=IF({src}="","",COUNTIFS({PC},{src},{PK},"Atrasado"))'); calc(p.cell(row=r,column=11))
    p.cell(row=r,column=12,value=f'=IF({src}="","",COUNTIFS({PC},{src},{PM},"Sim"))'); calc(p.cell(row=r,column=12))
p.conditional_formatting.add(f"K9:L{8+NL}", FormulaRule(formula=['AND(ISNUMBER(K9),K9>0)'], font=F(color="C8402E",size=10,bold=True)))
r0=9+NL+2
p.cell(row=r0,column=1,value="Por responsável").font=F(bold=True,size=13,color=UVA)
hdr(p,r0+1,["Responsável","Casos ativos","Ação atrasada","Esta semana","Sem próxima ação","Parados","Próxima ação a partir de hoje"])
for i in range(NL):
    r=r0+2+i; src=f"Config!$F${10+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({PA},"<>",{PE_},{src},{PD},"<>Encerrado"))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PK},"Atrasado"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PK},"Hoje")+COUNTIFS({PE_},{src},{PK},"Esta semana"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PK},"Sem próxima ação"))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PM},"Sim"))'); calc(p.cell(row=r,column=6))
    # menor data de ação de hoje em diante, sem MÍNIMOSES (Excel 2016 e Google Sheets): datas fora da condição viram 1E+10 e saem do MIN
    cond=f'(({PE_}={src})*({PD}<>"Encerrado")*({PG}>={HOJE}))'
    mf=f'SUMPRODUCT(MIN({cond}*{PG}+(1-{cond})*1E+10))'
    p.cell(row=r,column=7,value=f'=IF({src}="","",IFERROR(IF({mf}>=1E+10,"",{mf}),""))'); calc(p.cell(row=r,column=7),DATA)
p.conditional_formatting.add(f"C{r0+2}:C{r0+1+NL}", FormulaRule(formula=[f'AND(ISNUMBER(C{r0+2}),C{r0+2}>0)'], font=F(color="C8402E",size=10,bold=True)))
p.cell(row=r0+2+NL,column=1,value="Próxima ação a partir de hoje: a data mais próxima entre as ações de hoje em diante; as atrasadas estão na coluna \"Ação atrasada\".").font=F(size=9,color=LILAS)
r1=r0+NL+4
p.cell(row=r1,column=1,value=f'="Parados há mais de "&{PAR}&" dias (os mais antigos primeiro)"').font=F(bold=True,size=13,color=UVA)
p.cell(row=r1+1,column=1,value=f"Mostra os {TOP} casos ativos há mais tempo sem atualização. Um caso parado pode estar apenas aguardando o andamento; o painel avisa para que alguém confira.").font=F(size=9,color=LILAS); p.merge_cells(start_row=r1+1,start_column=1,end_row=r1+1,end_column=12)
hdr(p,r1+2,["#","Número","Cliente","Fase","Responsável","Última atualização","Dias parado","Próxima ação"])
for k in range(1,TOP+1):
    r=r1+2+k; m=f'MATCH(LARGE({PN},{k}),{PN},0)'; g=f'LARGE({PN},{k})>0'
    p.cell(row=r,column=1,value=k)
    for col,rng_ in zip((2,3,4,5,6,7,8),(PA,PB,PD,PE_,PH,PL,PF)):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},IF(INDEX({rng_},{m})="","",INDEX({rng_},{m})),""),"")')
    for col in range(1,9): calc(p.cell(row=r,column=col),center=(col not in (2,3,8)))
    p.cell(row=r,column=6).number_format=DATA; p.cell(row=r,column=7).number_format="0"
p.conditional_formatting.add(f"A{r1+3}:H{r1+2+TOP}", FormulaRule(formula=[f'AND(ISNUMBER($G{r1+3}),$G{r1+3}>0)'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
widths(p,(22,12,13,12,16,12,14,18,10,11,13,10)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Como usar ----------
como_usar(wb,"Andamento por processo",[
 ("O que esta planilha faz","Uma linha por caso com fase, responsável, próxima ação e data. O Painel mostra quantos casos há em cada fase e área, a carga de cada pessoa e quais casos estão parados há mais tempo sem atualização."),
 ("Passo 1","Em Config, confira a data de referência (fica em =HOJE()), o número de dias para considerar um caso parado, e as listas de fases, áreas e responsáveis. Preencha de cima para baixo, sem pular linha."),
 ("Passo 2","Em Processos, apague os exemplos e cadastre os seus casos: número, cliente, área, fase, responsável, próxima ação com data, e a data da última atualização. O cadastro (número, cliente, área, fase, responsável) é o mesmo da planilha 13 · Carteira: copie de lá e mantenha a 13 como fonte."),
 ("Passo 3","A cada movimentação, atualize a fase, a próxima ação e a data da última atualização. Ao encerrar, mude a fase para Encerrado: o caso sai das contagens de ativos."),
 ("Passo 4","Em Painel, confira os casos com ação atrasada, os sem próxima ação (ninguém sabe o próximo passo) e os parados há mais de N dias."),
 ("Rotina de segunda","5 minutos depois da Agenda de prazos: casos parados e sem próxima ação. Decida a ação e a data; se o caso só aguarda o andamento, registre isso na observação e atualize a data."),
 ("Exemplo","Caso consultivo não tem número de processo (referência CONS-ano-nº) e a próxima ação é entrega de parecer ou reunião. A próxima ação de cada caso é coerente com a fase (inicial: contestação, réplica, juntada, conciliação; instrução: audiência, laudo, alegações finais; sentença: embargos, recurso; recurso: contrarrazões; execução: cumprimento, penhora; acordo: minuta, homologação)."),
 ("Com a IA","Copie a tabela \"Parados\" ou \"Por responsável\" e use o prompt \"Prazos 05 · Resumo de andamento para o sócio\" da biblioteca do kit."),
])
proteger(wb); salvar(wb,"02-andamento-por-processo.xlsx","Andamento por processo · Kit de Gestão para Advogados")
