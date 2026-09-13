#!/usr/bin/env python3
"""Planilha 10 do Kit Completo: Base Limpa. Gera 10-base-limpa.xlsx"""
from ssg import *
from openpyxl.worksheet.table import Table, TableStyleInfo
from datetime import date
import random
N=1000; R0=2; RN=R0+N-1
wb=Workbook()
# ---------- Como usar (primeira) ----------
u=wb.active; u.title="Como usar"
u["A1"]="Base Limpa"; u["A1"].font=F(bold=True,size=20,color=UVA)
u["A2"]=KIT; u["A2"].font=F(size=10,color=LILAS)
linhas=[
 ("O que esta planilha faz","É o modelo de uma base de dados \"certa\": uma linha por registro, uma coluna por informação, sem células mescladas, sem totais no meio, com listas e validações. É a planilha que ensina a fazer todas as outras, e a que a tabela dinâmica e a IA leem sem erro."),
 ("As 7 regras","1. Cabeçalho na linha 1, uma coluna por informação. 2. Uma linha por registro; nada de linhas em branco ou subtotais no meio. 3. Datas como data, números como número, texto como texto. 4. Categorias vêm de lista, não digitadas à mão. 5. Nada mesclado. 6. O que é calculado fica em coluna própria, com fórmula igual do topo ao fim. 7. Os totais e as análises ficam em outra aba."),
 ("Passo 1","Na aba Base, apague os exemplos e cole os seus dados respeitando o cabeçalho. Troque os nomes das colunas para o seu caso; mantenha uma informação por coluna."),
 ("Passo 2","Use a aba Listas para as categorias. Cada coluna de categoria da Base aponta para uma lista; assim ninguém escreve \"marketing\", \"Marketing\" e \"MKT\" como três coisas diferentes."),
 ("Passo 3","Rode o Checklist de limpeza: ele conta linhas em branco, duplicadas, datas inválidas, categorias fora da lista e valores negativos. Zerou tudo, a base está pronta."),
 ("Passo 4","Na aba Resumo, o exemplo de análise por categoria e mês feito só com SOMASES e CONT.SES. A aula 2 mostra como montar a tabela dinâmica a partir desta Base."),
 ("Com a IA","Copie 20 a 30 linhas da Base (sem dados pessoais) e use \"Estruturar 03: desenhar as colunas\" para adaptar ao seu caso, ou \"Analisar 08: resumo executivo de uma tabela grande\"."),
 ("Legenda","Células amarelas: você preenche. Brancas: calculadas."),
 ("Proteção","Nesta planilha só as abas Checklist e Resumo são protegidas; a Base e as Listas ficam livres para você colar dados."),
 ("Google Sheets","Faça upload no Google Drive e abra com o Google Sheets. Para a tabela dinâmica: Inserir > Tabela dinâmica, selecionando a aba Base inteira."),
 ("Exemplos","Prisma Comunicação é uma empresa fictícia. Os dados são inventados."),
 ("Suporte","suporte@seusociogestor.com.br · resposta em até 5 dias úteis · reembolso em até 7 dias pelo mesmo canal."),
]
for i,(a,b) in enumerate(linhas,start=4):
    u.cell(row=i,column=1,value=a).font=F(bold=True,color=UVA); u.cell(row=i,column=2,value=b).font=F(color=TINTA)
    u.cell(row=i,column=2).alignment=Alignment(wrap_text=True,vertical="top"); u.cell(row=i,column=1).alignment=Alignment(vertical="top"); u.row_dimensions[i].height=58 if i==5 else 46
