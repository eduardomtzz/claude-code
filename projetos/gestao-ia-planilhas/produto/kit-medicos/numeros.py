#!/usr/bin/env python3
"""Gera NUMEROS.md: a "verdade" do exemplo Clínica Vida Plena, com os valores como aparecem nas 20 planilhas recalculadas.
Uso: python3 numeros.py <pasta com as 20 cópias recalculadas>   (as cópias vêm do recalc.py; ver CONVENCOES §10)
Fontes: as cópias (data_only) para tudo o que é fórmula; dados.py para listas (pessoas, turnos, tabela, lotes, orçamentos) e datas.
No fim, a lista de todos os nomes de prompt citados nas planilhas (para a biblioteca de prompts usar exatamente esses)."""
import sys, pathlib, datetime, re
import openpyxl, dados
P=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else "."); AQUI=pathlib.Path(__file__).resolve().parent
def linha_por_rotulo(ws,rotulo,col=1,r0=1,r1=200):
    """Linha cujo rótulo da coluna A começa com o texto dado. Endereço fixo desloca a cada
    mudança de painel e a referência passa a contradizer a planilha (achado da auditoria
    de 18/09, quando o quadro de trimestres desceu três linhas)."""
    for r in range(r0,r1):
        v=ws.cell(row=r,column=col).value
        if isinstance(v,str) and v.startswith(rotulo): return r
    raise AssertionError(f"{ws.title}: rótulo {rotulo!r} não encontrado")
def wb(p): return openpyxl.load_workbook(next(P.glob(p+"-*.xlsx")),data_only=True)
def brl(v,c=0):
    if v in (None,"","—"): return "—"
    v=float(v); s=f"{abs(v):,.{c}f}".replace(",","X").replace(".",",").replace("X",".")
    return ("−R$ " if v<0 else "R$ ")+s
def n(v,c=0):
    if v in (None,"","—"): return "—"
    return f"{float(v):,.{c}f}".replace(",","X").replace(".",",").replace("X",".")
def pct(v,c=1): return "—" if v in (None,"","—") else f"{float(v)*100:.{c}f} %".replace(".",",")
def dt(v):
    if isinstance(v,(datetime.datetime,datetime.date)): return v.strftime("%d/%m/%Y")
    return "—" if v in (None,"") else str(v)
def rel(d): return f"{dt(dados.HOJE+datetime.timedelta(days=d))} ({d:+d} dia{'s' if abs(d)!=1 else ''})" if d else f"{dt(dados.HOJE)} (hoje)"
def row(ws,r,cols): return [ws.cell(row=r,column=c).value for c in cols]
def tab(head,rows):
    # Linha sem rótulo é sobra de intervalo fixo e saía como "| None | None | — |" na
    # referência (achado da auditoria de 18/09). Nenhuma tabela daqui tem linha sem rótulo.
    out=["| "+" | ".join(head)+" |","|"+"|".join("---" for _ in head)+"|"]
    for r in rows:
        if not r or r[0] in (None,"","None"): continue
        out.append("| "+" | ".join(str(x) for x in r)+" |")
    return "\n".join(out)+"\n"
M=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro"]
L=[]; w=L.append
W={p:wb(p) for p in ("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20")}
T=dados.TOTAIS; E=dados.estado(dados.HOJE)

w("# NÚMEROS DO EXEMPLO · Clínica Vida Plena (Kit de Gestão para Médicos)\n")
w("Gerado por `numeros.py` a partir das 20 planilhas recalculadas e de `dados.py` (fonte única). Use estes valores em prompts, slides, manual e aulas: são exatamente os que aparecem nas planilhas.\n")
w("## 1. Referência e regras do exemplo\n")
w("- **Hoje (data de referência, Config = data literal 14/09/2026)**: segunda-feira **14/09/2026**. **Sexta do painel**: **11/09/2026**. Nenhum lançamento pago (caixa, parcela, lote de convênio) tem data depois de 11/09/2026.")
w("- **Meses**: caixa (09) lançado de janeiro a 11/09/2026; agenda (01) registrada de 01/06/2026 a hoje + 21 dias (antes, a recepção só fechava o caixa do dia); **17 Painel da clínica** mostra **setembro em andamento**; **18 Resultado mensal** e **20 Resumo do mês** analisam **agosto de 2026** (último mês fechado; 20 = agosto × julho); **16 Conciliação** está em **agosto**; **19 Metas** = 3º trimestre (semana 11 de 13, 82 % decorrido).")
w("- **Inadimplência (única no kit: 14, 17, 19, 20)** = vencido ÷ (pago + vencido), só do que foi combinado a prazo. Não é vencido ÷ em aberto.")
w(f"- **Alíquota de impostos** (05 a 10, 18): **{dados.ALIQ*100:.0f} %** (alíquota efetiva combinada com o contador; Simples anexo III/V simplificado; só imposto — a taxa da maquininha é despesa variável, conciliada na 16). **Margem mínima** 30 %, **margem alvo** 45 %, **retornos por consulta** 0,4 × 20 min (embutidos no custo da consulta), **custo do dinheiro** (07) 1,5 % ao mês, **repasse** da médica parceira 50 % da produção.")
w("- **Fontes de cadastro**: 01 · Agenda (abas Agenda e Pacientes) é a fonte da agenda e dos pacientes: 02 e 16 copiam a Agenda, 14 copia os Pacientes, 13 · Guias vem dos atendimentos de convênio. Particular à vista entra no caixa (09) pelo fechamento do dia (uma linha por dia e forma); particular a prazo vira parcela (14) e entra no caixa quando paga; convênio vira guia (13) e entra no caixa quando o lote é pago (menos a glosa); cartão entra pelo bruto no dia da venda e as taxas do mês saem numa linha só no fim do mês (o total da 16).")
w("- **Todas as datas são literais**: nenhuma célula do exemplo usa `=HOJE()+n`. O exemplo é uma foto de 14/09/2026 e os números fecham entre os vinte arquivos em qualquer dia em que o cliente abrir. Ao começar a usar com os seus dados, troque a data de referência em Config por `=HOJE()`.\n")
w("- **Nada clínico**: procedimento é só o nome administrativo (consulta, retorno, ECG, MAPA, Holter, teste ergométrico, avaliação endócrina); pacientes têm nome fictício e contato fictício (prefixo 90000); sem diagnóstico, prontuário ou exame.\n")

