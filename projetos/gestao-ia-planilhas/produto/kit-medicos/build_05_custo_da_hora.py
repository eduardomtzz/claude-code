#!/usr/bin/env python3
"""Planilha 5 do Kit de Gestão para Médicos: Custo da hora de atendimento. Gera 05-custo-da-hora.xlsx
Custo-hora = (custos fixos + equipe + pró-labore) ÷ horas de atendimento do mês (só de quem entra no custo-hora: os sócios).
A médica parceira (repasse) é custo variável e fica fora; a recepcionista já está nos custos fixos."""
from ssg import *
INC='"cadastro incompleto"'; MINV='"margens inválidas (Config)"'
SENS_OK=lambda r: f'IF(ISNUMBER(B{r}),AND(B{r}>=0,B{r}<1),FALSE)'   # queda da sensibilidade: 0 a 99 % (auditoria final-5)   # textos das guardas (auditoria final G01/G02)
from openpyxl.chart import BarChart, Reference
import dados
NCF=30; NP=10
CF0=5; CFN=CF0+NCF-1; CFT=CFN+2
P0=5; PN=P0+NP-1
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Margem e impostos definem a hora mínima a cobrar.",merge_to="F")
cfg["A4"]="Nome da clínica"; cfg["B4"]=f"{dados.CLINICA} (exemplo fictício)"
cfg["A5"]="Mês de referência"; cfg["B5"]="Setembro de 2026"
cfg["A6"]="Data de referência"; cfg["B6"]=dados.HOJE
cfg["A7"]="Margem mínima sobre o preço (%)"; cfg["B7"]=dados.MARGEM
cfg["A8"]="Impostos sobre o que entra (%)"; cfg["B8"]=dados.ALIQ
cfg["A9"]="Arredondar a hora mínima para múltiplos de (R$)"; cfg["B9"]=5
cfg["A10"]="Duração de uma consulta (minutos), para o custo do horário vazio"; cfg["B10"]=30
for r in range(4,11): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"]); calc(cfg["B6"],DATA); inp(cfg["B7"],PCT,center=True); inp(cfg["B8"],PCT,center=True); inp(cfg["B9"],BRL0,center=True); inp(cfg["B10"],"0",center=True)
# Auditoria final (G02): imposto e margem são percentuais de 0 a 99 % e a soma tem de ficar
# abaixo de 100 %; senão o denominador (1 − margem − impostos) zera ou inverte e o preço
# mínimo sai negativo. A validação barra a digitação; as fórmulas guardam a colagem.
def _val_pct(ws,cel,outro,msg):
    dv=DataValidation(type="custom",formula1=f'=IF(ISNUMBER({cel}),AND({cel}>=0,{cel}<1,{cel}+N({outro})<1),FALSE)',allow_blank=False,showErrorMessage=True,errorTitle="Percentual",error=msg)
    dv.add(cel); ws.add_data_validation(dv)
