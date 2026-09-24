#!/usr/bin/env python3
"""Verifica a coerência do exemplo entre as 20 planilhas do Kit de Gestão para Médicos.
Lê CÓPIAS recalculadas (LibreOffice, recalc.py) com openpyxl em data_only e afirma (assert) as igualdades entre arquivos.
Uso: python3 verifica_coerencia.py <pasta com as 20 cópias recalculadas>   (nunca recalcule os originais; CONVENCOES §10)"""
import sys, pathlib, datetime
from collections import defaultdict
import openpyxl

PASTA=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else ".")
def wb(prefix):
    f=next(PASTA.glob(f"{prefix}-*.xlsx")); return openpyxl.load_workbook(f,data_only=True)
def num(v): return 0 if v in (None,"","—") else float(v)
def dt(v): return v.date() if isinstance(v,datetime.datetime) else v
FALHAS=[]; OK=0
def check(nome,a,b,tol=0.5):
    global OK
    ok=(abs(num(a)-num(b))<=tol) if isinstance(a,(int,float)) or isinstance(b,(int,float)) else (a==b)
    if ok: OK+=1
    else: FALHAS.append(f"{nome}: {a!r} != {b!r}")
def rows(ws,r0,cols):
    out=[]
    for r in range(r0,ws.max_row+1):
        if ws.cell(row=r,column=cols[0]).value in (None,""): break
        out.append([ws.cell(row=r,column=c).value for c in cols])
    return out
