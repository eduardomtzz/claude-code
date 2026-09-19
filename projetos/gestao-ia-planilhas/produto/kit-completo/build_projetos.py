#!/usr/bin/env python3
"""Planilha 4 do Kit Completo: Projetos e Prazos. Gera 04-projetos-e-prazos.xlsx"""
from ssg import *
from openpyxl.chart import BarChart, Reference
from datetime import date, timedelta
N=300; R0=5; RN=R0+N-1; NP=10  # etapas, projetos
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Os projetos cadastrados aqui aparecem nas listas da aba Etapas.",merge_to="H")
cfg["A4"]="Equipe ou empresa"; cfg["B4"]="Prisma Comunicação (exemplo fictício)"
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]=date(2026,9,14)
cfg["A6"]="Avisar entregas nos próximos (dias)"; cfg["B6"]=7
for c in ("A4","A5","A6"): rotulo(cfg[c])
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"])
cfg["C5"]="O exemplo está congelado em 14/09/2026, para os arquivos do kit mostrarem a mesma foto. Ao usar com os seus dados, troque por =HOJE()."; nota(cfg["C5"])
cfg["A8"]="Projetos (até 10)"; rotulo(cfg["A8"])
hdr(cfg,9,["Projeto","Cliente ou área","Responsável","Início","Prazo final","Situação"])
for i in range(NP):
    r=10+i
    for c in range(1,6): inp(cfg.cell(row=r,column=c))
    cfg.cell(row=r,column=4).number_format=DATA; cfg.cell(row=r,column=5).number_format=DATA
    cfg.cell(row=r,column=6,value=f'=IF(A{r}="","",IF(COUNTIFS(Etapas!$A${R0}:$A${RN},A{r})=0,"Sem etapas",IF(COUNTIFS(Etapas!$A${R0}:$A${RN},A{r},Etapas!$G${R0}:$G${RN},"Atrasada")>0,"Com atraso",IF(COUNTIFS(Etapas!$A${R0}:$A${RN},A{r},Etapas!$G${R0}:$G${RN},"Concluída")=COUNTIFS(Etapas!$A${R0}:$A${RN},A{r}),"Concluído","No prazo"))))'); calc(cfg.cell(row=r,column=6))
cfg["A21"]="Responsáveis (até 10)"; rotulo(cfg["A21"])
for i in range(10): inp(cfg.cell(row=22+i,column=1))
widths(cfg,(34,26,18,12,12,14,3,3)); cfg.sheet_view.showGridLines=False
# ---------- Etapas ----------
et=wb.create_sheet("Etapas")
titulo(et,"Etapas","Uma linha por etapa. Preencha as colunas amarelas; situação e dias são calculados. Apague os exemplos e comece o seu.",merge_to="K")
hdr(et,4,["Projeto","Etapa","Responsável","Início","Fim previsto","% concluído","Situação","Dias para o fim","Fim real","Observação","Chave"])
HOJE="Config!$B$5"; AVISO="Config!$B$6"
for r in range(R0,RN+1):
    for c in (1,2,3,4,5,6,9,10): inp(et.cell(row=r,column=c))
    et.cell(row=r,column=4).number_format=DATA; et.cell(row=r,column=5).number_format=DATA; et.cell(row=r,column=9).number_format=DATA; et.cell(row=r,column=6).number_format=PCT
    for c in (1,3,4,5,6,9): et.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    # (auditoria final G06) etapa sem fim previsto não é atrasada: é pendência de prazo
    et.cell(row=r,column=7,value=f'=IF(B{r}="","",IF(OR(F{r}>=1,I{r}<>""),"Concluída",IF(E{r}="","Falta o prazo",IF(E{r}<{HOJE},"Atrasada",IF(E{r}-{HOJE}<={AVISO},"Vence em breve",IF(D{r}<={HOJE},"Em andamento","A iniciar"))))))'); calc(et.cell(row=r,column=7))
    # percentual efetivo: fim real preenchido vale 100 %, como o "Como usar" promete
    et.cell(row=r,column=12,value=f'=IF(B{r}="","",IF(I{r}<>"",1,N(F{r})))').font=F(size=9,color=CINZA)
    et.cell(row=r,column=8,value=f'=IF(OR(B{r}="",G{r}="Concluída",E{r}=""),"",E{r}-{HOJE})'); calc(et.cell(row=r,column=8),"0")
    et.cell(row=r,column=11,value=f'=IF(OR(B{r}="",G{r}="Concluída"),0,IF(G{r}="Atrasada",3000+MIN({HOJE}-E{r},60),IF(G{r}="Vence em breve",2000-(E{r}-{HOJE}),IF(G{r}="Em andamento",1000-MIN(E{r}-{HOJE},900),100)))-ROW()/100000)'); et.cell(row=r,column=11).font=F(color=CINZA,size=9)
