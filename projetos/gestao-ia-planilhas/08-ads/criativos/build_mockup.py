#!/usr/bin/env python3
"""Retrato do produto: notebook + celular com telas reais, logo certo, paleta da marca. Gera 1080x1920, 1080x1080 e 1600x1000 (site)."""
import pathlib, base64, subprocess, os, sys
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parents[1]; S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
DOCS=PROJ/'produto'/'kit-essencial'/'docs'; FONTS=PROJ/'site'/'public'/'assets'/'fonts'
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text(); LOGOB=(PROJ/'03-marca'/'logo'/'logo-branco.svg').read_text()
SIMB='<svg viewBox="0 0 72 72"><rect x="12" y="46" width="30" height="10" rx="5.5" fill="#B89BE0"/><rect x="21" y="31" width="30" height="10" rx="5.5" fill="#7A5AA8"/><rect x="30" y="16" width="30" height="10" rx="5.5" fill="#7A5AA8"/><circle cx="56" cy="52" r="6" fill="#FFC83D"/></svg>'
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} body{{margin:0;font-family:Figtree,sans-serif;color:#1F1235;background:#FFFAF0;overflow:hidden;position:relative}}
.marca{{position:absolute;opacity:.07;width:1400px;right:-350px;bottom:-250px}}
.logo svg{{height:auto}}
.t{{font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:-.025em;line-height:.98;color:#3B1F5E}} .t em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}}
.sub{{color:#5A4A78;line-height:1.3}}
.pill{{display:inline-flex;align-items:center;justify-content:center;background:#FFC83D;color:#3B1F5E;border-radius:999px;font-family:'Bricolage Grotesque';font-weight:800}}
.nota{{font-family:'IBM Plex Mono';color:#7A5AA8}}
/* dispositivos */
.cena{{position:absolute}}
.lap{{position:absolute;background:#1F1235;border-radius:26px 26px 6px 6px;padding:22px 22px 30px;box-shadow:0 60px 100px -50px rgba(31,18,53,.6)}}
.lap .scr{{background:#fff;border-radius:10px;overflow:hidden;position:relative}} .lap .scr img{{position:absolute;left:0;top:0;width:100%}}
.lap .base{{position:absolute;left:-6%;right:-6%;bottom:-26px;height:26px;background:linear-gradient(#2B1B45,#1F1235);border-radius:0 0 18px 18px}}
.lap .base::after{{content:'';position:absolute;left:44%;right:44%;top:0;height:8px;background:#3B1F5E;border-radius:0 0 8px 8px}}
.fone{{position:absolute;background:#1F1235;border-radius:46px;padding:14px;box-shadow:0 50px 90px -40px rgba(31,18,53,.7)}}
.fone .scr{{background:#fff;border-radius:34px;overflow:hidden;position:relative}} .fone .scr img{{position:absolute;left:0;top:0}}
.fone .notch{{position:absolute;left:50%;top:14px;transform:translateX(-50%);width:36%;height:26px;background:#1F1235;border-radius:0 0 18px 18px;z-index:2}}
.tag{{position:absolute;background:#3B1F5E;color:#fff;font-family:'IBM Plex Mono';font-size:22px;padding:10px 18px;border-radius:999px;z-index:5}}
"""
def zoom_fone(img, fw, fh):
    """Largura da captura no celular: nunca menor que o dobro da tela e grande o bastante para a imagem
    cobrir a altura do aparelho (sem faixa branca embaixo)."""
    from PIL import Image
    w, h = Image.open(img).size
    return int(max(fw * 2.0, fh * w / h))
def dispositivos(x,y,escala,lap='tela-relatorio-painel.png',fone='tela-ganhos-painel.png',tag1='Relatório Mensal Pronto',tag2='Ganhos e Gastos',docs=None):
    docs=docs or DOCS
    lw=int(1100*escala); lh=int(660*escala); fw=int(330*escala); fh=int(680*escala); ft=max(20,int(22*escala))
    return f'''<div class="cena" style="left:{x}px;top:{y}px;width:{lw+int(180*escala)}px;height:{lh+int(200*escala)}px">
      <div class="lap" style="left:0;top:0;width:{lw}px"><div class="scr" style="height:{lh-int(52*escala)}px"><img src="data:image/png;base64,{b64(docs/lap)}"></div><div class="base"></div></div>
      <div class="fone" style="left:{lw-int(150*escala)}px;top:{int(140*escala)}px;width:{fw}px;height:{fh}px"><div class="notch"></div><div class="scr" style="height:100%"><img src="data:image/png;base64,{b64(docs/fone)}" style="width:{zoom_fone(docs/fone,fw,fh)}px;left:{-int(fw*0.02)}px;top:0"></div></div>
      <div class="tag" style="left:{int(40*escala)}px;top:{lh-int(20*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag1}</div>
      <div class="tag" style="right:0;top:{int(140*escala)+fh+int(16*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag2}</div>
    </div>'''
def pagina(w,h,corpo,marca=True):
    m=f'<div class="marca">{SIMB}</div>' if marca else ''; bg='' if marca else 'html,body{background:transparent}'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} html,body{{width:{w}px;height:{h}px}} {bg}</style></head><body>{m}{corpo}</body></html>'
DOCS_C=PROJ/'produto'/'kit-completo'/'docs'; DOCS_A=PROJ/'produto'/'kit-advogados'/'docs'; DOCS_M=PROJ/'produto'/'kit-medicos'/'docs'
PRODUTOS={
 'essencial':dict(titulo='Kit IA no Trabalho<br><em>Essencial</em>',sub='3 planilhas prontas + 40 prompts de IA.<br>Você baixa, preenche e entrega.',pill='Comprar por R$ 37 · uma vez',nota='Pix ou cartão · acesso imediato · 7 dias para desistir',
   q_t='Não comece <em>do zero.</em>',q_sub='3 planilhas prontas e 40 prompts que fazem a IA trabalhar nos seus números.',q_pill='R$ 37 · uma vez',dev={}),
 'completo':dict(titulo='Kit IA no Trabalho<br><em>Completo</em>',sub='10 planilhas, 80 prompts e 8 aulas curtas.<br>Método pronto, do zero ao entregue.',pill='Comprar por R$ 197 · uma vez',nota='Pix ou 12× · acesso imediato · 7 dias para desistir',
   q_t='Método, <em>não braço.</em>',q_sub='10 planilhas, 80 prompts e 8 aulas curtas para entregar planilha, relatório e apresentação sem começar do zero.',q_pill='R$ 197 · uma vez',
   dev=dict(lap='tela-metas-painel.png',fone='tela-projetos-painel.png',tag1='Metas do Trimestre',tag2='Projetos e Prazos',docs=DOCS_C)),
 'advogados':dict(titulo='Kit de Gestão<br><em>para Advogados</em>',sub='20 planilhas em 5 núcleos: prazos, honorários,<br>caixa, carteira e painel do escritório.',pill='Comprar por R$ 497 · uma vez',nota='Pix ou 12× · acesso imediato · 7 dias para desistir',
   q_t='O escritório, <em>quem administra?</em>',q_sub='20 planilhas prontas: prazos com semáforo, custo-hora, caixa com provisão, carteira e painel de sexta.',q_pill='R$ 497 · uma vez',
   dev=dict(lap='tela-17.png',fone='tela-01.png',tag1='Painel do Escritório',tag2='Agenda de Prazos',docs=DOCS_A)),
 'medicos':dict(titulo='Kit de Gestão<br><em>para Médicos</em>',sub='20 planilhas em 5 núcleos: agenda, preço,<br>caixa, convênios e painel da clínica.',pill='Comprar por R$ 697 · uma vez',nota='Pix ou 12× · acesso imediato · 7 dias para desistir',
   q_t='A clínica, <em>quem administra?</em>',q_sub='20 planilhas prontas: agenda que se mede, custo da hora, caixa com provisão e repasse, convênios e painel de sexta.',q_pill='R$ 697 · uma vez',
   dev=dict(lap='tela-17.png',fone='tela-01.png',tag1='Painel da Clínica',tag2='Agenda e Ocupação',docs=DOCS_M)),
}
PRODUTOS={k:v for k,v in PRODUTOS.items() if not v['dev'] or (v['dev']['docs']/v['dev']['lap']).exists()}  # pula produto sem telas ainda
out=ROOT/'trabalho-mockup'; out.mkdir(exist_ok=True); alvos=[]
for slug,P in PRODUTOS.items():
    d=P['dev']
    V=pagina(1080,1920,f'''
<div class="logo" style="position:absolute;left:80px;top:150px;width:360px">{LOGO}</div>
<div class="t" style="position:absolute;left:80px;right:80px;top:290px;font-size:104px">{P['titulo']}</div>
<div class="sub" style="position:absolute;left:80px;right:80px;top:560px;font-size:44px">{P['sub']}</div>
{dispositivos(41,760,0.78,**d)}
<div class="pill" style="position:absolute;left:80px;right:80px;top:1560px;height:150px;font-size:60px">{P['pill']}</div>
<div class="nota" style="position:absolute;left:80px;right:80px;top:1740px;font-size:28px;text-align:center">{P['nota']}</div>
''')
    Q=pagina(1080,1080,f'''
<div class="logo" style="position:absolute;left:70px;top:70px;width:300px">{LOGO}</div>
<div class="t" style="position:absolute;left:70px;top:160px;width:900px;font-size:74px">{P['q_t']}</div>
<div class="sub" style="position:absolute;left:70px;top:270px;width:900px;font-size:32px">{P['q_sub']}</div>
{dispositivos(430,480,0.5,**d)}
<div class="pill" style="position:absolute;left:70px;top:900px;width:460px;height:110px;font-size:44px">{P['q_pill']}</div>
<div class="nota" style="position:absolute;left:70px;top:1030px;font-size:20px">7 dias para desistir · seusociogestor.com.br</div>
''')
    Hh=pagina(1600,1000,f'''{dispositivos(150,50,0.95,**d)}''',marca=False)
    for nome,html_,w,h in [(f'{slug}-produto-1080x1920',V,1080,1920),(f'{slug}-produto-1080x1080',Q,1080,1080),(f'{slug}-produto-hero-1600x1000',Hh,1600,1000)]:
        (out/f'{nome}.html').write_text(html_); alvos.append([nome,w,h])
import json
js=f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox']}});
for(const [n,w,h] of {json.dumps(alvos)}){{
 const p=await b.newPage({{viewport:{{width:w,height:h}}}}); await p.goto('file://{out}/'+n+'.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
 await p.screenshot({{path:'{ROOT}/'+n+'.png',omitBackground:n.includes('hero')}}); await p.close(); }}
await b.close(); console.log('ok');}})();"""
(out/'shot.js').write_text(js)
subprocess.run(['node',str(out/'shot.js')],check=True,env={**os.environ,'NODE_PATH':str(S/'pw'/'node_modules')})
