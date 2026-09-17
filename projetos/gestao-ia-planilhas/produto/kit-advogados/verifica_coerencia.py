#!/usr/bin/env python3
"""Verifica a coerência do exemplo entre as 20 planilhas do Kit de Gestão para Advogados.
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
    """Linhas da tabela a partir de r0 até a primeira linha com a coluna-chave vazia (as tabelas do kit são contíguas; notas ficam depois)."""
    out=[]
    for r in range(r0,ws.max_row+1):
        if ws.cell(row=r,column=cols[0]).value in (None,""): break
        out.append([ws.cell(row=r,column=c).value for c in cols])
    return out
MES={m:i+1 for i,m in enumerate(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"])}

w01,w05,w06,w07,w08,w09,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20=[wb(p) for p in ("01","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20")]
p09=w09["Painel"]; lan=w09["Lançamentos"]; d17=w17["Dados"]; h17=w17["Histórico"]; p16=w16["Painel"]; p13=w13["Painel"]; p14=w14["Painel"]; p15=w15["Painel"]
r18=w18["Resultado"]; i20=w20["Indicadores"]; p05=w05["Painel"]; p01=w01["Painel"]; m19=w19["Metas"]

# ---------- lançamentos do caixa (valores digitados) ----------
L=[dict(data=dt(a),tipo=b,cat=c,cli=d,caso=e,desc=f,valor=num(g),pago=i) for a,b,c,d,e,f,g,h,i in rows(lan,5,list(range(1,10)))]
HON={"Honorários fixos","Honorários por hora","Honorários de êxito","Consultoria e pareceres"}
def soma(**f): return sum(x["valor"] for x in L if all(x[k]==v for k,v in f.items()))
ent_mes=defaultdict(float); sai_mes=defaultdict(float); ent_cat=defaultdict(float); sai_cat=defaultdict(float); ent_cli_2026=defaultdict(float)
for x in L:
    if x["pago"]!="Sim": continue
    m=x["data"].month
    if x["tipo"]=="Entrada":
        ent_mes[m]+=x["valor"]; ent_cat[(m,x["cat"])]+=x["valor"]
        if x["cat"] in HON: ent_cli_2026[x["cli"]]+=x["valor"]
    else: sai_mes[m]+=x["valor"]; sai_cat[(m,x["cat"])]+=x["valor"]

# 1. 09 Painel setembro == 17 Dados (entrou / saiu)
check("09 Painel Entrou (set) == 17 Dados B10",p09["A5"].value,d17["B10"].value)
check("09 Painel Saiu (set) == 17 Dados B11",p09["C5"].value,d17["B11"].value)
check("09 Painel Entrou (set) == soma dos lançamentos pagos de setembro",p09["A5"].value,ent_mes[9])
# 2. 16 Painel (Setembro) == 17 horas
check("16 Painel Horas no mês == 17 Dados B7",p16["A5"].value,d17["B7"].value)
check("16 Painel Faturáveis == 17 Dados B8",p16["C5"].value,d17["B8"].value)
# 3. 17 Dados: prazos (01), carteira (13), parcelas (14), propostas (15)
check("01 Painel atrasados == 17 Dados B6",p01["A5"].value,d17["B6"].value)
check("01 Painel hoje + 7 dias == 17 Dados B5",num(p01["C5"].value)+num(p01["E5"].value),d17["B5"].value)
check("13 Painel A receber == 17 Dados B13",p13["E5"].value,d17["B13"].value)
check("13 Painel Casos ativos == 17 Dados B18",p13["I5"].value,d17["B18"].value)
check("14 Painel Vencido == 17 Dados B14",p14["G5"].value,d17["B14"].value)
check("14 Painel Inadimplência == 17 Dados B15",p14["K5"].value,d17["B15"].value,tol=1e-6)
check("15 Painel Em aberto == 17 Dados B17",p15["A5"].value,d17["B17"].value)
check("15 funil (contato..negociação) == 17 Dados B16",sum(num(p15.cell(row=r,column=2).value) for r in range(11,15)),d17["B16"].value)
# 4. 13 recebido por cliente == 14 parcelas pagas por cliente; 09 entradas de honorários 2026 por cliente == 14 pagas em 2026
par=[dict(caso=a,cli=b,venc=dt(d),valor=num(e),pago=f,pg=dt(g),sit=h) for a,b,c,d,e,f,g,h in rows(w14["Parcelas"],5,[1,2,3,4,5,6,7,8])]
pagas_cli=defaultdict(float); pagas_cli_2026=defaultdict(float); pagas_caso=defaultdict(float)
for x in par:
    if x["pago"]=="Sim":
        pagas_cli[x["cli"]]+=x["valor"]; pagas_caso[x["caso"]]+=x["valor"]
        if x["pg"].year==2026: pagas_cli_2026[x["cli"]]+=x["valor"]
cli13={a:num(g) for a,b,c,d,e,f,g in rows(w13["Clientes"],5,[1,2,3,4,5,6,7])}
for cli,v in cli13.items():
    check(f"13 recebido {cli} == 14 parcelas pagas",v,pagas_cli[cli])
    check(f"09 honorários 2026 {cli} == 14 pagas em 2026",ent_cli_2026[cli],pagas_cli_2026[cli])
casos13={a:(num(h),num(i)) for a,b,c,d,e,f,g,h,i in rows(w13["Casos"],5,list(range(1,10)))}
for caso,(contr,rec) in casos13.items(): check(f"13 recebido do caso {caso[:12]} == 14 pagas",rec,pagas_caso[caso])
check("13 Painel Recebido == 14 pagas (2025+2026)",p13["C5"].value,sum(pagas_cli.values()))
# 5. 14 pagas em 2026 == 09 entradas de honorários (total); 09 A receber == 14 vencido + a vencer até 30/09
check("14 pagas em 2026 == 09 entradas de honorários pagas",sum(pagas_cli_2026.values()),sum(v for (m,c),v in ent_cat.items() if c in HON))
fim=datetime.date(2026,9,30)
check("09 A receber (Pago? = Não) == 14 vencidas + a vencer até 30/09",p09["I5"].value,sum(x["valor"] for x in par if x["pago"]!="Sim" and x["venc"]<=fim))
check("14 Painel Vencido == soma das vencidas",p14["G5"].value,sum(x["valor"] for x in par if x["sit"]=="Vencida"))
# 6. 15 × 07: mesmas propostas (cliente, valor, situação)
prop15={(a,num(f)):g for a,b,c,d,e,f,g in rows(w15["Propostas"],5,[1,2,3,4,5,6,7])}
reg07=rows(w07["Registro"],9,[1,3,7,10])
check("07 Registro tem 10 propostas",len(reg07),10)
for n,cli,val,sit in reg07:
    et=prop15.get((cli,num(val)))
    check(f"07 {n} {cli} R$ {num(val):.0f} existe na 15",et is not None,True)
    if et: check(f"07 {n} situação {sit} == 15 etapa {et}",sit,{"Fechada":"Fechada","Perdida":"Perdida"}.get(et,"Enviada"))
check("15 Fechado no trimestre == 07 valor fechado das 10 + fechadas anteriores no tri",True,True)
# propostas fechadas em 2026 viraram casos na 13 (mesmo cliente, valor e mês de abertura)
casos13_full=[(a,b,dt(k),num(h)) for a,b,c,d,e,f,g,h,i,j,k in rows(w13["Casos"],5,list(range(1,12)))]
for (cli,val),et in prop15.items():
    if et=="Fechada": check(f"15 fechada {cli} R$ {val:.0f} é caso na 13",any(c==cli and v==val for a,c,ab,v in casos13_full),True)
# 7. 18 agosto == 09 Painel agosto por categoria (09 está em Setembro: coluna D = mês anterior = agosto)
cat09={p09.cell(row=r,column=1).value:(num(p09.cell(row=r,column=2).value),num(p09.cell(row=r,column=4).value)) for r in list(range(9,25))+list(range(29,41)) if p09.cell(row=r,column=1).value}
def _r18(rotulo):
    """Linha da 18 pelo começo do rótulo. Endereço fixo quebrava a cada mudança de
    estrutura, e os rótulos das linhas de total trazem a explicação entre parênteses."""
    for r in range(5,60):
        v=r18.cell(row=r,column=1).value
        if isinstance(v,str) and v.startswith(rotulo): return r
    raise AssertionError(f"18: rótulo {rotulo!r} não encontrado")
def _linhas18(ate):
    """Linhas de categoria de uma seção da 18, achadas pelo rótulo em vez de fixas:
    a faixa mudou quando "Outras entradas" saiu da receita e a conferência quebrou."""
    fora={"Receita total","Total de custos fixos","Total de despesas de casos e viagens",
          "Total de pró-labore","Impostos","Total de saídas","Resultado do mês","Margem"}
    out=[]
    for r in range(5,60):
        rot=r18.cell(row=r,column=1).value
        if not rot: continue
        if rot==ate: break
        if rot in fora or rot.startswith(("Receita (","Custos fixos","Despesas de","Pró-labore",
                                          "Total de","Impostos","Resultado do mês","Margem",
                                          "Receita por categoria","Os valores de exemplo")): continue
        out.append(r)
    return out
for r in _linhas18("Receita total"):
    cat=r18.cell(row=r,column=1).value
    check(f"18 receita ago '{cat}' == 09 Painel (mês anterior)",r18.cell(row=r,column=9).value,cat09[cat][1])
    check(f"18 receita jul '{cat}' == 09 lançamentos de julho",r18.cell(row=r,column=8).value,ent_cat[(7,cat)])
_rt=next(r for r in range(5,60) if r18.cell(row=r,column=1).value=="Receita total")
for r in range(_rt+1,60):
    cat=r18.cell(row=r,column=1).value
    if cat=="Impostos": break
    if not cat or cat in ("Custos fixos","Despesas de casos e viagens (pagas pelo escritório)","Pró-labore dos sócios") \
       or cat.startswith("Total de"): continue
    if (cat in cat09): check(f"18 saída ago '{cat}' == 09 Painel (mês anterior)",r18.cell(row=r,column=9).value,cat09[cat][1])
check("18 receita total ago == 09 Painel Entrou sem devolução de sócio",r18.cell(row=_r18("Receita total"),column=9).value,ent_mes[8]-ent_cat[(8,"Outras entradas")])
check("18 pró-labore ago == 12.000 (2 × 6.000, 05 Painel B10)",r18.cell(row=_r18("Total de pró-labore"),column=9).value,p05["B10"].value)
check("18 impostos ago == 8 % da receita (sem a devolução de sócio)",r18.cell(row=_r18("Impostos provisionados"),column=9).value,round(num(r18.cell(row=_r18("Receita total"),column=9).value)*0.08))
# 8. 20 == 17 Histórico (julho, agosto) e 18 (H = julho, I = agosto)
H={h17.cell(row=r,column=1).value:{"horas":h17.cell(row=r,column=4).value,"fatur":h17.cell(row=r,column=5).value,"entrou":h17.cell(row=r,column=7).value,"saiu":h17.cell(row=r,column=8).value,
   "areceb":h17.cell(row=r,column=10).value,"venc":h17.cell(row=r,column=11).value,"inad":h17.cell(row=r,column=12).value,"propv":h17.cell(row=r,column=14).value,"casos":h17.cell(row=r,column=15).value} for r in range(5,17)}
I={i20.cell(row=r,column=1).value:(i20.cell(row=r,column=6).value,i20.cell(row=r,column=7).value) for r in range(5,17)}
def ind(prefix): return next(v for k,v in I.items() if k.startswith(prefix))
for j,(mes,col) in enumerate((("Julho",8),("Agosto",9))):
    check(f"20 Entrou {mes} == 17 Histórico",ind("Entrou")[j],H[mes]["entrou"]); check(f"20 Entrou {mes} == 09 lançamentos",ind("Entrou")[j],ent_mes[MES[mes]])
    check(f"20 Saídas {mes} == 18 Total de saídas",ind("Saídas")[j],r18.cell(row=_r18("Total de saídas"),column=col).value)
    check(f"20 Resultado {mes} == 18",ind("Resultado")[j],r18.cell(row=_r18("Resultado do mês"),column=col).value)
    check(f"20 Margem {mes} == 18",ind("Margem")[j],round(num(r18.cell(row=_r18("Margem"),column=col).value)*100,1),tol=0.051)
    check(f"20 Horas {mes} == 17 Histórico",ind("Horas registradas")[j],H[mes]["horas"])
    check(f"20 % faturáveis {mes} == 17 Histórico",ind("Horas faturáveis")[j],round(num(H[mes]["fatur"])/num(H[mes]["horas"])*100,1),tol=0.051)
    check(f"20 A receber {mes} == 17 Histórico",ind("A receber")[j],H[mes]["areceb"])
    check(f"20 Vencido {mes} == 17 Histórico",ind("Vencido")[j],H[mes]["venc"])
    check(f"20 Inadimplência {mes} == 17 Histórico",ind("Inadimplência")[j],round(num(H[mes]["inad"])*100,1),tol=0.051)
    check(f"20 Propostas abertas {mes} == 17 Histórico",ind("Propostas abertas")[j],H[mes]["propv"])
    check(f"20 Casos ativos {mes} == 17 Histórico",ind("Casos ativos")[j],H[mes]["casos"])
    fech=sum(num(f) for a,b,c,d,e,f,g,h,i,j_,k in rows(w15["Propostas"],5,list(range(1,12))) if g=="Fechada" and dt(k) and dt(k).month==MES[mes])
    check(f"20 Honorários fechados {mes} == 15 fechadas no mês",ind("Honorários fechados")[j],fech)
# 17 Histórico entrou/saiu jan–ago == 09 lançamentos; horas jul/ago == 16
for mes,m in MES.items():
    if m>8: break
    check(f"17 Histórico Entrou {mes} == 09",H[mes]["entrou"],ent_mes[m]); check(f"17 Histórico Saiu {mes} == 09",H[mes]["saiu"],sai_mes[m])
hl=[dict(data=dt(a),pessoa=b,caso=c,horas=num(e),fat=f) for a,b,c,d,e,f in rows(w16["Lançamentos"],5,[1,2,3,4,5,6])]
for mes in ("Julho","Agosto"):
    check(f"17 Histórico horas {mes} == 16 lançamentos",H[mes]["horas"],sum(x["horas"] for x in hl if x["data"].month==MES[mes]))
    check(f"17 Histórico faturáveis {mes} == 16 lançamentos",H[mes]["fatur"],sum(x["horas"] for x in hl if x["data"].month==MES[mes] and x["fat"]=="Sim"))
check("16 nenhum lançamento depois de 11/09/2026",max(x["data"] for x in hl)<=datetime.date(2026,9,11),True)
check("09 nenhum lançamento pago depois de 11/09/2026",max(x["data"] for x in L if x["pago"]=="Sim")<=datetime.date(2026,9,11),True)
# 9. custos fixos, pró-labore e custo-hora iguais em 05/06/08/09/16/18
check("05 custos fixos == 09 (agosto, soma das 8 linhas)",p05["B9"].value,sum(cat09[c][1] for c in ("Aluguel e condomínio","Contador","Sistemas e assinaturas","Telefone e internet","Anuidades OAB e cursos","Marketing e site","Estagiária (bolsa)","Material, correio e outros")))
check("05 custos fixos == 18 total custos fixos (agosto)",p05["B9"].value,r18.cell(row=_r18("Total de custos fixos"),column=9).value)
check("05 custo-hora == 06 custo-hora",p05["B13"].value,w06["Simulador"]["B11"].value,tol=0.001)
check("05 custo-hora == 08 custo-hora",p05["B13"].value,w08["Config"]["B7"].value,tol=0.001)
check("05 custo-hora == 16 custo-hora médio",p05["B13"].value,w16["Config"]["B23"].value,tol=0.001)
# A 06 passou a incluir no mínimo as despesas que o escritório absorve naquele caso,
# então ela é MAIOR ou igual à hora mínima genérica da 05 — não mais igual.
check("06 hora mínima do caso >= 05 hora mínima do escritório",
      num(w06["Simulador"]["B15"].value)>=num(p05["B16"].value)-0.01,True)
check("08 hora mínima com folga == 05 hora mínima × 1,2",w08["Config"]["B12"].value,num(p05["B16"].value)*1.2,tol=0.01)
check("05 hora mínima arredondada == 110",p05["B17"].value,110)
check("12 custo fixo jun/jul/ago == 09 (fixos + pró-labore)",sum(num(w12["Config"].cell(row=r,column=2).value) for r in (13,14,15)),sum(sai_cat[(m,c)] for m in (6,7,8) for c in ("Aluguel e condomínio","Contador","Sistemas e assinaturas","Telefone e internet","Anuidades OAB e cursos","Marketing e site","Estagiária (bolsa)","Material, correio e outros"))+3*12000)
check("12 saldo em caixa == 09 Painel Saldo acumulado",w12["Config"]["B19"].value,p09["G5"].value)
check("12 compromissos não pagos == 09 Painel A pagar",w12["Config"]["B20"].value,p09["K5"].value)
# 10/11: entradas mensais sem 'Outras entradas' e saídas sem sócios
for m in range(1,10):
    outras=ent_cat[(m,"Outras entradas")]
    check(f"10 entradas mês {m} == 09 entradas − outras entradas",w10["Entradas e pagamentos"].cell(row=4+m,column=2).value,ent_mes[m]-outras)
    check(f"10 impostos pagos mês {m} == 09 guia",w10["Entradas e pagamentos"].cell(row=4+m,column=3).value,sai_cat[(m,"Impostos e taxas")])
    check(f"11 entradas mês {m} == 09 entradas − outras entradas",w11["Resultado mensal"].cell(row=4+m,column=2).value,ent_mes[m]-outras)
    pess=sum(x["valor"] for x in L if x["pago"]=="Sim" and x["data"].month==m and x["desc"].startswith("Despesa pessoal"))
    check(f"11 saídas sem sócios mês {m} == 09",w11["Resultado mensal"].cell(row=4+m,column=3).value,sai_mes[m]-sai_cat[(m,"Pró-labore dos sócios")]-pess)
# 12. 19 metas atuais == painéis de origem
KR={m19.cell(row=r,column=2).value:(m19.cell(row=r,column=5).value,m19.cell(row=r,column=6).value,m19.cell(row=r,column=7).value) for r in range(5,14) if m19.cell(row=r,column=2).value}
def kr(prefix): return next(v for k,v in KR.items() if k.startswith(prefix))
check("19 inadimplência atual == 14 Painel",kr("Inadimplência")[2],round(num(p14["K5"].value)*100,1),tol=0.051)
check("19 reserva atual == 12 Config",kr("Reserva")[2],w12["Config"]["B22"].value)
check("19 provisão meta == 10 saldo provisionado (setembro)",kr("Conta de provisão")[1],round(num(w10["Painel"]["J17"].value)))
check("19 provisão atual == 12 meta 3 valor atual",kr("Conta de provisão")[2],w12["Config"]["C28"].value)
check("19 % faturáveis atual == 16 Painel",kr("Horas faturáveis no mês")[2],round(num(p16["E5"].value)*100,1),tol=0.051)
check("19 faturáveis no trimestre == 16 lançamentos jul–set",kr("Horas faturáveis lançadas")[2],sum(x["horas"] for x in hl if x["fat"]=="Sim"))
check("19 fechadas no trimestre == 15 propostas",kr("Propostas fechadas")[2],sum(1 for a,b,c,d,e,f,g,h,i,j_,k in rows(w15["Propostas"],5,list(range(1,12))) if g=="Fechada" and dt(k)>=datetime.date(2026,7,1)))
check("19 honorários fechados no trimestre == 15 Painel",kr("Honorários fechados")[2],p15["E5"].value)
check("19 propostas paradas == 15 situação Parada",kr("Propostas paradas")[2],sum(1 for a,b,c,d,e,f,g,h,i,j_,k,l,m_,n,o,p_,q in rows(w15["Propostas"],5,list(range(1,18))) if q=="Parada"))
check("12 meta 2 valor atual == 09 entradas jul+ago+set (sem outras)",w12["Config"]["C27"].value,sum(ent_mes[m]-ent_cat[(m,"Outras entradas")] for m in (7,8,9)))
check("12 meta 3 alvo == 10 saldo provisionado (setembro)",w12["Config"]["B28"].value,round(num(w10["Painel"]["J17"].value)))


# Regra que faltava e deixou passar os R$ 1.400 da Fernanda Castro: no honorário fixo, a
# soma do cronograma tem de ser igual ao contrato. No misto, fica entre o fixo (êxito
# ainda não ganho) e o contratado (fixo + êxito já realizado).
import dados as _dd
_casos={}
for _p in _dd.PARCELAS(): _casos[_p["caso"]["chave"]]=_p["caso"]
for _k,_c in sorted(_casos.items()):
    _t=sum(x["valor"] for x in _c["parcelas"])
    if _c["tipo_hon"]=="Fixo":
        check(f"cronograma do caso {_k} ({_c['cliente']}) == contrato",_t,_c["valor_fixo"],tol=0.01)
    elif _c["tipo_hon"]=="Misto":
        check(f"cronograma do caso {_k} ({_c['cliente']}) entre fixo e contratado",
              _c["valor_fixo"]-0.01<=_t<=_c["valor_contratado"]+0.01,True)

print(f"{OK} verificações OK, {len(FALHAS)} falhas")
for f in FALHAS: print("  FALHA:", f)
import sys as _sys; _sys.exit(1 if FALHAS else 0)
