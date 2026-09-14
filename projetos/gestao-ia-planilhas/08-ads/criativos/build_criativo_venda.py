#!/usr/bin/env python3
"""Criativo de VENDA 9:16 do Kit Essencial: dor → custo → solução (infográfico animado) → prova → valor → preço."""
import sys, json, subprocess, pathlib, base64, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]/'produto'/'kit-completo'))
import video_engine as V
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parents[1]; DOCS=PROJ/'produto'/'kit-essencial'/'docs'
W,H=1080,1920; PAUSA=0.5
PROD=(sys.argv[1] if len(sys.argv)>1 else "essencial")
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text(); LOGOB=(PROJ/'03-marca'/'logo'/'logo-branco.svg').read_text()
FONTS=PROJ/'site'/'public'/'assets'/'fonts'; MOCK=ROOT/f'{PROD}-produto-hero-1600x1000.png'
SIMB='<svg viewBox="0 0 72 72"><rect x="12" y="46" width="30" height="10" rx="5.5" fill="#B89BE0"/><rect x="21" y="31" width="30" height="10" rx="5.5" fill="#fff"/><rect x="30" y="16" width="30" height="10" rx="5.5" fill="#fff"/><circle cx="56" cy="52" r="6" fill="#FFC83D"/></svg>'
CFG={
 'essencial':dict(
  cenas=[
   {'tipo':'dor','fala':'Toda segunda, a mesma planilha. Todo dia trinta, o relatório do zero. Toda reunião, os slides na véspera.','min':6.5,'h':'Você conhece essa <em class="esc">semana.</em>','itens':['Segunda: a mesma planilha','Dia 30: o relatório do zero','Véspera: os slides'],'rod':'e o chefe ainda pergunta "cadê o relatório?"'},
   {'tipo':'custo','fala':'Isso custa umas seis horas por semana. Trezentas horas por ano montando o que já podia estar pronto.','min':6.0,'num':300,'passo':6,'unid':'h','small':'por ano montando do zero','leg':'6 horas por semana × 50 semanas. Tempo que não volta.'},
   {'tipo':'fluxo','fala':'O Kit IA no Trabalho resolve em três passos. Você preenche a planilha pronta. Cola os números no prompt. A IA escreve, você revisa e entrega.','min':8.5,'h':'Três passos. <em>Pronto.</em>','passos':[('Preencher','a planilha já vem pronta'),('Perguntar','cola os números no prompt'),('Entregar','a IA escreve, você revisa')],'t':[1.6,4.0,6.0],'rod':'Kit IA no Trabalho · Essencial'},
   {'tipo':'prova','fala':'Não é promessa: são três planilhas reais, quarenta prompts prontos, manual e vídeos. No computador ou no celular.','min':6.5,'selos':['3 planilhas prontas','40 prompts de IA','Mini-manual','3 vídeos']},
   {'tipo':'valor','fala':'Um analista cobraria mais de cem reais por hora para montar isso. O kit custa trinta e sete. Uma vez.','min':6.5,'c1':('um analista','R$ 100+','por hora, e leva o dia'),'c2':('o kit','R$ 37','uma vez, seu para sempre'),'rod':'Menos que uma hora do seu trabalho montando do zero'},
   {'tipo':'fim','fala':'Kit IA no Trabalho Essencial. Trinta e sete reais. Sete dias para desistir. Comece hoje.','min':5.5,'tt':'Kit IA no Trabalho <em>Essencial</em>','preco':'Comprar por R$ 37','nota':'3 planilhas · 40 prompts · manual e vídeos<br>Pix ou cartão · acesso imediato · 7 dias para desistir'},
  ]),
 'completo':dict(
  cenas=[
   {'tipo':'dor','fala':'Segunda, o chefe pede um relatório rápido. Quarta, o cliente pergunta como está o projeto. Sexta, a reunião de resultados. E você monta tudo do zero.','min':8.0,'h':'Você conhece essa <em class="esc">semana.</em>','itens':['Segunda: "um relatório rápido"','Quarta: "como está o projeto?"','Sexta: os slides da reunião'],'rod':'e a planilha de metas continua em branco'},
   {'tipo':'custo','fala':'Montar essas dez planilhas do zero leva umas quarenta horas. E no fim, cada uma calcula de um jeito.','min':6.5,'num':40,'passo':1,'unid':'h','small':'para montar as dez planilhas do zero','leg':'Metas, projetos, orçamento, funil, horas. Cada uma de um jeito.'},
   {'tipo':'fluxo','fala':'O Kit Completo tem método em quatro passos. Estruturar antes de abrir o Excel. Preencher a planilha pronta. Perguntar à IA com os seus números. Entregar revisado.','min':10.0,'h':'Quatro passos. <em>Método.</em>','passos':[('Estruturar','quem lê, quando, para decidir o quê'),('Preencher','as 10 planilhas já vêm prontas'),('Perguntar','80 prompts com o seu bloco de números'),('Entregar','modelos de slides e checklists')],'t':[1.4,3.6,5.8,8.0],'rod':'Kit IA no Trabalho · Completo'},
   {'tipo':'prova','fala':'Não é promessa: dez planilhas reais, oitenta prompts, oito aulas curtas na tela e três modelos de apresentação. No computador ou no celular.','min':7.5,'selos':['10 planilhas prontas','80 prompts de IA','8 aulas curtas','3 modelos de slides']},
   {'tipo':'valor','fala':'Quarenta horas montando do zero, sem método. Ou o kit, por cento e noventa e sete reais. Uma vez, em até doze vezes no cartão.','min':7.0,'c1':('do zero','40 h','do seu tempo, sem método'),'c2':('o kit','R$ 197','uma vez, ou 12× no cartão'),'rod':'Menos que uma tarde de trabalho por mês'},
   {'tipo':'fim','fala':'Kit IA no Trabalho Completo. Cento e noventa e sete reais. Sete dias para desistir. Comece hoje.','min':6.0,'tt':'Kit IA no Trabalho <em>Completo</em>','preco':'Comprar por R$ 197','nota':'10 planilhas · 80 prompts · 8 aulas · 3 modelos<br>Pix ou 12× · acesso imediato · 7 dias para desistir'},
  ]),
}
CFG['advogados']=dict(
  cenas=[
   {'tipo':'dor','fala':'O prazo está no caderno, no celular e no e-mail. O cliente pergunta quanto fica e você responde de cabeça. E o imposto chega junto com o décimo terceiro.','min':8.5,'h':'Você advoga. <em class="esc">E o escritório?</em>','itens':['Prazo: caderno, celular, e-mail','"Quanto fica?" de cabeça','Imposto junto com o 13º'],'rod':'e ninguém sabe se o mês deu lucro'},
   {'tipo':'custo','fala':'Um caso de quarenta horas cobrado abaixo do custo da sua hora. Isso acontece toda vez que o honorário é chute.','min':6.5,'num':40,'passo':1,'unid':'h','small':'trabalhadas num caso cobrado no chute','leg':'Sem custo-hora, a proposta sai errada. E você só descobre no fim.'},
   {'tipo':'fluxo','fala':'O Kit de Gestão para Advogados tem cinco núcleos. Prazos com semáforo. Honorário pela hora. Caixa com provisão. Carteira viva. E o painel de sexta.','min':9.5,'h':'Cinco núcleos. <em>Uma rotina.</em>','passos':[('Prazos','semáforo por dias, rotina de segunda'),('Honorários','custo-hora × horas + margem'),('Caixa','impostos, 13º e pró-labore separados'),('Carteira e painel','quem deve, quanto, e uma tela na sexta')],'t':[1.4,3.6,5.8,7.8],'rod':'Kit de Gestão para Advogados'},
   {'tipo':'prova','fala':'Não é promessa: vinte planilhas reais, quarenta prompts, oito aulas curtas e três modelos de apresentação. No computador ou no celular.','min':7.5,'selos':['20 planilhas prontas','40 prompts','8 aulas curtas','3 modelos de slides']},
   {'tipo':'valor','fala':'Software jurídico custa a partir de duzentos e vinte reais por mês, todo mês. O kit custa quatrocentos e noventa e sete. Uma vez, em até doze vezes.','min':7.5,'c1':('software','R$ 220+','por mês, todo mês'),'c2':('o kit','R$ 497','uma vez, ou 12× no cartão'),'rod':'Menos que três meses do software, e os arquivos ficam com você'},
   {'tipo':'fim','fala':'Kit de Gestão para Advogados. Quatrocentos e noventa e sete reais. Sete dias para desistir. Comece hoje.','min':6.0,'tt':'Kit de Gestão <em>para Advogados</em>','preco':'Comprar por R$ 497','nota':'20 planilhas · 40 prompts · 8 aulas · 3 modelos<br>Pix ou 12× · acesso imediato · 7 dias para desistir'},
  ])
