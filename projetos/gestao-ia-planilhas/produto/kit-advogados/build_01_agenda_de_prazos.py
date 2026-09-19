#!/usr/bin/env python3
"""Planilha 1 do Kit de Gestão para Advogados: Agenda de prazos e audiências. Gera 01-agenda-de-prazos.xlsx"""
from ssg import *
import dados
N=400; R0=5; RN=R0+N-1; NRESP=10; NTIPO=20; TOP=30
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Responsáveis e tipos de prazo aparecem nas listas da aba Prazos.",merge_to="F")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]=dados.HOJE
cfg["A6"]="Alerta: avisar prazos nos próximos (dias)"; cfg["B6"]=7
cfg["A7"]="Janela do painel: prazos nos próximos (dias)"; cfg["B7"]=30
for c in ("A4","A5","A6","A7"): rotulo(cfg[c])
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],center=True); inp(cfg["B7"],center=True)
cfg["C5"]="O exemplo está congelado em 14/09/2026, para os arquivos do kit mostrarem a mesma foto. Ao usar com os seus dados, troque por =HOJE()."; nota(cfg["C5"])
cfg["C6"]="Prazos dentro desse número de dias ficam em alerta amarelo no painel."; nota(cfg["C6"])
cfg["C7"]="Prazos entre o alerta e essa janela contam no quarto quadro do painel; o resto fica como \"Depois\"."; nota(cfg["C7"])
cfg["A9"]=f"Responsáveis (até {NRESP})"; cfg["D9"]=f"Tipos de prazo (até {NTIPO})"; rotulo(cfg["A9"]); rotulo(cfg["D9"])
for i in range(NRESP): inp(cfg.cell(row=10+i,column=2))
for i in range(NTIPO): inp(cfg.cell(row=10+i,column=4))
for i,(n,_,_,_) in enumerate(dados.PESSOAS): cfg.cell(row=10+i,column=2,value=n)
TIPOS=dados.TIPOS_PRAZO
for i,t in enumerate(TIPOS): cfg.cell(row=10+i,column=4,value=t)
cfg["A31"]="Preencha responsáveis e tipos de cima para baixo, sem pular linha: as listas suspensas param na última linha preenchida."; nota(cfg["A31"])
cfg["A32"]="O tipo de prazo é só um rótulo para organizar a agenda. Conte os dias e confira a data na fonte oficial: a planilha avisa, não calcula prazo."; nota(cfg["A32"])
cfg["A33"]="No exemplo, a estagiária (Júlia Prado) responde pelos prazos de juntada de documentos; o caso continua com o sócio responsável (por isso ela tem prazos aqui e nenhum caso nas planilhas 02, 04 e 13)."; nota(cfg["A33"])
widths(cfg,(40,26,4,30,4,4)); cfg.sheet_view.showGridLines=False
# ---------- Prazos ----------
pz=wb.create_sheet("Prazos")
titulo(pz,"Prazos","Uma linha por prazo, audiência ou compromisso. Preencha as colunas amarelas; dias e situação são calculados. Quando cumprir, marque Sim em Feito.",merge_to="J")
hdr(pz,4,["Processo","Cliente","Tipo de prazo","Data","Responsável","Feito?","Observação","Dias","Situação","Chave"])
HOJE="Config!$B$5"; AL="Config!$B$6"; JAN="Config!$B$7"
for r in range(R0,RN+1):
    for c in (1,2,3,4,5,6,7): inp(pz.cell(row=r,column=c))
    for c in (3,4,5,6): pz.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    pz.cell(row=r,column=4).number_format=DATA
    pz.cell(row=r,column=9,value=f'=IF(AND(A{r}="",C{r}="",D{r}=""),"",IF(F{r}="Sim","Feito",IF(D{r}="","Sem data",IF(D{r}<{HOJE},"Atrasado",IF(D{r}={HOJE},"Hoje",IF(D{r}-{HOJE}<={AL},"Até "&{AL}&" dias",IF(D{r}-{HOJE}<={JAN},"Até "&{JAN}&" dias","Depois")))))))'); calc(pz.cell(row=r,column=9))
    pz.cell(row=r,column=8,value=f'=IF(OR(I{r}="",I{r}="Feito",I{r}="Sem data"),"",D{r}-{HOJE})'); calc(pz.cell(row=r,column=8),"0")
    pz.cell(row=r,column=10,value=f'=IF(OR(I{r}="",I{r}="Feito",I{r}="Sem data"),0,IF(I{r}="Atrasado",3000+MIN({HOJE}-D{r},60),IF(I{r}="Hoje",2500,IF(D{r}-{HOJE}<={AL},2000-(D{r}-{HOJE}),IF(D{r}-{HOJE}<={JAN},1000-(D{r}-{HOJE}),500-MIN(D{r}-{HOJE},400)))))-ROW()/100000)'); pz.cell(row=r,column=10).font=F(color=CINZA,size=9)
