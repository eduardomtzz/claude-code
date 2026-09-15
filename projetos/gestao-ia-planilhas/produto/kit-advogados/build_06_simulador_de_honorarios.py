#!/usr/bin/env python3
"""Planilha 6 do Kit de Gestão para Advogados: Simulador de honorários. Gera 06-simulador-de-honorarios.xlsx"""
from ssg import *
from openpyxl.chart import BarChart, Reference
import dados
NE=10; ND=6                      # etapas e despesas
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Impostos, margem e as regras de risco valem para todos os casos simulados.",merge_to="H")
cfg["A4"]="Nome do escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Mês de referência"; cfg["B5"]="Setembro de 2026"
cfg["A6"]="Data de referência"; cfg["B6"]="=TODAY()"
cfg["A7"]="Impostos e taxas sobre o que entra (%)"; cfg["B7"]=dados.ALIQ
cfg["A8"]="Margem desejada sobre o preço (%)"; cfg["B8"]=dados.MARGEM
cfg["A9"]="Chance de êxito mínima para aceitar êxito puro (%)"; cfg["B9"]=0.60
cfg["A10"]="Folga mínima de chance acima do ponto de equilíbrio (pontos)"; cfg["B10"]=0.15
cfg["A11"]="Folga mínima de horas no valor fixo (%)"; cfg["B11"]=0.20
cfg["A12"]="Aceitar risco médio na recomendação?"; cfg["B12"]="Sim"
for r in range(4,13): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"]); calc(cfg["B6"],DATA)
for r in (7,8,9,10,11): inp(cfg.cell(row=r,column=2),PCT,center=True)
inp(cfg["B12"],center=True)
dvsn=lista('"Sim,Não"'); dvsn.add("B12"); cfg.add_data_validation(dvsn)
notas={7:"Exemplo; confira com o contador. O mesmo percentual da planilha 05.",8:"Quanto do preço deve sobrar depois do custo. Igual à planilha 05.",
 9:"Abaixo disso, êxito puro é marcado como risco alto: o escritório trabalha meses e pode não receber.",
 10:"Se a chance estimada está a menos de 15 pontos da chance mínima para não ter prejuízo, o risco é alto.",
 11:"No fixo, o risco é o caso consumir mais horas que o estimado. Com 20% de folga ou mais, risco baixo.",
 12:"\"Não\" faz a recomendação escolher só entre modalidades de risco baixo."}
for r,t in notas.items(): cfg.cell(row=r,column=3,value=t); nota(cfg.cell(row=r,column=3))
cfg["E4"]="Áreas"; rotulo(cfg["E4"]); cfg["E3"]="Preencha de cima para baixo, sem pular linha."; nota(cfg["E3"])
for i in range(26): inp(cfg.cell(row=5+i,column=5))
for i,a in enumerate(dados.AREAS): cfg.cell(row=5+i,column=5,value=a)
cfg["G4"]="Modalidades"; rotulo(cfg["G4"])
for i,m in enumerate(dados.TIPOS_HON): cfg.cell(row=5+i,column=7,value=m).font=F(size=10,color=TINTA)
widths(cfg,(52,14,80,3,22,3,14)); cfg.sheet_view.showGridLines=False
# ---------- Simulador ----------
s=wb.create_sheet("Simulador",0)
titulo(s,'=Config!$B$4&" · Simulador de honorários · "&Config!$B$5',"Preencha o amarelo: dados do caso, horas por etapa, despesas e o que pretende cobrar em cada modalidade. A comparação e a recomendação são calculadas.",merge_to="K")
IMP="Config!$B$7"; MARG="Config!$B$8"; CHMIN="Config!$B$9"; FOLGA="Config!$B$10"; FOLGAH="Config!$B$11"; ACMED="Config!$B$12"
# 1. o caso
s["A7"]="1. O caso"; s["A7"].font=F(bold=True,size=13,color=UVA)
campos=[("Cliente","Cliente",None),("Área","Cível",None),("O que será feito (resumo)","Discussão de contrato de prestação de serviços",None),
 ("Custo-hora do escritório (R$)",dados.CUSTO_HORA,BRL),("Valor em discussão (R$)",60000,BRL0),("Chance de êxito estimada (%)",0.55,PCT)]
