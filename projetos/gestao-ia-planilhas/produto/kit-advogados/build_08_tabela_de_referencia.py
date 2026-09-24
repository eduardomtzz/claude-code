#!/usr/bin/env python3
"""Planilha 8 do Kit de Gestão para Advogados: Tabela de referência de honorários. Gera 08-tabela-de-referencia.xlsx"""
from ssg import *
from openpyxl.chart import BarChart, Reference
import dados
NREF=40; NC=200; T0=5; TN=T0+NREF-1; C0=5; CN=C0+NC-1
TIPOS=["Consultoria pontual","Contrato ou documento","Processo completo","Recurso","Acordo e negociação"]
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. O custo-hora vem da planilha 05; margens mínima e alvo definem a faixa de cada serviço.",merge_to="H")
campos=[("Nome do escritório",f"{dados.ESCRITORIO} (exemplo fictício)",None),("Mês de referência","Setembro de 2026",None),("Data de referência",dados.HOJE,DATA),
 ("Custo-hora do escritório (R$)",dados.CUSTO_HORA,BRL),("Impostos e taxas sobre o que entra (%)",dados.ALIQ,PCT),("Margem mínima sobre o preço (%)",dados.MARGEM,PCT),("Margem alvo sobre o preço (%)",dados.MARGEM_ALVO,PCT),("Folga para horas não previstas (%)",dados.FOLGA_HORAS,PCT)]
for i,(a,v,fmt) in enumerate(campos):
    r=4+i; cfg.cell(row=r,column=1,value=a); rotulo(cfg.cell(row=r,column=1)); cfg.cell(row=r,column=2,value=v)
    if r==6: calc(cfg.cell(row=r,column=2),fmt)
    else: inp(cfg.cell(row=r,column=2),fmt,center=fmt is not None)
# Auditoria final-2 (G01/G02): mesma regra da 06 dos Médicos. Custo-hora em branco não é hora
# mínima zero; impostos, margens e folga fora do domínio (texto, branco, negativo, mínima acima da
# alvo, soma de 100 %) viram "margens inválidas (Config)". Todas as saídas da tabela dependem de
# B12/B13 e só calculam quando elas são números.
_OK='IF(AND(ISNUMBER(B8),ISNUMBER(B9),ISNUMBER(B10),ISNUMBER(B11)),AND(B8>=0,B8<1,B9>=0,B9<=B10,B10<1,B8+B10<1,B11>=0),FALSE)'
cfg["A12"]="Hora mínima com folga (20 % de horas não previstas) (R$)"; cfg["B12"]=f'=IF(NOT(ISNUMBER(B7)),"falta o custo-hora",IF({_OK},B7*(1+B11)/(1-B8-B9),"margens inválidas (Config)"))'
cfg["A13"]="Hora alvo com folga (R$)"; cfg["B13"]=f'=IF(NOT(ISNUMBER(B7)),"falta o custo-hora",IF({_OK},B7*(1+B11)/(1-B8-B10),"margens inválidas (Config)"))'
for _c,_f,_m in (("B8",'=IF(ISNUMBER(B8),AND(B8>=0,B8<1,B8+N(B10)<1),FALSE)',"Impostos entre 0 % e 99 %, e impostos + margem alvo abaixo de 100 %."),
                 ("B9",'=IF(ISNUMBER(B9),AND(B9>=0,B9<=N(B10),N(B8)+B9<1),FALSE)',"Margem mínima entre 0 % e a margem alvo, e impostos + margem abaixo de 100 %."),
                 ("B10",'=IF(ISNUMBER(B10),AND(B10>=N(B9),B10<1,N(B8)+B10<1),FALSE)',"Margem alvo entre a margem mínima e 99 %, e impostos + margem alvo abaixo de 100 %."),
                 ("B11",'=IF(ISNUMBER(B11),AND(B11>=0),FALSE)',"Folga de 0 % para cima.")):
    _dv=DataValidation(type="custom",formula1=_f,allow_blank=False,showErrorMessage=True,errorTitle="Percentual",error=_m); _dv.add(_c); cfg.add_data_validation(_dv)
