#!/usr/bin/env python3
"""Planilha 20 do Kit de Gestão para Advogados: Resumo do Mês para a IA e para o contador. Gera 20-resumo-do-mes.xlsx
12 indicadores do mês (valor, mês anterior, meta), painel com variação e situação, e a aba Resumo que escreve sozinha
as frases do mês, os destaques e um bloco único para colar no prompt "Painel 01 · Explicar o mês ao sócio".
Exemplo: agosto × julho de 2026 (último mês fechado), números do Histórico da 17, da 18 e da 15 (fonte única: dados.py).
Os valores do Painel aparecem como texto formatado com FIXED (casas decimais de Indicadores!C; separadores no idioma do Excel);
os números ficam em colunas ocultas, usadas pelas fórmulas do Resumo."""
from ssg import *
import dados
NI=12; R0=5; RN=R0+NI-1   # indicadores nas linhas 5..16
H7=dados.HISTORICO[7]; H8=dados.HISTORICO[8]; D7=dados.dre(7); D8=dados.dre(8)
r1=lambda x: round(x,1)

wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche.",merge_to="E")
cfg["A4"]="Escritório"; cfg["B4"]=f"{dados.ESCRITORIO} (exemplo fictício)"
cfg["A5"]="Ano"; cfg["B5"]=2026
cfg["A6"]="Mês do resumo"; cfg["B6"]="Agosto"
cfg["A7"]="Número do mês"; cfg["B7"]="=MATCH(B6,$D$5:$D$16,0)"
cfg["A8"]="Mês anterior"; cfg["B8"]='=IF(B7>1,INDEX($D$5:$D$16,B7-1),INDEX($D$5:$D$16,12))'
for r in range(4,9): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"]); inp(cfg["B6"]); calc(cfg["B7"]); calc(cfg["B8"])
cfg["D4"]="Meses"; rotulo(cfg["D4"])
for i,m in enumerate(MESES): cfg.cell(row=5+i,column=4,value=m).font=F(size=10,color=TINTA)
dv=lista("=Config!$D$5:$D$16",allow_blank=False); dv.add("B6"); cfg.add_data_validation(dv)
cfg["A10"]="Use a mesma planilha todo mês: troque o mês aqui e, em Indicadores, mova o \"Mês atual\" para \"Mês anterior\" antes de digitar os novos valores. Resuma o último mês fechado (no exemplo, agosto; setembro está em andamento)."; nota(cfg["A10"])
widths(cfg,(28,40,4,14)); cfg.sheet_view.showGridLines=False

# ---------- Indicadores ----------
ind=wb.create_sheet("Indicadores")
titulo(ind,"Indicadores do mês","Até 12 indicadores (de cima para baixo, sem pular linha): nome, unidade, casas decimais, meta, se maior é melhor, valor do mês anterior e do mês atual. Copie os números do Painel do escritório (17, Histórico), do Resultado mensal (18) e do Funil (15).",merge_to="H")
hdr(ind,4,["Indicador","Unidade","Casas decimais","Meta do mês","Maior é melhor?","Mês anterior","Mês atual","Copie de (planilha do kit)"],height=30)
# exemplo: julho → agosto de 2026 (mesmos números do Histórico da 17, da 18 e da 15)
ex=[("Entrou no mês (recebimentos)","R$",0,26000,"Sim",H7["entrou"],H8["entrou"],"09 · Caixa (Painel) ou 17 · Painel (Histórico)"),
    ("Saídas do mês (custos, despesas de casos, pró-labore e impostos provisionados)","R$",0,21500,"Não",D7["saidas"],D8["saidas"],"18 · Resultado mensal (Total de saídas)"),
    ("Resultado do mês","R$",0,4000,"Sim",D7["resultado"],D8["resultado"],"18 · Resultado mensal"),
    ("Margem do mês","%",1,20,"Sim",r1(D7["margem"]*100),r1(D8["margem"]*100),"18 · Resultado mensal"),
    ("Horas registradas no mês","h",1,280,"Sim",H7["horas"],H8["horas"],"16 · Horas por caso e por pessoa (Config = mês)"),
    ("Horas faturáveis","%",1,75,"Sim",r1(H7["faturaveis"]/H7["horas"]*100),r1(H8["faturaveis"]/H8["horas"]*100),"16 · Horas por caso e por pessoa"),
    ("A receber (carteira; inclui êxito de casos ativos)","R$",0,None,"Sim",H7["a_receber"],H8["a_receber"],"13 · Carteira (fim do mês) ou 17 · Histórico"),
    ("Vencido (parcelas em atraso)","R$",0,10000,"Não",H7["vencido"],H8["vencido"],"14 · Parcelas (fim do mês) ou 17 · Histórico"),
    ("Inadimplência (vencido ÷ (pago + vencido))","%",1,4,"Não",r1(H7["inadimplencia"]*100),r1(H8["inadimplencia"]*100),"14 · Parcelas e inadimplência ou 17 · Histórico"),
    ("Propostas abertas (valor)","R$",0,40000,"Sim",H7["propostas_valor"],H8["propostas_valor"],"15 · Funil de propostas ou 17 · Histórico"),
    ("Casos ativos","un",0,30,"Sim",H7["casos_ativos"],H8["casos_ativos"],"13 · Carteira ou 17 · Histórico"),
    ("Honorários fechados em propostas no mês","R$",0,20000,"Sim",H7["fechado_mes"],H8["fechado_mes"],"15 · Funil de propostas (fechadas no mês)")]
