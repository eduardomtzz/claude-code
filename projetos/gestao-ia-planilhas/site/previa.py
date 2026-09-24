#!/usr/bin/env python3
"""Monta a prévia navegável do site para o visualizador de artefatos do Claude.
Uso: python3 previa.py public <pasta-da-previa>
- converte todo caminho absoluto (/assets/..., /kit/, /#kits, url(/...)) em relativo à página;
- gera page.html (a home só com o corpo e as referências de estilo): o visualizador embrulha a página
  principal num documento próprio, e um <html> completo dentro dele quebra estilo e links;
- apaga da cópia o que nenhuma página usa e lista em preview-files.json os outros arquivos, já no formato
  do parâmetro files (caminhos relativos à pasta; .vtt como text/plain).
Publicar: Artifact(file_path=<pasta>/page.html, root=<pasta>, files=<conteúdo de preview-files.json>)."""
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
# publica só o que as páginas usam (o limite por versão é 64 MB; as aulas completas não entram)
import os
ref=set()
for f in dst.rglob('*.html'):
    h=f.read_text(encoding='utf-8')
    us=re.findall(r'(?:href|src|poster)="([^"#?]+)', h)
    us+=[x.strip().split(' ')[0] for s_ in re.findall(r'srcset="([^"]+)"', h) for x in s_.split(',')]
    for u in us:
        if u and not re.match(r'(https?:|mailto:|tel:|data:|\{\{)', u): ref.add(os.path.normpath(f.parent/u))
fixos=('assets/css/','assets/js/','assets/fonts/')
for f in [f for f in dst.rglob('*') if f.is_file()]:
    r=str(f.relative_to(dst))
    if not (str(f) in ref or r.endswith('.html') or r.startswith(fixos)): f.unlink()
# index.html não pode ser arquivo extra (a página principal já é o índice); .vtt vai como texto
files={}
for f in dst.rglob('*'):
    r=str(f.relative_to(dst))
    if not f.is_file() or r in ('page.html','index.html'): continue
    files[r]={'from':r,'contentType':'text/plain'} if r.endswith('.vtt') else r
json.dump(files, open(dst.parent/'preview-files.json','w'), ensure_ascii=False)
tam=sum(f.stat().st_size for f in dst.rglob('*') if f.is_file())/1e6
print(len(files),'arquivos,',round(tam,1),'MB')
