"""Clínica fictícia compartilhada por todas as planilhas do Kit de Gestão para Médicos (fonte única do exemplo).
Clínica Vida Plena (Barueri/SP): 2 sócios (Dra. Carolina Mendes, clínica médica; Dr. Paulo Andrade, cardiologia),
1 médica parceira por repasse (Dra. Renata Sousa, endocrinologia, 2 turnos por semana, 50 % do que produz),
1 recepcionista (Bruna Carvalho, CLT), 2 consultórios (Sala 1 e Sala 2), 3 convênios fictícios (Saúde Total, MediPlan,
Vida Care) e ~130 pacientes fictícios. Tudo inventado. Nada clínico: "procedimento" é só o nome administrativo do
atendimento (consulta, retorno, ECG, MAPA, Holter, teste ergométrico, avaliação endócrina).

Referência do exemplo: HOJE = segunda-feira 14/09/2026; a "sexta do painel" é 11/09/2026. Nenhum lançamento pago
(caixa, parcela, lote de convênio) tem data depois de 11/09/2026. Agenda futura, vencimentos em aberto e datas de
orçamentos abertos são relativos a HOJE (fórmula =HOJE()+n, via prazo_formula); histórico é fixo.

Regra do dinheiro:
- A agenda (01) registra desde 01/06/2026 (antes, a recepção só fechava o caixa do dia). O gerador produz janeiro a
  maio também, mas só para alimentar caixa, lotes de convênio, parcelas a prazo e produção da parceira.
  Junho entra para que o Histórico da 17 tenha o mês anterior ao trimestre e a "partida" das metas (19) seja reproduzível.
- Particular à vista (Pix, dinheiro, cartão) entra no caixa (09) pelo fechamento do dia: uma linha por dia e forma.
- Particular a prazo vira parcela (14); parcela paga <=> entrada no caixa na data do pagamento.
- Convênio: cada atendimento realizado vira uma guia (13 · Guias); as guias do mês formam um lote por convênio,
  enviado no dia 5 do mês seguinte; o pagamento (menos a glosa) entra no caixa na data em que o convênio paga.
- Cartão: o caixa registra o valor bruto no dia da venda; as taxas do mês entram como uma saída no fim do mês
  (o mesmo total que a conciliação 16 calcula). Repasse da parceira: 50 % da produção do mês, pago dia 10 do mês seguinte.
"""
import random
from datetime import date, timedelta

CLINICA="Clínica Vida Plena"; CIDADE="Barueri/SP"
HOJE=date(2026,9,14)          # segunda-feira de referência
SEXTA=date(2026,9,11)         # última sexta (painel da semana)
ANO=2026
INICIO_AGENDA=date(2026,6,1)  # a agenda na planilha começou em junho
INICIO_GERADOR=date(2026,1,5) # o gerador produz jan-maio só para caixa/lotes/parcelas (não aparece na agenda da 01)
FUTURO=21                     # dias de agenda futura (relativa a hoje)
ALIQ=0.11                     # alíquota efetiva de impostos do exemplo (única em todo o kit; "combinada com o contador")
MARGEM=0.30                   # margem mínima sobre o preço (05/06/07/08)
MARGEM_ALVO=0.45              # margem alvo (06/08)
JUROS_MES=0.015               # custo do dinheiro no simulador convênio × particular (07)
REPASSE=0.50                  # parte da produção da médica parceira que é dela (11)
RETORNO_PROB=0.40             # em média, 0,4 retorno por consulta (tempo embutido na precificação, 06)
SALDO_INICIAL=26000           # caixa em 01/01/2026
CAR="Dra. Carolina Mendes"; PAU="Dr. Paulo Andrade"; REN="Dra. Renata Sousa"; BRU="Bruna Carvalho"
# nome, papel, tipo de remuneração, valor mensal (pró-labore ou salário), horas de atendimento planejadas por mês
PESSOAS=[(CAR,"Sócia · clínica médica","Pró-labore",9000,70),
         (PAU,"Sócio · cardiologia","Pró-labore",9000,70),
         (REN,"Médica parceira · endocrinologia","Repasse (50 % da produção)",0,35),
         (BRU,"Recepcionista (CLT)","Salário (já nos custos fixos)",2200,0)]
MEDICOS=[CAR,PAU,REN]; SOCIOS=[CAR,PAU]
ESPECIALIDADE={CAR:"Clínica médica",PAU:"Cardiologia",REN:"Endocrinologia"}
SALAS=["Sala 1","Sala 2"]
DIAS_SEMANA=["Segunda","Terça","Quarta","Quinta","Sexta"]
HORAS_TURNO=4
# turnos fixos da semana: profissional, dia (0=segunda), período, sala, hora de início
TURNOS=[(CAR,0,"Manhã","Sala 1",8),(CAR,1,"Manhã","Sala 1",8),(CAR,2,"Tarde","Sala 1",14),(CAR,3,"Manhã","Sala 1",8),
        (PAU,0,"Tarde","Sala 2",14),(PAU,1,"Tarde","Sala 2",14),(PAU,3,"Tarde","Sala 2",14),(PAU,4,"Manhã","Sala 2",8),
        (REN,1,"Tarde","Sala 1",14),(REN,3,"Tarde","Sala 1",14)]
FERIADOS=[date(2026,1,1),date(2026,2,16),date(2026,2,17),date(2026,4,3),date(2026,4,21),date(2026,5,1),date(2026,6,4),
          date(2026,9,7),date(2026,10,12),date(2026,11,2),date(2026,11,15),date(2026,11,20),date(2026,12,25)]
# procedimento (nome administrativo), duração (min), material por atendimento (R$), retorno esperado em (dias)
PROCEDIMENTOS=[("Consulta",30,4,30),("Retorno",20,2,0),("ECG",20,8,0),("MAPA",20,15,0),("Holter",20,18,0),
               ("Teste ergométrico",40,25,0),("Avaliação endócrina",40,4,45)]
DUR={p:d for p,d,_,_ in PROCEDIMENTOS}; MATERIAL={p:m for p,_,m,_ in PROCEDIMENTOS}; RETORNO_DIAS={p:r for p,_,_,r in PROCEDIMENTOS}
PROC_PROF={CAR:["Consulta","Retorno"],PAU:["Consulta","Retorno","ECG","MAPA","Holter","Teste ergométrico"],REN:["Avaliação endócrina","Retorno"]}
PESOS_PROC={CAR:{"Consulta":60,"Retorno":40},PAU:{"Consulta":36,"Retorno":24,"ECG":16,"MAPA":8,"Holter":7,"Teste ergométrico":9},REN:{"Avaliação endócrina":60,"Retorno":40}}
PAGADORES=["Particular","Saúde Total","MediPlan","Vida Care"]
CONVENIOS=[("Saúde Total",30,0.03),("MediPlan",45,0.06),("Vida Care",60,0.10)]   # nome, prazo de pagamento (dias), glosa histórica
PRAZO={n:p for n,p,_ in CONVENIOS}; GLOSA_HIST={n:g for n,_,g in CONVENIOS}
DIA_ENVIO_LOTE=5
# tabela de preços: procedimento -> valor por pagador (Particular, Saúde Total, MediPlan, Vida Care); None = não credenciado
TABELA={"Consulta":(380,120,100,90),"Retorno":(0,0,0,0),"ECG":(130,40,35,32),"MAPA":(300,95,85,75),"Holter":(350,105,95,85),
        "Teste ergométrico":(450,140,125,110),"Avaliação endócrina":(400,130,None,None)}
def preco(proc,pag):
    v=TABELA[proc][PAGADORES.index(pag)]; return v
CUSTOS_FIXOS=[("Aluguel e condomínio",3900),("Recepção (salário e encargos)",3100),("Contador",600),("Sistema de agenda e assinaturas",300),
              ("Energia, água, internet e telefone",550),("Limpeza e material de escritório",450),("Marketing e site",650),("Anuidade CRM, seguro e cursos",450)]
DIA_FIXO={"Aluguel e condomínio":5,"Recepção (salário e encargos)":5,"Contador":10,"Sistema de agenda e assinaturas":8,"Energia, água, internet e telefone":12,
          "Limpeza e material de escritório":15,"Marketing e site":20,"Anuidade CRM, seguro e cursos":15}
