#!/usr/bin/env python3
"""Planilha 19 do Kit de Gestão para Médicos: Metas do Trimestre da clínica. Gera 19-metas-do-trimestre.xlsx
3 objetivos com até 3 resultados-chave cada, valor da semana em Semanas (S1..S13), progresso × tempo decorrido e semáforo.
Exemplo: 3º trimestre de 2026, painel em 14/09/2026 (semana 11 de 13). Cada resultado-chave é um número das planilhas 01, 02, 10, 12, 13 e 14 (dados.metas_19)."""
from ssg import *
import dados
from datetime import date
NO=3; NK=3
wb=Workbook()
# ---------- Config ----------
cfg=wb.active; cfg.title="Config"
titulo(cfg,"Configurações","Células amarelas: você preenche.",merge_to="F")
cfg["A4"]="Clínica"; cfg["B4"]=f"{dados.CLINICA} (exemplo fictício)"
cfg["A5"]="Trimestre"; cfg["B5"]="3º trimestre de 2026"
cfg["A6"]="Início do trimestre"; cfg["B6"]=date(2026,7,1)
cfg["A7"]="Fim do trimestre"; cfg["B7"]=date(2026,9,30)
cfg["A8"]="Data de referência (hoje)"; cfg["B8"]=dados.HOJE
cfg["A9"]="Semana atual do trimestre"; cfg["B9"]='=IF(B8<B6,0,MIN(13,INT((B8-B6)/7)+1))'
cfg["A10"]="% do trimestre decorrido"; cfg["B10"]='=MAX(0,MIN(1,(B8-B6)/(B7-B6)))'
for r in range(4,11): rotulo(cfg.cell(row=r,column=1))
inp(cfg["B4"]); inp(cfg["B5"]); inp(cfg["B6"],DATA); inp(cfg["B7"],DATA); inp(cfg["B8"],DATA); calc(cfg["B9"]); calc(cfg["B10"],PCT)
cfg["C8"]="Para simular o fim do trimestre, troque por uma data."; nota(cfg["C8"])
cfg["A12"]="Pessoas da clínica (donos dos resultados-chave)"; rotulo(cfg["A12"])
cfg["C12"]="Preencha de cima para baixo, sem pular linha."; nota(cfg["C12"])
donos=[dados.CAR,dados.PAU,dados.BRU]
for i in range(12):
    c=cfg.cell(row=13+i,column=2); inp(c)
    if i<len(donos): c.value=donos[i]
cfg["A13"]="Nomes"; rotulo(cfg["A13"],bold=False)
widths(cfg,(44,28,50)); cfg.sheet_view.showGridLines=False
PESSOAS_LISTA="=OFFSET(Config!$B$13,0,0,MAX(1,COUNTA(Config!$B$13:$B$24)),1)"
# ---------- Metas ----------
m=wb.create_sheet("Metas")
titulo(m,"Metas do trimestre da clínica","Até 3 objetivos com até 3 resultados-chave cada. Preencha o amarelo; progresso e semáforo são calculados. Atualize o valor atual toda sexta.",merge_to="M")
hdr(m,4,["Objetivo","Resultado-chave","Dono","Unidade","Ponto de partida","Meta","Valor atual","Progresso","Esperado até hoje","Semáforo","Sentido","Observação"])
DEC="Config!$B$10"
rows=[]
for o in range(NO):
    for k in range(NK):
        r=5+o*NK+k; rows.append(r)
        if k==0:
            inp(m.cell(row=r,column=1)); m.merge_cells(start_row=r,start_column=1,end_row=r+NK-1,end_column=1); m.cell(row=r,column=1).alignment=Alignment(wrap_text=True,vertical="top")
        for c in (2,3,4,5,6,7,11,12): inp(m.cell(row=r,column=c))
        for c in (3,4,5,6,7,11): m.cell(row=r,column=c).alignment=Alignment(horizontal="center")
        # Progresso: atual no alvo = 100 %. Fora do alvo, mede o caminho entre ponto de partida e
        # meta; se o ponto de partida JÁ estava dentro da meta (é um teto ou piso a manter), mede
        # meta ÷ atual (16 pacientes para um teto de 8 = 50 %). Antes, (E−G)/(E−F) com E=0 e F=8
        # dava 100 % para 16 e 0 % para zero: o sinal do denominador invertia a meta (rodada 5).
        m.cell(row=r,column=8,value=f'=IF(OR(B{r}="",G{r}=""),"",IF(K{r}="Menor é melhor",IF(G{r}<=F{r},1,IF(E{r}>F{r},MAX(0,(E{r}-G{r})/(E{r}-F{r})),IF(G{r}=0,0,MAX(0,F{r}/G{r})))),IF(G{r}>=F{r},1,IF(E{r}<F{r},MAX(0,(G{r}-E{r})/(F{r}-E{r})),IF(F{r}=0,0,MAX(0,G{r}/F{r}))))))'); calc(m.cell(row=r,column=8),PCT)
        m.cell(row=r,column=9,value=f'=IF(B{r}="","",{DEC})'); calc(m.cell(row=r,column=9),PCT)
        m.cell(row=r,column=10,value=f'=IF(OR(B{r}="",H{r}=""),"",IF(H{r}>=1,"Atingido",IF(H{r}>=I{r}-0.1,"No ritmo",IF(H{r}>=I{r}-0.25,"Atenção","Em risco"))))'); calc(m.cell(row=r,column=10))
        m.cell(row=r,column=12).alignment=Alignment(wrap_text=True)
