#!/usr/bin/env python3
"""Gera NUMEROS.md: a "verdade" do exemplo Ferraz & Lima, com os valores como aparecem nas 20 planilhas recalculadas.
Uso: python3 numeros.py <pasta com as 20 cópias recalculadas>   (as cópias vêm do recalc.py; ver CONVENCOES §10)
Fontes: as cópias (data_only) para tudo o que é fórmula; dados.py para listas (casos, propostas, parcelas) e datas."""
import sys, pathlib, datetime
import openpyxl, dados
P=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else ".")
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
    out=["| "+" | ".join(head)+" |","|"+"|".join("---" for _ in head)+"|"]
    for r in rows: out.append("| "+" | ".join(str(x) for x in r)+" |")
    return "\n".join(out)+"\n"
M=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro"]
L=[]; w=L.append
W={p:wb(p) for p in ("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20")}
T=dados.TOTAIS; E=dados.estado(dados.HOJE)

w("# NÚMEROS DO EXEMPLO · Ferraz & Lima Advocacia (Kit de Gestão para Advogados)\n")
w("Gerado por `numeros.py` a partir das 20 planilhas recalculadas e de `dados.py` (fonte única). Use estes valores em prompts, slides, manual e aulas: são exatamente os que aparecem nas planilhas.\n")
w("## 1. Referência e regras do exemplo\n")
w("- **Hoje (data de referência, Config = HOJE())**: segunda-feira **14/09/2026**. **Sexta do painel**: **11/09/2026**. Nenhum lançamento pago (caixa, parcela, hora) tem data depois de 11/09/2026.")
w("- **Meses**: caixa (09) e horas (16) lançados de janeiro (caixa) / julho (horas) a 11/09/2026; **17 Painel do escritório** mostra **setembro em andamento**; **18 Resultado mensal** e **20 Resumo do mês** analisam **agosto de 2026** (último mês fechado; 20 = agosto × julho); **19 Metas** = 3º trimestre (semana 11 de 13, 82 % decorrido).")
w("- **Inadimplência (única no kit: 14, 17, 19, 20)** = vencido ÷ (pago + vencido). Não é vencido ÷ em aberto.")
w(f"- **Alíquota de impostos** (05, 06, 08, 09, 10, 18): **{dados.ALIQ*100:.0f} %**. **Margem mínima** 30 %, **margem alvo** 45 %, **folga de horas** 20 %.")
w("- **Fonte do cadastro de casos**: 13 · Carteira (aba Casos). 01, 02, 04, 08, 14 e 16 copiam de lá. Parcela paga na 14 = entrada no caixa da 09 (na data do pagamento); recebido do caso na 13 = soma das parcelas pagas (2025 + 2026; as de 2025 estão no saldo inicial do caixa).")
w("- **Datas relativas**: prazos (01/02), vencimentos em aberto (14) e propostas abertas (15) são `=HOJE()+n`; ao abrir em outro dia, esses números deslizam. Histórico (abertura, parcelas pagas, caixa, horas) é fixo.\n")

# ---------- 2. escritório ----------
p05=W["05"]["Painel"]; c08=W["08"]["Config"]; c16=W["16"]["Config"]
w("## 2. Escritório, custos e custo-hora (05, 06, 08, 16)\n")
w(tab(["Pessoa","Papel","Pró-labore / bolsa (R$/mês)","Horas de trabalho","Horas faturáveis (meta)","Custo-hora na 16 (R$)"],
      [(nme,pap,brl(c),dados.HORAS_TRABALHO[nme],h,brl(dados.custo_hora_pessoa(nme),2)) for nme,pap,c,h in dados.PESSOAS]))
