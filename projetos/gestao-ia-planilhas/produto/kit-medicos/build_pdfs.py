#!/usr/bin/env python3
"""Gera os PDFs do Kit de Gestão para Médicos (manual, prompts, bônus, checklists) a partir do Markdown, com a marca,
mais os .txt limpos (21 e 22) e os recortes das capturas do manual.

Uso:
  python3 build_pdfs.py                 # recortes + HTML em docs/
  python3 build_pdfs.py --pdf entrega   # também imprime os PDF (Chromium via Playwright) e grava os txt na pasta indicada
  python3 build_pdfs.py --pdf /tmp/x    # para conferir a diagramação sem tocar em entrega/
As capturas do manual vêm de docs/tela-NN.png (geradas por ../telas.py); daqui saem os recortes docs/recorte-NN.png
usados no manual: nas planilhas 01 a 05, cartões e primeira tabela; nas 06 a 20, só a faixa de cartões do alto do
Painel (ou as primeiras colunas da tabela, quando não há cartões), para o texto sair legível na largura da página.
"""
import markdown, pathlib, subprocess, re, sys, os, base64
ROOT=pathlib.Path(__file__).resolve().parent
FONTS=ROOT.parents[1]/'site'/'public'/'assets'/'fonts'
LOGO=(ROOT.parents[1]/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
RODAPE='Seu Sócio Gestor · Kit de Gestão para Médicos · página <span class="pageNumber"></span> de <span class="totalPages"></span>'
def b64(p): return base64.b64encode(p.read_bytes()).decode()
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
@page{{size:A4;margin:18mm 16mm 20mm 16mm}}
body{{font-family:Figtree,system-ui,sans-serif;font-size:11pt;line-height:1.5;color:#1F1235;margin:0;orphans:3;widows:3}}
h1{{font-family:'Bricolage Grotesque';font-weight:800;font-size:26pt;color:#3B1F5E;letter-spacing:-.02em;line-height:1.05;margin:0 0 6pt}}
h1+p{{color:#7A5AA8;font-family:'IBM Plex Mono';font-size:9pt;margin:0 0 18pt}}
h2{{font-family:'Bricolage Grotesque';font-weight:800;font-size:16pt;color:#3B1F5E;margin:22pt 0 8pt;page-break-after:avoid;break-after:avoid;border-top:1px solid #DCD2EC;padding-top:12pt}}
h3{{font-family:'Bricolage Grotesque';font-weight:600;font-size:12.5pt;color:#3B1F5E;margin:16pt 0 4pt;page-break-after:avoid;break-after:avoid}}
p{{margin:0 0 8pt}} li{{margin-bottom:3pt}}
/* Tabelas podem continuar na página seguinte com o cabeçalho repetido (sem deixar meia página vazia antes de uma tabela longa). */
table{{border-collapse:collapse;width:100%;font-size:9.5pt;margin:6pt 0 12pt;page-break-inside:auto}}
tr{{page-break-inside:avoid;break-inside:avoid}} thead{{display:table-header-group}}
th{{background:#3B1F5E;color:#fff;text-align:left;padding:5pt 7pt;font-family:'IBM Plex Mono';font-size:8pt;letter-spacing:.05em;text-transform:uppercase}}
td{{padding:5pt 7pt;border-bottom:1px solid #DCD2EC;vertical-align:top}}
/* Blocos de prompt e de mensagem NUNCA quebram de página: quem seleciona o prompt no PDF não pode levar o rodapé junto.
   Se um bloco for maior que uma página inteira, o navegador quebra assim mesmo (é o único caso), com 6 linhas mínimas de cada lado. */
pre,.pre{{background:#F3EEFB;border-left:4px solid #FFC83D;padding:9pt 11pt;font-family:'IBM Plex Mono';font-size:9pt;white-space:pre-wrap;word-wrap:break-word;border-radius:0 6px 6px 0;page-break-inside:avoid;break-inside:avoid;orphans:6;widows:6;line-height:1.45}}
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
/* Biblioteca (21): título + "Quando usar" + "Cole" ficam juntos e colados ao início do prompt.
   Texto do prompt um pouco mais compacto: como o bloco não pode quebrar, blocos menores deixam menos página em branco. */
.cab{{page-break-inside:avoid;break-inside:avoid;page-break-after:avoid;break-after:avoid}}
.prompts .pre{{font-size:8.6pt;line-height:1.36;padding:8pt 10pt}}
.prompts h3{{margin:13pt 0 3pt}} .prompts p{{margin:0 0 6.5pt}} .prompts h2{{margin:18pt 0 6pt;padding-top:10pt}}
/* Mensagens (22): título + "Quando" colados ao início do texto; o texto da mensagem também não quebra de página. */
.msgs .pre{{orphans:6;widows:6;font-size:8.8pt;line-height:1.4}} .msgs table{{page-break-inside:avoid;break-inside:avoid}}
.msgs h3{{margin:13pt 0 3pt}} .msgs p{{margin:0 0 6.5pt}}
/* Guia LGPD e roteiro do contador: ajustes finos para a última linha não abrir página nova. */
.lgpd{{font-size:10.6pt;line-height:1.44}} .lgpd .pre{{font-size:8.5pt;line-height:1.36;page-break-inside:auto;break-inside:auto;orphans:4;widows:4}} .lgpd h2{{margin-top:15pt;padding-top:9pt}} .lgpd p{{margin:0 0 6.5pt}} .lgpd li{{margin-bottom:1.5pt}}
.lgpd h3{{margin:12pt 0 3pt}} .lgpd table{{font-size:9pt;margin:5pt 0 9pt}} .lgpd td{{padding:4pt 6pt}}
.contador{{font-size:10.2pt;line-height:1.42}} .contador h2{{margin:13pt 0 4pt;padding-top:7pt;font-size:15pt}} .contador h3{{margin:10pt 0 3pt}}
.contador table{{font-size:8.6pt;margin:4pt 0 8pt}} .contador td{{padding:3.5pt 5pt}} .contador th{{padding:4pt 5pt}} .contador p{{margin:0 0 6pt}} .contador li{{margin-bottom:1.5pt}}
/* Manual: o título de cada planilha fica com o parágrafo seguinte e o recorte com a legenda; o resto pode quebrar
   de página (uma planilha por página deixava metade da página vazia). Recortes em largura total da mancha (178 mm),
   sem limite de altura: é o que mantém a captura legível. */
.planilha{{margin-bottom:6pt}}
.planilha p{{margin:0 0 4pt;line-height:1.36}} .planilha h3{{margin-top:8pt;page-break-after:avoid;break-after:avoid}}
.planilha h3+p{{page-break-before:avoid;break-before:avoid}}
figure.fig{{margin:5pt 0 7pt;text-align:center;page-break-inside:avoid;break-inside:avoid}}
figure.fig img{{max-height:none;width:100%;max-width:100%;margin:0}}
figure.fig figcaption{{font-family:'IBM Plex Mono';font-size:8pt;color:#7A5AA8;margin:3pt 0 0;letter-spacing:.03em}}
/* Checklists (25): uma página, duas colunas explícitas, fonte legível. */
body.check2{{font-size:10pt;line-height:1.32}}
.check2 h1+p{{font-family:Figtree,system-ui,sans-serif;font-size:10.5pt;color:#5A4A78;margin:0 0 10pt}} .check2 h1{{font-size:22pt}}
.cols{{display:flex;gap:9mm;align-items:flex-start}} .cols>div{{flex:1 1 0;min-width:0}}
.cols h2{{margin:0 0 6pt;border:0;padding-top:0;font-size:13.5pt}} .cols h2.cont{{font-size:11.5pt;color:#7A5AA8}}
.cols ul.check{{margin:0 0 7pt}} .cols ul.check li{{margin-bottom:1.5pt;break-inside:avoid}}
.cols .rodape{{font-family:'IBM Plex Mono';font-size:8.5pt;color:#7A5AA8;margin-top:6pt}}
"""
TITULOS={'21-biblioteca-de-prompts-da-clinica':'Biblioteca de prompts da clínica',
 '22-mensagens-de-confirmacao-e-cobranca':'Mensagens de confirmação e cobrança',
 '23-guia-lgpd-clinica-pequena':'Guia LGPD para a clínica pequena',
 '24-roteiro-reuniao-com-o-contador':'Roteiro da reunião com o contador',
 '25-checklists':'Checklists da clínica',
 '26-manual-de-implantacao':'Manual de implantação'}
# ---------- recortes das capturas (x0,y0,x1,y1 em px da tela-NN.png; o fundo branco do pé é aparado depois) ----------
RECORTES={'01':(0,0,1950,560),'02':(0,0,1950,660),'03':(0,0,1950,640),'04':(0,0,1950,700),'05':(0,0,1850,665),
 # 4.6 a 4.20: só a faixa de cartões do alto do Painel (ou as primeiras colunas da tabela, quando não há cartões).
 # Impressos em largura total (190 mm), o texto dos cartões fica em 6 pt ou mais; a tabela inteira, na mesma largura,
 # cairia para 3-4 pt — por isso ela não entra no recorte e a legenda diz o que a captura mostra.
 '06':(0,105,1179,500),'07':(0,0,1950,227),'08':(0,108,1950,268),'09':(0,0,1950,230),'10':(0,0,1950,227),
 '11':(0,0,1950,227),'12':(0,0,1950,238),'13':(0,0,2100,227),'14':(0,0,1950,230),'15':(0,0,1950,227),
 '16':(0,0,1950,227),'17':(0,0,2100,468),'18':(0,0,2100,211),'19':(0,0,1950,210),
 '20':(0,318,1950,712),'20-painel':(0,95,1131,600)}
def recortes():
    from PIL import Image
    import numpy as np
    for n,(x0,y0,x1,y1) in RECORTES.items():
        src=ROOT/'docs'/f'tela-{n}.png'
        if not src.exists(): print('falta',src); continue
        im=Image.open(src).convert('RGB'); x1=min(x1,im.width); y1=min(y1,im.height)
        a=np.array(im.crop((x0,y0,x1,y1))).astype(int)
        rows=np.where((a.sum(2)<740).sum(1)>0)[0]
        cols=np.where((a.sum(2)<740).sum(0)>0)[0]
        by=int(rows.max())+14 if len(rows) else y1-y0; bx=int(cols.max())+14 if len(cols) else x1-x0
        out=im.crop((x0,y0,min(x1,x0+bx),min(y1,y0+by)))
        # moldura branca de 10 px para o recorte não colar na borda
        fundo=Image.new('RGB',(out.width+20,out.height+20),'white'); fundo.paste(out,(10,10))
        fundo.save(ROOT/'docs'/f'recorte-{n}.png')
def secoes_planilha(html):
    """Envolve cada '### 4.x' do manual (até o próximo h2/h3) em <div class="planilha">, para não quebrar página no meio."""
    partes=re.split(r'(?=<h[23])',html); out=[]
    for p in partes:
        if re.match(r'<h3[^>]*>\d+\.\d+ ',p): out.append(f'<div class="planilha">{p}</div>')
        else: out.append(p)
    return ''.join(out)
def figuras(html):
    """<p><img alt="legenda"></p> vira <figure class="fig"><img><figcaption>legenda</figcaption></figure>."""
    return re.sub(r'<p>(<img alt="([^"]*)"[^>]*>)</p>',r'<figure class="fig">\1<figcaption>\2</figcaption></figure>',html)
def cabecas_prompts(html):
    """Biblioteca: h3 + <p>Quando usar + <p>Cole viram <div class="cab"> (juntos e colados ao <pre>)."""
    return re.sub(r'(<h3>[^<]*</h3>\n<p><strong>Quando usar:</strong>.*?</p>)\n(?=<div class="pre">)',r'<div class="cab">\1</div>\n',html,flags=re.S)
def cabecas_mensagens(html):
    """Mensagens: h3 + <p>Quando (e Atenção) viram <div class="cab"> colado ao <pre>."""
    return re.sub(r'(<h3>[^<]*</h3>\n<p><strong>Quando:</strong>.*?</p>)\n(?=<div class="pre">)',r'<div class="cab">\1</div>\n',html,flags=re.S)
def checklists_2cols(html):
    """Checklists: título e subtítulo fora das colunas; três listas em duas colunas explícitas;
    a lista que continua na 2ª coluna repete o título com '(continuação)'."""
    cabeca,resto=html.split('<h2>',1); resto='<h2>'+resto
    m=re.search(r'<p>seusociogestor\.com\.br.*?</p>\s*$',resto,flags=re.S); rod=''
    if m: rod=re.sub(r'</?p>','',m.group(0)).strip(); resto=resto[:m.start()]
    blocos=re.findall(r'<h2>(.*?)</h2>\s*<ul class="check">(.*?)</ul>',resto,flags=re.S)
    assert len(blocos)==3, len(blocos)
    def ul(items): return '<ul class="check">'+''.join(items)+'</ul>'
    itens=[re.findall(r'<li>.*?</li>',b[1],flags=re.S) for b in blocos]
    corte=7
    col1=f'<h2>{blocos[0][0]}</h2>{ul(itens[0])}<h2>{blocos[1][0]}</h2>{ul(itens[1][:corte])}'
    col2=f'<h2 class="cont">{blocos[1][0]} (continuação)</h2>{ul(itens[1][corte:])}<h2>{blocos[2][0]}</h2>{ul(itens[2])}<div class="rodape">{rod}</div>'
    return f'{cabeca}<div class="cols"><div>{col1}</div><div>{col2}</div></div>'
def build(md_path, pdf_name, titulo, sub, capa=True, classe=''):
    md=pathlib.Path(md_path).read_text()
    md=re.sub(r'^# .*\n\n?.*?\n\n','',md,count=1,flags=re.M) if capa else md
    md=md.replace('- [ ] ','- <input type="checkbox"> ')
    html=markdown.markdown(md,extensions=['tables','fenced_code'])
    html=html.replace('<ul>\n<li><input','<ul class="check">\n<li><input')
    html=re.sub(r'<pre><code>(.*?)</code></pre>',lambda m:'<div class="pre">'+m.group(1)+'</div>',html,flags=re.S)
    html=re.sub(r'<img alt="([^"]*)" src="docs/([^"]+)"',lambda m:f'<img alt="{m.group(1)}" src="data:image/png;base64,{b64(ROOT/"docs"/m.group(2))}"',html)
    if classe=='manual': html=secoes_planilha(figuras(html))
    if classe=='prompts': html=cabecas_prompts(html)
    if classe=='msgs': html=cabecas_mensagens(html)
    if classe=='check2': html=checklists_2cols(html)
    logo=LOGO.replace("<svg",'<svg class="logo"',1)
    capa_html=f'<div class="capa"><div>{logo}</div><div><div class="t">{titulo}</div><div class="s">{sub}</div></div><div class="m">Kit de Gestão para Médicos · versão 1.0 · setembro de 2026 · seusociogestor.com.br</div></div>' if capa else ''
    title=f'{TITULOS[pdf_name]} · Kit de Gestão para Médicos'
    extra='@page{size:A4;margin:14mm 14mm 16mm 14mm}' if classe=='check2' else ''
    doc=f'<!doctype html><html lang="pt-BR" class="{classe}"><head><meta charset="utf-8"><title>{title}</title><style>{CSS}{extra}</style></head><body class="{classe}">{capa_html}{html}</body></html>'
    out=ROOT/'docs'/(pdf_name+'.html'); out.write_text(doc)
    return out
# ---------- txt limpo (sem sintaxe Markdown), para copiar no celular ----------
def txt_limpo(md, rotulo='prompt'):
    out=[]; fence=False; par=[]
    def flush():
        if par: out.append(' '.join(s.strip() for s in par)); par.clear()
    def limpa(s):
        s=s.replace('**','').replace('`','')
        s=re.sub(r'!\[[^\]]*\]\([^)]*\)','',s); s=re.sub(r'\[([^\]]*)\]\((?:http|docs)[^)]*\)',r'\1',s)
        return s
    for line in md.splitlines():
        if line.startswith('```'):
            flush(); fence=not fence
            out.append(f'---- {rotulo}: copie daqui ----' if fence else f'---- fim ----'); continue
        if fence: out.append(line); continue
        s=line.rstrip()
        if not s.strip(): flush(); out.append(''); continue
        if s.startswith('#'):
            flush(); nivel=len(s)-len(s.lstrip('#')); tit=limpa(s.lstrip('#').strip())
            if nivel==1: out+= [tit.upper(), '='*min(len(tit),78)]
            elif nivel==2: out+= ['', '='*40, tit.upper(), '='*40]
            else: out+= ['', tit, '-'*min(len(tit),78)]
            continue
        if re.match(r'^\s*-{3,}\s*$',s): flush(); continue
        if s.startswith('|'):
            flush()
            if re.match(r'^\|\s*-',s): continue
            cels=[limpa(c).strip() for c in s.strip().strip('|').split('|')]
            out.append(' · '.join(c for c in cels if c!='') ); continue
        if re.match(r'^\s*(-|\d+\.)\s',s): flush(); par.append(limpa(s).replace('- [ ] ','[ ] ')); flush(); continue
        if re.match(r'^\s{2,}\S',s) and out and not par and out[-1] and re.match(r'^\s*(-|\d+\.|\[ \])',out[-1]):
            out[-1]=out[-1]+' '+limpa(s).strip(); continue   # continuação de item de lista
        if re.match(r'^\*\*[^*]+:\*\*',s): flush()   # rótulo em negrito (Quando usar:, Cole:, Exemplo:, Confira:) abre linha nova
        par.append(limpa(s))
    flush()
    txt='\n'.join(out); txt=re.sub(r'\n{3,}','\n\n',txt).strip()+'\n'
    for tok in ('**','```'):
        assert tok not in txt, f'sobrou {tok!r} no txt'
    assert not re.search(r'^(#|\|)',txt,flags=re.M), 'sobrou título # ou tabela em pipes no txt'
    return txt
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
if __name__=='__main__':
    recortes()
    jobs=[build('26-manual-de-implantacao.md','26-manual-de-implantacao','Manual de implantação: <em>quatro semanas, cinco núcleos</em>','As 20 planilhas, a ordem para começar, a rotina de segunda e de sexta, e os erros comuns. Leia uma vez; depois é só rotina.',classe='manual'),
      build('21-biblioteca-de-prompts-da-clinica.md','21-biblioteca-de-prompts-da-clinica','41 prompts <em>da clínica</em>','Explicar o mês ao sócio, escrever a cobrança educada, resumir os convênios, preparar a reunião com o contador, revisar a tabela de preços. Nenhum produz conteúdo clínico nem publicidade.',classe='prompts'),
      build('22-mensagens-de-confirmacao-e-cobranca.md','22-mensagens-de-confirmacao-e-cobranca','15 mensagens de <em>confirmação e cobrança</em>','WhatsApp e e-mail, tom educado, campos entre colchetes, na régua da planilha 14. Mensagens de rotina da recepção, não peças de divulgação. Bônus do kit.',classe='msgs'),
      build('23-guia-lgpd-clinica-pequena.md','23-guia-lgpd-clinica-pequena','Guia LGPD para a <em>clínica pequena</em>','Dado de saúde é sensível: o que guardar, onde, por quanto tempo, quem acessa, e o que nunca colar em IA pública. Bônus do kit.',classe='lgpd'),
      build('24-roteiro-reuniao-com-o-contador.md','24-roteiro-reuniao-com-o-contador','Roteiro da reunião mensal <em>com o contador</em>','Pauta de 30 minutos, PJ médica, o que levar do kit, o que perguntar, o que anotar. Bônus do kit.',classe='contador'),
      build('25-checklists.md','25-checklists','Checklists','',capa=False,classe='check2')]
    print('\n'.join(str(j) for j in jobs))
    if '--pdf' in sys.argv:
        dest=pathlib.Path(sys.argv[sys.argv.index('--pdf')+1]); imprimir(jobs, dest)
        # txt limpos (sem Markdown) dos prompts e das mensagens, para copiar no celular
        for nome,rot in (('21-biblioteca-de-prompts-da-clinica','prompt'),('22-mensagens-de-confirmacao-e-cobranca','mensagem')):
            (dest/f'{nome}.txt').write_text(txt_limpo(pathlib.Path(f'{nome}.md').read_text(),rot))
