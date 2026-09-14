#!/usr/bin/env python3
"""Demonstrações em vídeo do Kit Essencial: telas reais + zoom + legenda + narração (Piper, pt-BR).
Uso: python3 build_videos.py [nome]  (sem nome = todos). Saída em entrega/videos/*.mp4 + .srt
Renderização determinística: o HTML expõe seek(t) e o Node tira um screenshot por quadro (30 fps),
então vídeo e narração ficam sincronizados sem depender do relógio do navegador."""
import json, wave, subprocess, pathlib, sys, base64, shutil
ROOT=pathlib.Path(__file__).resolve().parent
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
VOZ=S/'voz'/'pt_BR-faber-medium.onnx'
FONTS=ROOT.parents[1]/'site'/'public'/'assets'/'fonts'
LOGO=(ROOT.parents[1]/'03-marca'/'logo'/'logo-horizontal.svg').read_text()
W,H=1280,720
FPS=30
PAUSA=0.9  # segundos de respiro após cada fala
# layout vertical: tela (topo 84) · faixa da legenda gravada (FAIXA) · barra roxa (BARRA_H) · rodapé (BARRA_B)
BARRA_H,BARRA_B,FAIXA=64,18,74
TELA_H=H-84-(BARRA_H+BARRA_B+FAIXA)  # 480
LEG_MARGEM,LEG_TAM=BARRA_H+BARRA_B+6,28  # legenda gravada: base 6 px acima da barra, corpo 28 px

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

