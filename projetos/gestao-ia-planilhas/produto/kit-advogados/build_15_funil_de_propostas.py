#!/usr/bin/env python3
"""Planilha 15 do Kit de Gestão para Advogados: Funil de Propostas do escritório.
Adaptação do funil do Kit Completo (08). Gera 15-funil-de-propostas.xlsx (Como usar, Painel, Config, Propostas)."""
from ssg import *
import dados
from openpyxl.chart import BarChart, Reference

N=300; R0=5; RN=R0+N-1
NL=10; L0=18; L1=L0+NL-1           # listas da Config: linhas 18..27
E0=10; E1=15                       # etapas: linhas 10..15
ETAPAS=[("Contato",0.10),("Reunião feita",0.25),("Proposta enviada",0.50),("Negociação",0.75),("Fechada",1.0),("Perdida",0.0)]
def off(sheet,col,r0,r1): return f"=OFFSET({sheet}!${col}${r0},0,0,MAX(1,COUNTA({sheet}!${col}${r0}:${col}${r1})),1)"
def dstr(ref): return f'TEXT(DAY({ref}),"00")&"/"&TEXT(MONTH({ref}),"00")&"/"&YEAR({ref})'
NOME_ESC=f"{dados.ESCRITORIO} (exemplo fictício)"
HOJE="Config!$B$5"; META="Config!$B$6"; PAR="Config!$B$7"

wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. As probabilidades por etapa alimentam a previsão ponderada.",merge_to="J")
cfg["A4"]="Escritório"; cfg["B4"]=NOME_ESC
cfg["A5"]="Data de referência (hoje)"; cfg["B5"]="=TODAY()"
cfg["A6"]="Meta de honorários fechados no trimestre (R$)"; cfg["B6"]=dados.META_FECHADO_TRI
cfg["A7"]="Proposta parada há mais de (dias)"; cfg["B7"]=14
for r in range(4,8): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"],DATA); inp(cfg["B6"],BRL0); inp(cfg["B7"],center=True)
hdr(cfg,9,["Etapa","Probabilidade de fechar"])
for i,(e,pb) in enumerate(ETAPAS):
    r=E0+i; cfg.cell(row=r,column=1,value=e).font=F(size=10,color=TINTA); cfg.cell(row=r,column=1).border=borda
    inp(cfg.cell(row=r,column=2),PCT,center=True); cfg.cell(row=r,column=2).value=pb
cfg["A16"]="Etapas fixas: contato → reunião → proposta enviada → negociação → fechada ou perdida. Ajuste só as probabilidades, pela sua experiência."; nota(cfg["A16"])
for col,nome in ((1,"Áreas de atuação"),(3,"Origens do contato"),(5,"Motivos de perda"),(7,"Responsáveis"),(9,"Serviços mais comuns")): hdr(cfg,L0-1,[nome],start=col)
for r in range(L0,L1+1):
    for c in (1,3,5,7,9): inp(cfg.cell(row=r,column=c))
cfg.cell(row=L1+2,column=1,value="Preencha cada lista de cima para baixo, sem pular linha: as listas suspensas de Propostas param na primeira célula vazia. Até 10 itens por lista. Serviço é texto livre; a lista só sugere.").font=F(size=9,color=LILAS)
widths(cfg,(40,20,18,3,26,3,20,3,34,3)); cfg.sheet_view.showGridLines=False
AREAS_L=off("Config","A",L0,L1); ORIG_L=off("Config","C",L0,L1); MOT_L=off("Config","E",L0,L1); RESP_L=off("Config","G",L0,L1); SERV_L=off("Config","I",L0,L1)