u.column_dimensions["A"].width=20; u.column_dimensions["B"].width=95; u.sheet_view.showGridLines=False
# ---------- Listas ----------
ls=wb.create_sheet("Listas")
titulo(ls,"Listas","Cada coluna é uma lista usada pela Base. Mude à vontade; adicione linhas abaixo.",merge_to="F")
hdr(ls,4,["Categoria","Canal","Responsável","Status","Cliente"])
cats=["Serviço","Produto","Reembolso","Ajuste"]; canais=["Indicação","Instagram","Site","Evento","Cliente antigo"]; resp=["Ana","Bruno","Carla","Diego"]; status=["Pago","Em aberto","Cancelado"]
cli=["Loja Verde","Bistrô 42","Horizonte","Padaria do Sol","Clínica Bem-Estar","Aurora Móveis","Café Central","Escola Nova Era"]
for j,col in enumerate((cats,canais,resp,status,cli)):
    for i in range(30):
        c=ls.cell(row=5+i,column=1+j); inp(c)
        if i<len(col): c.value=col[i]
widths(ls,(18,16,16,14,22)); ls.sheet_view.showGridLines=False
# ---------- Base ----------
b=wb.create_sheet("Base")
cols=["ID","Data","Cliente","Categoria","Canal","Responsável","Descrição","Quantidade","Valor unitário","Valor total","Status","Mês","Ano"]
hdr(b,1,cols,height=22)
for r in range(R0,RN+1):
    b.cell(row=r,column=1,value=f'=IF(B{r}="","",ROW()-1)'); calc(b.cell(row=r,column=1))
    for c in (2,3,4,5,6,7,8,9,11): inp(b.cell(row=r,column=c))
    for c in (2,3,4,5,6,8,11): b.cell(row=r,column=c).alignment=Alignment(horizontal="center")
    b.cell(row=r,column=2).number_format=DATA; b.cell(row=r,column=9).number_format=BRL; b.cell(row=r,column=8).number_format="0"
    b.cell(row=r,column=10,value=f'=IF(OR(H{r}="",I{r}=""),"",H{r}*I{r})'); calc(b.cell(row=r,column=10),BRL)
    b.cell(row=r,column=12,value=f'=IF(B{r}="","",MONTH(B{r}))'); calc(b.cell(row=r,column=12))
    b.cell(row=r,column=13,value=f'=IF(B{r}="","",YEAR(B{r}))'); calc(b.cell(row=r,column=13))
dvs=[lista("=Listas!$E$5:$E$34",strict=False),lista("=Listas!$A$5:$A$34"),lista("=Listas!$B$5:$B$34"),lista("=Listas!$C$5:$C$34"),lista("=Listas!$D$5:$D$34"),
     DataValidation(type="date",operator="greaterThan",formula1="1",allow_blank=True),DataValidation(type="decimal",operator="greaterThanOrEqual",formula1="0",allow_blank=True)]
for dv,rng in zip(dvs,[f"C{R0}:C{RN}",f"D{R0}:D{RN}",f"E{R0}:E{RN}",f"F{R0}:F{RN}",f"K{R0}:K{RN}",f"B{R0}:B{RN}",f"H{R0}:I{RN}"]): dv.add(rng); b.add_data_validation(dv)
widths(b,(6,12,22,12,14,14,34,11,14,14,12,6,7)); b.freeze_panes="A2"; b.auto_filter.ref=f"A1:M{RN}"
random.seed(5); rows=[]
desc={"Serviço":["Posts do mês","Layout de página","Consultoria de marca","Diagramação","Vídeo curto"],"Produto":["Template de apresentação","Pacote de ícones","E-book de marca"],"Reembolso":["Estorno parcial"],"Ajuste":["Ajuste de fatura"]}
for i in range(180):
    d=date(2026,1,1)+__import__('datetime').timedelta(days=random.randint(0,255))
    cat=random.choices(cats,[70,20,5,5])[0]; q=random.choice([1,1,1,2,3]); vu={"Serviço":random.choice([800,1200,1500,2400,3200]),"Produto":random.choice([49,97,149]),"Reembolso":-random.choice([200,400]),"Ajuste":random.choice([-150,150])}[cat]
    rows.append((d,random.choice(cli),cat,random.choice(canais),random.choice(resp),random.choice(desc[cat]),q,vu,random.choices(status,[80,15,5])[0]))
rows.sort(key=lambda x:x[0])
for i,row in enumerate(rows):
    for c,v in zip((2,3,4,5,6,7,8,9,11),row): b.cell(row=R0+i,column=c,value=v)
