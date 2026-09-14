#!/usr/bin/env python3
"""Planilha 4 do Kit de Gestão para Advogados: Checklist de abertura e encerramento de caso. Gera 04-checklist-abertura-e-encerramento.xlsx"""
from ssg import *
import dados
N=300; R0=5; RN=R0+N-1; NIT=10; NRESP=10; TOP=15
CA=5; CE=CA+NIT           # colunas dos itens: abertura E..N (5..14), encerramento O..X (15..24)
CPA,CPE,CNA,CNE,CTOT,CFAL,CKEY,CAUX=25,26,27,28,29,30,31,32   # Y % abertura, Z % encerramento, AA, AB pendências, AC total, AD o que falta, AE chave, AF auxiliar do texto
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Os itens cadastrados aqui viram as colunas da aba Checklist.",merge_to="F")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]="=TODAY()"
for c in ("A4","A5"): rotulo(cfg[c])
inp(cfg["B4"]); inp(cfg["B5"],DATA)
cfg["C5"]="Deixe =HOJE() para acompanhar o dia."; nota(cfg["C5"])
cfg["A9"]=f"Itens de abertura (até {NIT})"; cfg["D9"]=f"Itens de encerramento (até {NIT})"; cfg["F9"]=f"Responsáveis (até {NRESP})"
for c in ("A9","D9","F9"): rotulo(cfg[c])
for i in range(NIT):
    inp(cfg.cell(row=10+i,column=2)); inp(cfg.cell(row=10+i,column=4))
for i in range(NRESP): inp(cfg.cell(row=10+i,column=6))
ABERT=["Contrato de honorários assinado","Procuração recebida","Documentos do cliente recebidos","Honorário e forma de pagamento definidos",
       "Caso cadastrado no caixa e na carteira","Responsável definido","Primeiro prazo na agenda","Canal de contato combinado com o cliente","Pasta do caso criada (física ou digital)"]
ENCER=["Última parcela cobrada e recebida","Cliente avisado do encerramento","Documentos devolvidos ao cliente","Pasta arquivada",
       "Caso marcado como encerrado na carteira","Avaliação do cliente pedida","Prazos do caso baixados na agenda","Horas do caso fechadas"]
for i,v in enumerate(ABERT): cfg.cell(row=10+i,column=2,value=v)
for i,v in enumerate(ENCER): cfg.cell(row=10+i,column=4,value=v)
for i,(n,_,_,_) in enumerate(dados.PESSOAS): cfg.cell(row=10+i,column=6,value=n)
cfg["A21"]="Itens cadastrados"; rotulo(cfg["A21"]); cfg["B21"]=f"=COUNTA($B$10:$B${9+NIT})"; cfg["D21"]=f"=COUNTA($D$10:$D${9+NIT})"; calc(cfg["B21"]); calc(cfg["D21"])
cfg["A23"]="Preencha de cima para baixo, sem pular linha: as listas param na última linha preenchida e os itens vazios não contam no percentual."; nota(cfg["A23"])
cfg["A24"]="Os itens são administrativos (o que precisa estar em ordem para o caso começar e terminar sem pendência). Ajuste ao jeito do escritório."; nota(cfg["A24"])
widths(cfg,(30,40,4,40,4,20)); cfg.sheet_view.showGridLines=False
# ---------- Checklist ----------
ck=wb.create_sheet("Checklist")
titulo(ck,"Checklist por caso","Uma linha por caso (copie número, cliente e responsável da planilha 13 · Carteira, aba Casos: a 13 é a fonte). Em cada item marque Sim, Não ou N/A (não se aplica). Vazio conta como pendente. Os itens de encerramento só contam quando a situação é Encerrado.",merge_to="P")
HOJE="Config!$B$5"; NAB="Config!$B$21"; NEN="Config!$D$21"
g1=ck.cell(row=3,column=CA,value="Abertura"); g2=ck.cell(row=3,column=CE,value="Encerramento")
for g in (g1,g2): g.font=F(bold=True,color=UVA,size=10); g.alignment=Alignment(horizontal="center")
ck.merge_cells(start_row=3,start_column=CA,end_row=3,end_column=CA+NIT-1); ck.merge_cells(start_row=3,start_column=CE,end_row=3,end_column=CE+NIT-1)
heads=["Número","Cliente","Responsável","Situação"]+[f'=IF(Config!$B${10+i}="","",Config!$B${10+i})' for i in range(NIT)]+[f'=IF(Config!$D${10+i}="","",Config!$D${10+i})' for i in range(NIT)]+["% abertura","% encerramento","Pendências de abertura","Pendências de encerramento","Pendências","O que falta","Chave","Auxiliar"]
hdr(ck,4,heads,height=64)
for i in range(NIT):
    ck.cell(row=4,column=CA+i).fill=fill(LILAS); ck.cell(row=4,column=CE+i).fill=fill("5B3F87")