CUSTOS_FIXOS_TOTAL=sum(v for _,v in CUSTOS_FIXOS)                                    # 10.000
PRO_LABORE=[(n,v) for n,p,t,v,_ in PESSOAS if t=="Pró-labore"]                        # 9.000 + 9.000
PRO_LABORE_TOTAL=sum(v for _,v in PRO_LABORE)                                         # 18.000
CUSTO_TOTAL_MES=CUSTOS_FIXOS_TOTAL+PRO_LABORE_TOTAL                                   # 28.000
HORAS_ATENDIMENTO_MES=sum(h for n,p,t,v,h in PESSOAS if t=="Pró-labore")             # 140 (só quem entra no custo-hora)
CUSTO_HORA=round(CUSTO_TOTAL_MES/HORAS_ATENDIMENTO_MES,4)                            # 200,00
HORA_MINIMA_EXATA=round(CUSTO_HORA/(1-MARGEM-ALIQ),2)                                 # 338,98
HORA_MINIMA=340                                                                        # arredondada para múltiplo de 5 (05)
HORA_ALVO=round(CUSTO_HORA/(1-MARGEM_ALVO-ALIQ),2)                                    # 454,55
CUSTOS_SEM_EQUIPE=sum(v for n,v in CUSTOS_FIXOS if not n.startswith("Recepção"))    # 6.900
CUSTO_INDIRETO_HORA=round(CUSTOS_FIXOS_TOTAL/HORAS_ATENDIMENTO_MES,4)                # 71,4286 (05: custo da estrutura por hora; a 11 usa na margem da parceria)
def custo_procedimento(proc):
    """Custo cheio de um atendimento (06): tempo (+ retorno embutido, nas consultas) × custo-hora + material."""
    t=DUR[proc]+(RETORNO_PROB*DUR["Retorno"] if RETORNO_DIAS[proc]>0 else 0)
    return t/60*CUSTO_HORA+MATERIAL[proc]
def preco_minimo(proc): return custo_procedimento(proc)/(1-ALIQ-MARGEM)
def preco_alvo(proc): return custo_procedimento(proc)/(1-ALIQ-MARGEM_ALVO)
CAT_ENTRADA=["Particular à vista","Particular a prazo","Convênio · Saúde Total","Convênio · MediPlan","Convênio · Vida Care","Outras entradas"]
CAT_VARIAVEIS=["Materiais e insumos de atendimento","Taxas de cartão","Repasse à médica parceira","Manutenção de equipamentos"]
CAT_SAIDA=["Pró-labore dos sócios"]+[c for c,_ in CUSTOS_FIXOS]+CAT_VARIAVEIS+["Impostos e taxas","Outras saídas"]
FORMAS=["Pix","Dinheiro","Cartão de débito","Cartão de crédito","A prazo","Convênio"]
TAXAS={"Pix":0.0,"Cartão de débito":0.015,"Cartão de crédito":0.032,"Cartão de crédito parcelado":0.039}   # taxas do exemplo (16)
DIAS_CREDITO={"Cartão de débito":1,"Cartão de crédito":30}
SITUACOES=["Agendado","Confirmado","Realizado","Falta","Cancelado","Remarcado"]
OCUPACAO_ALVO={CAR:0.87,PAU:0.85,REN:0.80}
FALTA_PROB={"Particular":0.06,"Saúde Total":0.09,"MediPlan":0.10,"Vida Care":0.12}

def D(y,m,d): return date(y,m,d)
def prazo_formula(dias):
    """Data do exemplo como DATA LITERAL, ancorada em HOJE.

    Antes devolvia "=TODAY()+n", para o exemplo parecer sempre atual. O efeito
    colateral era pior do que o ganho: o histórico ficava preso em setembro de 2026
    e só a parte futura andava, então a mesma clínica mostrava ocupação diferente
    em arquivos diferentes conforme o dia em que o cliente abria (auditoria de
    17/09/2026). Com data literal o exemplo é reproduzível e fecha em qualquer dia;
    o "Como usar" e a nota em Config mandam trocar a data de referência por =HOJE() ao começar a usar.
    """
    return HOJE+timedelta(days=dias)
def dias(d): return (d-HOJE).days
def dia_util(d):
    while d.weekday()>=5 or d in FERIADOS: d+=timedelta(days=1)
    return d
def fim_mes(m,y=ANO): return date(y+(m==12),(m%12)+1,1)-timedelta(days=1)
def mes_abrev(m): return ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"][m-1]

# ---------------------------------------------------------------------------------------------------------------
# PACIENTES: ~130 nomes inventados; convênio; profissional principal; contato fictício (o prefixo 90000 não existe).
# ---------------------------------------------------------------------------------------------------------------
_NOMES=["Ana","Beatriz","Bruno","Camila","Carlos","Cláudia","Daniel","Débora","Eduardo","Elaine","Fábio","Fernanda","Gabriel","Gisele","Gustavo",
        "Helena","Henrique","Isabela","João","Juliana","Larissa","Leandro","Letícia","Lucas","Luciana","Marcelo","Márcia","Mariana","Mateus","Mônica",
        "Natália","Otávio","Patrícia","Paulo","Priscila","Rafael","Regina","Renato","Ricardo","Roberta","Rodrigo","Sandra","Sérgio","Simone","Tatiana",
        "Thiago","Vanessa","Vinícius","Viviane","Wagner"]
_SOBRENOMES=["Almeida","Araújo","Barbosa","Barros","Batista","Cardoso","Carvalho","Castro","Correia","Costa","Cunha","Dias","Duarte","Fernandes","Ferreira",
             "Freitas","Gomes","Gonçalves","Lima","Lopes","Macedo","Machado","Martins","Melo","Monteiro","Moreira","Nascimento","Nunes","Oliveira","Pereira",
             "Pinto","Ramos","Reis","Ribeiro","Rocha","Santos","Silva","Teixeira","Vieira","Xavier"]
def _pacientes():
    rng=random.Random(7); out=[]; usados=set()
    plano={CAR:68,PAU:54,REN:34}
    for prof,n in plano.items():
        k=0
        while k<n:
            nome=f"{rng.choice(_NOMES)} {rng.choice(_SOBRENOMES)}"
            if nome in usados: continue
            usados.add(nome)
            if prof==REN: conv=rng.choices(["Particular","Saúde Total"],[62,38])[0]
            else: conv=rng.choices(PAGADORES,[45,25,18,12])[0]
            out.append(dict(nome=nome,convenio=conv,profissional=prof,contato=f"(11) 90000-{len(out)+101:04d}"))
            k+=1
    out.sort(key=lambda p:p["nome"])
    return out
PACIENTES=_pacientes()
PAC={p["nome"]:p for p in PACIENTES}

