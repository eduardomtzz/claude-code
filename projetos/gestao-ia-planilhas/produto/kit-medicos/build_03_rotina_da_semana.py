#!/usr/bin/env python3
"""Planilha 3 do Kit de Gestão para Médicos: Rotina da semana da clínica (segunda: agenda; sexta: caixa e painel). Gera 03-rotina-da-semana.xlsx"""
from ssg import *
import dados, random
from datetime import date
NI=24; R0=5; RI=R0+NI-1; W=52; C0=5; CW=C0+W-1; NRESP=10
LW=L(CW); RT=RI+2
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche.",merge_to="F")
cfg["A4"]="Clínica"; cfg["B4"]=f"{dados.CLINICA} (exemplo fictício)"
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]="=TODAY()"
cfg["A6"]="Segunda-feira da semana 1"; cfg["B6"]=date(2026,1,5)
for c in ("A4","A5","A6"): rotulo(cfg[c])
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],DATA)
cfg["C5"]="Deixe =HOJE() para acompanhar o dia; troque por uma data para simular outro dia."; nota(cfg["C5"])
cfg["C6"]="Sugestão: a primeira segunda-feira do ano. As 52 colunas da aba Rotina contam a partir daqui. O exemplo está preenchido de 20/07 a 07/09/2026 (S29 a S36)."; nota(cfg["C6"])
cfg["C7"]="Virada do ano: em janeiro de 2027, salve uma cópia desta planilha, troque a data acima pela primeira segunda-feira de 2027 (04/01/2027) e limpe as marcações da aba Rotina. As 52 semanas recomeçam."; nota(cfg["C7"])
cfg["A8"]=f"Responsáveis (até {NRESP})"; rotulo(cfg["A8"])
for i in range(NRESP): inp(cfg.cell(row=9+i,column=2))
for i,n in enumerate((dados.CAR,dados.PAU,dados.BRU)): cfg.cell(row=9+i,column=2,value=n)
cfg["A20"]="Preencha de cima para baixo, sem pular linha: a lista suspensa para na última linha preenchida."; nota(cfg["A20"])
widths(cfg,(30,26,90,4,4,4)); cfg.sheet_view.showGridLines=False
# ---------- Rotina ----------
ro=wb.create_sheet("Rotina")
titulo(ro,"Rotina da semana","Linhas: as rotinas fixas de segunda (agenda) e de sexta (caixa e painel). Colunas: uma por semana. Marque Sim ou Não em cada semana; os totais e o Painel são calculados.",merge_to="D")
HOJE="Config!$B$5"; INI="Config!$B$6"
hdr(ro,4,["Dia","Rotina","Minutos","Responsável"])
for k in range(1,W+1):
    col=C0+k-1
    a=ro.cell(row=2,column=col,value=k); a.font=F(size=8,color=CINZA); a.alignment=Alignment(horizontal="center")
    b=ro.cell(row=3,column=col,value=f"={INI}+{7*(k-1)}"); b.number_format="dd/mm"; b.font=F(size=8,color=LILAS); b.alignment=Alignment(horizontal="center")
    c=ro.cell(row=4,column=col,value=f"S{k}"); c.font=F(bold=True,color=BRANCO,size=9); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center",vertical="center"); c.border=borda
ro["A3"]="Semana começa em"; nota(ro["A3"]); ro["A3"].alignment=Alignment(horizontal="right")
for r in range(R0,RI+1):
    for c in (1,2,3,4): inp(ro.cell(row=r,column=c))
    ro.cell(row=r,column=1).alignment=Alignment(horizontal="center"); ro.cell(row=r,column=3).alignment=Alignment(horizontal="center"); ro.cell(row=r,column=4).alignment=Alignment(horizontal="center")
    for k in range(W): inp(ro.cell(row=r,column=C0+k),center=True)
rot=[("Feitas na semana",f'=COUNTIF({{c}}{R0}:{{c}}{RI},"Sim")'),
     ("Registradas (Sim ou Não)",f'=COUNTIF({{c}}{R0}:{{c}}{RI},"Sim")+COUNTIF({{c}}{R0}:{{c}}{RI},"Não")'),
     ("Planejadas",f'=COUNTA($B${R0}:$B${RI})'),
     ("% da semana",f'=IF({{c}}{RT+1}=0,"",{{c}}{RT}/{{c}}{RT+2})'),
     ("Minutos feitos",f'=SUMIF({{c}}{R0}:{{c}}{RI},"Sim",$C${R0}:$C${RI})')]