_val_pct(cfg,"B7","B8","Margem entre 0 % e 99 %, e margem + impostos abaixo de 100 %: senão nenhum preço cobre o custo.")
_val_pct(cfg,"B8","B7","Impostos entre 0 % e 99 %, e margem + impostos abaixo de 100 %: senão nenhum preço cobre o custo.")
# Auditoria final-2 (G02): um predicado só, visível em Config!B11, decide se margem e impostos
# valem; toda hora mínima e todo preço desta planilha consultam essa célula.
cfg["A11"]="Margem e impostos conferem? (calculado)"; rotulo(cfg["A11"])
cfg["B11"]='=IF(AND(ISNUMBER(B7),ISNUMBER(B8)),IF(AND(B7>=0,B7<1,B8>=0,B8<1,B7+B8<1),"Sim","Não"),"Não")'; calc(cfg["B11"])
cfg["C11"]="\"Não\" suspende a hora mínima em todas as abas: cada percentual precisa ficar entre 0 % e 99 %, e margem + impostos abaixo de 100 %."; nota(cfg["C11"])
cfg["C7"]="Quanto do preço deve sobrar depois de pagar o custo da clínica. 30 % é um ponto de partida; ajuste ao seu mercado."
cfg["C8"]="Percentual de imposto que sai de cada real recebido pela PJ médica. No exemplo, 11 %: alíquota efetiva combinada com o contador (Simples, anexo III ou V, simplificado). Confira a sua com o contador. Só imposto: a taxa da maquininha NÃO entra aqui (ela é despesa variável, conciliada na 16 e lançada no caixa 09 e no resultado 18), e o convênio, que não passa na maquininha, pagaria a taxa sem dever."
cfg["C9"]="Só para o número ficar redondo na tabela de preços."
for r in (7,8,9): nota(cfg.cell(row=r,column=3))
cfg["A12"]="Custo da hora de atendimento = (custos fixos + pró-labore dos sócios) ÷ horas de atendimento planejadas no mês. Hora mínima = custo-hora ÷ (1 − margem − impostos): a margem é sobre o preço, não sobre o custo."; nota(cfg["A12"])
cfg["A13"]="No exemplo: R$ 28.000 ÷ 140 h = R$ 200,00; hora mínima R$ 338,98 → R$ 340. As planilhas 06, 07 e 08 usam este custo-hora. A médica parceira não entra: o repasse dela é custo variável (planilha 11)."; nota(cfg["A13"])
widths(cfg,(58,26,90)); cfg.sheet_view.showGridLines=False
# ---------- Custos fixos ----------
cfx=wb.create_sheet("Custos fixos")
titulo(cfx,"Custos fixos do mês","Tudo que a clínica paga todo mês mesmo com a agenda vazia. Preencha de cima para baixo, sem pular linha.",merge_to="D")
hdr(cfx,4,["Custo fixo","Valor mensal (R$)","Observação"])
for r in range(CF0,CFN+1):
    inp(cfx.cell(row=r,column=1)); inp(cfx.cell(row=r,column=2),BRL,center=True); inp(cfx.cell(row=r,column=3))
