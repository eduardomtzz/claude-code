#!/usr/bin/env python3
"""Gera os PDFs do kit (manual, biblioteca de prompts, dicionário, checklists) a partir do Markdown, com a marca.

Uso:
  python3 build_pdfs.py                 # só escreve os HTML em docs/
  python3 build_pdfs.py --pdf entrega   # também imprime os PDF (Chromium via Playwright) na pasta indicada
  python3 build_pdfs.py --pdf /tmp/x    # para conferir a diagramação sem tocar em entrega/
As capturas do manual vêm de docs/tela-<planilha>-<aba>.png; regere as capturas antes dos PDFs.
"""
import markdown, pathlib, subprocess, re, sys, os, base64
ROOT=pathlib.Path(__file__).resolve().parent
FONTS=ROOT.parents[1]/'site'/'public'/'assets'/'fonts'
LOGO=(ROOT.parents[1]/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
RODAPE='Seu Sócio Gestor · Kit IA no Trabalho · Completo · página <span class="pageNumber"></span> de <span class="totalPages"></span>'
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
/* Biblioteca: o título e o "Quando usar" ficam na mesma página que o prompt (no manual isso colaria seções sem figura na seguinte). */
body:not(.manual) h3+p{{page-break-after:avoid;break-after:avoid}}
/* Manual: cada planilha (título, texto, captura e "detalhe que importa") fica junta na mesma página;
   capturas com no máximo 62 mm de altura (duas seções cabem em uma página de 259 mm úteis), centralizadas. */
.planilha{{page-break-inside:avoid;break-inside:avoid;margin-bottom:6pt}}
.planilha p{{margin:0 0 6pt}}
.fig{{text-align:center;margin:4pt 0 6pt}} .fig img{{max-height:62mm;width:auto;margin:0}}
.figs{{display:flex;gap:4mm;justify-content:center;align-items:flex-start;margin:4pt 0 6pt}}
.figs img{{max-width:calc(46% - 2mm);max-height:55mm;width:auto;margin:0}}
/* Tabelas do manual (o que recebeu, ordem, erros comuns) podem continuar na página seguinte com o cabeçalho repetido. */
.manual table{{page-break-inside:auto}} .manual tr{{page-break-inside:avoid}} .manual thead{{display:table-header-group}}
/* Dicionário: larguras fixas; a coluna "O que faz" é a mais larga e o exemplo quebra onde precisar.
   As tabelas podem continuar na página seguinte (o cabeçalho repete), sem deixar páginas meio vazias. */
.dic table{{table-layout:fixed;font-size:9pt;page-break-inside:auto}} .dic tr{{page-break-inside:avoid}} .dic thead{{display:table-header-group}}
.dic td{{padding:4pt 6pt}}
.dic td:nth-child(1),.dic th:nth-child(1){{padding-left:4pt;padding-right:2pt}}
.dic td:nth-child(2),.dic td:nth-child(3){{font-size:8.5pt;padding-left:4pt;padding-right:3pt;overflow-wrap:anywhere}}
.dic td:nth-child(5) code{{font-size:8pt;overflow-wrap:anywhere;word-break:break-all}}
.dic h2{{page-break-after:avoid}}
/* Checklists: uma página, duas colunas (planilha e relatório à esquerda; apresentação e envio à direita). */
.check2 body{{font-size:10.5pt}}
.cols{{column-count:2;column-gap:10mm;column-fill:auto}}
.cols h2{{margin:0 0 6pt;border:0;padding-top:0;font-size:13.5pt;break-after:avoid}}
.cols h2+ul{{break-before:avoid}} .cols ul.check{{margin:0 0 14pt}} .cols ul.check li{{margin-bottom:5pt;break-inside:avoid;line-height:1.4}}
.cols .quebra{{break-before:column}}
"""
DIC_COLS='<colgroup><col style="width:5%"><col style="width:19%"><col style="width:15%"><col style="width:33%"><col style="width:28%"></colgroup>'
def secoes_planilha(html):
    """Envolve cada '### 3.x' do manual (até o próximo h2/h3) em <div class="planilha">, para não quebrar página no meio."""
    partes=re.split(r'(?=<h[23])',html); out=[]
    for p in partes:
        if re.match(r'<h3[^>]*>3\.\d+ ',p): out.append(f'<div class="planilha">{p}</div>')
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
    if classe=='dic': html=html.replace('<table>','<table>'+DIC_COLS)
    if classe=='check2':
        # título e subtítulo fora das colunas; os quatro checklists em duas colunas, quebra antes de "Apresentação"
        cabeca,resto=html.split('<h2>',1); resto='<h2>'+resto
        resto=resto.replace('<h2>Apresentação</h2>','<h2 class="quebra">Apresentação</h2>')
        rodape=''
        m=re.search(r'<p>seusociogestor\.com\.br.*?</p>\s*$',resto,flags=re.S)
        if m: rodape=m.group(0); resto=resto[:m.start()]
        html=f'{cabeca}<div class="cols">{resto}{rodape}</div>'
    logo=LOGO.replace("<svg",'<svg class="logo"',1)
    capa_html=f'<div class="capa"><div>{logo}</div><div><div class="t">{titulo}</div><div class="s">{sub}</div></div><div class="m">Kit IA no Trabalho · Completo · versão 1.0 · setembro de 2026 · seusociogestor.com.br</div></div>' if capa else ''
    doc=f'<!doctype html><html lang="pt-BR" class="{classe}"><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{classe}">{capa_html}{html}</body></html>'
    out=ROOT/'docs'/(pdf_name+'.html'); out.write_text(doc)
    return out
def imprimir(htmls, destino):
    """Imprime os HTML em PDF A4 com o Chromium do Playwright (mesmo rodapé de sempre)."""
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
jobs=[build('14-manual-do-metodo.md','14-manual-do-metodo','Manual do método: <em>estruturar, preencher, perguntar, entregar</em>','As 10 planilhas, os 80 prompts, as 8 aulas e a rotina da semana, do mês e do trimestre. Leia uma vez; depois é só rotina.',classe='manual'),
      build('11-biblioteca-de-prompts-b.md','11-biblioteca-de-prompts-b','Biblioteca B: 40 prompts para <em>estruturar e produzir</em>','Desenhar planilhas, escrever fórmulas, limpar dados, transformar números em relatório e apresentação. Copie, troque os colchetes, cole os seus dados.'),
      build('12-dicionario-de-formulas.md','12-dicionario-de-formulas','60 fórmulas <em>em uma frase</em>','Português e inglês, o que faz e um exemplo pronto. Para ter ao lado enquanto monta a sua planilha.',classe='dic'),
      build('13-checklists-de-revisao.md','13-checklists-de-revisao','Checklists','',capa=False,classe='check2')]
print('\n'.join(str(j) for j in jobs))
if '--pdf' in sys.argv: imprimir(jobs, sys.argv[sys.argv.index('--pdf')+1])
