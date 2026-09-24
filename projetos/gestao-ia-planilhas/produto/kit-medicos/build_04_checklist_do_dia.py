#!/usr/bin/env python3
"""Planilha 4 do Kit de Gestão para Médicos: Checklist de abertura e fechamento do dia. Gera 04-checklist-do-dia.xlsx
Uma linha por dia de atendimento; itens de abertura (agenda confirmada, salas prontas, guias separadas) e de fechamento
(caixa fechado e conferido, lançado na 09, faltas marcadas, retornos agendados). Exemplo: dias úteis de 01/06 a 11/09/2026."""
from ssg import *
import dados, random
from datetime import timedelta
N=300; R0=5; RN=R0+N-1; NIT=8; NRESP=10; TOP=12
CA=4; CE=CA+NIT           # itens: abertura D..K (4..11), fechamento L..S (12..19)
CPA,CPE,CNA,CNE,CTOT,CFAL,CKEY,CAUX=20,21,22,23,24,25,26,27
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Os itens cadastrados aqui viram as colunas da aba Checklist.",merge_to="F")
cfg["A4"]="Clínica"; cfg["B4"]=f"{dados.CLINICA} (exemplo fictício)"
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]=dados.HOJE
cfg["A6"]="Painel: olhar os últimos (dias registrados)"; cfg["B6"]=20
for c in ("A4","A5","A6"): rotulo(cfg[c])
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],"0",center=True)
cfg["C5"]="O exemplo está congelado em 14/09/2026, para os arquivos do kit mostrarem a mesma foto. Ao usar com os seus dados, troque por =HOJE()."; nota(cfg["C5"])
cfg["A9"]=f"Itens de abertura (até {NIT})"; cfg["D9"]=f"Itens de fechamento (até {NIT})"; cfg["F9"]=f"Responsáveis (até {NRESP})"
for c in ("A9","D9","F9"): rotulo(cfg[c])
for i in range(NIT):
    inp(cfg.cell(row=10+i,column=2)); inp(cfg.cell(row=10+i,column=4))
for i in range(NRESP): inp(cfg.cell(row=10+i,column=6))
ABERT=["Agenda do dia confirmada (mensagens de véspera respondidas)","Faltas e cancelamentos de ontem registrados na agenda","Salas e equipamentos prontos (ECG, MAPA, Holter)",
       "Guias e autorizações de convênio do dia separadas","Troco e maquininha conferidos","Orçamentos sem resposta revisados (lista da 15)"]
ENCER=["Caixa do dia fechado e conferido (Pix, cartão, dinheiro)","Fechamento do dia lançado no Caixa (09)","Situação de cada horário marcada (realizado, falta, cancelado)",
       "Guias do dia conferidas e guardadas para o lote (13)","Retornos e exames do dia agendados","Agenda de amanhã revisada e confirmações enviadas"]
for i,v in enumerate(ABERT): cfg.cell(row=10+i,column=2,value=v)
for i,v in enumerate(ENCER): cfg.cell(row=10+i,column=4,value=v)
for i,n in enumerate((dados.BRU,dados.CAR,dados.PAU)): cfg.cell(row=10+i,column=6,value=n)
cfg["A19"]="Itens cadastrados"; rotulo(cfg["A19"]); cfg["B19"]=f"=COUNTA($B$10:$B${9+NIT})"; cfg["D19"]=f"=COUNTA($D$10:$D${9+NIT})"; calc(cfg["B19"]); calc(cfg["D19"])
cfg["A21"]="Preencha de cima para baixo, sem pular linha: as listas param na última linha preenchida e os itens vazios não contam no percentual."; nota(cfg["A21"])
cfg["A22"]="Os itens são administrativos (o que precisa estar em ordem para o dia começar e terminar sem pendência). Nada clínico aqui. Ajuste ao jeito da clínica."; nota(cfg["A22"])
widths(cfg,(30,52,4,52,4,22)); cfg.sheet_view.showGridLines=False
# ---------- Checklist ----------
ck=wb.create_sheet("Checklist")
titulo(ck,"Checklist por dia","Uma linha por dia de atendimento. Em cada item marque Sim, Não ou N/A (não se aplica). Vazio conta como pendente. Quem fecha o dia é a recepção; quem confere é o sócio da semana.",merge_to="P")
HOJE="Config!$B$5"; NAB="Config!$B$19"; NEN="Config!$D$19"
g1=ck.cell(row=3,column=CA,value="Abertura"); g2=ck.cell(row=3,column=CE,value="Fechamento")
for g in (g1,g2): g.font=F(bold=True,color=UVA,size=10); g.alignment=Alignment(horizontal="center")
ck.merge_cells(start_row=3,start_column=CA,end_row=3,end_column=CA+NIT-1); ck.merge_cells(start_row=3,start_column=CE,end_row=3,end_column=CE+NIT-1)
heads=["Data","Dia da semana","Responsável"]+[f'=IF(Config!$B${10+i}="","",Config!$B${10+i})' for i in range(NIT)]+[f'=IF(Config!$D${10+i}="","",Config!$D${10+i})' for i in range(NIT)]+["% abertura","% fechamento","Pendências de abertura","Pendências de fechamento","Pendências","O que faltou","Chave","Auxiliar"]
hdr(ck,4,heads,height=72)
for i in range(NIT):
    ck.cell(row=4,column=CA+i).fill=fill(LILAS); ck.cell(row=4,column=CE+i).fill=fill("5B3F87")
