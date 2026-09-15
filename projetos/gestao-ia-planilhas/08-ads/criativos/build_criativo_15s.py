#!/usr/bin/env python3
"""Criativo curto de 15 s (9:16, 1080×1920) por produto, para Reels/Stories/ads.
Versão condensada do build_criativo_venda.py: 4 cenas (dor → solução com mockup animado → o que vem dentro →
preço + CTA), narração ≤ ~40 palavras (Piper, provisório até a chave do Google TTS), legenda gravada na imagem
(muita gente vê sem som), logo no topo, preço no último frame por ≥ 2,5 s. Áudio = narração + silêncio (sem trilha).
Uso: python3 build_criativo_15s.py <essencial|completo|advogados|medicos>
Saída: <produto>-15s-9x16.mp4 + .srt + frames-<produto>-15s.jpg (1 frame por segundo)."""
import sys, json, subprocess, pathlib, base64, os, html as _html
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]/'produto'/'kit-completo'))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]/'produto'))
import video_engine as V, legendas as LG
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parents[1]
W,H=1080,1920; PAUSA=0.3; DUR_MIN,DUR_MAX=14.0,16.0
PROD=(sys.argv[1] if len(sys.argv)>1 else 'essencial')
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
esc=lambda x: _html.escape(str(x), quote=False)
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text(); LOGOB=(PROJ/'03-marca'/'logo'/'logo-branco.svg').read_text()
FONTS=PROJ/'site'/'public'/'assets'/'fonts'; MOCK=ROOT/f'{PROD}-produto-hero-1600x1000.png'
# Legenda gravada: base do texto a 360 px do rodapé (acima da UI do Reels), corpo 48 px, até 2 linhas de ~34 caracteres.
LEG_MARGEM,LEG_TAM=360,48; LG.LINHA=34; LG.MAXC=68
CFG={
 'essencial':dict(
  dor=dict(fala='Planilha, relatório e slides. Toda semana, do zero?',min=3.5,h='Toda semana, <em>tudo do zero?</em>',itens=['Segunda: a planilha','Dia 30: o relatório','Véspera: os slides']),
  sol=dict(fala='O kit já vem pronto: você preenche, a IA escreve, você revisa.',min=4.5,h='Já vem pronto. <em>Você só preenche.</em>',ctx='Kit IA no Trabalho · Essencial · tela real da planilha',chips=['Preencher','Perguntar','Entregar'],num=True),
  prova=dict(fala='Três planilhas, quarenta prompts, manual e vídeos.',min=3.5,selos=['3 planilhas prontas','40 prompts de IA','Mini-manual em PDF','3 vídeos curtos']),
  fim=dict(fala='Trinta e sete reais, uma vez. Comece hoje.',min=3.5,tt='Kit IA no Trabalho <em>Essencial</em>',preco='Comprar por R$ 37',nota='3 planilhas · 40 prompts · manual e vídeos<br>Pix ou cartão · acesso imediato · 7 dias para desistir')),
 'completo':dict(
  dor=dict(fala='Relatório, projeto, reunião. E você monta tudo do zero?',min=3.5,h='Tudo do zero, <em>de novo?</em>',itens=['Segunda: "um relatório rápido"','Quarta: "como está o projeto?"','Sexta: os slides da reunião']),
  sol=dict(fala='O Kit Completo: dez planilhas prontas e a IA escreve com os seus números.',min=4.5,h='Com método. <em>Não no braço.</em>',ctx='Kit IA no Trabalho · Completo · tela real da planilha',chips=['Estruturar','Preencher','Perguntar','Entregar'],num=True),
  prova=dict(fala='Oitenta prompts, oito aulas e modelos de slides.',min=3.5,selos=['10 planilhas prontas','80 prompts de IA','8 aulas curtas','3 modelos de slides']),
  fim=dict(fala='Cento e noventa e sete reais. Comece hoje.',min=3.5,tt='Kit IA no Trabalho <em>Completo</em>',preco='Comprar por R$ 197',nota='10 planilhas · 80 prompts · 8 aulas · 3 modelos<br>Pix ou 12× · acesso imediato · 7 dias para desistir')),
 'medicos':dict(
  dor=dict(fala='Você atende o dia inteiro. E a clínica?',min=3.5,h='Você atende. <em>E a clínica?</em>',itens=['Agenda com buraco, sem medir','Convênio aceito sem calcular','Imposto junto com o 13º']),
  sol=dict(fala='Vinte planilhas prontas para a clínica: agenda, preço, caixa e convênios.',min=4.5,h='Cinco núcleos. <em>Uma rotina.</em>',ctx='Kit de Gestão para Médicos · tela real',chips=['Agenda','Preço','Caixa','Recebíveis','Painel'],num=False),
  prova=dict(fala='Quarenta e um prompts, oito aulas e modelos de slides.',min=3.5,selos=['20 planilhas prontas','41 prompts de IA','8 aulas curtas','3 modelos de slides']),
  fim=dict(fala='Seiscentos e noventa e sete reais. Comece hoje.',min=3.5,tt='Kit de Gestão <em>para Médicos</em>',preco='Comprar por R$ 697',nota='20 planilhas · 41 prompts · 8 aulas · 3 modelos<br>Pix ou 12× · acesso imediato · 7 dias para desistir')),
 'advogados':dict(
  dor=dict(fala='Você advoga o dia inteiro. E o escritório?',min=3.5,h='Você advoga. <em>E o escritório?</em>',itens=['Prazo: caderno, celular, e-mail','"Quanto fica?" de cabeça','Imposto junto com o 13º']),
  sol=dict(fala='Vinte planilhas prontas para o escritório: prazos, honorários e caixa.',min=4.5,h='Cinco núcleos. <em>Uma rotina.</em>',ctx='Kit de Gestão para Advogados · tela real',chips=['Prazos','Honorários','Caixa','Carteira','Painel'],num=False),
  prova=dict(fala='Quarenta prompts, oito aulas e modelos de slides.',min=3.5,selos=['20 planilhas prontas','40 prompts de IA','8 aulas curtas','3 modelos de slides']),
  fim=dict(fala='Quatrocentos e noventa e sete reais. Comece hoje.',min=3.5,tt='Kit de Gestão <em>para Advogados</em>',preco='Comprar por R$ 497',nota='20 planilhas · 40 prompts · 8 aulas · 3 modelos<br>Pix ou 12× · acesso imediato · 7 dias para desistir')),
}
C=CFG[PROD]; CENAS=[dict(tipo=k,**C[k]) for k in ('dor','sol','prova','fim')]
# Zonas verticais: logo 140 · conteúdo 280–1400 · legenda gravada ~1450–1560 · rodapé 1620+ (pode ficar sob a UI do app)
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#FFFAF0;font-family:Figtree,sans-serif;color:#1F1235}}
.cena{{position:absolute;inset:0;opacity:0;transition:opacity .3s;background:#FFFAF0}} .cena.on{{opacity:1}}
.uva{{background:#3B1F5E;color:#fff}} .lav{{background:#F3EEFB}}
.topo{{position:absolute;top:140px;left:60px;width:300px;z-index:5}} .topo svg{{width:300px;height:auto}}
.t{{font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:-.02em;line-height:1.02}}
.h{{position:absolute;left:60px;right:60px;top:290px;font-size:96px;color:#3B1F5E}} .uva .h{{color:#fff}}
.h em{{font-style:normal;color:#FFC83D}} .h em.esc{{background:linear-gradient(transparent 62%,#FFC83D 62%);color:inherit}}
/* faixa uva atrás da legenda gravada nas cenas claras (legenda branca precisa de fundo escuro) */
.faixa{{position:absolute;left:60px;right:60px;top:1420px;height:176px;border-radius:24px;background:#3B1F5E}}
/* dor: itens que entram um a um */
.dor .lista{{position:absolute;left:60px;right:60px;top:600px;list-style:none;margin:0;padding:0}}
.dor .lista li{{opacity:0;transform:translateY(24px);transition:all .45s;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.2);border-radius:24px;padding:38px 40px 38px 124px;font-size:52px;font-weight:600;margin-bottom:24px;position:relative;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:clip}}
.dor .lista li::before{{content:'✕';position:absolute;left:40px;top:38px;width:60px;height:60px;border-radius:50%;background:#FBE4E4;color:#C8402E;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700}}
.dor .lista li.on{{opacity:1;transform:none}}
/* solução: mockup animado (entra de baixo e aproxima devagar) + chips do mecanismo */
.sol .ctx{{position:absolute;left:60px;right:60px;top:510px;font-family:'IBM Plex Mono';font-size:28px;color:#7A5AA8}}
.sol .quadro{{position:absolute;left:40px;right:40px;top:566px;height:640px;border-radius:32px;background:#F3EEFB;overflow:hidden}}
.sol .mock{{position:absolute;left:10px;top:8px;width:980px;opacity:0;transform:translateY(80px) scale(.94);transition:opacity .7s,transform 4.6s cubic-bezier(.2,.6,.2,1)}} .sol .mock.on{{opacity:1;transform:translateY(0) scale(1.04)}} .sol .mock img{{width:100%;display:block}}
.selo{{position:absolute;right:56px;top:536px;background:#FFC83D;color:#3B1F5E;border-radius:999px;padding:14px 28px;font-family:'Bricolage Grotesque';font-weight:800;font-size:32px;z-index:6;transform:rotate(-4deg);white-space:nowrap}}
.sol .chips{{position:absolute;left:40px;right:40px;top:1232px;display:flex;flex-wrap:wrap;gap:16px;justify-content:center}}
.sol .chips span{{display:inline-flex;align-items:center;gap:14px;white-space:nowrap;background:#fff;border:2px solid #DCD2EC;border-radius:999px;padding:14px 30px 14px 16px;font-family:'Bricolage Grotesque';font-weight:700;font-size:34px;color:#3B1F5E;opacity:.35;transition:all .4s}}
.sol .chips span.sn{{padding-left:30px}} .sol .chips span.on{{opacity:1;border-color:#FFC83D;background:#FFF6D6}}
.sol .chips i{{width:48px;height:48px;border-radius:50%;background:#FFC83D;color:#3B1F5E;font-style:normal;font-weight:800;font-size:28px;display:inline-flex;align-items:center;justify-content:center;flex:none}}
/* prova: lista de selos grandes */
.prova .h{{font-size:84px}}
.prova .selos{{position:absolute;left:60px;right:60px;top:470px;list-style:none;margin:0;padding:0}}
.prova .selos li{{background:#fff;border:2px solid #DCD2EC;border-radius:24px;padding:32px 40px 32px 130px;font-family:'Bricolage Grotesque';font-weight:700;font-size:50px;color:#3B1F5E;margin-bottom:22px;position:relative;opacity:0;transform:translateY(20px);transition:all .4s;white-space:nowrap}}
.prova .selos li::before{{content:'';position:absolute;left:40px;top:30px;width:64px;height:64px;border-radius:50%;background:#FFC83D url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M4 9.5l3 3 7-7' fill='none' stroke='%233B1F5E' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/60% no-repeat}}
.prova .selos li.on{{opacity:1;transform:none}}
.prova .onde{{position:absolute;left:60px;right:60px;top:1150px;font-size:38px;line-height:1.3;color:#5A4A78;text-align:center}}
.prova .tag{{position:absolute;left:60px;right:60px;top:1270px;text-align:center}} .prova .tag span{{display:inline-block;white-space:nowrap;background:#3B1F5E;color:#fff;border-radius:999px;padding:16px 34px;font-family:'Bricolage Grotesque';font-weight:700;font-size:32px}}
/* fim: título, mockup, preço (visível desde o primeiro frame da cena), nota, site */
.fim .tt{{position:absolute;top:280px;left:60px;right:60px;font-size:84px}} .fim .tt em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%);color:#fff}}
.fim .mock{{position:absolute;left:90px;width:900px;top:470px;opacity:0;transform:translateY(60px);transition:all .8s cubic-bezier(.2,.7,.2,1)}} .fim .mock.on{{opacity:1;transform:none}} .fim .mock img{{width:100%;display:block}}
.fim .preco{{position:absolute;top:1075px;left:80px;right:80px;background:#FFC83D;color:#3B1F5E;border-radius:999px;height:150px;display:flex;align-items:center;justify-content:center;font-family:'Bricolage Grotesque';font-weight:800;font-size:64px;white-space:nowrap;animation:pulsa 1.6s ease-in-out infinite}}
@keyframes pulsa{{50%{{transform:scale(1.03)}}}}
.fim .nota{{position:absolute;top:1262px;left:60px;right:60px;font-family:'IBM Plex Mono';font-size:28px;line-height:1.5;color:#D9C8F5;text-align:center}}
.fim .site{{position:absolute;top:1620px;left:60px;right:60px;font-family:'Bricolage Grotesque';font-weight:600;font-size:34px;color:#FFC83D;text-align:center}}
"""
def html(cenas):
    partes=[]; extra=[]
    for i,c in enumerate(cenas):
        if c['tipo']=='dor':
            its=''.join(f'<li id="d{k}">{esc(x)}</li>' for k,x in enumerate(c['itens']))
            partes.append(f'<div class="cena uva dor" id="c{i}"><div class="topo">{LOGOB}</div><div class="t h">{c["h"]}</div><ul class="lista">{its}</ul></div>')
            extra.append(f'[0.3,1.1,1.9].forEach((s,k)=>setTimeout(()=>document.getElementById("d"+k).classList.add("on"),(T{i}+s)*1000));')
        elif c['tipo']=='sol':
            n=len(c['chips']); passo=(c['dur']-0.9)/n
            chips=''.join(f'<span id="ch{k}" class="{"" if c["num"] else "sn"}">{f"<i>{k+1}</i>" if c["num"] else ""}{esc(x)}</span>' for k,x in enumerate(c['chips']))
            partes.append(f'<div class="cena sol" id="c{i}"><div class="topo">{LOGO}</div><div class="t h">{c["h"]}</div><div class="ctx">{esc(c["ctx"])}</div><div class="selo">telas reais</div><div class="quadro"><div class="mock" id="mock{i}"><img src="data:image/png;base64,{b64(MOCK)}"></div></div><div class="chips">{chips}</div><div class="faixa"></div></div>')
            ts=[round(0.6+k*passo,2) for k in range(n)]
            extra.append(f'setTimeout(()=>document.getElementById("mock{i}").classList.add("on"),(T{i}+0.15)*1000); {json.dumps(ts)}.forEach((s,k)=>setTimeout(()=>document.getElementById("ch"+k).classList.add("on"),(T{i}+s)*1000));')
        elif c['tipo']=='prova':
            selos=''.join(f'<li id="s{k}">{esc(x)}</li>' for k,x in enumerate(c['selos']))
            partes.append(f'<div class="cena lav prova" id="c{i}"><div class="topo">{LOGO}</div><div class="t h">O que vem dentro</div><ul class="selos">{selos}</ul><div class="onde">Abre no Excel, no Google Planilhas<br>e no celular. Arquivos seus, para sempre.</div><div class="tag"><span>Pagamento único · sem mensalidade</span></div><div class="faixa"></div></div>')
            extra.append(f'[0.15,0.5,0.85,1.2].forEach((s,k)=>setTimeout(()=>document.getElementById("s"+k).classList.add("on"),(T{i}+s)*1000));')
        elif c['tipo']=='fim':
            partes.append(f'<div class="cena uva fim" id="c{i}"><div class="topo">{LOGOB}</div><div class="t tt">{c["tt"]}</div><div class="mock" id="mock{i}"><img src="data:image/png;base64,{b64(MOCK)}"></div><div class="preco">{esc(c["preco"])}</div><div class="nota">{c["nota"]}</div><div class="site">seusociogestor.com.br</div></div>')
            extra.append(f'setTimeout(()=>document.getElementById("mock{i}").classList.add("on"),(T{i}+0.15)*1000);')
    durs=[c['dur'] for c in cenas]; starts=[]; t=0
    for d in durs: starts.append(round(t,2)); t+=d
    consts=''.join(f'const T{i}={s};' for i,s in enumerate(starts))
    js=f"""const durs={json.dumps(durs)}; {consts}
let t=0; durs.forEach((d,i)=>{{ setTimeout(()=>{{ document.querySelectorAll('.cena.on').forEach(e=>e.classList.remove('on')); document.getElementById('c'+i).classList.add('on'); }}, t*1000); t+=d; }});
{''.join(extra)}
setTimeout(()=>{{document.title='FIM'}}, t*1000+300);"""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(partes)}<script>window.addEventListener("load",()=>{{ {js} }});</script></body></html>'
out=ROOT/f'trabalho-15s-{PROD}'; out.mkdir(exist_ok=True); wavs=[]
palavras=sum(len(c['fala'].split()) for c in CENAS)
for i,c in enumerate(CENAS):
    w=out/f'fala{i}.wav'; d=V.sintetiza(c['fala'],w); c['dur']=round(max(d+PAUSA,c['min']),2); wavs.append(w)
total=sum(c['dur'] for c in CENAS)
if total<DUR_MIN: CENAS[-1]['dur']=round(CENAS[-1]['dur']+DUR_MIN-total,2); total=sum(c['dur'] for c in CENAS)   # preço fica mais tempo na tela
if total>DUR_MAX: print(f'AVISO: {total:.2f}s passa de {DUR_MAX}s; encurte a narração', file=sys.stderr)
(out/'video.html').write_text(html(CENAS))
linhas=[]
for i,w in enumerate(wavs):
    p=out/f'cena{i}.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(w),'-af',f'apad=whole_dur={CENAS[i]["dur"]}','-ar','44100','-ac','1',str(p)],check=True); linhas.append(f"file '{p.name}'")
(out/'audio.txt').write_text('\n'.join(linhas)+'\n')
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(out/'audio.txt'),'-c','copy',str(out/'narracao.wav')],check=True)
subprocess.run(['node',str(ROOT/'trabalho'/'gravar.js'),str(out/'video.html'),str(out),str(total)],check=True,env={**os.environ,'NODE_PATH':str(V.S/'pw'/'node_modules')})
srt=ROOT/f'{PROD}-15s-9x16.srt'; srt.write_text(LG.cues(CENAS,0))   # cues até o fim da cena: legenda sempre visível
final=ROOT/f'{PROD}-15s-9x16.mp4'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(out/'gravacao.webm'),'-i',str(out/'narracao.wav'),'-map','0:v','-map','1:a','-vf',LG.filtro(srt,LEG_MARGEM,LEG_TAM,H),'-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',str(final)],check=True)
frames=ROOT/f'frames-{PROD}-15s.jpg'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(final),'-vf','fps=1,scale=-1:800,tile=8x2:padding=6:color=white','-frames:v','1','-q:v','3',str(frames)],check=True)
print(f'{PROD}: {total:.2f}s, {palavras} palavras, cenas={[c["dur"] for c in CENAS]}', final, srt, frames)
