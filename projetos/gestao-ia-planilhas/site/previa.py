#!/usr/bin/env python3
"""Monta a prévia navegável do site para o visualizador de artefatos do Claude.
Uso: python3 previa.py public <pasta-da-previa>
- converte todo caminho absoluto (/assets/..., /kit/, /#kits, url(/...)) em relativo à página;
- gera page.html (a home só com o corpo e as referências de estilo): o visualizador embrulha a página
  principal num documento próprio, e um <html> completo dentro dele quebra estilo e links;
- lista em preview-files.json todos os outros arquivos, que são publicados ao lado, nos mesmos caminhos.
Publicar: Artifact(file_path=<pasta>/page.html, root=<pasta>, files=<todos os arquivos da lista>)."""
import pathlib, re, shutil, sys, json
src=pathlib.Path(sys.argv[1]); dst=pathlib.Path(sys.argv[2])
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('_headers','*.srt'))
def rel(html, depth):
    pre='../'*depth
    def fix(m):
        attr,path=m.group(1),m.group(2)
        if path.startswith('//') or path=='/': return f'{attr}="{pre}index.html"' if path=='/' else m.group(0)
        p=path[1:]
        if p.startswith('#'): return f'{attr}="{pre}index.html{p}"'
        if '#' in p and p.split('#')[0].endswith('/'): a,b=p.split('#',1); return f'{attr}="{pre}{a}index.html#{b}"'
        if p.endswith('/'): p+='index.html'
        if p=='' : p='index.html'
        return f'{attr}="{pre}{p}"'
    html=re.sub(r'(href|src|poster)="(/[^"]*)"', fix, html)
    # srcset: lista de "caminho largura", cada caminho absoluto vira relativo (o host da prévia não serve /x)
    def fixset(m):
        partes=[]
        for item in m.group(1).split(','):
            item=item.strip()
            if not item: continue
            cam,_,resto=item.partition(' ')
            if cam.startswith('/'): cam=pre+cam[1:]
            partes.append((cam+' '+resto).strip())
        return 'srcset="'+', '.join(partes)+'"'
    html=re.sub(r'srcset="([^"]*)"', fixset, html)
    html=html.replace('href="/#','href="'+pre+'index.html#')
    html=re.sub(r"url\(/(assets/[^)]+)\)", lambda m: "url("+pre+m.group(1)+")", html)
    return html
for f in dst.rglob('*.html'):
    depth=len(f.relative_to(dst).parts)-1
    f.write_text(rel(f.read_text(encoding='utf-8'), depth), encoding='utf-8')
# page.html = index sem html/head/body
idx=(dst/'index.html').read_text(encoding='utf-8')
m=re.search(r'<title>.*?</title>', idx, re.S); head=re.search(r'<head>(.*?)</head>', idx, re.S).group(1)
keep=[l for l in head.splitlines() if re.search(r'<title>|<link rel="(preload|stylesheet)|<script>', l)]
body=re.search(r'<body[^>]*>(.*)</body>', idx, re.S).group(1)
estilos=re.findall(r'<style>.*?</style>', head, re.S)
(dst/'page.html').write_text('\n'.join(keep)+'\n'+'\n'.join(estilos)+'\n<style>body{margin:0}</style>\n'+body, encoding='utf-8')
files={str(f.relative_to(dst)):str(f) for f in dst.rglob('*') if f.is_file() and f.name!='page.html' and f.name!='_headers'}
json.dump(files, open(dst.parent/'preview-files.json','w'), indent=0)
print(len(files),'arquivos')