w(tab(["Custo fixo","R$/mês"],[(a,brl(v)) for a,v in dados.CUSTOS_FIXOS]+[("**Total de custos fixos (05, 09, 18)**",f"**{brl(dados.CUSTOS_FIXOS_TOTAL)}**"),("Pró-labore dos sócios (2 × 6.000)",brl(dados.PRO_LABORE_TOTAL)),("**Custo total do mês (05 Painel B11)**",f"**{brl(p05['B11'].value)}**")]))
w(f"- **Horas faturáveis no mês (meta, todas as pessoas)**: {n(p05['B12'].value)} h · horas de trabalho: {n(p05['B20'].value)} h · tempo faturável planejado (05): {pct(p05['B21'].value,0)}.")
w(f"- **Custo-hora do escritório (05 B13 = 06 B11 = 08 Config B7 = 16 Config B23)**: **{brl(p05['B13'].value,2)}** (18.500 ÷ 280 h; em 06/08 digitado como 66,0714).")
w(f"- **Hora mínima a cobrar (05)**: exata **{brl(p05['B16'].value,2)}** = 66,07 ÷ (1 − 0,30 − 0,08); arredondada **{brl(p05['B17'].value)}**. A 06 mostra a mesma conta ({brl(W['06']['Simulador']['B15'].value,2)}).")
w(f"- **Hora mínima com folga (08, 20 % de horas não previstas)**: **{brl(c08['B12'].value,2)}** = 66,07 × 1,20 ÷ 0,62. **Hora alvo com folga (08)**: **{brl(c08['B13'].value,2)}** (margem alvo 45 %).")
w(f"- **Custos indiretos por hora faturável (05)**: {brl(p05['B19'].value,2)} (custos fixos sem a bolsa, {brl(p05['B18'].value)}, ÷ 280 h). Custos fixos sem a equipe (16 Config): {brl(c16['B8'].value)}.")
w(tab(["Por pessoa (05)","Horas faturáveis","Ocupação","Custo direto/h","Custo-hora completo","Hora mínima"],[(a,n(b),pct(c,0),brl(d,2),brl(e,2),brl(f,2)) for a,b,c,d,e,f in [row(p05,r,(1,3,4,5,6,7)) for r in (26,27,28)]]))
w(tab(["Sensibilidade (05)","Queda","Horas faturáveis","Custo-hora","Hora mínima"],[(a,pct(b,0),n(c),brl(d,2),brl(e,2)) for a,b,c,d,e,_ in [row(p05,r,(1,2,3,4,5,6)) for r in range(41,45)]]))
p08=W["08"]["Referência"]
w(f"- **08 Tabela de referência**: casos abaixo do mínimo com folga: **{p08['E5'].value}**; falta até o mínimo: {brl(p08['G5'].value)}; valor por hora médio dos casos: {brl(p08['I5'].value,2)}.")
w(tab(["Área (08)","Casos","Contratado","Horas estimadas","Valor/hora","Contra a hora mínima com folga","Abaixo do mínimo","Falta até o mínimo"],[(a,b,brl(c),n(d),brl(e,2),f"{float(f)*100:+.0f} %".replace(".",","),g,brl(h)) for a,b,c,d,e,f,g,h in [row(p08,r,(1,2,3,4,5,6,7,8)) for r in range(54,59)]]))
w("")

# ---------- 3. caixa ----------
w("## 3. Caixa mês a mês (09 · Caixa do escritório)\n")
w(f"- Saldo em caixa antes do 1º lançamento (01/01/2026): **{brl(dados.SALDO_INICIAL)}** (já com honorários recebidos em 2025). Lançamentos: {len(dados.LANCAMENTOS)} linhas; {sum(1 for x in dados.LANCAMENTOS if x[8]=='Sim')} pagas.")
w(tab(["Mês","Entrou","Saiu","Sobrou","Saldo ao fim do mês"],[(M[m-1],brl(T[m]['ent']),brl(T[m]['sai_total']),brl(T[m]['ent']-T[m]['sai_total']),brl(T[m]['saldo'])) for m in range(1,10)]+[("**Jan–ago (8 meses fechados)**",f"**{brl(sum(T[m]['ent'] for m in range(1,9)))}**",f"**{brl(sum(T[m]['sai_total'] for m in range(1,9)))}**",f"**{brl(sum(T[m]['ent']-T[m]['sai_total'] for m in range(1,9)))}**",""),("Setembro = até 11/09 (mês em andamento)","","","","")]))
w("**Entradas por categoria (Pago? = Sim)**\n")
cats=dados.CAT_ENTRADA
w(tab(["Mês"]+cats+["Total"],[(M[m-1],*[brl(T[m]['por_cat'].get(c,0)) for c in cats],brl(T[m]['ent'])) for m in range(1,10)]+[("**Jan–ago**",*[f"**{brl(sum(T[m]['por_cat'].get(c,0) for m in range(1,9)))}**" for c in cats],f"**{brl(sum(T[m]['ent'] for m in range(1,9)))}**")]))
w("**Saídas por categoria (Pago? = Sim)**\n")
scats=["Pró-labore dos sócios","Custos fixos (8 linhas, 6.500)","Impostos e taxas","Custas e despesas de processo","Deslocamento e viagens","Outras saídas"]
fix={c for c,_ in dados.CUSTOS_FIXOS}
def sc(m,c):
    pc=T[m]['por_cat']
    return sum(v for k,v in pc.items() if k in fix) if c.startswith("Custos fixos") else pc.get(c,0)