cfx.cell(row=CFT,column=1,value="Total de custos fixos"); rotulo(cfx.cell(row=CFT,column=1)); cfx.cell(row=CFT,column=1).border=borda
# Auditoria final-4 (F4-G01): custo fixo com nome e sem valor, ou com texto, não é zero
cfx.cell(row=CFT,column=2,value=f'=IF(SUMPRODUCT(((A{CF0}:A{CFN}<>"")+(B{CF0}:B{CFN}<>"")>0)*((ISNUMBER(B{CF0}:B{CFN})=FALSE)+ISNUMBER(B{CF0}:B{CFN})*(B{CF0}:B{CFN}<0)>0))>0,"custo fixo sem valor numérico ou negativo",SUM(B{CF0}:B{CFN}))'); calc(cfx.cell(row=CFT,column=2),BRL); cfx.cell(row=CFT,column=2).font=F(bold=True,color=UVA,size=10)
cfx.cell(row=CFT+2,column=1,value="Pró-labore dos sócios vai na aba Equipe. Salário da recepção com encargos fica aqui (e marcado \"Sim\" na Equipe, para não contar duas vezes). Materiais de atendimento, taxas de cartão e repasse não são fixos: ficam na precificação (06) e no caixa (09).").font=F(size=9,color=LILAS)
widths(cfx,(40,18,60)); cfx.freeze_panes="A5"; cfx.sheet_view.showGridLines=False
# ---------- Equipe ----------
eq=wb.create_sheet("Equipe")
titulo(eq,"Equipe, pró-labore e horas de atendimento","Uma linha por pessoa. Horas de atendimento: as horas de agenda planejadas no mês (turnos × semanas). Quem é pago por repasse não entra no custo-hora.",merge_to="K")
hdr(eq,4,["Pessoa","Papel","Remuneração","Valor mensal (R$)","Já está nos custos fixos?","Horas de atendimento planejadas no mês","Entra no custo-hora?","Custo direto por hora","Custo-hora completo","Hora mínima a cobrar"],height=40)
IND_H="Painel!$B$20"; DIV="(1-Config!$B$7-Config!$B$8)"; CFGX='Config!$B$11<>"Sim"'
for r in range(P0,PN+1):
    inp(eq.cell(row=r,column=1)); inp(eq.cell(row=r,column=2)); inp(eq.cell(row=r,column=3),center=True); inp(eq.cell(row=r,column=4),BRL,center=True); inp(eq.cell(row=r,column=5),center=True)
    inp(eq.cell(row=r,column=6),"0",center=True); inp(eq.cell(row=r,column=7),center=True)
    # Auditoria final (G01): valor mensal ou horas em branco não viram custo zero — a linha
    # escreve o que falta e a coluna K (oculta) marca para o Painel suspender custo-hora,
    # hora mínima e sensibilidade com "cadastro incompleto".
    eq.cell(row=r,column=8,value=f'=IF(A{r}="","",IF(AND(G{r}<>"Sim",G{r}<>"Não"),"falta: entra no custo-hora?",IF(G{r}<>"Sim","",IF(AND(E{r}<>"Sim",E{r}<>"Não"),"falta: já está nos custos fixos?",IF(NOT(IF(ISNUMBER(F{r}),F{r}>0,FALSE)),"faltam as horas planejadas",IF(AND(E{r}<>"Sim",NOT(IF(ISNUMBER(D{r}),D{r}>=0,FALSE))),"falta o valor mensal",IF(E{r}="Sim",0,D{r})/F{r}))))))'); calc(eq.cell(row=r,column=8),BRL)
    eq.cell(row=r,column=9,value=f'=IF(H{r}="","",IF(NOT(ISNUMBER(H{r})),H{r},IF(NOT(ISNUMBER({IND_H})),{INC},H{r}+{IND_H})))'); calc(eq.cell(row=r,column=9),BRL)
    eq.cell(row=r,column=10,value=f'=IF(I{r}="","",IF(NOT(ISNUMBER(I{r})),I{r},IF({CFGX},{MINV},I{r}/{DIV})))'); calc(eq.cell(row=r,column=10),BRL)
    eq.cell(row=r,column=11,value=f'=IF(AND(A{r}<>"",OR(AND(G{r}<>"Sim",G{r}<>"Não"),AND(G{r}="Sim",OR(NOT(IF(ISNUMBER(F{r}),F{r}>0,FALSE)),AND(E{r}<>"Sim",E{r}<>"Não"),AND(E{r}<>"Sim",NOT(IF(ISNUMBER(D{r}),D{r}>=0,FALSE))))))),1,0)'); eq.cell(row=r,column=11).font=F(color=CINZA,size=9)
