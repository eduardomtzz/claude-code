"""Varredura de entradas: TODAS as células de entrada preenchidas do exemplo recebem vazio, texto e -1;
em cada coluna de tabela, a primeira célula de entrada vazia depois da última preenchida recebe texto e 1
(linha nova incompleta). Recalcula no LibreOffice pt-BR e compara TODAS as fórmulas com o exemplo. Sinaliza:
ERR  erro de fórmula;  NUM  número que mudou de valor sem aviso;  NEW  fórmula vazia que passou a número;
CLS  rótulo que trocou por outro rótulo (sem palavra de aviso).
Uso: python3 fuzz.py <arquivo relativo a produto/> <saida.json>"""
import openpyxl, subprocess, pathlib, os, shutil, sys, json, re
P=pathlib.Path('/home/user/claude-code/projetos/gestao-ia-planilhas/produto')
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
arq=sys.argv[1]; out=sys.argv[2]; tag=pathlib.Path(arq).stem
W=S/'fz'/('w-'+tag); shutil.rmtree(W,ignore_errors=True); (W/'calc').mkdir(parents=True)
ERR=('#REF!','#VALUE!','#NAME?','#DIV/0!','#N/A','#NUM!','#NULL!','Err:')
AVISO=re.compile(r'falta|Falta|inválid|incomplet|texto|sem base|Faltam|Corrija|Complete|Preencha|Sem recomendação|cadastro|Sem base|Estime|Margens|margens|Regra de risco|volume|Não há|preço inválido|Preço inválido|dados|sem nome',re.I)
wf=openpyxl.load_workbook(P/arq)
base=openpyxl.load_workbook(P/arq,data_only=True)
# entradas: desbloqueadas e preenchidas com valor (não fórmula); em cada coluna, 1ª, do meio e última linha
cols={}
for ws in wf.worksheets:
    if ws.title=='Como usar': continue
    for row in ws.iter_rows():
        for c in row:
            if type(c).__name__=='MergedCell' or not c.protection or c.protection.locked: continue
            if c.value is None or (isinstance(c.value,str) and c.value.startswith('=')): continue
            cols.setdefault((ws.title,c.column_letter),[]).append(c)
alvos=[]
for k,cs in cols.items():
    for c in cs: alvos.append((c.parent.title,c.coordinate,c.value))   # auditoria final-6: sem amostragem
casos=[]
for sh,co,v in alvos:
    casos.append((sh,co,None,'vazio')); casos.append((sh,co,'abc','texto'))
    if isinstance(v,(int,float)) and not isinstance(v,bool): casos.append((sh,co,-1,'negativo'))
# linha nova: primeira entrada vazia abaixo da última preenchida, em colunas de tabela (2+ células)
for (sh,col),cs in cols.items():
    if len(cs)<2: continue
    ws=wf[sh]; r=max(c.row for c in cs)+1
    c=ws[f'{col}{r}']
    if type(c).__name__=='MergedCell' or c.value is not None or not c.protection or c.protection.locked: continue
    casos.append((sh,c.coordinate,'abc','novo-texto')); casos.append((sh,c.coordinate,1,'novo-num'))
nomes=[]
for i,(sh,co,v,_) in enumerate(casos):
    wb=openpyxl.load_workbook(P/arq); wb[sh][co].value=v; fn=f"c{i:04d}.xlsx"; wb.save(W/fn); nomes.append(fn)
for k in range(0,len(nomes),120):
    subprocess.run(['soffice','--headless',f'-env:UserInstallation=file://{S}/lo-ptbr','--convert-to','xlsx','--outdir',str(W/'calc')]+[str(W/n) for n in nomes[k:k+120]],
                   env={**os.environ,'SAL_USE_VCLPLUGIN':'svp'},check=True,capture_output=True,timeout=3600)
fcells=[(ws.title,c.coordinate) for ws in wf.worksheets for row in ws.iter_rows() for c in row if isinstance(c.value,str) and c.value.startswith('=')]
res=[]
for i,(sh,co,v,modo) in enumerate(casos):
    wb=openpyxl.load_workbook(W/'calc'/nomes[i],data_only=True); r={'entrada':f'{sh}!{co}','modo':modo,'ERR':[],'NUM':[],'NEW':[],'CLS':[]}
    for s2,c2 in fcells:
        a=base[s2][c2].value; b=wb[s2][c2].value
        if isinstance(b,str) and b.startswith(ERR): r['ERR'].append(f'{s2}!{c2}'); continue
        if isinstance(a,(int,float)) and isinstance(b,(int,float)) and not isinstance(a,bool) and abs(a-b)>1e-9*max(1,abs(a)):
            r['NUM'].append(f'{s2}!{c2}: {a:.6g}→{b:.6g}')
        elif (a is None or a=='') and isinstance(b,(int,float)) and not isinstance(b,bool):
            r['NEW'].append(f'{s2}!{c2}: vazio→{b:.6g}')
        elif isinstance(a,str) and isinstance(b,str) and a!=b and a and b and not AVISO.search(a) and not AVISO.search(b) and len(a)<45 and len(b)<45:
            r['CLS'].append(f'{s2}!{c2}: {a}→{b}')
    res.append(r)
json.dump(res,open(out,'w'),ensure_ascii=False,indent=0)
print(arq,len(casos),'casos;',sum(bool(r['ERR']) for r in res),'com erro;',sum(bool(r['NUM']) for r in res),'com número mudado;',sum(bool(r['NEW']) for r in res),'com número novo;',sum(bool(r['CLS']) for r in res),'com rótulo mudado')
