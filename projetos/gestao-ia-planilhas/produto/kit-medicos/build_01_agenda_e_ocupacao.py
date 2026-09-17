#!/usr/bin/env python3
"""Planilha 1 do Kit de Gestão para Médicos: Agenda e ocupação por profissional e sala. Gera 01-agenda-e-ocupacao.xlsx
Fonte do cadastro de pacientes e da agenda do kit: 02 (faltas e retornos) e 16 (conciliação de cartão) copiam daqui.
Exemplo: agenda de 01/06/2026 a hoje + 21 dias (dados.AGENDA); Painel em Setembro (em andamento, até ontem)."""
from ssg import *
import dados
from openpyxl.chart import BarChart, Reference
from datetime import time

N=3000; R0=5; RN=R0+N-1            # Agenda: linhas 5..3004 (≈ 300 atendimentos/mês → 10 meses por arquivo)
NPAC=400; RP=R0+NPAC-1              # Pacientes: linhas 5..404
NPROF=8; NSALA=6; NPAG=6; NPROC=12; NTUR=24; NFER=20
T0=20; TN=T0+NTUR-1                 # turnos na Config: linhas 20..43
X0=50; XN=X0+30                     # auxiliar dias do mês: linhas 50..80
def off(sheet,col,r0,r1): return f"=OFFSET({sheet}!${col}${r0},0,0,MAX(1,COUNTA({sheet}!${col}${r0}:${col}${r1})),1)"
NOME=f"{dados.CLINICA} (exemplo fictício)"
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche. Profissionais, salas, pagadores, procedimentos, tabela de preços e turnos alimentam a Agenda e o Painel.",merge_to="R")
cfg["A4"]="Clínica"; cfg["B4"]=NOME
cfg["A5"]="Ano do painel"; cfg["B5"]=2026
cfg["A6"]="Mês do painel"; cfg["B6"]="Setembro"
cfg["A7"]="Número do mês"; cfg["B7"]="=MATCH(B6,$T$5:$T$16,0)"
cfg["A8"]="Data de referência (hoje)"; cfg["B8"]=dados.HOJE
cfg["A9"]="Painel conta horas disponíveis até"; cfg["B9"]="=MIN(DATE(B5,B7+1,0),B8-1)"
cfg["C9"]="Capacidade E horas atendidas usam esta mesma data de corte, por isso o dia de hoje fica fora dos dois: contar o dia em andamento de um lado só distorce a ocupação."
cfg["A10"]="Horas por turno (padrão)"; cfg["B10"]=dados.HORAS_TURNO
for r in range(4,11): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"],center=True); inp(cfg["B6"],center=True); calc(cfg["B7"]); inp(cfg["B8"],DATA); calc(cfg["B9"],DATA); inp(cfg["B10"],"0",center=True)
cfg["C8"]="Deixe =HOJE() para acompanhar o dia; troque por uma data para simular outro dia."; nota(cfg["C8"])
cfg["C9"]="Ontem, ou o fim do mês do painel se ele já passou: as horas disponíveis só contam dias que já aconteceram."; nota(cfg["C9"])
cfg["T4"]="Meses"; rotulo(cfg["T4"])
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=20,value=m).font=F(size=10,color=TINTA)
dv=lista("=Config!$T$5:$T$16",allow_blank=False); dv.add("B6"); cfg.add_data_validation(dv)
# listas
cfg["D4"]="Profissionais (até 8)"; cfg["E4"]="Especialidade"; cfg["F4"]="Salas (até 6)"; cfg["H4"]="Pagadores (até 6)"; cfg["J4"]="Procedimentos (até 12)"; cfg["K4"]="Minutos"; cfg["L4"]="Retorno em (dias)"
for c in ("D4","E4","F4","H4","J4","K4","L4"): rotulo(cfg[c])
cfg["M3"]="Tabela de preços por pagador (R$)"; rotulo(cfg["M3"])
for j in range(NPAG): cfg.cell(row=4,column=13+j,value=f'=IF($H${5+j}="","",$H${5+j})'); rotulo(cfg.cell(row=4,column=13+j))
for i in range(NPROF): inp(cfg.cell(row=5+i,column=4)); inp(cfg.cell(row=5+i,column=5))
for i in range(NSALA): inp(cfg.cell(row=5+i,column=6))
for i in range(NPAG): inp(cfg.cell(row=5+i,column=8))
for i in range(NPROC):
    inp(cfg.cell(row=5+i,column=10)); inp(cfg.cell(row=5+i,column=11),"0",center=True); inp(cfg.cell(row=5+i,column=12),"0",center=True)
    for j in range(NPAG): inp(cfg.cell(row=5+i,column=13+j),BRL0,center=True)
