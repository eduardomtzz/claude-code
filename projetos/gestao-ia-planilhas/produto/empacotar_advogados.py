#!/usr/bin/env python3
"""Monta kit-advogados/entrega/ (planilhas 01-20, PDFs 21-26 + txt, modelos 27-29, LEIA-ME, videos/) e o zip."""
import pathlib, shutil, subprocess, zipfile, sys
ROOT=pathlib.Path(__file__).resolve().parent/'kit-advogados'; E=ROOT/'entrega'; E.mkdir(exist_ok=True)
for f in sorted(ROOT.glob('[0-2][0-9]-*.xlsx')): shutil.copy2(f, E/f.name)
if '--pdf' in sys.argv: subprocess.run(['python3','build_pdfs.py','--pdf','entrega'],cwd=str(ROOT),check=True)
for f in sorted(ROOT.glob('2[7-9]-*.pptx')): shutil.copy2(f, E/f.name)
if (ROOT/'LEIA-ME.txt').exists(): shutil.copy2(ROOT/'LEIA-ME.txt', E/'LEIA-ME.txt')
if '--zip' in sys.argv:
    zipf=ROOT/'kit-de-gestao-para-advogados-v1.zip'
    with zipfile.ZipFile(zipf,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(E.rglob('*')):
            if f.is_file(): z.write(f, f.relative_to(E))
    print('pacote:', zipf, round(zipf.stat().st_size/1e6,1),'MB')
print('\n'.join(sorted(str(p.relative_to(E)) for p in E.rglob('*') if p.is_file())))
