#!/usr/bin/env python3
"""Recalcula todos os .xlsx de entrega/ dos quatro kits no LibreOffice pt-BR e
conta erro de fórmula célula por célula. Não altera o arquivo entregue: trabalha
numa cópia."""
import subprocess, pathlib, shutil, os, sys, re
import openpyxl
R = pathlib.Path('/home/user/claude-code/projetos/gestao-ia-planilhas/produto')
S = pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
PROFILE = S/'lo-ptbr'; WORK = S/'recalc-todos'
ERROS = ('#REF!','#VALUE!','#NAME?','#DIV/0!','#N/A','#NUM!','#NULL!','Err:')
total_f = total_e = 0
for kit in ('kit-essencial','kit-completo','kit-advogados','kit-medicos'):
    ent = R/kit/'entrega'
    out = WORK/kit; shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    arqs = sorted(ent.glob('*.xlsx'))
    for a in arqs: shutil.copy2(a, out/a.name)
    subprocess.run(['soffice','--headless',f'-env:UserInstallation=file://{PROFILE}',
                    '--convert-to','xlsx','--outdir',str(out/'calc')]+[str(out/a.name) for a in arqs],
                   env={**os.environ,'SAL_USE_VCLPLUGIN':'svp'}, check=True,
                   capture_output=True, timeout=3600)
    kf = ke = intenc = 0; ruins = []
    for a in arqs:
        rec = out/'calc'/a.name
        if not rec.exists(): ruins.append(f'{a.name}: não recalculou'); continue
        wbf = openpyxl.load_workbook(a); wbv = openpyxl.load_workbook(rec, data_only=True)
        for ws in wbf.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str) and c.value.startswith('='):
                        kf += 1
                        v = wbv[ws.title][c.coordinate].value
                        if not (isinstance(v, str) and any(v.startswith(e) for e in ERROS)):
                            continue
                        # #N/A vindo de NA() é proposital: no Excel faz o gráfico deixar
                        # um vão no mês sem dado, em vez de puxar a linha para zero.
                        if v.startswith('#N/A') and 'NA()' in c.value:
                            intenc += 1; continue
                        ke += 1; ruins.append(f'{a.name}!{ws.title}!{c.coordinate} = {v}')
    total_f += kf; total_e += ke
    print(f'{kit:16s} {len(arqs):2d} planilhas · {kf:6d} fórmulas · {ke} erro(s)'
          f'{f" · {intenc} vão de gráfico proposital" if intenc else ""}', flush=True)
    for r in ruins[:10]: print('   ', r)
print(f'\nTOTAL: {total_f} fórmulas, {total_e} erro(s)')
sys.exit(1 if total_e else 0)