AB=lambda r: f"{L(CA)}{r}:{L(CA+NIT-1)}{r}"; EN=lambda r: f"{L(CE)}{r}:{L(CE+NIT-1)}{r}"
for r in range(R0,RN+1):
    inp(ck.cell(row=r,column=1),DATA,center=True)
    ck.cell(row=r,column=2,value=f'=IF(A{r}="","",CHOOSE(WEEKDAY(A{r},2),"Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"))'); calc(ck.cell(row=r,column=2))
    inp(ck.cell(row=r,column=3),center=True)
    for c in range(CA,CE+NIT): inp(ck.cell(row=r,column=c),center=True)
    ck.cell(row=r,column=CPA,value=f'=IF(A{r}="","",IFERROR(COUNTIF({AB(r)},"Sim")/({NAB}-COUNTIF({AB(r)},"N/A")),""))'); calc(ck.cell(row=r,column=CPA),PCT)
    ck.cell(row=r,column=CPE,value=f'=IF(A{r}="","",IFERROR(COUNTIF({EN(r)},"Sim")/({NEN}-COUNTIF({EN(r)},"N/A")),""))'); calc(ck.cell(row=r,column=CPE),PCT)
    ck.cell(row=r,column=CNA,value=f'=IF(A{r}="","",MAX(0,{NAB}-COUNTIF({AB(r)},"Sim")-COUNTIF({AB(r)},"N/A")))'); calc(ck.cell(row=r,column=CNA))
    ck.cell(row=r,column=CNE,value=f'=IF(A{r}="","",MAX(0,{NEN}-COUNTIF({EN(r)},"Sim")-COUNTIF({EN(r)},"N/A")))'); calc(ck.cell(row=r,column=CNE))
    ck.cell(row=r,column=CTOT,value=f'=IF(A{r}="","",{L(CNA)}{r}+{L(CNE)}{r})'); calc(ck.cell(row=r,column=CTOT))
    partes=[f'IF(AND(Config!$B${10+i}<>"",{L(CA+i)}{r}<>"Sim",{L(CA+i)}{r}<>"N/A"),Config!$B${10+i}&"; ","")' for i in range(NIT)]
    partes+=[f'IF(AND(Config!$D${10+i}<>"",{L(CE+i)}{r}<>"Sim",{L(CE+i)}{r}<>"N/A"),Config!$D${10+i}&"; ","")' for i in range(NIT)]
    ck.cell(row=r,column=CAUX,value=f'=IF(A{r}="","",{"&".join(partes)})'); ck.cell(row=r,column=CAUX).font=F(color=CINZA,size=9)
    ck.cell(row=r,column=CFAL,value=f'=IF(OR(A{r}="",{L(CAUX)}{r}=""),"",LEFT({L(CAUX)}{r},LEN({L(CAUX)}{r})-2))'); calc(ck.cell(row=r,column=CFAL),center=False)
    ck.cell(row=r,column=CKEY,value=f'=IF(OR(A{r}="",{L(CTOT)}{r}=0),0,{L(CTOT)}{r}*100000+A{r}/100000)'); ck.cell(row=r,column=CKEY).font=F(color=CINZA,size=9)
    ck.cell(row=r,column=CAUX+1,value=f'=IF(A{r}="",0,COUNTIF($A${R0}:$A${RN},">"&A{r})+1)'); ck.cell(row=r,column=CAUX+1).font=F(color=CINZA,size=9)   # ordem do dia (1 = mais recente)