dv=lista('"Sim,Não"'); dv.add(f"E{P0}:E{PN}"); dv.add(f"G{P0}:G{PN}"); eq.add_data_validation(dv)
dvr=lista('"Pró-labore,Salário,Repasse"'); dvr.add(f"C{P0}:C{PN}"); eq.add_data_validation(dvr)
eq.cell(row=PN+2,column=1,value="Custo direto por hora = pró-labore ÷ horas de atendimento. Custo-hora completo = custo direto + rateio dos custos fixos por hora (calculado no Painel). Hora mínima = custo-hora completo ÷ (1 − margem − impostos).").font=F(size=9,color=LILAS)
eq.cell(row=PN+3,column=1,value="Horas de atendimento planejadas: turnos da semana × 4,33 semanas (a planilha 01 mostra as disponíveis e as atendidas de verdade). Médico parceiro por repasse: \"Entra no custo-hora? = Não\". O custo da estrutura já está inteiro dentro do custo-hora dos sócios; por isso, na planilha 11, o custo indireto por hora entra só como informação e a margem da parceria desconta o material, não a estrutura de novo.").font=F(size=9,color=LILAS)
widths(eq,(24,30,14,16,14,14,12,14,14,14)); eq.column_dimensions["K"].hidden=True; eq.freeze_panes="A5"; eq.sheet_view.showGridLines=False
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Custo da hora de atendimento · "&Config!$B$5',"Nada para digitar aqui, exceto os percentuais da sensibilidade e as horas atendidas de verdade. Custos vêm de Custos fixos, pessoas de Equipe, margem e impostos de Config.",merge_to="J")
PD=f"Equipe!$D${P0}:$D${PN}"; PE=f"Equipe!$E${P0}:$E${PN}"; PF=f"Equipe!$F${P0}:$F${PN}"; PG=f"Equipe!$G${P0}:$G${PN}"
FLAGP=f"SUM(Equipe!$K${P0}:$K${PN})"   # pessoas com valor, horas ou marcações em branco
FLAGC=f"IF(ISNUMBER('Custos fixos'!$B${CFT}),0,1)"   # custo fixo sem valor numérico (auditoria final-4)
FLAG=f"({FLAGP}+{FLAGC})"
kpi(p,4,1,"Custo total do mês","=B11",LAVANDA,UVA,fmt=BRL0)
kpi(p,4,3,"Horas de atendimento planejadas no mês","=B12",LAVANDA,UVA,fmt="#,##0")
kpi(p,4,5,"Custo da hora de atendimento","=B13",SOL,UVA,fmt=BRL)
kpi(p,4,7,"Hora mínima a cobrar","=B17",VERDE,VERDE_T,fmt=BRL)
kpi(p,4,9,"Custo de um horário vazio","=B21",VERM,VERM_T,fmt=BRL)
p["A6"]="A base do custo-hora são as horas de atendimento PLANEJADAS do mês (turnos × 4,33 semanas): é o preço que cobre o custo quando a agenda está cheia, e é ele que as planilhas 06, 07 e 08 usam. Como a agenda real nunca fica 100 % cheia, o bloco \"Sensibilidade\", no fim desta tela, mostra o custo-hora com as horas de fato atendidas (a última linha usa agosto, da planilha 01): é o número da conversa sobre faltas e horários vazios, não o da tabela de preços."
p["A3"]=(f'=IF({FLAG}=0,"",IF({FLAGC}>0,"Atenção: há custo fixo sem valor, com texto ou negativo na aba Custos fixos. ","")&IF({FLAGP}>0,"Atenção: "&{FLAGP}&" pessoa(s) na aba Equipe com valor mensal, horas ou marcação (entra no custo-hora? / já nos fixos?) em branco. ","")'
         f'&"Custo do mês, custo-hora e hora mínima ficam como \'cadastro incompleto\' até você completar: soma parcial daria custo-hora MENOR do que o real.")')
p["A3"].font=F(size=10,bold=True,color=VERM_T); p.merge_cells("A3:J3"); p["A3"].alignment=Alignment(wrap_text=True,vertical="top")