w(tab(["Mês"]+scats+["Total"],[(M[m-1],*[brl(sc(m,c)) for c in scats],brl(T[m]['sai_total'])) for m in range(1,10)]))
w("- \"Pró-labore dos sócios\" inclui o pró-labore fixo (12.000/mês), as retiradas extras (Rafael 1.500 em 16/03; Marina 2.000 em 19/06) e a distribuição de lucro dos trimestres fechados (paga dia 10 do mês seguinte: 1º tri em abril, 2º tri em julho). \"Outras saídas\" = despesas pessoais dos sócios pagas pelo escritório (a acertar). \"Outras entradas\" = devolução de despesa pessoal (Marina, 480 em 14/04).")
w("- Guia de impostos: paga dia 20, 8 % das entradas do mês anterior (sem Outras entradas); janeiro sobre dezembro/2025 (fictício, base 20.600). A guia de setembro (20/09) ainda não foi paga.")
w("- Setembro: custos fixos com vencimento depois de 11/09 (telefone, anuidades, marketing, material), pró-labore (28/09) e a guia (20/09) estão como Pago? = Não → **A pagar {brl(W['09']['Painel']['K5'].value)}**. **A receber (Pago? = Não) {brl(W['09']['Painel']['I5'].value)}** = parcelas vencidas + a vencer até 30/09 (o cronograma completo fica na 14).")
p09=W["09"]["Painel"]
w(f"- **09 Painel (Config = Setembro)**: Entrou {brl(p09['A5'].value)} · Saiu {brl(p09['C5'].value)} · Sobrou {brl(p09['E5'].value)} · Saldo acumulado **{brl(p09['G5'].value)}** · A receber {brl(p09['I5'].value)} · A pagar {brl(p09['K5'].value)}.")
w(tab(["Por cliente (09, ano até 11/09)","Entrou no ano","A receber (Pago? = Não)","Custas pagas no ano"],[(a,brl(c),brl(e),brl(f)) for a,b,c,e,f in [row(p09,r,(1,2,3,5,6)) for r in range(45,63)]]))
p11=W["11"]["Painel"]
w(tab(["11 · Trimestre","Entradas (sem devoluções)","Saídas sem sócios","Pró-labore fixo","Resultado após pró-labore","Fechado?","Distribuível (50 %)","Já distribuído"],[(a,brl(b),brl(c),brl(d),brl(e),f,brl(g),brl(h)) for a,b,c,d,e,f,g,h,i in [row(p11,r,(1,2,3,4,5,6,7,8,9)) for r in (32,33,34)]]))
w(f"- 11: pró-labore combinado {brl(p11['A5'].value)}/mês; a acertar com o escritório no ano {brl(p11['G5'].value)} (Marina: retirada extra 2.000 + despesas pessoais 1.440 − devolução 480 = 2.960; Rafael: 1.500 + 600 = 2.100). Setembro: pró-labore ainda não pago (dia 28).\n")

# ---------- 4. agosto fechado ----------
r18=W["18"]["Resultado"]; p18=W["18"]["Painel"]
w("## 4. Agosto de 2026 fechado (18 · Resultado mensal) e julho para comparação\n")
lin=[(6,"Honorários fixos"),(7,"Honorários por hora"),(8,"Honorários de êxito"),(9,"Consultoria e pareceres"),(10,"Reembolso de custas"),(11,"Outras entradas"),(12,"**Receita total**"),(22,"Custos fixos (8 linhas)"),(24,"Custas e despesas de processo"),(25,"Deslocamento e viagens"),(26,"**Despesas de casos e viagens**"),(30,"Pró-labore fixo (Marina 6.000 + Rafael 6.000)"),(31,"Impostos provisionados (8 % da receita)"),(32,"**Total de saídas**"),(33,"**Resultado do mês**")]
w(tab(["Linha da DRE","Julho","Agosto","Jan–ago (total)","Média jan–ago"],[(nm,brl(r18.cell(row=r,column=8).value),brl(r18.cell(row=r,column=9).value),brl(r18.cell(row=r,column=14).value),brl(r18.cell(row=r,column=15).value)) for r,nm in lin]+[("**Margem (resultado ÷ receita)**",f"**{pct(r18['H34'].value)}**",f"**{pct(r18['I34'].value)}**",pct(r18['N34'].value),pct(r18['O34'].value))]))
w(f"- Agosto: receita **{brl(p18['A5'].value)}**, saídas **{brl(p18['C5'].value)}**, resultado **{brl(p18['E5'].value)}**, margem **{pct(p18['G5'].value)}** (julho: {pct(r18['H34'].value)}; variação **−7,1 p.p.**). Previsto de agosto: receita 27.000, custos fixos 6.500, despesas 400, pró-labore 12.000 → resultado previsto 5.940, margem prevista 22,0 %.")
w(tab(["Comparação (18 Painel, agosto)","Mês","Mês anterior","Variação","Previsto","Vs. previsto","Situação"],[(a,brl(b) if a!="Margem" else pct(b),brl(c) if a!="Margem" else pct(c),(f"{float(d):+.1f} p.p." if a=="Margem" else f"{float(d)*100:+.1f} %").replace(".",","),brl(e) if a!="Margem" else pct(e),(f"{float(f):+.1f} p.p." if a=="Margem" else f"{float(f)*100:+.1f} %").replace(".",","),g) for a,b,c,d,e,f,g in [row(p18,r,(1,3,4,5,6,7,8)) for r in range(9,17)]]))
w("- A DRE não inclui retiradas extras, distribuição de lucro nem despesas pessoais dos sócios (ficam na 11); por isso \"Saiu no mês\" do caixa (agosto: 21.897) é diferente do \"Total de saídas\" da DRE (21.212: impostos são provisão de 8 % da receita, e não a guia paga).\n")