# ---------- Propostas ----------
pr=wb.create_sheet("Propostas")
titulo(pr,"Propostas","Uma linha por proposta de honorários. Atualize a etapa conforme avança; ao fechar, marque Fechada ou Perdida, a data e, se perdida, o motivo.",merge_to="Q")
hdr(pr,4,["Cliente","Área","Serviço","Origem","Responsável","Valor (R$)","Etapa","Data de entrada","Última movimentação","Fechamento previsto","Data de fechamento","Motivo (se perdida)","Probabilidade","Valor ponderado","Dias parada","Dias até fechar","Situação"])
for r in range(R0,RN+1):
    for c in range(1,13): inp(pr.cell(row=r,column=c))
    for c in (2,4,5,7,8,9,10,11): pr.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    for c in (8,9,10,11): pr.cell(row=r,column=c).number_format=DATA
    pr.cell(row=r,column=6).number_format=BRL0
    pr.cell(row=r,column=13,value=f'=IF(G{r}="","",IFERROR(INDEX(Config!$B${E0}:$B${E1},MATCH(G{r},Config!$A${E0}:$A${E1},0)),0))'); calc(pr.cell(row=r,column=13),PCT)
    pr.cell(row=r,column=14,value=f'=IF(OR(G{r}="",F{r}=""),"",F{r}*M{r})'); calc(pr.cell(row=r,column=14),BRL0)
    pr.cell(row=r,column=15,value=f'=IF(OR(G{r}="",G{r}="Fechada",G{r}="Perdida",AND(H{r}="",I{r}="")),"",{HOJE}-IF(I{r}="",H{r},I{r}))'); calc(pr.cell(row=r,column=15),"0")
    pr.cell(row=r,column=16,value=f'=IF(AND(G{r}="Fechada",K{r}<>"",H{r}<>""),K{r}-H{r},"")'); calc(pr.cell(row=r,column=16),"0")
    pr.cell(row=r,column=17,value=f'=IF(G{r}="","",IF(G{r}="Fechada","Fechada",IF(G{r}="Perdida","Perdida",IF(AND(J{r}<>"",J{r}<{HOJE}),"Previsão vencida",IF(AND(O{r}<>"",O{r}>{PAR}),"Parada","Ativa")))))'); calc(pr.cell(row=r,column=17))
    pr.cell(row=r,column=18,value=f'=IF(OR(G{r}="",Q{r}="Fechada",Q{r}="Perdida"),0,IF(Q{r}="Previsão vencida",3000,IF(Q{r}="Parada",2000,1000))+MIN(N(O{r}),500)+N(F{r})/1000000-ROW()/100000)'); pr.cell(row=r,column=18).font=F(color=CINZA,size=9)
pr.column_dimensions["R"].hidden=True
dvs=[lista(AREAS_L), lista(SERV_L,strict=False), lista(ORIG_L,strict=False), lista(RESP_L), lista(f"=Config!$A${E0}:$A${E1}"), lista(MOT_L,strict=False),
     DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True), DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True)]