# ---------- 2. clínica ----------
p05=W["05"]["Painel"]; s06=W["06"]["Precificação"]; s07=W["07"]["Simulador"]; t08=W["08"]["Tabela"]
w("## 2. Clínica, custos e custo da hora (05, 06, 07, 08)\n")
w(tab(["Pessoa","Papel","Remuneração","Valor mensal","Horas de atendimento/mês (planejadas)","Turnos"],[(nm,pap,tipo,brl(v) if v else "—",h or "—",", ".join(f"{dados.DIAS_SEMANA[wd]} {per.lower()} ({sala})" for p_,wd,per,sala,h0 in dados.TURNOS if p_==nm) or "—") for nm,pap,tipo,v,h in dados.PESSOAS]))
w("- Salas: Sala 1 (Carolina de manhã seg/ter/qui e quarta à tarde; Renata ter/qui à tarde) e Sala 2 (Paulo seg/ter/qui à tarde e sexta de manhã). Turnos de 4 h. Feriados de 2026 cadastrados na 01 (07/09 é feriado: setembro tem menos horas).")
w(tab(["Custo fixo","R$/mês"],[(a,brl(v)) for a,v in dados.CUSTOS_FIXOS]+[("**Total de custos fixos (05, 09, 18)**",f"**{brl(dados.CUSTOS_FIXOS_TOTAL)}**"),("Pró-labore dos sócios (2 × 9.000)",brl(dados.PRO_LABORE_TOTAL)),("**Custo total do mês (05 Painel B11)**",f"**{brl(p05['B11'].value)}**")]))
w(f"- **Horas de atendimento planejadas (sócios)**: {n(p05['B12'].value)} h (70 + 70). A médica parceira (35 h) não entra: o repasse dela é custo variável (11).")
w(f"- **Custo da hora de atendimento (05 B13 = 06 Config B7 = 07 Config B5 = 08 Config B7)**: **{brl(p05['B13'].value,2)}** (28.000 ÷ 140 h).")
w(f"- **Hora mínima a cobrar (05)**: exata **{brl(p05['B16'].value,2)}** = 200 ÷ (1 − 0,30 − 0,11); arredondada **{brl(p05['B17'].value)}**. Hora alvo (08 Config): {brl(W['08']['Config']['B14'].value,2)}. Custo direto por hora (pró-labore ÷ horas): {brl(p05['B18'].value,2)}; custo da estrutura por hora (custos fixos ÷ horas, 05 B20 = 11 Config B11): {brl(p05['B20'].value,2)}. **Custo de um horário vazio de 30 min**: {brl(p05['B21'].value,2)}.")
w(tab(["Sensibilidade (05)","Queda","Horas atendidas","Custo-hora","Hora mínima"],[(a,pct(b,0),n(c,1),brl(d,2),brl(e,2)) for a,b,c,d,e,_ in [row(p05,r,(1,2,3,4,5,6)) for r in range(41,46)]]))
w("- A última linha usa as horas atendidas dos sócios em agosto (Painel da 01): o custo-hora real de agosto contra os R$ 200 planejados.")
w("**Precificação (06 = 08): custo cheio, mínimo, alvo e tabelas**\n")
w(tab(["Procedimento","Minutos","Retorno?","Material","Custo cheio","Preço mínimo","Preço alvo","Particular","Margem particular","Situação","Saúde Total","Margem","MediPlan","Margem","Vida Care","Margem"],
      [(a,b,c,brl(d),brl(f,2),brl(g,2),brl(h,2),brl(i),pct(j) if j not in (None,"") else "—",k or "Sem cobrança",brl(l) if l else "—",pct(m) if m not in (None,"") else "—",brl(o) if o else "—",pct(pp) if pp not in (None,"") else "—",brl(q) if q else "—",pct(rr) if rr not in (None,"") else "—") for a,b,c,d,e,f,g,h,i,j,k,l,m,o,pp,q,rr in [row(s06,r,list(range(1,18))) for r in range(5,12)]]))
w(f"- 06 Resumo: procedimentos com particular abaixo do mínimo: {s06['E24'].value}; tabelas de convênio abaixo do custo cheio + imposto: {s06['E25'].value}; maior prejuízo por atendimento em convênio: {brl(s06['E26'].value,2)}. Simulação de exemplo (consulta estendida de 45 min a R$ 480): custo {brl(s06['B36'].value,2)}, mínimo {brl(s06['B37'].value,2)}, alvo {brl(s06['B38'].value,2)}, margem {pct(s06['B39'].value)}.")
w(f"- 08 Tabela (volume de agosto, Painel da 01): produção do mês {brl(t08['G5'].value)}; valor médio por hora {brl(t08['I5'].value,2)} ({pct(t08['K5'].value,0)} contra a hora mínima); particular abaixo do mínimo: {t08['C5'].value}; tabelas de convênio abaixo do custo cheio + imposto: {t08['E5'].value} (o mesmo número do Resumo da 06).")
w(tab(["Procedimento (08)","Realizados em agosto","Produção","Valor médio praticado","Contra o mínimo"],[(a,b,brl(c),brl(d,2),pct(e,0) if e not in (None,"") else "—") for a,b,c,d,e in [row(t08,r,(1,16,17,18,19)) for r in range(8,15)]]))
w(tab(["Valor por hora por pagador (08)","Minutos c/ retorno","Particular","Saúde Total","MediPlan","Vida Care","Hora mínima","Hora alvo"],[(a,n(b,1),brl(c),brl(d) if d else "—",brl(e) if e else "—",brl(f) if f else "—",brl(i),brl(j)) for a,b,c,d,e,f,g,h,i,j in [row(t08,r,list(range(1,11))) for r in range(27,34)]]))
w("**Simulador convênio × particular (07), consulta**\n")
w(tab(["Pagador","Tabela","Prazo","Glosa esperada","Após glosa","Custo do dinheiro","Impostos","Líquido","Custo cheio","Margem","Margem %","Líquido/hora","Contra a hora mínima","Leitura (agenda cheia)"],
      [(a,brl(b),c,pct(d,0),brl(e,2),brl(f,2),brl(g,2),brl(h,2),brl(i,2),brl(j,2),pct(k,0),brl(l,2),f"{float(m)*100:+.0f} %".replace(".",","),nn) for a,b,c,d,e,f,g,h,i,j,k,l,m,nn in [row(s07,r,list(range(1,15))) for r in range(19,23)]]))