dvp=lista("=Config!$A$10:$A$19",strict=True); dvp.add(f"A{R0}:A{RN}")
dvr=lista("=Config!$A$22:$A$31",strict=True); dvr.add(f"C{R0}:C{RN}")
dvd=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True); dvd.add(f"D{R0}:E{RN}"); dvd.add(f"I{R0}:I{RN}")
dvpc=DataValidation(type="decimal",operator="between",formula1="0",formula2="1",allow_blank=True,error="Digite entre 0% e 100%",showErrorMessage=True); dvpc.add(f"F{R0}:F{RN}")
for dv in (dvp,dvr,dvd,dvpc): et.add_data_validation(dv)
et.conditional_formatting.add(f"A{R0}:J{RN}", FormulaRule(formula=[f'$G{R0}="Atrasada"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
et.conditional_formatting.add(f"E{R0}:G{RN}", FormulaRule(formula=[f'$G{R0}="Falta o prazo"'], fill=fill("EDEDED"), font=F(color="8A86A0",size=10)))
et.conditional_formatting.add(f"A{R0}:J{RN}", FormulaRule(formula=[f'$G{R0}="Vence em breve"'], fill=fill("FFF4CC")))
et.conditional_formatting.add(f"A{R0}:J{RN}", FormulaRule(formula=[f'$G{R0}="Concluída"'], font=F(color="8A86A0",size=10)))
widths(et,(24,36,16,12,12,11,15,12,12,30,6)); et.column_dimensions["K"].hidden=True; et.column_dimensions["L"].hidden=True
et.freeze_panes="C5"; et.sheet_view.showGridLines=False; et.auto_filter.ref=f"A4:J{RN}"
# exemplos fictícios (Prisma Comunicação, set/2026)
hoje=date(2026,9,14)
proj=[("Site novo · Loja Verde","Loja Verde","Ana",date(2026,8,10),date(2026,10,9)),
      ("Campanha de fim de ano · Bistrô 42","Bistrô 42","Carla",date(2026,9,1),date(2026,11,20)),
      ("Relatório anual · Horizonte","Horizonte","Ana",date(2026,9,8),date(2026,9,30)),
      ("Identidade visual · Padaria do Sol","Padaria do Sol","Bruno",date(2026,7,15),date(2026,9,5))]
for i,(a,b,c,d,e) in enumerate(proj):
    for k,v in enumerate((a,b,c,d,e),start=1): cfg.cell(row=10+i,column=k,value=v)
for i,v in enumerate(["Ana","Bruno","Carla","Diego"]): cfg.cell(row=22+i,column=1,value=v)
ex=[
 ("Site novo · Loja Verde","Briefing e mapa do site","Ana",date(2026,8,10),date(2026,8,15),1,date(2026,8,14)),
 ("Site novo · Loja Verde","Wireframes das 5 páginas","Ana",date(2026,8,16),date(2026,8,26),1,date(2026,8,27)),
 ("Site novo · Loja Verde","Layout da home","Bruno",date(2026,8,27),date(2026,9,8),1,date(2026,9,8)),
 ("Site novo · Loja Verde","Layout das páginas internas","Bruno",date(2026,9,9),date(2026,9,19),0.6,None),
 ("Site novo · Loja Verde","Textos das páginas","Carla",date(2026,9,2),date(2026,9,12),0.7,None),
 ("Site novo · Loja Verde","Implementação","Diego",date(2026,9,20),date(2026,10,3),0,None),
 ("Site novo · Loja Verde","Revisão e publicação","Ana",date(2026,10,4),date(2026,10,9),0,None),
 ("Campanha de fim de ano · Bistrô 42","Conceito criativo","Carla",date(2026,9,1),date(2026,9,12),1,date(2026,9,11)),
 ("Campanha de fim de ano · Bistrô 42","Aprovação do cliente","Carla",date(2026,9,13),date(2026,9,17),0.5,None),
 ("Campanha de fim de ano · Bistrô 42","Produção das peças","Bruno",date(2026,9,18),date(2026,10,15),0,None),
 ("Campanha de fim de ano · Bistrô 42","Plano de mídia","Ana",date(2026,10,1),date(2026,10,20),0,None),
 ("Campanha de fim de ano · Bistrô 42","Veiculação","Diego",date(2026,11,1),date(2026,11,20),0,None),
 ("Relatório anual · Horizonte","Coleta dos números","Ana",date(2026,9,8),date(2026,9,12),1,date(2026,9,12)),
 ("Relatório anual · Horizonte","Redação","Ana",date(2026,9,13),date(2026,9,19),0.3,None),
 ("Relatório anual · Horizonte","Diagramação","Bruno",date(2026,9,20),date(2026,9,26),0,None),
 ("Relatório anual · Horizonte","Revisão final e entrega","Ana",date(2026,9,27),date(2026,9,30),0,None),
 ("Identidade visual · Padaria do Sol","Pesquisa e painel de referências","Bruno",date(2026,7,15),date(2026,7,25),1,date(2026,7,25)),
 ("Identidade visual · Padaria do Sol","Logo: 3 caminhos","Bruno",date(2026,7,26),date(2026,8,12),1,date(2026,8,15)),
 ("Identidade visual · Padaria do Sol","Refino e aplicações","Bruno",date(2026,8,13),date(2026,8,29),1,date(2026,9,2)),
 ("Identidade visual · Padaria do Sol","Manual da marca","Carla",date(2026,8,30),date(2026,9,5),0.8,None),
]
for i,row in enumerate(ex):
    a,b,c,d,e,f,g=row
    for col,v in zip((1,2,3,4,5,6,9),(a,b,c,d,e,f,g)):
        if v is not None: et.cell(row=R0+i,column=col,value=v)
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
p["A1"]='=Config!B4&" · painel de "&TEXT(DAY(Config!B5),"00")&"/"&TEXT(MONTH(Config!B5),"00")&"/"&YEAR(Config!B5)'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:H1")
p["A2"]="Nada para preencher aqui: tudo vem de Config e Etapas."; nota(p["A2"]); p.merge_cells("A2:H2")
p["A6"]=f'=IF(COUNTIF(Etapas!$G${R0}:$G${RN},"Falta o prazo")=0,"","Atenção: "&COUNTIF(Etapas!$G${R0}:$G${RN},"Falta o prazo")&" etapa(s) sem fim previsto na aba Etapas (em cinza lá). Elas não entram em atrasadas nem em \'vence em breve\' até você preencher o prazo.")'
p["A6"].font=F(size=10,bold=True,color=VERM_T); p.merge_cells("A6:H6"); p["A6"].alignment=Alignment(wrap_text=True,vertical="top")
EA=f"Etapas!$A${R0}:$A${RN}"; EG=f"Etapas!$G${R0}:$G${RN}"; EF=f"Etapas!$F${R0}:$F${RN}"; EB=f"Etapas!$B${R0}:$B${RN}"; EE=f"Etapas!$E${R0}:$E${RN}"; EC=f"Etapas!$C${R0}:$C${RN}"; EK=f"Etapas!$K${R0}:$K${RN}"; EFEF=f"Etapas!$L${R0}:$L${RN}"; EH=f"Etapas!$H${R0}:$H${RN}"
kpi(p,4,1,"Projetos ativos",'=COUNTIFS(Config!$F$10:$F$19,"No prazo")+COUNTIFS(Config!$F$10:$F$19,"Com atraso")',LAVANDA,UVA)
kpi(p,4,3,"Etapas atrasadas",f'=COUNTIFS({EG},"Atrasada")',VERM,VERM_T)
kpi(p,4,5,"Vencem em breve",f'=COUNTIFS({EG},"Vence em breve")',SOL,UVA)
kpi(p,4,7,"Concluído (média)",f'=IFERROR(AVERAGEIFS({EFEF},{EB},"<>"),0)',VERDE,VERDE_T,fmt="0%")
p["A7"]="Por projeto"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Projeto","Responsável","Prazo final","Etapas","Concluídas","Atrasadas","% médio","Situação"])
for i in range(NP):
    r=9+i; src=f"Config!$A${10+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",Config!$C${10+i})'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",Config!$E${10+i})'); calc(p.cell(row=r,column=3),DATA)
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({EA},{src}))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({EA},{src},{EG},"Concluída"))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF({src}="","",COUNTIFS({EA},{src},{EG},"Atrasada"))'); calc(p.cell(row=r,column=6))
    p.cell(row=r,column=7,value=f'=IF(OR({src}="",D{r}=0),"",AVERAGEIFS({EFEF},{EA},{src}))'); calc(p.cell(row=r,column=7),PCT)
    p.cell(row=r,column=8,value=f'=IF({src}="","",Config!$F${10+i})'); calc(p.cell(row=r,column=8))