nota(p["A6"]); p.merge_cells("A6:J6"); p["A6"].alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[6].height=30
p["A7"]="Como chegamos ao número"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Passo","Valor","De onde vem"])
linhas=[
 ("Custos fixos do mês",f"='Custos fixos'!B{CFT}",BRL,"Aba Custos fixos"),
 ("Pró-labore e salários fora dos custos fixos (de quem entra no custo-hora)",f'=IF({FLAG}>0,{INC},SUMIFS({PD},{PE},"Não",{PG},"Sim"))',BRL,"Aba Equipe: marcados \"Entra no custo-hora? = Sim\" e \"Já está nos custos fixos? = Não\""),
 ("Custo total do mês",f'=IF({FLAG}>0,{INC},B9+B10)',BRL,"Soma dos dois acima"),
 ("Horas de atendimento planejadas no mês (quem entra no custo-hora)",f'=IF({FLAG}>0,{INC},SUMIFS({PF},{PG},"Sim"))',"#,##0","Aba Equipe: turnos da semana × 4,33 semanas"),
 ("Custo da hora de atendimento",f'=IF({FLAG}>0,{INC},IF(B12=0,"",B11/B12))',BRL,"Custo total ÷ horas de atendimento"),
 ("Margem mínima sobre o preço",'=IF(ISNUMBER(Config!$B$7),Config!$B$7,"falta em Config")',PCT,"Config"),
 ("Impostos sobre o que entra",'=IF(ISNUMBER(Config!$B$8),Config!$B$8,"falta em Config")',PCT,"Config"),
 ("Hora mínima a cobrar (exata)",f'=IF(B13="","",IF(NOT(ISNUMBER(B13)),B13,IF({CFGX},{MINV},B13/{DIV})))',BRL,"Custo-hora ÷ (1 − margem − impostos)"),
 ("Hora mínima a cobrar (arredondada)",'=IF(B16="","",IF(NOT(ISNUMBER(B16)),B16,IF(NOT(IF(ISNUMBER(Config!$B$9),Config!$B$9>0,FALSE)),"falta o múltiplo de arredondamento em Config",CEILING(B16,Config!$B$9))))',BRL,"Arredondada para cima, no múltiplo de Config"),
 ("Custo direto médio por hora (pró-labore ÷ horas)",f'=IF({FLAG}>0,{INC},IF(B12=0,0,B10/B12))',BRL,"O que os sócios custam por hora de agenda"),
 ("Custos indiretos (custos fixos, com a recepção)",f'=IF({FLAG}>0,{INC},B9)',BRL,"Para ratear por hora de atendimento"),
 ("Custo indireto por hora de atendimento",f'=IF({FLAG}>0,{INC},IF(B12=0,0,B19/B12))',BRL,"Custos fixos ÷ horas de atendimento (estrutura, recepção, aluguel). Já está dentro do custo-hora acima: na 11 serve só para mostrar quanto vale a hora de sala"),
 ("Custo de um horário vazio (consulta de Config, em minutos)",'=IF(B13="","",IF(NOT(ISNUMBER(B13)),B13,IF(NOT(IF(ISNUMBER(Config!$B$10),Config!$B$10>0,FALSE)),"falta a duração da consulta em Config",B13*Config!$B$10/60)))',BRL,"Custo-hora × duração da consulta: o que uma falta custa à clínica"),
]
for i,(a,f_,fmt,c) in enumerate(linhas):
    r=9+i
    p.cell(row=r,column=1,value=a); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f_); calc(p.cell(row=r,column=2),fmt)
    p.cell(row=r,column=3,value=c); calc(p.cell(row=r,column=3),center=False); nota(p.cell(row=r,column=3))
