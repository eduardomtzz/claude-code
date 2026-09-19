import openpyxl,pathlib,sys,datetime
P=pathlib.Path("/home/user/claude-code/projetos/gestao-ia-planilhas/produto")
KITS=[("01-essencial","Kit IA no Trabalho · Essencial (R$ 37)","kit-essencial"),("02-completo","Kit IA no Trabalho · Completo (R$ 197)","kit-completo"),("03-advogados","Kit de Gestão para Advogados (R$ 497)","kit-advogados"),("04-medicos","Kit de Gestão para Médicos (R$ 697)","kit-medicos")]
out=[f"# Inventário das 53 planilhas · {datetime.date.today().strftime('%d/%m/%Y')}, depois de nove rodadas de auditoria\n","Gerado dos próprios arquivos de `entrega/` com openpyxl. As quatro últimas colunas são de controle e devem ser zero: validação sem bloqueio de erro, célula desbloqueada fora do amarelo, `_xlfn` e regra condicional apontando direto para outra aba (sem INDIRECT).\n"]
T={"f":0,"e":0,"v":0,"cf":0,"abas":0,"arq":0}
for pasta,nome,kit in KITS:
    files=sorted((P/kit/"entrega").glob("[0-2][0-9]-*.xlsx"))
    out.append(f"\n## {pasta} — {nome} · {len(files)} planilhas\n\n| Arquivo | Abas | Fórmulas | Entradas | Listas | Regras cond. | Sem bloqueio | Soltas fora do amarelo | _xlfn | Regra sem INDIRECT |\n|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for f in files:
        wb=openpyxl.load_workbook(f); nf=ne=nv=nsb=nsolta=nx=ncf=ncfx=0
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    v=c.value
                    if isinstance(v,str) and v.startswith("="):
                        nf+=1
                        if "_xlfn" in v: nx+=1
                    if c.protection is not None and not c.protection.locked and v is not None or (c.protection is not None and not c.protection.locked and c.fill is not None and c.fill.fgColor is not None and str(c.fill.fgColor.rgb).endswith("FFF4CC")):
                        ne+=1
                        rgb=str(c.fill.fgColor.rgb) if c.fill is not None and c.fill.fgColor is not None else ""
                        if not rgb.endswith("FFF4CC") and not (isinstance(v,str) and v.startswith("=")): nsolta+=0  # entradas sem amarelo contadas abaixo
            for dv in ws.data_validations.dataValidation:
                nv+=1
                if not dv.showErrorMessage: nsb+=1
            for cf in ws.conditional_formatting:
                for r in cf.rules:
                    ncf+=1
                    for fm in (r.formula or []):
                        if "!" in fm and "INDIRECT(" not in fm: ncfx+=1
            # soltas: desbloqueadas sem amarelo (só células com valor ou estilo)
            for row in ws.iter_rows():
                for c in row:
                    if type(c).__name__!="MergedCell" and c.protection is not None and not c.protection.locked:
                        rgb=str(c.fill.fgColor.rgb) if c.fill is not None and c.fill.fgColor is not None else ""
                        if not rgb.endswith("FFF4CC") and (c.value is not None or c.has_style): nsolta+=1
        out.append(f"| `{f.name}` | {' · '.join(wb.sheetnames)} | {nf} | {ne} | {nv} | {ncf} | {nsb} | {nsolta} | {nx} | {ncfx} |")
        T["f"]+=nf; T["e"]+=ne; T["v"]+=nv; T["cf"]+=ncf; T["abas"]+=len(wb.sheetnames); T["arq"]+=1
out.append(f"\n## Total\n\n{T['arq']} arquivos · {T['abas']} abas · {T['f']:,} fórmulas · {T['e']:,} células de entrada · {T['v']} validações · {T['cf']} regras condicionais.".replace(",","."))
pathlib.Path(sys.argv[1]).write_text("\n".join(out)+"\n"); print("\n".join(out[-3:]))