# ---------------------------------------------------------------------------------------------------------------
# AGENDA: gerada turno a turno de 05/01/2026 a hoje + 21 dias. Visível na 01/02/16 só a partir de 01/07/2026.
# Cada atendimento: data, hora, profissional, sala, paciente, pagador, procedimento, situação, forma, valor, parcelas (a prazo).
# ---------------------------------------------------------------------------------------------------------------
def _gera_agenda():
    rng=random.Random(2026); rows=[]
    pool={CAR:[p for p in PACIENTES if p["profissional"]==CAR],PAU:[p for p in PACIENTES if p["profissional"]==PAU],REN:[p for p in PACIENTES if p["profissional"]==REN]}
    ultima={}      # (prof,paciente) -> data da última consulta/avaliação sem retorno
    ultimo_at={}   # (prof,paciente) -> data do último atendimento
    fim=HOJE+timedelta(days=FUTURO); d=INICIO_GERADOR
    def fator_mes(m): return {1:0.82,2:0.86,7:0.96}.get(m,1.0)
    def fator_dia(wd,per): return 0.92 if (wd==0 and per=="Manhã") or (wd==4) else 1.0
    bloqueio={}    # (prof,paciente) -> data até a qual o paciente não volta (alta ou abandono do acompanhamento)
    def escolhe_paciente(prof,proc,dia,exame=False):
        todos=[p for p in pool[prof]+(pool[CAR] if (prof==PAU and exame) else []) if preco(proc,p["convenio"]) is not None]
        cand=[p for p in todos if bloqueio.get((prof,p["nome"]),dia)<=dia and (dia-ultimo_at.get((prof,p["nome"]),date(2025,1,1))).days>=7]
        if not cand: cand=todos     # todos "de alta": volta quem está há mais tempo sem vir
        # quem está há mais tempo sem vir tem mais chance de voltar (mas não é fila fixa: alguns somem, e entram na lista de retorno)
        pesos=[min(150,(dia-ultimo_at.get((prof,p["nome"]),date(2025,1,1))).days)**1.5+8 for p in cand]
        return rng.choices(cand,pesos)[0]
    def escolhe_retorno(prof,dia):
        for k in [k for k,dt in ultima.items() if (dia-dt).days>70]: del ultima[k]   # retorno não marcado: paciente some (lista de retorno da 02)
        cand=[(k,dt) for k,dt in ultima.items() if k[0]==prof and 14<=(dia-dt).days<=70]
        if not cand: return None
        k,dt=rng.choice(cand); del ultima[k]; return PAC[k[1]]
    def situacao(dia,pag):
        if dia>=HOJE: return "Confirmado" if ((dia-HOJE).days<=2 and rng.random()<0.7) else "Agendado"
        x=rng.random()
        if x<FALTA_PROB[pag]: return "Falta"
        if x<FALTA_PROB[pag]+0.03: return "Cancelado"
        if x<FALTA_PROB[pag]+0.045: return "Remarcado"
        return "Realizado"
    def forma_pgto(valor):
        if valor==0: return "Sem cobrança",None
        x=rng.random()
        if valor>=300: probs=[("Pix",0.30),("Cartão de crédito",0.33),("Cartão de débito",0.15),("Dinheiro",0.05),("A prazo",0.17)]
        else: probs=[("Pix",0.36),("Cartão de crédito",0.28),("Cartão de débito",0.22),("Dinheiro",0.09),("A prazo",0.05)]
        acc=0
        for f,pr in probs:
            acc+=pr
            if x<acc: break
        parc=None
        if f=="Cartão de crédito" and valor>=300 and rng.random()<0.35: parc=2
        return f,parc
    while d<=fim:
        wd=d.weekday()
        if wd<5 and d not in FERIADOS:
            for prof,twd,per,sala,h0 in TURNOS:
                if twd!=wd: continue
                occ=OCUPACAO_ALVO[prof]*fator_mes(d.month)*fator_dia(wd,per)
                t=h0*60; fim_t=(h0+HORAS_TURNO)*60
                while t+20<=fim_t:
                    if rng.random()>=occ: t+=30; continue
                    # check-up cardiológico: consulta + ECG + teste ergométrico no mesmo bloco (particular)
                    if prof==PAU and rng.random()<0.03 and t+90<=fim_t:
                        pac=escolhe_paciente(prof,"Teste ergométrico",d,exame=True)
                        if pac["convenio"]=="Particular":
                            st=situacao(d,"Particular")
                            f,parc=forma_pgto(960) if st=="Realizado" else ("",None)
                            for proc in ("Consulta","ECG","Teste ergométrico"):
                                rows.append(dict(data=d,hora=t,profissional=prof,sala=sala,paciente=pac["nome"],pagador="Particular",procedimento=proc,
                                                 situacao=st,forma=f if st=="Realizado" else "",parcelas=parc if st=="Realizado" else None,valor=preco(proc,"Particular"),checkup=True))
                                t+=DUR[proc]
                            ultimo_at[(prof,pac["nome"])]=d; ultima[(prof,pac["nome"])]=d
                            continue
                    procs=list(PESOS_PROC[prof].items()); proc=rng.choices([p for p,_ in procs],[w for _,w in procs])[0]
                    if t+DUR[proc]>fim_t:
                        curtos=[p for p in PROC_PROF[prof] if DUR[p]<=fim_t-t]
                        if not curtos: break
                        proc=rng.choice(curtos)
                    if proc=="Retorno":
                        pac=escolhe_retorno(prof,d)
                        if pac is None: proc="Consulta" if prof!=REN else "Avaliação endócrina"
                    if proc!="Retorno": pac=escolhe_paciente(prof,proc,d,exame=proc in ("ECG","MAPA","Holter","Teste ergométrico"))
                    pag=pac["convenio"]; valor=preco(proc,pag)
                    st=situacao(d,pag)
                    f,parc=("",None)
                    if st=="Realizado":
                        if pag=="Particular": f,parc=forma_pgto(valor)
                        else: f="Convênio" if valor>0 else "Sem cobrança"
                    rows.append(dict(data=d,hora=t,profissional=prof,sala=sala,paciente=pac["nome"],pagador=pag,procedimento=proc,situacao=st,forma=f,parcelas=parc,valor=valor,checkup=False))
                    if st in ("Realizado","Agendado","Confirmado"):
                        ultimo_at[(prof,pac["nome"])]=d
                        if RETORNO_DIAS[proc]>0 and st=="Realizado":
                            if rng.random()<0.12: bloqueio[(prof,pac["nome"])]=d+timedelta(days=rng.randint(60,120))   # não volta: entra na lista de retorno
                            else: ultima[(prof,pac["nome"])]=d
                        elif proc=="Retorno" and rng.random()<0.25: bloqueio[(prof,pac["nome"])]=d+timedelta(days=rng.randint(45,100))
                    t+=DUR[proc]
        d+=timedelta(days=1)
    rows.sort(key=lambda r:(r["data"],r["hora"],r["sala"]))
    return rows
AGENDA_TODA=_gera_agenda()
AGENDA=[r for r in AGENDA_TODA if r["data"]>=INICIO_AGENDA]        # o que aparece na planilha 01 (e 02, 16)
for _r in AGENDA_TODA:
    assert _r["situacao"]!="Realizado" or _r["data"]<=SEXTA, _r
    assert _r["data"]<HOJE or _r["situacao"] in ("Agendado","Confirmado"), _r
def hora_txt(m): return f"{m//60:02d}:{m%60:02d}"
def periodo(h): return "Manhã" if h<12*60 else "Tarde"

# ---------------------------------------------------------------------------------------------------------------
# PARCELAS A PRAZO (14): particular com pagamento combinado depois (1 ou 2 parcelas de 30 em 30 dias).
# ---------------------------------------------------------------------------------------------------------------
def _parcelas():
    """Parcelas do particular a prazo. Regra do exemplo (e do kit): a clínica não combina um novo pagamento a prazo
    com quem já tem parcela vencida em aberto — nesse dia o pagamento é à vista (Pix). Por isso este gerador percorre
    os atendimentos em ordem de data e, quando o paciente está inadimplente, troca a forma do atendimento na AGENDA."""
    rng=random.Random(14); out=[]
    vistos=set()          # o check-up (3 linhas do mesmo paciente no mesmo dia) é uma única cobrança
    por_paciente={}       # paciente -> parcelas já combinadas
    def inadimplente(pac,d):
        return any(q["vencimento"]<d and (q["pagamento"] is None or q["pagamento"]>d) for q in por_paciente.get(pac,[]))
    for r in sorted((x for x in AGENDA_TODA if x["situacao"]=="Realizado"),key=lambda x:(x["data"],x["hora"])):
        if r["forma"]!="A prazo": continue
        chave=(r["data"],r["paciente"])
        if inadimplente(r["paciente"],r["data"]):
            # sem crédito novo: o atendimento do dia vira à vista (Pix) para todas as linhas do mesmo paciente
            for x in AGENDA_TODA:
                if x["data"]==r["data"] and x["paciente"]==r["paciente"] and x["forma"]=="A prazo": x["forma"]="Pix"; x["parcelas"]=None
            continue
        if r["checkup"]:
            if chave in vistos: continue
            vistos.add(chave); valor=sum(x["valor"] for x in AGENDA_TODA if x["data"]==r["data"] and x["paciente"]==r["paciente"] and x["checkup"]); proc="Check-up cardiológico (consulta + ECG + teste ergométrico)"
        else: valor=r["valor"]; proc=r["procedimento"]
        n=2 if (valor>=300 and rng.random()<0.45) else 1
        for k in range(1,n+1):
            venc=r["data"]+timedelta(days=30*k); val=round(valor/n)
            if k==n: val=valor-round(valor/n)*(n-1)
            pago=None
            if venc<=SEXTA:
                x=rng.random()
                if x<0.87: pago=min(SEXTA,venc+timedelta(days=rng.choice([0,0,0,1,2,3,5])))
            pc=dict(paciente=r["paciente"],procedimento=proc,atendimento=r["data"],profissional=r["profissional"],n=k,total=n,vencimento=venc,valor=val,pago=pago is not None,pagamento=pago)
            out.append(pc); por_paciente.setdefault(r["paciente"],[]).append(pc)
    out.sort(key=lambda p:(p["atendimento"],p["paciente"],p["n"]))
    for p in out: assert p["pagamento"] is None or p["pagamento"]<=SEXTA
    for p in out:
        assert not any(q["vencimento"]<p["atendimento"] and (q["pagamento"] is None or q["pagamento"]>p["atendimento"])
                       for q in por_paciente[p["paciente"]] if q["atendimento"]<p["atendimento"]), p
    return out
PARCELAS=_parcelas()
def status_parcela(p,ref=HOJE):
    if p["pago"] and p["pagamento"]<=ref: return "Paga"
    return "Vencida" if p["vencimento"]<ref else "A vencer"