p.conditional_formatting.add("A9:H18", FormulaRule(formula=['$H9="Com atraso"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
p.conditional_formatting.add("A9:H18", FormulaRule(formula=['$H9="Concluído"'], font=F(color="8A86A0",size=10)))
p.conditional_formatting.add("F9:F18", FormulaRule(formula=['F9>0'], font=F(color="C8402E",size=10,bold=True)))
p["A20"]="O que fazer primeiro"; p["A20"].font=F(bold=True,size=13,color=UVA)
p["A21"]="Ordem: atrasadas (mais tempo de atraso primeiro), depois as que vencem em breve, depois em andamento."; nota(p["A21"])
hdr(p,22,["#","Projeto","Etapa","Responsável","Fim previsto","Situação","Dias","% feito"])
TOP=12
for k in range(1,TOP+1):
    r=22+k; m=f'MATCH(LARGE({EK},{k}),{EK},0)'; g=f'LARGE({EK},{k})>0'
    p.cell(row=r,column=1,value=k)
    for col,rng in zip((2,3,4,5,6,7,8),(EA,EB,EC,EE,EG,EH,EF)):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},INDEX({rng},{m}),""),"")')
    for col in range(1,9): calc(p.cell(row=r,column=col),center=(col not in (2,3)))
    p.cell(row=r,column=5).number_format=DATA; p.cell(row=r,column=8).number_format=PCT; p.cell(row=r,column=7).number_format="0"
