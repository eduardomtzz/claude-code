#!/usr/bin/env python3
"""Motor das aulas em vídeo do Kit de Gestão para Médicos (cópia do motor do Kit Advogados): telas reais + zoom + legenda + narração (Piper, pt-BR).
Uso: python3 build_aulas.py [nome]  (sem nome = todos). Saída em entrega/videos/*.mp4"""
import json, wave, subprocess, pathlib, sys, base64, shutil
ROOT=pathlib.Path(__file__).resolve().parent
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
VOZ=S/'voz'/'pt_BR-faber-medium.onnx'
FONTS=ROOT.parents[1]/'site'/'public'/'assets'/'fonts'
LOGO=(ROOT.parents[1]/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
W,H=1280,720
# layout vertical: tela (topo 84) · faixa da legenda gravada (FAIXA) · barra roxa (BARRA_H) · rodapé (BARRA_B)
BARRA_H,BARRA_B,FAIXA=64,18,70
TELA_H=H-84-(BARRA_H+BARRA_B+FAIXA)  # 484
LEG_MARGEM,LEG_TAM=BARRA_H+BARRA_B+6,26  # legenda gravada: base 6 px acima da barra, corpo 26 px
KICKER_B=LEG_MARGEM+2*int(LEG_TAM*1.25)+16   # capa: kicker fixo no rodapé, acima de 2 linhas de legenda (169 px)
PAUSA=1.1  # segundos de respiro após cada fala
ESPERA_INICIO=0.8  # s entre a página pronta (capa já pintada) e o início da linha do tempo

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

from tts import sintetiza as _tts
def sintetiza(texto, wav, voz=None): return _tts(texto, wav, voz)

CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#FFFAF0;font-family:Figtree,sans-serif;color:#1F1235}}
.cena{{position:absolute;inset:0;opacity:0;transition:opacity .5s}} .cena.on{{opacity:1}}
.topo{{position:absolute;top:22px;left:32px;width:220px;z-index:5}}
.topo svg{{width:220px;height:auto}}
.tela{{position:absolute;left:32px;top:84px;width:{W-64}px;height:{TELA_H}px;border-radius:14px;overflow:hidden;background:#fff;border:1px solid #DCD2EC;box-shadow:0 18px 40px -24px rgba(31,18,53,.45)}}
.tela img{{position:absolute;left:0;top:0;transform-origin:0 0;transition:transform 1.6s cubic-bezier(.4,0,.2,1)}}
.legenda{{position:absolute;left:32px;right:32px;bottom:{BARRA_B}px;height:{BARRA_H}px;background:#3B1F5E;color:#fff;border-radius:14px;display:flex;align-items:center;padding:0 28px;font-size:28px;font-weight:600;letter-spacing:-.01em;z-index:6}}
.legenda b{{background:#FFC83D;color:#3B1F5E;border-radius:999px;padding:4px 14px;font-size:16px;margin-right:18px;font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:0;white-space:nowrap}}
.capa{{background:#3B1F5E;color:#fff;padding:70px 90px}} .capa .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:76px;line-height:1.02;letter-spacing:-.02em;margin-top:118px;max-width:1000px}}
.capa .t em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}} .capa .s{{font-size:30px;color:#D9C8F5;margin-top:22px}}
.capa .k{{font-family:'Bricolage Grotesque';font-weight:600;font-size:22px;color:#FFC83D;position:absolute;left:90px;bottom:{KICKER_B}px;margin:0}}
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
            partes.append(f'<div class="cena capa{" on" if i==0 else ""}" id="c{i}"><div class="simb">{SIMB}</div><div class="t"><em>Aula {rot["n"]}</em><br>{rot["titulo"]}</div><div class="s">{rot["sub"]}</div><div class="k">Kit de Gestão para Médicos · Seu Sócio Gestor</div></div>')
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
const durs={json.dumps(durs)}; const W={W-64}, H={TELA_H};
function foco(img){{ const [fx,fy,fw,fh]=img.dataset.foco.split(',').map(Number); const nw=img.naturalWidth, nh=img.naturalHeight;
  const base=W/nw; // escala para caber na largura
  const sx=W/(nw*fw), sy=H/(nh*fh); const s=Math.min(sx,sy, base*3.2);
  let tx=-fx*nw*s + (W-fw*nw*s)/2, ty=-fy*nh*s + (H-fh*nh*s)/2;
  // sem faixa em branco: se a imagem cobre o quadro, mantém dentro; se não cobre, encosta em cima/esquerda
  tx = nw*s>=W ? Math.min(0,Math.max(W-nw*s,tx)) : 0;
  ty = nh*s>=H ? Math.min(0,Math.max(H-nh*s,ty)) : 0;
  return `translate(${{tx}}px, ${{ty}}px) scale(${{s}})`; }}
document.querySelectorAll('.tela img').forEach(img=>{{ const nw=img.naturalWidth||1650; img.style.transform=`scale(${{W/nw}})`; }});
// a capa (c0) já nasce visível no HTML; a linha do tempo só começa quando o gravador chama iniciar()
window.iniciar=function(){{ let t=0; durs.forEach((d,i)=>{{ setTimeout(()=>{{ document.querySelectorAll('.cena.on').forEach(e=>e.classList.remove('on')); const c=document.getElementById('c'+i); c.classList.add('on');
   const img=c.querySelector('.tela img'); if(img){{ img.style.transform=`scale(${{W/img.naturalWidth}})`; setTimeout(()=>{{img.style.transform=foco(img);}},900); }} }}, t*1000); t+=d; }});
setTimeout(()=>{{document.title='FIM'}}, t*1000+300); }};
requestAnimationFrame(()=>requestAnimationFrame(()=>{{document.title='PRONTO';}}));
"""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(partes)}<script>window.addEventListener("load",()=>{{ {js} }});</script></body></html>'

def transicoes(webm, fps=20, lag=6):
    """Instantes (s) em que a cena troca na gravação: mede, na faixa da barra roxa de legenda (que muda de texto
    a cada cena e não se mexe durante o zoom), a fração de pixels que mudou em relação a `lag` quadros antes."""
    raw=subprocess.run(['ffmpeg','-loglevel','error','-i',str(webm),'-vf',f'fps={fps},crop={W-64}:{BARRA_H}:32:{H-BARRA_B-BARRA_H},scale=304:16','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True,check=True).stdout
    F=304*16; fr=[raw[i:i+F] for i in range(0,len(raw)-F+1,F)]
    d=[0.0]*lag+[sum(1 for a,b in zip(fr[i],fr[i-lag]) if abs(a-b)>60)/F for i in range(lag,len(fr))]
    out=[]; i=0
    while i<len(d):
        if d[i]>0.01:
            j=i
            while j<len(d) and d[j]>0.01: j+=1
            out.append((i-lag+3)/fps); i=j+fps   # o limiar dispara ~3 quadros depois do começo do fade
        else: i+=1
    return [t for t in out if t>3.0]   # antes de 3 s só há o carregamento da página (capa dura mais que isso)

def sincronia(webm, durs):
    """A gravação do Chromium (recordVideo) corre ~2% mais lenta que o relógio da página, e não de modo uniforme.
    Mede no webm o instante de cada troca de cena e devolve um filtro que reescala cada trecho para a troca cair
    exatamente onde a narração espera (trim + setpts por cena + concat). Se não achar todas as trocas, cai na
    correção linear pela capa e pela cena final; sem marcos, devolve '' (sem correção)."""
    esp=[]; t=0
    for d in durs[:-1]: t+=d; esp.append(t)
    med=transicoes(webm)
    if len(med)==len(esp):
        kg=(med[-1]-med[0])/(esp[-1]-esp[0]); ini=max(0.0,med[0]-esp[0]*kg)
        pontos=[ini]+med; segs=[]
        for i in range(len(durs)):
            a=pontos[i]; b=pontos[i+1] if i+1<len(pontos) else None
            k=(durs[i]/(b-a)) if b else 1/kg
            segs.append(f"[0:v]trim=start={a:.3f}"+(f":end={b:.3f}" if b else '')+f",setpts=(PTS-STARTPTS)*{k:.5f}[s{i}]")
        desv=max(abs((m-med[0])/kg-(e-esp[0])) for m,e in zip(med,esp))
        print(f'  sincronia: {len(med)} trocas de cena medidas; início em {ini:.2f}s; fator médio {1/kg:.4f}; maior desvio antes da correção {desv:.2f}s')
        return ';'.join(segs)+';'+''.join(f'[s{i}]' for i in range(len(durs)))+f'concat=n={len(durs)}:v=1:a=0,'
    raw=subprocess.run(['ffmpeg','-loglevel','error','-i',str(webm),'-vf','fps=10,crop=2:2:20:20','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout
    roxo=[raw[i]<128 for i in range(0,len(raw)-11,12)]   # canal R baixo = fundo roxo (#3B1F5E) da capa/fim
    t0=next((i for i in range(0,min(100,len(roxo))) if roxo[i]),None)
    if len(roxo)<20 or t0 is None: return '[0:v]null,'
    t1=next((i for i in range(t0,len(roxo)) if not roxo[i]),None)
    t2=next((i for i in range(len(roxo)-1,0,-1) if not roxo[i]),None)
    if t1 is None or t2 is None or t2<=t1: return '[0:v]null,'
    t1/=10; t2=(t2+1)/10; e1=durs[0]+0.25; e2=sum(durs[:-1])+0.25
    k=(e2-e1)/(t2-t1); ini=max(0.0,t1-e1/k)
    print(f'  sincronia (linear, achou {len(med)} de {len(esp)} trocas): capa termina em {t1:.1f}s (esperado {e1:.1f}), fim começa em {t2:.1f}s (esperado {e2:.1f}); fator {k:.4f}')
    return f'[0:v]trim=start={ini:.3f},setpts=(PTS-STARTPTS)*{k:.5f},'

def normaliza(entrada, saida, lufs=-16.0, tp=-1.5):
    """Normaliza a narração em duas passagens (EBU R128): média em torno de `lufs`, pico real ≤ `tp` dBTP (o AAC sobe ~0,3 dB: −1,5 no wav dá ≈ −1 dBTP no mp4)."""
    alvo=f'I={lufs}:TP={tp}:LRA=11'
    r=subprocess.run(['ffmpeg','-y','-loglevel','info','-i',str(entrada),'-af',f'loudnorm={alvo}:print_format=json','-f','null','-'],capture_output=True,text=True)
    j=json.loads(r.stderr[r.stderr.rfind('{'):r.stderr.rfind('}')+1])
    med=(f":measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}"
         f":offset={j['target_offset']}:linear=true")
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(entrada),'-af',f'loudnorm={alvo}{med}','-ar','44100','-ac','1',str(saida)],check=True)

def build(nome):
    rot=ROTEIROS[nome]; out=ROOT/'videos'/nome; out.mkdir(parents=True,exist_ok=True)
    cenas=rot['cenas']; wavs=[]
    (ROOT/'entrega'/'videos').mkdir(parents=True,exist_ok=True)
    for i,c in enumerate(cenas):
        w=out/f'fala{i}.wav'; d=sintetiza(c['fala'],w,c.get('voz')); c['dur']=round(d+PAUSA,2); wavs.append((w,c['dur']))
    total=sum(c['dur'] for c in cenas)
    (out/'video.html').write_text(html_video(nome,rot,cenas))
    # áudio: cada fala seguida de silêncio até completar a duração da cena
    lista=out/'audio.txt'; linhas=[]
    for i,(w,d) in enumerate(wavs):
        p=out/f'cena{i}.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(w),'-af',f'apad=whole_dur={d}','-ar','44100','-ac','1',str(p)],check=True); linhas.append(f"file '{p.name}'")
    lista.write_text('\n'.join(linhas)+'\n')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(lista),'-c','copy',str(out/'narracao_bruta.wav')],check=True)
    normaliza(out/'narracao_bruta.wav', out/'narracao.wav')
    # vídeo: gravação do Chromium
    rec=S/'gravar.js'
    rec.write_text("""const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [html,dir,total]=process.argv.slice(2);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox','--disable-gpu']});
const ctx=await b.newContext({viewport:{width:%d,height:%d},recordVideo:{dir:dir,size:{width:%d,height:%d}}});
const p=await ctx.newPage(); await p.goto('file://'+html); await p.waitForFunction(()=>document.title==='PRONTO',null,{timeout:60000});
await p.waitForTimeout(%d); await p.evaluate(()=>window.iniciar()); await p.waitForFunction(()=>document.title==='FIM',null,{timeout:(Number(total)+15)*1000});
const v=p.video(); await ctx.close(); const f=await v.path(); fs.renameSync(f,path.join(dir,'gravacao.webm')); await b.close(); console.log('gravado');})();""" % (W,H,W,H,int(ESPERA_INICIO*1000)))
    subprocess.run(['node',str(rec),str(out/'video.html'),str(out),str(total)],check=True,env={**dict(__import__('os').environ),'NODE_PATH':str(S/'pw'/'node_modules')})
    # junta: corta o vídeo na duração do áudio, codifica mp4
    final=ROOT/'entrega'/'videos'/f'aula-{nome}.mp4'
    # legendas .srt (cues curtos) escritas antes do mux, e gravadas na imagem acima da barra roxa
    import sys as _s; _s.path.insert(0,str(ROOT.parent)); import legendas as _lg
    srt_path=ROOT/'entrega'/'videos'/f'aula-{nome}.srt'; srt=_lg.cues(cenas,PAUSA); srt_path.write_text(srt)
    probs=_lg.confere(srt)
    if probs: raise SystemExit(f'{nome}: legenda fora da regra: '+'; '.join(probs))
    mux(nome, cenas, srt_path, final)
    print(nome, f'{total:.1f}s', final)

def mux(nome, cenas, srt_path, final):
    """Junta gravação + narração já prontas em videos/<nome>/ (corrige a sincronia e grava a legenda)."""
    out=ROOT/'videos'/nome
    import sys as _s; _s.path.insert(0,str(ROOT.parent)); import legendas as _lg
    fc=sincronia(out/'gravacao.webm',durs=[c['dur'] for c in cenas])+_lg.filtro(srt_path,LEG_MARGEM,LEG_TAM,H)+'[v]'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(out/'gravacao.webm'),'-i',str(out/'narracao.wav'),'-filter_complex',fc,'-map','[v]','-map','1:a','-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(final)],check=True)

def remux(nome):
    """Refaz só a junção (sincronia + legenda + mux) de uma aula já gravada, lendo as durações dos cena*.wav."""
    out=ROOT/'videos'/nome; cenas=[]
    for w in sorted(out.glob('cena*.wav'),key=lambda p:int(p.stem[4:])):
        with wave.open(str(w)) as f: cenas.append({'dur':round(f.getnframes()/f.getframerate(),2)})
    mux(nome, cenas, ROOT/'entrega'/'videos'/f'aula-{nome}.srt', ROOT/'entrega'/'videos'/f'aula-{nome}.mp4')
    print(nome,'remux ok')

if __name__=='__main__':
    nomes=sys.argv[1:] or list(ROTEIROS)
    for n in nomes: build(n)

def build_all(roteiros, nomes=None):
    global ROTEIROS
    ROTEIROS=roteiros
    for n in (nomes or list(roteiros)): build(n)