# ---------------------------------------------------------------------------------------------------------------
# GUIAS E LOTES DE CONVÊNIO (13): uma guia por atendimento realizado de convênio; lote = convênio × mês de competência,
# enviado no dia 5 (útil) do mês seguinte; pago no prazo do convênio, menos a glosa (guias glosadas por inteiro).
# ---------------------------------------------------------------------------------------------------------------
def _guias():
    out=[]; n=0
    for r in AGENDA_TODA:
        if r["situacao"]=="Realizado" and r["pagador"]!="Particular" and r["valor"]>0:
            n+=1; out.append(dict(numero=f"G{r['data'].year}-{n:04d}",data=r["data"],paciente=r["paciente"],convenio=r["pagador"],procedimento=r["procedimento"],profissional=r["profissional"],valor=r["valor"],glosada=False,recurso=""))
    return out
GUIAS=_guias()
LOTES_2025={("Saúde Total",10):(46,4290),("MediPlan",10):(31,2580),("Vida Care",10):(22,1730),("Saúde Total",11):(44,4110),("MediPlan",11):(33,2740),("Vida Care",11):(20,1580),
            ("Saúde Total",12):(38,3560),("MediPlan",12):(27,2250),("Vida Care",12):(17,1350)}
def _lotes():
    rng=random.Random(13); out=[]
    comps=[(2025,m) for m in (10,11,12)]+[(2026,m) for m in range(1,10)]
    for conv,prazo,gh in CONVENIOS:
        for (y,m) in comps:
            gs=[g for g in GUIAS if g["convenio"]==conv and g["data"].year==y and g["data"].month==m]
            if y==2025: n_g,valor=LOTES_2025[(conv,m)]
            else: n_g,valor=len(gs),sum(g["valor"] for g in gs)
            comp=date(y,m,1)
            if (y,m)==(2026,9):   # setembro: guias em separação, lote ainda não enviado
                out.append(dict(convenio=conv,competencia=comp,n_guias=n_g,valor=valor,envio=None,previsao=None,pagamento=None,pago=0,glosa=0,recurso="",recuperado=0,data_recuperacao=None)); continue
            envio=dia_util(date(y+(m==12),(m%12)+1,DIA_ENVIO_LOTE)); prev=envio+timedelta(days=prazo)
            pago=None; vpago=0; glosa=0; rec=""; recup=0; drec=None
            atrasado=(conv=="Vida Care" and (y,m)==(2026,6))     # o lote de junho da Vida Care está atrasado
            if prev<=SEXTA and not atrasado:
                pago=dia_util(prev+timedelta(days=rng.choice([0,0,1,1,2,3])))
                if pago>SEXTA: pago=dia_util_ate(prev)
                alvo=valor*gh*rng.uniform(0.5,1.7)
                if gs:
                    cand=gs[:]; rng.shuffle(cand); soma=0
                    for g in cand:
                        if soma>=alvo or soma+g["valor"]>alvo*1.4: continue
                        g["glosada"]=True; soma+=g["valor"]
                    glosa=soma
                else: glosa=round(alvo/10)*10
                vpago=valor-glosa
                if glosa>=200:
                    x=rng.random()
                    if pago+timedelta(days=35)<=SEXTA and x<0.5:
                        rec="Aceito"; recup=round(glosa*rng.uniform(0.5,0.85)/10)*10; drec=dia_util_ate(min(SEXTA,pago+timedelta(days=rng.randint(28,40))))
                    elif x<0.75 and pago+timedelta(days=20)<=SEXTA: rec="Negado"
                    else: rec="Em recurso"
                    for g in gs:
                        if g["glosada"]: g["recurso"]=rec
            out.append(dict(convenio=conv,competencia=comp,n_guias=n_g,valor=valor,envio=envio,previsao=prev,pagamento=pago,pago=vpago,glosa=glosa,recurso=rec,recuperado=recup,data_recuperacao=drec))
    # história fixa do exemplo: o recurso do lote de maio da Vida Care foi aceito e recebido em setembro; o de março foi negado
    for l in out:
        if l["convenio"]=="Vida Care" and l["competencia"]==date(2026,5,1) and l["glosa"]>0:
            l["recurso"]="Aceito"; l["recuperado"]=round(l["glosa"]*0.7/10)*10; l["data_recuperacao"]=date(2026,9,8)
        if l["competencia"]<date(2026,4,1) and l["recurso"]=="Em recurso": l["recurso"]="Negado"   # recurso antigo sem resposta: a clínica deu por negado
    out.sort(key=lambda l:(l["competencia"],CONVENIOS.index(next(c for c in CONVENIOS if c[0]==l["convenio"]))))
    return out
def dia_util_ate(d):
    while d.weekday()>=5 or d in FERIADOS: d-=timedelta(days=1)
    return d
LOTES=_lotes()
for _l in LOTES:
    assert _l["pagamento"] is None or _l["pagamento"]<=SEXTA, _l
    assert _l["data_recuperacao"] is None or _l["data_recuperacao"]<=SEXTA, _l
def status_lote(l,ref=HOJE):
    if l["envio"] is None: return "Em separação"
    if l["pagamento"] is not None and l["pagamento"]<=ref: return "Em recurso" if (l["recurso"]=="Em recurso") else ("Paga com glosa" if l["glosa"]>0 else "Paga")
    if l["envio"]>ref: return "Em separação"
    return "Atrasada" if l["previsao"]<ref else "Aguardando"
def lote_txt(l): return f"{mes_abrev(l['competencia'].month)}/{l['competencia'].year}"

# ---------------------------------------------------------------------------------------------------------------
# ORÇAMENTOS (15): exames e pacotes particulares apresentados pela recepção desde junho. Aprovados viram atendimentos.
# ---------------------------------------------------------------------------------------------------------------
TIPOS_ORC=["Check-up cardiológico","Exame cardiológico","Avaliação endócrina","Pacote de consultas"]
MOTIVOS_ORC=["Preço","Vai fazer pelo convênio","Vai pensar / sem retorno","Fez em outro lugar","Sem indicação no momento"]
ETAPAS_ORC=["Apresentado","Em análise","Aprovado","Recusado","Sem retorno"]
def _orcamentos():
    rng=random.Random(15); out=[]; vistos=set()
    exames=("MAPA","Holter","Teste ergométrico")
    for r in AGENDA_TODA:
        if r["pagador"]!="Particular" or r["profissional"]!=PAU or r["data"]<date(2026,7,1): continue   # aprovados viram exames na agenda visível (01)
        if r["situacao"] in ("Falta","Cancelado","Remarcado"): continue
        chave=(r["data"],r["paciente"])
        if chave in vistos: continue
        if r["checkup"]:
            vistos.add(chave); itens="Consulta + ECG + teste ergométrico"; tipo="Check-up cardiológico"; valor=960
        elif r["procedimento"] in exames:
            mesmos=[x for x in AGENDA_TODA if x["data"]==r["data"] and x["paciente"]==r["paciente"] and x["procedimento"] in exames]
            vistos.add(chave); itens=" + ".join(x["procedimento"] for x in mesmos); tipo="Exame cardiológico"; valor=sum(x["valor"] for x in mesmos)
        else: continue
        if rng.random()<0.45: continue      # nem todo exame passa por orçamento formal
        # a decisão vem antes do atendimento e nunca depois da última sexta; a apresentação vem antes da decisão
        dec=dia_util_ate(min(r["data"]-timedelta(days=1),SEXTA)-timedelta(days=rng.randint(0,2)))
        apres=dia_util_ate(dec-timedelta(days=rng.randint(4,18)))
        if apres<date(2026,6,1): continue
        assert apres<=dec<=min(r["data"],SEXTA)
        out.append(dict(data=apres,paciente=r["paciente"],profissional=PAU,tipo=tipo,itens=itens,valor=valor,etapa="Aprovado",decisao=dec,motivo="",obs="Agendado para "+r["data"].strftime("%d/%m"),atendimento=r["data"]))
    # não aprovados e em aberto (sem atendimento correspondente)
    outros=[p for p in PACIENTES if p["convenio"]=="Particular"]
    extras=[("Exame cardiológico","MAPA",300),("Exame cardiológico","Holter",350),("Check-up cardiológico","Consulta + ECG + teste ergométrico",960),("Exame cardiológico","Teste ergométrico",450),
            ("Avaliação endócrina","Avaliação endócrina + retorno",400),("Pacote de consultas","Consulta + 2 retornos (acompanhamento)",380),("Exame cardiológico","MAPA + Holter",650)]
    plano=[("Recusado","Preço",-70),("Recusado","Vai fazer pelo convênio",-55),("Sem retorno","Vai pensar / sem retorno",-40),("Recusado","Fez em outro lugar",-32),("Sem retorno","Vai pensar / sem retorno",-26),
           ("Recusado","Preço",-20),("Em análise","",-12),("Sem retorno","Vai pensar / sem retorno",-16),("Em análise","",-6),("Apresentado","",-3),("Apresentado","",-1),("Em análise","",-9),("Recusado","Sem indicação no momento",-45),("Apresentado","",0)]
    for i,(et,mot,dd) in enumerate(plano):
        tipo,itens,valor=extras[i%len(extras)]; pac=outros[(i*7)%len(outros)]
        prof=REN if tipo=="Avaliação endócrina" else (CAR if tipo=="Pacote de consultas" else PAU)
        pac=next(p for p in outros if p["profissional"]==prof and p["nome"] not in {o["paciente"] for o in out}) if prof!=PAU else pac
        dec=None
        if et in ("Recusado","Sem retorno"): dec=min(0,dd+rng.randint(3,12))
        out.append(dict(data=dd,paciente=pac["nome"],profissional=prof,tipo=tipo,itens=itens,valor=valor,etapa=et,decisao=dec,motivo=mot,obs="",atendimento=None))
    def dt(x): return HOJE+timedelta(days=x) if isinstance(x,int) else x
    out.sort(key=lambda o:dt(o["data"]))
    return out
