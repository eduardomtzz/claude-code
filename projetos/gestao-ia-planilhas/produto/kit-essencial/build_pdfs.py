#!/usr/bin/env python3
"""Gera os PDFs do Kit Essencial (mini-manual, biblioteca de prompts, checklist) a partir do Markdown, com a marca,
e a biblioteca de prompts em .txt.

Uso:
  python3 build_pdfs.py                        # só escreve os HTML em docs/
  python3 build_pdfs.py --pdf entrega          # imprime os PDF (Chromium via Playwright) e o 04 .txt na pasta indicada
  python3 build_pdfs.py --pdf /tmp/x           # para conferir a diagramação sem tocar em entrega/
  python3 build_pdfs.py --completo             # só a biblioteca de prompts, como "Biblioteca A" do Kit Completo:
                                               #   11-biblioteca-de-prompts-a.pdf e .txt em ../kit-completo/entrega/
  python3 build_pdfs.py --completo --pdf /tmp/x   # idem, em outra pasta (para validar antes de gravar em entrega/)
As capturas do manual vêm de docs/tela-<planilha>-<aba>.png; regere as capturas antes dos PDFs.
O .txt do Essencial (04) é texto puro, só os prompts, para copiar no celular; o do Completo (11-a) é o Markdown
inteiro, no mesmo formato do 11-biblioteca-de-prompts-b.txt.
"""
import markdown, pathlib, subprocess, re, sys, os, base64
ROOT=pathlib.Path(__file__).resolve().parent
COMPLETO=ROOT.parent/'kit-completo'
FONTS=ROOT.parents[1]/'site'/'public'/'assets'/'fonts'
LOGO=(ROOT.parents[1]/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
KIT='Completo' if '--completo' in sys.argv else 'Essencial'
RODAPE=f'Seu Sócio Gestor · Kit IA no Trabalho · {KIT} · página <span class="pageNumber"></span> de <span class="totalPages"></span>'
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
/* Manual: cada planilha (título, captura, passos e dicas) fica junta na mesma página;
   capturas com no máximo ~40 % da altura útil da página (259 mm), centralizadas. */
.planilha{{page-break-inside:avoid;break-inside:avoid}}
.planilha p{{margin:0 0 6pt}}
.fig{{text-align:center;margin:4pt 0 8pt}} .fig img{{max-height:100mm;width:auto;margin:0}}
.figs{{display:flex;gap:4mm;justify-content:center;align-items:flex-start;margin:4pt 0 8pt}}
.figs img{{max-width:calc(50% - 2mm);max-height:90mm;width:auto;margin:0}}
"""
def secoes_planilha(html):
    """Em cada '## N. Planilha N em 15 minutos' do manual, envolve título + captura(s) + passos numerados em
    <div class="planilha">, para ficarem na mesma página; as dicas depois dos passos podem fluir."""
    partes=re.split(r'(?=<h2)',html); out=[]
    for p in partes:
        if re.match(r'<h2[^>]*>\d+\. Planilha ',p) and '</ol>' in p:
            bloco,resto=p.split('</ol>',1); out.append(f'<div class="planilha">{bloco}</ol></div>{resto}')
        else: out.append(p)
    return ''.join(out)
def figuras(html):
    """<p><img></p> vira <div class="fig">; duas capturas seguidas viram <div class="figs"> lado a lado."""
    html=re.sub(r'<p>(<img [^>]*>)</p>\s*<p>(<img [^>]*>)</p>',r'<div class="figs">\1\2</div>',html)
    html=re.sub(r'<p>(<img [^>]*>)</p>',r'<div class="fig">\1</div>',html)
    return html
def build(md_path, pdf_name, titulo, sub, capa=True, classe=''):
    md=pathlib.Path(md_path).read_text()
    md=re.sub(r'^# .*\n\n?.*?\n\n','',md,count=1,flags=re.M) if capa else md
    md=md.replace('- [ ] ','- <input type="checkbox"> ')
    html=markdown.markdown(md,extensions=['tables','fenced_code'])
    html=html.replace('<ul>\n<li><input','<ul class="check">\n<li><input')
    html=re.sub(r'<img alt="([^"]*)" src="docs/([^"]+)"',lambda m:f'<img alt="{m.group(1)}" src="data:image/png;base64,{b64(ROOT/"docs"/m.group(2))}"',html)
    if classe=='manual': html=secoes_planilha(figuras(html))
    logo=LOGO.replace("<svg",'<svg class="logo"',1)
    # A capa quebra o título onde o <br> manda (nunca deixa "IA" ou "15 minutos" sozinhos com o sublinhado quebrado).
    capa_html=f'<div class="capa"><div>{logo}</div><div><div class="t">{titulo}</div><div class="s">{sub}</div></div><div class="m">Kit IA no Trabalho · {KIT} · versão 1.0 · setembro de 2026 · seusociogestor.com.br</div></div>' if capa else ''
    meta=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',titulo).replace('&nbsp;',' ')).strip()+f' · Kit IA no Trabalho · {KIT} · Seu Sócio Gestor'
    doc=f'<!doctype html><html lang="pt-BR" class="{classe}"><head><meta charset="utf-8"><title>{meta}</title><style>{CSS}</style></head><body class="{classe}">{capa_html}{html}</body></html>'
    out=ROOT/'docs'/(pdf_name+'.html'); out.write_text(doc)
    return out
def txt_prompts(md, destino):
    """Versão em texto puro da biblioteca (Essencial): título em maiúsculas + prompt, sem exemplos nem comentários."""
    linhas=['BIBLIOTECA DE PROMPTS · KIT IA NO TRABALHO · ESSENCIAL · SEU SÓCIO GESTOR',
            'Copie o prompt, troque o que está entre colchetes, cole os seus dados no fim.','']
    for secao in re.split(r'^### ',md,flags=re.M)[1:]:   # um bloco por prompt (### Grupo NN · Título)
        titulo=secao.split('\n',1)[0]; prompt=re.search(r'```\n([\s\S]*?)```',secao).group(1)
        linhas+=['='*70,titulo.strip().upper(),'-'*70,prompt.rstrip('\n'),'']
    destino.write_text('\n'.join(linhas))
def txt_markdown(md, destino):
    """Versão .txt da Biblioteca A no Kit Completo: o Markdown inteiro, como o 11-biblioteca-de-prompts-b.txt."""
    md=md.replace('# Biblioteca de prompts · Kit IA no Trabalho · Essencial','# Biblioteca de prompts A · 40 prompts do dia a dia · Kit IA no Trabalho · Completo',1)
    destino.write_text(md)
def imprimir(htmls, destino):
    """Imprime os HTML em PDF A4 com o Chromium do Playwright (rodapé com kit e número de página)."""
    destino=pathlib.Path(destino); destino.mkdir(parents=True,exist_ok=True)
    js=destino/'_pdf.js'
    js.write_text("""const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox','--disable-gpu']});
const dest=process.argv[2];
for(const f of process.argv.slice(3)){const p=await b.newPage(); await p.goto('file://'+f,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
 const out=dest+'/'+f.replace(/^.*\\//,'').replace(/\\.html$/,'.pdf');
 await p.pdf({path:out,format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<div></div>',footerTemplate:'<div style="font-family:sans-serif;font-size:8px;color:#7A5AA8;width:100%;text-align:center">"""+RODAPE+"""</div>'}); console.log(out); await p.close();}
await b.close();})();""")
    env={**os.environ,'NODE_PATH':os.pathsep.join(p for p in [os.environ.get('NODE_PATH',''),'/opt/node22/lib/node_modules'] if p)}
    subprocess.run(['node',str(js),str(destino)]+[str(h) for h in htmls],check=True,env=env); js.unlink()
    return destino
PROMPTS_MD=ROOT/'04-biblioteca-de-prompts.md'
if KIT=='Completo':
    jobs=[build(PROMPTS_MD,'11-biblioteca-de-prompts-a','Biblioteca A: 40 prompts<br><em>do dia a dia</em>','Organizar, analisar, escrever, apresentar, revisar e aprender. Copie, troque os colchetes, cole os seus dados.')]
    print('\n'.join(str(j) for j in jobs))
    destino=imprimir(jobs, sys.argv[sys.argv.index('--pdf')+1] if '--pdf' in sys.argv else COMPLETO/'entrega')
    txt_markdown(PROMPTS_MD.read_text(), destino/'11-biblioteca-de-prompts-a.txt'); print(destino/'11-biblioteca-de-prompts-a.txt')
else:
    jobs=[build('05-mini-manual.md','05-mini-manual','Mini-manual:<br><em>comece em 15&nbsp;minutos</em>','Como abrir, preencher e usar as três planilhas, a biblioteca de prompts e os bônus. Leia uma vez; depois é só rotina.',classe='manual'),
          build(PROMPTS_MD,'04-biblioteca-de-prompts','40 prompts para<br><em>trabalhar com IA</em>','Organizar, analisar, escrever, apresentar, revisar e aprender. Copie, troque os colchetes, cole os seus dados.'),
          build('07-checklist-antes-de-enviar.md','07-checklist-antes-de-enviar','Checklist','',capa=False)]
    print('\n'.join(str(j) for j in jobs))
    if '--pdf' in sys.argv:
        destino=imprimir(jobs, sys.argv[sys.argv.index('--pdf')+1])
        txt_prompts(PROMPTS_MD.read_text(), destino/'04-biblioteca-de-prompts.txt'); print(destino/'04-biblioteca-de-prompts.txt')