# ---------- 5. semana ----------
w("## 5. A semana de 11/09/2026 (17 · Painel do escritório, aba Dados)\n")
d17=W["17"]["Dados"]
w(tab(["Indicador","Valor desta sexta","Limite ou meta","Sentido","Situação","Copiado de"],[(a,(pct(b) if isinstance(b,float) and b<1 and 'fatur' in a.lower() or 'Inadimpl' in a else (brl(b) if any(k in a for k in ('Entrou','Saiu','Sobrou','receber','Vencido','valor')) else n(b,1 if isinstance(b,float) and b!=int(b) else 0))),("—" if c in (None,"") else (pct(c,0) if isinstance(c,float) and c<1 else (brl(c) if any(k in a for k in ('Entrou','Saiu','Sobrou','receber','Vencido','valor')) else n(c)))),d or "—",f,e) for a,b,c,d,e,f in [row(d17,r,(1,2,3,4,5,6)) for r in range(5,19)]]))
p01=W["01"]["Painel"]; PZ=dados.resumo_prazos()
w(f"### Prazos (01 · Agenda de prazos, {dt(dados.HOJE)})\n")
w(f"- **Atrasados {p01['A5'].value} · Hoje {p01['C5'].value} · Próximos 7 dias {p01['E5'].value}** · de 8 a 30 dias {p01['G5'].value} · abertos no total {p01['I5'].value} · feitos {p01['K5'].value}. Agenda: {len(dados.PRAZOS())} linhas (prazo principal de cada caso ativo = próxima ação da 02, mais {len(dados.PRAZOS_EXTRAS)} compromissos extras, 2 já feitos).")
w(tab(["#","Processo","Cliente","Tipo de prazo","Data","Dias","Situação","Responsável"],[(i+1,a,b,c,dt(d),e,f,g) for i,(a,b,c,d,e,f,g) in enumerate(row(p01,r,(2,3,4,5,6,7,8)) for r in range(10,40)) if a]))
w(tab(["Carga por responsável (01)","Abertos","Atrasados","Hoje","Em alerta (7 dias)","Mais antigo em aberto","Feitos"],[(a,b,c,d,e,dt(f),g) for a,b,c,d,e,f,g in [row(p01,r,(1,3,4,5,6,7,8)) for r in (43,44,45)] if a]))
w("- Júlia Prado (estagiária) responde pelos prazos de juntada de documentos; os casos continuam com o sócio responsável (por isso ela tem prazos na 01 e nenhum caso na 02, 04 e 13).")
p02=W["02"]["Painel"]
w(f"### Andamento (02): casos ativos {p02['A5'].value} · ação atrasada {p02['C5'].value} · hoje ou esta semana {p02['E5'].value} · sem próxima ação {p02['G5'].value} · parados há mais de 30 dias {p02['I5'].value} · encerrados {p02['K5'].value}\n")
w(tab(["Fase (02)","Casos","Ação atrasada","Esta semana","Sem próxima ação","Parados"],[row(p02,r,(1,2,3,4,5,6)) for r in range(9,17)]))
w(tab(["Área (02)","Ativos","Encerrados","Ação atrasada","Parados"],[row(p02,r,(8,9,10,11,12)) for r in range(9,14)]))
w("- Parados (>30 dias sem atualização): Bistrô 42 (execução, 41 dias), Oficina Mecânica Central (inicial, aguardando audiência, 36), Luciana Farias (acordo, aguardando homologação, 33), Helena Duarte (execução, 47).")
p16=W["16"]["Painel"]
w("### Horas (16 · Horas por caso, Config = Setembro; setembro até 11/09)\n")
w(f"- **Setembro (até 11/09)**: horas **{n(p16['A5'].value,1)}** · faturáveis **{n(p16['C5'].value,1)}** ({pct(p16['E5'].value)}) · custo das horas {brl(p16['G5'].value)} · meta de faturáveis atingida {pct(p16['I5'].value)} · consomem mais do que pagam: {p16['K5'].value}.")
H=dados.HISTORICO
w(f"- **Agosto (fechado)**: {n(H[8]['horas'],1)} h, faturáveis {n(H[8]['faturaveis'],1)} h ({pct(H[8]['faturaveis']/H[8]['horas'])}). **Julho**: {n(H[7]['horas'],1)} h, faturáveis {n(H[7]['faturaveis'],1)} h ({pct(H[7]['faturaveis']/H[7]['horas'])}). Lançamentos: {len(dados.HORAS)} linhas de 01/07 a 11/09; o controle de horas começou em julho (antes: \"horas gastas antes\" por caso).")
w(tab(["Pessoa","Set (h)","Set faturáveis","Ago (h)","Ago faturáveis","Jul (h)","Jul faturáveis","Meta faturável/mês","Custo-hora"],[(nm,n(dados.horas_pessoa_mes(nm,9)[0],1),n(dados.horas_pessoa_mes(nm,9)[1],1),n(dados.horas_pessoa_mes(nm,8)[0],1),n(dados.horas_pessoa_mes(nm,8)[1],1),n(dados.horas_pessoa_mes(nm,7)[0],1),n(dados.horas_pessoa_mes(nm,7)[1],1),h,brl(dados.custo_hora_pessoa(nm),2)) for nm,_,_,h in dados.PESSOAS]))
w(tab(["Casos para olhar primeiro (16, ativos)","Cliente","Responsável","Horas estimadas","Horas gastas","Custo das horas","Contratado","Margem","Situação"],[(a,b,c,d,n(e,1),brl(f),brl(g),brl(h),i) for a,b,c,d,e,f,g,h,i in [row(p16,r,(2,3,4,5,6,7,8,9,10)) for r in range(12,20)] if a]))
p14=W["14"]["Painel"]; p13=W["13"]["Painel"]; p15=W["15"]["Painel"]
w(f"### Caixa, carteira, parcelas e propostas na sexta\n")
w(f"- Caixa de setembro até 11/09 (09): entrou **{brl(p09['A5'].value)}**, saiu **{brl(p09['C5'].value)}**, sobrou {brl(p09['E5'].value)}; saldo acumulado {brl(p09['G5'].value)}.")
w(f"- Carteira (13): contratado **{brl(p13['A5'].value)}** · recebido **{brl(p13['C5'].value)}** · **a receber {brl(p13['E5'].value)}** ({pct(p13['G5'].value,0)} recebido) · **casos ativos {p13['I5'].value}** · encerrados {p13['K5'].value}. A receber inclui o êxito esperado de casos ativos e o que ainda não virou parcela: não é atraso.")
w(f"- Parcelas (14): vence em 7 dias {brl(p14['A5'].value)} · vence em 30 dias {brl(p14['C5'].value)} · em aberto (total) {brl(p14['E5'].value)} · **vencido {brl(p14['G5'].value)}** em **{p14['I5'].value} parcelas** · **inadimplência {pct(p14['K5'].value)}** = {brl(p14['G5'].value)} ÷ ({brl(E['pago'])} pago + {brl(p14['G5'].value)}). Pela outra conta (vencido ÷ em aberto) daria {pct(E['vencido']/E['em_aberto'])}: não use.")
w(f"- Propostas (15): abertas **{E['propostas_n']}** somando **{brl(p15['A5'].value)}** · previsão ponderada {brl(p15['C5'].value)} · **fechado no trimestre {brl(p15['E5'].value)}** ({pct(p15['G5'].value,0)} da meta de {brl(dados.META_FECHADO_TRI)}) · taxa de fechamento {pct(p15['I5'].value,0)} (7 fechadas ÷ 11 decididas) · dias até fechar (média) {n(p15['K5'].value,0)}.\n")