ORCAMENTOS=_orcamentos()
def orc_dt(x): return HOJE+timedelta(days=x) if isinstance(x,int) else x

# ---------------------------------------------------------------------------------------------------------------
# CAIXA (09): fechamento do dia (particular à vista por forma), parcelas pagas, lotes pagos, saídas.
# ---------------------------------------------------------------------------------------------------------------
DISTRIB=0.5; LUCRO_MINIMO=3000
def taxa_cartao(r):
    if r["forma"]=="Cartão de débito": return round(r["valor"]*TAXAS["Cartão de débito"],2)
    if r["forma"]=="Cartão de crédito": return round(r["valor"]*(TAXAS["Cartão de crédito parcelado"] if r["parcelas"] else TAXAS["Cartão de crédito"]),2)
    return 0.0
def producao(prof,m,y=ANO,ate=SEXTA):
    return sum(r["valor"] for r in AGENDA_TODA if r["profissional"]==prof and r["situacao"]=="Realizado" and r["data"].month==m and r["data"].year==y and r["data"]<=ate)
PRODUCAO_REN_DEZ=6200
def material(prof,m,y=ANO,ate=SEXTA):
    """Material e insumo dos atendimentos realizados de um profissional no mês (custo direto da parceria, 11)."""
    return sum(MATERIAL[r["procedimento"]] for r in AGENDA_TODA if r["profissional"]==prof and r["situacao"]=="Realizado" and r["data"].month==m and r["data"].year==y and r["data"]<=ate)
