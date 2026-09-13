#!/usr/bin/env python3
"""Gera os PDFs do kit (manual, biblioteca de prompts, checklist) a partir do Markdown, com a marca."""
import markdown, pathlib, subprocess, re, json, base64
ROOT=pathlib.Path(__file__).resolve().parent
FONTS=ROOT.parents[1]/'site'/'public'/'assets'/'fonts'
LOGO=(ROOT.parents[1]/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
def b64(p): return base64.b64encode(p.read_bytes()).decode()
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
@page{{size:A4;margin:18mm 16mm 20mm 16mm}}
body{{font-family:Figtree,system-ui,sans-serif;font-size:11pt;line-height:1.5;color:#1F1235;margin:0}}
h1{{font-family:'Bricolage Grotesque';font-weight:800;font-size:26pt;color:#3B1F5E;letter-spacing:-.02em;line-height:1.05;margin:0 0 6pt}}
h1+p{{color:#7A5AA8;font-family:'IBM Plex Mono';font-size:9pt;margin:0 0 18pt}}
h2{{font-family:'Bricolage Grotesque';font-weight:800;font-size:16pt;color:#3B1F5E;margin:22pt 0 8pt;page-break-after:avoid;border-top:1px solid #DCD2EC;padding-top:12pt}}
h3{{font-family:'Bricolage Grotesque';font-weight:600;font-size:12.5pt;color:#3B1F5E;margin:16pt 0 4pt;page-break-after:avoid}}
p{{margin:0 0 8pt}} li{{margin-bottom:3pt}}
table{{border-collapse:collapse;width:100%;font-size:9.5pt;margin:6pt 0 12pt;page-break-inside:avoid}}
th{{background:#3B1F5E;color:#fff;text-align:left;padding:5pt 7pt;font-family:'IBM Plex Mono';font-size:8pt;letter-spacing:.05em;text-transform:uppercase}}
td{{padding:5pt 7pt;border-bottom:1px solid #DCD2EC;vertical-align:top}}
pre{{background:#F3EEFB;border-left:4px solid #FFC83D;padding:9pt 11pt;font-family:'IBM Plex Mono';font-size:9pt;white-space:pre-wrap;word-wrap:break-word;border-radius:0 6px 6px 0;page-break-inside:avoid;line-height:1.45}}
code{{font-family:'IBM Plex Mono';font-size:9.5pt}}
img{{max-width:100%;border:1px solid #DCD2EC;border-radius:6px;margin:4pt 0 10pt;page-break-inside:avoid}}
strong{{color:#3B1F5E}}
blockquote{{margin:0;padding:6pt 12pt;background:#FFF4CC;border-radius:6px}}
.capa{{height:250mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always}}
.capa .logo{{width:70mm}} .capa .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:34pt;color:#3B1F5E;line-height:1.02;letter-spacing:-.02em}}
.capa .t em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}}
.capa .s{{font-size:13pt;color:#5A4A78;margin-top:14pt;max-width:120mm}} .capa .m{{font-family:'IBM Plex Mono';font-size:9pt;color:#7A5AA8}}
input[type=checkbox]{{width:11pt;height:11pt;vertical-align:-1pt;margin-right:6pt}}
ul.check{{list-style:none;padding-left:0}} ul.check li{{margin-bottom:6pt}}
"""
def build(md_path, pdf_name, titulo, sub, capa=True):
    md=pathlib.Path(md_path).read_text()
    md=re.sub(r'^# .*\n\n?.*?\n\n','',md,count=1,flags=re.M) if capa else md
    md=md.replace('- [ ] ','- <input type="checkbox"> ')
    html=markdown.markdown(md,extensions=['tables','fenced_code'])
    html=html.replace('<ul>\n<li><input','<ul class="check">\n<li><input')
    html=re.sub(r'<img alt="([^"]*)" src="docs/([^"]+)"',lambda m:f'<img alt="{m.group(1)}" src="data:image/png;base64,{b64(ROOT/"docs"/m.group(2))}"',html)
    logo=LOGO.replace("<svg",'<svg class="logo"',1)
    capa_html=f'<div class="capa"><div>{logo}</div><div><div class="t">{titulo}</div><div class="s">{sub}</div></div><div class="m">Kit IA no Trabalho · Essencial · versão 1.0 · setembro de 2026 · seusociogestor.com.br</div></div>' if capa else ''
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{capa_html}{html}</body></html>'
    out=ROOT/'docs'/(pdf_name+'.html'); out.write_text(doc)
    return out
jobs=[build('05-mini-manual.md','05-mini-manual','Mini-manual: <em>comece em 15 minutos</em>','Como abrir, preencher e usar as três planilhas, a biblioteca de prompts e os bônus. Leia uma vez; depois é só rotina.'),
      build('04-biblioteca-de-prompts.md','04-biblioteca-de-prompts','40 prompts para <em>trabalhar com IA</em>','Organizar, analisar, escrever, apresentar, revisar e aprender. Copie, troque os colchetes, cole os seus dados.'),
      build('07-checklist-antes-de-enviar.md','07-checklist-antes-de-enviar','Checklist','',capa=False)]
print('\n'.join(str(j) for j in jobs))