for r in (11,13,17): p.cell(row=r,column=2).font=F(bold=True,color=UVA,size=10)
for r in range(9,22): p.merge_cells(start_row=r,start_column=3,end_row=r,end_column=6)
# por pessoa
r0=24
p.cell(row=r0,column=1,value="Por pessoa").font=F(bold=True,size=13,color=UVA)
hdr(p,r0+1,["Pessoa","Papel","Remuneração","Horas planejadas","Custo direto por hora","Custo-hora completo","Hora mínima a cobrar"],height=30)
for i in range(NP):
    r=r0+2+i; src=f"Equipe!$A${P0+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",Equipe!$B${P0+i})'); calc(p.cell(row=r,column=2),center=False)
    p.cell(row=r,column=3,value=f'=IF({src}="","",Equipe!$C${P0+i})'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=IF({src}="","",IF(Equipe!$F${P0+i}="","",Equipe!$F${P0+i}))'); calc(p.cell(row=r,column=4),"#,##0")
    for col,src_c in ((5,"H"),(6,"I"),(7,"J")):
        p.cell(row=r,column=col,value=f'=IF({src}="","",IF(Equipe!${src_c}${P0+i}="","—",Equipe!${src_c}${P0+i}))'); calc(p.cell(row=r,column=col),BRL)
p.cell(row=r0+2+NP,column=1,value="Quem é pago por repasse ou já está nos custos fixos aparece com \"—\": não tem custo-hora próprio. O custo-hora completo de cada sócio = pró-labore ÷ horas + rateio da estrutura.").font=F(size=9,color=LILAS)
# sensibilidade
s0=r0+NP+4
p.cell(row=s0,column=1,value="Sensibilidade: e se faltas e horários vazios tirarem horas do mês?").font=F(bold=True,size=13,color=UVA)
p.cell(row=s0+1,column=1,value="O custo fixo continua e cada hora atendida fica mais cara. Os percentuais em amarelo podem ser trocados; a última linha usa as horas atendidas de verdade (Painel da planilha 01, mês fechado).").font=F(size=9,color=LILAS)
hdr(p,s0+2,["Cenário","Queda nas horas","Horas atendidas","Custo-hora","Hora mínima a cobrar","Diferença por hora"],height=30)
for i,q in enumerate((0,0.10,0.20,0.30)):
    r=s0+3+i
    p.cell(row=r,column=1,value="Agenda planejada" if i==0 else f'=IF({SENS_OK(r)},"Queda de "&ROUND(B{r}*100,0)&"%","Percentual inválido (0 a 99 %)")'); calc(p.cell(row=r,column=1),center=False)
    if i==0: p.cell(row=r,column=2,value=0); calc(p.cell(row=r,column=2),PCT)
    else: p.cell(row=r,column=2,value=q); inp(p.cell(row=r,column=2),PCT,center=True)
    p.cell(row=r,column=3,value=f'=IF(AND(ISNUMBER($B$12),{SENS_OK(r)}),$B$12*(1-B{r}),"")'); calc(p.cell(row=r,column=3),"#,##0.0")
    p.cell(row=r,column=4,value=f'=IF(OR(NOT(IF(ISNUMBER(C{r}),C{r}>0,FALSE)),NOT(ISNUMBER($B$11))),"",$B$11/C{r})'); calc(p.cell(row=r,column=4),BRL)
    p.cell(row=r,column=5,value=f'=IF(D{r}="","",IF({CFGX},{MINV},D{r}/{DIV}))'); calc(p.cell(row=r,column=5),BRL)
    p.cell(row=r,column=6,value=f'=IF(D{r}="","",D{r}-$D${s0+3})'); calc(p.cell(row=r,column=6),BRL)
r=s0+7
p.cell(row=r,column=1,value="Agosto de 2026 realizado (horas atendidas dos sócios: Painel da 01 com Config = Agosto, coluna \"Horas atendidas\" da Dra. Carolina + do Dr. Paulo, sem a médica parceira)"); calc(p.cell(row=r,column=1),center=False)
h_ago=round(dados.horas_atendidas(8,prof=dados.CAR)+dados.horas_atendidas(8,prof=dados.PAU),1)
p.cell(row=r,column=3,value=h_ago); inp(p.cell(row=r,column=3),"#,##0.0",center=True)
p.cell(row=r,column=2,value=f'=IF(OR(C{r}="",NOT(ISNUMBER($B$12))),"",IF(NOT(IF(ISNUMBER(C{r}),C{r}>=0,FALSE)),"horas inválidas",1-C{r}/$B$12))'); calc(p.cell(row=r,column=2),PCT)
p.cell(row=r,column=4,value=f'=IF(OR(NOT(IF(ISNUMBER(C{r}),C{r}>0,FALSE)),NOT(ISNUMBER($B$11))),"",$B$11/C{r})'); calc(p.cell(row=r,column=4),BRL)
p.cell(row=r,column=5,value=f'=IF(D{r}="","",IF({CFGX},{MINV},D{r}/{DIV}))'); calc(p.cell(row=r,column=5),BRL)
p.cell(row=r,column=6,value=f'=IF(D{r}="","",D{r}-$D${s0+3})'); calc(p.cell(row=r,column=6),BRL)
p.cell(row=r+1,column=1,value="Planejado × realizado: a diferença entre o custo-hora de R$ 200 e o de agosto é o preço das faltas e dos horários vazios. Reduzir faltas (planilha 02) barateia a hora sem cortar nada.").font=F(size=9,color=LILAS)
bc=BarChart(); bc.type="col"; bc.height=7; bc.width=14; bc.title="Custo-hora por cenário"; bc.style=2
bc.add_data(Reference(p,min_col=4,min_row=s0+2,max_row=s0+7),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=s0+3,max_row=s0+7))
bc.series[0].graphicalProperties.solidFill="3B1F5E"; bc.legend=None; bc.y_axis.majorGridlines=None
p.add_chart(bc,f"H{s0}")
widths(p,(52,16,16,16,16,16,16,14,14,14)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
# ---------- exemplos (dados.py) ----------
for i,(nome,valor) in enumerate(dados.CUSTOS_FIXOS):
    cfx.cell(row=CF0+i,column=1,value=nome); cfx.cell(row=CF0+i,column=2,value=valor)
cfx.cell(row=CF0+1,column=3,value="Bruna Carvalho (CLT): a mesma pessoa da aba Equipe, marcada \"Sim\" lá")
for i,(nome,papel,tipo,custo,h) in enumerate(dados.PESSOAS):
    r=P0+i
    rem={"Pró-labore":"Pró-labore","Salário (já nos custos fixos)":"Salário","Repasse (50 % da produção)":"Repasse"}[tipo]
    for c,v in zip((1,2,3,4,5,6,7),(nome,papel,rem,custo if custo else None,"Sim" if rem=="Salário" else "Não",h if h else None,"Sim" if rem=="Pró-labore" else "Não")):
        if v is not None: eq.cell(row=r,column=c,value=v)
como_usar(wb,"Custo da hora de atendimento",[
 ("O que esta planilha faz","Responde \"quanto custa uma hora da minha agenda?\". Soma custos fixos e pró-labore dos sócios, divide pelas horas de atendimento planejadas no mês e mostra o custo-hora, a hora mínima a cobrar (com margem e impostos), o custo de um horário vazio e o que acontece quando faltas tiram horas do mês."),
 ("Passo 1","Em Custos fixos, liste o que a clínica paga todo mês (aluguel, recepção com encargos, contador, sistema, energia, marketing). Uma linha por item, de cima para baixo."),
 ("Passo 2","Em Equipe, cada pessoa: remuneração (pró-labore, salário ou repasse), valor mensal, se já está nos custos fixos, horas de atendimento planejadas no mês e se entra no custo-hora. Sócios entram; médico parceiro por repasse não; recepção já está nos fixos."),
 ("Passo 3","Em Config, a margem mínima sobre o preço e o percentual de impostos e taxas que sai de cada recebimento (a alíquota efetiva que o contador informar)."),
 ("Passo 4","Em Painel: custo-hora, hora mínima a cobrar, custo por pessoa, custo de um horário vazio e a sensibilidade. Use o custo-hora nas planilhas 06 (precificação), 07 (simulador de convênio) e 08 (tabela de preços)."),
 ("Rotina","Revise uma vez por trimestre ou quando mudar aluguel, equipe ou pró-labore. Leva 10 minutos. Na última linha da sensibilidade, digite as horas atendidas do mês fechado (Painel da 01) para ver o custo-hora real."),
 ("Com a IA","Copie \"Como chegamos ao número\" e use o prompt \"Preço 01 · Entender o custo da minha hora\" da biblioteca do kit para explicar o custo-hora ao sócio em linguagem simples."),
])
proteger(wb); salvar(wb,"05-custo-da-hora.xlsx","Custo da hora de atendimento · Kit de Gestão para Médicos")