ROTEIROS={
 '01-semana-organizada': {
   'titulo':'Semana Organizada',
   'sub':'tarefas, prioridades e o que fazer primeiro',
   'cenas':[
    {'tipo':'capa','fala':'Esta é a Semana Organizada, a primeira planilha do Kit IA no Trabalho. Em quinze minutos você começa.'},
    {'tipo':'tela','img':'docs/tela-semana-tarefas.png','foco':[0.055,0.07,0.665,0.52],'fala':'Na aba Tarefas, você preenche só as células amarelas: nome da tarefa, projeto, responsável, prazo, impacto e urgência de um a três, horas e status.','legenda':'Preencha só as células amarelas'},
    {'tipo':'tela','img':'docs/tela-semana-tarefas.png','foco':[0.235,0.068,0.685,0.57],'fala':'Prioridade, dias para o prazo e situação são calculados na hora. Tarefa atrasada fica vermelha; a de hoje, amarela; o que está feito, cinza.','legenda':'Prioridade e situação: calculadas sozinhas'},
    {'tipo':'tela','img':'docs/tela-semana-hoje.png','foco':[0,0.062,1,0.44],'fala':'Na aba Hoje não se preenche nada. O painel mostra atrasadas, para hoje, esta semana e o total em aberto, e a lista do que fazer primeiro, já na ordem certa.','legenda':'Aba Hoje: o que fazer primeiro, na ordem'},
    {'tipo':'tela','img':'docs/tela-semana-hoje.png','foco':[0,0.519,0.897,0.395],'fala':'Logo abaixo, a carga dos próximos sete dias contra a sua capacidade, com um aviso quando o dia não cabe, e o resumo por pessoa.','legenda':'Carga dos 7 dias e resumo por pessoa'},
    {'tipo':'card','titulo':'Prompt Organizar 01','texto':'Cole a lista bagunçada de uma reunião ou e-mail. A IA devolve as tarefas no formato da planilha: nome, projeto, responsável, prazo, impacto, urgência e horas. Você cola e pronto.','fala':'Com o prompt Organizar zero um da biblioteca, a IA transforma uma lista bagunçada nas linhas da planilha. Você cola e pronto.','legenda':'Da lista bagunçada à planilha, com a IA'},
    {'tipo':'fim','fala':'Todo dia, marque o que foi feito. Toda sexta, revise os prazos. O mini-manual mostra o passo a passo.'},
   ]},
 '02-relatorio-mensal-pronto': {
   'titulo':'Relatório Mensal Pronto',
   'sub':'indicadores, painel, gráfico e resumo para a IA',
   'cenas':[
    {'tipo':'capa','fala':'Esta é a Relatório Mensal Pronto. Você digita os indicadores; ela escreve o resumo do mês.'},
    {'tipo':'tela','img':'docs/tela-relatorio-painel.png','foco':[0.007,0.045,0.782,0.29],'fala':'Na aba Indicadores você cadastra até doze indicadores, com meta e se maior é melhor, e digita o valor de cada mês. No Painel, cada um aparece com o mês, o mês anterior, a variação, a meta e a situação: verde no alvo, vermelho fora.','legenda':'Painel: variação, meta e situação de cada indicador'},
    {'tipo':'tela','img':'docs/tela-relatorio-painel.png','foco':[0.007,0.765,0.62,0.235],'fala':'Escolha um indicador e o gráfico mostra a evolução no ano, com a linha da meta tracejada.','legenda':'Gráfico de evolução com a meta'},
    {'tipo':'tela','img':'docs/tela-relatorio-resumo.png','foco':[0,0.115,0.328,0.267],'foco2':[0,0.58,0.328,0.267],'fala':'A aba Resumo escreve sozinha as frases do mês: cada indicador com valor, variação e situação, e os destaques automáticos, como maior alta e maior queda.','legenda':'Resumo: as frases do mês, escritas sozinhas'},
    {'tipo':'card','titulo':'Prompt Escrever 01 · relatório executivo','texto':'Copie o bloco único da aba Resumo, cole no prompt com os seus comentários sobre o porquê dos números e receba o relatório de 300 palavras. O prompt Apresentar 01 faz o roteiro dos 8 slides.','fala':'Copie o bloco único, cole no prompt Escrever zero um com os seus comentários, e a IA devolve o relatório pronto para revisar. O prompt Apresentar zero um monta o roteiro dos oito slides.','legenda':'Do resumo ao relatório e aos slides'},
    {'tipo':'fim','fala':'Todo mês, digite os valores novos e troque o mês em Config. O resto se refaz sozinho.'},
   ]},
 '03-ganhos-e-gastos': {
   'titulo':'Ganhos e Gastos',
   'sub':'quanto entrou, quanto saiu, quanto sobrou',
   'cenas':[
    {'tipo':'capa','fala':'Esta é a Ganhos e Gastos. Serve para você, para o seu negócio ou para os dois.'},
    {'tipo':'tela','img':'docs/tela-ganhos-lancamentos.png','foco':[0.006,0.085,0.781,0.62],'fala':'Na aba Lançamentos, uma linha por entrada ou saída: data, tipo, categoria, descrição, valor, forma de pagamento e se já foi pago. Lance na hora ou uma vez por semana.','legenda':'Uma linha por entrada ou saída'},
    {'tipo':'tela','img':'docs/tela-ganhos-painel.png','foco':[0,0,0.897,0.29],'fala':'No Painel, escolha o mês e veja quanto entrou, quanto saiu, quanto sobrou, o saldo acumulado e o que ainda falta pagar.','legenda':'Entrou, saiu, sobrou, saldo e a pagar'},
    {'tipo':'tela','img':'docs/tela-ganhos-painel.png','foco':[0.007,0.111,0.616,0.2],'foco2':[0.007,0.231,0.821,0.267],'fala':'A reserva mostra quantos meses de despesa o seu saldo cobre e se você está no caminho da meta. Depois, para onde o dinheiro foi, categoria por categoria, com a barra e o mês anterior ao lado.','legenda':'Reserva em meses e para onde foi o dinheiro'},
    {'tipo':'tela','img':'docs/tela-ganhos-painel.png','foco':[0,0.675,1,0.325],'fala':'No fim, o ano mês a mês: entrou, saiu, sobrou e o saldo ao fim de cada mês, com o gráfico.','legenda':'O ano, mês a mês'},
    {'tipo':'card','titulo':'Prompts Analisar 03 e Escrever 05','texto':'Copie a tabela "Para onde foi o dinheiro" e peça à IA onde cortar sem prejudicar o essencial. Ou peça para explicar o mês em linguagem simples para um sócio, um cliente ou a família.','fala':'Com o prompt Analisar zero três, a IA ajuda a decidir onde cortar. Com o Escrever zero cinco, ela explica o mês em linguagem simples.','legenda':'Onde cortar e como explicar o mês'},
    {'tipo':'fim','fala':'Antes de um gasto grande, olhe a linha da reserva. Se estiver abaixo da meta, o painel avisa.'},
   ]},
}

def sintetiza(texto, wav):
    from piper import PiperVoice
    global _voz
    try: _voz
    except NameError: _voz=PiperVoice.load(str(VOZ))
    with wave.open(str(wav),'wb') as w: _voz.synthesize_wav(texto, w)
    with wave.open(str(wav),'rb') as w: return w.getnframes()/w.getframerate()

CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#FFFAF0;font-family:Figtree,sans-serif;color:#1F1235}}
.cena{{position:absolute;inset:0;opacity:0}}
.topo{{position:absolute;top:22px;left:32px;width:220px;z-index:5}}
.topo svg{{width:220px;height:auto}}
.tela{{position:absolute;left:32px;top:84px;width:{W-64}px;height:{TELA_H}px;border-radius:14px;overflow:hidden;background:#fff;border:1px solid #DCD2EC;box-shadow:0 18px 40px -24px rgba(31,18,53,.45)}}
.tela img{{position:absolute;left:0;top:0;transform-origin:0 0}}
.legenda{{position:absolute;left:32px;right:32px;bottom:{BARRA_B}px;height:{BARRA_H}px;background:#3B1F5E;color:#fff;border-radius:14px;display:flex;align-items:center;padding:0 28px;font-size:28px;font-weight:600;letter-spacing:-.01em;z-index:6}}
.legenda b{{background:#FFC83D;color:#3B1F5E;border-radius:999px;padding:4px 14px;font-size:16px;margin-right:18px;font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:0;white-space:nowrap}}
.capa{{background:#3B1F5E;color:#fff;padding:70px 90px}} .capa .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:76px;line-height:1.02;letter-spacing:-.02em;margin-top:150px;max-width:1000px}}
.capa .t em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}} .capa .s{{font-size:30px;color:#D9C8F5;margin-top:22px}} .capa .k{{font-family:'Bricolage Grotesque';font-weight:600;font-size:22px;color:#FFC83D;margin-top:60px}}
.capa .simb{{position:absolute;right:90px;top:70px;width:170px}}
.card{{padding:110px 120px 0}} .card .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:44px;color:#3B1F5E;letter-spacing:-.02em}} .card .p{{font-size:32px;line-height:1.35;margin-top:26px;max-width:1000px;color:#1F1235}}
.card .box{{background:#F3EEFB;border-left:10px solid #FFC83D;border-radius:0 14px 14px 0;padding:26px 30px;font-family:'IBM Plex Mono',monospace;font-size:22px;color:#3B1F5E;margin-top:34px;max-width:1000px}}
.fim{{background:#3B1F5E;color:#fff;padding:120px 90px}} .fim .t{{font-family:'Bricolage Grotesque';font-weight:800;font-size:54px;line-height:1.05;letter-spacing:-.02em;max-width:1000px}}
.fim .s{{font-size:28px;color:#D9C8F5;margin-top:26px}} .fim .site{{position:absolute;bottom:60px;left:90px;font-family:'Bricolage Grotesque';font-weight:600;font-size:26px;color:#FFC83D}}
"""
SIMB='<svg viewBox="0 0 72 72"><rect x="12" y="46" width="30" height="10" rx="5.5" fill="#B89BE0"/><rect x="21" y="31" width="30" height="10" rx="5.5" fill="#fff"/><rect x="30" y="16" width="30" height="10" rx="5.5" fill="#fff"/><circle cx="56" cy="52" r="6" fill="#FFC83D"/></svg>'

def html_video(nome, rot, cenas):
    partes=[]
    for i,c in enumerate(cenas):
        if c['tipo']=='capa':
            partes.append(f'<div class="cena capa" id="c{i}"><div class="simb">{SIMB}</div><div class="t">{rot["titulo"]}<br><em>em 15 minutos</em></div><div class="s">{rot["sub"]}</div><div class="k">Kit IA no Trabalho · Essencial · Seu Sócio Gestor</div></div>')
        elif c['tipo']=='tela':
            src='data:image/png;base64,'+b64(ROOT/c['img'])
            f2=(' data-foco2="'+','.join(map(str,c['foco2']))+'"') if c.get('foco2') else ''  # pan opcional na metade da cena
            partes.append(f'<div class="cena" id="c{i}"><div class="topo">{LOGO}</div><div class="tela"><img src="{src}" data-foco="{",".join(map(str,c["foco"]))}"{f2}></div><div class="legenda"><b>{i}</b>{c["legenda"]}</div></div>')
        elif c['tipo']=='card':
            partes.append(f'<div class="cena card" id="c{i}"><div class="topo">{LOGO}</div><div class="t">{c["titulo"]}</div><div class="p">{c["texto"]}</div><div class="legenda"><b>{i}</b>{c["legenda"]}</div></div>')
        elif c['tipo']=='fim':
            partes.append(f'<div class="cena fim" id="c{i}"><div class="t">{c["fala"]}</div><div class="s">Suporte por e-mail · reembolso em 7 dias · pagamento único</div><div class="site">seusociogestor.com.br</div></div>')
    durs=[c['dur'] for c in cenas]
    js=f"""
const durs={json.dumps(durs)}; const W={W-64}, H={TELA_H};
const starts=[]; let acc=0; durs.forEach(d=>{{starts.push(acc); acc+=d;}});
function foco(img,ret){{ const [fx,fy,fw,fh]=ret.split(',').map(Number); const nw=img.naturalWidth, nh=img.naturalHeight;
  const base=W/nw; // escala para caber na largura
  const sx=W/(nw*fw), sy=H/(nh*fh); const s=Math.min(sx,sy, base*3.2);
  let tx=-fx*nw*s + (W-fw*nw*s)/2, ty=-fy*nh*s + (H-fh*nh*s)/2;
  // sem faixa em branco: se a imagem cobre o quadro, mantém dentro; se não cobre, encosta em cima/esquerda
  tx = nw*s>=W ? Math.min(0,Math.max(W-nw*s,tx)) : 0;
  ty = nh*s>=H ? Math.min(0,Math.max(H-nh*s,ty)) : 0;
  return {{tx,ty,s}}; }}
const ease=u=>u<=0?0:u>=1?1:(u<.5?4*u*u*u:1-Math.pow(-2*u+2,3)/2);
const mix=(a,b,u)=>({{tx:a.tx+(b.tx-a.tx)*u, ty:a.ty+(b.ty-a.ty)*u, s:a.s+(b.s-a.s)*u}});
const ZOOM_INI=0.9, ZOOM_DUR=1.6; // visão geral por 0,9 s, depois 1,6 s de zoom até o foco
// estado exato no instante t (segundos): cena visível (fusão de 0,5 s) e posição da tela
window.seek=function(t){{
  let i=0; while(i<durs.length-1 && t>=starts[i+1]) i++;
  const u=t-starts[i];
  document.querySelectorAll('.cena').forEach((e,j)=>{{ e.style.opacity = j===i ? Math.min(1,u/0.5) : (j===i-1 ? Math.max(0,1-u/0.5) : 0); }});
  const img=document.getElementById('c'+i).querySelector('.tela img');
  if(img){{ const a={{tx:0,ty:0,s:W/img.naturalWidth}}, b=foco(img,img.dataset.foco); let st;
    if(u<ZOOM_INI) st=a; else st=mix(a,b,ease((u-ZOOM_INI)/ZOOM_DUR));
    if(img.dataset.foco2){{ const t2=durs[i]*0.5; if(u>=t2) st=mix(b,foco(img,img.dataset.foco2),ease((u-t2)/ZOOM_DUR)); }}
    img.style.transform=`translate(${{st.tx}}px, ${{st.ty}}px) scale(${{st.s}})`; }}
  return i; }};
document.querySelectorAll('.tela img').forEach(img=>{{ img.style.transform=`scale(${{W/(img.naturalWidth||1650)}})`; }});
document.fonts.ready.then(()=>{{ window.seek(0); document.title='PRONTO'; }});
"""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(partes)}<script>window.addEventListener("load",()=>{{ {js} }});</script></body></html>'

def build(nome):
    rot=ROTEIROS[nome]; out=ROOT/'videos'/nome; out.mkdir(parents=True,exist_ok=True)
    cenas=rot['cenas']; wavs=[]
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
    # vídeo: um screenshot por quadro, no instante exato (sem gravação em tempo real, que derivava)
    quadros=out/'quadros'; shutil.rmtree(quadros,ignore_errors=True); quadros.mkdir()
    rec=S/'gravar.js'
    rec.write_text("""const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [html,dir,total,fps]=process.argv.slice(2);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox','--disable-gpu']});
const p=await b.newPage({viewport:{width:%d,height:%d}}); await p.goto('file://'+html);
await p.waitForFunction(()=>document.title==='PRONTO',null,{timeout:60000});
const n=Math.ceil(Number(total)*Number(fps));
for(let f=0;f<n;f++){ await p.evaluate(t=>window.seek(t), f/Number(fps));
  fs.writeFileSync(path.join(dir,'q'+String(f).padStart(5,'0')+'.jpg'), await p.screenshot({type:'jpeg',quality:93})); }
await b.close(); console.log('quadros',n);})();""" % (W,H))
    subprocess.run(['node',str(rec),str(out/'video.html'),str(quadros),str(total),str(FPS)],check=True,env={**dict(__import__('os').environ),'NODE_PATH':str(S/'pw'/'node_modules')})
    # junta: quadros + narração, legenda gravada, corta na duração do áudio, codifica mp4
    final=ROOT/'entrega'/'videos'/f'{nome}.mp4'
    # legendas .srt (cues curtos) escritas antes do mux, e gravadas na imagem acima da barra roxa
    import sys as _s; _s.path.insert(0,str(ROOT.parent)); import legendas as _lg
    srt_path=ROOT/'entrega'/'videos'/f'{nome}.srt'; srt_path.write_text(_lg.cues(cenas,PAUSA))
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',str(quadros/'q%05d.jpg'),'-i',str(out/'narracao.wav'),'-map','0:v','-map','1:a','-vf',_lg.filtro(srt_path,LEG_MARGEM,LEG_TAM,H),'-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(final)],check=True)
    shutil.rmtree(quadros,ignore_errors=True)
    print(nome, f'{total:.1f}s', final)

if __name__=='__main__':
    nomes=sys.argv[1:] or list(ROTEIROS)
    for n in nomes: build(n)