for i,(a,v,fmt) in enumerate(campos):
    r=8+i; s.cell(row=r,column=1,value=a); rotulo(s.cell(row=r,column=1)); s.cell(row=r,column=2,value=v); inp(s.cell(row=r,column=2),fmt,center=fmt is not None)
s["B8"]=dados.CLIENTES[7][0]
s["C11"]="Copie da planilha 05 · Custo-hora (Painel, \"Custo-hora do escritório\"). No exemplo, R$ 66,0714 (18.500 ÷ 280 h): a hora mínima abaixo fica igual à da 05 (R$ 106,57)."; nota(s["C11"])
s["C12"]="Quanto o cliente recebe, deixa de pagar ou economiza se o caso der certo. Base do cálculo de êxito."; nota(s["C12"])
s["C13"]="Sua estimativa honesta. Ela define o valor esperado e o risco das modalidades com êxito."; nota(s["C13"])
s["A14"]="Valor esperado da causa (R$)"; rotulo(s["A14"]); s["B14"]="=B12*B13"; calc(s["B14"],BRL0); s["C14"]="Valor em discussão × chance. É o que se espera receber, em média."; nota(s["C14"])
s["A15"]="Hora mínima para este caso (R$)"; rotulo(s["A15"]); s["B15"]=f"=IFERROR(B11/(1-{IMP}-{MARG}),\"\")"; calc(s["B15"],BRL); s["C15"]="Custo-hora ÷ (1 − impostos − margem)."; nota(s["C15"])
dva=lista("=OFFSET(Config!$E$5,0,0,MAX(1,COUNTA(Config!$E$5:$E$30)),1)"); dva.add("B9"); s.add_data_validation(dva)
CH="$B$11"; VC="$B$12"; PCH="$B$13"; VE="$B$14"
# 2. horas por etapa
E0=19; EN=E0+NE-1; ET=EN+1
s.cell(row=E0-2,column=1,value="2. Horas estimadas por etapa").font=F(bold=True,size=13,color=UVA)
hdr(s,E0-1,["Etapa","Horas estimadas","Custo (R$)"])
for r in range(E0,EN+1):
    inp(s.cell(row=r,column=1)); inp(s.cell(row=r,column=2),"0.0",center=True)
    s.cell(row=r,column=3,value=f'=IF(B{r}="","",B{r}*{CH})'); calc(s.cell(row=r,column=3),BRL)
s.cell(row=ET,column=1,value="Total de horas e custo das horas"); rotulo(s.cell(row=ET,column=1)); s.cell(row=ET,column=1).border=borda
s.cell(row=ET,column=2,value=f"=SUM(B{E0}:B{EN})"); calc(s.cell(row=ET,column=2),"0.0"); s.cell(row=ET,column=3,value=f"=SUM(C{E0}:C{EN})"); calc(s.cell(row=ET,column=3),BRL)
for c in (2,3): s.cell(row=ET,column=c).font=F(bold=True,color=UVA,size=10)
HT=f"$B${ET}"; CHT=f"$C${ET}"
# 3. despesas
D0=ET+4; DN=D0+ND-1; DT=DN+1
s.cell(row=D0-2,column=1,value="3. Despesas do caso").font=F(bold=True,size=13,color=UVA)
hdr(s,D0-1,["Despesa","Valor (R$)","Cliente reembolsa?","Custo para o escritório (R$)"])
for r in range(D0,DN+1):
    inp(s.cell(row=r,column=1)); inp(s.cell(row=r,column=2),BRL,center=True); inp(s.cell(row=r,column=3),center=True)
    s.cell(row=r,column=4,value=f'=IF(B{r}="","",IF(C{r}="Sim",0,B{r}))'); calc(s.cell(row=r,column=4),BRL)