for dv,rng in zip(dvs,[f"B{R0}:B{RN}",f"C{R0}:C{RN}",f"D{R0}:D{RN}",f"E{R0}:E{RN}",f"G{R0}:G{RN}",f"L{R0}:L{RN}",f"H{R0}:K{RN}",f"F{R0}:F{RN}"]): dv.add(rng); pr.add_data_validation(dv)
pr.conditional_formatting.add(f"A{R0}:Q{RN}", FormulaRule(formula=[f'$Q{R0}="Parada"'], fill=fill("FFF4CC")))
pr.conditional_formatting.add(f"A{R0}:Q{RN}", FormulaRule(formula=[f'$Q{R0}="Previsão vencida"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
pr.conditional_formatting.add(f"A{R0}:Q{RN}", FormulaRule(formula=[f'$Q{R0}="Fechada"'], font=F(color=VERDE_T,size=10,bold=True)))
pr.conditional_formatting.add(f"A{R0}:Q{RN}", FormulaRule(formula=[f'$Q{R0}="Perdida"'], font=F(color="8A86A0",size=10)))
pr.conditional_formatting.add(f"L{R0}:L{RN}", FormulaRule(formula=[f'AND($G{R0}="Perdida",$L{R0}="")'], fill=fill(VERM)))
pr.cell(row=RN+2,column=1,value="Amarelo: parada há mais dias que o limite da Config. Vermelho: fechamento previsto já passou. Verde: fechada. Cinza: perdida. Motivo em vermelho: perdida sem motivo (preencha, é o que ensina).").font=F(size=9,color=LILAS)
widths(pr,(26,14,30,13,14,13,17,12,13,13,13,22,11,13,9,9,16)); pr.freeze_panes="C5"; pr.sheet_view.showGridLines=False; pr.auto_filter.ref=f"A4:Q{RN}"

# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,f'=Config!$B$4&" · Funil de propostas · "&{dstr(HOJE)}',"Nada para digitar aqui: tudo vem de Propostas e Config.",merge_to="L")
p.merge_cells("A1:L1")
PA=f"Propostas!$A${R0}:$A${RN}"; PB=f"Propostas!$B${R0}:$B${RN}"; PC=f"Propostas!$C${R0}:$C${RN}"; PD=f"Propostas!$D${R0}:$D${RN}"; PE_=f"Propostas!$E${R0}:$E${RN}"
PF=f"Propostas!$F${R0}:$F${RN}"; PG=f"Propostas!$G${R0}:$G${RN}"; PK=f"Propostas!$K${R0}:$K${RN}"; PL=f"Propostas!$L${R0}:$L${RN}"; PN=f"Propostas!$N${R0}:$N${RN}"
PO=f"Propostas!$O${R0}:$O${RN}"; PP=f"Propostas!$P${R0}:$P${RN}"; PQ=f"Propostas!$Q${R0}:$Q${RN}"; PR_=f"Propostas!$R${R0}:$R${RN}"
ABERTA=f'{PG},"<>Fechada",{PG},"<>Perdida",{PG},"<>"'
TRI=f'DATE(YEAR({HOJE}),3*INT((MONTH({HOJE})-1)/3)+1,1)'
kpi(p,4,1,"Em aberto (R$)",f'=SUMIFS({PF},{ABERTA})',LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Previsão ponderada",f'=SUMIFS({PN},{ABERTA})',SOL,UVA,fmt=BRL0)
kpi(p,4,5,"Fechado no trimestre",f'=SUMIFS({PF},{PG},"Fechada",{PK},">="&{TRI})',VERDE,VERDE_T,fmt=BRL0)
kpi(p,4,7,"% da meta",f'=IFERROR(E5/{META},0)',VERDE,VERDE_T,fmt=PCT)
kpi(p,4,9,"Taxa de fechamento",f'=IFERROR(COUNTIFS({PG},"Fechada")/(COUNTIFS({PG},"Fechada")+COUNTIFS({PG},"Perdida")),0)',LAVANDA,UVA,fmt=PCT)
kpi(p,4,11,"Dias até fechar (média)",f'=IFERROR(AVERAGEIFS({PP},{PG},"Fechada"),0)',LAVANDA,UVA,fmt="0")
p["A7"]="Taxa de fechamento = fechadas ÷ (fechadas + perdidas). Dias até fechar = da data de entrada à data de fechamento, média das fechadas."; nota(p["A7"]); p.merge_cells("A7:L7")
p["A9"]="Funil por etapa"; p["A9"].font=F(bold=True,size=13,color=UVA)
hdr(p,10,["Etapa","Propostas","Valor (R$)","Ponderado (R$)","Taxa de passagem","Barra"]); p.merge_cells("F10:H10")
for i,(e,pb) in enumerate(ETAPAS[:4]):
    r=11+i
    p.cell(row=r,column=1,value=f'=Config!$A${E0+i}'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=COUNTIFS({PG},A{r})'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=SUMIFS({PF},{PG},A{r})'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f'=SUMIFS({PN},{PG},A{r})'); calc(p.cell(row=r,column=4),BRL0)
    adiante="+".join([f'COUNTIFS({PG},Config!$A${E0+j})' for j in range(i+1,6)])
    p.cell(row=r,column=5,value=f'=IFERROR(({adiante})/(B{r}+{adiante}),0)'); calc(p.cell(row=r,column=5),PCT)
    p.cell(row=r,column=6,value=f'=REPT("█",ROUND(IFERROR(C{r}/MAX($C$11:$C$14),0)*30,0))'); p.cell(row=r,column=6).font=F(size=10,color=LILAS); p.cell(row=r,column=6).border=borda; p.merge_cells(start_row=r,start_column=6,end_row=r,end_column=8)
p.cell(row=15,column=1,value="Fechadas (total)"); p.cell(row=15,column=2,value=f'=COUNTIFS({PG},"Fechada")'); p.cell(row=15,column=3,value=f'=SUMIFS({PF},{PG},"Fechada")')
p.cell(row=16,column=1,value="Perdidas (total)"); p.cell(row=16,column=2,value=f'=COUNTIFS({PG},"Perdida")'); p.cell(row=16,column=3,value=f'=SUMIFS({PF},{PG},"Perdida")')
p.cell(row=17,column=1,value="Honorário médio das fechadas"); p.cell(row=17,column=2,value='=IFERROR(C15/B15,0)'); p.cell(row=17,column=2).number_format=BRL0
for r in (15,16,17): calc(p.cell(row=r,column=1),center=False); calc(p.cell(row=r,column=2)); calc(p.cell(row=r,column=3),BRL0)
p.cell(row=17,column=3).value=None
p["A18"]="Taxa de passagem: de tudo o que chegou a uma etapa, quanto já seguiu adiante (inclui fechadas e perdidas)."; nota(p["A18"])
p["A20"]="O que mexer primeiro"; p["A20"].font=F(bold=True,size=13,color=UVA)
p["A21"]="Propostas abertas com previsão vencida ou paradas há mais tempo; as de maior valor primeiro."; nota(p["A21"]); p.merge_cells("A21:L21")
hdr(p,22,["#","Cliente","Serviço","Etapa","Valor (R$)","Dias parada","Situação","Responsável"])
TOP=8
for k in range(1,TOP+1):
    r=22+k; m=f'MATCH(LARGE({PR_},{k}),{PR_},0)'; g=f'LARGE({PR_},{k})>0'
    p.cell(row=r,column=1,value=k); calc(p.cell(row=r,column=1))
    for col,src in zip((2,3,4,5,6,7,8),("A","C","G","F","O","Q","E")):
        p.cell(row=r,column=col,value=f'=IFERROR(IF({g},INDEX(Propostas!${src}${R0}:${src}${RN},{m}),""),"")'); calc(p.cell(row=r,column=col),center=(col not in (2,3)))
    p.cell(row=r,column=5).number_format=BRL0; p.cell(row=r,column=6).number_format="0"
p.conditional_formatting.add(f"A23:H{22+TOP}", FormulaRule(formula=['$G23="Previsão vencida"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
p.conditional_formatting.add(f"A23:H{22+TOP}", FormulaRule(formula=['$G23="Parada"'], fill=fill("FFF4CC")))
ra=22+TOP+2
p.cell(row=ra,column=1,value="Por área").font=F(bold=True,size=13,color=UVA)
hdr(p,ra+1,["Área","Propostas","Fechadas","Perdidas","Taxa de fechamento","Valor fechado (R$)","Em aberto (R$)"])
for i in range(NL):
    r=ra+2+i; src=f"Config!$A${L0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({PB},{src}))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",COUNTIFS({PB},{src},{PG},"Fechada"))'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS({PB},{src},{PG},"Perdida"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",IFERROR(C{r}/(C{r}+D{r}),0))'); calc(p.cell(row=r,column=5),PCT)
    p.cell(row=r,column=6,value=f'=IF({src}="","",SUMIFS({PF},{PB},{src},{PG},"Fechada"))'); calc(p.cell(row=r,column=6),BRL0)
    p.cell(row=r,column=7,value=f'=IF({src}="","",SUMIFS({PF},{PB},{src},{ABERTA}))'); calc(p.cell(row=r,column=7),BRL0)
rm=ra+2+NL+1
p.cell(row=rm,column=1,value="Motivos de perda").font=F(bold=True,size=13,color=UVA)
hdr(p,rm+1,["Motivo","Perdidas","Valor perdido (R$)","% das perdidas"])
for i in range(NL):
    r=rm+2+i; src=f"Config!$E${L0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({PL},{src},{PG},"Perdida"))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({PF},{PL},{src},{PG},"Perdida"))'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f'=IF({src}="","",IFERROR(B{r}/$B$16,0))'); calc(p.cell(row=r,column=4),PCT)
hdr(p,rm+1,["Origem","Propostas","Fechadas","Taxa de fechamento","Valor fechado (R$)"],start=6)
for i in range(NL):
    r=rm+2+i; src=f"Config!$C${L0+i}"
    p.cell(row=r,column=6,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=6),center=False)
    p.cell(row=r,column=7,value=f'=IF({src}="","",COUNTIFS({PD},{src}))'); calc(p.cell(row=r,column=7))
    p.cell(row=r,column=8,value=f'=IF({src}="","",COUNTIFS({PD},{src},{PG},"Fechada"))'); calc(p.cell(row=r,column=8))
    p.cell(row=r,column=9,value=f'=IF({src}="","",IFERROR(H{r}/(H{r}+COUNTIFS({PD},{src},{PG},"Perdida")),0))'); calc(p.cell(row=r,column=9),PCT)
    p.cell(row=r,column=10,value=f'=IF({src}="","",SUMIFS({PF},{PD},{src},{PG},"Fechada"))'); calc(p.cell(row=r,column=10),BRL0)
p.cell(row=rm+2+NL+1,column=1,value="Fonte: aba Propostas. Uma proposta perdida com o motivo anotado vale mais que três sem: é o que mostra o que ajustar no preço, no prazo ou na abordagem.").font=F(size=9,color=LILAS)
bc=BarChart(); bc.type="bar"; bc.height=6; bc.width=13; bc.title="Valor por etapa (R$)"; bc.style=2
bc.add_data(Reference(p,min_col=3,min_row=10,max_row=14),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=11,max_row=14))
bc.series[0].graphicalProperties.solidFill="3B1F5E"; bc.legend=None; bc.x_axis.majorGridlines=None
p.add_chart(bc,"J9")
widths(p,(26,26,30,16,15,16,16,14,14,16,12,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False

# ---------- Exemplo (Ferraz & Lima) ----------
for i,v in enumerate(dados.AREAS): cfg.cell(row=L0+i,column=1,value=v)
for i,v in enumerate(["Indicação de cliente","Site e Google","Instagram","Cliente antigo","Parceria (contador, imobiliária)","Evento ou palestra"]): cfg.cell(row=L0+i,column=3,value=v)
for i,v in enumerate(["Preço","Fechou com outro escritório","Desistiu da demanda","Sem resposta","Fora da área de atuação","Prazo de atendimento"]): cfg.cell(row=L0+i,column=5,value=v)
for i,(nome,_,_,_) in enumerate(dados.PESSOAS[:2]): cfg.cell(row=L0+i,column=7,value=nome)
for i,v in enumerate(["Assessoria mensal (12 meses)","Ação trabalhista","Defesa em reclamação trabalhista","Revisão de benefício","Planejamento previdenciário","Cobrança judicial","Contratos e consultoria","Contratos com convênios","Divórcio e partilha","Inventário"]): cfg.cell(row=L0+i,column=9,value=v)
# exemplo: o funil único do kit (dados.PROPOSTAS). As 10 propostas mais recentes já enviadas aparecem também no Registro da 07,
# e as fechadas em 2026 são casos da carteira (13), abertos no mês do fechamento. Datas abertas em dias relativos a hoje.
def _dt(x): return None if x is None else (dados.prazo_formula(x) if isinstance(x,int) else x)
ex=[(p["cliente"],p["area"],p["servico"],p["origem"],p["responsavel"],p["valor"],p["etapa"],p["entrada"],_dt(p["ultima_mov"]),_dt(p["fech_previsto"]),p["fechamento"],p["motivo"]) for p in dados.PROPOSTAS]
for i,row in enumerate(ex):
    for c,v in enumerate(row,start=1):
        if v is not None and v!="": pr.cell(row=R0+i,column=c,value=v)
print(len(ex),"propostas no exemplo")

como_usar(wb,"Funil de Propostas",[
 ("O que esta planilha faz","Você registra cada proposta de honorários com valor e etapa; ela calcula a previsão ponderada, mostra o funil por etapa, o que está parado ou com previsão vencida, a taxa de fechamento por área e origem e por que o escritório perde propostas."),
 ("Passo 1","Em Config, preencha a meta de honorários fechados no trimestre, o limite de \"parada\" (14 dias é um bom padrão), as áreas, origens, motivos de perda, responsáveis e serviços. Ajuste as probabilidades por etapa se a sua experiência for diferente."),
 ("Passo 2","Em Propostas, uma linha por proposta: cliente, área, serviço, origem, responsável, valor, etapa e datas. Sempre que falar com o cliente, atualize a última movimentação."),
 ("Passo 3","Ao fechar, mude a etapa para Fechada ou Perdida e preencha a data. Se perdida, anote o motivo: é a parte mais valiosa da planilha."),
 ("Passo 4","Em Painel, veja o funil, a previsão ponderada, a lista \"O que mexer primeiro\", a taxa de fechamento por área e origem e os motivos de perda."),
 ("Rotina","Sexta-feira, 10 minutos: atualizar etapas e datas, retomar as paradas. Dia 1 do mês: comparar o fechado com a meta e olhar os motivos de perda."),
 ("Com a IA","Copie \"Motivos de perda\" e use o prompt \"Clientes 06 · Por que as propostas não fecham\" da biblioteca; para uma proposta parada, \"Honorários 02 · Revisar a proposta pela margem\" antes de retomar o contato. A proposta fechada vira caso na planilha 13 (Carteira)."),
 ("Exemplo","O funil traz 20 propostas de junho a setembro de 2026: as 7 fechadas viraram casos na planilha 13 (abertura no mês do fechamento) e as 10 mais recentes já enviadas são as mesmas do Registro da planilha 07."),
])
proteger(wb); salvar(wb,"15-funil-de-propostas.xlsx","Funil de Propostas · Kit de Gestão para Advogados")