# ---------- Checklist ----------
ck=wb.create_sheet("Checklist")
titulo(ck,"Checklist de limpeza","Rode antes de analisar. Tudo zerado = base pronta para tabela dinâmica e para a IA.",merge_to="D")
hdr(ck,4,["Verificação","Resultado","Situação","Como corrigir"])
BB=f"Base!$B${R0}:$B${RN}"; BC=f"Base!$C${R0}:$C${RN}"; BD=f"Base!$D${R0}:$D${RN}"; BH=f"Base!$H${R0}:$H${RN}"; BI=f"Base!$I${R0}:$I${RN}"; BK=f"Base!$K${R0}:$K${RN}"; BG=f"Base!$G${R0}:$G${RN}"
checks=[("Linhas preenchidas",f'=COUNTA({BB})',None,"Só informação."),
 ("Linhas com data mas sem valor",f'=COUNTIFS({BB},"<>",{BI},"")',"=B6=0","Preencha o valor unitário ou apague a linha."),
 ("Linhas com valor mas sem data",f'=COUNTIFS({BB},"",{BI},"<>")',"=B7=0","Toda linha precisa de data."),
 ("Datas fora do intervalo (antes de 2020 ou no futuro)",f'=COUNTIFS({BB},"<"&DATE(2020,1,1))+COUNTIFS({BB},">"&TODAY())',"=B8=0","Confira digitação: 2062 em vez de 2026, por exemplo."),
 ("Categorias fora da lista",f'=COUNTIFS({BB},"<>")-SUMPRODUCT(COUNTIFS({BD},Listas!$A$5:$A$34,{BB},"<>"))',"=B9=0","Use a lista da coluna Categoria; padronize maiúsculas e abreviações."),
 ("Clientes fora da lista",f'=COUNTIFS({BB},"<>")-SUMPRODUCT(COUNTIFS({BC},Listas!$E$5:$E$34,{BB},"<>"))',"=B10=0","Cadastre o cliente em Listas ou corrija o nome."),
 ("Status em branco",f'=COUNTIFS({BB},"<>",{BK},"")',"=B11=0","Escolha Pago, Em aberto ou Cancelado."),
 ("Quantidade zero ou em branco",f'=COUNTIFS({BB},"<>",{BH},"")+COUNTIFS({BB},"<>",{BH},0)',"=B12=0","Quantidade mínima é 1."),
 ("Descrições duplicadas no mesmo dia e cliente (possível lançamento em dobro)",f'=SUMPRODUCT(--(COUNTIFS({BB},{BB},{BC},{BC},{BG},{BG},{BI},{BI})>1),--({BB}<>""))',"=B13=0","Abra o filtro por cliente e data e confira se é repetição."),
 ("Células mescladas na Base (confira: Página Inicial > Mesclar deve estar desligado)","0","=B14=0","Nunca mescle células em uma base. Se mesclar, a tabela dinâmica quebra."),
]
for i,(a,f_,ok,como) in enumerate(checks):
    r=5+i
    ck.cell(row=r,column=1,value=a); calc(ck.cell(row=r,column=1),center=False)
    ck.cell(row=r,column=2,value=f_ if f_.startswith("=") else int(f_)); calc(ck.cell(row=r,column=2))
    ck.cell(row=r,column=3,value=("—" if ok is None else f'=IF({ok[1:]},"OK","Corrigir")')); calc(ck.cell(row=r,column=3))
    ck.cell(row=r,column=4,value=como); calc(ck.cell(row=r,column=4),center=False); ck.cell(row=r,column=4).alignment=Alignment(wrap_text=True)
