#!/usr/bin/env python3
"""Criativo de vídeo 9:16 do Kit Essencial (roteiro A, 'Não comece do zero'). Gera essencial-nao-comece-do-zero-9x16.mp4 + cartão final."""
import sys, json, wave, subprocess, pathlib, base64, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]/'produto'/'kit-completo'))
import video_engine as V
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parents[1]; DOCS=PROJ/'produto'/'kit-essencial'/'docs'
W,H=1080,1920; PAUSA=0.6
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text(); LOGOB=(PROJ/'03-marca'/'logo'/'logo-branco.svg').read_text()
FONTS=PROJ/'site'/'public'/'assets'/'fonts'
CENAS=[
 {'tipo':'branco','fala':'Toda semana, a mesma planilha do zero.','legenda':'A mesma planilha. Do zero.'},
 {'tipo':'tela','img':DOCS/'tela-semana-hoje.png','foco':[0,0,1,0.55],'fala':'Esta já vem pronta: você digita as tarefas, ela diz o que fazer primeiro.','legenda':'Você digita. Ela ordena.','rotulo':'Semana Organizada · aba Hoje'},
 {'tipo':'tela','img':DOCS/'tela-relatorio-resumo.png','foco':[0,0,0.75,0.7],'fala':'Esta escreve as frases do seu relatório do mês.','legenda':'O relatório se escreve.','rotulo':'Relatório Mensal Pronto · aba Resumo'},
 {'tipo':'chat','fala':'Cola no prompt e a IA devolve o texto para você revisar.','legenda':'40 prompts prontos.'},
 {'tipo':'tela','img':DOCS/'tela-ganhos-painel.png','foco':[0,0,0.85,0.35],'fala':'E esta mostra quanto sobrou e para onde foi.','legenda':'Quanto sobrou. Onde foi.','rotulo':'Ganhos e Gastos · Painel'},
 {'tipo':'fim','fala':'Kit IA no Trabalho. Trinta e sete reais, uma vez. Sete dias para desistir.','legenda':'R$ 37 · Comprar'},
]
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#FFFAF0;font-family:Figtree,sans-serif;color:#1F1235}}
.cena{{position:absolute;inset:0;opacity:0;transition:opacity .4s}} .cena.on{{opacity:1}}
.topo{{position:absolute;top:150px;left:60px;width:300px;z-index:5}} .topo svg{{width:300px;height:auto}}
.rotulo{{position:absolute;top:240px;left:60px;right:60px;font-family:'IBM Plex Mono';font-size:26px;color:#7A5AA8}}
.tela{{position:absolute;left:60px;top:300px;width:{W-120}px;height:1080px;border-radius:24px;overflow:hidden;background:#fff;border:2px solid #DCD2EC;box-shadow:0 30px 60px -30px rgba(31,18,53,.45)}}
.tela img{{position:absolute;left:0;top:0;transform-origin:0 0;transition:transform 2.2s cubic-bezier(.4,0,.2,1)}}
.legenda{{position:absolute;left:60px;right:60px;bottom:330px;min-height:150px;background:#3B1F5E;color:#fff;border-radius:24px;display:flex;align-items:center;padding:28px 40px;font-family:'Bricolage Grotesque';font-weight:800;font-size:64px;line-height:1.05;letter-spacing:-.02em;z-index:6}}
.legenda em{{font-style:normal;color:#FFC83D}}
.rodape{{position:absolute;left:60px;right:60px;bottom:250px;font-family:'IBM Plex Mono';font-size:24px;color:#7A5AA8;z-index:6}}
/* planilha em branco */
.grid{{position:absolute;left:0;top:0;right:0;bottom:0;background:#fff}}
.grid .cab{{height:52px;background:#F3F3F3;border-bottom:1px solid #C9C9C9;display:flex}} .grid .cab i{{width:150px;border-right:1px solid #C9C9C9;font-style:normal;font-family:Arial;font-size:22px;color:#555;display:flex;align-items:center;justify-content:center}}
.grid .cab i:first-child{{width:70px}}
.grid .row{{height:44px;border-bottom:1px solid #E3E3E3;display:flex}} .grid .row i{{width:150px;border-right:1px solid #E3E3E3;font-style:normal;font-family:Arial;font-size:20px;color:#777;display:flex;align-items:center;justify-content:center}} .grid .row i:first-child{{width:70px;background:#F3F3F3}}
.cursor{{position:absolute;left:70px;top:52px;width:150px;height:44px;border:3px solid #217346;animation:pisca 1s steps(2) infinite}}
@keyframes pisca{{50%{{opacity:.2}}}}
/* chat */
.chat{{position:absolute;left:0;top:0;right:0;bottom:0;background:#F7F7F8;padding:40px}}
.msg{{border-radius:20px;padding:26px 30px;font-size:27px;line-height:1.4;margin-bottom:26px;max-width:92%}}
.eu{{background:#3B1F5E;color:#fff;margin-left:auto;font-family:'IBM Plex Mono';font-size:22px}}
.ia{{background:#fff;border:1px solid #E1E1E6;color:#1F1235}} .ia b{{color:#3B1F5E}}
.ia .cur{{display:inline-block;width:14px;height:30px;background:#3B1F5E;vertical-align:-6px;animation:pisca .8s steps(2) infinite}}
/* fim */
.fim{{background:#3B1F5E;color:#fff;padding:0 80px}} .fim .l{{position:absolute;top:240px;left:80px;width:520px}} .fim .l svg{{width:520px;height:auto}}
.fim .t{{position:absolute;top:520px;left:80px;right:80px;font-family:'Bricolage Grotesque';font-weight:800;font-size:96px;line-height:1.0;letter-spacing:-.02em}}
.fim .t em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}}
.fim .lista{{position:absolute;top:920px;left:80px;right:80px;list-style:none;padding:0;margin:0}} .fim .lista li{{font-size:40px;padding:18px 0 18px 70px;position:relative;border-top:1px solid rgba(255,255,255,.18);color:#F3EEFB}}
.fim .lista li::before{{content:'';position:absolute;left:0;top:26px;width:36px;height:36px;border-radius:50%;background:#FFC83D url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M4 9.5l3 3 7-7' fill='none' stroke='%233B1F5E' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/60% no-repeat}}
.fim .preco{{position:absolute;top:1290px;left:80px;right:80px;background:#FFC83D;color:#3B1F5E;border-radius:999px;height:150px;display:flex;align-items:center;justify-content:center;font-family:'Bricolage Grotesque';font-weight:800;font-size:64px}}
.fim .nota{{position:absolute;top:1470px;left:80px;right:80px;font-family:'IBM Plex Mono';font-size:28px;color:#D9C8F5;text-align:center}}
.fim .site{{position:absolute;top:1560px;left:80px;right:80px;font-family:'Bricolage Grotesque';font-weight:600;font-size:34px;color:#FFC83D;text-align:center}}
"""
def grid():
    cab='<div class="cab"><i></i>'+''.join(f'<i>{c}</i>' for c in 'ABCDEFG')+'</div>'
    rows=''.join(f'<div class="row"><i>{r}</i>'+'<i></i>'*7+'</div>' for r in range(1,25))
    return f'<div class="grid">{cab}{rows}<div class="cursor"></div></div>'
def chat():
    return ('<div class="chat"><div class="msg eu">Escreva o relatório mensal para a diretoria, em até 300 palavras, com: Resultado do mês em uma frase; Destaques; Pontos de atenção; Próximos passos...<br>Números:<br>Receita: R$ 131.200 (+5%); Despesas: R$ 89.800 (+3%); Resultado: R$ 41.400 (+11%)...</div>'
            '<div class="msg ia"><b>Resultado do mês.</b> Setembro fechou com resultado de R$ 41.400, 11% acima de agosto e 18% acima da meta.<br><br><b>Destaques.</b> Receita de R$ 131.200 (+5%, meta batida). Ticket médio de R$ 9.700 (+3%). Inadimplência em 2,4%, abaixo da meta.<br><br><b>Pontos de atenção.</b> Despesas de R$ 89.800, acima da meta [explicar]<span class="cur"></span></div></div>')
def html(cenas):
    partes=[]
    for i,c in enumerate(cenas):
        leg=f'<div class="legenda">{c["legenda"]}</div>'
        rod='<div class="rodape">Tela real · dados fictícios</div>'
        if c['tipo']=='branco':
            partes.append(f'<div class="cena" id="c{i}"><div class="topo">{LOGO}</div><div class="rotulo">segunda-feira, 8h02</div><div class="tela">{grid()}</div>{leg}</div>')
        elif c['tipo']=='tela':
            partes.append(f'<div class="cena" id="c{i}"><div class="topo">{LOGO}</div><div class="rotulo">{c["rotulo"]}</div><div class="tela"><img src="data:image/png;base64,{b64(c["img"])}" data-foco="{",".join(map(str,c["foco"]))}"></div>{leg}{rod}</div>')
        elif c['tipo']=='chat':
            partes.append(f'<div class="cena" id="c{i}"><div class="topo">{LOGO}</div><div class="rotulo">Prompt Escrever 01 · na IA que você já usa</div><div class="tela">{chat()}</div>{leg}</div>')
        elif c['tipo']=='fim':
            partes.append(f'<div class="cena fim" id="c{i}"><div class="l">{LOGOB}</div><div class="t">Kit IA no Trabalho <em>Essencial</em></div><ul class="lista"><li>3 planilhas prontas</li><li>40 prompts de IA</li><li>Mini-manual e 3 vídeos</li></ul><div class="preco">R$ 37 · uma vez</div><div class="nota">Pix ou cartão · 7 dias para desistir</div><div class="site">seusociogestor.com.br</div></div>')
    durs=[c['dur'] for c in cenas]
    js=f"""const durs={json.dumps(durs)}; const W={W-120}, H=1080;
function foco(img){{ const [fx,fy,fw,fh]=img.dataset.foco.split(',').map(Number); const nw=img.naturalWidth, nh=img.naturalHeight;
  const base=W/nw; const sx=W/(nw*fw), sy=H/(nh*fh); const s=Math.min(sx,sy,base*3); const tx=-fx*nw*s+(W-fw*nw*s)/2, ty=-fy*nh*s+Math.max(0,(H-fh*nh*s)/2);
  return `translate(${{tx}}px, ${{Math.min(0,ty)}}px) scale(${{s}})`; }}
document.querySelectorAll('.tela img').forEach(img=>{{ img.style.transform=`scale(${{W/img.naturalWidth}})`; }});
let t=0; durs.forEach((d,i)=>{{ setTimeout(()=>{{ document.querySelectorAll('.cena.on').forEach(e=>e.classList.remove('on')); const c=document.getElementById('c'+i); c.classList.add('on');
  const img=c.querySelector('.tela img'); if(img){{ img.style.transform=`scale(${{W/img.naturalWidth}})`; setTimeout(()=>{{img.style.transform=foco(img);}},700); }} }}, t*1000); t+=d; }});
setTimeout(()=>{{document.title='FIM'}}, t*1000+300);"""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(partes)}<script>window.addEventListener("load",()=>{{ {js} }});</script></body></html>'
out=ROOT/'trabalho'; out.mkdir(exist_ok=True)
wavs=[]
for i,c in enumerate(CENAS):
    w=out/f'fala{i}.wav'; d=V.sintetiza(c['fala'],w); c['dur']=round(max(d+PAUSA, 2.6 if c['tipo']=='branco' else 4.2),2); wavs.append((w,c['dur']))
total=sum(c['dur'] for c in CENAS)
(out/'video.html').write_text(html(CENAS))
linhas=[]
for i,(w,d) in enumerate(wavs):
    p=out/f'cena{i}.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(w),'-af',f'apad=whole_dur={d}','-ar','44100','-ac','1',str(p)],check=True); linhas.append(f"file '{p.name}'")
(out/'audio.txt').write_text('\n'.join(linhas)+'\n')
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(out/'audio.txt'),'-c','copy',str(out/'narracao.wav')],check=True)
rec=out/'gravar.js'
rec.write_text("""const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [html,dir,total]=process.argv.slice(2);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox','--disable-gpu']});
const ctx=await b.newContext({viewport:{width:%d,height:%d},recordVideo:{dir:dir,size:{width:%d,height:%d}}});
const p=await ctx.newPage(); await p.goto('file://'+html); await p.waitForFunction(()=>document.title==='FIM',null,{timeout:(Number(total)+15)*1000});
const v=p.video(); await ctx.close(); const f=await v.path(); fs.renameSync(f,path.join(dir,'gravacao.webm')); await b.close(); console.log('gravado');})();""" % (W,H,W,H))
subprocess.run(['node',str(rec),str(out/'video.html'),str(out),str(total)],check=True,env={**os.environ,'NODE_PATH':str(V.S/'pw'/'node_modules')})
final=ROOT/'essencial-nao-comece-do-zero-9x16.mp4'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(out/'gravacao.webm'),'-i',str(out/'narracao.wav'),'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(final)],check=True)
srt=[]; t=0.0
def ts(x): h=int(x//3600); m=int(x%3600//60); s=x%60; return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.',',')
for i,c in enumerate(CENAS): srt.append(f"{i+1}\n{ts(t)} --> {ts(t+c['dur']-PAUSA)}\n{c['fala']}\n"); t+=c['dur']
(ROOT/'essencial-nao-comece-do-zero-9x16.srt').write_text('\n'.join(srt))
print(f'{total:.1f}s', final)