# ---------- 6. carteira ----------
w("## 6. Carteira (13 · Carteira de clientes e casos)\n")
w(tab(["Área","Casos","Ativos","Contratado","Recebido","A receber","% recebido"],[(a,b,c,brl(d),brl(e),brl(f),pct(g,0)) for a,b,c,d,e,f,g in [row(p13,r,(1,2,3,4,5,6,7)) for r in range(9,14)]]))
w(tab(["Responsável","Casos","Ativos","Contratado","Recebido","A receber","% recebido"],[(a,b,c,brl(d),brl(e),brl(f),pct(g,0)) for a,b,c,d,e,f,g in [row(p13,r,(1,2,3,4,5,6,7)) for r in range(22,24)]]))
w(tab(["Modalidade","Casos","Ativos","Contratado","Recebido","A receber","% recebido"],[(a,b,c,brl(d),brl(e),brl(f),pct(g,0)) for a,b,c,d,e,f,g in [row(p13,r,(1,2,3,4,5,6,7)) for r in range(35,39)]]))
w(tab(["#","Top 5 clientes","Tipo","Casos","Contratado","Recebido","A receber","% recebido"],[(a,b,c,d,brl(e),brl(f),brl(g),pct(h,0)) for a,b,c,d,e,f,g,h in [row(p13,r,(1,2,3,4,5,6,7,8)) for r in range(48,53)]]))
w(tab(["Situação","Casos","Contratado","Recebido","A receber","% recebido"],[(a,b,brl(c),brl(d),brl(e),pct(f,0)) for a,b,c,d,e,f in [row(p13,r,(1,2,3,4,5,6)) for r in (56,57)]]))
w("- A receber dos encerrados (1.400) = última parcela de Fernanda Castro, vencida em 13/02/2026 (também pendência de encerramento na 04).")
w(tab(["Cliente (13)","Tipo","Área","Casos","Ativos","Contratado","Recebido","A receber","Último caso aberto"],[(a,b,c,d,e,brl(f),brl(g),brl(h),dt(j)) for a,b,c,d,e,f,g,h,i,j in [row(W["13"]["Clientes"],r,(1,2,3,4,5,6,7,8,9,10)) for r in range(5,23)]]))
def acao(c):
    if c["fase"]=="Encerrado": return f"encerrado em {dt(c['encerramento'])}"
    return f"{c['descricao_prazo']} · {rel(c['proximo_prazo_dias'])}"
w(tab(["Chave","Número","Cliente","Área","Fase","Responsável","Modalidade","Contratado","Recebido","Horas est./gastas","Abertura","Próxima ação (prazo principal)"],
      [(c["chave"],c["numero"],c["cliente"],c["area"],c["fase"],c["responsavel"],c["tipo_hon"]+(f" (fixo {brl(c['valor_fixo'])} + êxito {brl(c['valor_exito'])})" if c["tipo_hon"]=="Misto" else ""),brl(c["valor_contratado"]),brl(c["recebido"]),f"{c['horas_estimadas']}/{c['horas_gastas']}",dt(c["abertura"]),acao(c)) for c in dados.CASOS]))