dvr=lista(f"=OFFSET(Config!$F$10,0,0,MAX(1,COUNTA(Config!$F$10:$F${9+NRESP})),1)",strict=True); dvr.add(f"C{R0}:C{RN}")
dvi=lista('"Sim,Não,N/A"'); dvi.add(f"{L(CA)}{R0}:{L(CE+NIT-1)}{RN}")
dvd=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True); dvd.add(f"A{R0}:A{RN}")
for dv in (dvr,dvi,dvd): ck.add_data_validation(dv)
IT=f"{L(CA)}{R0}:{L(CE+NIT-1)}{RN}"
ck.conditional_formatting.add(IT, FormulaRule(formula=[f'{L(CA)}{R0}="Sim"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
ck.conditional_formatting.add(IT, FormulaRule(formula=[f'{L(CA)}{R0}="Não"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
ck.conditional_formatting.add(IT, FormulaRule(formula=[f'{L(CA)}{R0}="N/A"'], font=F(color="8A86A0",size=10)))
ck.conditional_formatting.add(f"A{R0}:C{RN}", FormulaRule(formula=[f'AND(ISNUMBER(${L(CTOT)}{R0}),${L(CTOT)}{R0}>0)'], font=F(color="C8402E",size=10,bold=True)))
ck.conditional_formatting.add(f"{L(CPA)}{R0}:{L(CPE)}{RN}", FormulaRule(formula=[f'AND(ISNUMBER({L(CPA)}{R0}),{L(CPA)}{R0}<1)'], font=F(color="C8402E",size=10,bold=True)))
widths(ck,[12,11,18]+[12]*(2*NIT)+[10,12,11,12,11,60,8,6,6]); ck.column_dimensions[L(CKEY)].hidden=True; ck.column_dimensions[L(CAUX)].hidden=True; ck.column_dimensions[L(CAUX+1)].hidden=True
ck.freeze_panes=f"{L(CA)}{R0}"; ck.sheet_view.showGridLines=False; ck.auto_filter.ref=f"A4:{L(CFAL)}{RN}"
# exemplo: dias úteis de 01/06 a 11/09/2026, quase tudo Sim; algumas pendências
rng_=random.Random(4); d=dados.INICIO_AGENDA; i=0
PEND={}
while d<=dados.SEXTA:
    if d.weekday()<5 and d not in dados.FERIADOS:
        r=R0+i; ck.cell(row=r,column=1,value=d); ck.cell(row=r,column=3,value=dados.BRU)
        for j in range(len(ABERT)):
            v="Sim"
            if j==5 and d.weekday()!=4: v="N/A"          # orçamentos: só na sexta
            elif rng_.random()<0.04: v="Não"
            ck.cell(row=r,column=CA+j,value=v)
        for j in range(len(ENCER)):
            v="Sim"
            if rng_.random()<(0.10 if j==1 else 0.04): v="Não"
            if d>=dados.SEXTA-timedelta(days=1) and j in (1,3) and rng_.random()<0.5: v=""     # ainda não fechado
            if v: ck.cell(row=r,column=CE+j,value=v)
        i+=1
    d+=timedelta(days=1)
NDIAS=i
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Abertura e fechamento do dia · "&TEXT(DAY(Config!$B$5),"00")&"/"&TEXT(MONTH(Config!$B$5),"00")&"/"&YEAR(Config!$B$5)',"Nada para digitar aqui: tudo vem de Config e Checklist. Pendência = item de abertura ou de fechamento que não está marcado como Sim ou N/A.",merge_to="J")
KA=f"Checklist!$A${R0}:$A${RN}"; KB=f"Checklist!$B${R0}:$B${RN}"; KC=f"Checklist!$C${R0}:$C${RN}"
KPA=f"Checklist!${L(CPA)}${R0}:${L(CPA)}${RN}"; KPE=f"Checklist!${L(CPE)}${R0}:${L(CPE)}${RN}"; KNA=f"Checklist!${L(CNA)}${R0}:${L(CNA)}${RN}"; KNE=f"Checklist!${L(CNE)}${R0}:${L(CNE)}${RN}"
KT=f"Checklist!${L(CTOT)}${R0}:${L(CTOT)}${RN}"; KF=f"Checklist!${L(CFAL)}${R0}:${L(CFAL)}${RN}"; KK=f"Checklist!${L(CKEY)}${R0}:${L(CKEY)}${RN}"; KO=f"Checklist!${L(CAUX+1)}${R0}:${L(CAUX+1)}${RN}"
NJ="Config!$B$6"
kpi(p,4,1,"Dias registrados",f'=COUNTIFS({KA},"<>")',LAVANDA,UVA)
kpi(p,4,3,'="Abertura completa (últimos "&Config!$B$6&" dias)"',f'=IFERROR(COUNTIFS({KO},"<="&{NJ},{KO},">0",{KNA},0)/MIN({NJ},COUNTIFS({KA},"<>")),"")',VERDE,VERDE_T,fmt=PCT)
kpi(p,4,5,'="Fechamento completo (últimos "&Config!$B$6&" dias)"',f'=IFERROR(COUNTIFS({KO},"<="&{NJ},{KO},">0",{KNE},0)/MIN({NJ},COUNTIFS({KA},"<>")),"")',VERDE,VERDE_T,fmt=PCT)
kpi(p,4,7,"Dias com pendência",f'=COUNTIFS({KT},">0")',VERM,VERM_T)
kpi(p,4,9,"Itens pendentes no total",f'=SUM({KT})',SOL,UVA)
p["A7"]="Dias com pendência (mais itens pendentes primeiro; empate: o mais recente)"; p["A7"].font=F(bold=True,size=13,color=UVA)
p["A8"]=f"Mostra os {TOP} primeiros; os demais ficam na aba Checklist, que pode ser filtrada pela coluna Pendências."; nota(p["A8"]); p.merge_cells("A8:J8")
hdr(p,9,["#","Data","Dia","Responsável","% abertura","% fechamento","Pendências","O que faltou"])
p.merge_cells(start_row=9,start_column=8,end_row=9,end_column=10)
for k in range(1,TOP+1):
    r=9+k; m=f'MATCH(LARGE({KK},{k}),{KK},0)'; g=f'LARGE({KK},{k})>0'
    p.cell(row=r,column=1,value=k)
    for col,rng in zip((2,3,4,5,6,7,8),(KA,KB,KC,KPA,KPE,KT,KF)):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},IF(INDEX({rng},{m})="","",INDEX({rng},{m})),""),"")')
    for col in range(1,11): calc(p.cell(row=r,column=col),center=(col not in (8,)))
    p.cell(row=r,column=2).number_format=DATA; p.cell(row=r,column=5).number_format=PCT; p.cell(row=r,column=6).number_format=PCT
    p.cell(row=r,column=8).alignment=Alignment(wrap_text=True,vertical="top"); p.merge_cells(start_row=r,start_column=8,end_row=r,end_column=10); p.row_dimensions[r].height=30
p.conditional_formatting.add(f"G10:G{9+TOP}", FormulaRule(formula=['AND(ISNUMBER(G10),G10>0)'], font=F(color="C8402E",size=10,bold=True)))
r0=9+TOP+2
p.cell(row=r0,column=1,value="Item mais esquecido").font=F(bold=True,size=13,color=UVA)
p.cell(row=r0+1,column=1,value="Conta todos os dias registrados. Item pendente muitas vezes é sinal de que a rotina do dia precisa mudar (horário, responsável ou o próprio item).").font=F(size=9,color=LILAS); p.merge_cells(start_row=r0+1,start_column=1,end_row=r0+1,end_column=10)
hdr(p,r0+2,["Item de abertura","","Pendente em","Feito em","N/A","Item de fechamento","","Pendente em","Feito em","N/A"])
p.merge_cells(start_row=r0+2,start_column=1,end_row=r0+2,end_column=2); p.merge_cells(start_row=r0+2,start_column=6,end_row=r0+2,end_column=7)
for i in range(NIT):
    r=r0+3+i; src=f"Config!$B${10+i}"; col=f"Checklist!${L(CA+i)}${R0}:${L(CA+i)}${RN}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({KA},"<>",{col},"<>Sim",{col},"<>N/A"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({KA},"<>",{col},"Sim"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({KA},"<>",{col},"N/A"))'); calc(p.cell(row=r,column=5))
    src2=f"Config!$D${10+i}"; col2=f"Checklist!${L(CE+i)}${R0}:${L(CE+i)}${RN}"
    p.cell(row=r,column=6,value=f'=IF({src2}="","",{src2})'); calc(p.cell(row=r,column=6),center=False); p.merge_cells(start_row=r,start_column=6,end_row=r,end_column=7); calc(p.cell(row=r,column=7))
    p.cell(row=r,column=8,value=f'=IF({src2}="","",COUNTIFS({KA},"<>",{col2},"<>Sim",{col2},"<>N/A"))'); calc(p.cell(row=r,column=8))
    p.cell(row=r,column=9,value=f'=IF({src2}="","",COUNTIFS({KA},"<>",{col2},"Sim"))'); calc(p.cell(row=r,column=9))
    p.cell(row=r,column=10,value=f'=IF({src2}="","",COUNTIFS({KA},"<>",{col2},"N/A"))'); calc(p.cell(row=r,column=10))
    p.cell(row=r,column=1).alignment=Alignment(wrap_text=True,vertical="center"); p.cell(row=r,column=6).alignment=Alignment(wrap_text=True,vertical="center"); p.row_dimensions[r].height=30
p.conditional_formatting.add(f"C{r0+3}:C{r0+2+NIT}", FormulaRule(formula=[f'AND(ISNUMBER(C{r0+3}),C{r0+3}>0)'], font=F(color="C8402E",size=10,bold=True)))
p.conditional_formatting.add(f"H{r0+3}:H{r0+2+NIT}", FormulaRule(formula=[f'AND(ISNUMBER(H{r0+3}),H{r0+3}>0)'], font=F(color="C8402E",size=10,bold=True)))
r1=r0+NIT+5
p.cell(row=r1,column=1,value="Por dia da semana (todos os dias registrados)").font=F(bold=True,size=13,color=UVA)
hdr(p,r1+1,["Dia","","Dias","Com pendência","Itens pendentes","Abertura completa","Fechamento completo"])
p.merge_cells(start_row=r1+1,start_column=1,end_row=r1+1,end_column=2)
for i,dia in enumerate(["Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]):
    r=r1+2+i
    p.cell(row=r,column=1,value=dia); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=COUNTIFS({KB},A{r})'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=COUNTIFS({KB},A{r},{KT},">0")'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=SUMIFS({KT},{KB},A{r})'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF(C{r}=0,"",COUNTIFS({KB},A{r},{KNA},0)/C{r})'); calc(p.cell(row=r,column=6),PCT)
    p.cell(row=r,column=7,value=f'=IF(C{r}=0,"",COUNTIFS({KB},A{r},{KNE},0)/C{r})'); calc(p.cell(row=r,column=7),PCT)
p.conditional_formatting.add(f"A{r1+2}:G{r1+7}", FormulaRule(formula=[f'$C{r1+2}=0'], font=F(color="B0A6C4",size=10)))
p.cell(row=r1+9,column=1,value="Fechamento do dia sem o caixa conferido é a origem da maior parte das diferenças no extrato. Se um item pende sempre no mesmo dia da semana, mude a rotina desse dia, não a pessoa.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=r1+9,start_column=1,end_row=r1+9,end_column=10)
widths(p,(6,12,11,18,11,13,11,30,12,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
como_usar(wb,"Checklist de abertura e fechamento do dia",[
 ("O que esta planilha faz","Para cada dia de atendimento, marca os itens administrativos que precisam estar em ordem na abertura (agenda confirmada, salas prontas, guias separadas, troco conferido) e no fechamento (caixa fechado e conferido, lançado no Caixa, situação de cada horário marcada, guias guardadas, retornos agendados). Calcula o % concluído por dia e mostra no Painel os dias com pendência e o item mais esquecido."),
 ("Passo 1","Em Config, ajuste os itens de abertura e de fechamento ao jeito da clínica e cadastre os responsáveis. Preencha de cima para baixo, sem pular linha."),
 ("Passo 2","Em Checklist, apague os exemplos e crie uma linha por dia (data e responsável). Em cada item, marque Sim, Não ou N/A. Vazio conta como pendente, de propósito: o dia só fecha quando tudo está marcado."),
 ("Passo 3","Em Painel: aderência dos últimos 20 dias (abertura e fechamento completos), os dias com pendência e \"Item mais esquecido\": se o mesmo item pende em vários dias, o problema é a rotina, não o dia."),
 ("Rotina","É o roteiro diário da recepção, fora dos 30 minutos semanais dos sócios (planilha 03): abertura, 3 minutos antes do primeiro paciente; fechamento, 10 minutos depois do último — são 13 minutos por dia. O fechamento inclui lançar o caixa do dia na planilha 09; na sexta a sócia só confere os cinco fechamentos da semana (rotina de sexta da 03)."),
 ("Exemplo","Dias úteis de 01/06 a 11/09/2026, preenchidos pela recepção. Sexta-feira 11/09 tem itens de fechamento em branco: é o que o Painel aponta na segunda."),
 ("Com a IA","Copie a coluna \"O que faltou\" de um dia e use o prompt \"Agenda 06 · Pendências do dia viram tarefas da recepção\" da biblioteca do kit."),
])
proteger(wb); salvar(wb,"04-checklist-do-dia.xlsx","Checklist de abertura e fechamento do dia · Kit de Gestão para Médicos")