for r in (12,13): rotulo(cfg.cell(row=r,column=1)); calc(cfg.cell(row=r,column=2),BRL); cfg.cell(row=r,column=2).font=F(bold=True,color=UVA,size=10)
cfg["C7"]="Copie do Painel da planilha 05 (\"Custo-hora do escritório\")."; cfg["C8"]="Exemplo; confira com o contador."
cfg["C9"]="Abaixo disso o caso não vale a pena. Define o piso da faixa. A mesma margem desejada da planilha 05."; cfg["C10"]="A margem que você quer de verdade. Define o teto da faixa."
cfg["C11"]="Caso costuma consumir mais horas que o estimado; a folga protege a faixa. Igual à folga de horas da planilha 06."
cfg["C12"]="Custo-hora × (1 + folga) ÷ (1 − impostos − margem mínima). É a hora mínima da planilha 05 (R$ 106,57 → R$ 110) com 20 % de folga para horas não previstas: por isso é maior. A tabela usa esta, mais protegida, porque a faixa é fixada antes de conhecer o caso."; cfg["C13"]="Custo-hora × (1 + folga) ÷ (1 − impostos − margem alvo)."
for r in range(7,14): nota(cfg.cell(row=r,column=3))
cfg["A14"]="Listas (preencha de cima para baixo, sem pular linha)"; rotulo(cfg["A14"])
listas={5:("Áreas",dados.AREAS),7:("Tipos de serviço",TIPOS),9:("Modalidades",dados.TIPOS_HON)}
for col,(nome,vals) in listas.items():
    cfg.cell(row=15,column=col,value=nome); rotulo(cfg.cell(row=15,column=col))
    for i in range(20): inp(cfg.cell(row=16+i,column=col))
    for i,v in enumerate(vals): cfg.cell(row=16+i,column=col,value=v)
def LST(col): return f"=OFFSET(Config!${col}$16,0,0,MAX(1,COUNTA(Config!${col}$16:${col}$35)),1)"
widths(cfg,(40,16,60,3,18,3,26,3,14)); cfg.sheet_view.showGridLines=False
HMIN="Config!$B$12"; HALVO="Config!$B$13"
# ---------- Nossos casos ----------
k=wb.create_sheet("Nossos casos")
titulo(k,"O que cobramos hoje","Uma linha por caso (copie da planilha 13 · Carteira, aba Casos: a 13 é a fonte; horas estimadas da 16). O valor por hora é comparado com a hora mínima com folga e a hora alvo de Config.",merge_to="L")
hdr(k,4,["Nº do processo ou caso","Cliente","Área","Modalidade","Fase","Valor contratado (R$)","Horas estimadas","Valor por hora (R$)","Contra a hora mínima com folga","Situação","Falta até o mínimo (R$)","Ordem"],height=32)
for r in range(C0,CN+1):
    for c in (1,2,3,4,5,6,7): inp(k.cell(row=r,column=c))
    for c in (3,4,5,7): k.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    k.cell(row=r,column=6).number_format=BRL0; k.cell(row=r,column=7).number_format="0"
    # Auditoria final-4 (F4-G01): valor ou horas em texto não viram #VALUE! nem somem das contagens
    k.cell(row=r,column=8,value=f'=IF(OR(A{r}="",G{r}="",F{r}=""),"",IF(OR(NOT(ISNUMBER(F{r})),NOT(ISNUMBER(G{r}))),"valor ou horas inválidos",IF(G{r}=0,"",F{r}/G{r})))'); calc(k.cell(row=r,column=8),BRL)
    k.cell(row=r,column=9,value=f'=IF(OR(NOT(ISNUMBER(H{r})),NOT(ISNUMBER({HMIN}))),"",IF({HMIN}=0,"sem base (mínimo zero)",H{r}/{HMIN}-1))'); calc(k.cell(row=r,column=9),"+0%;-0%;0%")
    k.cell(row=r,column=10,value=f'=IF(H{r}="","",IF(NOT(ISNUMBER(H{r})),H{r},IF(NOT(ISNUMBER({HMIN})),{HMIN},IF(NOT(ISNUMBER({HALVO})),{HALVO},IF(H{r}<{HMIN},"Abaixo do mínimo",IF(H{r}<{HALVO},"Na faixa","Acima do alvo"))))))'); calc(k.cell(row=r,column=10))
    k.cell(row=r,column=11,value=f'=IF(OR(NOT(ISNUMBER(H{r})),NOT(ISNUMBER({HMIN}))),"",MAX(0,{HMIN}*G{r}-F{r}))'); calc(k.cell(row=r,column=11),BRL0)
    k.cell(row=r,column=12,value=f'=IF(K{r}="","",K{r}+ROW()/1000000)'); calc(k.cell(row=r,column=12),"0.00"); k.cell(row=r,column=12).font=F(size=9,color=CINZA)