for i in range(NI):
    r=R0+i
    for c in range(1,8): inp(ind.cell(row=r,column=c),center=(c>1))
    for c in (4,6,7): ind.cell(row=r,column=c).number_format="#,##0.00"
    ind.cell(row=r,column=1).alignment=Alignment(horizontal="left")
    inp(ind.cell(row=r,column=8)); ind.cell(row=r,column=8).font=F(size=9,color=LILAS)
    if i<len(ex):
        for c,v in enumerate(ex[i],start=1):
            if v is not None: ind.cell(row=r,column=c,value=v)
dv_sn=lista('"Sim,Não"'); dv_sn.add(f"E{R0}:E{RN}"); ind.add_data_validation(dv_sn)
dv_cd=lista('"0,1,2"'); dv_cd.add(f"C{R0}:C{RN}"); ind.add_data_validation(dv_cd)
dv_un=lista('"R$,%,un,h,pts"'); dv_un.add(f"B{R0}:B{RN}"); ind.add_data_validation(dv_un)
ind.cell(row=RN+2,column=1,value='Para indicadores em %, digite 5,1 (não 0,051). "Maior é melhor?" = Não para saídas, vencido, inadimplência e prazos atrasados. Meta em branco = informativo (ex.: A receber é a carteira contratada, não um problema). Meta 0 funciona: a situação aparece, a distância em % não.').font=F(size=9,color=LILAS)
ind.merge_cells(start_row=RN+2,start_column=1,end_row=RN+2,end_column=8); ind.cell(row=RN+2,column=1).alignment=Alignment(wrap_text=True,vertical="top"); ind.row_dimensions[RN+2].height=30
widths(ind,(52,9,10,13,12,13,13,40)); ind.freeze_panes="B5"; ind.sheet_view.showGridLines=False