w(tab(["Pagador (agenda vazia)","Líquido","Material","Contribuição","Contribuição/hora","Atendimentos = 1 particular","Leitura"],[(a,brl(b,2),brl(c),brl(d,2),brl(e,2),n(f,1) if f not in (None,"") else "—",g) for a,b,c,d,e,f,g in [row(s07,r,(1,2,3,4,5,6,7)) for r in range(31,35)]]))
w(tab(["Mix de agosto (07, consultas realizadas)","Atendimentos","Horas","Líquido","Custo cheio","Resultado","% atend.","% líquido"],[(a,b,n(c,1),brl(d),brl(e),brl(f),pct(g,0),pct(h,0)) for a,b,c,d,e,f,g,h in [row(s07,r,(1,2,3,4,5,6,7,8)) for r in range(43,48)]]+[("**Total**",s07['B49'].value,n(s07['C49'].value,1),brl(s07['D49'].value),brl(s07['E49'].value),f"**{brl(s07['F49'].value)}**","","")]))
w(f"- 07 KPIs: custo cheio da consulta {brl(s07['A5'].value,2)}; hora mínima {brl(s07['C5'].value,2)}; particular líquido por hora {brl(s07['E5'].value,2)}; melhor convênio \"{s07['G5'].value}\"; pior \"{s07['J5'].value}\".\n")

# ---------- 3. caixa ----------
p09=W["09"]["Painel"]
w("## 3. Caixa mês a mês (09 · Caixa da clínica) e repasse (11)\n")
w(f"- Saldo em caixa antes do 1º lançamento (01/01/2026): **{brl(dados.SALDO_INICIAL)}**. Lançamentos: {len(dados.LANCAMENTOS)} linhas; {sum(1 for x in dados.LANCAMENTOS if x[8]=='Sim')} pagas.")
w(tab(["Mês","Entrou","Saiu","Sobrou","Saldo ao fim do mês"],[(M[m-1],brl(T[m]['ent']),brl(T[m]['sai_total']),brl(T[m]['ent']-T[m]['sai_total']),brl(T[m]['saldo'])) for m in range(1,10)]+[("**Jan–ago (8 meses fechados)**",f"**{brl(sum(T[m]['ent'] for m in range(1,9)))}**",f"**{brl(sum(T[m]['sai_total'] for m in range(1,9)))}**",f"**{brl(sum(T[m]['ent']-T[m]['sai_total'] for m in range(1,9)))}**",""),("Setembro = até 11/09 (mês em andamento)","","","","")]))
w("**Entradas por categoria (Pago? = Sim)**\n")
cats=dados.CAT_ENTRADA
w(tab(["Mês"]+cats+["Total"],[(M[m-1],*[brl(T[m]['por_cat'].get(c,0)) for c in cats],brl(T[m]['ent'])) for m in range(1,10)]+[("**Jan–ago**",*[f"**{brl(sum(T[m]['por_cat'].get(c,0) for m in range(1,9)))}**" for c in cats],f"**{brl(sum(T[m]['ent'] for m in range(1,9)))}**")]))
w("**Saídas por categoria (Pago? = Sim)**\n")
fix={c for c,_ in dados.CUSTOS_FIXOS}
scats=["Pró-labore dos sócios","Custos fixos (8 linhas, 10.000)"]+dados.CAT_VARIAVEIS+["Impostos e taxas","Outras saídas"]
def sc(m,c):
    pc=T[m]['por_cat']
    return sum(v for k,v in pc.items() if k in fix) if c.startswith("Custos fixos") else pc.get(c,0)