dvr=lista('"Sim,Não"'); dvr.add(f"C{D0}:C{DN}"); s.add_data_validation(dvr)
s.cell(row=DT,column=1,value="Total de despesas · custo para o escritório"); rotulo(s.cell(row=DT,column=1)); s.cell(row=DT,column=1).border=borda
s.cell(row=DT,column=2,value=f"=SUM(B{D0}:B{DN})"); calc(s.cell(row=DT,column=2),BRL); s.cell(row=DT,column=4,value=f"=SUM(D{D0}:D{DN})"); calc(s.cell(row=DT,column=4),BRL)
s.cell(row=DT,column=4).font=F(bold=True,color=UVA,size=10)
DESP=f"$D${DT}"
s.cell(row=DT+1,column=1,value="Custo total do caso (horas + despesas que o escritório absorve)"); rotulo(s.cell(row=DT+1,column=1)); s.cell(row=DT+1,column=1).border=borda
s.cell(row=DT+1,column=4,value=f"={CHT}+{DESP}"); calc(s.cell(row=DT+1,column=4),BRL); s.cell(row=DT+1,column=4).font=F(bold=True,color=UVA,size=10)
CUSTO=f"$D${DT+1}"
# 4. o que cobrar
M0=DT+5
s.cell(row=M0-2,column=1,value="4. O que você pretende cobrar em cada modalidade").font=F(bold=True,size=13,color=UVA)
hdr(s,M0-1,["Modalidade","Valor","Como funciona"])
mod_in=[("Fixo · valor fechado (R$)",7000,BRL0,"Um valor pelo caso inteiro, independente das horas. Risco: o caso consumir mais horas que o estimado."),
 ("Hora · valor da hora cobrada (R$)",dados.VALOR_HORA_COBRADA,BRL,"Cobra as horas trabalhadas. Risco baixo para o escritório; o cliente pode questionar as horas."),
 ("Êxito · % sobre o resultado",0.25,PCT,"Só recebe se o caso der certo, no fim. Risco: trabalhar e não receber."),
 ("Misto · entrada fixa (R$)",4500,BRL0,"Uma parte fixa no início (cobre o custo) mais um percentual sobre o resultado."),
 ("Misto · % sobre o resultado",0.15,PCT,"")]
for i,(a,v,fmt,t) in enumerate(mod_in):
    r=M0+i; s.cell(row=r,column=1,value=a); calc(s.cell(row=r,column=1),center=False); s.cell(row=r,column=2,value=v); inp(s.cell(row=r,column=2),fmt,center=True)
    s.cell(row=r,column=3,value=t); calc(s.cell(row=r,column=3),center=False); nota(s.cell(row=r,column=3)); s.merge_cells(start_row=r,start_column=3,end_row=r,end_column=8)