for j,(lab,fml) in enumerate(rot):
    r=RT+j; ro.cell(row=r,column=2,value=lab); rotulo(ro.cell(row=r,column=2))
    for k in range(W):
        c=ro.cell(row=r,column=C0+k,value=fml.format(c=L(C0+k))); calc(c, PCT if j==3 else "0")
ro.cell(row=RT+5,column=2,value="Sim = feita; Não = pulada; vazio = semana ainda não registrada. Só as semanas registradas entram no Painel.").font=F(size=9,color=LILAS)
dvd=lista('"Segunda,Terça,Quarta,Quinta,Sexta"'); dvd.add(f"A{R0}:A{RI}")
dvr=lista(f"=OFFSET(Config!$B$9,0,0,MAX(1,COUNTA(Config!$B$9:$B${8+NRESP})),1)",strict=False); dvr.add(f"D{R0}:D{RI}")
dvs=lista('"Sim,Não"'); dvs.add(f"{L(C0)}{R0}:{LW}{RI}")
dvm=DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True); dvm.add(f"C{R0}:C{RI}")
for dv in (dvd,dvr,dvs,dvm): ro.add_data_validation(dv)
rng=f"{L(C0)}{R0}:{LW}{RI}"
ro.conditional_formatting.add(rng, FormulaRule(formula=[f'{L(C0)}{R0}="Sim"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
ro.conditional_formatting.add(rng, FormulaRule(formula=[f'{L(C0)}{R0}="Não"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
ro.conditional_formatting.add(f"{L(C0)}3:{LW}4", FormulaRule(formula=[f'AND({L(C0)}$3<={HOJE},{L(C0)}$3+6>={HOJE})'], fill=fill(SOL), font=F(color=UVA,size=9,bold=True)))
ro.conditional_formatting.add(f"A{R0}:D{RI}", FormulaRule(formula=[f'$A{R0}="Sexta"'], fill=fill(LAVANDA)))
widths(ro,[10,56,9,22]+[6]*W); ro.freeze_panes=f"{L(C0)}{R0}"; ro.sheet_view.showGridLines=False
itens=[("Segunda","Abrir a Agenda (01): olhar as vagas dos próximos 7 dias e a ocupação da semana",4,dados.BRU),
       ("Segunda","Confirmar por mensagem os agendados da semana",3,dados.BRU),
       ("Segunda","Ligar ou mandar mensagem para a lista de retorno (02)",3,dados.BRU),
       ("Segunda","Registrar as faltas da semana passada e remarcar",2,dados.BRU),
       ("Sexta","Lançar os fechamentos do dia da semana no Caixa (09)",5,dados.CAR),
       ("Sexta","Marcar parcelas recebidas e enviar a cobrança educada (14)",4,dados.BRU),
       ("Sexta","Separar as guias da semana e atualizar os lotes (13)",3,dados.BRU),
       ("Sexta","Atualizar os orçamentos apresentados e aprovados (15)",3,dados.BRU),
       ("Sexta","Olhar o Painel da clínica (17) e anotar até 3 decisões",3,dados.PAU)]
assert sum(i[2] for i in itens)==30
for i,row in enumerate(itens):
    for col,v in enumerate(row,start=1): ro.cell(row=R0+i,column=col,value=v)
rng_=random.Random(25)
for k in range(29,37):
    for i in range(len(itens)):
        pr=0.9 if itens[i][0]=="Segunda" else 0.8
        if i==2: pr=0.6
        ro.cell(row=R0+i,column=C0+k-1,value="Sim" if rng_.random()<pr else "Não")
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Aderência à rotina · "&TEXT(Config!$B$5,"dd/mm/yyyy")',"Nada para digitar aqui: tudo vem de Config e Rotina. Aderência = rotinas feitas ÷ rotinas planejadas nas últimas 4 semanas registradas.",merge_to="H")
IDX=f"Rotina!${L(C0)}$2:${LW}$2"; DAT=f"Rotina!${L(C0)}$3:${LW}$3"; FEI=f"Rotina!${L(C0)}${RT}:${LW}${RT}"; REG=f"Rotina!${L(C0)}${RT+1}:${LW}${RT+1}"; PLA=f"Rotina!${L(C0)}${RT+2}:${LW}${RT+2}"; MIN_=f"Rotina!${L(C0)}${RT+4}:${LW}${RT+4}"
p["J4"]="Última semana registrada"; p["K4"]=f'=SUMPRODUCT(MAX(({REG}>0)*{IDX}))'
p["J5"]="Semana da data de referência"; p["K5"]=f'=MIN({W},MAX(1,INT(({HOJE}-{INI})/7)+1))'
p["J6"]="Semanas consideradas"; p["K6"]="=MIN(4,K4)"
p["J7"]="Rotinas planejadas"; p["K7"]=f'=COUNTA(Rotina!$B${R0}:$B${RI})'
for r in (4,5,6,7): nota(p.cell(row=r,column=10)); p.cell(row=r,column=11).font=F(size=9,color=LILAS); p.cell(row=r,column=11).alignment=Alignment(horizontal="center")
ULT="$K$4"; CUR="$K$5"; NS="$K$6"; NPL="$K$7"
kpi(p,4,1,"Aderência (últimas 4 semanas)",f'=IF(OR({ULT}=0,{NPL}=0),"",SUMPRODUCT(({IDX}>={ULT}-3)*({IDX}<={ULT})*{FEI})/({NS}*{NPL}))',LAVANDA,UVA,fmt="0%")
kpi(p,4,3,"Semana atual",f'="S"&{CUR}&" · "&TEXT({INI}+7*({CUR}-1),"dd/mm")',SOL,UVA,fmt="@")
kpi(p,4,5,"Última registrada",f'=IF({ULT}=0,"nenhuma","S"&{ULT}&" · "&TEXT({INI}+7*({ULT}-1),"dd/mm"))',LAVANDA,UVA,fmt="@")
kpi(p,4,7,"Minutos por semana",f'=SUM(Rotina!$C${R0}:$C${RI})',VERDE,VERDE_T)
p["A7"]="Por dia da semana (últimas 4 semanas registradas)"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Dia","Rotinas","Minutos","Feitas","Planejadas","Aderência"])
RA=f"Rotina!$A${R0}:$A${RI}"; RC=f"Rotina!$C${R0}:$C${RI}"
for i,dia in enumerate(["Segunda","Terça","Quarta","Quinta","Sexta"]):
    r=9+i
    p.cell(row=r,column=1,value=dia); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=COUNTIFS({RA},A{r},Rotina!$B${R0}:$B${RI},"<>")'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=SUMIFS({RC},{RA},A{r},Rotina!$B${R0}:$B${RI},"<>")'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({ULT}=0,"",SUMIFS($E$29:$E${28+NI},$A$29:$A${28+NI},A{r}))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({ULT}=0,"",B{r}*{NS})'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF(OR(E{r}="",E{r}=0),"",D{r}/E{r})'); calc(p.cell(row=r,column=6),PCT)
p.conditional_formatting.add("A9:F13", FormulaRule(formula=['$B9=0'], font=F(color="B0A6C4",size=10)))
p.conditional_formatting.add("F9:F13", FormulaRule(formula=['AND(ISNUMBER(F9),F9<0.7)'], font=F(color="C8402E",size=10,bold=True)))
p["A15"]="Últimas 8 semanas registradas"; p["A15"].font=F(bold=True,size=13,color=UVA)
hdr(p,16,["Semana","Segunda-feira","Feitas","Planejadas","Aderência","Minutos","Barra"])
for j in range(8):
    r=17+j; k=f'({ULT}-{7-j})'
    p.cell(row=r,column=1,value=f'=IF({k}<1,"","S"&{k})'); calc(p.cell(row=r,column=1))
    p.cell(row=r,column=2,value=f'=IF(A{r}="","",INDEX({DAT},{k}))'); calc(p.cell(row=r,column=2),DATA)
    p.cell(row=r,column=3,value=f'=IF(A{r}="","",INDEX({FEI},{k}))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF(A{r}="","",INDEX({PLA},{k}))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF(OR(A{r}="",D{r}=0),"",C{r}/D{r})'); calc(p.cell(row=r,column=5),PCT)
    p.cell(row=r,column=6,value=f'=IF(A{r}="","",INDEX({MIN_},{k}))'); calc(p.cell(row=r,column=6))
    p.cell(row=r,column=7,value=f'=IF(E{r}="","",REPT("█",ROUND(E{r}*10,0)))'); calc(p.cell(row=r,column=7),center=False); p.cell(row=r,column=7).font=F(size=10,color=LILAS); p.merge_cells(start_row=r,start_column=7,end_row=r,end_column=8)
p.conditional_formatting.add("E17:E24", FormulaRule(formula=['AND(ISNUMBER(E17),E17<0.7)'], font=F(color="C8402E",size=10,bold=True)))
p["A26"]="Por rotina (últimas 4 semanas registradas)"; p["A26"].font=F(bold=True,size=13,color=UVA)
p["A27"]="A rotina mais pulada é a que merece ser encurtada, delegada ou trocada de dia."; nota(p["A27"])
hdr(p,28,["Dia","Rotina","Minutos","Responsável","Feitas","De","Aderência","Atenção"])
for i in range(NI):
    r=29+i; s=R0+i
    p.cell(row=r,column=1,value=f'=IF(Rotina!$B{s}="","",Rotina!$A{s})'); calc(p.cell(row=r,column=1))
    p.cell(row=r,column=2,value=f'=IF(Rotina!$B{s}="","",Rotina!$B{s})'); calc(p.cell(row=r,column=2),center=False)
    p.cell(row=r,column=3,value=f'=IF(Rotina!$B{s}="","",Rotina!$C{s})'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF(Rotina!$B{s}="","",Rotina!$D{s})'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF(OR(Rotina!$B{s}="",{ULT}=0),"",SUMPRODUCT((Rotina!${L(C0)}${s}:${LW}${s}="Sim")*({IDX}>={ULT}-3)*({IDX}<={ULT})))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF(E{r}="","",{NS})'); calc(p.cell(row=r,column=6))
    p.cell(row=r,column=7,value=f'=IF(OR(E{r}="",F{r}=0),"",E{r}/F{r})'); calc(p.cell(row=r,column=7),PCT)
    p.cell(row=r,column=8,value=f'=IF(G{r}="","",IF(G{r}<0.5,"Pulada na maioria das semanas",IF(G{r}<0.75,"Pulada às vezes","")))'); calc(p.cell(row=r,column=8),center=False)
p.conditional_formatting.add(f"A29:H{28+NI}", FormulaRule(formula=['AND(ISNUMBER($G29),$G29<0.5)'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
p.conditional_formatting.add(f"A29:H{28+NI}", FormulaRule(formula=['AND(ISNUMBER($G29),$G29>=0.5,$G29<0.75)'], fill=fill("FFF4CC")))
widths(p,(12,56,10,22,10,10,11,26,3,26,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
como_usar(wb,"Rotina da semana da clínica",[
 ("O que esta planilha faz","Fixa a rotina de gestão em dois momentos curtos: segunda (agenda, faltas e retornos) e sexta (caixa, guias, orçamentos e painel). Você marca, semana a semana, o que foi feito; o Painel mostra a aderência das últimas 4 semanas, por dia e por rotina."),
 ("Passo 1","Em Config, confira a data de referência (fica em =HOJE()), a segunda-feira da semana 1 (sugestão: a primeira do ano) e as pessoas da clínica."),
 ("Passo 2","Em Rotina, ajuste as linhas: dia, rotina, minutos e responsável. O exemplo soma 30 minutos por semana (12 na segunda, 18 na sexta), a maior parte com a recepção; mantenha curto, o que é longo não vira hábito."),
 ("Passo 3","Toda segunda e toda sexta, depois de fazer a rotina, marque Sim (ou Não, se pulou) na coluna da semana. A coluna da semana atual fica destacada em amarelo."),
 ("Passo 4","Em Painel, veja a aderência das últimas 4 semanas registradas, a série das últimas 8 e qual rotina está sendo pulada. Menos de 70% em vermelho."),
 ("Exemplo","A clínica fictícia registrou de 20/07 a 07/09/2026 (S29 a S36). O Painel sempre olha as últimas semanas registradas, então o exemplo continua fazendo sentido em qualquer data. Em janeiro de 2027, troque a segunda-feira da semana 1 em Config (veja a nota lá)."),
 ("Com a IA","Copie a tabela \"Por rotina\" e use o prompt \"Agenda 05 · Rotina da recepção em 30 minutos por semana\" da biblioteca do kit."),
])
proteger(wb); salvar(wb,"03-rotina-da-semana.xlsx","Rotina da semana da clínica · Kit de Gestão para Médicos")