cfg["D14"]="Preencha as listas de cima para baixo, sem pular linha: as listas suspensas da Agenda param na última linha preenchida. Retorno em (dias) = prazo em que se espera o paciente de volta (0 = não se aplica); a planilha 02 usa isso na lista de retorno."; nota(cfg["D14"])
cfg["D15"]="Tabela de preços: valor de cada procedimento para cada pagador. Célula vazia = não credenciado. A Agenda busca o valor aqui. COPIE DA PLANILHA 08 (Tabela de preços): ela é a fonte única da tabela no kit; 06 e 07 também copiam de lá. Mudou um preço? Atualize a 08 primeiro e depois 06, 07 e esta Config."; nota(cfg["D15"])
for i,(n,pap,tipo,v,h) in enumerate(dados.PESSOAS[:3]): cfg.cell(row=5+i,column=4,value=n); cfg.cell(row=5+i,column=5,value=dados.ESPECIALIDADE[n])
for i,s in enumerate(dados.SALAS): cfg.cell(row=5+i,column=6,value=s)
for i,pg in enumerate(dados.PAGADORES): cfg.cell(row=5+i,column=8,value=pg)
for i,(p,d,m,r) in enumerate(dados.PROCEDIMENTOS):
    cfg.cell(row=5+i,column=10,value=p); cfg.cell(row=5+i,column=11,value=d); cfg.cell(row=5+i,column=12,value=r)
    for j,pg in enumerate(dados.PAGADORES):
        v=dados.preco(p,pg)
        if v is not None: cfg.cell(row=5+i,column=13+j,value=v)
# turnos
cfg["A18"]="Turnos da semana (até 24): quem atende, em que dia, período e sala"; rotulo(cfg["A18"])
hdr(cfg,19,["Profissional","Dia da semana","Período","Sala","Início","Horas","Horas disponíveis no mês (até o limite)"],height=32)
for r in range(T0,TN+1):
    for c in (1,2,3,4,5,6): inp(cfg.cell(row=r,column=c),center=(c>1))
    cfg.cell(row=r,column=5).number_format="hh:mm"
    cfg.cell(row=r,column=7,value=f'=IF(A{r}="","",IF(F{r}="",$B$10,F{r})*IFERROR(INDEX($J$45:$J$50,MATCH(B{r},$I$45:$I$50,0)),0))'); calc(cfg.cell(row=r,column=7),"0")
for i,(prof,wd,per,sala,h0) in enumerate(dados.TURNOS):
    r=T0+i; cfg.cell(row=r,column=1,value=prof); cfg.cell(row=r,column=2,value=dados.DIAS_SEMANA[wd]); cfg.cell(row=r,column=3,value=per); cfg.cell(row=r,column=4,value=sala); cfg.cell(row=r,column=5,value=time(h0,0)); cfg.cell(row=r,column=6,value=dados.HORAS_TURNO)