RL=4+NO*NK
dvsent=lista('"Maior é melhor,Menor é melhor"'); dvsent.add(f"K5:K{RL}"); m.add_data_validation(dvsent)
dvdono=lista(PESSOAS_LISTA); dvdono.add(f"C5:C{RL}"); m.add_data_validation(dvdono)
dvnum=DataValidation(type="decimal",allow_blank=True,showErrorMessage=True); dvnum.add(f"E5:G{RL}"); m.add_data_validation(dvnum)
for cor,txt,fnt in ((VERDE,"Atingido",VERDE_T),("E6F4EA","No ritmo",VERDE_T),(AMARELO,"Atenção","7A5200"),(VERM,"Em risco",VERM_T)):
    m.conditional_formatting.add(f"J5:J{RL}", FormulaRule(formula=[f'J5="{txt}"'], fill=fill(cor), font=F(color=fnt,size=10,bold=(txt in ("Atingido","Em risco")))))
m.cell(row=RL+2,column=1,value="Progresso: valor atual no alvo = 100 %; fora do alvo, é o caminho andado entre o ponto de partida e a meta — e, quando o ponto de partida já estava dentro da meta (um teto ou piso a manter), é meta ÷ atual (16 pacientes para um teto de 8 = 50 %). Semáforo: Atingido (100%); No ritmo (progresso até 10 pontos abaixo do tempo decorrido); Atenção (até 25 pontos abaixo); Em risco (mais que isso). A planilha avisa; a ação é da clínica.").font=F(size=9,color=LILAS)
m.merge_cells(start_row=RL+2,start_column=1,end_row=RL+2,end_column=12)
for r in range(5,RL+1): m.cell(row=r,column=12).alignment=Alignment(wrap_text=True,vertical="top"); m.cell(row=r,column=2).alignment=Alignment(wrap_text=True,vertical="top"); m.row_dimensions[r].height=44
m.cell(row=RL+3,column=1,value="Inadimplência = vencido ÷ (pago + vencido), a mesma conta das planilhas 14, 17 e 20 (só o que foi combinado a prazo). Valores em % digitados como 5,1 (não 0,051).").font=F(size=9,color=LILAS)
widths(m,(28,44,16,10,12,10,11,11,12,11,16,44)); m.freeze_panes="C5"; m.sheet_view.showGridLines=False
ex=dados.metas_19()
for o,(obj,krs) in enumerate(ex):
    m.cell(row=5+o*NK,column=1,value=obj)
    for k,(kr,dono,un,ini,meta,atual,sent,obs,serie) in enumerate(krs):
        r=5+o*NK+k
        for c,v in zip((2,3,4,5,6,7,11,12),(kr,dono,un,ini,meta,atual,sent,obs)): m.cell(row=r,column=c,value=v)
# ---------- Semanas ----------
w=wb.create_sheet("Semanas")
titulo(w,"Acompanhamento semanal","Toda sexta, copie o valor atual de cada resultado-chave para a coluna da semana. A linha fica com o histórico do trimestre.",merge_to="P")
hdr(w,4,["Resultado-chave","Meta"]+[f"S{i}" for i in range(1,14)])
for i,r in enumerate(rows):
    rr=5+i
    w.cell(row=rr,column=1,value=f'=IF(Metas!B{r}="","",Metas!B{r})'); calc(w.cell(row=rr,column=1),center=False)
    w.cell(row=rr,column=2,value=f'=IF(Metas!B{r}="","",Metas!F{r})'); calc(w.cell(row=rr,column=2))
    for s_ in range(13): inp(w.cell(row=rr,column=3+s_),center=True)