AB=lambda r: f"{L(CA)}{r}:{L(CA+NIT-1)}{r}"; EN=lambda r: f"{L(CE)}{r}:{L(CE+NIT-1)}{r}"
for r in range(R0,RN+1):
    for c in range(1,CE+NIT): inp(ck.cell(row=r,column=c))
    for c in range(3,CE+NIT): ck.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    ck.cell(row=r,column=CPA,value=f'=IF(A{r}="","",IFERROR(COUNTIF({AB(r)},"Sim")/({NAB}-COUNTIF({AB(r)},"N/A")),""))'); calc(ck.cell(row=r,column=CPA),PCT)
    ck.cell(row=r,column=CPE,value=f'=IF(OR(A{r}="",D{r}<>"Encerrado"),"",IFERROR(COUNTIF({EN(r)},"Sim")/({NEN}-COUNTIF({EN(r)},"N/A")),""))'); calc(ck.cell(row=r,column=CPE),PCT)
    ck.cell(row=r,column=CNA,value=f'=IF(A{r}="","",MAX(0,{NAB}-COUNTIF({AB(r)},"Sim")-COUNTIF({AB(r)},"N/A")))'); calc(ck.cell(row=r,column=CNA))
    ck.cell(row=r,column=CNE,value=f'=IF(OR(A{r}="",D{r}<>"Encerrado"),"",MAX(0,{NEN}-COUNTIF({EN(r)},"Sim")-COUNTIF({EN(r)},"N/A")))'); calc(ck.cell(row=r,column=CNE))
    ck.cell(row=r,column=CTOT,value=f'=IF(A{r}="","",{L(CNA)}{r}+IF({L(CNE)}{r}="",0,{L(CNE)}{r}))'); calc(ck.cell(row=r,column=CTOT))
    # "O que falta" sem UNIRTEXTO (Excel 2016 e Google Sheets): a coluna auxiliar AF concatena "item; " por IF e AD tira o "; " final
    partes=[f'IF(AND(Config!$B${10+i}<>"",{L(CA+i)}{r}<>"Sim",{L(CA+i)}{r}<>"N/A"),Config!$B${10+i}&"; ","")' for i in range(NIT)]
    partes+=[f'IF(AND($D{r}="Encerrado",Config!$D${10+i}<>"",{L(CE+i)}{r}<>"Sim",{L(CE+i)}{r}<>"N/A"),Config!$D${10+i}&"; ","")' for i in range(NIT)]
    ck.cell(row=r,column=CAUX,value=f'=IF(A{r}="","",{"&".join(partes)})'); ck.cell(row=r,column=CAUX).font=F(color=CINZA,size=9)
    ck.cell(row=r,column=CFAL,value=f'=IF(OR(A{r}="",{L(CAUX)}{r}=""),"",LEFT({L(CAUX)}{r},LEN({L(CAUX)}{r})-2))'); calc(ck.cell(row=r,column=CFAL),center=False)
    ck.cell(row=r,column=CKEY,value=f'=IF(OR(A{r}="",{L(CTOT)}{r}=0),0,{L(CTOT)}{r}*100-ROW()/100000)'); ck.cell(row=r,column=CKEY).font=F(color=CINZA,size=9)