w("- Casos consultivos têm referência CONS-ano-nº (sem número CNJ). Casos por hora (Clínica Bem-Estar CONS-2025-05, Agência Prisma): contratado = estimativa (horas × R$ 180), faturas mensais no dia 10 pelas horas do mês anterior.\n")

# ---------- 7. parcelas ----------
w("## 7. Parcelas e inadimplência (14)\n")
w(tab(["Faixa de atraso","Parcelas","Valor","% do vencido"],[(a,b,brl(c),pct(d,0)) for a,b,c,d,e in [row(p14,r,(1,2,3,4,5)) for r in range(11,16)]]))
w(tab(["Cobrar primeiro (14)","Cliente","Caso","Parcela","Vencimento","Valor","Dias de atraso","Faixa"],[(i+1,a,b,c,dt(d),brl(e),f,g) for i,(a,b,c,d,e,f,g,h) in enumerate(row(p14,r,(2,3,4,5,6,7,8,9)) for r in range(20,30)) if a]))
w(tab(["Vencem nos próximos 30 dias (14)","Cliente","Caso","Parcela","Vencimento","Valor","Dias para vencer"],[(i+1,a,b,c,dt(d),brl(e),f) for i,(a,b,c,d,e,f) in enumerate(row(p14,r,(2,3,4,5,6,7)) for r in range(34,42)) if a]))
w(f"- Total de parcelas cadastradas: {len(dados.PARCELAS())} (pagas {sum(1 for p in dados.PARCELAS() if p['pago'])}, das quais {sum(1 for p in dados.PARCELAS() if p['pago'] and p['pagamento'].year==2025)} pagas em 2025). Régua de cobrança: 1 dia (lembrete), 7 dias (mensagem do responsável), 15 dias (demonstrativo e renegociação), 30 dias (ligação e plano de pagamento).\n")

# ---------- 8. propostas ----------
w("## 8. Propostas (15 · Funil e 07 · Registro)\n")
w(tab(["Etapa (15)","Propostas","Valor","Ponderado","Taxa de passagem"],[(a,b,brl(c),brl(d),pct(e,0)) for a,b,c,d,e in [row(p15,r,(1,2,3,4,5)) for r in range(11,15)]]+[("Fechadas (total)",p15['B15'].value,brl(p15['C15'].value),"",""),("Perdidas (total)",p15['B16'].value,brl(p15['C16'].value),"",""),("Honorário médio das fechadas",brl(p15['B17'].value),"","","")]))
def pd_(x): return "—" if x is None else (rel(x) if isinstance(x,int) else dt(x))
w(tab(["Nº","Cliente","Área","Serviço","Origem","Resp.","Valor","Modalidade","Etapa","Entrada","Envio","Última mov.","Fech. previsto","Fechamento","Motivo","Caso na 13"],
      [(p["numero"],p["cliente"],p["area"],p["servico"],p["origem"],p["responsavel"].split()[0],brl(p["valor"]),p["modalidade"],p["etapa"],dt(p["entrada"]),pd_(p["proposta"]),pd_(p["ultima_mov"]),pd_(p["fech_previsto"]),dt(p["fechamento"]),p["motivo"] or "—",p["caso"] or "—") for p in dados.PROPOSTAS]))
w("- Situação na 15 em 14/09: Patrícia Gomes = Parada (16 dias sem movimento); Clínica Bem-Estar e José Antônio Ribeiro = Previsão vencida; as demais abertas = Ativa. Motivos de perda: Preço 2 (Bistrô 42, Agência Prisma), Fechou com outro escritório 1 (Fernanda Castro), Sem resposta 1 (Oficina).")
g07=W["07"]["Registro"]
w(f"- **07 Registro** (as 10 mais recentes já enviadas, mesmos valores e situação): aguardando resposta {g07['A5'].value} · fechadas {g07['C5'].value} · perdidas {g07['E5'].value} · valor fechado {brl(g07['G5'].value)} · taxa de fechamento {pct(g07['I5'].value,0)} · em aberto {brl(g07['K5'].value)}. Alertas: Patrícia Gomes, Clínica Bem-Estar e Transportadora com validade vencida; José Antônio vence em até 3 dias.\n")