w(tab(["Mês"]+scats+["Total"],[(M[m-1],*[brl(sc(m,c)) for c in scats],brl(T[m]['sai_total'])) for m in range(1,10)]))
w("- \"Pró-labore dos sócios\" inclui o pró-labore fixo (18.000/mês), as retiradas extras (Paulo 2.000 em 16/03; Carolina 1.500 em 19/06) e a distribuição de lucro dos trimestres fechados (paga dia 10 do mês seguinte, quando o resultado do trimestre após pró-labore passa de R$ 3.000). \"Outras saídas\" = despesas pessoais dos sócios pagas pela clínica (a acertar). \"Outras entradas\" = devolução de despesa pessoal (Carolina, 620 em 14/04).")
w("- Guia de impostos: paga dia 20, 11 % das entradas do mês anterior (sem Outras entradas); janeiro sobre dezembro/2025 (fictício, base 33.000). A guia de setembro (20/09) ainda não foi paga. Taxas de cartão: uma saída no último dia do mês (o total da 16). Repasse: dia 10, 50 % da produção da Dra. Renata no mês anterior.")
w(f"- Setembro: custos fixos com vencimento depois de 11/09, pró-labore (28/09), materiais (22/09) e a guia (20/09) estão como Pago? = Não → **A pagar {brl(p09['K5'].value)}**. **A receber (Pago? = Não) {brl(p09['I5'].value)}** = lotes de convênio enviados com previsão até 30/09 + parcelas a prazo vencidas e a vencer até 30/09.")
w(f"- **09 Painel (Config = Setembro)**: Entrou {brl(p09['A5'].value)} · Saiu {brl(p09['C5'].value)} · Sobrou {brl(p09['E5'].value)} · Saldo acumulado **{brl(p09['G5'].value)}** · A receber {brl(p09['I5'].value)} · A pagar {brl(p09['K5'].value)}.")
w(tab(["Entradas por forma (09, setembro / ano)","No mês","% do mês","No ano","% do ano"],[(a,brl(b),pct(c,0),brl(d),pct(e,0)) for a,b,c,d,e in [row(p09,r,(1,2,3,4,5)) for r in range(45,51)]]))
p11=W["11"]["Painel"]; rp=W["11"]["Repasse"]
w(tab(["11 · Parceira (mês / ano até setembro)","Produção no mês","Repasse devido no mês","Produção no ano","Repasse no ano","Pago no ano","A pagar","Fica com a clínica","Material e insumo (ano)","Margem da parceria (ano)","Custo indireto das horas (informativo)"],[(a,brl(b),brl(c),brl(d),brl(e),brl(f),brl(g),brl(h),brl(i),brl(j),brl(k)) for a,b,c,d,e,f,g,h,i,j,k in [row(p11,linha_por_rotulo(p11,dados.REN),list(range(1,12)))]]))
w(tab(["Repasse (11), mês a mês","Produção","Horas atendidas","Repasse devido (50 %)","Pago em","Valor pago","Fica com a clínica","Material e insumo","Margem da parceria","Custo indireto (inform.)"],[(a,brl(d),n(e,1),brl(g),dt(h),brl(i) if i else "—",brl(k),brl(l),brl(m_),brl(nn)) for a,b,c,d,e,f,g,h,i,j,k,l,m_,nn in [row(rp,r,list(range(1,15))) for r in range(5,14)]]))
w(tab(["11 · Trimestre","Entradas (sem devoluções)","Saídas sem sócios","Pró-labore fixo","Resultado após pró-labore","Fechado?","Distribuível (50 %)","Já distribuído"],[(a,brl(b),brl(c),brl(d),brl(e),f,brl(g),brl(h)) for a,b,c,d,e,f,g,h,i in [row(p11,r,(1,2,3,4,5,6,7,8,9)) for r in [linha_por_rotulo(p11,t) for t in ("1º trimestre","2º trimestre","3º trimestre")]]]))
w(f"- 11 KPIs: repasse devido no mês {brl(p11['A5'].value)} (setembro até 11/09, pago em 10/10); a pagar no ano {brl(p11['C5'].value)}; pró-labore combinado {brl(p11['E5'].value)}/mês; a acertar com a clínica no ano {brl(p11['I5'].value)} (Carolina: retirada extra 1.500 + despesas pessoais 1.860 − devolução 620 = 2.740; Paulo: 2.000 + 700 = 2.700). Setembro: pró-labore ainda não pago (dia 28).\n")

# ---------- 4. agosto ----------
r18=W["18"]["Resultado"]; p18=W["18"]["Painel"]
w("## 4. Agosto de 2026 fechado (18 · Resultado mensal) e julho para comparação\n")
lin=[(6,"Particular à vista"),(7,"Particular a prazo"),(8,"Convênio · Saúde Total"),(9,"Convênio · MediPlan"),(10,"Convênio · Vida Care"),(11,"**Receita total**"),(12,"Reembolsos de sócios (fora da receita e do imposto)"),(22,"Custos fixos (8 linhas)"),(24,"Materiais e insumos"),(25,"Taxas de cartão"),(26,"Repasse à médica parceira"),(27,"Manutenção de equipamentos"),(28,"**Despesas variáveis**"),(32,"Pró-labore fixo (Carolina 9.000 + Paulo 9.000)"),(33,"Provisão de 13º e férias (planilha 10)"),(34,"Impostos provisionados (11 % da receita)"),(35,"**Total de saídas**"),(36,"**Resultado do mês**")]
_rm18=linha_por_rotulo(r18,"Margem")
w(tab(["Linha da DRE","Julho","Agosto","Jan–ago (total)","Média jan–ago"],[(nm,brl(r18.cell(row=r,column=8).value),brl(r18.cell(row=r,column=9).value),brl(r18.cell(row=r,column=14).value),brl(r18.cell(row=r,column=15).value)) for r,nm in lin]+[("**Margem (resultado ÷ receita)**",f"**{pct(r18.cell(row=_rm18,column=8).value)}**",f"**{pct(r18.cell(row=_rm18,column=9).value)}**",pct(r18.cell(row=_rm18,column=14).value),pct(r18.cell(row=_rm18,column=15).value))]))
w(f"- Agosto: receita **{brl(p18['A5'].value)}**, saídas **{brl(p18['C5'].value)}**, resultado **{brl(p18['E5'].value)}**, margem **{pct(p18['G5'].value)}** (julho: {pct(r18['H37'].value)}). Previsto de agosto: receita 46.000, custos fixos 10.000, variáveis 6.000, pró-labore 18.000, provisão de 13º e férias 1.962.")
w(tab(["Comparação (18 Painel, agosto)","Mês","Mês anterior","Variação","Previsto","Vs. previsto","Situação"],[(a,brl(b) if a!="Margem" else pct(b),brl(c) if a!="Margem" else pct(c),(f"{float(d):+.1f} p.p." if a=="Margem" else f"{float(d)*100:+.1f} %").replace(".",","),brl(e) if a!="Margem" else pct(e),(f"{float(f):+.1f} p.p." if a=="Margem" else f"{float(f)*100:+.1f} %").replace(".",","),g) for a,b,c,d,e,f,g in [row(p18,r,(1,3,4,5,6,7,8)) for r in range(9,18)]]))
w("- A DRE não inclui retiradas extras, distribuição de lucro nem despesas pessoais dos sócios (ficam na 11); por isso \"Saiu no mês\" do caixa é diferente do \"Total de saídas\" da DRE (impostos são provisão de 11 % da receita, e não a guia paga; a provisão de 13º e férias, R$ 1.962/mês, vem da planilha 10 e ainda não saiu do caixa).")
w("- Reembolso de sócio (a devolução de despesa pessoal de 14/04, R$ 620) fica numa linha própria, fora da receita e fora da base do imposto: a \"Receita total\" da 18 é o \"Entrou no mês\" da 09 menos essa linha, a mesma base das planilhas 10 e 11.\n")

