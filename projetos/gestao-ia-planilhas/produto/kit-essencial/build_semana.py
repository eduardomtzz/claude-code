#!/usr/bin/env python3
"""Planilha 1 do Kit IA no Trabalho: Semana Organizada. Gera 01-semana-organizada.xlsx"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter

UVA="3B1F5E"; SOL="FFC83D"; LILAS="7A5AA8"; LAVANDA="F3EEFB"; CREME="FFFAF0"; TINTA="1F1235"; AMARELO="FFF4CC"; BRANCO="FFFFFF"
F=lambda **k: Font(name="Arial", **k)
fill=lambda c: PatternFill("solid", fgColor=c)
thin=Side(style="thin", color="DCD2EC"); borda=Border(left=thin,right=thin,top=thin,bottom=thin)
N_ROWS=300; FIRST=4; LAST=FIRST+N_ROWS-1   # linhas 4..303

wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
cfg["A1"]="Configurações"; cfg["A1"].font=F(bold=True,size=16,color=UVA)
cfg["A2"]="Células amarelas: você preenche. As demais são calculadas."; cfg["A2"].font=F(italic=True,size=10,color=LILAS)
cfg["A4"]="Data de referência (hoje)"; cfg["B4"]="=TODAY()"; cfg["C4"]="Deixe =HOJE() ou digite uma data (ex.: 13/09/2026) para simular outro dia."
cfg["A6"]="Capacidade por dia (horas)"; cfg["B6"]=6; cfg["C6"]="Quantas horas de trabalho focado cabem no seu dia."
cfg["A8"]="Responsáveis"; cfg["D8"]="Status"; cfg["F8"]="Projetos ou clientes"
for r,v in enumerate(["Ana (você)","Bruno","Carla"],start=9): cfg.cell(row=r,column=2,value=v)
for r,v in enumerate(["A fazer","Fazendo","Feito","Cancelado"],start=9): cfg.cell(row=r,column=4,value=v)
for r,v in enumerate(["Relatório mensal","Cliente Aurora","Interno","Cliente Horizonte"],start=9): cfg.cell(row=r,column=6,value=v)
for c in ("A4","A6","A8","D8","F8"): cfg[c].font=F(bold=True,color=UVA)
for c in ("C4","C6"): cfg[c].font=F(size=10,color=LILAS)
cfg["B4"].number_format="dd/mm/yyyy"
for rng in ("B4","B6"): cfg[rng].fill=fill(AMARELO); cfg[rng].protection=Protection(locked=False); cfg[rng].border=borda; cfg[rng].font=F(color=TINTA)
CINZA="F2F2F2"
for r in range(9,17):
    for col in (2,6):
        c=cfg.cell(row=r,column=col); c.fill=fill(AMARELO); c.border=borda; c.font=F(color=TINTA); c.protection=Protection(locked=False)
for r in range(9,13):  # status: lista fixa, bloqueada, fundo cinza claro (não é célula de preenchimento)
    c=cfg.cell(row=r,column=4); c.fill=fill(CINZA); c.border=borda; c.font=F(color=TINTA)
cfg["A18"]="A lista de status é fixa (fundo cinza): as fórmulas dependem de \"Feito\" e \"Cancelado\"."; cfg["A18"].font=F(size=10,color=LILAS)
cfg["A19"]="Preencha responsáveis e projetos de cima para baixo, sem pular linha: as listas suspensas param na última linha preenchida."; cfg["A19"].font=F(size=10,color=LILAS)
for col,w in zip("ABCDEF",(30,22,70,14,4,26)): cfg.column_dimensions[col].width=w
cfg.sheet_view.showGridLines=False

# ---------- Tarefas ----------
t=wb.create_sheet("Tarefas")
t["A1"]="Tarefas"; t["A1"].font=F(bold=True,size=16,color=UVA)
t["A2"]="Preencha só as colunas amarelas. Prioridade, dias, situação e ordem são calculados. Apague os exemplos e comece a sua lista."; t["A2"].font=F(italic=True,size=10,color=LILAS)
heads=["ID","Tarefa","Projeto ou cliente","Responsável","Prazo","Impacto (1-3)","Urgência (1-3)","Horas","Status","Prioridade","Dias p/ prazo","Situação","Ordem","Observação"]
widths=[5,44,20,14,12,12,12,8,12,12,12,13,9,36]
for i,(h,w) in enumerate(zip(heads,widths),start=1):
    c=t.cell(row=3,column=i,value=h); c.font=F(bold=True,color=BRANCO); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True); c.border=borda
    t.column_dimensions[get_column_letter(i)].width=w
t.row_dimensions[3].height=32
inputs=[2,3,4,5,6,7,8,9,14]
for r in range(FIRST,LAST+1):
    t.cell(row=r,column=1,value=f'=IF(B{r}="","",ROW()-{FIRST-1})')
    t.cell(row=r,column=10,value=f'=IF(B{r}="","",IF(F{r}*G{r}>=6,"Alta",IF(F{r}*G{r}>=3,"Média","Baixa")))')
    t.cell(row=r,column=11,value=f'=IF(OR(B{r}="",E{r}=""),"",E{r}-Config!$B$4)')
    t.cell(row=r,column=12,value=f'=IF(B{r}="","",IF(OR(I{r}="Feito",I{r}="Cancelado"),I{r},IF(E{r}="","Sem prazo",IF(K{r}<0,"Atrasada",IF(K{r}=0,"Hoje",IF(K{r}<=6,"Esta semana","Depois"))))))')
    t.cell(row=r,column=13,value=f'=IF(OR(B{r}="",L{r}="Feito",L{r}="Cancelado",L{r}="Sem prazo",L{r}="Depois"),0,IF(L{r}="Atrasada",2000,IF(L{r}="Hoje",1500,500))+F{r}*G{r}*100+IF(K{r}<0,MIN(-K{r},30),10-K{r})-ROW()/100000)')
    for col in range(1,15):
        c=t.cell(row=r,column=col); c.border=borda; c.font=F(color=TINTA,size=10)
        if col in inputs: c.fill=fill(AMARELO); c.protection=Protection(locked=False)
        if col==5: c.number_format="dd/mm/yyyy"
        if col in (6,7,8,11,13,1): c.alignment=Alignment(horizontal="center")
    t.cell(row=r,column=13).font=F(color="B0A6C4",size=9)
# validações
dv_resp=DataValidation(type="list",formula1="=OFFSET(Config!$B$9,0,0,MAX(1,COUNTA(Config!$B$9:$B$16)),1)",allow_blank=True,showErrorMessage=True); dv_resp.add(f"D{FIRST}:D{LAST}")
dv_123=DataValidation(type="list",formula1='"1,2,3"',allow_blank=True,showErrorMessage=True); dv_123.add(f"F{FIRST}:G{LAST}")
dv_status=DataValidation(type="list",formula1="=Config!$D$9:$D$12",allow_blank=True,showErrorMessage=True); dv_status.add(f"I{FIRST}:I{LAST}")
dv_proj=DataValidation(type="list",formula1="=OFFSET(Config!$F$9,0,0,MAX(1,COUNTA(Config!$F$9:$F$16)),1)",allow_blank=True,showErrorMessage=True); dv_proj.add(f"C{FIRST}:C{LAST}")
dv_data=DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True); dv_data.add(f"E{FIRST}:E{LAST}")
dv_h=DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True,showErrorMessage=True); dv_h.add(f"H{FIRST}:H{LAST}")
for dv in (dv_resp,dv_123,dv_status,dv_proj,dv_data,dv_h): t.add_data_validation(dv)
# formatação condicional
rng=f"A{FIRST}:N{LAST}"
t.conditional_formatting.add(rng, FormulaRule(formula=[f'$L{FIRST}="Atrasada"'], fill=fill("FBE4E4"), font=Font(name="Arial",color="7A1F1F",size=10)))
t.conditional_formatting.add(rng, FormulaRule(formula=[f'$L{FIRST}="Hoje"'], fill=fill("FFF1BF")))
t.conditional_formatting.add(rng, FormulaRule(formula=[f'OR($L{FIRST}="Feito",$L{FIRST}="Cancelado")'], font=Font(name="Arial",color="8C8C8C",size=10)))
t.conditional_formatting.add(f"J{FIRST}:J{LAST}", FormulaRule(formula=[f'$J{FIRST}="Alta"'], font=Font(name="Arial",bold=True,color=UVA,size=10)))
t.merge_cells("A2:N2"); t.column_dimensions["M"].hidden=True
t.freeze_panes="C4"; t.sheet_view.showGridLines=False
t.auto_filter.ref=f"A3:N{LAST}"
# exemplos (empresa fictícia: Ana, analista de marketing na Prisma)
# Prazos relativos a HOJE(), para o exemplo não envelhecer. O deslocamento +1 reproduz a distribuição
# original vista em 13/09/2026 (2 atrasadas, 1 para hoje, 9 nesta semana).
def d(n):
    k=n+1
    return "=TODAY()" if k==0 else f"=TODAY(){k:+d}"
ex=[
("Enviar relatório de setembro para a diretoria","Relatório mensal","Ana (você)",d(-2),3,3,2,"Fazendo","Faltam os gráficos de vendas"),
("Revisar proposta comercial da Aurora","Cliente Aurora","Ana (você)",d(-1),3,2,1.5,"A fazer","Cliente pediu desconto de 10%"),
("Responder pesquisa de clima","Interno","Ana (você)",d(-3),1,1,0.5,"A fazer",""),
("Montar apresentação da reunião de quinta","Cliente Horizonte","Ana (você)",d(0),3,3,3,"A fazer","Usar o modelo de 8 slides do kit"),
("Atualizar planilha de leads","Cliente Aurora","Bruno",d(0),2,2,1,"Fazendo",""),
("Aprovar arte do post de terça","Cliente Horizonte","Carla",d(0),2,3,0.5,"A fazer",""),
("Reunião de alinhamento com o Bruno","Interno","Ana (você)",d(1),2,2,1,"A fazer","14h"),
("Fechar pauta de outubro","Cliente Aurora","Carla",d(2),3,2,2,"A fazer",""),
("Conferir faturas dos fornecedores","Interno","Ana (você)",d(3),2,1,1,"A fazer",""),
("Escrever e-mail de resultados para a Horizonte","Cliente Horizonte","Ana (você)",d(3),3,2,1,"A fazer","Usar prompt Escrever 04"),
("Organizar pasta de fotos do evento","Interno","Bruno",d(4),1,1,2,"A fazer",""),
("Preparar orçamento do vídeo institucional","Cliente Aurora","Ana (você)",d(5),3,1,2,"A fazer",""),
("Treinar estagiário na planilha de leads","Interno","Bruno",d(6),2,1,1.5,"A fazer",""),
("Relatório de mídia de agosto","Relatório mensal","Ana (você)",d(-10),3,3,3,"Feito",""),
("Renovar domínio do site","Interno","Carla",d(9),2,1,0.5,"A fazer",""),
("Pesquisar concorrentes da Horizonte","Cliente Horizonte","Bruno",d(12),2,2,4,"A fazer",""),
("Briefing da campanha de fim de ano","Cliente Aurora","Ana (você)",d(15),3,1,2,"A fazer",""),
("Post sobre lançamento cancelado","Cliente Horizonte","Carla",d(-4),1,2,1,"Cancelado","Cliente adiou o lançamento"),
("Revisar contrato de prestação de serviço","Interno","Ana (você)",None,2,1,1,"A fazer","Sem prazo definido ainda"),
("Backup mensal dos arquivos","Interno","Bruno",d(-7),2,2,1,"Feito",""),
]
for i,row in enumerate(ex):
    r=FIRST+i
    for col,val in zip([2,3,4,5,6,7,8,9,14],row):
        if val is not None: t.cell(row=r,column=col,value=val)

# ---------- Hoje ----------
h=wb.create_sheet("Hoje",0)
h["A1"]="Hoje"; h["A1"].font=F(bold=True,size=18,color=UVA)
h["A2"]="=\"Painel de \"&TEXT(Config!B4,\"dd/mm/yyyy\")&\". Nada para preencher aqui: tudo vem da aba Tarefas.\""; h["A2"].font=F(italic=True,size=10,color=LILAS)
kpis=[("Atrasadas",'=COUNTIF(Tarefas!$L$4:$L$303,"Atrasada")',"FBE4E4","7A1F1F"),
      ("Para hoje",'=COUNTIF(Tarefas!$L$4:$L$303,"Hoje")',SOL,UVA),
      ("Esta semana",'=COUNTIF(Tarefas!$L$4:$L$303,"Esta semana")',LAVANDA,UVA),
      ("Abertas no total",'=COUNTIFS(Tarefas!$B$4:$B$303,"<>",Tarefas!$I$4:$I$303,"<>Feito",Tarefas!$I$4:$I$303,"<>Cancelado")',LAVANDA,UVA),
      ("Feitas",'=COUNTIF(Tarefas!$I$4:$I$303,"Feito")',"DDF3E7","155E3C")]
for i,(lab,fml,bg,fg) in enumerate(kpis):
    col=1+i*2
    a=h.cell(row=4,column=col,value=lab); a.font=F(size=9,bold=True,color=fg); a.fill=fill(bg); a.alignment=Alignment(horizontal="center")
    b=h.cell(row=5,column=col,value=fml); b.font=F(size=22,bold=True,color=fg); b.fill=fill(bg); b.alignment=Alignment(horizontal="center")
    h.merge_cells(start_row=4,start_column=col,end_row=4,end_column=col+1); h.merge_cells(start_row=5,start_column=col,end_row=5,end_column=col+1)
    h.cell(row=4,column=col+1).fill=fill(bg); h.cell(row=5,column=col+1).fill=fill(bg)
h.row_dimensions[5].height=34
# O que fazer primeiro
h["A7"]="O que fazer primeiro"; h["A7"].font=F(bold=True,size=13,color=UVA)
h["A8"]="Ordem (as 12 primeiras): situação (atrasada, hoje, esta semana) combinada com impacto × urgência. Uma tarefa alta de hoje vem antes de uma baixa atrasada. As demais ficam na aba Tarefas."; h["A8"].font=F(size=9,color=LILAS)
hd=["#","Tarefa","Prazo","Situação","Prioridade","Responsável","Horas"]
for i,v in enumerate(hd,start=1):
    c=h.cell(row=9,column=i,value=v); c.font=F(bold=True,color=BRANCO,size=10); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center"); c.border=borda
TOP=12
for k in range(1,TOP+1):
    r=9+k
    h.cell(row=r,column=1,value=k)
    m=f'MATCH(LARGE(Tarefas!$M$4:$M$303,{k}),Tarefas!$M$4:$M$303,0)'
    g=f'LARGE(Tarefas!$M$4:$M$303,{k})>0'
    h.cell(row=r,column=2,value=f'=IFERROR(IF({g},INDEX(Tarefas!$B$4:$B$303,{m}),""),"")')
    h.cell(row=r,column=3,value=f'=IFERROR(IF({g},INDEX(Tarefas!$E$4:$E$303,{m}),""),"")')
    h.cell(row=r,column=4,value=f'=IFERROR(IF({g},INDEX(Tarefas!$L$4:$L$303,{m}),""),"")')
    h.cell(row=r,column=5,value=f'=IFERROR(IF({g},INDEX(Tarefas!$J$4:$J$303,{m}),""),"")')
    h.cell(row=r,column=6,value=f'=IFERROR(IF({g},INDEX(Tarefas!$D$4:$D$303,{m}),""),"")')
    h.cell(row=r,column=7,value=f'=IFERROR(IF({g},INDEX(Tarefas!$H$4:$H$303,{m}),""),"")')
    for col in range(1,8):
        c=h.cell(row=r,column=col); c.border=borda; c.font=F(size=10,color=TINTA)
        if col in (1,3,4,5,7): c.alignment=Alignment(horizontal="center")
    h.cell(row=r,column=3).number_format="dd/mm/yyyy"
rng=f"A10:G{9+TOP}"
h.conditional_formatting.add(rng, FormulaRule(formula=['$D10="Atrasada"'], fill=fill("FBE4E4"), font=Font(name="Arial",color="7A1F1F",size=10)))
h.conditional_formatting.add(rng, FormulaRule(formula=['$D10="Hoje"'], fill=fill("FFF1BF")))
# Carga dos próximos 7 dias
R0=9+TOP+3
h.cell(row=R0-1,column=1,value="Carga dos próximos 7 dias").font=F(bold=True,size=13,color=UVA)
hd2=["Dia","Data","Tarefas","Horas","% da capacidade","Barra"]
for i,v in enumerate(hd2,start=1):
    c=h.cell(row=R0,column=i,value=v); c.font=F(bold=True,color=BRANCO,size=10); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center"); c.border=borda
h.merge_cells(start_row=R0,start_column=6,end_row=R0,end_column=8)
for dI in range(7):
    r=R0+1+dI
    h.cell(row=r,column=2,value=f"=Config!$B$4+{dI}").number_format="dd/mm/yyyy"
    h.cell(row=r,column=1,value=f'=CHOOSE(WEEKDAY(B{r}),"dom","seg","ter","qua","qui","sex","sáb")')
    h.cell(row=r,column=3,value=f'=COUNTIFS(Tarefas!$E$4:$E$303,B{r},Tarefas!$I$4:$I$303,"<>Feito",Tarefas!$I$4:$I$303,"<>Cancelado",Tarefas!$B$4:$B$303,"<>")')
    h.cell(row=r,column=4,value=f'=SUMIFS(Tarefas!$H$4:$H$303,Tarefas!$E$4:$E$303,B{r},Tarefas!$I$4:$I$303,"<>Feito",Tarefas!$I$4:$I$303,"<>Cancelado")')
    h.cell(row=r,column=5,value=f'=IF(Config!$B$6>0,D{r}/Config!$B$6,0)'); h.cell(row=r,column=5).number_format="0%"
    h.cell(row=r,column=6,value=f'=REPT("█",ROUND(D{r},0))&IF(D{r}>Config!$B$6," ⚠ acima da capacidade","")')
    h.merge_cells(start_row=r,start_column=6,end_row=r,end_column=8)
    for col in range(1,9):
        c=h.cell(row=r,column=col); c.border=borda; c.font=F(size=10,color=TINTA)
        if col in (1,2,3,4,5): c.alignment=Alignment(horizontal="center")
    h.cell(row=r,column=6).font=F(size=10,color=LILAS)
h.conditional_formatting.add(f"A{R0+1}:H{R0+7}", FormulaRule(formula=[f'$E{R0+1}>1'], font=Font(name="Arial",color="7A1F1F",size=10,bold=True)))
h.cell(row=R0+8,column=1,value="Capacidade por dia definida em Config (padrão 6 h).").font=F(size=9,color=LILAS)
# Por responsável
R1=R0+11
h.cell(row=R1-1,column=1,value="Por responsável").font=F(bold=True,size=13,color=UVA)
hd3=["Responsável","Abertas","Atrasadas","Para hoje","Horas abertas"]
for i,v in enumerate(hd3,start=1):
    c=h.cell(row=R1,column=i,value=v); c.font=F(bold=True,color=BRANCO,size=10); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center"); c.border=borda
h.merge_cells(start_row=R1,start_column=1,end_row=R1,end_column=2)
for i in range(8):
    r=R1+1+i; src=f"Config!$B${9+i}"
    h.cell(row=r,column=1,value=f'=IF({src}="","",{src})')
    h.merge_cells(start_row=r,start_column=1,end_row=r,end_column=2)
    h.cell(row=r,column=2,value=None)
    h.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS(Tarefas!$D$4:$D$303,{src},Tarefas!$I$4:$I$303,"<>Feito",Tarefas!$I$4:$I$303,"<>Cancelado",Tarefas!$B$4:$B$303,"<>"))')
    h.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS(Tarefas!$D$4:$D$303,{src},Tarefas!$L$4:$L$303,"Atrasada"))')
    h.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS(Tarefas!$D$4:$D$303,{src},Tarefas!$L$4:$L$303,"Hoje"))')
    h.cell(row=r,column=6,value=f'=IF({src}="","",SUMIFS(Tarefas!$H$4:$H$303,Tarefas!$D$4:$D$303,{src},Tarefas!$I$4:$I$303,"<>Feito",Tarefas!$I$4:$I$303,"<>Cancelado"))')
    for col in range(1,7):
        c=h.cell(row=r,column=col); c.border=borda; c.font=F(size=10,color=TINTA)
        if col>2: c.alignment=Alignment(horizontal="center")
# ajuste: cabeçalho por responsável tem 5 rótulos em 6 colunas (A:B mesclado)
h.cell(row=R1,column=6,value="Horas abertas"); h.cell(row=R1,column=5,value="Para hoje"); h.cell(row=R1,column=4,value="Atrasadas"); h.cell(row=R1,column=3,value="Abertas"); h.cell(row=R1,column=2,value=None)
for col in range(1,7):
    c=h.cell(row=R1,column=col); c.font=F(bold=True,color=BRANCO,size=10); c.fill=fill(UVA); c.alignment=Alignment(horizontal="center"); c.border=borda
for col,w in zip("ABCDEFGH",(14,40,12,13,12,14,9,9)): h.column_dimensions[col].width=w
h.column_dimensions["B"].width=40
h.merge_cells("A2:H2"); h.merge_cells("A8:H8"); h.merge_cells(start_row=R0+8,start_column=1,end_row=R0+8,end_column=8)
h.sheet_view.showGridLines=False
h.freeze_panes="A4"

# ---------- Como usar ----------
u=wb.create_sheet("Como usar",0)
u["A1"]="Semana Organizada"; u["A1"].font=F(bold=True,size=20,color=UVA)
u["A2"]="Kit IA no Trabalho · Seu Sócio Gestor · versão 1.0 (setembro de 2026)"; u["A2"].font=F(size=10,color=LILAS)
linhas=[
("O que esta planilha faz","Lista as suas tarefas com prazo e prioridade e mostra, na aba Hoje, o que fazer primeiro, a carga dos próximos 7 dias e a situação de cada responsável."),
("Passo 1","Abra a aba Config. Confira a data de referência (fica em =HOJE()) e a capacidade de horas por dia. Ajuste a lista de responsáveis e de projetos, preenchendo de cima para baixo, sem pular linha."),
("Passo 2","Vá para a aba Tarefas. Apague os exemplos (linhas amarelas) e digite as suas tarefas: nome, projeto, responsável, prazo, impacto (1 a 3), urgência (1 a 3), horas e status."),
("Passo 3","Abra a aba Hoje. Ela é só leitura: prioridades, carga por dia e resumo por pessoa se atualizam sozinhos."),
("Passo 4","Todo dia, mude o status do que terminou para Feito. Uma vez por semana, revise prazos e horas."),
("Com a IA","Use o prompt \"Organizar 01\" da biblioteca do kit: cole uma lista bagunçada (e-mail, ata, áudio transcrito) e a IA devolve as tarefas no formato desta planilha, prontas para colar."),
("Legenda","Células amarelas: você preenche. Células brancas: calculadas, não mexa. Linhas vermelhas: atrasadas. Linhas amarelas na aba Hoje: vencem hoje."),
("Proteção","As fórmulas estão protegidas sem senha, só para evitar apagar sem querer. Para editar: Revisar > Desproteger planilha (Excel) ou Dados > Proteger intervalos (Google Sheets)."),
("Google Sheets","Faça upload do arquivo no Google Drive e abra com o Google Sheets. Tudo funciona: listas, cores e fórmulas."),
("Exemplos","Os dados de exemplo são fictícios (Ana, Bruno e Carla numa agência inventada). Os exemplos usam datas relativas a hoje (prazos como =HOJE()+2); apague-os e digite as suas."),
("Suporte","suporte@seusociogestor.com.br · resposta em até 5 dias úteis · reembolso em até 7 dias pelo mesmo canal."),
]
for i,(a,b) in enumerate(linhas,start=4):
    u.cell(row=i,column=1,value=a).font=F(bold=True,color=UVA); u.cell(row=i,column=2,value=b).font=F(color=TINTA)
    u.cell(row=i,column=2).alignment=Alignment(wrap_text=True,vertical="top"); u.cell(row=i,column=1).alignment=Alignment(vertical="top")
    u.row_dimensions[i].height=44
u.column_dimensions["A"].width=20; u.column_dimensions["B"].width=95; u.sheet_view.showGridLines=False
c=u.cell(row=16,column=1,value="Amostra"); c.fill=fill(AMARELO); c.border=borda; u.cell(row=16,column=2,value="Assim ficam as células que você preenche.").font=F(size=10,color=LILAS)

# ---------- proteção ----------
for ws in (t,cfg,h,u):
    ws.protection.sheet=True; ws.protection.formatColumns=False; ws.protection.formatRows=False
    ws.protection.sort=False; ws.protection.autoFilter=False; ws.protection.selectLockedCells=False
wb.properties.creator="Seu Sócio Gestor"; wb.properties.title="Semana Organizada · Kit IA no Trabalho"
wb.save("01-semana-organizada.xlsx"); print("salvo")