ck.conditional_formatting.add("C5:C14", FormulaRule(formula=['C5="OK"'], fill=fill(VERDE), font=F(color=VERDE_T,size=10,bold=True)))
ck.conditional_formatting.add("C5:C14", FormulaRule(formula=['C5="Corrigir"'], fill=fill(VERM), font=F(color=VERM_T,size=10,bold=True)))
ck["A16"]="Base pronta?"; rotulo(ck["A16"]); ck["B16"]='=IF(COUNTIF(C6:C14,"Corrigir")=0,"Sim: pode analisar","Ainda não: "&COUNTIF(C6:C14,"Corrigir")&" item(ns) para corrigir")'; ck["B16"].font=F(bold=True,size=12,color=UVA); ck.merge_cells("B16:D16")
widths(ck,(52,12,12,60)); ck.sheet_view.showGridLines=False
# ---------- Resumo ----------
s=wb.create_sheet("Resumo")
titulo(s,"Resumo por categoria e mês","Exemplo de análise feita só com SOMASES e CONT.SES em cima da Base. A tabela dinâmica faz o mesmo em 3 cliques (aula 2).",merge_to="O")
s["A4"]="Ano"; rotulo(s["A4"]); s["B4"]=2026; inp(s["B4"],center=True)
s["A5"]="Só status"; rotulo(s["A5"]); s["B5"]="Pago"; inp(s["B5"],center=True)
dvst=lista("=Listas!$D$5:$D$34"); dvst.add("B5"); s.add_data_validation(dvst)
hdr(s,7,["Categoria"]+[m_[:3] for m_ in MESES]+["Total"])
BJ=f"Base!$J${R0}:$J${RN}"; BL=f"Base!$L${R0}:$L${RN}"; BM=f"Base!$M${R0}:$M${RN}"
for i in range(8):
    r=8+i; src=f"Listas!$A${5+i}"
    s.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(s.cell(row=r,column=1),center=False)
    for m_ in range(12):
        s.cell(row=r,column=2+m_,value=f'=IF({src}="","",SUMIFS({BJ},{BD},{src},{BL},{m_+1},{BM},$B$4,{BK},$B$5))'); calc(s.cell(row=r,column=2+m_),BRL0)
    s.cell(row=r,column=14,value=f'=IF(A{r}="","",SUM(B{r}:M{r}))'); calc(s.cell(row=r,column=14),BRL0)
s.cell(row=16,column=1,value="Total"); rotulo(s.cell(row=16,column=1)); s.cell(row=16,column=1).border=borda
for m_ in range(13):
    c=s.cell(row=16,column=2+m_,value=f'=SUM({L(2+m_)}8:{L(2+m_)}15)'); calc(c,BRL0); c.font=F(bold=True,color=UVA,size=10)
s["A18"]="Por cliente"; s["A18"].font=F(bold=True,size=13,color=UVA)
hdr(s,19,["Cliente","Registros","Valor no ano","Ticket médio","Último registro"])
for i in range(8):
    r=20+i; src=f"Listas!$E${5+i}"
    s.cell(row=r,column=1,value=f'=IF({src}="","",{src})'); calc(s.cell(row=r,column=1),center=False)
    s.cell(row=r,column=2,value=f'=IF({src}="","",COUNTIFS({BC},{src},{BM},$B$4,{BK},$B$5))'); calc(s.cell(row=r,column=2))
    s.cell(row=r,column=3,value=f'=IF({src}="","",SUMIFS({BJ},{BC},{src},{BM},$B$4,{BK},$B$5))'); calc(s.cell(row=r,column=3),BRL0)
    s.cell(row=r,column=4,value=f'=IF(OR({src}="",B{r}=0),"",C{r}/B{r})'); calc(s.cell(row=r,column=4),BRL0)
    s.cell(row=r,column=5,value=f'=IF({src}="","",IFERROR(IF(_xlfn.MAXIFS({BB},{BC},{src})=0,"",_xlfn.MAXIFS({BB},{BC},{src})),""))'); calc(s.cell(row=r,column=5),DATA)
widths(s,[22]+[10]*12+[12]); s.freeze_panes="B8"; s.sheet_view.showGridLines=False
for ws in (ck,s):
    ws.protection.sheet=True; ws.protection.formatColumns=False; ws.protection.formatRows=False; ws.protection.selectLockedCells=False
salvar(wb,"10-base-limpa.xlsx","Base Limpa · Kit IA no Trabalho Completo")