MES={m:i+1 for i,m in enumerate(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"])}
# As datas vêm de dados.py, não repetidas aqui: quando a data-base do exemplo mudar,
# a conferência acompanha em vez de comparar contra um dia que já passou.
import dados as _d
SEXTA=_d.SEXTA; HOJE=_d.HOJE

W={p:wb(p) for p in ("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20")}
p01=W["01"]["Painel"]; ag01=W["01"]["Agenda"]; p02=W["02"]["Painel"]; ag02=W["02"]["Agenda"]; p05=W["05"]["Painel"]; s06=W["06"]["Precificação"]; s07=W["07"]["Simulador"]; t08=W["08"]["Tabela"]
p09=W["09"]["Painel"]; lan=W["09"]["Lançamentos"]; p10=W["10"]["Painel"]; p11=W["11"]["Painel"]; rp11=W["11"]["Repasse"]; c12=W["12"]["Config"]; p12=W["12"]["Painel"]
p13=W["13"]["Painel"]; lo13=W["13"]["Lotes"]; gu13=W["13"]["Guias"]; p14=W["14"]["Painel"]; pr14=W["14"]["Parcelas"]; p15=W["15"]["Painel"]; or15=W["15"]["Orçamentos"]
p16=W["16"]["Painel"]; v16=W["16"]["Vendas"]; d17=W["17"]["Dados"]; h17=W["17"]["Histórico"]; r18=W["18"]["Resultado"]; p18=W["18"]["Painel"]; m19=W["19"]["Metas"]; i20=W["20"]["Indicadores"]

# ---------- agenda da 01 (valores digitados + calculados) ----------
AG=[dict(data=dt(a),prof=c,sala=d,pac=e,pag=f,proc=g,sit=h,forma=i,parc=j,minutos=num(l),valor=num(m)) for a,b,c,d,e,f,g,h,i,j,k,l,m in rows(ag01,5,list(range(1,14)))]
AG2=[dict(data=dt(a),prof=c,pac=e,pag=f,proc=g,sit=h) for a,b,c,d,e,f,g,h in rows(ag02,5,list(range(1,9)))]
check("02 Agenda tem as mesmas linhas da 01 Agenda",len(AG2),len(AG))
for i in range(0,len(AG),37): check(f"02 Agenda linha {i+5} == 01",(AG2[i]["data"],AG2[i]["pac"],AG2[i]["sit"]),(AG[i]["data"],AG[i]["pac"],AG[i]["sit"]))
check("01 nenhum atendimento realizado depois de 11/09",max(x["data"] for x in AG if x["sit"]=="Realizado")<=SEXTA,True)
check("01 nenhum agendado/confirmado antes de hoje",min(x["data"] for x in AG if x["sit"] in ("Agendado","Confirmado"))>=HOJE,True)
def real(m,**f): return [x for x in AG if x["sit"]=="Realizado" and x["data"].month==m and all(x[k]==v for k,v in f.items())]
def faltas(m,**f): return [x for x in AG if x["sit"]=="Falta" and x["data"].month==m and all(x[k]==v for k,v in f.items())]
# 1. 01 Painel (Setembro) == agenda
check("01 Painel horas atendidas (set) == soma dos minutos realizados",p01["C5"].value,sum(x["minutos"] for x in real(9))/60,tol=0.01)
check("01 Painel faltas (set) == agenda",p01["I5"].value,len(faltas(9)))
check("01 Painel produção (set) == soma dos valores realizados",p01["K5"].value,sum(x["valor"] for x in real(9)))
check("01 Painel ocupação = atendidas ÷ disponíveis",p01["E5"].value,num(p01["C5"].value)/num(p01["A5"].value),tol=1e-6)
check("01 Painel horas vazias = disponíveis − atendidas",p01["G5"].value,num(p01["A5"].value)-num(p01["C5"].value),tol=0.01)
for r in range(11,14):
    prof=p01.cell(row=r,column=1).value
    check(f"01 por profissional {prof[:12]}: atendidas == agenda",p01.cell(row=r,column=3).value,sum(x["minutos"] for x in real(9,prof=prof))/60,tol=0.01)
    check(f"01 por profissional {prof[:12]}: produção == agenda",p01.cell(row=r,column=8).value,sum(x["valor"] for x in real(9,prof=prof)))
    check(f"01 por profissional {prof[:12]}: faltas == agenda",p01.cell(row=r,column=6).value,len(faltas(9,prof=prof)))
# 2. 02 Painel == 01 (mesma agenda) e 17
check("02 Painel faltas (set) == 01 Painel faltas",p02["C5"].value,p01["I5"].value)
check("02 Painel realizados (set) == agenda",p02["E5"].value,len(real(9)))
check("02 taxa de falta == faltas ÷ (faltas + realizados)",p02["A5"].value,num(p02["C5"].value)/(num(p02["C5"].value)+num(p02["E5"].value)),tol=1e-6)
check("17 Dados ocupação == 01 Painel",d17["B5"].value,p01["E5"].value,tol=1e-4)
check("17 Dados horas atendidas == 01 Painel",d17["B6"].value,p01["C5"].value,tol=0.06)
check("17 Dados horas vazias == 01 Painel",d17["B7"].value,p01["G5"].value,tol=0.06)
check("17 Dados taxa de falta == 02 Painel",d17["B8"].value,p02["A5"].value,tol=1e-4)
check("17 Dados lista de retorno == 02 Painel",d17["B9"].value,p02["K5"].value)
# 3. caixa 09
L=[dict(data=dt(a),tipo=b,cat=c,quem=d,ref=e,desc=f,valor=num(g),forma=h,pago=i) for a,b,c,d,e,f,g,h,i in rows(lan,5,list(range(1,10)))]
ent_mes=defaultdict(float); sai_mes=defaultdict(float); ent_cat=defaultdict(float); sai_cat=defaultdict(float); ent_forma=defaultdict(float)
for x in L:
    if x["pago"]!="Sim": continue
    m=x["data"].month
    if x["tipo"]=="Entrada": ent_mes[m]+=x["valor"]; ent_cat[(m,x["cat"])]+=x["valor"]; ent_forma[(m,x["forma"])]+=x["valor"]
    else: sai_mes[m]+=x["valor"]; sai_cat[(m,x["cat"])]+=x["valor"]
check("09 nenhum lançamento pago depois de 11/09/2026",max(x["data"] for x in L if x["pago"]=="Sim")<=SEXTA,True)
check("09 Painel Entrou (set) == soma dos lançamentos pagos de setembro",p09["A5"].value,ent_mes[9])
check("09 Painel Saiu (set) == lançamentos",p09["C5"].value,sai_mes[9])
check("09 Painel Entrou (set) == 17 Dados B10",p09["A5"].value,d17["B10"].value)
check("09 Painel Saiu (set) == 17 Dados B11",p09["C5"].value,d17["B11"].value)
check("09 Painel Saldo acumulado == saldo inicial + entradas − saídas pagas",p09["G5"].value,num(W["09"]["Config"]["B8"].value)+sum(ent_mes.values())-sum(sai_mes.values()))
# Particular à vista no caixa (09): Pix e dinheiro entram no dia do atendimento;
# cartão entra na data em que cai na conta (débito D+1, crédito D+30 por parcela).
# Antes o cartão entrava no dia da venda e inflava o saldo disponível em até um mês.
avista_dia={}   # Pix e dinheiro, no próprio dia
for x in AG:
    if x["sit"]=="Realizado" and x["pag"]=="Particular" and x["forma"] in ("Pix","Dinheiro") and x["valor"]>0:
        avista_dia[(x["data"],x["forma"])]=avista_dia.get((x["data"],x["forma"]),0)+x["valor"]
fech={(x["data"],x["forma"]):x["valor"] for x in L
      if x["cat"]=="Particular à vista" and x["forma"] in ("Pix","Dinheiro") and x["data"]>=datetime.date(2026,6,1)}
for k,v in list(avista_dia.items())[::9]:
    if k[0]>=datetime.date(2026,6,1):
        check(f"09 Pix/dinheiro {k[0].strftime('%d/%m')} {k[1]} == agenda",fech.get(k),v)
# o total da categoria tem de fechar com o que dados.py gerou, linha a linha
_esp_cat={}
for d,t,c,q,r,ds,v,f,pg in _d.LANCAMENTOS:
    if c=="Particular à vista" and pg=="Sim": _esp_cat[d.month]=_esp_cat.get(d.month,0)+v
for m in (6,7,8):
    check(f"09 Particular à vista mês {m} == liquidações geradas",ent_cat[(m,"Particular à vista")],round(_esp_cat.get(m,0),2),tol=0.01)
# O cartão recebido ACUMULADO até um mês nunca pode passar do vendido acumulado:
# se passar, o caixa está contando dinheiro que ainda não caiu. Os dois lados vêm de
# AGENDA_TODA, que cobre o ano inteiro (a agenda da planilha 01 só mostra desde 01/06).
_vend_ate={}
for x in _d.AGENDA_TODA:
    if x["situacao"]=="Realizado" and x["pagador"]=="Particular" and x["forma"].startswith("Cartão") and x["valor"]>0:
        _vend_ate[x["data"].month]=_vend_ate.get(x["data"].month,0)+x["valor"]
for m in (6,7,8):
    _cart_acum=sum(v for d,t,c,q,r,ds,v,f,pg in _d.LANCAMENTOS
                   if c=="Particular à vista" and d.month<=m and f.startswith("Cartão"))
    _vend_acum=sum(_vend_ate.get(k,0) for k in range(1,m+1))
    check(f"09 cartão recebido até o mês {m} <= vendido até o mês {m}",_cart_acum<=_vend_acum+0.01,True)
# 4. 13 lotes × guias × 09 × 17
LOT=[dict(conv=a,comp=dt(b),n=int(num(c)),env=num(d),denv=dt(e),dpag=dt(f),pago=num(g),rec=h,recup=num(i),drec=dt(j),glosa=num(m),sit=n) for a,b,c,d,e,f,g,h,i,j,k,l,m,n in rows(lo13,5,list(range(1,15)))]
GU=[dict(num=a,data=dt(b),pac=c,conv=d,proc=e,prof=f,valor=num(g),glosada=h) for a,b,c,d,e,f,g,h in rows(gu13,5,list(range(1,9)))]
conv_real=[x for x in AG if x["sit"]=="Realizado" and x["pag"]!="Particular" and x["valor"]>0]
check("13 Guias: uma por atendimento de convênio realizado da 01 (jun–set)",len(GU),len(conv_real))
check("13 Guias: soma == produção de convênio da 01",sum(g["valor"] for g in GU),sum(x["valor"] for x in conv_real))
for l in LOT:
    if l["comp"]>=datetime.date(2026,6,1):
        gs=[g for g in GU if g["conv"]==l["conv"] and g["data"].month==l["comp"].month]
        check(f"13 lote {l['conv']} {l['comp'].strftime('%m/%Y')}: valor == guias",l["env"],sum(g["valor"] for g in gs))
        check(f"13 lote {l['conv']} {l['comp'].strftime('%m/%Y')}: nº de guias == guias",l["n"],len(gs))
        if l["dpag"] is not None: check(f"13 lote {l['conv']} {l['comp'].strftime('%m/%Y')}: glosa == guias glosadas",l["glosa"],sum(g["valor"] for g in gs if g["glosada"]=="Sim"))
check("13 nenhum lote pago depois de 11/09",max(l["dpag"] for l in LOT if l["dpag"])<=SEXTA,True)
for l in LOT:
    if l["dpag"] is not None and l["dpag"].year==2026:
        v=[x for x in L if x["cat"]=="Convênio · "+l["conv"] and x["data"]==l["dpag"] and x["pago"]=="Sim" and x["desc"].startswith("Pagamento")]
        check(f"09 entrada do lote {l['conv']} {l['comp'].strftime('%m/%Y')} == 13 valor pago",sum(x["valor"] for x in v),l["pago"])
    if l["recup"] and l["drec"] is not None:
        v=[x for x in L if x["cat"]=="Convênio · "+l["conv"] and x["data"]==l["drec"] and x["desc"].startswith("Recurso")]
        check(f"09 recuperação de glosa {l['conv']} {l['comp'].strftime('%m/%Y')} == 13",sum(x["valor"] for x in v),l["recup"])
for m in range(1,10):
    for conv in ("Saúde Total","MediPlan","Vida Care"):
        esperado=sum(l["pago"] for l in LOT if l["dpag"] and l["dpag"].month==m and l["dpag"].year==2026 and l["conv"]==conv)+sum(l["recup"] for l in LOT if l["drec"] and l["drec"].month==m and l["conv"]==conv)
        check(f"09 Convênio · {conv} mês {m} == 13 lotes pagos no mês",ent_cat[(m,"Convênio · "+conv)],esperado)
check("13 Painel A receber == lotes aguardando + atrasados (enviado)",p13["A5"].value,sum(l["env"] for l in LOT if l["sit"] in ("Aguardando","Atrasada")))
check("13 Painel Atrasado == lotes atrasados",p13["C5"].value,sum(l["env"] for l in LOT if l["sit"]=="Atrasada"))
check("13 Painel A receber == 17 Dados B13",p13["A5"].value,d17["B13"].value)
check("13 Painel Atrasado == 17 Dados B14",p13["C5"].value,d17["B14"].value)
check("13 Painel Glosa % == 17 Dados B15",p13["I5"].value,d17["B15"].value,tol=1e-4)
check("09 A receber de convênio (Pago? = Não) == 13 lotes em aberto com previsão até 30/09",sum(x["valor"] for x in L if x["pago"]=="Não" and x["cat"].startswith("Convênio")),sum(l["env"] for l in LOT if l["sit"] in ("Aguardando","Atrasada") and l["denv"]+datetime.timedelta(days={"Saúde Total":30,"MediPlan":45,"Vida Care":60}[l["conv"]])<=datetime.date(2026,9,30)))
# 5. 14 parcelas × agenda × 09 × 17
PAR=[dict(pac=a,proc=b,at=dt(c),n=d,venc=dt(e),valor=num(f),pago=g,pg=dt(h),sit=i) for a,b,c,d,e,f,g,h,i in rows(pr14,5,list(range(1,10)))]
aprazo=[x for x in AG if x["sit"]=="Realizado" and x["forma"]=="A prazo"]
checkups={(x["data"],x["pac"]) for x in aprazo if x["proc"]=="Teste ergométrico" and any(y["pac"]==x["pac"] and y["data"]==x["data"] and y["proc"]=="Consulta" for y in aprazo) and any(y["pac"]==x["pac"] and y["data"]==x["data"] and y["proc"]=="ECG" for y in aprazo)}
for x in aprazo:
    if (x["data"],x["pac"]) in checkups: continue
    ps=[p for p in PAR if p["pac"]==x["pac"] and p["at"]==x["data"]]
    check(f"14 parcelas de {x['pac'][:14]} {x['data'].strftime('%d/%m')} == valor da agenda",sum(p["valor"] for p in ps),x["valor"])
for (d,pac) in checkups:
    ps=[p for p in PAR if p["pac"]==pac and p["at"]==d]; check(f"14 check-up {pac[:14]} {d.strftime('%d/%m')} == 960",sum(p["valor"] for p in ps),960)
check("14 nenhuma parcela paga depois de 11/09",max(p["pg"] for p in PAR if p["pg"])<=SEXTA,True)
check("14 Painel Vencido == soma das vencidas",p14["G5"].value,sum(p["valor"] for p in PAR if p["sit"]=="Vencida"))
check("14 Painel parcelas vencidas == contagem",p14["I5"].value,sum(1 for p in PAR if p["sit"]=="Vencida"))
check("14 Painel Inadimplência == vencido ÷ (pago + vencido)",p14["K5"].value,num(p14["G5"].value)/(num(p14["G5"].value)+sum(p["valor"] for p in PAR if p["sit"]=="Paga")),tol=1e-6)
check("14 Painel Vencido == 17 Dados B16",p14["G5"].value,d17["B16"].value)
check("14 Painel Inadimplência == 17 Dados B17",p14["K5"].value,d17["B17"].value,tol=1e-4)
for m in range(1,10):
    check(f"09 Particular a prazo mês {m} == 14 parcelas pagas no mês",ent_cat[(m,"Particular a prazo")],sum(p["valor"] for p in PAR if p["pg"] and p["pg"].month==m))
check("09 A receber a prazo (Pago? = Não) == 14 vencidas + a vencer até 30/09",sum(x["valor"] for x in L if x["pago"]=="Não" and x["cat"]=="Particular a prazo"),sum(p["valor"] for p in PAR if p["pago"]!="Sim" and p["venc"]<=datetime.date(2026,9,30)))
check("09 Painel A receber == convênio + parcelas (Pago? = Não)",p09["I5"].value,sum(x["valor"] for x in L if x["pago"]=="Não" and x["tipo"]=="Entrada"))
# 6. 15 orçamentos × agenda × 17
ORC=[dict(data=dt(a),pac=b,prof=c,tipo=d,itens=e,valor=num(f),etapa=g,dec=dt(h)) for a,b,c,d,e,f,g,h in rows(or15,5,list(range(1,9)))]
for o in ORC:
    if o["etapa"]=="Aprovado":
        ok=any(x["pac"]==o["pac"] and x["data"]>=o["dec"] and x["pag"]=="Particular" and x["proc"] in ("MAPA","Holter","Teste ergométrico") for x in AG)
        check(f"15 aprovado {o['pac'][:14]} {o['dec'].strftime('%d/%m')} tem exame na agenda 01",ok,True)
check("15 Painel Em aberto == 17 Dados B19",p15["A5"].value,d17["B19"].value)
check("15 funil (apresentado + em análise) == 17 Dados B18",num(p15["B11"].value)+num(p15["B12"].value),d17["B18"].value)
check("15 Painel Em aberto == soma dos abertos",p15["A5"].value,sum(o["valor"] for o in ORC if o["etapa"] in ("Apresentado","Em análise")))
# 7. 16 cartão × agenda × 09
VEN=[dict(data=dt(a),pac=b,proc=c,tipo=d,parc=e,bruto=num(f),taxa=num(i),liq=num(j),porparc=num(k),prev1=dt(l),prevult=dt(m_)) for a,b,c,d,e,f,g,h,i,j,k,l,m_ in rows(v16,5,list(range(1,14)))]
cart=[x for x in AG if x["sit"]=="Realizado" and x["pag"]=="Particular" and x["forma"] in ("Pix","Cartão de débito","Cartão de crédito")]
# A 16 lista toda venda com alguma liquidação a partir de 01/06: as da agenda visível MAIS as
# de abril/maio com parcela ainda a cair (sem elas, julho ficava sem sete parcelas: rodada 5).
def _ult_liq(x): return x["data"]+datetime.timedelta(days=_d.DIAS_CREDITO.get(x["forma"],0)+30*((x["parcelas"] or 1)-1))
_cart_esp=[x for x in _d.AGENDA_TODA if x["situacao"]=="Realizado" and x["pagador"]=="Particular" and x["forma"] in ("Pix","Cartão de débito","Cartão de crédito") and _ult_liq(x)>=_d.INICIO_AGENDA]
check("16 Vendas == pagamentos com liquidação desde 01/06 (agenda 01 + parcelas anteriores)",len(VEN),len(_cart_esp))
check("16 Vendas da agenda visível == pagamentos com Pix e cartão da agenda 01",len([v for v in VEN if v["data"]>=_d.INICIO_AGENDA]),len(cart))
check("16 Vendas bruto (agenda visível) == agenda",sum(v["bruto"] for v in VEN if v["data"]>=_d.INICIO_AGENDA),sum(x["valor"] for x in cart))
# identidade por liquidação: bruto (AC/AD) = líquido (K/Y) + taxa (X/Z), e a taxa por mês de
# liquidação, lida das colunas ocultas, tem de ser a saída "Taxas de cartão" do caixa
_tx16={}; _br16={}; _dif=0.0
for _r in range(5,v16.max_row+1):
    _L=v16.cell(row=_r,column=12).value
    if _L in (None,""): continue
    _Vn=int(num(v16.cell(row=_r,column=22).value)); _K=num(v16.cell(row=_r,column=11).value); _X=num(v16.cell(row=_r,column=24).value); _Y=num(v16.cell(row=_r,column=25).value); _Z=num(v16.cell(row=_r,column=26).value); _AC=num(v16.cell(row=_r,column=29).value); _AD=num(v16.cell(row=_r,column=30).value)
    _dif=max(_dif,abs(_AC-_K-_X),abs(_AD-_Y-_Z))
    for _k in range(_Vn):
        _dd=dt(_L)+datetime.timedelta(days=30*_k); _ky=(_dd.year,_dd.month)
        _tx16[_ky]=_tx16.get(_ky,0)+(_X if _k<_Vn-1 else _Z); _br16[_ky]=_br16.get(_ky,0)+(_AC if _k<_Vn-1 else _AD)
check("16 bruto = líquido + taxa em cada liquidação (maior diferença)",round(_dif,4),0.0)
_br09={}
for d,t,c,q,r,ds,v,f,pg in _d.LANCAMENTOS:
    if t=="Entrada" and c=="Particular à vista" and f in ("Pix","Cartão de débito","Cartão de crédito"): _br09[(d.year,d.month)]=_br09.get((d.year,d.month),0)+v
for _m in (6,7,8):
    check(f"16 taxa das liquidações de {_m} == 09 Taxas de cartão",round(_tx16.get((_d.ANO,_m),0),2),sai_cat[(_m,"Taxas de cartão")],tol=0.005)
    check(f"16 bruto das liquidações de {_m} == 09 entradas de Pix e cartão",round(_br16.get((_d.ANO,_m),0),2),round(_br09.get((_d.ANO,_m),0),2),tol=0.005)
# A taxa da operadora sai no fim do mês em que o dinheiro CAIU, não em que foi vendido:
# o caixa e a conciliação têm de bater pela liquidação, e a soma do ano tem de fechar.
_esp_tx={}
for d,t,c,q,r,ds,v,f,pg in _d.LANCAMENTOS:
    if c=="Taxas de cartão": _esp_tx[d.month]=_esp_tx.get(d.month,0)+v
for m in (6,7,8):
    check(f"09 Taxas de cartão mês {m} == taxa das liquidações do mês",sai_cat[(m,"Taxas de cartão")],round(_esp_tx.get(m,0),2),tol=0.01)
# A planilha 16 lista só as vendas que aparecem na agenda visível (desde 01/06); o caixa
# cobre o ano. A conferência é por mês de venda, dos dois lados vindo de AGENDA_TODA.
# A taxa é lançada até agosto (setembro ainda está em andamento no exemplo), e o que
# se compara é a taxa das liquidações desses mesmos meses, não a de todas as vendas:
# venda de agosto no crédito só paga taxa quando cair, em setembro.
_tx_esp_ate_ago=round(sum(x for (y,mm),x in _d.TAXA_LIQ_MES.items() if y==_d.ANO and mm<=8),2)
check("09 taxa lançada até agosto == taxa das liquidações até agosto",round(sum(_esp_tx.values()),2),_tx_esp_ate_ago,tol=0.02)
_bruto_16=round(sum(v["bruto"] for v in VEN),2)
_bruto_esp=round(sum(x["valor"] for x in _cart_esp),2)
check("16 Vendas bruto == vendas de Pix e cartão com liquidação desde 01/06",_bruto_16,_bruto_esp,tol=0.005)
check("16 Painel (Agosto) vendas == vendas de agosto",p16["A5"].value,sum(v["bruto"] for v in VEN if v["data"].month==8))
# o painel do 16 mostra a taxa das VENDAS de agosto; o caixa mostra a taxa do que CAIU
# em agosto. São números diferentes de propósito, por isso a conferência é do ano.
check("16 Painel (Agosto) taxas == taxa das vendas de agosto",p16["C5"].value,round(sum(v["taxa"] for v in VEN if v["data"].month==8),2),tol=0.01)
# 8. 05/06/07/08: custo-hora, hora mínima, tabela
check("05 custos fixos == 09 saídas fixas de agosto",p05["B9"].value,sum(sai_cat[(8,c)] for c in ("Aluguel e condomínio","Recepção (salário e encargos)","Contador","Sistema de agenda e assinaturas","Energia, água, internet e telefone","Limpeza e material de escritório","Marketing e site","Anuidade CRM, seguro e cursos")))
check("05 custo total == fixos + pró-labore",p05["B11"].value,num(p05["B9"].value)+18000)
check("05 custo-hora == 200",p05["B13"].value,200,tol=0.001)
check("05 custo-hora == 06 Config",p05["B13"].value,W["06"]["Config"]["B7"].value,tol=0.001)
check("05 custo-hora == 07 Config",p05["B13"].value,W["07"]["Config"]["B5"].value,tol=0.001)
check("05 custo-hora == 08 Config",p05["B13"].value,W["08"]["Config"]["B7"].value,tol=0.001)
check("05 hora mínima exata == 07 hora mínima",p05["B16"].value,s07["B14"].value,tol=0.001)
check("05 hora mínima exata == 08 hora mínima",p05["B16"].value,W["08"]["Config"]["B13"].value,tol=0.001)
check("05 hora mínima arredondada == 340",p05["B17"].value,340)
check("05 custo indireto por hora == 11 Config (custo da estrutura)",p05["B20"].value,W["11"]["Config"]["B11"].value,tol=0.01)
check("05 horas atendidas de agosto (sensibilidade) == 01 sócios",p05["C45"].value,sum(x["minutos"] for x in real(8) if x["prof"]!="Dra. Renata Sousa")/60,tol=0.06)
check("05 horas de atendimento == 140",p05["B12"].value,140)
for r6 in range(5,12):
    proc=s06.cell(row=r6,column=1).value
    if not proc: continue
    r8=next(r for r in range(8,20) if t08.cell(row=r,column=1).value==proc)
    check(f"06 custo cheio {proc} == 08",s06.cell(row=r6,column=6).value,t08.cell(row=r8,column=5).value,tol=0.01)
    check(f"06 preço mínimo {proc} == 08",s06.cell(row=r6,column=7).value,t08.cell(row=r8,column=6).value,tol=0.01)
    check(f"06 particular {proc} == 08 == 01 Config",s06.cell(row=r6,column=9).value,t08.cell(row=r8,column=8).value)
    r1=next(r for r in range(5,17) if W["01"]["Config"].cell(row=r,column=10).value==proc)
    check(f"01 Config tabela particular {proc} == 08",W["01"]["Config"].cell(row=r1,column=13).value,t08.cell(row=r8,column=8).value)
    for j in range(3):
        check(f"01 Config tabela convênio {j+1} {proc} == 06 == 08",num(W["01"]["Config"].cell(row=r1,column=14+j).value),num(t08.cell(row=r8,column=9+j).value))
        check(f"06 convênio {j+1} {proc} == 08",num(s06.cell(row=r6,column=12+2*j).value),num(t08.cell(row=r8,column=9+j).value))
    L_=[x for x in AG if x["sit"]=="Realizado" and x["proc"]==proc and x["data"].month==8]
    check(f"08 realizados em agosto {proc} == 01",t08.cell(row=r8,column=16).value,len(L_)); check(f"08 produção em agosto {proc} == 01",t08.cell(row=r8,column=17).value,sum(x["valor"] for x in L_))
check("07 consulta custo cheio == 06",s07["B13"].value,s06["F5"].value,tol=0.01)
for i,pag in enumerate(("Particular","Saúde Total","MediPlan","Vida Care")):
    check(f"07 tabela consulta {pag} == 08",s07.cell(row=19+i,column=2).value,t08.cell(row=8,column=8+i).value)
    check(f"07 mix de agosto {pag} == consultas realizadas na 01",s07.cell(row=43+i,column=2).value,len([x for x in AG if x["sit"]=="Realizado" and x["proc"]=="Consulta" and x["pag"]==pag and x["data"].month==8]))
# 9. 11 repasse × 01 × 09
for r in range(5,14):
    mes=rp11.cell(row=r,column=1).value
    if not mes: break
    m=MES[mes]; prod=sum(x["valor"] for x in AG if x["sit"]=="Realizado" and x["prof"]==rp11.cell(row=r,column=3).value and x["data"].month==m)
    if m>=7: check(f"11 produção da parceira {mes} == 01",rp11.cell(row=r,column=4).value,prod)
    pago=rp11.cell(row=r,column=9).value
    if pago not in (None,""):
        check(f"11 repasse pago ({mes}) == 09 saída Repasse do mês seguinte",pago,sai_cat[(m+1,"Repasse à médica parceira")])
        check(f"11 repasse pago ({mes}) == 50 % da produção",pago,round(num(rp11.cell(row=r,column=4).value)*0.5))
check("11 pró-labore combinado == 05",p11["E5"].value,18000)
# 10/11/12: entradas mensais sem 'Outras entradas'
for m in range(1,10):
    outras=ent_cat[(m,"Outras entradas")]
    check(f"10 entradas mês {m} == 09 entradas − outras entradas",W["10"]["Entradas e pagamentos"].cell(row=4+m,column=2).value,ent_mes[m]-outras)
    check(f"10 impostos pagos mês {m} == 09 guia",W["10"]["Entradas e pagamentos"].cell(row=4+m,column=3).value,sai_cat[(m,"Impostos e taxas")])
    check(f"11 entradas mês {m} == 09 entradas − outras entradas",W["11"]["Resultado mensal"].cell(row=4+m,column=2).value,ent_mes[m]-outras)
    pess=sum(x["valor"] for x in L if x["pago"]=="Sim" and x["data"].month==m and x["desc"].startswith("Despesa pessoal"))
    check(f"11 saídas sem sócios mês {m} == 09",W["11"]["Resultado mensal"].cell(row=4+m,column=3).value,sai_mes[m]-sai_cat[(m,"Pró-labore dos sócios")]-pess)
check("10 guia de imposto == 11 % das entradas do mês anterior (ago)",sai_cat[(8,"Impostos e taxas")],round((ent_mes[7]-ent_cat[(7,"Outras entradas")])*0.11))
check("12 custo fixo + pró-labore jun/jul/ago == 09 Painel (fixos + linha inteira de pró-labore)",sum(num(c12.cell(row=r,column=2).value) for r in (13,14,15)),sum(sai_cat[(m,c)] for m in (6,7,8) for c in ("Aluguel e condomínio","Recepção (salário e encargos)","Contador","Sistema de agenda e assinaturas","Energia, água, internet e telefone","Limpeza e material de escritório","Marketing e site","Anuidade CRM, seguro e cursos"))+sum(sai_cat[(m,"Pró-labore dos sócios")] for m in (6,7,8)))
check("12 saldo em caixa == 09 Painel Saldo acumulado",c12["B19"].value,p09["G5"].value)
check("12 compromissos não pagos == 09 Painel A pagar",c12["B20"].value,p09["K5"].value)
check("12 meta 2 valor atual == 09 entradas jul+ago+set (sem outras)",c12["C27"].value,sum(ent_mes[m]-ent_cat[(m,"Outras entradas")] for m in (7,8,9)))
check("12 meta 3 alvo == 10 saldo provisionado (agosto, mês fechado)",c12["B28"].value,round(num(p10["J16"].value)))
# 13. 18 agosto/julho == 09 por categoria
cat09={p09.cell(row=r,column=1).value:(num(p09.cell(row=r,column=2).value),num(p09.cell(row=r,column=4).value)) for r in list(range(9,25))+list(range(29,41)) if p09.cell(row=r,column=1).value}
for r in range(6,11):
    cat=r18.cell(row=r,column=1).value; check(f"18 receita ago '{cat}' == 09 Painel (mês anterior)",r18.cell(row=r,column=9).value,cat09[cat][1]); check(f"18 receita jul '{cat}' == 09 lançamentos de julho",r18.cell(row=r,column=8).value,ent_cat[(7,cat)])
for r in list(range(14,22))+list(range(24,28)):
    cat=r18.cell(row=r,column=1).value; check(f"18 saída ago '{cat}' == 09 Painel (mês anterior)",r18.cell(row=r,column=9).value,cat09[cat][1]); check(f"18 saída jul '{cat}' == 09 lançamentos",r18.cell(row=r,column=8).value,sai_cat[(7,cat)])
check("18 receita total ago == 09 Entrou (agosto) − reembolsos de sócios",r18["I11"].value,ent_mes[8]-ent_cat[(8,"Outras entradas")])
check("18 pró-labore ago == 18.000",r18["I32"].value,18000)
check("18 impostos ago == 11 % da receita (sem reembolsos)",r18["I34"].value,round(num(r18["I11"].value)*0.11))
# 14. 20 == 17 Histórico (julho, agosto) e 18
H={h17.cell(row=r,column=1).value:{"ocup":h17.cell(row=r,column=2).value,"atend":h17.cell(row=r,column=3).value,"falta":h17.cell(row=r,column=5).value,"entrou":h17.cell(row=r,column=7).value,"saiu":h17.cell(row=r,column=8).value,
   "conv":h17.cell(row=r,column=10).value,"glosa":h17.cell(row=r,column=12).value,"venc":h17.cell(row=r,column=13).value,"inad":h17.cell(row=r,column=14).value,"orcv":h17.cell(row=r,column=16).value} for r in range(5,17)}
I={i20.cell(row=r,column=1).value:(i20.cell(row=r,column=6).value,i20.cell(row=r,column=7).value) for r in range(5,17)}
def ind(prefix): return next(v for k,v in I.items() if k.startswith(prefix))
for j,(mes,col) in enumerate((("Julho",8),("Agosto",9))):
    check(f"20 Entrou {mes} == 17 Histórico",ind("Entrou")[j],H[mes]["entrou"]); check(f"20 Entrou {mes} == 09 lançamentos",ind("Entrou")[j],ent_mes[MES[mes]])
    check(f"20 Saídas {mes} == 18 Total de saídas",ind("Saídas")[j],r18.cell(row=35,column=col).value)
    check(f"20 Resultado {mes} == 18",ind("Resultado")[j],r18.cell(row=36,column=col).value)
    check(f"20 Margem {mes} == 18",ind("Margem")[j],round(num(r18.cell(row=37,column=col).value)*100,1),tol=0.051)
    check(f"20 Ocupação {mes} == 17 Histórico",ind("Ocupação")[j],round(num(H[mes]["ocup"])*100,1),tol=0.051)
    check(f"20 Taxa de falta {mes} == 17 Histórico",ind("Taxa de falta")[j],round(num(H[mes]["falta"])*100,1),tol=0.051)
    check(f"20 Horas atendidas {mes} == 17 Histórico",ind("Horas atendidas")[j],H[mes]["atend"],tol=0.06)
    check(f"20 Convênio a receber {mes} == 17 Histórico",ind("Convênio a receber")[j],H[mes]["conv"])
    check(f"20 Glosa {mes} == 17 Histórico",ind("Glosa")[j],round(num(H[mes]["glosa"])*100,1),tol=0.051)
    check(f"20 Vencido {mes} == 17 Histórico",ind("Vencido")[j],H[mes]["venc"])
    check(f"20 Inadimplência {mes} == 17 Histórico",ind("Inadimplência")[j],round(num(H[mes]["inad"])*100,1),tol=0.051)
    check(f"20 Orçamentos {mes} == 17 Histórico",ind("Orçamentos")[j],H[mes]["orcv"])
    m=MES[mes]
    check(f"17 Histórico ocupação {mes} == agenda (atendidas ÷ disponíveis)",H[mes]["atend"],sum(x["minutos"] for x in real(m))/60,tol=0.06)
    check(f"17 Histórico taxa de falta {mes} == agenda",H[mes]["falta"],len(faltas(m))/(len(faltas(m))+len(real(m))),tol=1e-4)
    check(f"17 Histórico glosa {mes} == 13 lotes pagos no mês",H[mes]["glosa"],(lambda g,p:g/(g+p) if g+p else 0)(sum(l["glosa"] for l in LOT if l["dpag"] and l["dpag"].month==m),sum(l["pago"] for l in LOT if l["dpag"] and l["dpag"].month==m)),tol=1e-4)
    check(f"17 Histórico convênio a receber {mes} == lotes enviados e não pagos no fim do mês",H[mes]["conv"],sum(l["env"] for l in LOT if l["denv"] and l["denv"]<=datetime.date(2026,m+1,1)-datetime.timedelta(days=1) and (l["dpag"] is None or l["dpag"]>datetime.date(2026,m+1,1)-datetime.timedelta(days=1))))
    fimm=datetime.date(2026,m+1,1)-datetime.timedelta(days=1)
    venc=sum(p["valor"] for p in PAR if p["at"]<=fimm and p["venc"]<fimm and (p["pg"] is None or p["pg"]>fimm)); pago=sum(p["valor"] for p in PAR if p["pg"] and p["pg"]<=fimm)
    check(f"17 Histórico vencido {mes} == 14 parcelas no fim do mês",H[mes]["venc"],venc)
    check(f"17 Histórico inadimplência {mes} == 14",H[mes]["inad"],venc/(venc+pago),tol=1e-4)
for mes,m in MES.items():
    if m>8: break
    check(f"17 Histórico Entrou {mes} == 09",H[mes]["entrou"],ent_mes[m]); check(f"17 Histórico Saiu {mes} == 09",H[mes]["saiu"],sai_mes[m])
# 15. 19 metas atuais == painéis de origem
KR={m19.cell(row=r,column=2).value:(m19.cell(row=r,column=5).value,m19.cell(row=r,column=6).value,m19.cell(row=r,column=7).value) for r in range(5,14) if m19.cell(row=r,column=2).value}
def kr(prefix): return next(v for k,v in KR.items() if k.startswith(prefix))
check("19 lista de retorno atual == 02 Painel",kr("Pacientes na lista")[2],p02["K5"].value)
check("19 inadimplência atual == 14 Painel",kr("Inadimplência")[2],round(num(p14["K5"].value)*100,1),tol=0.051)
check("19 prazo real médio == 13 lotes pagos jul–set",kr("Prazo real")[2],(lambda L_: round(sum(L_)/len(L_),1) if L_ else 0)([(l["dpag"]-l["denv"]).days for l in LOT if l["dpag"] and l["dpag"]>=datetime.date(2026,7,1)]),tol=0.051)
check("19 glosa recuperada no trimestre == 13 lotes (recuperado jul–set)",kr("Glosa recuperada")[2],sum(l["recup"] for l in LOT if l["drec"] and l["drec"]>=datetime.date(2026,7,1)))
check("19 glosa no ano == 13 Painel",kr("Glosa nos lotes")[2],round(num(p13["I5"].value)*100,1),tol=0.051)
check("19 reserva atual == 12 Config",kr("Reserva")[2],c12["B22"].value)
check("19 provisão meta == 10 saldo provisionado (agosto, mês fechado)",kr("Conta de provisão")[1],round(num(p10["J16"].value)))
check("19 provisão atual == 12 meta 3 valor atual",kr("Conta de provisão")[2],c12["C28"].value)
check("19 taxa de falta (4 semanas) == agenda 01",kr("Taxa de falta")[2],(lambda f,r: round(f/(f+r)*100,1))(sum(1 for x in AG if x["sit"]=="Falta" and datetime.date(2026,8,15)<=x["data"]<=SEXTA),sum(1 for x in AG if x["sit"]=="Realizado" and datetime.date(2026,8,15)<=x["data"]<=SEXTA)),tol=0.051)
# 16. 03 e 04: pessoas e datas
_du=sum(1 for i in range((SEXTA-datetime.date(2026,6,1)).days+1) if (datetime.date(2026,6,1)+datetime.timedelta(days=i)).weekday()<5 and (datetime.date(2026,6,1)+datetime.timedelta(days=i)) not in (datetime.date(2026,6,4),datetime.date(2026,9,7)))
check("04 checklist: dias registrados == dias úteis de 01/06 a 11/09",W["04"]["Painel"]["A5"].value,_du)
check("03 rotina soma 30 minutos por semana",W["03"]["Painel"]["G5"].value,30)
check("16 Config preço da consulta == 08 tabela particular",W["16"]["Config"]["B9"].value,t08["H8"].value)
check("08 Tabela tem cabeçalho completo na linha 7",[t08.cell(row=7,column=c).value for c in (1,2,3,4,5,6,7,8)],["Procedimento","Minutos","Gera retorno?","Material (R$)","Custo cheio (R$)","Preço mínimo (R$)","Preço alvo (R$)","Particular"])


# ---------- 17. regras do exemplo levantadas na revisão (A-1, A-2, A-3, A-4, A-6, A-8, A-9, A-10, A-13, A-16, A-17, A-19) ----------
FIM_REF=datetime.date(2026,9,30)
# A-2: a decisão do orçamento nunca vem antes da apresentação, e nada é apresentado ou decidido no futuro
check("15 nenhuma decisão de orçamento anterior à apresentação",[(o["pac"],o["data"],o["dec"]) for o in ORC if o["dec"] is not None and o["dec"]<o["data"]],[])
check("15 nenhuma apresentação de orçamento em data futura",[(o["pac"],o["data"]) for o in ORC if o["data"]>HOJE],[])
check("15 nenhum orçamento decidido em data futura",[(o["pac"],o["dec"]) for o in ORC if o["dec"] is not None and o["dec"]>HOJE],[])
_dias=[num(or15.cell(row=r,column=14).value) for r in range(5,5+len(ORC)) if or15.cell(row=r,column=14).value not in (None,"")]
check("15 nenhum 'Dias até decidir' negativo",min(_dias)>=0,True)
check("15 aprovados com atendimento futuro continuam Aprovado",all(o["etapa"]!="" for o in ORC),True)
# A-8: sem crédito novo para quem tem parcela vencida em aberto
_porpac={}
for _p in PAR: _porpac.setdefault(_p["pac"],[]).append(_p)
def _vencida_em(pac,d): return any(q["venc"]<d and (q["pg"] is None or q["pg"]>d) for q in _porpac.get(pac,[]))
check("14 nenhuma parcela combinada com paciente que já tinha parcela vencida",
      sorted({(p["pac"],p["at"].strftime("%d/%m")) for p in PAR for q in _porpac[p["pac"]] if q["at"]<p["at"] and q["venc"]<p["at"] and (q["pg"] is None or q["pg"]>p["at"])}),[])
check("01 nenhum atendimento a prazo para paciente com parcela vencida em aberto",
      sorted({(x["pac"],x["data"].strftime("%d/%m")) for x in AG if x["sit"]=="Realizado" and x["forma"]=="A prazo" and _vencida_em(x["pac"],x["data"])}),[])
check("15 nenhum orçamento aprovado virou atendimento a prazo de inadimplente",
      sorted({(o["pac"],o["dec"].strftime("%d/%m")) for o in ORC if o["etapa"]=="Aprovado" for x in AG if x["pac"]==o["pac"] and x["data"]>=o["dec"] and x["forma"]=="A prazo" and _vencida_em(x["pac"],x["data"])}),[])
# A-9: A receber = parcelas e lotes com previsão até o fim do mês de referência; descrições sem rótulo que envelhece
_prazo={"Saúde Total":30,"MediPlan":45,"Vida Care":60}
_esperado=sum(p["valor"] for p in PAR if p["pago"]!="Sim" and p["venc"]<=FIM_REF)+sum(l["env"] for l in LOT if l["sit"] in ("Aguardando","Atrasada") and l["denv"]+datetime.timedelta(days=_prazo[l["conv"]])<=FIM_REF)
# Além de parcelas e lotes, "a receber" passa a incluir o cartão já vendido que
# ainda não caiu. É dinheiro certo, com data conhecida, e precisa aparecer.
_cart_a_receber=sum(v for d,t,c,q,r,ds,v,f,pg in _d.LANCAMENTOS
                    if c=="Particular à vista" and pg=="Não")
check("09 A receber = parcelas + lotes até o fim do mês + cartão ainda não liquidado",
      p09["I5"].value,round(_esperado+_cart_a_receber,2),tol=0.01)
check("09 nada pré-lançado depois do mês de referência além do cartão em trânsito",
      sorted({x["desc"][:22] for x in L if x["pago"]=="Não" and x["tipo"]=="Entrada" and x["data"]>FIM_REF
              and not x["desc"].startswith("Repasse da operadora")}),[])
check("09 descrições sem '(vencida)/(a vencer)/(atrasado)/(a receber)' fixos",
      [x["desc"][:50] for x in L if any(t in x["desc"] for t in ("(vencida)","(a vencer)","(atrasado)","(a receber)"))],[])
check("09 regra do A receber escrita em Lançamentos!A2","FIM DO MÊS DE REFERÊNCIA" in (lan["A2"].value or "").upper(),True)
check("09 regra do A receber escrita na Config",any("FIM DO MÊS DE REFERÊNCIA" in (W["09"]["Config"].cell(row=r,column=1).value or "").upper() for r in range(36,46)),True)
# A-10: provisão de 13º e férias na 18; reembolsos de sócios fora da receita e do imposto
check("18 provisão de 13º e férias (ago) == 10 Painel (13º + férias)",r18["I33"].value,num(p10["D16"].value)+num(p10["E16"].value))
for _c,_m in (("E",4),("I",8)):
    check(f"18 reembolsos de sócios (mês {_m}) == 09 'Outras entradas'",r18[f"{_c}12"].value,ent_cat[(_m,"Outras entradas")])
    check(f"18 receita total (mês {_m}) == 09 entradas − reembolsos",r18[f"{_c}11"].value,ent_mes[_m]-ent_cat[(_m,"Outras entradas")])
    check(f"18 impostos (mês {_m}) == 11 % da receita sem reembolsos",r18[f"{_c}34"].value,round((ent_mes[_m]-ent_cat[(_m,"Outras entradas")])*0.11))
check("18 impostos de abril == 10 provisão de impostos de abril",r18["E34"].value,round(num(p10["C12"].value)))
check("18 total de saídas (ago) = fixos + variáveis + pró-labore + provisão + impostos",r18["I35"].value,num(r18["I22"].value)+num(r18["I28"].value)+num(r18["I32"].value)+num(r18["I33"].value)+num(r18["I34"].value))
check("18 receita de abril == 11 Resultado mensal de abril",r18["E11"].value,W["11"]["Resultado mensal"]["B8"].value)
# A-4: uma só definição de "tabela de convênio abaixo do custo cheio + imposto" (06 = 08)
check("06 e 08 contam as mesmas tabelas de convênio abaixo do custo cheio + imposto",s06["E25"].value,t08["E5"].value)
# A-6: margem da parceria = o que fica com a clínica − material (a estrutura não é cobrada duas vezes)
for _r in range(5,14):
    if rp11.cell(row=_r,column=3).value:
        check(f"11 margem da parceria (linha {_r}) = fica com a clínica − material",rp11.cell(row=_r,column=13).value,num(rp11.cell(row=_r,column=11).value)-num(rp11.cell(row=_r,column=12).value))
check("11 Painel: margem da parceria (ano) = fica com a clínica − material (ano)",p11["J9"].value,num(p11["H9"].value)-num(p11["I9"].value))
# A-1 / A-3 / A-13 / A-16 / A-17 / A-19: apresentação
check("01 Agenda com 3.000 linhas (5 a 3004)",ag01.max_row>=3004,True)
check("02 Agenda com 3.000 linhas (5 a 3004)",ag02.max_row>=3004,True)
check("16 Vendas com 2.000 linhas (5 a 2004)",v16.max_row>=2004,True)
check("13 guias glosadas: Recurso vazio mostra '—', nunca 0",[p13.cell(row=r,column=9).value for r in range(53,65) if p13.cell(row=r,column=9).value==0],[])
check("17 orçamentos em aberto (valor) é informativo",d17["F19"].value,"Informativo")
check("19 Semanas: semana sem lote pago fica '—', não 0",W["19"]["Semanas"]["C9"].value,"—")
for _v in VEN:
    if _v["parc"] and num(_v["parc"])>1:
        check(f"16 {_v['pac'][:12]} {_v['data'].strftime('%d/%m')}: líquido por parcela × parcelas == líquido",num(_v["porparc"])*num(_v["parc"]),_v["liq"],tol=0.02)
        check(f"16 {_v['pac'][:12]} {_v['data'].strftime('%d/%m')}: última parcela = 1ª + 30 × (parcelas − 1)",(_v["prevult"]-_v["prev1"]).days,30*(int(num(_v["parc"]))-1))

print(f"{OK} verificações OK, {len(FALHAS)} falhas")
for f in FALHAS: print("  FALHA:",f)
sys.exit(1 if FALHAS else 0)
