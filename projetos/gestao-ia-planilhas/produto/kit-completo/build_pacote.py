#!/usr/bin/env python3
"""Monta o pacote de entrega do Kit Completo (zip) a partir dos arquivos gerados."""
import pathlib, shutil, subprocess, zipfile
ROOT=pathlib.Path(__file__).resolve().parent; ESS=ROOT.parent/'kit-essencial'; E=ROOT/'entrega'
E.mkdir(exist_ok=True)
# planilhas 1-3 do Essencial, 4-10 daqui
for f in ['01-semana-organizada.xlsx','02-relatorio-mensal-pronto.xlsx','03-ganhos-e-gastos.xlsx']: shutil.copy2(ESS/'entrega'/f, E/f)
for f in sorted(ROOT.glob('0[4-9]-*.xlsx'))+sorted(ROOT.glob('10-*.xlsx')): shutil.copy2(f, E/f.name)
# bibliotecas: A (gerada do 04 do Essencial com capa/rodapé do Completo) e B; txt para copiar
subprocess.run(['python3',str(ESS/'build_pdfs.py'),'--completo'],check=True,cwd=str(ESS))
(E/'11-biblioteca-de-prompts-b.txt').write_text((ROOT/'11-biblioteca-de-prompts-b.md').read_text())
# modelo de 8 slides do Essencial
shutil.copy2(ESS/'entrega'/'06-modelo-apresentacao-8-slides.pptx', E/'15-modelo-relatorio-mensal-8-slides.pptx')
shutil.copy2(ROOT/'LEIA-ME.txt', E/'LEIA-ME.txt')  # fonte editável: kit-completo/LEIA-ME.txt
zipf=ROOT/'kit-ia-no-trabalho-completo-v1.zip'
with zipfile.ZipFile(zipf,'w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(E.rglob('*')):
        if f.is_file(): z.write(f, f.relative_to(E))
print('pacote:', zipf, round(zipf.stat().st_size/1e6,1),'MB'); print('\n'.join(sorted(str(p.relative_to(E)) for p in E.rglob('*') if p.is_file())))