for o,(obj,krs) in enumerate(ex):
    for k,(kr,dono,un,ini,meta,atual,sent,obs,serie) in enumerate(krs):
        r=5+o*NK+k; assert serie[-1]==atual,(kr,serie[-1],atual)
        for s_,v in enumerate(serie): w.cell(row=r,column=3+s_,value="—" if v is None else v)
w.conditional_formatting.add("C4:O4", FormulaRule(formula=['COLUMN()-2=Config!$B$9'], fill=fill(SOL), font=F(color=UVA,size=10,bold=True)))
w.cell(row=RL+2,column=1,value="A coluna da semana atual fica destacada. Valores em % são digitados como 16,8 (não 0,168). Semana sem nada a medir: escreva \"—\" (não escreva 0, que puxa a série para baixo como se o resultado tivesse desabado). No exemplo, S1 a S11 são as sextas de 03/07 a 11/09/2026, e o prazo real dos lotes fica \"—\" na S1 porque nenhum lote foi pago naquela semana do trimestre.").font=F(size=9,color=LILAS)
w.merge_cells(start_row=RL+2,start_column=1,end_row=RL+2,end_column=15); w.cell(row=RL+2,column=1).alignment=Alignment(wrap_text=True,vertical="top"); w.row_dimensions[RL+2].height=30
widths(w,[44,10]+[7]*13); w.freeze_panes="C5"; w.sheet_view.showGridLines=False
# ---------- Painel ----------
p=wb.create_sheet("Painel",0)
p["A1"]='=Config!B4&" · Metas do trimestre · "&Config!B5'; p["A1"].font=F(bold=True,size=16,color=UVA); p.merge_cells("A1:H1")
p["A2"]='="Semana "&Config!B9&" de 13 · "&TEXT(Config!B10,"0%")&" do trimestre decorrido. Nada para preencher aqui."'; nota(p["A2"]); p.merge_cells("A2:H2")
MJ=f"Metas!$J$5:$J${RL}"; MB=f"Metas!$B$5:$B${RL}"; MH=f"Metas!$H$5:$H${RL}"
kpi(p,4,1,"Resultados-chave",f'=COUNTIFS({MB},"<>")',LAVANDA,UVA)
kpi(p,4,3,"Atingidos",f'=COUNTIFS({MJ},"Atingido")',VERDE,VERDE_T)
kpi(p,4,5,"Em risco",f'=COUNTIFS({MJ},"Em risco")',VERM,VERM_T)
kpi(p,4,7,"Progresso médio",f'=IFERROR(AVERAGEIFS({MH},{MB},"<>"),0)',SOL,UVA,fmt="0%")
p["A7"]="Por objetivo"; p["A7"].font=F(bold=True,size=13,color=UVA)
hdr(p,8,["Objetivo","Resultados-chave","Progresso médio","Atingidos","Em risco","Barra"]); p.merge_cells("F8:H8")
for o in range(NO):
    r=9+o; a=5+o*NK; b=a+NK-1; src=f"Metas!$A${a}"
    p.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(p.cell(row=r,column=1),center=False); p.cell(row=r,column=1).alignment=Alignment(wrap_text=True,vertical="center")
    p.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS(Metas!$B${a}:$B${b},"<>"))'); calc(p.cell(row=r,column=2))
    p.cell(row=r,column=3,value=f'=IF(OR({src}="",B{r}=0),"",AVERAGEIFS(Metas!$H${a}:$H${b},Metas!$B${a}:$B${b},"<>"))'); calc(p.cell(row=r,column=3),PCT)
    p.cell(row=r,column=4,value=f'=IF({src}="","",COUNTIFS(Metas!$J${a}:$J${b},"Atingido"))'); calc(p.cell(row=r,column=4))
    p.cell(row=r,column=5,value=f'=IF({src}="","",COUNTIFS(Metas!$J${a}:$J${b},"Em risco"))'); calc(p.cell(row=r,column=5))
    p.cell(row=r,column=6,value=f'=IF(C{r}="","",REPT("█",ROUND(C{r}*30,0)))'); p.cell(row=r,column=6).font=F(size=10,color=LILAS); p.cell(row=r,column=6).border=borda; p.merge_cells(start_row=r,start_column=6,end_row=r,end_column=8)
    p.row_dimensions[r].height=30