# ---------- 5. semana ----------
w("## 5. A semana de 11/09/2026 (17 · Painel da clínica, aba Dados)\n")
d17=W["17"]["Dados"]
def fmtv(a,b):
    if b in (None,""): return "—"
    if any(k in a for k in ("Ocupação","Taxa de falta","Glosa","Inadimplência")): return pct(b)
    if any(k in a for k in ("Entrou","Saiu","Sobrou","Convênio","Vencido","valor")): return brl(b)
    return n(b,1 if isinstance(b,float) and b!=int(b) else 0)
w(tab(["Indicador","Valor desta sexta","Limite ou meta","Sentido","Situação","Copiado de"],[(a,fmtv(a,b),fmtv(a,c),d or "—",f,e) for a,b,c,d,e,f in [row(d17,r,(1,2,3,4,5,6)) for r in range(5,20)]]))
p01=W["01"]["Painel"]
w("### Agenda (01 · Agenda e ocupação, Config = Setembro, horas disponíveis até ontem)\n")
w(f"- **Horas disponíveis {n(p01['A5'].value,1)} · atendidas {n(p01['C5'].value,1)} · ocupação {pct(p01['E5'].value)} · vazias {n(p01['G5'].value,1)} · faltas {p01['I5'].value} · produção {brl(p01['K5'].value)}**. Agenda: {len(dados.AGENDA)} linhas de 01/06 a {dt(dados.HOJE+datetime.timedelta(days=dados.FUTURO))} ({sum(1 for r in dados.AGENDA if r['situacao']=='Realizado')} realizados, {sum(1 for r in dados.AGENDA if r['situacao']=='Falta')} faltas, {sum(1 for r in dados.AGENDA if r['situacao'] in ('Agendado','Confirmado'))} agendados/confirmados). Pacientes cadastrados: {len(dados.PACIENTES)}.")
w(tab(["Por profissional (01, setembro)","Disponíveis","Atendidas","Ocupação","Realizados","Faltas","Taxa de falta","Produção"],[(a,n(b,1),n(c,1),pct(d,0),e,f,pct(g,0),brl(h)) for a,b,c,d,e,f,g,h in [row(p01,r,(1,2,3,4,5,6,7,8)) for r in range(11,14)]]))
w(tab(["Por sala (01, setembro)","Disponíveis","Atendidas","Ocupação","Vazias","Turnos por semana"],[(a,n(b,1),n(c,1),pct(d,0),n(e,1),f) for a,b,c,d,e,f in [row(p01,r,(1,2,3,4,5,6)) for r in range(23,25)]]))
w(tab(["Dia (01, setembro)","Manhã disp.","Manhã atend.","Manhã ocup.","Tarde disp.","Tarde atend.","Tarde ocup.","Faltas"],[(a,n(b,1),n(c,1),pct(d,0) if d not in (None,"") else "—",n(e,1),n(f,1),pct(g,0) if g not in (None,"") else "—",h) for a,b,c,d,e,f,g,h in [row(p01,r,(1,2,3,4,5,6,7,8)) for r in range(34,39)]]))
w(tab(["Procedimento (01, setembro)","Realizados","Horas","Produção","Valor médio"],[(a,b,n(c,1),brl(d),brl(e) if e not in (None,"") else "—") for a,b,c,d,e in [row(p01,r,(1,2,3,4,5)) for r in range(44,51)]]))
w(tab(["Pagador (01, setembro)","Realizados","Faltas","Taxa de falta","Produção","Valor médio","% da produção"],[(a,b,c,pct(d,0) if d not in (None,"") else "—",brl(e),brl(f),pct(g,0)) for a,b,c,d,e,f,g in [row(p01,r,(7,8,9,10,11,12,13)) for r in range(44,48)]]))
w(tab(["Próximos 7 dias (01)","Data","Agendados","Confirmados","Horas marcadas","Horas de turno","Vagas (h)"],[(a,dt(b),c,d,n(e,1),n(f,1),n(g,1)) for a,b,c,d,e,f,g in [row(p01,r,(1,2,3,4,5,6,7)) for r in range(61,68)]]))
for m in (7,8):
    ag=dados.resumo_agenda(m); w(f"- **{M[m-1]} fechado (01 com Config = {M[m-1]})**: disponíveis {n(ag['disponiveis'],1)} h · atendidas {n(ag['atendidas'],1)} h · ocupação {pct(ag['ocupacao'])} · faltas {ag['faltas']} ({pct(ag['taxa_falta'])}) · produção {brl(ag['producao'])}.")