# ---------- 9. Roberto ----------
s06=W["06"]["Simulador"]; p07=W["07"]["Proposta"]
w("## 9. O caso da proposta: Roberto Almeida (06 · Simulador e 07 · Proposta nº 2026-023)\n")
w(f"- Cliente antigo (2 casos na carteira: sentença cível de {brl(15000)} todo pago e recurso misto). Novo caso: **discussão de contrato de prestação de serviços** (Cível). Valor em discussão {brl(s06['B12'].value)}, chance de êxito {pct(s06['B13'].value,0)} → valor esperado da causa {brl(s06['B14'].value)}. Custo-hora {brl(s06['B11'].value,2)} → hora mínima para o caso {brl(s06['B15'].value,2)}.")
w(tab(["Etapa (06)","Horas","Custo (R$)"],[(a,b,brl(c,2)) for a,b,c in [row(s06,r,(1,2,3)) for r in range(19,25)]]+[("**Total**",f"**{s06['B29'].value}**",f"**{brl(s06['C29'].value,2)}**")]))
w(tab(["Despesa (06)","Valor","Cliente reembolsa?","Custo para o escritório"],[(a,brl(b),c,brl(d)) for a,b,c,d in [row(s06,r,(1,2,3,4)) for r in range(33,37)]]+[("**Total de despesas**",brl(s06['B39'].value),"",f"**{brl(s06['D39'].value)}**"),("**Custo total do caso (horas + despesas absorvidas)**","","",f"**{brl(s06['D40'].value,2)}**")]))
w(tab(["Modalidade (06)","Valor pretendido","Receita esperada","Impostos","Custo do caso","Margem esperada","Margem %","Se perder","Risco"],[(a,v,brl(b),brl(c),brl(d),brl(e),pct(f,0),brl(g),i) for (a,b,c,d,e,f,g,h,i),v in zip([row(s06,r,(1,2,3,4,5,6,7,8,9)) for r in range(52,56)],[brl(s06['B44'].value),brl(s06['B45'].value,2)+"/h",pct(s06['B46'].value,0),brl(s06['B47'].value)+" + "+pct(s06['B48'].value,0)])]))
w(f"- Recomendação do simulador: **{s06['A5'].value}** (margem esperada {brl(s06['C5'].value)}, risco {s06['E5'].value}); fora por risco alto: Êxito. Texto do ponto de equilíbrio da hora: \"{s06['H53'].value}\".")
w(f"- **Proposta 07 (nº {p07['B4'].value}, {dt(p07['E4'].value)}, válida por {p07['E5'].value} dias até {dt(p07['E6'].value)}, modalidade {p07['E7'].value})**: objeto \"{p07['B8'].value}\".")
w(tab(["Etapa ou serviço (07)","O que inclui","Prazo previsto","Horas","Valor"],[(a,b,c,d,brl(e)) for a,b,c,d,e in [row(p07,r,(1,2,3,4,5)) for r in range(12,16)]]+[("**Total dos honorários fixos**","","",f"**{p07['D21'].value}**",f"**{brl(p07['E21'].value)}**"),("Honorários de êxito","sobre o resultado, ao fim do caso","","",pct(p07['E22'].value,0))]))
w(f"- Condições: entrada {pct(p07['B24'].value,0)} = **{brl(p07['E24'].value)}** na aceitação; restante {brl(p07['E25'].value)} em **{p07['B25'].value} parcelas de {brl(p07['E26'].value)}** ({dt(p07['C32'].value)}, {dt(p07['C33'].value)}, {dt(p07['C34'].value)}; datas contadas da data da proposta = HOJE()); forma de pagamento {p07['E27'].value}. Na 15 a proposta está como \"Proposta enviada\" (entrada 09/09, envio hoje, previsão de fechamento em 15 dias).\n")

# ---------- 10. metas ----------
m19=W["19"]["Metas"]; w19=W["19"]["Semanas"]
w("## 10. Metas do trimestre (19), reserva (12) e provisão (10)\n")
w(f"- 3º trimestre de 2026 (01/07 a 30/09): semana **{W['19']['Config']['B9'].value} de 13**, {pct(W['19']['Config']['B10'].value,0)} decorrido. Resultados-chave: {W['19']['Painel']['A5'].value} · atingidos {W['19']['Painel']['C5'].value} · em risco {W['19']['Painel']['E5'].value} · progresso médio {pct(W['19']['Painel']['G5'].value,0)}.")
rows=[]
for r in range(5,14):
    a=row(m19,r,(1,2,3,4,5,6,7,8,10,11))
    if not a[1]: continue
    s=[w19.cell(row=r,column=c).value for c in range(3,14)]
    rows.append((a[0] or "",a[1],a[2].split()[0],a[3],n(a[4],1),n(a[5],1),n(a[6],1),pct(a[7],0),a[8],a[9]," · ".join(n(x,1) for x in s)))
w(tab(["Objetivo","Resultado-chave","Dono","Unid.","Partida (30/06)","Meta","Atual (11/09)","Progresso","Semáforo","Sentido","S1…S11 (sextas 03/07 → 11/09)"],rows))
c12=W["12"]["Config"]; p12=W["12"]["Painel"]
w(f"- **12 Reserva**: meta {c12['B8'].value} meses de custo fixo × custo fixo médio {brl(c12['B16'].value)} (jun/jul/ago, com pró-labore) = **{brl(p12['A5'].value)}**; reserva hoje **{brl(p12['C5'].value)}**; falta {brl(p12['E5'].value)}; cobre **{n(p12['G5'].value,1)} meses**; semáforo \"{p12['B7'].value}\"; com aporte de {brl(c12['B9'].value)}/mês a meta chega em **{p12['I5'].value}**. Saldo em caixa {brl(c12['B19'].value)} − compromissos não pagos {brl(c12['B20'].value)} = caixa livre {brl(c12['B21'].value)} (\"contando o caixa livre: 2,2 meses\").")
w(tab(["Meta de caixa do trimestre (12)","Alvo","Atual","Progresso","Prazo","Situação"],[(a,brl(b),brl(c),pct(d,0),dt(f),h) for a,b,c,d,f,g,h in [row(p12,r,(1,2,3,4,6,7,8)) for r in (37,38,39)]]))
p10=W["10"]["Painel"]
w(f"- **10 Provisão (Config = Setembro, alíquota 8 %)**: 13º dos sócios 500 + 500 e recesso da estagiária 155,56 por mês; entradas de setembro até 11/09 {brl(p10['A5'].value)}; a separar no mês {brl(p10['C5'].value)}; **saldo provisionado ao fim de setembro {brl(p10['E5'].value)}** (separado 27.407 − usado 16.087 em guias); compromisso do mês seguinte {brl(p10['G5'].value)}; situação {p10['K5'].value}. Janeiro foi o único mês com \"Falta separar\" (492).")
w(tab(["Mês (10)","Entradas (sem Outras)","Provisão 8 %","Total a separar","Guia paga no mês","Saldo provisionado"],[(a,brl(b),brl(c),brl(f),brl(g),brl(j)) for a,b,c,d,e,f,g,h,i,j in [row(p10,r,(1,2,3,4,5,6,7,8,9,10)) for r in range(9,18)]]))
w("")