R_T=9+NO+1
p.cell(row=R_T,column=1,value="Todos os resultados-chave").font=F(bold=True,size=13,color=UVA)
hdr(p,R_T+1,["Resultado-chave","Dono","Atual","Meta","Progresso","Esperado","Semáforo","Barra"])
for i,r in enumerate(rows):
    rr=R_T+2+i
    p.cell(row=rr,column=1,value=f'=IF(Metas!B{r}="","",Metas!B{r})'); calc(p.cell(row=rr,column=1),center=False)
    p.cell(row=rr,column=2,value=f'=IF(Metas!B{r}="","",Metas!C{r})'); calc(p.cell(row=rr,column=2))
    p.cell(row=rr,column=3,value=f'=IF(Metas!B{r}="","",Metas!G{r})'); calc(p.cell(row=rr,column=3),"#,##0.#")
    p.cell(row=rr,column=4,value=f'=IF(Metas!B{r}="","",Metas!F{r})'); calc(p.cell(row=rr,column=4),"#,##0.#")
    p.cell(row=rr,column=5,value=f'=IF(Metas!B{r}="","",Metas!H{r})'); calc(p.cell(row=rr,column=5),PCT)
    p.cell(row=rr,column=6,value=f'=IF(Metas!B{r}="","",Metas!I{r})'); calc(p.cell(row=rr,column=6),PCT)
    p.cell(row=rr,column=7,value=f'=IF(Metas!B{r}="","",Metas!J{r})'); calc(p.cell(row=rr,column=7))
    p.cell(row=rr,column=8,value=f'=IF(E{rr}="","",REPT("█",ROUND(E{rr}*20,0)))'); p.cell(row=rr,column=8).font=F(size=10,color=LILAS); p.cell(row=rr,column=8).border=borda
R1=R_T+2; R2=R1+NO*NK-1
for cor,txt,fnt in ((VERDE,"Atingido",VERDE_T),("E6F4EA","No ritmo",VERDE_T),(AMARELO,"Atenção","7A5200"),(VERM,"Em risco",VERM_T)):
    p.conditional_formatting.add(f"G{R1}:G{R2}", FormulaRule(formula=[f'G{R1}="{txt}"'], fill=fill(cor), font=F(color=fnt,size=10,bold=(txt in ("Atingido","Em risco")))))
p.cell(row=R2+2,column=1,value="Em risco primeiro: veja o que muda na rotina da semana (planilha 03) antes de mexer na meta.").font=F(size=9,color=LILAS)
p.merge_cells(start_row=R2+2,start_column=1,end_row=R2+2,end_column=8)
widths(p,(44,20,10,10,11,10,11,24)); p.freeze_panes="A4"; p.sheet_view.showGridLines=False
como_usar(wb,"Metas do Trimestre",[
 ("O que esta planilha faz","Você define até 3 objetivos da clínica com até 3 resultados-chave cada (ponto de partida, meta, valor atual). Ela calcula o progresso, compara com o tempo já decorrido do trimestre e acende o semáforo: atingido, no ritmo, atenção ou em risco."),
 ("Passo 1","Em Config, preencha o trimestre, as datas de início e fim, troque a data de referência por =HOJE() (no exemplo ela está congelada em 14/09/2026) e liste as pessoas da clínica (de cima para baixo, sem pular linha)."),
 ("Passo 2","Em Metas, escreva cada objetivo e seus resultados-chave. Ponto de partida é o valor no dia 1; meta é onde quer chegar; valor atual é o número de hoje. Diga se maior ou menor é melhor. No exemplo, cada resultado-chave é um número de outra planilha do kit: ocupação e faltas (01, 02), glosa e atrasos (13), inadimplência, reserva e provisão (14, 12, 10)."),
 ("Passo 3","Toda sexta, atualize o valor atual (os números vêm do Painel da clínica, 17, ou dos painéis das planilhas de origem) e copie para a coluna da semana em Semanas. Semana sem número: escreva \"—\", não 0. O Painel mostra o resumo por objetivo e a lista completa com semáforo. No exemplo, S1 a S11 são as sextas de 03/07 a 11/09/2026."),
 ("Rotina","Esta é uma planilha MENSAL. Na sexta, os valores já estão no Painel da clínica (17), que você atualiza em 3 minutos: copiar o número de cada resultado-chave para a coluna da semana em Semanas leva menos de um minuto e cabe nessa mesma parada. A conversa sobre as metas é mensal: primeira segunda do mês, 20 minutos entre os sócios olhando o Painel."),
 ("Com a IA","Copie a tabela \"Todos os resultados-chave\" e use o prompt \"Painel 05 · Meta realista para o trimestre\" ou \"Painel 06 · Meta × realizado: explicar o desvio\" da biblioteca do kit. No fim do trimestre, o modelo de apresentação \"Resultado do mês para os sócios\"."),
])
proteger(wb); salvar(wb,"19-metas-do-trimestre.xlsx","Metas do Trimestre · Kit de Gestão para Médicos")