p02=W["02"]["Painel"]
w("### Faltas e retornos (02, Config = Setembro)\n")
w(f"- **Taxa de falta {pct(p02['A5'].value)} · faltas {p02['C5'].value} · realizados {p02['E5'].value} · cancelamentos {p02['G5'].value} · remarcações {p02['I5'].value} · na lista de retorno {p02['K5'].value}**.")
w(tab(["Dia da semana (02, setembro)","Realizados","Faltas","Taxa de falta","Cancel.","Remarc."],[(a,b,c,pct(d) if d not in (None,"") else "—",e,f) for a,b,c,d,e,f in [row(p02,r,(1,2,3,4,5,6)) for r in range(11,16)]]))
w(tab(["Pagador (02, setembro)","Realizados","Faltas","Taxa de falta"],[(a,b,c,pct(d) if d not in (None,"") else "—") for a,b,c,d in [row(p02,r,(1,2,3,4)) for r in range(26,30)]]))
w(tab(["Profissional (02, setembro)","Realizados","Faltas","Taxa de falta"],[(a,b,c,pct(d) if d not in (None,"") else "—") for a,b,c,d in [row(p02,r,(1,2,3,4)) for r in range(35,38)]]))
w(tab(["Últimas 8 semanas (02)","Segunda-feira","Realizados","Faltas","Taxa de falta"],[(a,dt(b),c,d,pct(e) if e not in (None,"") else "—") for a,b,c,d,e in [row(p02,r,(1,2,3,4,5)) for r in range(47,55)]]))
w(tab(["Lista de retorno (02)","Profissional","Pagador","Último atendimento","Procedimento","Retorno previsto","Dias além"],[(b,c,d,dt(e),f,dt(g),h) for a,b,c,d,e,f,g,h in [row(p02,r,(1,2,3,4,5,6,7,8)) for r in range(61,86)] if b]))
p13=W["13"]["Painel"]; p14=W["14"]["Painel"]; p15=W["15"]["Painel"]
w("### Caixa, convênios, parcelas e orçamentos na sexta\n")
w(f"- Caixa de setembro até 11/09 (09): entrou **{brl(p09['A5'].value)}**, saiu **{brl(p09['C5'].value)}**, sobrou {brl(p09['E5'].value)}; saldo acumulado {brl(p09['G5'].value)}.")
w(f"- Convênios (13): **a receber {brl(p13['A5'].value)}** (lotes enviados e não pagos) · **atrasado {brl(p13['C5'].value)}** (lote de junho da Vida Care) · recebido no ano {brl(p13['E5'].value)} · glosa no ano {brl(p13['G5'].value)} (**{pct(p13['I5'].value)}**) · em recurso {brl(p13['K5'].value)}.")
w(f"- Parcelas a prazo (14): vence em 7 dias {brl(p14['A5'].value)} · vence em 30 dias {brl(p14['C5'].value)} · em aberto (total) {brl(p14['E5'].value)} · **vencido {brl(p14['G5'].value)}** em **{p14['I5'].value} parcelas** · **inadimplência {pct(p14['K5'].value)}** = {brl(p14['G5'].value)} ÷ ({brl(E['pago'])} pago + {brl(p14['G5'].value)}).")
w(f"- Orçamentos (15): em aberto **{brl(p15['A5'].value)}** · previsão ponderada {brl(p15['C5'].value)} · **aprovado no trimestre {brl(p15['E5'].value)}** ({pct(p15['G5'].value,0)} da meta de {brl(dados.META_APROVADO_TRI)}) · taxa de aprovação {pct(p15['I5'].value,0)} · dias até decidir (média) {n(p15['K5'].value,0)}.\n")

# ---------- 6. convênios ----------
w("## 6. Convênios (13 · Convênios a receber)\n")
w(tab(["Convênio","Prazo (dias)","Glosa histórica (Config)","Lotes no ano","Enviado","Pago","Glosa","Glosa %","Recuperado","A receber","Atrasado","Prazo real (média)"],[(a,dados.PRAZO[a],pct(dados.GLOSA_HIST[a],0),b,brl(c),brl(d),brl(e),pct(f),brl(g),brl(h),brl(i),n(k,0) if k not in (None,"","—") else "—") for a,b,c,d,e,f,g,h,i,j,k,l in [row(p13,r,list(range(1,13))) for r in range(11,14)]]))
w(tab(["Lote","Competência","Guias","Enviado","Envio","Previsão","Pagamento","Pago","Glosa","Recurso","Recuperado","Recebido em","Situação"],
      [(l["convenio"],dados.lote_txt(l),l["n_guias"],brl(l["valor"]),dt(l["envio"]),dt(l["envio"]+datetime.timedelta(days=dados.PRAZO[l["convenio"]])) if l["envio"] else "—",dt(l["pagamento"]),brl(l["pago"]) if l["pagamento"] else "—",brl(l["glosa"]) if l["pagamento"] else "—",l["recurso"] or "—",brl(l["recuperado"]) if l["recuperado"] else "—",dt(l["data_recuperacao"]),dados.status_lote(l)) for l in dados.LOTES]))
w(f"- Guias na aba Guias (jun–set): {sum(1 for g in dados.GUIAS if g['data']>=dados.INICIO_AGENDA)} (uma por atendimento de convênio realizado); glosadas: {sum(1 for g in dados.GUIAS if g['data']>=dados.INICIO_AGENDA and g['glosada'])}. Lotes de out/2025 a mai/2026 vêm dos registros anteriores à agenda (sem detalhe por guia).")
w(tab(["Guias glosadas para recorrer (13 Painel)","Data","Paciente","Convênio","Procedimento","Profissional","Valor","Recurso"],[(b,dt(c),d,e,f,g,brl(h),i or "—") for a,b,c,d,e,f,g,h,i in [row(p13,r,list(range(1,10))) for r in range(53,65)] if b]))
w("")

# ---------- 7. parcelas ----------
w("## 7. Parcelas a prazo e inadimplência (14)\n")
w(tab(["Faixa de atraso","Parcelas","Valor","% do vencido"],[(a,b,brl(c),pct(d,0)) for a,b,c,d,e in [row(p14,r,(1,2,3,4,5)) for r in range(11,16)]]))
w(tab(["Cobrar primeiro (14)","Paciente","Procedimento","Parcela","Vencimento","Valor","Dias de atraso","Faixa"],[(i+1,a,b,c,dt(d),brl(e),f,g) for i,(a,b,c,d,e,f,g,h) in enumerate(row(p14,r,(2,3,4,5,6,7,8,9)) for r in range(20,30)) if a]))
w(tab(["Vencem nos próximos 30 dias (14)","Paciente","Procedimento","Parcela","Vencimento","Valor","Dias para vencer"],[(i+1,a,b,c,dt(d),brl(e),f) for i,(a,b,c,d,e,f) in enumerate(row(p14,r,(2,3,4,5,6,7)) for r in range(34,42)) if a]))
w(f"- Total de parcelas cadastradas: {len(dados.PARCELAS)} (pagas {sum(1 for p in dados.PARCELAS if p['pago'])}), de {len({p['paciente'] for p in dados.PARCELAS})} pacientes; {sum(1 for p in dados.PARCELAS if p['total']==2)//2} atendimentos em 2 parcelas. Régua de cobrança: 1 dia (lembrete), 7 dias (mensagem da recepção), 15 dias (ligação com demonstrativo), 30 dias (conversa e plano de pagamento).\n")