MATERIAL_REN_DEZ=120
TAXA_LIQ_MES={}   # (ano,mês da liquidação) -> taxa de cartão daquele mês, preenchido por lancamentos()
def lancamentos():
    """Tuplas (data, tipo, categoria, paciente ou convênio, referência, descrição, valor, forma, pago) de jan a set/2026."""
    ex=[]
    def add(d,t,c,quem,ref,desc,v,f="Pix",p="Sim"):
        assert not (p=="Sim" and d>SEXTA), (d,desc)
        ex.append((d,t,c,quem,ref,desc,round(v,2),f,p))
    # Particular à vista: o dinheiro entra no caixa na data em que CAI NA CONTA, não na
    # data da venda. Pix e dinheiro caem no dia; débito cai em D+1; crédito à vista em
    # D+30; crédito parcelado, uma parcela a cada 30 dias. Registrar cartão no dia da
    # venda inflava o saldo disponível por até um mês (achado da auditoria de 17/09).
    # O bruto entra aqui e a taxa sai no fim do mês em que caiu, para a receita continuar
    # bruta na 18 e a taxa continuar visível como despesa variável.
    por_liq={}      # (data_de_liquidacao, forma) -> [valor, n_atendimentos, primeira_venda]
    taxa_por_mes={} # mes_de_liquidacao -> taxa somada
    for r in AGENDA_TODA:
        if not (r["situacao"]=="Realizado" and r["pagador"]=="Particular" and r["valor"]>0): continue
        f=r["forma"]
        if f not in ("Pix","Dinheiro","Cartão de débito","Cartão de crédito"): continue
        if f in ("Pix","Dinheiro"):
            parcelas=[(r["data"], r["valor"])]
        elif f=="Cartão de débito":
            parcelas=[(r["data"]+timedelta(days=DIAS_CREDITO["Cartão de débito"]), r["valor"])]
        else:
            n_par=r["parcelas"] or 1
            cota=round(r["valor"]/n_par,2); resto=round(r["valor"]-cota*n_par,2)
            parcelas=[(r["data"]+timedelta(days=DIAS_CREDITO["Cartão de crédito"]*(k+1)),
                       cota+(resto if k==0 else 0)) for k in range(n_par)]
        tx_total=taxa_cartao(r)
        for k,(d_liq,v_par) in enumerate(parcelas):
            kk=(d_liq,f); por_liq.setdefault(kk,[0,0,r["data"]])
            por_liq[kk][0]+=v_par; por_liq[kk][1]+=1
            por_liq[kk][2]=min(por_liq[kk][2], r["data"])
            if tx_total:
                # a taxa acompanha a parcela, rateada pelo peso dela na venda
                taxa_por_mes.setdefault((d_liq.year,d_liq.month),0.0)
                taxa_por_mes[(d_liq.year,d_liq.month)]+=tx_total*v_par/r["valor"]
    TAXA_LIQ_MES.clear(); TAXA_LIQ_MES.update({k:round(x,2) for k,x in taxa_por_mes.items()})
    for (d,f),(v,n,primeira) in sorted(por_liq.items()):
        if f in ("Pix","Dinheiro"):
            desc=f"Fechamento do dia · {n} atendimento{'s' if n>1 else ''} · {f.lower()}"
        else:
            desc=(f"Repasse da operadora · {f.lower()} · {n} pagamento{'s' if n>1 else ''}"
                  f" · vendas desde {primeira.strftime('%d/%m')}")
        add(d,"Entrada","Particular à vista","","Caiu na conta",desc,v,f,
            "Sim" if d<=SEXTA else "Não")
    # parcelas a prazo
    fim_mes_ref=date(2026,9,30)   # regra do exemplo: a receber = parcelas e lotes com previsão até o fim do mês de referência
    for p in PARCELAS:
        desc=f"{p['procedimento']} de {p['atendimento'].strftime('%d/%m')} · parcela {p['n']}/{p['total']}"
        if p["pago"]: add(p["pagamento"],"Entrada","Particular a prazo",p["paciente"],"Parcela",desc,p["valor"],"Pix")
        elif p["vencimento"]<=fim_mes_ref: add(p["vencimento"],"Entrada","Particular a prazo",p["paciente"],"Parcela",desc+f" · vence {p['vencimento'].strftime('%d/%m')}",p["valor"],"Pix","Não")
    # lotes de convênio
    for l in LOTES:
        if l["envio"] is None: continue
        cat="Convênio · "+l["convenio"]
        if l["pagamento"] is not None:
            if l["pagamento"].year==ANO: add(l["pagamento"],"Entrada",cat,l["convenio"],"Lote "+lote_txt(l),f"Pagamento do lote de {lote_txt(l)} ({l['n_guias']} guias"+(f", glosa de R$ {l['glosa']:,.0f}".replace(",",".") if l["glosa"] else "")+")",l["pago"],"Transferência")
            if l["recuperado"] and l["data_recuperacao"]: add(l["data_recuperacao"],"Entrada",cat,l["convenio"],"Lote "+lote_txt(l),f"Recurso de glosa aceito · lote de {lote_txt(l)}",l["recuperado"],"Transferência")
        elif l["previsao"]<=fim_mes_ref: add(l["previsao"],"Entrada",cat,l["convenio"],"Lote "+lote_txt(l),f"Lote de {lote_txt(l)} enviado em {l['envio'].strftime('%d/%m')} · previsão {l['previsao'].strftime('%d/%m')}",l["valor"],"Transferência","Não")
    # custos fixos, pró-labore, repasse, impostos, materiais, taxas, manutenção
    for m in range(1,10):
        for c,v in CUSTOS_FIXOS:
            d=date(2026,m,DIA_FIXO[c]); pago="Sim" if d<=SEXTA else "Não"
            desc={"Recepção (salário e encargos)":"Salário e encargos · Bruna Carvalho","Aluguel e condomínio":"Aluguel e condomínio da clínica","Contador":"Honorários do contador"}.get(c,c)
            add(d,"Saída",c,"","",desc,v,"Boleto" if c in ("Aluguel e condomínio","Contador","Energia, água, internet e telefone") else ("Transferência" if c.startswith("Recepção") else "Cartão de crédito"),pago)
        for n_,v in PRO_LABORE: add(date(2026,m,28),"Saída","Pró-labore dos sócios","","",f"Pró-labore · {n_}",v,"Transferência","Sim" if m<9 else "Não")
        prod=PRODUCAO_REN_DEZ if m==1 else producao(REN,m-1)
        add(date(2026,m,10),"Saída","Repasse à médica parceira",REN,"",f"Repasse · {REN} · 50 % da produção de {mes_abrev(12 if m==1 else m-1)}",round(prod*REPASSE),"Transferência")
        mat=sum(MATERIAL[r["procedimento"]] for r in AGENDA_TODA if r["situacao"]=="Realizado" and r["data"].month==m and r["data"].year==ANO)
        base=mat if m<9 else 900
        add(date(2026,m,8),"Saída","Materiais e insumos de atendimento","","","Eletrodos, manguitos e descartáveis (fornecedor)",round(base*0.6/10)*10,"Boleto")
        d2=date(2026,m,22); add(d2,"Saída","Materiais e insumos de atendimento","","","Reposição de descartáveis e papel para ECG",round(base*0.4/10)*10,"Cartão de crédito","Sim" if d2<=SEXTA else "Não")
        if m<9:
            tx=round(taxa_por_mes.get((ANO,m),0.0),2)
            if tx: add(fim_mes(m),"Saída","Taxas de cartão","","",f"Taxas da operadora de cartão · recebimentos de {mes_abrev(m)}",tx,"Transferência")
    add(date(2026,5,12),"Saída","Manutenção de equipamentos","","","Calibração e manutenção do MAPA e do Holter",800,"Boleto")
    add(date(2026,8,18),"Saída","Manutenção de equipamentos","","","Conserto do eletrocardiógrafo",450,"Pix")
    # imposto: guia paga dia 20 sobre as entradas do mês anterior (alíquota efetiva combinada com o contador); janeiro sobre dezembro/2025 (fictício)
    for m in range(1,10):
        base=base_imposto(ex,m-1) if m>1 else 33000
        add(date(2026,m,20),"Saída","Impostos e taxas","","","Guia de impostos do mês anterior (alíquota efetiva combinada com o contador)",round(base*ALIQ),"Boleto","Sim" if m<9 else "Não")
    # movimentos sócio × clínica (detalhados na 11)
    for m in (2,5,8): add(date(2026,m,6),"Saída","Outras saídas","","","Despesa pessoal · Dra. Carolina Mendes · plano de saúde da família (a acertar)",620,"Boleto")
    for m in (3,7): add(date(2026,m,11),"Saída","Outras saídas","","","Despesa pessoal · Dr. Paulo Andrade · combustível particular (a acertar)",350,"Cartão de crédito")
    add(date(2026,4,14),"Entrada","Outras entradas","","","Devolução de despesa pessoal · Dra. Carolina Mendes",620,"Pix")
    add(date(2026,3,16),"Saída","Pró-labore dos sócios","","","Retirada extra · Dr. Paulo Andrade · adiantamento para congresso",2000,"Transferência")
    add(date(2026,6,19),"Saída","Pró-labore dos sócios","","","Retirada extra · Dra. Carolina Mendes · reforma em casa",1500,"Transferência")
    # distribuição de lucro: 50 % do resultado do trimestre fechado (após pró-labore fixo), meio a meio, paga no dia 10 do mês seguinte
    for q,(m_ini,m_pag) in enumerate(((1,4),(4,7)),start=1):
        lucro=sum(v if t=="Entrada" else -v for d,t,c,quem,ref,desc,v,f,p in ex if p=="Sim" and m_ini<=d.month<=m_ini+2 and not desc.startswith(("Retirada extra","Despesa pessoal","Devolução","Distribuição")))
        if lucro>=LUCRO_MINIMO:
            total=round(lucro*DISTRIB); cotas=[total//2,total-total//2]
            for (n_,_),cota in zip(PRO_LABORE,cotas): add(date(2026,m_pag,10),"Saída","Pró-labore dos sócios","","",f"Distribuição de lucro · {q}º trimestre · {n_}",cota,"Transferência")
    ex.sort(key=lambda x:(x[0],x[1],x[2],x[5]))
    return ex
def base_imposto(ex,m):
    return sum(v for d,t,c,quem,ref,desc,v,f,p in ex if t=="Entrada" and p=="Sim" and d.month==m and d.year==ANO and c!="Outras entradas")
LANCAMENTOS=lancamentos()

def totais_mensais(ex=None):
    ex=ex or LANCAMENTOS; out={}; saldo=SALDO_INICIAL
    fixos={c for c,_ in CUSTOS_FIXOS}
    for m in range(1,13):
        L_=[x for x in ex if x[0].month==m and x[0].year==ANO and x[8]=="Sim"]
        pro=sum(x[6] for x in L_ if x[5].startswith("Pró-labore"))
        por_cat={}
        for x in L_: por_cat[x[2]]=por_cat.get(x[2],0)+x[6]
        ent=sum(x[6] for x in L_ if x[1]=="Entrada"); sai_tot=sum(x[6] for x in L_ if x[1]=="Saída"); saldo+=ent-sai_tot
        out[m]=dict(ent=ent,devol=sum(x[6] for x in L_ if x[5].startswith("Devolução")),ent_sem_devol=ent-sum(x[6] for x in L_ if x[2]=="Outras entradas"),
                    sai_total=sai_tot,sai=sum(x[6] for x in L_ if x[1]=="Saída" and x[2]!="Pró-labore dos sócios"),pessoal=sum(x[6] for x in L_ if x[5].startswith("Despesa pessoal")),
                    pro=pro,extra=sum(x[6] for x in L_ if x[5].startswith("Retirada extra")),distrib=sum(x[6] for x in L_ if x[5].startswith("Distribuição")),
                    fixo=sum(x[6] for x in L_ if x[2] in fixos)+pro,imp=sum(x[6] for x in L_ if x[2]=="Impostos e taxas"),por_cat=por_cat,saldo=saldo)
    return out
TOTAIS=totais_mensais()
def a_pagar(): return sum(v for d,t,c,q,ref,desc,v,f,p in LANCAMENTOS if t=="Saída" and p=="Não")
def a_receber_caixa(): return sum(v for d,t,c,q,ref,desc,v,f,p in LANCAMENTOS if t=="Entrada" and p=="Não")

# ---------------------------------------------------------------------------------------------------------------
# AGENDA: horas disponíveis e atendidas, faltas, ocupação (01/02/17/19).
# ---------------------------------------------------------------------------------------------------------------
def horas_disponiveis(m,y=ANO,ate=None,prof=None,sala=None):
    """Horas dos turnos nos dias úteis do mês até a data (padrão: fim do mês ou ontem, o que vier antes)."""
    lim=fim_mes(m,y) if ate is None else ate
    lim=min(lim,fim_mes(m,y)); d=date(y,m,1); h=0
    while d<=lim:
        if d.weekday()<5 and d not in FERIADOS:
            for p,wd,per,s,h0 in TURNOS:
                if wd==d.weekday() and (prof is None or p==prof) and (sala is None or s==sala): h+=HORAS_TURNO
        d+=timedelta(days=1)
    return h
def agenda_mes(m,y=ANO,ate=SEXTA,prof=None,sala=None,pag=None):
    return [r for r in AGENDA_TODA if r["data"].month==m and r["data"].year==y and r["data"]<=ate and (prof is None or r["profissional"]==prof) and (sala is None or r["sala"]==sala) and (pag is None or r["pagador"]==pag)]
def horas_atendidas(m,y=ANO,ate=SEXTA,**k):
    return sum(DUR[r["procedimento"]] for r in agenda_mes(m,y,ate,**k) if r["situacao"]=="Realizado")/60
def ocupacao(m,y=ANO,ate=SEXTA,**k):
    corte=min(ate,HOJE-timedelta(days=1))
    disp=horas_disponiveis(m,y,corte,prof=k.get("prof"),sala=k.get("sala")); at=horas_atendidas(m,y,corte,**k)
    return at/disp if disp else 0
def faltas(m,y=ANO,ate=SEXTA,**k):
    L_=agenda_mes(m,y,ate,**k); f=sum(1 for r in L_ if r["situacao"]=="Falta"); real=sum(1 for r in L_ if r["situacao"]=="Realizado")
    return f,real,(f/(f+real) if f+real else 0)
def resumo_agenda(m,y=ANO,ate=SEXTA):
    corte=min(ate,HOJE-timedelta(days=1))
    disp=horas_disponiveis(m,y,corte); at=horas_atendidas(m,y,corte); f,real,tx=faltas(m,y,corte)
    return dict(disponiveis=disp,atendidas=at,ocupacao=at/disp if disp else 0,vazias=disp-at,faltas=f,realizados=real,taxa_falta=tx,
                producao=sum(r["valor"] for r in agenda_mes(m,y,ate) if r["situacao"]=="Realizado"))
def lista_retorno(ref=HOJE):
    """Pacientes com consulta/avaliação realizada há mais de N dias (retorno esperado) e sem atendimento posterior marcado ou realizado (02)."""
    n=0
    for r in AGENDA:
        if r["situacao"]!="Realizado" or RETORNO_DIAS[r["procedimento"]]==0 or r["data"]>ref: continue
        if r["data"]+timedelta(days=RETORNO_DIAS[r["procedimento"]])>ref: continue
        depois=[x for x in AGENDA if x["paciente"]==r["paciente"] and x["data"]>r["data"] and x["situacao"] not in ("Falta","Cancelado")]
        if not depois: n+=1
    return n
def ultimas_4_semanas(ref):
    ini=ref-timedelta(days=27); L_=[r for r in AGENDA_TODA if ini<=r["data"]<=ref]
    f=sum(1 for r in L_ if r["situacao"]=="Falta"); real=sum(1 for r in L_ if r["situacao"]=="Realizado")
    at=sum(DUR[r["procedimento"]] for r in L_ if r["situacao"]=="Realizado")/60
    d=ini; disp=0
    while d<=ref:
        if d.weekday()<5 and d not in FERIADOS: disp+=sum(HORAS_TURNO for p,wd,per,s,h0 in TURNOS if wd==d.weekday())
        d+=timedelta(days=1)
    return dict(taxa_falta=f/(f+real) if f+real else 0,ocupacao=at/disp if disp else 0)

# ---------------------------------------------------------------------------------------------------------------
# ESTADO em uma data (Histórico da 17, Indicadores da 20, semanas da 19).
# ---------------------------------------------------------------------------------------------------------------
def estado(ref):
    pago=0; vencido=0; em_aberto=0; nvenc=0
    for p in PARCELAS:
        if p["atendimento"]>ref: continue
        s=status_parcela(p,ref)
        if s=="Paga": pago+=p["valor"]
        elif s=="Vencida": vencido+=p["valor"]; nvenc+=1; em_aberto+=p["valor"]
        else: em_aberto+=p["valor"]
    inad=vencido/(pago+vencido) if pago+vencido else 0
    conv=0; atras=0; glosa_mes=0; pago_mes=0; em_rec=0
    for l in LOTES:
        if l["envio"] is None or l["envio"]>ref: continue
        if l["pagamento"] is None or l["pagamento"]>ref:
            conv+=l["valor"]
            if l["previsao"]<ref: atras+=l["valor"]
        else:
            if l["pagamento"].month==ref.month and l["pagamento"].year==ref.year: glosa_mes+=l["glosa"]; pago_mes+=l["pago"]
            if l["recurso"]=="Em recurso": em_rec+=l["glosa"]
    orcs=[o for o in ORCAMENTOS if orc_dt(o["data"])<=ref]
    abertos=[o for o in orcs if o["etapa"] in ("Apresentado","Em análise") or (o["decisao"] is not None and orc_dt(o["decisao"])>ref)]
    aprov_mes=[o for o in orcs if o["etapa"]=="Aprovado" and orc_dt(o["decisao"]).month==ref.month and orc_dt(o["decisao"]).year==ref.year and orc_dt(o["decisao"])<=ref]
    apres_mes=[o for o in orcs if orc_dt(o["data"]).month==ref.month and orc_dt(o["data"]).year==ref.year]
    return dict(pago=pago,vencido=vencido,parcelas_vencidas=nvenc,inadimplencia=inad,em_aberto=em_aberto,convenio_a_receber=conv,convenio_atrasado=atras,
                glosa_mes=glosa_mes,pago_conv_mes=pago_mes,glosa_pct_mes=glosa_mes/(glosa_mes+pago_mes) if glosa_mes+pago_mes else 0,em_recurso=em_rec,
                orcamentos_n=len(abertos),orcamentos_valor=sum(o["valor"] for o in abertos),aprovados_mes_n=len(aprov_mes),aprovados_mes=sum(o["valor"] for o in aprov_mes),
                apresentados_mes=sum(o["valor"] for o in apres_mes))
def historico():
    out={}
    for m in range(1,10):
        ref=min(fim_mes(m),HOJE); e=estado(ref); t=TOTAIS[m]      # setembro = hoje, como a aba Dados da 17
        ag=resumo_agenda(m,ANO,min(ref,SEXTA)) if m>=INICIO_AGENDA.month else None
        out[m]=dict(entrou=t["ent"],saiu=t["sai_total"],ocupacao=ag["ocupacao"] if ag else None,atendidas=ag["atendidas"] if ag else None,
                    taxa_falta=ag["taxa_falta"] if ag else None,faltas=ag["faltas"] if ag else None,producao=ag["producao"] if ag else None,
                    convenio=e["convenio_a_receber"],atrasado=e["convenio_atrasado"],glosa_pct=e["glosa_pct_mes"],vencido=e["vencido"],inadimplencia=e["inadimplencia"],
                    orcamentos_valor=e["orcamentos_valor"] if m>=6 else None,orcamentos_n=e["orcamentos_n"] if m>=6 else None,aprovados_mes=e["aprovados_mes"] if m>=6 else None,
                    retorno=lista_retorno(ref) if m>=INICIO_AGENDA.month else None)
    return out
HISTORICO=historico()

# ---------------------------------------------------------------------------------------------------------------
# DRE (18), PROVISÃO (10), RESERVA E METAS (12, 19)
# ---------------------------------------------------------------------------------------------------------------
def dre(m):
    """DRE simplificada da 18. Reembolso de sócio ("Outras entradas") fica FORA da receita e do imposto;
    a provisão de 13º e férias (10) entra nas saídas, antes do resultado."""
    pc=TOTAIS[m]["por_cat"]
    rec={c:pc.get(c,0) for c in CAT_ENTRADA if c!="Outras entradas"}
    reemb=pc.get("Outras entradas",0)
    fixos={c:pc.get(c,0) for c,_ in CUSTOS_FIXOS}
    var={c:pc.get(c,0) for c in CAT_VARIAVEIS}
    pro={n:v for n,v in PRO_LABORE}
    receita=sum(rec.values()); imp=round(receita*ALIQ)
    pr=provisao_10()[m]; prov=round(pr["dec13"]+pr["ferias"])
    saidas=sum(fixos.values())+sum(var.values())+sum(pro.values())+prov+imp
    return dict(receita=rec,reembolsos=reemb,fixos=fixos,variaveis=var,pro_labore=pro,receita_total=receita,provisao=prov,impostos=imp,saidas=saidas,resultado=receita-saidas,margem=(receita-saidas)/receita if receita else 0)
ENCARGOS=0.08   # FGTS sobre 13º e férias da recepcionista (exemplo; confirmar com o contador)
_PROV_CACHE={}
def provisao_10():
    if _PROV_CACHE: return _PROV_CACHE
    dec13=sum(v/12*(1+ENCARGOS) for n,p,t,v,_ in PESSOAS if t=="Salário (já nos custos fixos)")+sum(v/12 for n,v in PRO_LABORE)
    ferias=sum(v*(1+1/3)/12*(1+ENCARGOS) for n,p,t,v,_ in PESSOAS if t=="Salário (já nos custos fixos)")
    out={}; sep=0; usado=0
    for m in range(1,10):
        ent=TOTAIS[m]["ent_sem_devol"]; imp=ent*ALIQ; sep+=imp+dec13+ferias; usado+=TOTAIS[m]["imp"]
        out[m]=dict(entradas=ent,imp=imp,dec13=dec13,ferias=ferias,separar=imp+dec13+ferias,usado=TOTAIS[m]["imp"],saldo=sep-usado)
    _PROV_CACHE.update(out); return out
RESERVA_GUARDADA=14000; RESERVA_INICIO_TRI=8000; APORTE_RESERVA=3000
PROVISAO_SEPARADA=17500
META_APROVADO_TRI=18000       # meta de orçamentos aprovados no trimestre (15 e 19)
SEXTAS_TRI=[date(2026,7,3)+timedelta(days=7*i) for i in range(11)]
def reserva_em(ref): return RESERVA_INICIO_TRI+APORTE_RESERVA*sum(1 for m in (7,8) if ref>=fim_mes(m))
def glosa_tri(ref):
    L_=[l for l in LOTES if l["pagamento"] is not None and date(2026,7,1)<=l["pagamento"]<=ref]
    g=sum(l["glosa"] for l in L_); p=sum(l["pago"] for l in L_)
    return g/(g+p) if g+p else 0
def glosa_ano(ref=HOJE,y=ANO):
    """Glosa ÷ (pago + glosa) dos lotes pagos no ano até a data (KPI da 13)."""
    L_=[l for l in LOTES if l["pagamento"] is not None and l["pagamento"].year==y and l["pagamento"]<=ref]
    g=sum(l["glosa"] for l in L_); p=sum(l["pago"] for l in L_)
    return g/(g+p) if g+p else 0
def lotes_atrasados(ref): return sum(1 for l in LOTES if l["envio"] is not None and l["envio"]<=ref and (l["pagamento"] is None or l["pagamento"]>ref) and l["previsao"]<ref)
def prazo_real(ref,desde=date(2026,7,1)):
    """Dias médios entre o envio do lote e o pagamento, nos lotes pagos entre `desde` e `ref` (13: prazo real).
    None quando nenhum lote foi pago no período: a série da 19 mostra "—" e o gráfico não cai para zero."""
    L_=[(l["pagamento"]-l["envio"]).days for l in LOTES if l["pagamento"] is not None and desde<=l["pagamento"]<=ref]
    return round(sum(L_)/len(L_),1) if L_ else None
def recuperado_tri(ref): return sum(l["recuperado"] for l in LOTES if l["data_recuperacao"] is not None and date(2026,7,1)<=l["data_recuperacao"]<=ref)
def aprovados_tri(ref=HOJE): return sum(o["valor"] for o in ORCAMENTOS if o["etapa"]=="Aprovado" and date(2026,7,1)<=orc_dt(o["decisao"])<=ref)
def metas_19():
    """[(objetivo, [(resultado-chave, dono, unidade, partida, meta, atual, sentido, observação, série S1..S11)])]"""
    S=SEXTAS_TRI; ini=date(2026,6,30)
    r1=lambda x: round(x*100,1)
    u4=[ultimas_4_semanas(r) for r in S]
    inad=lambda r: r1(estado(r)["inadimplencia"])
    prov=provisao_10()
    metas=[
     ("Agenda cheia, sem faltas",[
       ("Ocupação da agenda nas últimas 4 semanas (%)",BRU,"%",r1(u4[0]["ocupacao"]),80.0,r1(ultimas_4_semanas(SEXTA)["ocupacao"]),"Maior é melhor","Horas atendidas ÷ disponíveis nas 4 semanas até a sexta (Agenda da planilha 01). Partida = sexta 03/07, que olha 06/06 a 03/07: a agenda da 01 começa em 01/06, então dá para refazer a conta.",[r1(x["ocupacao"]) for x in u4]),
       ("Taxa de falta nas últimas 4 semanas (%)",BRU,"%",r1(u4[0]["taxa_falta"]),5.0,r1(ultimas_4_semanas(SEXTA)["taxa_falta"]),"Menor é melhor","Painel da planilha 02 (faltas ÷ (faltas + realizados)). Confirmação de véspera por mensagem e lista de espera.",[r1(x["taxa_falta"]) for x in u4]),
       ("Pacientes na lista de retorno sem agendamento",BRU,"pacientes",lista_retorno(S[0]),8,lista_retorno(HOJE),"Menor é melhor","Lista de retorno da planilha 02 (hoje). Ligar na segunda-feira; a rotina da semana (03) tem esse passo.",[lista_retorno(r) for r in S[:-1]]+[lista_retorno(HOJE)])]),
     ("Convênio sob controle",[
       ("Glosa nos lotes pagos no ano (%)",PAU,"%",r1(glosa_ano(ini)),4.0,r1(glosa_ano(HOJE)),"Menor é melhor","Painel da planilha 13 (\"Glosa no ano %\": glosa ÷ (pago + glosa) dos lotes pagos no ano). Conferir guias antes do envio (checklist do dia, 04).",[r1(glosa_ano(r)) for r in S]),
       ("Prazo real médio de pagamento dos lotes (dias)",PAU,"dias",prazo_real(ini,date(2026,1,1)),40,prazo_real(HOJE),"Menor é melhor","Dias entre o envio e o pagamento dos lotes pagos no trimestre (aba Lotes da 13, colunas Data de envio e Data do pagamento). Partida = mesma conta nos lotes pagos de janeiro a junho, que estão na mesma aba. Semana sem lote pago fica \"—\".",[prazo_real(r) for r in S]),
       ("Glosa recuperada por recurso no trimestre (R$)",PAU,"R$",0,1000,recuperado_tri(SEXTA),"Maior é melhor","Coluna \"Valor recuperado\" da planilha 13 (lotes com recurso aceito, recebido de julho a setembro).",[recuperado_tri(r) for r in S])]),
     ("Caixa previsível",[
       ("Inadimplência a prazo: vencido ÷ (pago + vencido) (%)",CAR,"%",inad(ini),8.0,inad(HOJE),"Menor é melhor","Painel da planilha 14 (só o que foi combinado a prazo). Régua de cobrança educada na 14.",[inad(r) for r in S]),
       ("Reserva guardada em conta separada (R$)",CAR,"R$",RESERVA_INICIO_TRI,RESERVA_INICIO_TRI+3*APORTE_RESERVA,RESERVA_GUARDADA,"Maior é melhor","Aporte de R$ 3.000 no fechamento de cada mês (planilha 12). A meta do ano é 1 mês de custo fixo com pró-labore (R$ 28.000); a do trimestre, três aportes.",[reserva_em(r) for r in S]),
       ("Conta de provisão de impostos, 13º e férias (R$)",CAR,"R$",8200,round(prov[8]["saldo"]),PROVISAO_SEPARADA,"Maior é melhor","Meta = saldo provisionado de AGOSTO na planilha 10 (último mês fechado; o de setembro ainda muda até o dia 30). Atual = o que já está na conta separada (planilha 12).",
        [8200,8200,8200,8200,11300,11300,11300,11300,11300,14400,17500])])]
    # S11 é a sexta 11/09; o "valor atual" é de hoje (14/09): a última coluna de Semanas recebe o valor atual, como na 17 (Dados = esta sexta)
    return [(obj,[kr[:8]+(kr[8][:-1]+[kr[5]],) for kr in krs]) for obj,krs in metas]

if __name__=="__main__":
    print(len(PACIENTES),"pacientes;",len(AGENDA_TODA),"atendimentos gerados;",len(AGENDA),"na agenda visível (desde 01/06);",len(GUIAS),"guias;",len(PARCELAS),"parcelas a prazo;",len(ORCAMENTOS),"orçamentos;",len(LANCAMENTOS),"lançamentos")
    from collections import Counter
    print("situações (agenda visível):",Counter(r["situacao"] for r in AGENDA))
    print("pagadores (realizados jul-set):",Counter(r["pagador"] for r in AGENDA if r["situacao"]=="Realizado"))
    print("formas:",Counter(r["forma"] for r in AGENDA if r["situacao"]=="Realizado"))
    vis=Counter(r["paciente"] for r in AGENDA); print("atendimentos por paciente (visível): máx",max(vis.values()),"média",round(sum(vis.values())/len(vis),1))
    for m in range(1,10):
        t=TOTAIS[m]; print(f"{m:2d} entrou {t['ent']:9.0f} saiu {t['sai_total']:9.0f} sobrou {t['ent']-t['sai_total']:8.0f} saldo {t['saldo']:8.0f} imp {t['imp']}")
    for m in (7,8,9): print("agenda",m,resumo_agenda(m))
    for m in (7,8): print("DRE",m,round(dre(m)["receita_total"]),round(dre(m)["saidas"]),round(dre(m)["resultado"]),round(dre(m)["margem"]*100,1))
    print("estado hoje:",estado(HOJE))
    print("a pagar",a_pagar(),"a receber (caixa)",a_receber_caixa())
    print("custo-hora",CUSTO_HORA,"hora mínima",HORA_MINIMA_EXATA,HORA_MINIMA,"alvo",HORA_ALVO)
    for p,_,_,_ in PROCEDIMENTOS: print(f"  {p:22s} custo {custo_procedimento(p):7.2f} mín {preco_minimo(p):7.2f} alvo {preco_alvo(p):7.2f}")
    print("lotes:",[(l["convenio"][:5],lote_txt(l),l["valor"],l["pago"],l["glosa"],status_lote(l),l["recurso"]) for l in LOTES if l["competencia"]>=date(2026,5,1)])
    print("produção Renata jul/ago:",producao(REN,7),producao(REN,8),"| lista de retorno:",lista_retorno())
    for obj,krs in metas_19():
        print(obj)
        for kr in krs: print("  ",kr[0][:45],kr[3],kr[4],kr[5],kr[8])
    print("hist:",{m:(round(h["convenio"]),round(h["vencido"]),round(h["inadimplencia"]*100,1),h["orcamentos_n"]) for m,h in HISTORICO.items()})
