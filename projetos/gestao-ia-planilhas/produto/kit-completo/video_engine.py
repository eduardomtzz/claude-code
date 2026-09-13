#!/usr/bin/env python3
"""Motor das aulas em vídeo do Kit Completo: telas reais + zoom + legenda + narração (Piper, pt-BR).
Uso: python3 build_videos.py [nome]  (sem nome = todos). Saída em entrega/videos/*.mp4"""
import json, wave, subprocess, pathlib, sys, base64, shutil
ROOT=pathlib.Path(__file__).resolve().parent
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
VOZ=S/'voz'/'pt_BR-faber-medium.onnx'
FONTS=ROOT.parents[1]/'site'/'public'/'assets'/'fonts'
LOGO=(ROOT.parents[1]/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
W,H=1280,720
PAUSA=1.1  # segundos de respiro após cada fala

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

def sintetiza(texto, wav):
    from piper import PiperVoice
    global _voz
    try: _voz
    except NameError: _voz=PiperVoice.load(str(VOZ))
    try:
        from piper import SynthesisConfig
        cfgv=SynthesisConfig(length_scale=1.1)
        with wave.open(str(wav),'wb') as w: _voz.synthesize_wav(texto, w, syn_config=cfgv)
    except Exception:
        with wave.open(str(wav),'wb') as w: _voz.synthesize_wav(texto, w)
    with wave.open(str(wav),'rb') as w: return w.getnframes()/w.getframerate()

CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#FFFAF0;font-family:Figtree,sans-serif;color:#1F1235}}
.cena{{position:absolute;inset:0;opacity:0;transition:opacity .5s}} .cena.on{{opacity:1}}
.topo{{position:absolute;top:22px;left:32px;width:220px;z-index:5}}
.topo svg{{width:220px;height:auto}}
.tela{{position:absolute;left:32px;top:84px;width:{W-64}px;height:{H-84-118}px;border-radius:14px;overflow:hidden;background:#fff;border:1px solid #DCD2EC;box-shadow:0 18px 40px -24px rgba(31,18,53,.45)}}
.tela img{{position:absolute;left:0;top:0;transform-origin:0 0;transition:transform 1.6s cubic-bezier(.4,0,.2,1)}}
.legenda{{position:absolute;left:32px;right:32px;bottom:26px;height:74px;background:#3B1F5E;color:#fff;border-radius:14px;display:flex;align-items:center;padding:0 28px;font-size:28px;font-weight:600;letter-spacing:-.01em;z-index:6}}
.legenda b{{background:#FFC83D;color:#3B1F5E;border-radius:999px;padding:4px 14px;font-size:16px;margin-right:18px;font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:0;white-space:nowrap}}
.capa{{background:#3B1F5E;color:#fff;padding:70px 90px}} .capa .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:76px;line-height:1.02;letter-spacing:-.02em;margin-top:150px;max-width:1000px}}
.capa .t em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}} .capa .s{{font-size:30px;color:#D9C8F5;margin-top:22px}} .capa .k{{font-family:'Bricolage Grotesque';font-weight:600;font-size:22px;color:#FFC83D;margin-top:60px}}
.capa .simb{{position:absolute;right:90px;top:70px;width:170px}}
.card{{padding:96px 100px 0}} .card .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:44px;color:#3B1F5E;letter-spacing:-.02em}} .card .p{{font-size:29px;line-height:1.35;margin-top:26px;max-width:1000px;color:#1F1235}}
.card .li{{list-style:none;padding:0;margin:26px 0 0;max-width:1060px}} .card .li li{{font-size:28px;line-height:1.3;padding:10px 0 10px 44px;position:relative;color:#1F1235;border-top:1px solid #DCD2EC}} .card .li li::before{{content:'';position:absolute;left:0;top:18px;width:22px;height:22px;border-radius:50%;background:#FFC83D}}
.card .box{{background:#F3EEFB;border-left:10px solid #FFC83D;border-radius:0 14px 14px 0;padding:26px 30px;font-family:'IBM Plex Mono',monospace;font-size:22px;color:#3B1F5E;margin-top:34px;max-width:1000px}}
.fim{{background:#3B1F5E;color:#fff;padding:120px 90px}} .fim .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:54px;line-height:1.05;letter-spacing:-.02em;max-width:1000px}}
.fim .s{{font-size:28px;color:#D9C8F5;margin-top:26px}} .fim .site{{position:absolute;bottom:60px;left:90px;font-family:'Bricolage Grotesque';font-weight:600;font-size:26px;color:#FFC83D}}
"""
SIMB='<svg viewBox="0 0 72 72"><rect x="12" y="46" width="30" height="10" rx="5.5" fill="#B89BE0"/><rect x="21" y="31" width="30" height="10" rx="5.5" fill="#fff"/><rect x="30" y="16" width="30" height="10" rx="5.5" fill="#fff"/><circle cx="56" cy="52" r="6" fill="#FFC83D"/></svg>'

import html as _html
def esc(x): return _html.escape(str(x), quote=False)
def html_video(nome, rot, cenas):
    partes=[]
    for i,c in enumerate(cenas):
        if c['tipo']=='capa':
            partes.append(f'<div class="cena capa" id="c{i}"><div class="simb">{SIMB}</div><div class="t"><em>Aula {rot["n"]}</em><br>{rot["titulo"]}</div><div class="s">{rot["sub"]}</div><div class="k">Kit IA no Trabalho · Completo · Seu Sócio Gestor</div></div>')
        elif c['tipo']=='tela':
            src='data:image/png;base64,'+b64(ROOT/c['img'])
            partes.append(f'<div class="cena" id="c{i}"><div class="topo">{LOGO}</div><div class="tela"><img src="{src}" data-foco="{",".join(map(str,c["foco"]))}"></div><div class="legenda"><b>{i}</b>{esc(c["legenda"])}</div></div>')
        elif c['tipo']=='card':
            box=f'<div class="box">{esc(c["box"])}</div>' if c.get('box') else ''
            partes.append(f'<div class="cena card" id="c{i}"><div class="topo">{LOGO}</div><div class="t">{esc(c["titulo"])}</div><div class="p">{esc(c["texto"])}</div>{box}<div class="legenda"><b>{i}</b>{esc(c["legenda"])}</div></div>')
        elif c['tipo']=='lista':
            its=''.join(f'<li>{esc(x)}</li>' for x in c['itens'])
            partes.append(f'<div class="cena card" id="c{i}"><div class="topo">{LOGO}</div><div class="t">{esc(c["titulo"])}</div><ul class="li">{its}</ul><div class="legenda"><b>{i}</b>{esc(c["legenda"])}</div></div>')
        elif c['tipo']=='fim':
            partes.append(f'<div class="cena fim" id="c{i}"><div class="t">{esc(c["fala"])}</div><div class="s">Suporte por e-mail · reembolso em 7 dias · pagamento único</div><div class="site">seusociogestor.com.br</div></div>')
    durs=[c['dur'] for c in cenas]
    js=f"""
const durs={json.dumps(durs)}; const W={W-64}, H={H-84-118};
function foco(img){{ const [fx,fy,fw,fh]=img.dataset.foco.split(',').map(Number); const nw=img.naturalWidth, nh=img.naturalHeight;
  const base=W/nw; // escala para caber na largura
  const sx=W/(nw*fw), sy=H/(nh*fh); const s=Math.min(sx,sy, base*3.2);
  const tx=-fx*nw*s + (W-fw*nw*s)/2, ty=-fy*nh*s + Math.max(0,(H-fh*nh*s)/2);
  return `translate(${{tx}}px, ${{Math.min(0,ty)}}px) scale(${{s}})`; }}
document.querySelectorAll('.tela img').forEach(img=>{{ const nw=img.naturalWidth||1650; img.style.transform=`scale(${{W/nw}})`; }});
let t=0; durs.forEach((d,i)=>{{ setTimeout(()=>{{ document.querySelectorAll('.cena.on').forEach(e=>e.classList.remove('on')); const c=document.getElementById('c'+i); c.classList.add('on');
   const img=c.querySelector('.tela img'); if(img){{ img.style.transform=`scale(${{W/img.naturalWidth}})`; setTimeout(()=>{{img.style.transform=foco(img);}},900); }} }}, t*1000); t+=d; }});
setTimeout(()=>{{document.title='FIM'}}, t*1000+300);
"""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(partes)}<script>window.addEventListener("load",()=>{{ {js} }});</script></body></html>'

def build(nome):
    rot=ROTEIROS[nome]; out=ROOT/'videos'/nome; out.mkdir(parents=True,exist_ok=True)
    cenas=rot['cenas']; wavs=[]
    (ROOT/'entrega'/'videos').mkdir(parents=True,exist_ok=True)
    for i,c in enumerate(cenas):
        w=out/f'fala{i}.wav'; d=sintetiza(c['fala'],w); c['dur']=round(d+PAUSA,2); wavs.append((w,c['dur']))
    total=sum(c['dur'] for c in cenas)
    (out/'video.html').write_text(html_video(nome,rot,cenas))
    # áudio: cada fala seguida de silêncio até completar a duração da cena
    lista=out/'audio.txt'; linhas=[]
    for i,(w,d) in enumerate(wavs):
        p=out/f'cena{i}.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(w),'-af',f'apad=whole_dur={d}','-ar','44100','-ac','1',str(p)],check=True); linhas.append(f"file '{p.name}'")
    lista.write_text('\n'.join(linhas)+'\n')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(lista),'-c','copy',str(out/'narracao.wav')],check=True)
    # vídeo: gravação do Chromium
    rec=S/'gravar.js'
    rec.write_text("""const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [html,dir,total]=process.argv.slice(2);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox','--disable-gpu']});
const ctx=await b.newContext({viewport:{width:%d,height:%d},recordVideo:{dir:dir,size:{width:%d,height:%d}}});
const p=await ctx.newPage(); await p.goto('file://'+html); await p.waitForFunction(()=>document.title==='FIM',null,{timeout:(Number(total)+15)*1000});
const v=p.video(); await ctx.close(); const f=await v.path(); fs.renameSync(f,path.join(dir,'gravacao.webm')); await b.close(); console.log('gravado');})();""" % (W,H,W,H))
    subprocess.run(['node',str(rec),str(out/'video.html'),str(out),str(total)],check=True,env={**dict(__import__('os').environ),'NODE_PATH':str(S/'pw'/'node_modules')})
    # junta: corta o vídeo na duração do áudio, codifica mp4
    final=ROOT/'entrega'/'videos'/f'{nome}.mp4'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(out/'gravacao.webm'),'-i',str(out/'narracao.wav'),'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(final)],check=True)
    # legendas .srt (acessibilidade e Kiwify)
    srt=[]; t=0.0
    def ts(x): h=int(x//3600); m=int(x%3600//60); s=x%60; return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.',',')
    for i,c in enumerate(cenas):
        srt.append(f"{i+1}\n{ts(t)} --> {ts(t+c['dur']-PAUSA)}\n{c['fala']}\n"); t+=c['dur']
    (ROOT/'entrega'/'videos'/f'{nome}.srt').write_text('\n'.join(srt))
    print(nome, f'{total:.1f}s', final)

if __name__=='__main__':
    nomes=sys.argv[1:] or list(ROTEIROS)
    for n in nomes: build(n)

def build_all(roteiros, nomes=None):
    global ROTEIROS
    ROTEIROS=roteiros
    for n in (nomes or list(roteiros)): build(n)
