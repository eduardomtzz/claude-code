#!/usr/bin/env python3
"""Zip de entrega do Kit Essencial a partir de kit-essencial/entrega/."""
import pathlib, zipfile
ROOT=pathlib.Path(__file__).resolve().parent/'kit-essencial'; E=ROOT/'entrega'; zipf=ROOT/'kit-ia-no-trabalho-essencial-v1.zip'
with zipfile.ZipFile(zipf,'w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(E.rglob('*')):
        if f.is_file(): z.write(f, f.relative_to(E))
print('pacote:', zipf, round(zipf.stat().st_size/1e6,1),'MB', sum(1 for f in E.rglob('*') if f.is_file()),'arquivos')