p.conditional_formatting.add(f"A23:H{22+TOP}", FormulaRule(formula=['$F23="Atrasada"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
p.conditional_formatting.add(f"A23:H{22+TOP}", FormulaRule(formula=['$F23="Vence em breve"'], fill=fill("FFF4CC")))
p["A36"]="Carga por responsável"; p["A36"].font=F(bold=True,size=13,color=UVA)
hdr(p,37,["Responsável","Etapas abertas","Atrasadas","Vencem em breve","Próximo fim"])
for i in range(10):
    r=38+i; src=f"Config!$A${22+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({EC},{src},{EB},"<>")-COUNTIFS({EC},{src},{EG},"Concluída"))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({EC},{src},{EG},"Atrasada"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({EC},{src},{EG},"Vence em breve"))'); calc(p.cell(row=r,column=4))
    # Menor data com condição sem MINIFS (que exige Excel > 2016 perpétuo):
    # soma-se 1E+10 nas linhas que não casam, para elas nunca ganharem o MIN.
    cond=f'({EC}={src})*({EG}<>"Concluída")*({EB}<>"")*({EE}<>"")'
    mf=f'SUMPRODUCT(MIN({cond}*{EE}+(1-{cond})*1E+10))'
    p.cell(row=r,column=5,value=f'=IF({src}="","",IFERROR(IF(OR({mf}=0,{mf}>=1E+10),"",{mf}),""))'); calc(p.cell(row=r,column=5),DATA)
widths(p,(30,16,14,12,12,12,12,14)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- Linha do tempo ----------
lt=wb.create_sheet("Linha do tempo",1)
lt["A1"]="Linha do tempo (semanas)"; lt["A1"].font=F(bold=True,size=16,color=UVA)
lt["A2"]="As 40 primeiras etapas da aba Etapas, semana a semana, a partir da segunda-feira da data de referência. Barra roxa: etapa em curso; cinza: concluída; vermelha: atrasada."; nota(lt["A2"]); lt.merge_cells("A2:R2")
lt["A3"]="Começar em"; rotulo(lt["A3"]); lt["B3"]="=Config!$B$5-WEEKDAY(Config!$B$5,3)-7"; calc(lt["B3"],DATA)
lt["C3"]="(uma semana antes da data de referência; mude a data em Config para navegar)"; nota(lt["C3"])
W=14
hdr(lt,4,["Projeto","Etapa","Resp.","Fim"])
for w in range(W):
    c=lt.cell(row=4,column=5+w,value=f"=$B$3+{7*w}"); c.font=F(bold=True,color=BRANCO,size=8); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center",vertical="center",textRotation=90); c.number_format="dd/mm"; c.border=borda
lt.row_dimensions[4].height=42
for i in range(40):
    r=5+i; e=R0+i
    lt.cell(row=r,column=1,value=f'=IF(Etapas!B{e}="","",Etapas!A{e})'); calc(lt.cell(row=r,column=1),center=False)
    lt.cell(row=r,column=2,value=f'=IF(Etapas!B{e}="","",Etapas!B{e})'); calc(lt.cell(row=r,column=2),center=False)
    lt.cell(row=r,column=3,value=f'=IF(Etapas!B{e}="","",Etapas!C{e})'); calc(lt.cell(row=r,column=3))
    lt.cell(row=r,column=4,value=f'=IF(Etapas!B{e}="","",Etapas!E{e})'); calc(lt.cell(row=r,column=4),DATA)
    for w in range(W):
        col=5+w; cl=L(col)
        c=lt.cell(row=r,column=col,value=f'=IF(Etapas!$B{e}="","",IF(AND({cl}$4<=Etapas!$E{e},{cl}$4+6>=Etapas!$D{e}),IF(Etapas!$G{e}="Concluída",1,IF(Etapas!$G{e}="Atrasada",3,2)),""))')
        c.font=F(color=BRANCO,size=8); c.border=Border(left=Side(style="thin",color="EEE9F6"),right=Side(style="thin",color="EEE9F6"),top=thin,bottom=thin); c.alignment=Alignment(horizontal="center")
rng=f"E5:{L(4+W)}44"
lt.conditional_formatting.add(rng, FormulaRule(formula=['E5=1'], fill=fill("CFC6E0"), font=F(color="CFC6E0",size=8)))
lt.conditional_formatting.add(rng, FormulaRule(formula=['E5=2'], fill=fill(LILAS), font=F(color=LILAS,size=8)))
lt.conditional_formatting.add(rng, FormulaRule(formula=['E5=3'], fill=fill("C8402E"), font=F(color="C8402E",size=8)))
lt.conditional_formatting.add(f"E4:{L(4+W)}4", FormulaRule(formula=['AND(E$4<=Config!$B$5,E$4+6>=Config!$B$5)'], fill=fill(SOL), font=F(color=UVA,size=8,bold=True)))
widths(lt,[24,30,8,10]+[4.2]*W); lt.freeze_panes="E5"; lt.sheet_view.showGridLines=False
# ---------- Como usar ----------
como_usar(wb,"Projetos e Prazos",[
 ("O que esta planilha faz","Você cadastra os projetos e as etapas de cada um; ela diz o que está atrasado, o que vence em breve, quanto cada projeto avançou, quem está sobrecarregado e desenha a linha do tempo por semanas."),
 ("Passo 1","Em Config, preencha o nome da equipe, troque a data de referência por =HOJE() (no exemplo ela está congelada em 14/09/2026), cadastre até 10 projetos (nome, cliente, responsável, início e prazo final) e as pessoas da equipe."),
 ("Passo 2","Em Etapas, uma linha por etapa: projeto (lista), etapa, responsável (lista), início, fim previsto e % concluído. Quando terminar, marque 100% ou preencha o fim real."),
 ("Passo 3","Em Painel, veja os projetos com atraso, a lista do que fazer primeiro e a carga por pessoa. Em Linha do tempo, veja as próximas 14 semanas."),
 ("Rotina","Segunda-feira, 10 minutos: atualize o % das etapas em andamento e olhe o Painel. Sexta: registre o que fechou."),
 ("Com a IA","Copie a tabela \"O que fazer primeiro\" e use o prompt \"Organizar 03: prioridade quando tudo parece urgente\". Para o cliente, copie \"Por projeto\" e use \"Escrever 04: justificativa\" ou \"Escrever 07: resumo para quem não foi\"."),
])
proteger(wb); salvar(wb,"04-projetos-e-prazos.xlsx","Projetos e Prazos · Kit IA no Trabalho Completo")