FX=f"$B${M0}"; HR=f"$B${M0+1}"; EX=f"$B${M0+2}"; ME=f"$B${M0+3}"; MP=f"$B${M0+4}"
# 5. comparação
C0=M0+8
s.cell(row=C0-2,column=1,value="5. Comparação das modalidades").font=F(bold=True,size=13,color=UVA)
hdr(s,C0-1,["Modalidade","Receita esperada (R$)","Impostos e taxas (R$)","Custo do caso (R$)","Margem esperada (R$)","Margem (%)","Se o caso for perdido (R$)","Ponto de equilíbrio","Risco","Pontuação","Por que este risco"],height=40)
LIQ=f"(1-{IMP})"
rows=[
 ("Fixo",f"={FX}",f"=E{{r}}",
  f'="Até "&ROUND(({FX}*{LIQ}-{DESP})/{CH},0)&" horas sem prejuízo (estimadas: "&ROUND({HT},0)&")"',
  f'=IF({HT}=0,"Alto",IF(({FX}*{LIQ}-{DESP})/{CH}/{HT}-1>={FOLGAH},"Baixo",IF(({FX}*{LIQ}-{DESP})/{CH}>={HT},"Médio","Alto")))',
  f'="Folga de horas: "&ROUND((({FX}*{LIQ}-{DESP})/{CH}/{HT}-1)*100,0)&"% (mínimo para risco baixo: "&ROUND({FOLGAH}*100,0)&"%)"'),
 ("Hora",f"={HR}*{HT}",f"=E{{r}}",
  f'="Hora mínima sem prejuízo: R$ "&FIXED({CUSTO}/({HT}*{LIQ}),2)&" (você cobra R$ "&FIXED({HR},2)&")"',   # FIXED usa o separador do idioma do Excel (pt-BR: 1.234,56)
  f'=IF({HR}>=$B$15,"Baixo",IF({HR}*{HT}*{LIQ}>={CUSTO},"Médio","Alto"))',
  f'=IF({HR}>=$B$15,"A hora cobrada cobre custo, impostos e margem desejada","A hora cobrada fica abaixo da hora mínima com margem (R$ "&FIXED($B$15,2)&")")'),
 ("Êxito",f"={EX}*{VE}",f"=-{CUSTO}",
  f'="Chance mínima de êxito para não ter prejuízo: "&ROUND({CUSTO}/({EX}*{VC}*{LIQ})*100,0)&"% (estimada: "&ROUND({PCH}*100,0)&"%)"',
  f'=IF(OR({PCH}<{CHMIN},{PCH}<{CUSTO}/({EX}*{VC}*{LIQ})+{FOLGA}),"Alto","Médio")',
  f'=IF({PCH}<{CHMIN},"Chance estimada abaixo do mínimo aceitável para êxito puro ("&ROUND({CHMIN}*100,0)&"%)",IF({PCH}<{CUSTO}/({EX}*{VC}*{LIQ})+{FOLGA},"Chance estimada perto demais do ponto de equilíbrio","Só recebe no fim; o caixa precisa aguentar até lá"))'),
 ("Misto",f"={ME}+{MP}*{VE}",f"={ME}*{LIQ}-{CUSTO}",
  f'=IF({ME}*{LIQ}>={CUSTO},"A entrada já cobre o custo do caso; o êxito é margem","Chance mínima de êxito para não ter prejuízo: "&ROUND(({CUSTO}-{ME}*{LIQ})/({MP}*{VC}*{LIQ})*100,0)&"% (estimada: "&ROUND({PCH}*100,0)&"%)")',
  f'=IF({PCH}<MAX(0,({CUSTO}-{ME}*{LIQ})/({MP}*{VC}*{LIQ}))+{FOLGA},"Alto",IF({ME}*{LIQ}<{CUSTO},"Médio","Baixo"))',
  f'=IF({ME}*{LIQ}>={CUSTO},"Entrada cobre o custo: mesmo perdendo, não há prejuízo",IF({ME}*{LIQ}<{CUSTO},"Entrada não cobre todo o custo; parte depende do êxito",""))'),
]
for i,(nome,rec,perde,pe,risco,pq) in enumerate(rows):
    r=C0+i
    s.cell(row=r,column=1,value=nome); calc(s.cell(row=r,column=1),center=False); s.cell(row=r,column=1).font=F(bold=True,color=UVA,size=10)
    s.cell(row=r,column=2,value=rec); calc(s.cell(row=r,column=2),BRL)
    s.cell(row=r,column=3,value=f"=B{r}*{IMP}"); calc(s.cell(row=r,column=3),BRL)
    s.cell(row=r,column=4,value=f"={CUSTO}"); calc(s.cell(row=r,column=4),BRL)
    s.cell(row=r,column=5,value=f"=B{r}-C{r}-D{r}"); calc(s.cell(row=r,column=5),BRL)
    s.cell(row=r,column=6,value=f'=IF(B{r}=0,"",E{r}/B{r})'); calc(s.cell(row=r,column=6),PCT)
    s.cell(row=r,column=7,value=perde.format(r=r)); calc(s.cell(row=r,column=7),BRL)
    s.cell(row=r,column=8,value=f'=IFERROR({pe[1:]},"Preencha horas e valores")'); calc(s.cell(row=r,column=8),center=False); s.cell(row=r,column=8).alignment=Alignment(wrap_text=True,vertical="center")
    s.cell(row=r,column=9,value=f'=IFERROR({risco[1:]},"Alto")'); calc(s.cell(row=r,column=9))
    s.cell(row=r,column=10,value=f'=IF(OR(I{r}="Alto",AND(I{r}="Médio",{ACMED}="Não")),-1E+9,E{r})'); calc(s.cell(row=r,column=10),BRL0); s.cell(row=r,column=10).font=F(size=9,color=CINZA)
    s.cell(row=r,column=11,value=f'=IFERROR({pq[1:]},"")'); calc(s.cell(row=r,column=11),center=False); s.cell(row=r,column=11).alignment=Alignment(wrap_text=True,vertical="center"); nota(s.cell(row=r,column=11))
    s.row_dimensions[r].height=42