# ---------- 8. orçamentos ----------
w("## 8. Orçamentos (15 · Apresentados × aprovados)\n")
w(tab(["Etapa (15)","Orçamentos","Valor","Ponderado"],[(a,b,brl(c),brl(d) if d not in (None,"") else "—") for a,b,c,d in [row(p15,r,(1,2,3,4)) for r in range(11,16)]]+[("Valor médio dos aprovados",brl(p15['B16'].value),"","")]))
def pd_(x): return "—" if x is None else (rel(x) if isinstance(x,int) else dt(x))
w(tab(["Data","Paciente","Profissional","Tipo","Itens","Valor","Etapa","Decisão","Motivo","Observação"],[(pd_(o["data"]),o["paciente"],o["profissional"],o["tipo"],o["itens"],brl(o["valor"]),o["etapa"],pd_(o["decisao"]),o["motivo"] or "—",o["obs"] or "—") for o in dados.ORCAMENTOS]))
w(tab(["Por tipo (15)","Orçamentos","Aprovados","Recusados / sem retorno","Taxa de aprovação","Valor aprovado","Em aberto"],[(a,b,c,d,pct(e,0),brl(f),brl(g)) for a,b,c,d,e,f,g in [row(p15,r,(1,2,3,4,5,6,7)) for r in range(32,36)] if a]))
w(tab(["Motivo de recusa (15)","Recusados","Valor","% dos recusados"],[(a,b,brl(c),pct(d,0)) for a,b,c,d in [row(p15,r,(1,2,3,4)) for r in range(45,50)] if a]))
w("")

# ---------- 9. cartão ----------
p16=W["16"]["Painel"]
w("## 9. Cartão e taxas (16 · Conciliação, Config = Agosto)\n")
w(f"- **Agosto**: vendas no cartão e Pix {brl(p16['A5'].value)} · taxas **{brl(p16['C5'].value,2)}** ({pct(p16['E5'].value,2)}) · líquido {brl(p16['G5'].value,2)} · ainda vai cair {brl(p16['I5'].value,2)} · a conferir {brl(p16['K5'].value,2)}. \"{p16['A7'].value}\"")
w(tab(["Tipo (16, agosto)","Vendas","Bruto","Taxas","Taxa média","Líquido","% do bruto"],[(a,b,brl(c),brl(d,2),pct(e,2) if e not in (None,"") else "—",brl(f),pct(g,0) if g not in (None,"") else "—") for a,b,c,d,e,f,g in [row(p16,r,(1,2,3,4,5,6,7)) for r in range(11,15)]]))
w(f"- Taxas do exemplo (Config): Pix 0 %, débito 1,5 % (D+1), crédito à vista 3,2 % (D+30), crédito parcelado 3,9 % (parcelas de 30 em 30 dias); sem antecipação. Vendas na aba: {len([r for r in dados.AGENDA if r['situacao']=='Realizado' and r['pagador']=='Particular' and r['forma'] in ('Pix','Cartão de débito','Cartão de crédito')])} (01/06 a 11/09). Taxas de julho (saída do caixa em 31/07): {brl(T[7]['por_cat'].get('Taxas de cartão',0),2)}; de agosto (31/08): {brl(T[8]['por_cat'].get('Taxas de cartão',0),2)}.\n")

# ---------- 10. metas ----------
m19=W["19"]["Metas"]; w19=W["19"]["Semanas"]
w("## 10. Metas do trimestre (19), reserva (12) e provisão (10)\n")
w(f"- 3º trimestre de 2026 (01/07 a 30/09): semana **{W['19']['Config']['B9'].value} de 13**, {pct(W['19']['Config']['B10'].value,0)} decorrido. Resultados-chave: {W['19']['Painel']['A5'].value} · atingidos {W['19']['Painel']['C5'].value} · em risco {W['19']['Painel']['E5'].value} · progresso médio {pct(W['19']['Painel']['G5'].value,0)}.")
rows=[]
for r in range(5,14):
    a=row(m19,r,(1,2,3,4,5,6,7,8,10,11))
    if not a[1]: continue
    s=[w19.cell(row=r,column=c).value for c in range(3,14)]
    rows.append((a[0] or "",a[1],a[2].split()[1] if a[2].startswith("Dr") else a[2].split()[0],a[3],n(a[4],1),n(a[5],1),n(a[6],1),pct(a[7],0) if a[7] not in (None,"") else "—",a[8],a[9]," · ".join(n(x,1) for x in s)))
w(tab(["Objetivo","Resultado-chave","Dono","Unid.","Partida (30/06)","Meta","Atual (14/09)","Progresso","Semáforo","Sentido","S1…S11 (sextas 03/07 → 11/09; S11 = atual)"],rows))
c12=W["12"]["Config"]; p12=W["12"]["Painel"]
w(f"- **12 Reserva**: meta {c12['B8'].value} meses de custo fixo + pró-labore × custo fixo + pró-labore médio {brl(c12['B16'].value)} (jun/jul/ago, como a 09 mostra) = **{brl(p12['A5'].value)}**; reserva hoje **{brl(p12['C5'].value)}**; falta {brl(p12['E5'].value)}; cobre **{n(p12['G5'].value,1)} meses**; semáforo \"{p12['B7'].value}\"; com aporte de {brl(c12['B9'].value)}/mês a meta chega em **{p12['I5'].value}**. Saldo em caixa {brl(c12['B19'].value)} − compromissos não pagos {brl(c12['B20'].value)} = caixa livre {brl(c12['B21'].value)}.")
w(tab(["Meta de caixa do trimestre (12)","Alvo","Atual","Progresso","Prazo","Situação"],[(a,brl(b),brl(c),pct(d,0),dt(f),h) for a,b,c,d,e,f,g,h in [row(p12,r,(1,2,3,4,5,6,7,8)) for r in (43,44,45)]]))
p10=W["10"]["Painel"]; prov=dados.provisao_10()
w(f"- **10 Provisão (Config = Setembro, alíquota 11 %)**: 13º dos sócios 750 + 750 (reserva de dezembro decidida pelos sócios) e da recepcionista {n(prov[9]['dec13']-1500,2)} (com FGTS), férias da recepcionista {n(prov[9]['ferias'],2)} por mês; entradas de setembro até 11/09 {brl(p10['A5'].value)}; a separar no mês {brl(p10['C5'].value)}; **saldo provisionado ao fim de setembro {brl(p10['E5'].value)}**; compromisso do mês seguinte {brl(p10['G5'].value)}; situação {p10['K5'].value}.")
w(tab(["Mês (10)","Entradas (sem Outras)","Provisão 11 %","Total a separar","Guia paga no mês","Saldo provisionado"],[(a,brl(b),brl(c),brl(f),brl(g),brl(j)) for a,b,c,d,e,f,g,h,i,j in [row(p10,r,(1,2,3,4,5,6,7,8,9,10)) for r in range(9,18)]]))
w("")