dvd=lista('"Segunda,Terça,Quarta,Quinta,Sexta,Sábado"'); dvd.add(f"B{T0}:B{TN}")
dvp=lista('"Manhã,Tarde,Noite"'); dvp.add(f"C{T0}:C{TN}")
dvpr=lista(off("Config","D",5,4+NPROF)); dvpr.add(f"A{T0}:A{TN}")
dvsa=lista(off("Config","F",5,4+NSALA)); dvsa.add(f"D{T0}:D{TN}")
for dv in (dvd,dvp,dvpr,dvsa): cfg.add_data_validation(dv)
cfg["I18"]="Feriados e dias sem atendimento (até 20)"; rotulo(cfg["I18"])
for i in range(NFER): inp(cfg.cell(row=19+i,column=9),DATA,center=True)
for i,d in enumerate(dados.FERIADOS): cfg.cell(row=19+i,column=9,value=d)
cfg["I43"]="Dias úteis do mês do painel (até o limite), por dia da semana"; rotulo(cfg["I43"])
hdr(cfg,44,["Dia","Dias no mês"],start=9)
for i,dia in enumerate(["Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]):
    r=45+i; cfg.cell(row=r,column=9,value=dia); calc(cfg.cell(row=r,column=9),center=False)
    cfg.cell(row=r,column=10,value=f'=COUNTIF($C${X0}:$C${XN},I{r})'); calc(cfg.cell(row=r,column=10),"0")
cfg.cell(row=X0-2,column=1,value="Auxiliar: dias do mês do painel (calculado; sábado só conta se houver turno de sábado)"); nota(cfg.cell(row=X0-2,column=1))
hdr(cfg,X0-1,["Dia","Data","Conta? (dia da semana)"])
for i in range(31):
    r=X0+i
    cfg.cell(row=r,column=1,value=i+1); calc(cfg.cell(row=r,column=1))
    cfg.cell(row=r,column=2,value=f'=IF({i+1}>DAY(DATE($B$5,$B$7+1,0)),"",DATE($B$5,$B$7,{i+1}))'); calc(cfg.cell(row=r,column=2),DATA)
    cfg.cell(row=r,column=3,value=f'=IF(B{r}="","",IF(OR(B{r}>$B$9,WEEKDAY(B{r},2)=7,COUNTIF($I$19:$I${18+NFER},B{r})>0),"",CHOOSE(WEEKDAY(B{r},2),"Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo")))'); calc(cfg.cell(row=r,column=3))
widths(cfg,(30,16,12,26,18,12,3,16,14,22,9,12,12,12,12,12,12,12,3,12)); cfg.sheet_view.showGridLines=False
PROF_L=off("Config","D",5,4+NPROF); SALA_L=off("Config","F",5,4+NSALA); PAG_L=off("Config","H",5,4+NPAG); PROC_L=off("Config","J",5,4+NPROC)
PROCS=f"Config!$J$5:$J${4+NPROC}"; DURS=f"Config!$K$5:$K${4+NPROC}"; PAGS=f"Config!$H$5:$H${4+NPAG}"; PRECOS=f"Config!$M$5:$R${4+NPROC}"
# ---------- Pacientes ----------
pc=wb.create_sheet("Pacientes")
titulo(pc,"Pacientes","Uma linha por paciente: nome, pagador (particular ou convênio), profissional principal e contato. Só dados de gestão; nada clínico. As colunas brancas vêm da Agenda.",merge_to="I")
hdr(pc,4,["Paciente","Pagador","Profissional principal","Contato","Observação","Atendimentos realizados","Faltas","Último atendimento","Próximo agendado"],height=32)
AA=f"Agenda!$A${R0}:$A${RN}"; AE=f"Agenda!$E${R0}:$E${RN}"; AH=f"Agenda!$H${R0}:$H${RN}"
for r in range(R0,RP+1):
    for c in (1,2,3,4,5): inp(pc.cell(row=r,column=c),center=(c in (2,3)))
    pc.cell(row=r,column=6,value=f'=IF(A{r}="","",COUNTIFS({AE},A{r},{AH},"Realizado"))'); calc(pc.cell(row=r,column=6))
    pc.cell(row=r,column=7,value=f'=IF(A{r}="","",COUNTIFS({AE},A{r},{AH},"Falta"))'); calc(pc.cell(row=r,column=7))
    mx=f'SUMPRODUCT(MAX(({AE}=A{r})*({AH}="Realizado")*{AA}))'
    pc.cell(row=r,column=8,value=f'=IF(A{r}="","",IF({mx}=0,"",{mx}))'); calc(pc.cell(row=r,column=8),DATA)
    cond=f'(({AE}=A{r})*(({AH}="Agendado")+({AH}="Confirmado")))'
    mn=f'SUMPRODUCT(MIN({cond}*{AA}+(1-{cond})*1E+10))'
    pc.cell(row=r,column=9,value=f'=IF(A{r}="","",IF({mn}>=1E+10,"",{mn}))'); calc(pc.cell(row=r,column=9),DATA)
dvpg=lista(PAG_L,strict=True); dvpg.add(f"B{R0}:B{RP}"); dvpp=lista(PROF_L,strict=True); dvpp.add(f"C{R0}:C{RP}")
for dv in (dvpg,dvpp): pc.add_data_validation(dv)
pc.cell(row=RP+2,column=1,value="Esta aba é a fonte do cadastro de pacientes do kit: a planilha 14 (parcelas) copia os nomes daqui. Contato fictício no exemplo. Não guarde aqui nada além do necessário para agendar e cobrar.").font=F(size=9,color=LILAS)
widths(pc,(28,14,24,16,30,13,9,14,14)); pc.freeze_panes="B5"; pc.sheet_view.showGridLines=False; pc.auto_filter.ref=f"A4:I{RP}"
for i,p in enumerate(dados.PACIENTES):
    r=R0+i; pc.cell(row=r,column=1,value=p["nome"]); pc.cell(row=r,column=2,value=p["convenio"]); pc.cell(row=r,column=3,value=p["profissional"]); pc.cell(row=r,column=4,value=p["contato"])
PAC_L=off("Pacientes","A",R0,RP)
# ---------- Agenda ----------
ag=wb.create_sheet("Agenda")
titulo(ag,"Agenda","Uma linha por horário marcado. Preencha o amarelo; duração, valor, mês e período são calculados. Situação: Agendado, Confirmado, Realizado, Falta, Cancelado ou Remarcado. Esta aba é a fonte da agenda do kit (02 e 16 copiam daqui).",merge_to="R")
hdr(ag,4,["Data","Hora","Profissional","Sala","Paciente","Pagador","Procedimento","Situação","Forma de pagamento","Parcelas (cartão)","Observação","Minutos","Valor (R$)","Mês","Ano","Dia da semana","Período","Horas atendidas"],height=32)
for r in range(R0,RN+1):
    for c in range(1,12): inp(ag.cell(row=r,column=c),center=(c not in (5,11)))
    ag.cell(row=r,column=1).number_format=DATA; ag.cell(row=r,column=2).number_format="hh:mm"
    ag.cell(row=r,column=12,value=f'=IF(G{r}="","",IFERROR(INDEX({DURS},MATCH(G{r},{PROCS},0)),""))'); calc(ag.cell(row=r,column=12),"0")
    ag.cell(row=r,column=13,value=f'=IF(OR(G{r}="",F{r}=""),"",IFERROR(INDEX({PRECOS},MATCH(G{r},{PROCS},0),MATCH(F{r},{PAGS},0)),""))'); calc(ag.cell(row=r,column=13),BRL0)
    ag.cell(row=r,column=14,value=f'=IF(A{r}="","",MONTH(A{r}))'); calc(ag.cell(row=r,column=14))
    ag.cell(row=r,column=15,value=f'=IF(A{r}="","",YEAR(A{r}))'); calc(ag.cell(row=r,column=15))
    ag.cell(row=r,column=16,value=f'=IF(A{r}="","",CHOOSE(WEEKDAY(A{r},2),"Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"))'); calc(ag.cell(row=r,column=16))
    ag.cell(row=r,column=17,value=f'=IF(B{r}="","",IF(B{r}<TIME(12,0,0),"Manhã",IF(B{r}<TIME(18,0,0),"Tarde","Noite")))'); calc(ag.cell(row=r,column=17))
    # o mesmo corte de data da capacidade (Config!$B$9): numerador e denominador da
    # ocupação precisam cobrir o mesmo período, senão a ocupação sobe sozinha
    ag.cell(row=r,column=18,value=f'=IF(AND(H{r}="Realizado",L{r}<>"",A{r}<=Config!$B$9),L{r}/60,0)'); calc(ag.cell(row=r,column=18),"0.00")
dvs=[(lista(PROF_L),f"C{R0}:C{RN}"),(lista(SALA_L),f"D{R0}:D{RN}"),(lista(PAC_L,strict=True),f"E{R0}:E{RN}"),(lista(PAG_L),f"F{R0}:F{RN}"),(lista(PROC_L),f"G{R0}:G{RN}"),
     (lista('"'+",".join(dados.SITUACOES)+'"'),f"H{R0}:H{RN}"),(lista('"Pix,Dinheiro,Cartão de débito,Cartão de crédito,A prazo,Convênio,Sem cobrança"'),f"I{R0}:I{RN}"),
     (DataValidation(type="whole",operator="between",formula1="1",formula2="12",allow_blank=True,showErrorMessage=True),f"J{R0}:J{RN}"),
     (DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True,showErrorMessage=True),f"A{R0}:A{RN}")]
for dv,rng in dvs: dv.add(rng); ag.add_data_validation(dv)
ag.conditional_formatting.add(f"A{R0}:R{RN}", FormulaRule(formula=[f'$H{R0}="Realizado"'], font=F(color=VERDE_T,size=10)))
ag.conditional_formatting.add(f"A{R0}:R{RN}", FormulaRule(formula=[f'$H{R0}="Falta"'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
ag.conditional_formatting.add(f"A{R0}:R{RN}", FormulaRule(formula=[f'OR($H{R0}="Cancelado",$H{R0}="Remarcado")'], font=F(color="8A86A0",size=10)))
ag.conditional_formatting.add(f"A{R0}:R{RN}", FormulaRule(formula=[f'OR($H{R0}="Agendado",$H{R0}="Confirmado")'], fill=fill(LAVANDA)))
ag.conditional_formatting.add(f"I{R0}:I{RN}", FormulaRule(formula=[f'AND($H{R0}="Realizado",$M{R0}>0,$I{R0}="")'], fill=fill(VERM)))
ag.cell(row=RN+2,column=1,value="Verde: realizado. Vermelho: falta. Lilás: agendado ou confirmado. Cinza: cancelado ou remarcado. Forma de pagamento em vermelho: atendimento realizado com valor e sem forma. Convênio: escolha \"Convênio\" (a guia vai para a planilha 13). A prazo: a parcela vai para a planilha 14. Cartão: a conciliação é a planilha 16.").font=F(size=9,color=LILAS)
ag.cell(row=RN+3,column=1,value=f"No exemplo, a agenda na planilha começou em 01/06/2026 (antes, a recepção só fechava o caixa do dia). Datas até 11/09/2026 são fixas; de hoje em diante são relativas a hoje (=HOJE()+n).").font=F(size=9,color=LILAS)
ag.cell(row=RN+4,column=1,value=f"Esta aba tem {N} linhas ({R0} a {RN}): cerca de 300 atendimentos por mês cabem 10 meses. Para estender, desproteja a aba (Revisar > Desproteger), selecione a última linha inteira, copie e cole nas linhas seguintes (as fórmulas das colunas brancas vêm juntas) e depois troque {RN} pelo novo número final nas fórmulas do Painel (Localizar e substituir). Ou comece um arquivo por ano, que é o mais simples.").font=F(size=9,color=LILAS)
widths(ag,(11,7,22,8,26,12,18,11,17,9,26,8,11,6,6,11,8,9)); ag.freeze_panes="F5"; ag.sheet_view.showGridLines=False; ag.auto_filter.ref=f"A4:R{RN}"
assert len(dados.AGENDA)<=N
for i,r_ in enumerate(dados.AGENDA):
    r=R0+i
    ag.cell(row=r,column=1,value=r_["data"] if r_["data"]<dados.HOJE else dados.prazo_formula(dados.dias(r_["data"])))
    ag.cell(row=r,column=2,value=time(r_["hora"]//60,r_["hora"]%60))
    for c,k in ((3,"profissional"),(4,"sala"),(5,"paciente"),(6,"pagador"),(7,"procedimento"),(8,"situacao")): ag.cell(row=r,column=c,value=r_[k])
    if r_["forma"]: ag.cell(row=r,column=9,value=r_["forma"])
    if r_["parcelas"]: ag.cell(row=r,column=10,value=r_["parcelas"])
    if r_["checkup"]: ag.cell(row=r,column=11,value="Check-up cardiológico (consulta + ECG + teste ergométrico)")
    elif r_["situacao"]=="Remarcado": ag.cell(row=r,column=11,value="Paciente pediu outra data")
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
titulo(p,'=Config!$B$4&" · Agenda e ocupação · "&Config!$B$6&" de "&Config!$B$5',"Nada para digitar aqui. Escolha o mês em Config; tudo vem de Agenda e dos turnos. Ocupação = horas atendidas ÷ horas disponíveis (só dias já passados).",merge_to="L")
M="Config!$B$7"; Y="Config!$B$5"; LIM="Config!$B$9"
AC=f"Agenda!$C${R0}:$C${RN}"; AD=f"Agenda!$D${R0}:$D${RN}"; AF=f"Agenda!$F${R0}:$F${RN}"; AG_=f"Agenda!$G${R0}:$G${RN}"; AM=f"Agenda!$M${R0}:$M${RN}"
AN=f"Agenda!$N${R0}:$N${RN}"; AO=f"Agenda!$O${R0}:$O${RN}"; AP=f"Agenda!$P${R0}:$P${RN}"; AQ=f"Agenda!$Q${R0}:$Q${RN}"; AR=f"Agenda!$R${R0}:$R${RN}"; AL=f"Agenda!$L${R0}:$L${RN}"
TA=f"Config!$A${T0}:$A${TN}"; TB=f"Config!$B${T0}:$B${TN}"; TC=f"Config!$C${T0}:$C${TN}"; TD=f"Config!$D${T0}:$D${TN}"; TG=f"Config!$G${T0}:$G${TN}"
MES=f"{AN},{M},{AO},{Y}"
kpi(p,4,1,"Horas disponíveis (até ontem)",f"=SUM({TG})",LAVANDA,UVA,fmt="#,##0.0")
kpi(p,4,3,"Horas atendidas",f"=SUMIFS({AR},{MES})",VERDE,VERDE_T,fmt="#,##0.0")
kpi(p,4,5,"Ocupação",'=IF(A5=0,"",C5/A5)',SOL,UVA,fmt=PCT)
kpi(p,4,7,"Horas vazias",'=IF(A5=0,"",MAX(0,A5-C5))',VERM,VERM_T,fmt="#,##0.0")
kpi(p,4,9,"Faltas no mês",f'=COUNTIFS({AH},"Falta",{MES})',VERM,VERM_T,fmt="0")
kpi(p,4,11,"Produção (R$)",f'=SUMIFS({AM},{AH},"Realizado",{MES})',LAVANDA,UVA,fmt=BRL0)
p["A7"]="Horas vazias = disponíveis − atendidas: inclui faltas, cancelamentos e horários que ninguém marcou. Produção = valor de tabela dos atendimentos realizados (particular e convênio), antes de glosa e taxas; o que entrou de fato está no caixa (09)."; nota(p["A7"]); p.merge_cells("A7:L7"); p["A7"].alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[7].height=30
# por profissional
p["A9"]="Por profissional"; p["A9"].font=F(bold=True,size=13,color=UVA)
hdr(p,10,["Profissional","Horas disponíveis","Horas atendidas","Ocupação","Realizados","Faltas","Taxa de falta","Produção (R$)","Barra"]); p.merge_cells("I10:L10")
for i in range(NPROF):
    r=11+i; src=f"Config!$D${5+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",SUMIFS({TG},{TA},{src}))'); calc(p.cell(row=r,column=2),"#,##0.0")
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({AR},{AC},{src},{MES}))'); calc(p.cell(row=r,column=3),"#,##0.0")
    p.cell(row=r,column=4,value=f'=IF(OR({src}="",B{r}=0),"",C{r}/B{r})'); calc(p.cell(row=r,column=4),PCT)
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS({AC},{src},{AH},"Realizado",{MES}))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF({src}="","",COUNTIFS({AC},{src},{AH},"Falta",{MES}))'); calc(p.cell(row=r,column=6))
    p.cell(row=r,column=7,value=f'=IF({src}="","",IF(E{r}+F{r}=0,"",F{r}/(E{r}+F{r})))'); calc(p.cell(row=r,column=7),PCT)
    p.cell(row=r,column=8,value=f'=IF({src}="","",SUMIFS({AM},{AC},{src},{AH},"Realizado",{MES}))'); calc(p.cell(row=r,column=8),BRL0)
    p.cell(row=r,column=9,value=f'=IF(D{r}="","",REPT("█",ROUND(MIN(1,D{r})*30,0)))'); p.cell(row=r,column=9).font=F(size=10,color=LILAS); p.cell(row=r,column=9).border=borda; p.merge_cells(start_row=r,start_column=9,end_row=r,end_column=12)
p.conditional_formatting.add(f"D11:D{10+NPROF}", FormulaRule(formula=['AND(ISNUMBER(D11),D11<0.6)'], fill=fill(AMARELO)))
p.conditional_formatting.add(f"G11:G{10+NPROF}", FormulaRule(formula=['AND(ISNUMBER(G11),G11>0.1)'], font=F(color="C8402E",size=10,bold=True)))
p.cell(row=11+NPROF,column=1,value="Ocupação abaixo de 60 % fica em amarelo; taxa de falta acima de 10 % em vermelho. Taxa de falta = faltas ÷ (faltas + realizados), a mesma conta da planilha 02.").font=F(size=9,color=LILAS)
# por sala
S0=11+NPROF+2
p.cell(row=S0,column=1,value="Por sala").font=F(bold=True,size=13,color=UVA)
hdr(p,S0+1,["Sala","Horas disponíveis","Horas atendidas","Ocupação","Horas vazias","Turnos por semana"])
for i in range(NSALA):
    r=S0+2+i; src=f"Config!$F${5+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",SUMIFS({TG},{TD},{src}))'); calc(p.cell(row=r,column=2),"#,##0.0")
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({AR},{AD},{src},{MES}))'); calc(p.cell(row=r,column=3),"#,##0.0")
    p.cell(row=r,column=4,value=f'=IF(OR({src}="",B{r}=0),"",C{r}/B{r})'); calc(p.cell(row=r,column=4),PCT)
    p.cell(row=r,column=5,value=f'=IF(B{r}="","",MAX(0,B{r}-C{r}))'); calc(p.cell(row=r,column=5),"#,##0.0")
    p.cell(row=r,column=6,value=f'=IF({src}="","",COUNTIFS({TD},{src},{TA},"<>"))'); calc(p.cell(row=r,column=6))
p.cell(row=S0+2+NSALA,column=1,value="Sala com poucos turnos por semana é capacidade parada: cabe outro profissional por repasse (planilha 11) sem aumentar o aluguel.").font=F(size=9,color=LILAS)
# por dia da semana e período
D0=S0+2+NSALA+3
p.cell(row=D0,column=1,value="Por dia da semana e período (onde a agenda esvazia)").font=F(bold=True,size=13,color=UVA)
hdr(p,D0+1,["Dia","Manhã · disponíveis","Manhã · atendidas","Manhã · ocupação","Tarde · disponíveis","Tarde · atendidas","Tarde · ocupação","Faltas no dia"],height=32)
for i,dia in enumerate(["Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]):
    r=D0+2+i
    p.cell(row=r,column=1,value=dia); calc(p.cell(row=r,column=1),center=False)
    for j,per in enumerate(("Manhã","Tarde")):
        c0=2+3*j
        p.cell(row=r,column=c0,value=f'=SUMIFS({TG},{TB},A{r},{TC},"{per}")'); calc(p.cell(row=r,column=c0),"#,##0.0")
        p.cell(row=r,column=c0+1,value=f'=SUMIFS({AR},{AP},A{r},{AQ},"{per}",{MES})'); calc(p.cell(row=r,column=c0+1),"#,##0.0")
        p.cell(row=r,column=c0+2,value=f'=IF({L(c0)}{r}=0,"",{L(c0+1)}{r}/{L(c0)}{r})'); calc(p.cell(row=r,column=c0+2),PCT)
    p.cell(row=r,column=8,value=f'=COUNTIFS({AP},A{r},{AH},"Falta",{MES})'); calc(p.cell(row=r,column=8))
p.conditional_formatting.add(f"A{D0+2}:H{D0+7}", FormulaRule(formula=[f'AND($B{D0+2}=0,$E{D0+2}=0)'], font=F(color="B0A6C4",size=10)))
p.cell(row=D0+8,column=1,value="Dia em cinza: nenhum turno disponível no período contado. As horas disponíveis só contam dias já passados e pulam os feriados de Config, então num mês em andamento um dia da semana pode aparecer zerado sem que a clínica tenha fechado. No exemplo (setembro), a segunda aparece assim: 07/09 é feriado e 14/09 é hoje, e as duas segundas anteriores ao mês não contam — Dra. Carolina e Dr. Paulo atendem normalmente às segundas.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=D0+8,start_column=1,end_row=D0+8,end_column=12); p.cell(row=D0+8,column=1).alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[D0+8].height=30
for col in ("D","G"): p.conditional_formatting.add(f"{col}{D0+2}:{col}{D0+7}", FormulaRule(formula=[f'AND(ISNUMBER({col}{D0+2}),{col}{D0+2}<0.6)'], fill=fill(AMARELO)))
# por procedimento e por pagador
P0=D0+10
p.cell(row=P0,column=1,value="Por procedimento").font=F(bold=True,size=13,color=UVA)
hdr(p,P0+1,["Procedimento","Realizados","Horas","Produção (R$)","Valor médio (R$)"])
for i in range(NPROC):
    r=P0+2+i; src=f"Config!$J${5+i}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({AG_},{src},{AH},"Realizado",{MES}))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({AR},{AG_},{src},{MES}))'); calc(p.cell(row=r,column=3),"#,##0.0")
    p.cell(row=r,column=4,value=f'=IF({src}="","",SUMIFS({AM},{AG_},{src},{AH},"Realizado",{MES}))'); calc(p.cell(row=r,column=4),BRL0)
    p.cell(row=r,column=5,value=f'=IF(OR({src}="",B{r}=0),"",D{r}/B{r})'); calc(p.cell(row=r,column=5),BRL0)
hdr(p,P0+1,["Pagador","Realizados","Faltas","Taxa de falta","Produção (R$)","Valor médio (R$)","% da produção"],start=7)
for i in range(NPAG):
    r=P0+2+i; src=f"Config!$H${5+i}"
    p.cell(row=r,column=7,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=7),center=False)
    p.cell(row=r,column=8,value=f'=IF({src}="","",COUNTIFS({AF},{src},{AH},"Realizado",{MES}))'); calc(p.cell(row=r,column=8))
    p.cell(row=r,column=9,value=f'=IF({src}="","",COUNTIFS({AF},{src},{AH},"Falta",{MES}))'); calc(p.cell(row=r,column=9))
    p.cell(row=r,column=10,value=f'=IF({src}="","",IF(H{r}+I{r}=0,"",I{r}/(H{r}+I{r})))'); calc(p.cell(row=r,column=10),PCT)
    p.cell(row=r,column=11,value=f'=IF({src}="","",SUMIFS({AM},{AF},{src},{AH},"Realizado",{MES}))'); calc(p.cell(row=r,column=11),BRL0)
    p.cell(row=r,column=12,value=f'=IF(OR({src}="",H{r}=0),"",K{r}/H{r})'); calc(p.cell(row=r,column=12),BRL0)
    p.cell(row=r,column=13,value=f'=IF(OR({src}="",$K$5=0),"",K{r}/$K$5)'); calc(p.cell(row=r,column=13),PCT)
p.cell(row=P0+2+NPROC,column=1,value="Retorno tem valor zero (incluído na consulta): ocupa agenda e não produz. A planilha 06 embute esse tempo no preço da consulta.").font=F(size=9,color=LILAS)
# próximos 7 dias
Q0=P0+2+NPROC+3
p.cell(row=Q0,column=1,value="Próximos 7 dias (a partir de hoje)").font=F(bold=True,size=13,color=UVA)
hdr(p,Q0+1,["Dia","Data","Agendados","Confirmados","Horas marcadas","Horas de turno","Vagas (horas)"])
for d in range(7):
    r=Q0+2+d
    p.cell(row=r,column=2,value=f"=Config!$B$8+{d}"); calc(p.cell(row=r,column=2),DATA)
    p.cell(row=r,column=1,value=f'=CHOOSE(WEEKDAY(B{r},2),"Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo")'); calc(p.cell(row=r,column=1))
    p.cell(row=r,column=3,value=f'=COUNTIFS({AA},B{r},{AH},"Agendado")'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'=COUNTIFS({AA},B{r},{AH},"Confirmado")'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=(SUMIFS({AL},{AA},B{r},{AH},"Agendado")+SUMIFS({AL},{AA},B{r},{AH},"Confirmado"))/60'); calc(p.cell(row=r,column=5),"#,##0.0")
    p.cell(row=r,column=6,value=f'=IF(COUNTIF(Config!$I$19:$I${18+NFER},B{r})>0,0,SUMPRODUCT(({TB}=A{r})*({TA}<>"")*IF({TG}="",0,1)*IF(Config!$F${T0}:$F${TN}="",Config!$B$10,Config!$F${T0}:$F${TN})))'); calc(p.cell(row=r,column=6),"#,##0.0")
    p.cell(row=r,column=7,value=f'=MAX(0,F{r}-E{r})'); calc(p.cell(row=r,column=7),"#,##0.0")
p.conditional_formatting.add(f"A{Q0+2}:G{Q0+8}", FormulaRule(formula=[f'$F{Q0+2}=0'], font=F(color="B0A6C4",size=10)))
p.conditional_formatting.add(f"G{Q0+2}:G{Q0+8}", FormulaRule(formula=[f'AND($F{Q0+2}>0,G{Q0+2}>=$F{Q0+2}*0.4)'], fill=fill(AMARELO)))
p.cell(row=Q0+9,column=1,value="Vagas em amarelo: mais de 40 % do turno livre. É a lista para a recepção oferecer horários à lista de retorno (planilha 02) e aos orçamentos aprovados (15). A planilha avisa; a agenda é da clínica.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=Q0+9,start_column=1,end_row=Q0+9,end_column=12)
bc=BarChart(); bc.type="col"; bc.grouping="clustered"; bc.height=7; bc.width=14; bc.title="Horas disponíveis × atendidas"; bc.style=2
bc.add_data(Reference(p,min_col=2,max_col=3,min_row=10,max_row=10+len(dados.MEDICOS)),titles_from_data=True); bc.set_categories(Reference(p,min_col=1,min_row=11,max_row=10+len(dados.MEDICOS)))
bc.series[0].graphicalProperties.solidFill="B89BE0"; bc.series[1].graphicalProperties.solidFill=UVA; bc.legend.position="b"; bc.y_axis.majorGridlines=None
p.add_chart(bc,f"I{S0}")
widths(p,(26,14,14,12,12,11,12,14,13,13,14,13,12)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
como_usar(wb,"Agenda e ocupação por profissional e sala",[
 ("O que esta planilha faz","Registra cada horário da agenda (quem atende, em que sala, qual paciente, pagador e procedimento, e o que aconteceu) e mede o que ninguém mede: quantas horas a clínica tinha disponíveis, quantas foram atendidas, a ocupação por profissional, por sala e por dia da semana, as faltas e a produção do mês."),
 ("Passo 1","Em Config, cadastre profissionais, salas, pagadores (particular e convênios), procedimentos com duração e a tabela de preços por pagador. Depois os turnos da semana (quem atende em que dia, período e sala) e os feriados. Preencha as listas de cima para baixo, sem pular linha."),
 ("Passo 2","Em Pacientes, uma linha por paciente: nome, pagador, profissional principal e contato. Só o necessário para agendar e cobrar; nada clínico. Esta aba é a fonte do cadastro de pacientes (a 14 copia daqui)."),
 ("Passo 3","Em Agenda, uma linha por horário: data, hora, profissional, sala, paciente, pagador, procedimento e situação. No fim do dia, a recepção marca Realizado, Falta, Cancelado ou Remarcado e a forma de pagamento (a planilha 04 tem esse passo no fechamento do dia)."),
 ("Passo 4","Em Painel, escolha o mês em Config: horas disponíveis (só dias já passados), atendidas, ocupação, horas vazias, faltas e produção; por profissional, por sala, por dia da semana e período, por procedimento e por pagador; e os próximos 7 dias com as vagas."),
 ("Rotina de segunda","4 minutos: olhar as vagas dos próximos 7 dias e a ocupação da semana. Confirmar os agendados da semana é a rotina seguinte (mais 4 minutos). As duas estão na planilha 03 · Rotina da semana, que soma 12 minutos na segunda e 18 na sexta."),
 ("Limite e como estender","A aba Agenda tem 3.000 linhas (5 a 3004): com cerca de 300 atendimentos por mês, dá 10 meses. Quando chegar perto do fim, copie a última linha preenchida para baixo (a aba precisa ser desprotegida em Revisar > Desproteger planilha) e ajuste o número final nas fórmulas do Painel, ou comece um arquivo por ano — é o mais simples e mantém o histórico separado. A aba Pacientes tem 400 linhas."),
 ("Ligação com as outras planilhas","A produção por profissional alimenta o repasse (11); os atendimentos de convênio viram guias (13); os a prazo, parcelas (14); os no cartão, a conciliação (16). O Painel da clínica (17) copia horas atendidas, ocupação e faltas daqui. A planilha 02 copia esta Agenda para medir faltas e montar a lista de retorno."),
 ("Com a IA","Copie \"Por dia da semana e período\" e \"Por profissional\" e use o prompt \"Agenda 01 · Onde a agenda esvazia\" da biblioteca do kit. Nunca cole a aba Pacientes ou a Agenda com nomes na IA: use só as tabelas do Painel."),
])
proteger(wb); salvar(wb,"01-agenda-e-ocupacao.xlsx","Agenda e ocupação · Kit de Gestão para Médicos")
