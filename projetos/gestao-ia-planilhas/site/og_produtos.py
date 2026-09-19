#!/usr/bin/env python3
"""Imagem Open Graph (1200×630) por página de produto: nome, promessa curta, preço e o mockup notebook+celular.
Saída: public/assets/<kit>/og-1200x630.jpg. Uso: python3 og_produtos.py [kit|completo|advogados|medicos|todos]"""
import pathlib, base64, subprocess, os, sys, json
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parent
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
FONTS=ROOT/'public'/'assets'/'fonts'; CRI=PROJ/'08-ads'/'criativos'
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
SIMB='<svg viewBox="0 0 72 72"><rect x="12" y="46" width="30" height="10" rx="5.5" fill="#B89BE0"/><rect x="21" y="31" width="30" height="10" rx="5.5" fill="#7A5AA8"/><rect x="30" y="16" width="30" height="10" rx="5.5" fill="#7A5AA8"/><circle cx="56" cy="52" r="6" fill="#FFC83D"/></svg>'
PROD={
 'kit':dict(mock='essencial', eyebrow='Kit IA no Trabalho · Essencial', t='3 planilhas prontas e <em>40 prompts</em> de IA', sub='Semana, relatório do mês e ganhos e gastos. Manual e vídeos.', preco='R$ 37'),
 'completo':dict(mock='completo', eyebrow='Kit IA no Trabalho · Completo', t='10 planilhas, 80 prompts, <em>8 aulas</em>', sub='Método de 4 passos para relatório, projeto, metas e orçamento.', preco='R$ 197'),
 'advogados':dict(mock='advogados', eyebrow='Kit de Gestão para Advogados', t='20 planilhas em <em>5 núcleos</em> do escritório', sub='Prazos, honorários, caixa, carteira e painel. 40 prompts, 8 aulas.', preco='R$ 497'),
 'medicos':dict(mock='medicos', eyebrow='Kit de Gestão para Médicos', t='20 planilhas em <em>5 núcleos</em> da clínica', sub='Agenda, preço, convênios, caixa e painel. 40 prompts, 8 aulas.', preco='R$ 697'),
}
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#FFFAF0;font-family:Figtree,sans-serif;color:#1F1235;position:relative}}
.marca{{position:absolute;opacity:.06;width:760px;right:-200px;bottom:-230px}}
.logo{{position:absolute;left:64px;top:52px;width:250px}} .logo svg{{width:250px;height:auto}}
.eyebrow{{position:absolute;left:64px;top:140px;font-family:'IBM Plex Mono';font-size:19px;letter-spacing:.08em;text-transform:uppercase;color:#7A5AA8}}
.t{{position:absolute;left:64px;top:184px;width:560px;font-family:'Bricolage Grotesque';font-weight:800;font-size:58px;line-height:1.02;letter-spacing:-.025em;color:#3B1F5E}}
.t em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}}
.sub{{position:absolute;left:64px;top:392px;width:540px;font-size:24px;line-height:1.35;color:#5A4A78}}
.pill{{position:absolute;left:64px;bottom:56px;display:inline-flex;align-items:center;background:#FFC83D;color:#3B1F5E;border-radius:999px;font-family:'Bricolage Grotesque';font-weight:800;padding:0 30px;height:64px;font-size:30px;white-space:nowrap}}
.pill small{{font-family:Figtree;font-weight:600;font-size:18px;margin-left:14px;color:#3B1F5E;opacity:.8}}
.mock{{position:absolute;right:-40px;top:96px;width:640px}} .mock img{{width:100%;display:block}}
"""
def gera(kit):
    c=PROD[kit]; out=S/'og'/kit; out.mkdir(parents=True,exist_ok=True)
    mock=CRI/f"{c['mock']}-produto-hero-1600x1000.png"
    if not mock.exists(): print('sem herói ainda:',mock.name,'(rode 08-ads/criativos/build_mockup.py)'); return
    html=f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="marca">{SIMB}</div><div class="logo">{LOGO}</div>
<p class="eyebrow">{c['eyebrow']}</p><h1 class="t">{c['t']}</h1><p class="sub">{c['sub']}</p>
<div class="pill">{c['preco']}<small>pagamento único · 7 dias para desistir</small></div>
<div class="mock"><img src="data:image/png;base64,{b64(mock)}"></div></body></html>'''
    (out/'og.html').write_text(html,encoding='utf-8')
    js=f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox']}});
const p=await b.newPage({{viewport:{{width:1200,height:630}}}}); await p.goto('file://{out}/og.html'); await p.waitForTimeout(300); await p.screenshot({{path:'{out}/og.png'}}); await b.close();}})();"""
    (out/'shot.js').write_text(js); subprocess.run(['node',str(out/'shot.js')],check=True,env={**os.environ,'NODE_PATH':str(S/'pw'/'node_modules')})
    dest=ROOT/'public'/'assets'/kit/'og-1200x630.jpg'; Image.open(out/'og.png').convert('RGB').save(dest,'JPEG',quality=86,optimize=True); print(kit,dest.stat().st_size//1024,'KB')
alvo=sys.argv[1] if len(sys.argv)>1 else 'todos'
for k in PROD:
    if alvo in (k,'todos'): gera(k)