# ---------- Painel ----------
p=wb.create_sheet("Painel")
p["A1"]='=Config!B4&" · Resumo do mês · "&Config!B6&" de "&Config!B5'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:H1")
p["A2"]="Nada para digitar aqui. Escolha o mês em Config; os números vêm de Indicadores. Variação de indicadores em % é em pontos percentuais (p.p.)."; nota(p["A2"]); p.merge_cells("A2:H2")
hdr(p,4,["Indicador","Mês","Mês anterior","Variação","Meta","Vs. meta","Situação","Unidade"])
# colunas ocultas: N casas, O distância da meta (positiva = fora, no sentido do indicador), P variação com sinal de melhora,
# Q valor do mês, R mês anterior, S meta, T variação numérica (relativa; em p.p. para %), U vs. meta numérica
for i in range(NI):
    r=R0+i; s=R0+i
    A=f"Indicadores!A{s}"; B=f"Indicadores!B{s}"; C=f"Indicadores!C{s}"; Dm=f"Indicadores!D{s}"; Em=f"Indicadores!E{s}"; Fm=f"Indicadores!F{s}"; G=f"Indicadores!G{s}"
    p.cell(row=r,column=14,value=f'=IF({C}="",2,{C})')
    p.cell(row=r,column=17,value=f'=IF(OR({A}="",{G}=""),"",{G})')
    p.cell(row=r,column=18,value=f'=IF(OR({A}="",{Fm}=""),"",{Fm})')
    p.cell(row=r,column=19,value=f'=IF(OR({A}="",{Dm}=""),"",{Dm})')
    p.cell(row=r,column=20,value=f'=IF(OR(Q{r}="",R{r}=""),"",IF({B}="%",Q{r}-R{r},IF(R{r}=0,"",(Q{r}-R{r})/ABS(R{r}))))')
    p.cell(row=r,column=21,value=f'=IF(OR(Q{r}="",S{r}=""),"",IF({B}="%",Q{r}-S{r},IF(S{r}=0,"",(Q{r}-S{r})/ABS(S{r}))))')
    p.cell(row=r,column=15,value=f'=IF(OR(U{r}="",G{r}="",G{r}="No alvo"),"",IF({Em}="Não",U{r},-U{r}))')
    p.cell(row=r,column=16,value=f'=IF(T{r}="","",IF({Em}="Não",-T{r},T{r}))')
    for c in (14,15,16,17,18,19,20,21): p.cell(row=r,column=c).font=F(size=9,color=CINZA)
    num=lambda x: f'IF({B}="R$","R$ ","")&FIXED({x},N{r})&IF({B}="%","%",IF(OR({B}="R$",{B}="",{B}="un"),""," "&{B}))'
    var=lambda x: f'IF({x}="","",IF({x}>=0,"+","")&IF({B}="%",FIXED({x},1)&" p.p.",FIXED({x}*100,1)&"%"))'
    p.cell(row=r,column=1,value=f'=IF({A}="","",{A})'); calc(p.cell(row=r,column=1),center=False)
    p.cell(row=r,column=2,value=f'=IF(Q{r}="","",{num(f"Q{r}")})'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF(R{r}="","",{num(f"R{r}")})'); calc(p.cell(row=r,column=3))
    p.cell(row=r,column=4,value=f'={var(f"T{r}")}'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF(S{r}="","",{num(f"S{r}")})'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'={var(f"U{r}")}'); calc(p.cell(row=r,column=6))
    p.cell(row=r,column=7,value=f'=IF(OR(Q{r}="",S{r}=""),"",IF({Em}="Não",IF(Q{r}<=S{r},"No alvo","Acima da meta"),IF(Q{r}>=S{r},"No alvo","Abaixo da meta")))'); calc(p.cell(row=r,column=7))
    p.cell(row=r,column=8,value=f'=IF({A}="","",{B})'); calc(p.cell(row=r,column=8))
rng=f"A{R0}:H{RN}"
p.conditional_formatting.add(rng, FormulaRule(formula=[f'OR($G{R0}="Abaixo da meta",$G{R0}="Acima da meta")'], fill=fill(VERM), font=F(color=VERM_T,size=10)))
p.conditional_formatting.add(rng, FormulaRule(formula=[f'$G{R0}="No alvo"'], fill=fill(VERDE)))
p.cell(row=RN+2,column=1,value="Verde: no alvo. Vermelho: fora da meta. Sem meta: informativo. Os valores são texto formatado (FIXED, casas decimais de Indicadores; separadores no idioma do Excel); as colunas N a U (ocultas) guardam os números e a distância da meta, usadas nos destaques do Resumo.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=RN+2,start_column=1,end_row=RN+2,end_column=8); p.cell(row=RN+2,column=1).alignment=Alignment(wrap_text=True,vertical="top"); p.row_dimensions[RN+2].height=30
for col in "NOPQRSTU": p.column_dimensions[col].hidden=True
widths(p,(52,14,14,12,14,12,15,9)); p.freeze_panes="A5"; p.sheet_view.showGridLines=False

# ---------- Resumo ----------
rs=wb.create_sheet("Resumo")
rs["A1"]="Resumo do mês, pronto para a IA e para o contador"; rs["A1"].font=F(bold=True,size=16,color=UVA)
rs["A2"]="Só a célula amarela é para digitar (observações do escritório). Copie o bloco único e cole no prompt \"Painel 01 · Explicar o mês ao sócio\" da biblioteca do kit, ou envie ao sócio e ao contador. Os números vêm do Painel."; nota(rs["A2"]); rs.merge_cells("A2:D2")
rs["A4"]='="Resumo de "&Config!B6&" de "&Config!B5&" · "&Config!B4'; rs["A4"].font=F(bold=True,color=UVA); rs.merge_cells("A4:D4")
rs["A5"]="Observações do escritório (opcional; entram no fim do bloco):"; rotulo(rs["A5"],bold=False)
rs["A6"]="Agosto fechou com três propostas novas viradas em caso (Escola Aurora, Loja Verde e Marcos Vinícius); a cobrança da Construtora já havia entrado em julho e não conta neste mês; Bistrô 42 e Agência Prisma seguem com parcelas vencidas e entraram na régua de cobrança; o caso da Oficina (execução) e o recurso da Escola Aurora estouraram as horas estimadas."
inp(rs["A6"]); [inp(rs[c+"6"]) for c in "BCD"]; rs.merge_cells("A6:D6"); rs["A6"].alignment=Alignment(wrap_text=True,vertical="top"); rs.row_dimensions[6].height=58
F0=8
def frase(i):
    r=R0+i
    v=f"Painel!Q{r}"; a=f"Painel!R{r}"; var=f"Painel!T{r}"; meta=f"Painel!S{r}"; st=f"Painel!G{r}"; nome=f"Painel!A{r}"
    return (f'=IF(OR({nome}="",{v}=""),"",'
            f'"• "&{nome}&": "&Painel!B{r}'
            f'&IF({var}<>"",IF({var}=0," (igual a "&Config!$B$8&")"," ("&Painel!D{r}&" em relação a "&Config!$B$8&")"),'
            f'IF(AND({a}<>"",{a}=0,{v}<>0)," (sem base de comparação: "&Config!$B$8&" foi zero)",'
            f'IF({a}<>""," (igual a "&Config!$B$8&")","")))'
            f'&IF({meta}<>"","; meta "&Painel!E{r}&", "&LOWER({st}),"")&".")')
for i in range(NI):
    rs.cell(row=F0+i,column=1,value=frase(i)).font=F(size=10,color=TINTA); rs.merge_cells(start_row=F0+i,start_column=1,end_row=F0+i,end_column=4)
    rs.cell(row=F0+i,column=1).alignment=Alignment(wrap_text=True,vertical="top")
D0=F0+NI+1
rs.cell(row=D0,column=1,value="Destaques automáticos").font=F(bold=True,color=UVA)
NR=f"Painel!$A${R0}:$A${RN}"; VD=f"Painel!$D${R0}:$D${RN}"; FR=f"Painel!$F${R0}:$F${RN}"; AR=f"Painel!$O${R0}:$O${RN}"; SR=f"Painel!$G${R0}:$G${RN}"; PR=f"Painel!$P${R0}:$P${RN}"
def pick(agg): return f'INDEX({NR},MATCH({agg}({PR}),{PR},0))'
def varde(agg): return f'INDEX({VD},MATCH({agg}({PR}),{PR},0))'
rs.cell(row=D0+1,column=1,value=f'=IF(COUNT({PR})=0,"• Melhora e piora: preencha o mês anterior para comparar.",IF(MAX({PR})<=0,"• Nenhum indicador melhorou contra "&Config!$B$8&".","• Maior melhora contra "&Config!$B$8&": "&{pick("MAX")}&" ("&{varde("MAX")}&")."))')
rs.cell(row=D0+2,column=1,value=f'=IF(COUNT({PR})=0,"",IF(MIN({PR})>=0,"• Nenhum indicador piorou contra "&Config!$B$8&".","• Maior piora contra "&Config!$B$8&": "&{pick("MIN")}&" ("&{varde("MIN")}&")."))')
_fora=f'(COUNTIF({SR},"Acima da meta")+COUNTIF({SR},"Abaixo da meta"))'
rs.cell(row=D0+3,column=1,value=f'=IF({_fora}=0,"• Nenhum indicador fora da meta.",'
    f'IF(COUNT({AR})=0,"• "&{_fora}&" indicador(es) fora da meta (sem percentual: a meta é zero).",'
    f'"• Mais longe da meta: "&INDEX({NR},MATCH(MAX({AR}),{AR},0))&" ("&INDEX({FR},MATCH(MAX({AR}),{AR},0))&" da meta, "&LOWER(INDEX({SR},MATCH(MAX({AR}),{AR},0)))&")."))')
rs.cell(row=D0+4,column=1,value=f'="• Indicadores no alvo: "&COUNTIF({SR},"No alvo")&" de "&(COUNTIF({SR},"No alvo")+COUNTIF({SR},"Acima da meta")+COUNTIF({SR},"Abaixo da meta"))&" com meta."')
for k in range(1,5):
    rs.cell(row=D0+k,column=1).font=F(size=10,color=TINTA); rs.merge_cells(start_row=D0+k,start_column=1,end_row=D0+k,end_column=4); rs.cell(row=D0+k,column=1).alignment=Alignment(wrap_text=True,vertical="top")
T0=D0+6
rs.cell(row=T0,column=1,value="Bloco único para copiar").font=F(bold=True,color=UVA)
partes=" & ".join([f'IF(A{F0+i}="","",A{F0+i}&CHAR(10))' for i in range(NI)])
destaques=" & ".join([f'IF(A{D0+k}="","",A{D0+k}&CHAR(10))' for k in range(1,5)])
rs.cell(row=T0+1,column=1,value=f'=A4&CHAR(10)&CHAR(10)&"Indicadores do mês:"&CHAR(10)&{partes}&CHAR(10)&"Destaques:"&CHAR(10)&{destaques}&IF(A6="","",CHAR(10)&"Observações do escritório: "&A6)')
rs.merge_cells(start_row=T0+1,start_column=1,end_row=T0+1,end_column=4); rs.cell(row=T0+1,column=1).alignment=Alignment(wrap_text=True,vertical="top"); rs.cell(row=T0+1,column=1).font=F(size=10,color=TINTA); rs.cell(row=T0+1,column=1).fill=fill(LAVANDA)
rs.row_dimensions[T0+1].height=360
rs.cell(row=T0+3,column=1,value="Os textos são gerados por fórmula. Revise antes de enviar: a IA e o contador precisam do porquê dos números, e isso só o escritório sabe. Nenhum dado de cliente entra aqui: só totais. Variação de indicadores em % em pontos percentuais (p.p.).").font=F(size=9,color=LILAS)
rs.merge_cells(start_row=T0+3,start_column=1,end_row=T0+3,end_column=4)
widths(rs,(44,30,30,30)); rs.sheet_view.showGridLines=False
wb._sheets=[wb["Painel"],wb["Resumo"],wb["Config"],wb["Indicadores"]]   # ordem: Como usar (inserida na frente), Painel, Resumo, Config, Indicadores

como_usar(wb,"Resumo do Mês",[
 ("O que esta planilha faz","Você digita até 12 indicadores do mês (valor, mês anterior, meta). Ela calcula variação e situação, monta o Painel e escreve sozinha as frases do mês, os destaques (maior melhora, maior piora, mais longe da meta, respeitando se maior ou menor é melhor) e um bloco único para colar na IA ou mandar ao sócio e ao contador."),
 ("Passo 1","Em Config, preencha o escritório, o ano e escolha o mês do resumo (o último mês fechado; no exemplo, agosto de 2026)."),
 ("Passo 2","Em Indicadores, troque os exemplos pelos seus (de cima para baixo, sem pular linha): nome, unidade, casas decimais, meta e se maior é melhor. Depois, o valor do mês anterior e do mês atual, copiados do Painel do escritório (17, aba Histórico), do Resultado mensal (18) e do Funil (15). Em %, digite 5,1 e não 0,051."),
 ("Passo 3","Abra Painel: cada indicador com mês, mês anterior, variação (em p.p. para indicadores em %), meta e situação (verde no alvo, vermelho fora)."),
 ("Passo 4","Abra Resumo: as frases já estão escritas. Escreva as observações do mês na célula amarela, copie o bloco único e cole no prompt \"Painel 01 · Explicar o mês ao sócio\" (para o sócio) ou \"Caixa 04 · Preparar a reunião mensal com o contador\" da biblioteca do kit."),
 ("Todo mês","Em Indicadores, mova o \"Mês atual\" para \"Mês anterior\", digite os novos valores e troque o mês em Config. O resto se refaz sozinho."),
 ("Cuidado com dados","O bloco só tem totais do escritório. Não cole nome de cliente, número de processo ou detalhe de caso na IA: veja o guia LGPD do kit."),
])
proteger(wb); salvar(wb,"20-resumo-do-mes.xlsx","Resumo do Mês · Kit de Gestão para Advogados")