# ---------- 11. resumo 20 ----------
p20=W["20"]["Painel"]
w("## 11. Resumo do mês (20): agosto × julho de 2026\n")
ptbr=lambda x: "—" if x in (None,"") else str(x).replace(" p.p."," PP").translate(str.maketrans(",.",".,")).replace(" PP"," p.p.")   # texto do Painel como o Excel em português mostra
w(tab(["Indicador","Agosto","Julho","Variação","Meta","Vs. meta","Situação"],[(a,ptbr(b),ptbr(c),ptbr(d),ptbr(e),ptbr(f),g or "informativo") for a,b,c,d,e,f,g in [row(p20,r,(1,2,3,4,5,6,7)) for r in range(5,17)]]))
w("(Valores como o Excel em português mostra; os separadores seguem o idioma do Excel.)")
w("- Destaques automáticos: maior melhora contra julho = Horas faturáveis (+4,7 p.p.); maior piora = Margem do mês (−7,1 p.p.); mais longe da meta = Inadimplência (+0,5 p.p. da meta, acima da meta); indicadores no alvo: 9 de 11 com meta.")
w("- Observações do escritório (célula amarela do exemplo): \"Agosto fechou com quatro propostas novas viradas em caso (Escola Aurora, Loja Verde, Marcos Vinícius e a cobrança da Construtora entrou em julho); Bistrô 42 e Agência Prisma seguem com parcelas vencidas e entraram na régua de cobrança; o caso da Oficina (execução) e o recurso da Escola Aurora estouraram as horas estimadas.\"\n")

# ---------- 12. histórico 17 ----------
h17=W["17"]["Histórico"]
w("## 12. Histórico mensal (17 · Histórico; jan–ago = Painel mensal da 09 e 16, carteira no fim de cada mês; setembro = Dados)\n")
w(tab(["Mês","Prazos hoje+7","Atrasados","Horas","Faturáveis","% fat.","Entrou","Saiu","Sobrou","A receber","Vencido","Inadimpl.","Propostas abertas","Valor das propostas","Casos ativos"],
      [(a,b or "—",c or "—",n(d,1) if d else "—",n(e,1) if e else "—",pct(f,0) if f else "—",brl(g),brl(h),brl(i),brl(j),brl(k),pct(l),m_,brl(o),q) for a,b,c,d,e,f,g,h,i,j,k,l,m_,o,q in [row(h17,r,list(range(1,16))) for r in range(5,14)]]))
w("- Prazos: a agenda (01) não guarda histórico (o escritório começou a anotar em setembro). Horas: o controle (16) começou em julho. Propostas abertas: o funil (15) começou em junho.\n")

# ---------- 13. rotina, checklist ----------
p03=W["03"]["Painel"]; p04=W["04"]["Painel"]
w("## 13. Rotina (03) e checklist (04)\n")
w(f"- **03 Rotina**: 9 rotinas (4 de segunda = 12 min; 5 de sexta = 18 min; **30 min/semana**); registradas S29 a S36 (20/07 a 07/09/2026); semana atual {p03['C5'].value}; aderência nas últimas 4 semanas **{pct(p03['A5'].value,0)}** (segunda 94 %, sexta 75 %); rotina mais pulada: \"Enviar a cobrança educada das parcelas atrasadas\" (1 de 4). Série S29–S36: 67 %, 78 %, 89 %, 89 %, 100 %, 78 %, 78 %, 78 %.")
w(f"- **04 Checklist**: casos cadastrados {p04['A5'].value} · abertos com pendência de abertura {p04['C5'].value} · encerrados com pendência {p04['E5'].value} · itens pendentes no total **{p04['G5'].value}** · casos sem pendência {p04['I5'].value}. Itens mais esquecidos: \"Caso cadastrado no caixa e na carteira\" (2) e, no encerramento, \"Avaliação do cliente pedida\" (2). Fernanda Castro (encerrado) pende \"Última parcela cobrada e recebida\" (a parcela vencida da 14).")
w("")
open(pathlib.Path(__file__).resolve().parent/"NUMEROS.md","w").write("\n".join(L))
print("NUMEROS.md gerado:",len("\n".join(L)),"caracteres")