dvt=lista(f"=OFFSET(Config!$D$10,0,0,MAX(1,COUNTA(Config!$D$10:$D${9+NTIPO})),1)",strict=True); dvt.add(f"C{R0}:C{RN}")
dvr=lista(f"=OFFSET(Config!$B$10,0,0,MAX(1,COUNTA(Config!$B$10:$B${9+NRESP})),1)",strict=True); dvr.add(f"E{R0}:E{RN}")
dvf=lista('"Sim"'); dvf.add(f"F{R0}:F{RN}")
dvd=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True); dvd.add(f"D{R0}:D{RN}")
for dv in (dvt,dvr,dvf,dvd): pz.add_data_validation(dv)
pz.conditional_formatting.add(f"A{R0}:I{RN}", FormulaRule(formula=[f'$I{R0}="Atrasado"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
pz.conditional_formatting.add(f"A{R0}:I{RN}", FormulaRule(formula=[f'$I{R0}="Hoje"'], fill=fill(SOL), font=F(color=UVA,size=10,bold=True)))
pz.conditional_formatting.add(f"A{R0}:I{RN}", FormulaRule(formula=[f'LEFT($I{R0},4)="Até "'], fill=fill("FFF4CC")))
pz.conditional_formatting.add(f"A{R0}:I{RN}", FormulaRule(formula=[f'$I{R0}="Feito"'], font=F(color="8A86A0",size=10)))
widths(pz,(28,26,24,12,16,8,36,7,14,6)); pz.column_dimensions["J"].hidden=True
pz.freeze_panes="C5"; pz.sheet_view.showGridLines=False; pz.auto_filter.ref=f"A4:I{RN}"
# exemplos: prazos dos casos ativos de dados.py (o prazo principal de cada caso é a "próxima ação" da planilha 02) + compromissos extras e dois já cumpridos
ex=[(num,cli,t,dados.prazo_formula(d),resp,"Sim" if feito else "",o) for num,cli,t,d,resp,feito,o in dados.PRAZOS()]
for i,row in enumerate(ex):
    for col,v in enumerate(row,start=1):
        if v!="": pz.cell(row=R0+i,column=col,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Painel de prazos · "&TEXT(DAY(Config!$B$5),"00")&"/"&TEXT(MONTH(Config!$B$5),"00")&"/"&YEAR(Config!$B$5)',"Nada para digitar aqui: tudo vem de Config e Prazos. A planilha avisa; a conferência do prazo é de quem responde por ele.",merge_to="L")
PA=f"Prazos!$A${R0}:$A${RN}"; PB=f"Prazos!$B${R0}:$B${RN}"; PC=f"Prazos!$C${R0}:$C${RN}"; PD=f"Prazos!$D${R0}:$D${RN}"; PE_=f"Prazos!$E${R0}:$E${RN}"
PF=f"Prazos!$F${R0}:$F${RN}"; PH=f"Prazos!$H${R0}:$H${RN}"; PI=f"Prazos!$I${R0}:$I${RN}"; PJ=f"Prazos!$J${R0}:$J${RN}"
kpi(p,4,1,"Atrasados",f'=COUNTIFS({PI},"Atrasado")',VERM,VERM_T)
kpi(p,4,3,"Hoje",f'=COUNTIFS({PI},"Hoje")',SOL,UVA)
kpi(p,4,5,f'="Próximos "&{AL}&" dias"',f'=COUNTIFS({PI},"Até "&{AL}&" dias")',"FFE9A8",UVA)
kpi(p,4,7,f'="De "&({AL}+1)&" a "&{JAN}&" dias"',f'=COUNTIFS({PI},"Até "&{JAN}&" dias")',LAVANDA,UVA)
kpi(p,4,9,"Abertos no total",f'=COUNTIF({PJ},">0")+COUNTIFS({PI},"Sem data")',LAVANDA,UVA)
kpi(p,4,11,"Feitos",f'=COUNTIFS({PI},"Feito")',VERDE,VERDE_T)
p["A7"]="O que vence primeiro"; p["A7"].font=F(bold=True,size=13,color=UVA)
p["A8"]=f"Ordem: atrasados (mais tempo de atraso primeiro), hoje, depois os mais próximos. Mostra os {TOP} primeiros (cabe a semana inteira); os demais ficam na aba Prazos, que pode ser filtrada por situação."; nota(p["A8"]); p.merge_cells("A8:L8")
hdr(p,9,["#","Processo","Cliente","Tipo de prazo","Data","Dias","Situação","Responsável"])
for k in range(1,TOP+1):
    r=9+k; m=f'MATCH(LARGE({PJ},{k}),{PJ},0)'; g=f'LARGE({PJ},{k})>0'
    p.cell(row=r,column=1,value=k)
    for col,rng in zip((2,3,4,5,6,7,8),(PA,PB,PC,PD,PH,PI,PE_)):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},IF(INDEX({rng},{m})="","",INDEX({rng},{m})),""),"")')
    for col in range(1,9): calc(p.cell(row=r,column=col),center=(col not in (2,3,4)))
    p.cell(row=r,column=5).number_format=DATA; p.cell(row=r,column=6).number_format="0"
p.conditional_formatting.add(f"A10:H{9+TOP}", FormulaRule(formula=['$G10="Atrasado"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
p.conditional_formatting.add(f"A10:H{9+TOP}", FormulaRule(formula=['$G10="Hoje"'], fill=fill(SOL), font=F(color=UVA,size=10,bold=True)))
p.conditional_formatting.add(f"A10:H{9+TOP}", FormulaRule(formula=['LEFT($G10,4)="Até "'], fill=fill("FFF4CC")))
r0=9+TOP+2
p.cell(row=r0,column=1,value="Carga por responsável").font=F(bold=True,size=13,color=UVA)
hdr(p,r0+1,["","Responsável","Abertos","Atrasados","Hoje","Em alerta","Mais antigo em aberto","Feitos"])
p.merge_cells(start_row=r0+1,start_column=1,end_row=r0+1,end_column=2); p.cell(row=r0+1,column=1,value="Responsável"); p.cell(row=r0+1,column=2,value=None)
for i in range(NRESP):
    r=r0+2+i; src=f"Config!$B${10+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PJ},">0")+COUNTIFS({PE_},{src},{PI},"Sem data"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PI},"Atrasado"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PI},"Hoje"))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PI},"Até "&{AL}&" dias"))'); calc(p.cell(row=r,column=6))
    # menor data em aberto do responsável, sem MÍNIMOSES (Excel 2016 e Google Sheets): datas fora da condição viram 1E+10 e saem do MIN
    cond=f'(({PE_}={src})*({PJ}>0))'
    mf=f'SUMPRODUCT(MIN({cond}*{PD}+(1-{cond})*1E+10))'
    p.cell(row=r,column=7,value=f'=IF({src}="","",IFERROR(IF({mf}>=1E+10,"",{mf}),""))'); calc(p.cell(row=r,column=7),DATA)
    p.cell(row=r,column=8,value=f'=IF({src}="","",COUNTIFS({PE_},{src},{PI},"Feito"))'); calc(p.cell(row=r,column=8))
p.conditional_formatting.add(f"D{r0+2}:D{r0+1+NRESP}", FormulaRule(formula=[f'AND(ISNUMBER(D{r0+2}),D{r0+2}>0)'], font=F(color="C8402E",size=10,bold=True)))
p.cell(row=r0+2+NRESP,column=1,value="Prazos sem responsável não entram nesta tabela: confira na aba Prazos, filtrando a coluna Responsável por vazio.").font=F(size=9,color=LILAS)
r1=r0+NRESP+5
p.cell(row=r1,column=1,value="Próximos 7 dias, dia a dia").font=F(bold=True,size=13,color=UVA)
hdr(p,r1+1,["Dia","Data","Prazos","Do responsável 1","Do responsável 2","Do responsável 3"])
p.merge_cells(start_row=r1+1,start_column=1,end_row=r1+1,end_column=2); p.cell(row=r1+1,column=1,value="Dia"); p.cell(row=r1+1,column=2,value=None)
p.cell(row=r1+1,column=3,value="Data"); p.cell(row=r1+1,column=4,value="Prazos abertos")
for j in range(3): p.cell(row=r1+1,column=5+j,value=f'=IF(Config!$B${10+j}="","",Config!$B${10+j})')
for c in range(1,8): p.cell(row=r1+1,column=c).font=F(bold=True,color=BRANCO,size=10); p.cell(row=r1+1,column=c).fill=fill(UVA); p.cell(row=r1+1,column=c).alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); p.cell(row=r1+1,column=c).border=borda
for d in range(7):
    r=r1+2+d
    p.cell(row=r,column=1,value=f'=CHOOSE(WEEKDAY(C{r}),"domingo","segunda","terça","quarta","quinta","sexta","sábado")'); calc(p.cell(row=r,column=1)); p.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f"={HOJE}+{d}"); calc(p.cell(row=r,column=3),DATA)
    p.cell(row=r,column=4,value=f'=COUNTIFS({PD},C{r},{PF},"<>Sim")'); calc(p.cell(row=r,column=4))
    for j in range(3):
        p.cell(row=r,column=5+j,value=f'=IF(Config!$B${10+j}="","",COUNTIFS({PD},C{r},{PF},"<>Sim",{PE_},Config!$B${10+j}))'); calc(p.cell(row=r,column=5+j))
p.conditional_formatting.add(f"A{r1+2}:G{r1+8}", FormulaRule(formula=[f'$D{r1+2}>0'], font=F(color=UVA,size=10,bold=True)))
p.cell(row=r1+9,column=1,value="Os atrasados não aparecem aqui: estão no primeiro quadro e no topo de \"O que vence primeiro\".").font=F(size=9,color=LILAS)
widths(p,(6,28,26,24,12,8,14,16,10,10,10,10)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Como usar ----------
como_usar(wb,"Agenda de prazos e audiências",[
 ("O que esta planilha faz","Reúne todos os prazos, audiências e compromissos do escritório em uma lista só e mostra, no Painel, o que está atrasado, o que vence hoje, o que vence nos próximos dias, quem responde por cada um e quantos caem em cada dia da semana."),
 ("Passo 1","Em Config, troque a data de referência por =HOJE() (no exemplo ela está congelada em 14/09/2026), cadastre as pessoas do escritório e ajuste a lista de tipos de prazo. Preencha de cima para baixo, sem pular linha."),
 ("Passo 2","Em Prazos, apague os exemplos e registre uma linha por prazo: processo, cliente, tipo (lista), data, responsável (lista) e observação. Quando cumprir, marque Sim em Feito: a linha fica cinza e sai do painel."),
 ("Passo 3","Em Painel, leia de cima para baixo: quadros de contagem, lista \"O que vence primeiro\", carga por responsável e os próximos 7 dias."),
 ("Rotina de segunda","10 minutos: abra o Painel e trate os atrasados. Prazo processual em atraso NÃO se reagenda aqui: confira na fonte oficial (sistema do tribunal, publicação) e leve ao responsável; a planilha mantém a data original e serve só de registro. Só tarefa administrativa pode ser remarcada. Depois confirme os prazos da semana e registre os que chegaram."),
 ("Exemplo","Os prazos do exemplo são os dos 38 casos da planilha 13 · Carteira (a 13 é a fonte do cadastro de casos); o prazo principal de cada caso é a mesma \"próxima ação\" da planilha 02. Audiência já realizada não conta como atraso: marque Feito."),
 ("Limite","A planilha organiza e avisa. A contagem do prazo, a conferência da data na fonte oficial e o cumprimento continuam sendo responsabilidade de quem responde pelo caso."),
 ("Com a IA","Copie a tabela \"O que vence primeiro\" e use o prompt \"Prazos 04 · Distribuir a semana entre as pessoas\" da biblioteca do kit."),
])
proteger(wb); salvar(wb,"01-agenda-de-prazos.xlsx","Agenda de prazos e audiências · Kit de Gestão para Advogados")
