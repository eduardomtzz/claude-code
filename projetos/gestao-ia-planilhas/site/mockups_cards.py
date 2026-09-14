#!/usr/bin/env python3
"""Cards do inventário das páginas de produto: cada planilha em um notebook (aba principal) com uma
segunda aba no celular. Padrão para todos os kits. Saída: public/assets/<kit>/mock-<nome>.webp (1200×750).
Uso: python3 mockups_cards.py [kit|completo|advogados|medicos|todos]"""
import pathlib, base64, subprocess, os, sys, json
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parent
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
DE=PROJ/'produto'/'kit-essencial'/'docs'; DC=PROJ/'produto'/'kit-completo'/'docs'; DA=PROJ/'produto'/'kit-advogados'/'docs'; DM=PROJ/'produto'/'kit-medicos'/'docs'
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
W,H=1600,1000
CSS="""*{box-sizing:border-box} html,body{margin:0;width:1600px;height:1000px;background:transparent;overflow:hidden;position:relative}
.lap{position:absolute;background:#1F1235;border-radius:26px 26px 6px 6px;padding:22px 22px 30px;box-shadow:0 60px 100px -50px rgba(31,18,53,.6)}
.lap .scr{background:#fff;border-radius:10px;overflow:hidden;position:relative} .lap .scr img{position:absolute;left:0;top:0;width:100%}
.lap .base{position:absolute;left:-6%;right:-6%;bottom:-26px;height:26px;background:linear-gradient(#2B1B45,#1F1235);border-radius:0 0 18px 18px}
.lap .base::after{content:'';position:absolute;left:44%;right:44%;top:0;height:8px;background:#3B1F5E;border-radius:0 0 8px 8px}
.fone{position:absolute;background:#1F1235;border-radius:46px;padding:14px;box-shadow:0 50px 90px -40px rgba(31,18,53,.7)}
.fone .scr{background:#fff;border-radius:34px;overflow:hidden;position:relative} .fone .scr img{position:absolute;left:0;top:0}
.fone .notch{position:absolute;left:50%;top:14px;transform:translateX(-50%);width:36%;height:26px;background:#1F1235;border-radius:0 0 18px 18px;z-index:2}"""
def cena(lap,fone,escala=0.95,x=150,y=50,fone_zoom=2.0):
    lw=int(1100*escala); lh=int(660*escala); fw=int(330*escala); fh=int(680*escala)
    return f'''<div style="position:absolute;left:{x}px;top:{y}px">
      <div class="lap" style="left:0;top:0;width:{lw}px"><div class="scr" style="height:{lh-int(52*escala)}px"><img src="data:image/png;base64,{b64(lap)}"></div><div class="base"></div></div>
      <div class="fone" style="left:{lw-int(150*escala)}px;top:{int(140*escala)}px;width:{fw}px;height:{fh}px"><div class="notch"></div><div class="scr" style="height:100%"><img src="data:image/png;base64,{b64(fone)}" style="width:{int(fw*fone_zoom)}px;left:{-int(fw*0.02)}px;top:0"></div></div>
    </div>'''
# kit -> {nome: (tela do notebook, tela do celular)}
CARDS={
 'kit':{'semana':(DE/'tela-semana-hoje.png',DE/'tela-semana-tarefas.png'),'relatorio':(DE/'tela-relatorio-painel.png',DE/'tela-relatorio-resumo.png'),'ganhos':(DE/'tela-ganhos-painel.png',DE/'tela-ganhos-lancamentos.png')},
 'completo':{'semana':(DE/'tela-semana-hoje.png',DE/'tela-semana-tarefas.png'),'relatorio':(DE/'tela-relatorio-painel.png',DE/'tela-relatorio-resumo.png'),'ganhos':(DE/'tela-ganhos-painel.png',DE/'tela-ganhos-lancamentos.png'),
   'projetos':(DC/'tela-projetos-painel.png',DC/'tela-projetos-linha.png'),'ata':(DC/'tela-ata-aberto.png',DC/'tela-ata-resumo.png'),'metas':(DC/'tela-metas-painel.png',DC/'tela-metas-metas.png'),
   'orcamento':(DC/'tela-orcamento-painel.png',DC/'tela-orcamento-previsto.png'),'funil':(DC/'tela-funil-painel.png',DC/'tela-funil-propostas.png'),'horas':(DC/'tela-horas-painel.png',DC/'tela-horas-lancamento.png'),'base':(DC/'tela-base-checklist.png',DC/'tela-base-base.png')},
 'advogados':{'prazos':(DA/'tela-01.png',DA/'tela-02.png'),'honorarios':(DA/'tela-05.png',DA/'tela-06.png'),'caixa':(DA/'tela-09.png',DA/'tela-10.png'),'carteira':(DA/'tela-13.png',DA/'tela-14.png'),'painel':(DA/'tela-17.png',DA/'tela-20.png')},
 'medicos':{'agenda':(DM/'tela-01.png',DM/'tela-02.png'),'preco':(DM/'tela-05.png',DM/'tela-06.png'),'caixa':(DM/'tela-09.png',DM/'tela-10.png'),'convenios':(DM/'tela-13.png',DM/'tela-14.png'),'painel':(DM/'tela-17.png',DM/'tela-20-painel.png')},
}
def gera(kit):
    out=S/'mock-cards'/kit; out.mkdir(parents=True,exist_ok=True); jobs=[]
    for nome,(lap,fone) in CARDS[kit].items():
        if not (lap.exists() and fone.exists()): print('sem tela',kit,nome); continue
        (out/f'{nome}.html').write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{cena(lap,fone)}</body></html>')
        jobs.append(nome)
    js=f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox']}});
for(const n of {json.dumps(jobs)}){{const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}}); await p.goto('file://{out}/'+n+'.html'); await p.waitForTimeout(300); await p.screenshot({{path:'{out}/'+n+'.png',omitBackground:true}}); await p.close();}}
await b.close();}})();"""
    (out/'shot.js').write_text(js); subprocess.run(['node',str(out/'shot.js')],check=True,env={**os.environ,'NODE_PATH':str(S/'pw'/'node_modules')})
    dest=ROOT/'public'/'assets'/('kit' if kit=='kit' else kit); dest.mkdir(exist_ok=True)
    for nome in jobs:
        im=Image.open(out/f'{nome}.png').convert('RGBA'); im=im.crop(im.getbbox())
        # enquadra em 1200×750 com margem, fundo transparente
        cv=Image.new('RGBA',(1200,750),(0,0,0,0)); k=min(1120/im.width,700/im.height); im=im.resize((int(im.width*k),int(im.height*k)),Image.LANCZOS)
        cv.paste(im,((1200-im.width)//2,(750-im.height)//2),im); cv.save(dest/f'mock-{nome}.webp','WEBP',quality=82,method=6); print(kit,nome,'ok')
alvo=sys.argv[1] if len(sys.argv)>1 else 'todos'
for k in CARDS:
    if alvo in(k,'todos'): gera(k)