# ---------- 11. resumo 20 ----------
p20=W["20"]["Painel"]
w("## 11. Resumo do mês (20): agosto × julho de 2026\n")
ptbr=lambda x: "—" if x in (None,"") else str(x).replace(" p.p."," PP").translate(str.maketrans(",.",".,")).replace(" PP"," p.p.")
w(tab(["Indicador","Agosto","Julho","Variação","Meta","Vs. meta","Situação"],[(a,ptbr(b),ptbr(c),ptbr(d),ptbr(e),ptbr(f),g or "informativo") for a,b,c,d,e,f,g in [row(p20,r,(1,2,3,4,5,6,7)) for r in range(5,17)]]))
w("(Valores como o Excel em português mostra; os separadores seguem o idioma do Excel.)")
rs=W["20"]["Resumo"]
w("- Destaques automáticos: "+" ".join(ptbr(rs.cell(row=r,column=1).value).strip() for r in range(22,26) if rs.cell(row=r,column=1).value))
w(f"- Observações da clínica (célula amarela do exemplo): \"{rs['A6'].value}\"\n")

# ---------- 12. histórico 17 ----------
h17=W["17"]["Histórico"]
w("## 12. Histórico mensal (17 · Histórico; jan–ago = Painel mensal da 09, agenda desde junho, convênios/parcelas no fim de cada mês; setembro = Dados)\n")
w(tab(["Mês","Ocupação","Horas atendidas","Vazias","Taxa de falta","Lista de retorno","Entrou","Saiu","Sobrou","Convênio a receber","Atrasado","Glosa no mês","Vencido","Inadimpl.","Orçamentos abertos","Valor"],
      [(a,pct(b,0) if b else "—",n(c,1) if c else "—",n(d,1) if d else "—",pct(e) if e else "—",f if f not in (None,"") else "—",brl(g),brl(h),brl(i),brl(j),brl(k),pct(l),brl(m_),pct(o),pp if pp not in (None,"") else "—",brl(q) if q not in (None,"") else "—") for a,b,c,d,e,f,g,h,i,j,k,l,m_,o,pp,q in [row(h17,r,list(range(1,17))) for r in range(5,14)]]))
w("- Agenda: a planilha 01 começou em junho (antes fica em branco). Orçamentos: o funil (15) começou em junho. Glosa no mês = dos lotes pagos naquele mês; no Dados (setembro), o acumulado do ano.\n")

# ---------- 13. rotina, checklist ----------
p03=W["03"]["Painel"]; p04=W["04"]["Painel"]
w("## 13. Rotina (03) e checklist do dia (04)\n")
w(f"- **03 Rotina**: 8 rotinas (3 de segunda = 12 min, com a recepção; 5 de sexta = 18 min; **30 min/semana**); registradas S29 a S36 (20/07 a 07/09/2026); semana atual {p03['C5'].value}; aderência nas últimas 4 semanas **{pct(p03['A5'].value,0)}**; rotina mais pulada: \"{next((p03.cell(row=r,column=2).value,p03.cell(row=r,column=7).value) for r in range(29,38) if p03.cell(row=r,column=8).value)[0]}\".")
w(f"- **04 Checklist do dia**: dias registrados {p04['A5'].value} (dias úteis de 01/06 a 11/09) · abertura completa nos últimos 20 dias {pct(p04['C5'].value,0)} · fechamento completo {pct(p04['E5'].value,0)} · dias com pendência {p04['G5'].value} · itens pendentes no total {p04['I5'].value}. Item mais esquecido no fechamento: \"{max(((p04.cell(row=r,column=6).value,p04.cell(row=r,column=8).value) for r in range(26,32)),key=lambda x:x[1] or 0)[0]}\".")
w("")

# ---------- 14. prompts citados ----------
w("## 14. Nomes de prompt citados nas planilhas (a biblioteca de prompts deve usar exatamente estes)\n")
nomes=set()
for f in sorted(AQUI.glob("build_*.py")):
    for m_ in re.finditer(r'((?:Agenda|Preço|Caixa|Recebíveis|Painel) \d\d · [^"\\\']+?)(?=\\"|"|\')',f.read_text()):
        nomes.add(m_.group(1).strip())
grupos={}
for nm in sorted(nomes): grupos.setdefault(nm.split(" ")[0],[]).append(nm)
for g in ("Agenda","Preço","Caixa","Recebíveis","Painel"):
    if g in grupos:
        w(f"**{g}**\n")
        for nm in grupos[g]: w(f"- {nm}")
        w("")
w(f"Total: {len(nomes)} nomes citados em {sum(1 for _ in AQUI.glob('build_*.py'))} planilhas. Os números das planilhas citadas nos \"Como usar\" (01 a 20) são os desta lista de arquivos.")
open(AQUI/"NUMEROS.md","w").write("\n".join(L))
print("NUMEROS.md gerado:",len("\n".join(L)),"caracteres;",len(nomes),"prompts citados")