CENAS=CFG[PROD]['cenas']
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#FFFAF0;font-family:Figtree,sans-serif;color:#1F1235}}
.cena{{position:absolute;inset:0;opacity:0;transition:opacity .35s}} .cena.on{{opacity:1}}
.topo{{position:absolute;top:150px;left:60px;width:300px;z-index:5}} .topo svg{{width:300px;height:auto}}
.uva{{background:#3B1F5E;color:#fff}} .uva .topo svg path,.uva .topo svg text{{}} 
.t{{font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:-.02em;line-height:1.02}}
.h{{position:absolute;left:60px;right:60px;top:300px;font-size:92px}} .h em{{font-style:normal;color:#FFC83D}}
.h.esc em{{background:linear-gradient(transparent 62%,#FFC83D 62%);color:inherit}}
.sub{{position:absolute;left:60px;right:60px;font-size:40px;line-height:1.3;color:#5A4A78}} .uva .sub{{color:#D9C8F5}}
.rod{{position:absolute;left:60px;right:60px;bottom:250px;font-family:'IBM Plex Mono';font-size:26px;color:#7A5AA8;text-align:center}} .uva .rod{{color:#B89BE0}}
/* dor: itens que entram um a um */
.dor .lista{{position:absolute;left:60px;right:60px;top:640px;list-style:none;margin:0;padding:0}}
.dor .lista li{{opacity:0;transform:translateY(24px);transition:all .5s;background:#fff;border:2px solid #DCD2EC;border-radius:24px;padding:34px 40px 34px 120px;font-size:46px;font-weight:600;margin-bottom:26px;position:relative;color:#1F1235}}
.dor .lista li::before{{content:'✕';position:absolute;left:40px;top:30px;width:56px;height:56px;border-radius:50%;background:#FBE4E4;color:#C8402E;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700}}
.dor .lista li.on{{opacity:1;transform:none}}
/* custo: número grande que sobe */
.custo .num{{position:absolute;left:60px;right:60px;top:600px;font-size:300px;font-family:'Bricolage Grotesque';font-weight:800;color:#3B1F5E;letter-spacing:-.04em;line-height:1}}
.custo .num small{{display:block;font-size:56px;letter-spacing:-.01em;color:#7A5AA8;margin-top:10px}}
.custo .barra{{position:absolute;left:60px;right:60px;top:1060px;height:40px;background:#F3EEFB;border-radius:999px;overflow:hidden}} .custo .barra i{{display:block;height:100%;width:0;background:#C8402E;transition:width 3s linear}}
.custo .leg{{position:absolute;left:60px;right:60px;top:1130px;font-size:40px;color:#5A4A78}}
/* fluxo: três passos que acendem */
.fluxo .passos{{position:absolute;left:60px;right:60px;top:600px}}
.fluxo .p{{display:flex;align-items:center;gap:34px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.16);border-radius:28px;padding:36px 40px;margin-bottom:28px;opacity:.25;transform:scale(.97);transition:all .5s}}
.fluxo .p.on{{opacity:1;transform:none;background:rgba(255,255,255,.12);border-color:#FFC83D}}
.fluxo .n{{width:96px;height:96px;border-radius:50%;background:#FFC83D;color:#3B1F5E;font-family:'Bricolage Grotesque';font-weight:800;font-size:52px;display:flex;align-items:center;justify-content:center;flex:none}}
.fluxo .p b{{display:block;font-family:'Bricolage Grotesque';font-weight:700;font-size:54px;color:#fff}} .fluxo .p span{{font-size:34px;color:#D9C8F5}}
.fluxo .seta{{text-align:center;color:#FFC83D;font-size:44px;margin:-18px 0 6px}}
/* fluxo com 4 passos: mais compacto */
.fluxo--4 .passos{{top:560px}} .fluxo--4 .p{{padding:24px 34px;margin-bottom:16px}} .fluxo--4 .n{{width:80px;height:80px;font-size:44px}} .fluxo--4 .p b{{font-size:48px}} .fluxo--4 .p span{{font-size:31px}} .fluxo--4 .seta{{font-size:36px;margin:-10px 0 2px}}
/* prova: mockup notebook + celular entra de baixo */
.mock{{position:absolute;left:0;width:{W}px;opacity:0;transform:translateY(90px);transition:all .9s cubic-bezier(.2,.7,.2,1)}} .mock.on{{opacity:1;transform:none}} .mock img{{width:100%;display:block}}
.prova .mock{{top:470px}} .prova .selos{{position:absolute;left:60px;right:60px;top:1200px;display:flex;gap:18px;flex-wrap:wrap;justify-content:center}}
.prova .selos span{{background:#fff;border:2px solid #DCD2EC;border-radius:999px;padding:16px 30px;font-family:'Bricolage Grotesque';font-weight:700;font-size:36px;color:#3B1F5E;opacity:0;transform:translateY(20px);transition:all .4s}} .prova .selos span.on{{opacity:1;transform:none}}
.tela{{position:absolute;left:60px;top:560px;width:{W-120}px;height:900px;border-radius:24px;overflow:hidden;background:#fff;border:2px solid #DCD2EC;box-shadow:0 30px 60px -30px rgba(31,18,53,.45)}}
.tela img{{position:absolute;left:0;top:0;transform-origin:0 0;transition:transform 2.2s cubic-bezier(.4,0,.2,1)}}
.selo{{position:absolute;right:60px;top:500px;background:#FFC83D;color:#3B1F5E;border-radius:999px;padding:16px 30px;font-family:'Bricolage Grotesque';font-weight:800;font-size:34px;z-index:6;transform:rotate(-4deg)}}
.legenda{{position:absolute;left:60px;right:60px;bottom:330px;min-height:150px;background:#3B1F5E;color:#fff;border-radius:24px;display:flex;align-items:center;padding:28px 40px;font-family:'Bricolage Grotesque';font-weight:800;font-size:60px;line-height:1.05;letter-spacing:-.02em;z-index:6}}
/* valor: comparação */
.valor .comp{{position:absolute;left:60px;right:60px;top:620px;display:grid;grid-template-columns:1fr 1fr;gap:26px}}
.valor .c{{border-radius:28px;padding:40px 30px;text-align:center}} .valor .c1{{background:#fff;border:2px solid #DCD2EC}} .valor .c2{{background:#FFC83D}}
.valor .c small{{display:block;font-family:'IBM Plex Mono';font-size:26px;color:#7A5AA8;margin-bottom:18px;text-transform:uppercase;letter-spacing:.06em}} .valor .c2 small{{color:#3B1F5E}}
.valor .c b{{display:block;font-family:'Bricolage Grotesque';font-weight:800;font-size:96px;color:#3B1F5E;letter-spacing:-.03em;line-height:1}} .valor .c i{{display:block;font-style:normal;font-size:32px;color:#5A4A78;margin-top:14px}} .valor .c2 i{{color:#3B1F5E}}
.valor .risco{{position:relative}} .valor .risco::after{{content:'';position:absolute;left:-6%;right:-6%;top:52%;height:10px;background:#C8402E;transform:rotate(-8deg);border-radius:6px;opacity:0;transition:opacity .3s}} .valor .risco.on::after{{opacity:1}}
/* fim */
.fim .l{{position:absolute;top:140px;left:80px;width:440px}} .fim .l svg{{width:440px;height:auto}}
.fim .tt{{position:absolute;top:290px;left:80px;right:80px;font-size:84px}} .fim .tt em{{font-style:normal;background:linear-gradient(transparent 62%,#FFC83D 62%)}}
.fim .mock{{top:520px}}
.fim .lista{{position:absolute;top:840px;left:80px;right:80px;list-style:none;padding:0;margin:0}} .fim .lista li{{font-size:40px;padding:18px 0 18px 70px;position:relative;border-top:1px solid rgba(255,255,255,.18);color:#F3EEFB}}
.fim .lista li::before{{content:'';position:absolute;left:0;top:26px;width:36px;height:36px;border-radius:50%;background:#FFC83D url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M4 9.5l3 3 7-7' fill='none' stroke='%233B1F5E' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/60% no-repeat}}
.fim .preco{{position:absolute;top:1260px;left:80px;right:80px;background:#FFC83D;color:#3B1F5E;border-radius:999px;height:150px;display:flex;align-items:center;justify-content:center;font-family:'Bricolage Grotesque';font-weight:800;font-size:64px;animation:pulsa 1.6s ease-in-out infinite}}
@keyframes pulsa{{50%{{transform:scale(1.03)}}}}
.fim .nota{{position:absolute;top:1440px;left:80px;right:80px;font-family:'IBM Plex Mono';font-size:28px;color:#D9C8F5;text-align:center}}
.fim .site{{position:absolute;top:1530px;left:80px;right:80px;font-family:'Bricolage Grotesque';font-weight:600;font-size:34px;color:#FFC83D;text-align:center}}
"""
def html(cenas):
    partes=[]; extra=[]
    for i,c in enumerate(cenas):
        if c['tipo']=='dor':
            its=''.join(f'<li id="d{k}">{x}</li>' for k,x in enumerate(c['itens']))
            partes.append(f'<div class="cena dor" id="c{i}"><div class="topo">{LOGO}</div><div class="t h">{c["h"]}</div><ul class="lista">{its}</ul><div class="rod">{c["rod"]}</div></div>')
            extra.append(f'[0.4,1.9,3.6].forEach((s,k)=>setTimeout(()=>document.getElementById("d"+k).classList.add("on"),(T{i}+s)*1000));')
        elif c['tipo']=='custo':
            partes.append(f'<div class="cena custo" id="c{i}"><div class="topo">{LOGO}</div><div class="t h">Quanto isso custa?</div><div class="num"><span id="cnum">0</span> {c["unid"]}<small>{c["small"]}</small></div><div class="barra"><i id="cbar"></i></div><div class="leg">{c["leg"]}</div></div>')
            extra.append(f'setTimeout(()=>{{document.getElementById("cbar").style.width="100%"; let n=0; const iv=setInterval(()=>{{n+={c["passo"]}; if(n>={c["num"]}){{n={c["num"]};clearInterval(iv);}} document.getElementById("cnum").textContent=n;}},60);}},(T{i}+0.5)*1000);')
        elif c['tipo']=='fluxo':
            ps=c['passos']; comp=' fluxo--4' if len(ps)>3 else ''
            inner=''.join(f'<div class="p" id="f{k}"><div class="n">{k+1}</div><div><b>{a}</b><span>{b}</span></div></div>'+('<div class="seta">▼</div>' if k<len(ps)-1 else '') for k,(a,b) in enumerate(ps))
            partes.append(f'<div class="cena uva fluxo{comp}" id="c{i}"><div class="topo">{LOGOB}</div><div class="t h">{c["h"]}</div><div class="passos">{inner}</div><div class="rod">{c["rod"]}</div></div>')
            extra.append(f'{json.dumps(c["t"])}.forEach((s,k)=>setTimeout(()=>document.getElementById("f"+k).classList.add("on"),(T{i}+s)*1000));')
        elif c['tipo']=='prova':
            selos=''.join(f'<span id="s{k}">{x}</span>' for k,x in enumerate(c['selos']))
            partes.append(f'<div class="cena prova" id="c{i}"><div class="topo">{LOGO}</div><div class="t h" style="font-size:72px">O que você recebe hoje</div><div class="selo">telas reais</div><div class="mock" id="mock{i}"><img src="data:image/png;base64,{b64(MOCK)}"></div><div class="selos">{selos}</div><div class="rod">Abre no Excel, no Google Planilhas e no celular</div></div>')
            extra.append(f'setTimeout(()=>document.getElementById("mock{i}").classList.add("on"),(T{i}+0.3)*1000); [1.6,2.4,3.2,4.0].forEach((s,k)=>setTimeout(()=>document.getElementById("s"+k).classList.add("on"),(T{i}+s)*1000));')
        elif c['tipo']=='valor':
            partes.append(f'<div class="cena valor" id="c{i}"><div class="topo">{LOGO}</div><div class="t h">Faça a conta.</div><div class="comp"><div class="c c1"><small>{c["c1"][0]}</small><b class="risco" id="risco">{c["c1"][1]}</b><i>{c["c1"][2]}</i></div><div class="c c2"><small>{c["c2"][0]}</small><b>{c["c2"][1]}</b><i>{c["c2"][2]}</i></div></div><div class="rod">{c["rod"]}</div></div>')
            extra.append(f'setTimeout(()=>document.getElementById("risco").classList.add("on"),(T{i}+3.2)*1000);')
        elif c['tipo']=='fim':
            partes.append(f'<div class="cena uva fim" id="c{i}"><div class="l">{LOGOB}</div><div class="t tt">{c["tt"]}</div><div class="mock" id="mock{i}"><img src="data:image/png;base64,{b64(MOCK)}"></div><div class="preco">{c["preco"]}</div><div class="nota">{c["nota"]}</div><div class="site">seusociogestor.com.br</div></div>')
            extra.append(f'setTimeout(()=>document.getElementById("mock{i}").classList.add("on"),(T{i}+0.2)*1000);')
    durs=[c['dur'] for c in cenas]
    starts=[]; t=0
    for d in durs: starts.append(round(t,2)); t+=d
    consts=''.join(f'const T{i}={s};' for i,s in enumerate(starts))
    js=f"""const durs={json.dumps(durs)}; {consts} const W={W-120}, H=900;
function foco(img){{ const [fx,fy,fw,fh]=img.dataset.foco.split(',').map(Number); const nw=img.naturalWidth, nh=img.naturalHeight;
  const base=W/nw; const sx=W/(nw*fw), sy=H/(nh*fh); const s=Math.min(sx,sy,base*3); const tx=-fx*nw*s+(W-fw*nw*s)/2, ty=-fy*nh*s+Math.max(0,(H-fh*nh*s)/2);
  return `translate(${{tx}}px, ${{Math.min(0,ty)}}px) scale(${{s}})`; }}
document.querySelectorAll('.tela img').forEach(img=>{{ img.style.transform=`scale(${{W/img.naturalWidth}})`; }});
let t=0; durs.forEach((d,i)=>{{ setTimeout(()=>{{ document.querySelectorAll('.cena.on').forEach(e=>e.classList.remove('on')); const c=document.getElementById('c'+i); c.classList.add('on');
  const img=c.querySelector('.tela img'); if(img){{ setTimeout(()=>{{img.style.transform=foco(img);}},700); }} }}, t*1000); t+=d; }});
{''.join(extra)}
setTimeout(()=>{{document.title='FIM'}}, t*1000+300);"""
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(partes)}<script>window.addEventListener("load",()=>{{ {js} }});</script></body></html>'
out=ROOT/f'trabalho-venda-{PROD}'; out.mkdir(exist_ok=True); wavs=[]
for i,c in enumerate(CENAS):
    w=out/f'fala{i}.wav'; d=V.sintetiza(c['fala'],w); c['dur']=round(max(d+PAUSA,c['min']),2); wavs.append((w,c['dur']))
total=sum(c['dur'] for c in CENAS); (out/'video.html').write_text(html(CENAS))
linhas=[]
for i,(w,d) in enumerate(wavs):
    p=out/f'cena{i}.wav'; subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(w),'-af',f'apad=whole_dur={d}','-ar','44100','-ac','1',str(p)],check=True); linhas.append(f"file '{p.name}'")
(out/'audio.txt').write_text('\n'.join(linhas)+'\n')
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(out/'audio.txt'),'-c','copy',str(out/'narracao.wav')],check=True)
rec=ROOT/'trabalho'/'gravar.js'
subprocess.run(['node',str(rec),str(out/'video.html'),str(out),str(total)],check=True,env={**os.environ,'NODE_PATH':str(V.S/'pw'/'node_modules')})
final=ROOT/f'{PROD}-venda-9x16.mp4'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(out/'gravacao.webm'),'-i',str(out/'narracao.wav'),'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',str(final)],check=True)
srt=[]; t=0.0
def ts(x): h=int(x//3600); m=int(x%3600//60); s=x%60; return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.',',')
for i,c in enumerate(CENAS): srt.append(f"{i+1}\n{ts(t)} --> {ts(t+c['dur']-PAUSA)}\n{c['fala']}\n"); t+=c['dur']
(ROOT/f'{PROD}-venda-9x16.srt').write_text('\n'.join(srt)); print(f'{total:.1f}s', final)