for dv,rng in ((lista(LST("E"),strict=True),f"C{C0}:C{CN}"),(lista(LST("I")),f"D{C0}:D{CN}")): dv.add(rng); k.add_data_validation(dv)
k.conditional_formatting.add(f"J{C0}:J{CN}", FormulaRule(formula=[f'$J{C0}="Abaixo do mínimo"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
k.conditional_formatting.add(f"J{C0}:J{CN}", FormulaRule(formula=[f'$J{C0}="Na faixa"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
k.conditional_formatting.add(f"J{C0}:J{CN}", FormulaRule(formula=[f'$J{C0}="Acima do alvo"'], fill=fill(LAVANDA)))
k.cell(row=CN+2,column=1,value="Em êxito e misto, o valor contratado é o esperado (só entra no fim). \"Falta até o mínimo\" = hora mínima × horas estimadas − valor contratado. \"Ordem\" é coluna auxiliar da lista do Painel.").font=F(size=9,color=LILAS)
widths(k,(26,26,14,12,12,16,10,14,12,18,16,10)); k.column_dimensions["L"].hidden=True; k.freeze_panes=f"A{C0}"; k.sheet_view.showGridLines=False; k.auto_filter.ref=f"A4:L{CN}"
KF=f"'Nossos casos'!$F${C0}:$F${CN}"; KG=f"'Nossos casos'!$G${C0}:$G${CN}"; KH=f"'Nossos casos'!$H${C0}:$H${CN}"; KJ=f"'Nossos casos'!$J${C0}:$J${CN}"
KK=f"'Nossos casos'!$K${C0}:$K${CN}"; KL=f"'Nossos casos'!$L${C0}:$L${CN}"; KC=f"'Nossos casos'!$C${C0}:$C${CN}"; KA=f"'Nossos casos'!$A${C0}:$A${CN}"
# ---------- Referência ----------
p=wb.create_sheet("Referência",0)
titulo(p,'=Config!$B$4&" · Tabela de referência de honorários · "&Config!$B$5',"Tabela interna: faixa de valor por área e tipo de serviço, calculada do custo-hora. Amarelo: horas típicas e modalidade. Abaixo, o que cobramos hoje contra a referência.",merge_to="K")
kpi(p,4,1,"Hora mínima com folga",f"={HMIN}",LAVANDA,UVA,fmt=BRL)
kpi(p,4,3,"Hora alvo com folga",f"={HALVO}",SOL,UVA,fmt=BRL)
KINV=f'COUNTIF({KH},"valor ou horas inválidos")'
kpi(p,4,5,"Casos abaixo do mínimo",f'=IF(NOT(ISNUMBER({HMIN})),{HMIN},IF({KINV}>0,{KINV}&" caso(s) com valor ou horas inválidos",COUNTIF({KJ},"Abaixo do mínimo")&" de "&(COUNTIF({KJ},"Abaixo do mínimo")+COUNTIF({KJ},"Na faixa")+COUNTIF({KJ},"Acima do alvo"))))',VERM,VERM_T,fmt="@")
kpi(p,4,7,"Falta até o mínimo",f'=IF(NOT(ISNUMBER({HMIN})),{HMIN},IF({KINV}>0,{KINV}&" caso(s) com valor ou horas inválidos",SUM({KK})))',VERM,VERM_T,fmt=BRL0)
kpi(p,4,9,"Valor por hora médio",f'=IFERROR(SUM({KF})/SUM({KG}),0)',VERDE,VERDE_T,fmt=BRL)
p["A7"]="Faixa de referência por área e tipo de serviço"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Área","Tipo de serviço","Horas típicas · de","Horas típicas · até","Modalidade recomendada","Mínimo (R$)","Máximo (R$)","Ponto médio (R$)","Como usar a faixa"],height=32)
T0=9; TN=T0+NREF-1
for r in range(T0,TN+1):
    inp(p.cell(row=r,column=1)); inp(p.cell(row=r,column=2)); inp(p.cell(row=r,column=3),"0",center=True); inp(p.cell(row=r,column=4),"0",center=True); inp(p.cell(row=r,column=5),center=True)
    p.cell(row=r,column=6,value=f'=IF(OR(A{r}="",C{r}=""),"",IF(NOT(ISNUMBER(C{r})),"horas inválidas",IF(ISNUMBER({HMIN}),C{r}*{HMIN},{HMIN})))'); calc(p.cell(row=r,column=6),BRL0)
    p.cell(row=r,column=7,value=f'=IF(OR(A{r}="",D{r}=""),"",IF(NOT(ISNUMBER(D{r})),"horas inválidas",IF(ISNUMBER({HALVO}),D{r}*{HALVO},{HALVO})))'); calc(p.cell(row=r,column=7),BRL0)
    p.cell(row=r,column=8,value=f'=IF(OR(NOT(ISNUMBER(F{r})),NOT(ISNUMBER(G{r}))),"",(F{r}+G{r})/2)'); calc(p.cell(row=r,column=8),BRL0)
    p.cell(row=r,column=9,value=f'=IF(A{r}="","",IF(E{r}="Hora","Cobre a hora entre a mínima e a alvo; a faixa é o total esperado",IF(E{r}="Êxito","Percentual que, na chance esperada, fique dentro da faixa",IF(E{r}="Misto","Entrada perto do mínimo; o êxito leva ao máximo","Caso simples perto do mínimo; complexo perto do máximo"))))'); calc(p.cell(row=r,column=9),center=False); nota(p.cell(row=r,column=9))
for dv,rng in ((lista(LST("E")),f"A{T0}:A{TN}"),(lista(LST("G")),f"B{T0}:B{TN}"),(lista(LST("I")),f"E{T0}:E{TN}")): dv.add(rng); p.add_data_validation(dv)
p.cell(row=TN+1,column=1,value="Mínimo = horas de × hora mínima com folga. Máximo = horas até × hora alvo com folga (as duas incluem os 20 % de horas não previstas de Config; por isso a hora mínima daqui é maior que a da planilha 05). Abaixo do mínimo, o caso paga o custo mas não a margem que o escritório precisa.").font=F(size=9,color=LILAS)
# comparação por área
A0=TN+4
p.cell(row=A0,column=1,value="O que cobramos hoje, por área").font=F(bold=True,size=13,color=UVA)
hdr(p,A0+1,["Área","Casos","Valor contratado (R$)","Horas estimadas","Valor por hora (R$)","Contra a hora mínima","Abaixo do mínimo","Falta até o mínimo (R$)"],height=32)
for i in range(20):
    r=A0+2+i; src=f"Config!$E${16+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({KC},{src},{KJ},"<>"))'); calc(p.cell(row=r,column=2),"0")
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({KF},{KC},{src}))'); calc(p.cell(row=r,column=3),BRL0)
    p.cell(row=r,column=4,value=f'=IF({src}="","",SUMIFS({KG},{KC},{src}))'); calc(p.cell(row=r,column=4),"0")
    p.cell(row=r,column=5,value=f'=IF(OR({src}="",D{r}=0),"",C{r}/D{r})'); calc(p.cell(row=r,column=5),BRL)
    p.cell(row=r,column=6,value=f'=IF(OR(E{r}="",NOT(ISNUMBER({HMIN}))),"",IF({HMIN}=0,"sem base (mínimo zero)",E{r}/{HMIN}-1))'); calc(p.cell(row=r,column=6),"+0%;-0%;0%")
    p.cell(row=r,column=7,value=f'=IF(OR({src}="",NOT(ISNUMBER({HMIN}))),"",COUNTIFS({KC},{src},{KJ},"Abaixo do mínimo"))'); calc(p.cell(row=r,column=7),"0")
    p.cell(row=r,column=8,value=f'=IF(OR({src}="",NOT(ISNUMBER({HMIN}))),"",SUMIFS({KK},{KC},{src}))'); calc(p.cell(row=r,column=8),BRL0)
AN=A0+21
p.conditional_formatting.add(f"F{A0+2}:F{AN}", FormulaRule(formula=[f'AND(ISNUMBER(F{A0+2}),F{A0+2}<0)'], font=F(color="C8402E",size=10,bold=True)))
p.conditional_formatting.add(f"G{A0+2}:G{AN}", FormulaRule(formula=[f'AND(ISNUMBER(G{A0+2}),G{A0+2}>0)'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
# casos mais abaixo do mínimo
B0=AN+3
p.cell(row=B0,column=1,value="Os 8 casos mais abaixo do mínimo").font=F(bold=True,size=13,color=UVA)
hdr(p,B0+1,["Nº do processo ou caso","Cliente","Área","Modalidade","Valor contratado (R$)","Horas estimadas","Valor por hora (R$)","Falta até o mínimo (R$)"],height=32)
for i in range(1,9):
    r=B0+1+i
    p.cell(row=r,column=9,value=f'=IFERROR(IF(LARGE({KL},{i})<1,"",MATCH(LARGE({KL},{i}),{KL},0)),"")'); calc(p.cell(row=r,column=9),"0"); p.cell(row=r,column=9).font=F(size=9,color=CINZA)
    for c,(colk,fmt) in enumerate((("A",None),("B",None),("C",None),("D",None),("F",BRL0),("G","0"),("H",BRL),("K",BRL0)),start=1):
        p.cell(row=r,column=c,value=f'=IF($I{r}="","",INDEX(\'Nossos casos\'!${colk}${C0}:${colk}${CN},$I{r}))'); calc(p.cell(row=r,column=c),fmt,center=c not in (1,2))
p.cell(row=B0+1,column=9,value="Linha"); p.cell(row=B0+1,column=9).font=F(size=9,color=CINZA)
p.cell(row=B0+10,column=1,value="Se a lista estiver vazia, nenhum caso está abaixo do mínimo. Esses casos merecem conversa na renovação ou revisão do que foi combinado.").font=F(size=9,color=LILAS)
bc=BarChart(); bc.type="col"; bc.height=7; bc.width=13; bc.title="Valor por hora médio por área"; bc.style=2
bc.add_data(Reference(p,min_col=5,min_row=A0+1,max_row=A0+1+len(dados.AREAS)),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=A0+2,max_row=A0+1+len(dados.AREAS)))
bc.series[0].graphicalProperties.solidFill="3B1F5E"; bc.legend=None; bc.y_axis.majorGridlines=None
p.add_chart(bc,f"J{A0}")
widths(p,(24,26,14,14,16,14,14,14,44,8,8)); p.freeze_panes="A7"; p.sheet_view.showGridLines=False
# ---------- exemplos ----------
horas={"Consultoria pontual":(3,8),"Contrato ou documento":(6,15),"Recurso":(15,35),"Acordo e negociação":(8,25)}
proc={"Cível":(50,100),"Trabalhista":(35,70),"Previdenciário":(30,60),"Empresarial":(60,120),"Família":(30,70)}
modal={"Consultoria pontual":"Fixo","Contrato ou documento":"Fixo","Recurso":"Fixo","Acordo e negociação":"Misto"}
modproc={"Cível":"Misto","Trabalhista":"Êxito","Previdenciário":"Êxito","Empresarial":"Hora","Família":"Fixo"}
i=0
for a in dados.AREAS:
    for t in TIPOS:
        h=proc[a] if t=="Processo completo" else horas[t]; m=modproc[a] if t=="Processo completo" else modal[t]
        if t=="Consultoria pontual" and a=="Empresarial": h=(4,12); m="Hora"
        for c,v in enumerate((a,t,h[0],h[1],m),start=1): p.cell(row=T0+i,column=c,value=v)
        i+=1
for i,cs in enumerate(dados.CASOS):
    for c,v in enumerate((cs["numero"],cs["cliente"],cs["area"],cs["tipo_hon"],cs["fase"],cs["valor_contratado"],cs["horas_estimadas"]),start=1): k.cell(row=C0+i,column=c,value=v)
como_usar(wb,"Tabela de referência de honorários",[
 ("O que esta planilha faz","Cria a tabela interna de honorários do escritório: para cada área e tipo de serviço, uma faixa mínima e máxima calculada do custo-hora, com horas típicas e modalidade recomendada. Depois compara o que já está contratado com essa referência e aponta os casos abaixo do mínimo."),
 ("Passo 1","Em Config, o custo-hora (da planilha 05), impostos, as margens mínima e alvo e a folga para horas não previstas. Isso vira a hora mínima com folga e a hora alvo com folga: a hora mínima da 05 (R$ 110 no exemplo) acrescida de 20 % de horas não previstas (R$ 127,88)."),
 ("Passo 2","Em Referência, ajuste as horas típicas (de e até) e a modalidade de cada linha. Adicione linhas para os serviços que o escritório faz. A faixa em reais é calculada."),
 ("Passo 3","Em Nossos casos, uma linha por caso com valor contratado e horas estimadas. A situação mostra se está abaixo do mínimo, na faixa ou acima do alvo."),
 ("Passo 4","No topo de Referência: quantos casos estão abaixo do mínimo, quanto falta e o valor por hora médio por área. Use a faixa ao montar a proposta (planilha 07)."),
 ("Rotina","Revise a tabela a cada trimestre, junto com o custo-hora. Antes de aceitar caso novo, confira a faixa."),
 ("Com a IA","Copie \"O que cobramos hoje, por área\" e use o prompt \"Honorários 06 · Montar a tabela de referência interna\" da biblioteca do kit para apontar onde o escritório está cobrando abaixo do custo e sugerir uma conversa de reajuste. Os valores da tabela são do seu escritório, não uma tabela oficial."),
])
proteger(wb); salvar(wb,"08-tabela-de-referencia.xlsx","Tabela de referência de honorários · Kit de Gestão para Advogados")