CN=C0+3
s.conditional_formatting.add(f"I{C0}:I{CN}", FormulaRule(formula=[f'I{C0}="Alto"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
s.conditional_formatting.add(f"I{C0}:I{CN}", FormulaRule(formula=[f'I{C0}="Médio"'], fill=fill(AMARELO)))
s.conditional_formatting.add(f"I{C0}:I{CN}", FormulaRule(formula=[f'I{C0}="Baixo"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10)))
s.conditional_formatting.add(f"E{C0}:G{CN}", FormulaRule(formula=[f'AND(ISNUMBER(E{C0}),E{C0}<0)'], font=F(color="C8402E",size=10,bold=True)))
s.conditional_formatting.add(f"A{C0}:A{CN}", FormulaRule(formula=[f'$A{C0}=$A$5'], fill=fill(SOL)))
s.cell(row=CN+1,column=1,value="Pontuação: coluna auxiliar da recomendação (margem esperada; modalidade com risco recusado vale −1 bilhão). Receita esperada de êxito e misto = percentual × valor esperado da causa.").font=F(size=9,color=LILAS)
# recomendação no topo
PONT=f"$J${C0}:$J${CN}"; MODS=f"$A${C0}:$A${CN}"; RISC=f"$I${C0}:$I${CN}"
kpi(s,4,1,"Modalidade recomendada",f'=IF(MAX({PONT})<=-1E+9,"Nenhuma com risco aceitável",INDEX({MODS},MATCH(MAX({PONT}),{PONT},0)))',SOL,UVA,fmt="@")
kpi(s,4,3,"Margem esperada",f'=IF(MAX({PONT})<=-1E+9,"",INDEX($E${C0}:$E${CN},MATCH(MAX({PONT}),{PONT},0)))',VERDE,VERDE_T,fmt=BRL0)
kpi(s,4,5,"Risco da recomendada",f'=IF(MAX({PONT})<=-1E+9,"",INDEX({RISC},MATCH(MAX({PONT}),{PONT},0)))',LAVANDA,UVA,fmt="@")
kpi(s,4,7,"Custo total do caso",f"={CUSTO}",LAVANDA,UVA,fmt=BRL0)
kpi(s,4,9,"Hora mínima para o caso","=$B$15",LAVANDA,UVA,fmt=BRL)
fora=f'IF($I${C0}="Alto","Fixo, ","")&IF($I${C0+1}="Alto","Hora, ","")&IF($I${C0+2}="Alto","Êxito, ","")&IF($I${C0+3}="Alto","Misto, ","")'
s["A6"]=(f'=IF(MAX({PONT})<=-1E+9,"Nenhuma modalidade ficou com risco aceitável. Reveja horas, valores ou a chance de êxito; a maior margem em números seria "&INDEX({MODS},MATCH(MAX($E${C0}:$E${CN}),$E${C0}:$E${CN},0))&".",'
         f'"Regra: maior margem esperada entre as modalidades com risco aceitável. Fora por risco alto: "&IF(COUNTIF({RISC},"Alto")=0,"nenhuma",LEFT({fora},LEN({fora})-2))&". Compare também a coluna \'Se o caso for perdido\' antes de decidir.")')
nota(s["A6"]); s.merge_cells("A6:K6"); s["A6"].alignment=Alignment(wrap_text=True,vertical="top"); s.row_dimensions[6].height=30
bc=BarChart(); bc.type="col"; bc.height=7; bc.width=13; bc.title="Margem esperada × se perder"; bc.style=2
bc.add_data(Reference(s,min_col=5,min_row=C0-1,max_row=CN),titles_from_data=True); bc.add_data(Reference(s,min_col=7,min_row=C0-1,max_row=CN),titles_from_data=True)
bc.set_categories(Reference(s,min_col=1,min_row=C0,max_row=CN)); bc.series[0].graphicalProperties.solidFill="3B1F5E"; bc.series[1].graphicalProperties.solidFill="B89BE0"; bc.legend.position="b"; bc.y_axis.majorGridlines=None
s.add_chart(bc,f"F{E0-2}")
widths(s,(40,16,16,16,16,10,16,40,10,12,44)); s.freeze_panes="A7"; s.sheet_view.showGridLines=False
# ---------- exemplo ----------
etapas=[("Reunião inicial e análise dos documentos",4),("Estudo do caso e estratégia",6),("Redação e protocolo inicial",12),
        ("Acompanhamento e manifestações",20),("Audiências e reuniões",8),("Encerramento e prestação de contas",3)]
for i,(a,h) in enumerate(etapas): s.cell(row=E0+i,column=1,value=a); s.cell(row=E0+i,column=2,value=h)
desp=[("Taxas e custas",800,"Sim"),("Deslocamentos",300,"Não"),("Cópias e certidões",150,"Não"),("Terceiros (perito, tradutor)",0,"Sim")]
for i,(a,v,rb) in enumerate(desp): s.cell(row=D0+i,column=1,value=a); s.cell(row=D0+i,column=2,value=v); s.cell(row=D0+i,column=3,value=rb)
como_usar(wb,"Simulador de honorários",[
 ("O que esta planilha faz","Para um caso, estima as horas por etapa e as despesas, calcula o custo do caso e compara quatro formas de cobrar: fixo, por hora, êxito e misto. Mostra a margem esperada, o que acontece se o caso for perdido, o ponto de equilíbrio e o risco de cada uma, e recomenda a de maior margem com risco aceitável."),
 ("Passo 1","Em Config, confira impostos, margem e as regras de risco (chance mínima para êxito puro, folgas). Uma vez só."),
 ("Passo 2","Em Simulador, bloco 1: cliente, área, custo-hora (copie da planilha 05), valor em discussão e a chance de êxito que você estima."),
 ("Passo 3","Blocos 2 e 3: horas por etapa e despesas do caso, marcando o que o cliente reembolsa."),
 ("Passo 4","Bloco 4: o valor que você pretende cobrar em cada modalidade. Mude os números e veja a comparação e a recomendação no topo mudarem na hora."),
 ("Rotina","Antes de cada proposta: 10 minutos. Depois, leve a modalidade escolhida para a planilha 07 (Proposta de honorários)."),
 ("Com a IA","Copie o bloco 5 e use o prompt \"Honorários 07 · Fixo, hora, êxito ou misto: perguntas antes de escolher\" da biblioteca do kit para listar o que falta perguntar antes de fechar o valor. A decisão continua sua."),
 ("Números em texto","As frases da comparação (\"Hora mínima sem prejuízo: R$ ...\") usam a função FIXED: o separador de milhar e de decimal segue o idioma do Excel (no Excel em português: 1.234,56)."),
])
proteger(wb); salvar(wb,"06-simulador-de-honorarios.xlsx","Simulador de honorários · Kit de Gestão para Advogados")