dvr=lista(f"=OFFSET(Config!$F$10,0,0,MAX(1,COUNTA(Config!$F$10:$F${9+NRESP})),1)",strict=False); dvr.add(f"C{R0}:C{RN}")
dvs=lista('"Em andamento,Encerrado"'); dvs.add(f"D{R0}:D{RN}")
dvi=lista('"Sim,Não,N/A"'); dvi.add(f"{L(CA)}{R0}:{L(CE+NIT-1)}{RN}")
for dv in (dvr,dvs,dvi): ck.add_data_validation(dv)
IT=f"{L(CA)}{R0}:{L(CE+NIT-1)}{RN}"
ck.conditional_formatting.add(IT, FormulaRule(formula=[f'{L(CA)}{R0}="Sim"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
ck.conditional_formatting.add(IT, FormulaRule(formula=[f'{L(CA)}{R0}="Não"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
ck.conditional_formatting.add(IT, FormulaRule(formula=[f'{L(CA)}{R0}="N/A"'], font=F(color="8A86A0",size=10)))
ck.conditional_formatting.add(f"{L(CE)}{R0}:{L(CE+NIT-1)}{RN}", FormulaRule(formula=[f'$D{R0}<>"Encerrado"'], fill=fill("F2F0F5"), font=F(color="B0A6C4",size=10)))
ck.conditional_formatting.add(f"A{R0}:D{RN}", FormulaRule(formula=[f'AND(ISNUMBER(${L(CTOT)}{R0}),${L(CTOT)}{R0}>0)'], font=F(color="C8402E",size=10,bold=True)))
ck.conditional_formatting.add(f"{L(CPA)}{R0}:{L(CPE)}{RN}", FormulaRule(formula=[f'AND(ISNUMBER({L(CPA)}{R0}),{L(CPA)}{R0}<1)'], font=F(color="C8402E",size=10,bold=True)))
widths(ck,[28,26,16,14]+[11]*(2*NIT)+[10,12,11,12,11,60,6,6]); ck.column_dimensions[L(CKEY)].hidden=True; ck.column_dimensions[L(CAUX)].hidden=True
ck.freeze_panes=f"{L(CA)}{R0}"; ck.sheet_view.showGridLines=False; ck.auto_filter.ref=f"A4:{L(CFAL)}{RN}"
# exemplos: os 38 casos de dados.py
for i,c in enumerate(dados.CASOS):
    PEND_AB={i:dados.PEND_ABERTURA.get(c["chave"],{})}; PEND_EN={i:dados.PEND_ENCERRAMENTO.get(c["chave"],{})}
    r=R0+i; enc=c["fase"]=="Encerrado"
    ck.cell(row=r,column=1,value=c["numero"]); ck.cell(row=r,column=2,value=c["cliente"]); ck.cell(row=r,column=3,value=c["responsavel"]); ck.cell(row=r,column=4,value="Encerrado" if enc else "Em andamento")
    for j in range(len(ABERT)):
        v="Sim"
        if c["fase"]=="Consultivo" and j in (1,6): v="N/A"
        v=PEND_AB.get(i,{}).get(j,v)
        if v: ck.cell(row=r,column=CA+j,value=v)
    if enc:
        for j in range(len(ENCER)):
            v=PEND_EN.get(i,{}).get(j,"Sim")
            if v: ck.cell(row=r,column=CE+j,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Abertura e encerramento · "&TEXT(Config!$B$5,"dd/mm/yyyy")',"Nada para digitar aqui: tudo vem de Config e Checklist. Pendência = item de abertura (ou de encerramento, em caso encerrado) que não está marcado como Sim ou N/A.",merge_to="J")
KA=f"Checklist!$A${R0}:$A${RN}"; KB=f"Checklist!$B${R0}:$B${RN}"; KC=f"Checklist!$C${R0}:$C${RN}"; KD=f"Checklist!$D${R0}:$D${RN}"
KPA=f"Checklist!${L(CPA)}${R0}:${L(CPA)}${RN}"; KPE=f"Checklist!${L(CPE)}${R0}:${L(CPE)}${RN}"; KNA=f"Checklist!${L(CNA)}${R0}:${L(CNA)}${RN}"; KNE=f"Checklist!${L(CNE)}${R0}:${L(CNE)}${RN}"
KT=f"Checklist!${L(CTOT)}${R0}:${L(CTOT)}${RN}"; KF=f"Checklist!${L(CFAL)}${R0}:${L(CFAL)}${RN}"; KK=f"Checklist!${L(CKEY)}${R0}:${L(CKEY)}${RN}"
kpi(p,4,1,"Casos cadastrados",f'=COUNTIFS({KA},"<>")',LAVANDA,UVA)
kpi(p,4,3,"Abertos com pendência de abertura",f'=COUNTIFS({KD},"Em andamento",{KNA},">0")',VERM,VERM_T)
kpi(p,4,5,"Encerrados com pendência",f'=COUNTIFS({KD},"Encerrado",{KNE},">0")',VERM,VERM_T)
kpi(p,4,7,"Itens pendentes no total",f'=SUM({KT})',SOL,UVA)
kpi(p,4,9,"Casos sem pendência",f'=COUNTIFS({KA},"<>",{KT},0)',VERDE,VERDE_T)
p["A7"]="Casos com pendência (mais itens pendentes primeiro)"; p["A7"].font=F(bold=True,size=13,color=UVA)
p["A8"]=f"Mostra os {TOP} primeiros; os demais ficam na aba Checklist, que pode ser filtrada pela coluna Pendências."; nota(p["A8"]); p.merge_cells("A8:J8")
hdr(p,9,["#","Número","Cliente","Situação","Responsável","% abertura","% encerramento","Pendências","O que falta"])
p.merge_cells(start_row=9,start_column=9,end_row=9,end_column=10)
for k in range(1,TOP+1):
    r=9+k; m=f'MATCH(LARGE({KK},{k}),{KK},0)'; g=f'LARGE({KK},{k})>0'
    p.cell(row=r,column=1,value=k)
    for col,rng in zip((2,3,4,5,6,7,8,9),(KA,KB,KD,KC,KPA,KPE,KT,KF)):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},IF(INDEX({rng},{m})="","",INDEX({rng},{m})),""),"")')
    for col in range(1,11): calc(p.cell(row=r,column=col),center=(col not in (2,3,9)))
    p.cell(row=r,column=6).number_format=PCT; p.cell(row=r,column=7).number_format=PCT
    p.cell(row=r,column=9).alignment=Alignment(wrap_text=True,vertical="top"); p.merge_cells(start_row=r,start_column=9,end_row=r,end_column=10); p.row_dimensions[r].height=28
p.conditional_formatting.add(f"A10:J{9+TOP}", FormulaRule(formula=['$D10="Encerrado"'], fill=fill(LAVANDA)))
p.conditional_formatting.add(f"H10:H{9+TOP}", FormulaRule(formula=['AND(ISNUMBER(H10),H10>0)'], font=F(color="C8402E",size=10,bold=True)))
r0=9+TOP+2
p.cell(row=r0,column=1,value="Item mais esquecido").font=F(bold=True,size=13,color=UVA)
p.cell(row=r0+1,column=1,value="Abertura: conta todos os casos cadastrados. Encerramento: só os casos com situação Encerrado. Item pendente muitas vezes é sinal de que a rotina de abertura precisa mudar.").font=F(size=9,color=LILAS); p.merge_cells(start_row=r0+1,start_column=1,end_row=r0+1,end_column=10)
hdr(p,r0+2,["","Item de abertura","Pendente em","Feito em","N/A","","Item de encerramento","Pendente em","Feito em","N/A"])
p.merge_cells(start_row=r0+2,start_column=1,end_row=r0+2,end_column=2); p.cell(row=r0+2,column=1,value="Item de abertura"); p.cell(row=r0+2,column=2,value=None)
p.cell(row=r0+2,column=6,value=None); p.cell(row=r0+2,column=6).fill=fill(BRANCO); p.cell(row=r0+2,column=6).border=Border()
for i in range(NIT):
    r=r0+3+i; src=f"Config!$B${10+i}"; col=f"Checklist!${L(CA+i)}${R0}:${L(CA+i)}${RN}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({KA},"<>",{col},"<>Sim",{col},"<>N/A"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({KA},"<>",{col},"Sim"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({KA},"<>",{col},"N/A"))'); calc(p.cell(row=r,column=5))
    src2=f"Config!$D${10+i}"; col2=f"Checklist!${L(CE+i)}${R0}:${L(CE+i)}${RN}"
    p.cell(row=r,column=7,value=f'=IF({src2}="","",{src2})'); calc(p.cell(row=r,column=7),center=False)
    p.cell(row=r,column=8,value=f'=IF({src2}="","",COUNTIFS({KD},"Encerrado",{col2},"<>Sim",{col2},"<>N/A"))'); calc(p.cell(row=r,column=8))
    p.cell(row=r,column=9,value=f'=IF({src2}="","",COUNTIFS({KD},"Encerrado",{col2},"Sim"))'); calc(p.cell(row=r,column=9))
    p.cell(row=r,column=10,value=f'=IF({src2}="","",COUNTIFS({KD},"Encerrado",{col2},"N/A"))'); calc(p.cell(row=r,column=10))
p.conditional_formatting.add(f"C{r0+3}:C{r0+2+NIT}", FormulaRule(formula=[f'AND(ISNUMBER(C{r0+3}),C{r0+3}>0)'], font=F(color="C8402E",size=10,bold=True)))
p.conditional_formatting.add(f"H{r0+3}:H{r0+2+NIT}", FormulaRule(formula=[f'AND(ISNUMBER(H{r0+3}),H{r0+3}>0)'], font=F(color="C8402E",size=10,bold=True)))
r1=r0+NIT+5
p.cell(row=r1,column=1,value="Por responsável").font=F(bold=True,size=13,color=UVA)
hdr(p,r1+1,["","Responsável","Casos","Em andamento","Encerrados","Com pendência","Itens pendentes"])
p.merge_cells(start_row=r1+1,start_column=1,end_row=r1+1,end_column=2); p.cell(row=r1+1,column=1,value="Responsável"); p.cell(row=r1+1,column=2,value=None)
for i in range(NRESP):
    r=r1+2+i; src=f"Config!$F${10+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({KC},{src},{KA},"<>"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({KC},{src},{KD},"Em andamento"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({KC},{src},{KD},"Encerrado"))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF({src}="","",COUNTIFS({KC},{src},{KT},">0"))'); calc(p.cell(row=r,column=6))
    p.cell(row=r,column=7,value=f'=IF({src}="","",SUMIFS({KT},{KC},{src}))'); calc(p.cell(row=r,column=7))
p.conditional_formatting.add(f"F{r1+2}:F{r1+1+NRESP}", FormulaRule(formula=[f'AND(ISNUMBER(F{r1+2}),F{r1+2}>0)'], font=F(color="C8402E",size=10,bold=True)))
widths(p,(6,28,26,14,16,11,13,11,34,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Como usar ----------
como_usar(wb,"Checklist de abertura e encerramento de caso",[
 ("O que esta planilha faz","Para cada caso, marca os itens administrativos que precisam estar em ordem na abertura (contrato, procuração, documentos, honorário, cadastro no caixa) e no encerramento (última parcela, arquivo, devolução, avaliação). Calcula o % concluído por caso e mostra no Painel quem está com pendência."),
 ("Passo 1","Em Config, ajuste os itens de abertura e de encerramento ao jeito do escritório e cadastre os responsáveis. Preencha de cima para baixo, sem pular linha."),
 ("Passo 2","Em Checklist, apague os exemplos e cadastre uma linha por caso (número, cliente e responsável copiados da planilha 13 · Carteira, que é a fonte do cadastro). Em cada item, marque Sim, Não ou N/A (não se aplica). Vazio conta como pendente, de propósito: caso novo começa com tudo pendente."),
 ("Passo 3","Ao encerrar um caso, mude a situação para Encerrado: os itens de encerramento passam a contar. Enquanto o caso está em andamento, essa parte fica cinza."),
 ("Passo 4","Em Painel, resolva primeiro os casos com mais pendências e olhe \"Item mais esquecido\": se o mesmo item pende em vários casos, o problema é a rotina, não o caso."),
 ("Rotina","Na abertura de cada caso, 3 minutos para criar a linha. Na sexta, junto com o caixa, confira os encerrados do mês: caso encerrado sem a última parcela cobrada é dinheiro parado."),
 ("Com a IA","Copie a coluna \"O que falta\" de um caso e use o prompt \"Prazos 07 · Pendências de abertura e encerramento viram tarefas\" da biblioteca do kit."),
])
proteger(wb); salvar(wb,"04-checklist-abertura-e-encerramento.xlsx","Checklist de abertura e encerramento de caso · Kit de Gestão para Advogados")
