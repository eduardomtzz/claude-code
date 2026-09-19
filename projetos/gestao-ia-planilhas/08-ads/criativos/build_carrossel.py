#!/usr/bin/env python3
"""Carrosséis de anúncio (Meta Ads, feed e Instagram), 1080×1350, 6 cartões por produto.
Estrutura fixa (regra do dono): 1 dor → 2 custo → 3 solução (mockup) → 4 prova (inventário real)
→ 5 valor (do zero × kit) → 6 preço + CTA. Saída em carrossel/<produto>-NN-1080x1350.png e
carrossel/previa-<produto>.jpg. Uso: python3 build_carrossel.py [essencial|completo|advogados|medicos]"""
import pathlib, base64, subprocess, os, sys, json
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parents[1]
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
DE=PROJ/'produto'/'kit-essencial'/'docs'; DC=PROJ/'produto'/'kit-completo'/'docs'; DA=PROJ/'produto'/'kit-advogados'/'docs'; DM=PROJ/'produto'/'kit-medicos'/'docs'
AS=PROJ/'site'/'public'/'assets'; FONTS=AS/'fonts'; OUT=ROOT/'carrossel'; TRAB=ROOT/'trabalho-carrossel'
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def img(p): return f"data:image/{'webp' if str(p).endswith('.webp') else 'png'};base64,{b64(p)}"
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text(); LOGOB=(PROJ/'03-marca'/'logo'/'logo-branco.svg').read_text()
W,H=1080,1350; N=6
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;font-family:Figtree,sans-serif;position:relative}}
body.creme{{background:#FFFAF0;color:#1F1235}} body.uva{{background:#3B1F5E;color:#fff}} body.lav{{background:#F3EEFB;color:#1F1235}}
.topo{{position:absolute;left:72px;top:64px;width:300px}} .topo svg{{width:300px;height:auto}}
.cont{{position:absolute;right:72px;top:70px;display:flex;align-items:center;gap:18px;font-family:'IBM Plex Mono';font-size:24px;color:#7A5AA8;white-space:nowrap}} .uva .cont{{color:#D9C8F5}}
.dots{{display:flex;gap:8px}} .dots i{{width:14px;height:14px;border-radius:50%;background:#DCD2EC;display:block}} .dots i.on{{background:#3B1F5E;width:34px;border-radius:999px}}
.uva .dots i{{background:rgba(255,255,255,.25)}} .uva .dots i.on{{background:#FFC83D}}
.rod{{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;font-family:'IBM Plex Mono';font-size:22px;color:#7A5AA8;white-space:nowrap}} .uva .rod{{color:#D9C8F5}}
.eyebrow{{position:absolute;left:72px;top:150px;font-family:'IBM Plex Mono';font-size:22px;letter-spacing:.08em;text-transform:uppercase;color:#7A5AA8;white-space:nowrap}} .uva .eyebrow{{color:#FFC83D}}
.t{{font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:-.025em;line-height:1;color:#3B1F5E}} .uva .t{{color:#fff}}
.t em{{font-style:normal;background:linear-gradient(transparent 60%,#FFC83D 60%)}} .uva .t em{{color:#FFC83D;background:none}}
.h{{position:absolute;left:72px;right:72px;top:196px;font-size:80px}}
.sub{{position:absolute;left:72px;right:72px;font-size:34px;line-height:1.3;color:#5A4A78}} .uva .sub{{color:#D9C8F5}}
.pill{{display:inline-flex;align-items:center;justify-content:center;background:#FFC83D;color:#3B1F5E;border-radius:999px;font-family:'Bricolage Grotesque';font-weight:800;padding:0 44px;height:104px;font-size:42px;white-space:nowrap}}
.chip{{display:inline-flex;align-items:center;gap:12px;background:#fff;border:2px solid #DCD2EC;color:#3B1F5E;border-radius:999px;padding:0 24px;height:58px;font-size:26px;font-weight:600;white-space:nowrap}}
.uva .chip{{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.2);color:#fff}}
.chip .pt{{width:14px;height:14px;border-radius:50%;background:#FFC83D;flex:none}}
.mono{{font-family:'IBM Plex Mono'}}
.card{{background:#fff;border:2px solid #DCD2EC;border-radius:28px;padding:30px 34px}} .uva .card{{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.18)}}
.card b{{display:block;font-family:'Bricolage Grotesque';font-weight:700;font-size:36px;color:#3B1F5E;line-height:1.1;margin-bottom:8px}} .uva .card b{{color:#fff}}
.card span{{font-size:27px;color:#5A4A78;line-height:1.3;display:block}} .uva .card span{{color:#D9C8F5}}
.num{{width:64px;height:64px;border-radius:50%;background:#FFC83D;color:#3B1F5E;font-family:'Bricolage Grotesque';font-weight:800;font-size:34px;display:inline-flex;align-items:center;justify-content:center;flex:none}}
.ok,.x{{width:48px;height:48px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:26px;font-weight:700;flex:none}}
.ok{{background:#DDF3E4;color:#1E7A3E}} .x{{background:#FBE4E4;color:#C8402E}}
.lin{{display:flex;align-items:center;gap:22px;font-size:32px;font-weight:600;padding:20px 0;border-top:2px solid #DCD2EC;line-height:1.2}} .uva .lin{{border-color:rgba(255,255,255,.16)}}
/* dispositivos (mesma direção de build_mockup.py) */
.lap{{position:absolute;background:#1F1235;border-radius:26px 26px 6px 6px;padding:22px 22px 30px;box-shadow:0 60px 100px -50px rgba(31,18,53,.6)}}
.lap .scr{{background:#fff;border-radius:10px;overflow:hidden;position:relative}} .lap .scr img{{position:absolute;left:0;top:0;width:100%}}
.lap .base{{position:absolute;left:-6%;right:-6%;bottom:-26px;height:26px;background:linear-gradient(#2B1B45,#1F1235);border-radius:0 0 18px 18px}}
.lap .base::after{{content:'';position:absolute;left:44%;right:44%;top:0;height:8px;background:#3B1F5E;border-radius:0 0 8px 8px}}
.fone{{position:absolute;background:#1F1235;border-radius:46px;padding:14px;box-shadow:0 50px 90px -40px rgba(31,18,53,.7)}}
.fone .scr{{background:#fff;border-radius:34px;overflow:hidden;position:relative}} .fone .scr img{{position:absolute;left:0;top:0}}
.fone .notch{{position:absolute;left:50%;top:14px;transform:translateX(-50%);width:36%;height:26px;background:#1F1235;border-radius:0 0 18px 18px;z-index:2}}
.tag{{position:absolute;background:#3B1F5E;color:#fff;font-family:'IBM Plex Mono';border-radius:999px;z-index:5;white-space:nowrap}}
/* inventário: cards de mockup reais do site */
.inv{{position:absolute;left:72px;right:72px;display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.inv .m{{position:relative;background:#fff;border:2px solid #DCD2EC;border-radius:24px;overflow:hidden}} .inv .m img{{display:block;width:100%;height:100%;object-fit:cover}}
.inv .m .tag{{left:14px;bottom:14px;font-size:22px;padding:9px 18px}}
/* comparação do zero × kit */
.cmp{{position:absolute;left:72px;right:72px;border:2px solid #DCD2EC;border-radius:28px;overflow:hidden;background:#fff}}
.cmp .r{{display:grid;grid-template-columns:250px 1fr 1fr;border-top:2px solid #DCD2EC}} .cmp .r:first-child{{border-top:0}}
.cmp .c{{padding:22px 24px;font-size:27px;line-height:1.25;color:#5A4A78;border-left:2px solid #DCD2EC;display:flex;align-items:center;gap:14px}}
.cmp .c:first-child{{border-left:0;font-weight:700;color:#3B1F5E}}
.cmp .hd .c{{font-family:'Bricolage Grotesque';font-weight:800;font-size:30px;color:#3B1F5E;background:#F3EEFB;white-space:nowrap}}
.cmp .c.kit{{background:#FFF7DD;color:#1F1235;font-weight:600}}
.big{{font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:-.04em;line-height:.9}}
.nota{{font-family:'IBM Plex Mono';font-size:22px;color:#7A5AA8;line-height:1.35}} .uva .nota{{color:#D9C8F5}}
"""
def dispositivos(x,y,escala,lap,fone,tag1,tag2,fone_zoom=2.6):
    lw=int(1100*escala); lh=int(660*escala); fw=int(330*escala); fh=int(680*escala); ft=max(22,int(22*escala))
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{lw+int(180*escala)}px;height:{lh+int(200*escala)}px">
      <div class="lap" style="left:0;top:0;width:{lw}px"><div class="scr" style="height:{lh-int(52*escala)}px"><img src="{img(lap)}"></div><div class="base"></div></div>
      <div class="fone" style="left:{lw-int(150*escala)}px;top:{int(140*escala)}px;width:{fw}px;height:{fh}px"><div class="notch"></div><div class="scr" style="height:100%"><img src="{img(fone)}" style="width:{int(fw*fone_zoom)}px;left:{-int(fw*0.02)}px;top:0"></div></div>
      <div class="tag" style="left:{int(40*escala)}px;top:{lh-int(20*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag1}</div>
      <div class="tag" style="right:0;top:{int(140*escala)+fh+int(16*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag2}</div>
    </div>'''
def chips(items,top,gap=14):
    return f'<div style="position:absolute;left:72px;right:72px;top:{top}px;display:flex;flex-wrap:wrap;gap:{gap}px">'+''.join(f'<span class="chip"><i class="pt"></i>{c}</span>' for c in items)+'</div>'
def barra(label,val,pct):
    return f'<div style="display:flex;align-items:center;gap:20px;margin:16px 0"><div style="width:270px;font-size:30px;font-weight:600;line-height:1.1">{label}</div><div style="flex:1;height:48px;background:rgba(122,90,168,.12);border-radius:999px;overflow:hidden"><div style="width:{pct}%;height:100%;background:#3B1F5E;border-radius:999px"></div></div><div class="mono" style="width:110px;text-align:right;font-size:28px">{val}</div></div>'
def inventario(top,cells,h=272):
    """cells: lista de (webp, rótulo) ou ('txt', html). Grade 2 colunas."""
    out=[]
    for a,b in cells:
        if a=='txt': out.append(f'<div class="card" style="height:{h}px;padding:24px 28px">{b}</div>')
        else: out.append(f'<div class="m" style="height:{h}px"><img src="{img(a)}"><div class="tag">{b}</div></div>')
    return f'<div class="inv" style="top:{top}px">{"".join(out)}</div>'
def comparacao(top,cab,linhas):
    r=[f'<div class="r hd"><div class="c">&nbsp;</div><div class="c">{cab[0]}</div><div class="c kit">{cab[1]}</div></div>']
    for lab,a,b in linhas: r.append(f'<div class="r"><div class="c">{lab}</div><div class="c"><span class="x">✕</span><span>{a}</span></div><div class="c kit"><span class="ok">✓</span><span>{b}</span></div></div>')
    return f'<div class="cmp" style="top:{top}px">{"".join(r)}</div>'
def lista_txt(itens,fs=25):
    return ''.join(f'<div style="display:flex;gap:12px;align-items:flex-start;font-size:{fs}px;line-height:1.25;color:#1F1235;margin:0 0 12px"><span class="mono" style="color:#7A5AA8;flex:none">+</span><span>{i}</span></div>' for i in itens)
def preco(valor,parc,itens,cta,nota):
    li=''.join(f'<div class="lin" style="font-size:29px;padding:16px 0"><span class="ok" style="background:#FFC83D;color:#3B1F5E">✓</span>{i}</div>' for i in itens)
    return f'''
<div class="eyebrow">Pagamento único · sem mensalidade</div>
<div class="big" style="position:absolute;left:72px;top:200px;font-size:210px;color:#fff">{valor}</div>
<div class="nota" style="position:absolute;left:72px;top:410px;font-size:28px">{parc}</div>
<div style="position:absolute;left:72px;right:72px;top:500px">{li}<div style="border-top:2px solid rgba(255,255,255,.16)"></div></div>
<div class="pill" style="position:absolute;left:72px;right:72px;top:1030px;height:120px;font-size:48px">{cta}</div>
<div class="nota" style="position:absolute;left:72px;right:72px;top:1176px;font-size:24px;text-align:center;white-space:nowrap">{nota}</div>'''

# ---------------- conteúdo por produto ----------------
PRODUTOS={
'essencial':dict(nome='Kit IA no Trabalho · Essencial',url='seusociogestor.com.br/kit',cartoes=[
 ('uva',f'''
<div class="eyebrow">Kit IA no Trabalho · Essencial</div>
<div class="t h" style="font-size:96px;top:210px">Montar a planilha. Escrever o relatório. Fazer os slides. <em>Toda semana, do zero.</em></div>
<div class="sub" style="top:790px;font-size:36px">A planilha em branco não sabe o que é urgente. A IA sem os seus números inventa. Dá para começar pronto.</div>
<div class="pill" style="position:absolute;right:72px;top:1120px;height:96px;font-size:38px;padding:0 40px">Arraste para ver <span style="margin-left:16px">→</span></div>'''),
 ('creme',f'''
<div class="eyebrow">O custo de montar do zero</div>
<div class="t h" style="font-size:80px">Quanto tempo vai embora <em>todo mês?</em></div>
<div style="position:absolute;left:72px;right:72px;top:440px">
  {barra('Planilha da semana','4 h',40)}{barra('Relatório do mês','2 h',20)}{barra('Slides da reunião','2 h',20)}{barra('Controle do dinheiro','2 h',20)}
  <div style="display:flex;align-items:baseline;gap:22px;margin-top:36px"><span class="big" style="font-size:150px;color:#3B1F5E">10 h</span><span style="font-size:32px;color:#5A4A78;line-height:1.2">por mês montando<br>o que já podia estar pronto</span></div>
</div>
<div class="sub" style="top:1010px;font-size:30px">Estimativa para quem monta planilha, relatório e slides no braço. A sua conta pode ser maior.</div>'''),
 ('creme',f'''
<div class="eyebrow">A solução</div>
<div class="t h" style="font-size:72px">3 planilhas prontas + 40 prompts de IA. Você baixa, <em>preenche e entrega.</em></div>
<div class="sub" style="top:440px;font-size:28px">Telas reais do kit, no computador e no celular:</div>
{dispositivos(72,486,0.66,DE/'tela-relatorio-painel.png',DE/'tela-ganhos-painel.png','Relatório Mensal Pronto','Ganhos e Gastos')}
{chips(['Ordenam a semana','Escrevem as frases do relatório','Mostram quanto sobrou e para onde foi'],1096)}'''),
 ('lav',f'''
<div class="eyebrow">O que vem dentro</div>
<div class="t h" style="font-size:76px">Sete arquivos, <em>todos seus.</em></div>
{inventario(360,[(AS/'kit'/'mock-semana.webp','Semana Organizada'),(AS/'kit'/'mock-relatorio.webp','Relatório Mensal Pronto'),(AS/'kit'/'mock-ganhos.webp','Ganhos e Gastos'),
  ('txt','<b style="font-size:30px;margin-bottom:14px">E mais</b>'+lista_txt(['40 prompts com exemplo','Mini-manual de 15 minutos','3 vídeos de demonstração','8 slides + checklist'],25))],h=320)}
{chips(['Excel','Google Sheets','Celular','Fórmulas protegidas'],1044)}
<div class="nota" style="position:absolute;left:72px;top:1136px">Telas reais das três planilhas · exemplo preenchido · dados de exemplo</div>'''),
 ('creme',f'''
<div class="eyebrow">Faça a conta</div>
<div class="t h" style="font-size:80px">Montar do zero ou <em>começar pronto?</em></div>
{comparacao(420,('Do zero','Com o kit'),[('Tempo','Horas por mês, todo mês','15 minutos para começar'),('Fórmulas','Você monta e confere','Prontas e protegidas'),('Exemplo','Começa em branco','Vem preenchido'),('Prompts de IA','Escreve e testa cada um','40 prontos, com exemplo'),('Custo','As suas horas','R$ 37, uma vez')])}
<div class="sub" style="top:1150px;font-size:30px">Menos que uma hora do seu trabalho. Os arquivos ficam com você.</div>'''),
 ('uva',preco('R$ 37','Pix ou cartão · acesso imediato após a aprovação',['3 planilhas prontas (Excel, Sheets e celular)','40 prompts de IA com exemplo','Mini-manual e 3 vídeos de demonstração','Modelo de 8 slides + checklist','7 dias para desistir, sem explicar'],'Comprar por R$ 37','Pix ou cartão · 7 dias para desistir')),
]),
'completo':dict(nome='Kit IA no Trabalho · Completo',url='seusociogestor.com.br/completo',cartoes=[
 ('uva',f'''
<div class="eyebrow">Kit IA no Trabalho · Completo</div>
<div class="t h" style="font-size:96px;top:210px">Pedem "um relatório rápido". Você abre um Excel <em>em branco.</em></div>
<div class="sub" style="top:690px;font-size:36px">Junta números de três lugares, escreve do zero, monta os slides na véspera. Planilha, relatório e apresentação podem ter método.</div>
<div class="pill" style="position:absolute;right:72px;top:1120px;height:96px;font-size:38px;padding:0 40px">Arraste para ver <span style="margin-left:16px">→</span></div>'''),
 ('creme',f'''
<div class="eyebrow">O custo de fazer no braço</div>
<div class="t h" style="font-size:80px">Três segundas-feiras <em>que você conhece.</em></div>
<div style="position:absolute;left:72px;right:72px;top:440px;display:grid;gap:20px">
  <div class="card" style="display:flex;gap:26px;align-items:center"><div class="num">1</div><div><b>O relatório "rápido"</b><span>Pedido na segunda, entregue na quarta. Dois dias juntando número e escrevendo do zero.</span></div></div>
  <div class="card" style="display:flex;gap:26px;align-items:center"><div class="num">2</div><div><b>O projeto que atrasou</b><span>Você responde de memória e descobre depois que uma etapa estourou.</span></div></div>
  <div class="card" style="display:flex;gap:26px;align-items:center"><div class="num">3</div><div><b>A reunião de sexta</b><span>Slides montados na quinta à noite, com título "Receita" e gráfico de pizza.</span></div></div>
</div>
<div class="sub" style="top:1130px;font-size:30px">Tempo, retrabalho e uma noite por mês. Sem método, a conta se repete.</div>'''),
 ('creme',f'''
<div class="eyebrow">A solução</div>
<div class="t h" style="font-size:72px">10 planilhas, 80 prompts e 8 aulas curtas. <em>Método, não braço.</em></div>
<div class="sub" style="top:440px;font-size:28px">Telas reais do kit, no computador e no celular:</div>
{dispositivos(72,486,0.66,DC/'tela-metas-painel.png',DC/'tela-projetos-painel.png','Metas do Trimestre','Projetos e Prazos')}
{chips(['O semáforo diz se a meta vai','Mostra o atraso antes da pergunta','Guarda o histórico semana a semana'],1096)}'''),
 ('lav',f'''
<div class="eyebrow">O que vem dentro</div>
<div class="t h" style="font-size:60px;top:196px">Dez planilhas, <em>uma pergunta cada.</em></div>
{inventario(300,[(AS/'completo'/'mock-semana.webp','Semana Organizada'),(AS/'completo'/'mock-relatorio.webp','Relatório Mensal Pronto'),(AS/'completo'/'mock-metas.webp','Metas do Trimestre'),(AS/'completo'/'mock-projetos.webp','Projetos e Prazos'),(AS/'completo'/'mock-funil.webp','Funil de Propostas'),(AS/'completo'/'mock-orcamento.webp','Orçamento Previsto × Realizado')],h=232)}
{chips(['+ Ganhos e Gastos','+ Ata e Pendências','+ Horas e Custo por Projeto','+ Base Limpa'],1092)}
<div class="nota" style="position:absolute;left:72px;top:1046px">Mais 80 prompts · 8 aulas curtas · manual · 3 modelos de slides</div>'''),
 ('creme',f'''
<div class="eyebrow">Faça a conta</div>
<div class="t h" style="font-size:80px">No braço ou <em>com método?</em></div>
{comparacao(360,('No braço','Com o kit'),[('10 planilhas','Dias montando e conferindo','Prontas hoje, com exemplo'),('Fórmulas','Tentativa e erro','Protegidas + dicionário de 60'),('Aprender','Curso longo, sem arquivo','8 aulas curtas, na tela'),('Slides','Na véspera, do zero','3 modelos prontos'),('Custo','As suas horas, todo mês','R$ 197, uma vez')])}
<div class="sub" style="top:1100px;font-size:30px">Menos que uma tarde de trabalho por mês. Os arquivos ficam com você.</div>'''),
 ('uva',preco('R$ 197','ou 12× de R$ 19,90 no cartão · acesso imediato',['10 planilhas prontas (Excel, Sheets e celular)','80 prompts de IA com exemplo','8 aulas curtas com legenda + manual do método','3 modelos de apresentação e 4 checklists','7 dias para desistir, sem explicar'],'Comprar por R$ 197','Pix ou 12× no cartão · 7 dias para desistir')),
]),
'advogados':dict(nome='Kit de Gestão para Advogados',url='seusociogestor.com.br/advogados',cartoes=[
 ('uva',f'''
<div class="eyebrow">Kit de Gestão para Advogados</div>
<div class="t h" style="font-size:92px;top:210px">Você advoga o dia inteiro. O escritório, <em>quem administra?</em></div>
<div class="sub" style="top:670px;font-size:36px">Prazo no caderno, honorário de cabeça, imposto no susto. Vinte planilhas prontas cuidam do dinheiro e do tempo do escritório.</div>
<div class="pill" style="position:absolute;right:72px;top:1120px;height:96px;font-size:38px;padding:0 40px">Arraste para ver <span style="margin-left:16px">→</span></div>'''),
 ('creme',f'''
<div class="eyebrow">O custo de cobrar de cabeça</div>
<div class="t h" style="font-size:80px">Fechou o caso. Cobrou menos que <em>o custo da hora.</em></div>
<div style="position:absolute;left:72px;right:72px;top:500px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
  <div class="card"><span class="mono" style="font-size:22px;text-transform:uppercase;letter-spacing:.06em">Honorário fechado</span><b class="big" style="font-size:74px;margin:10px 0 2px">R$ 2.500</b><span>÷ 40 horas de trabalho</span><b class="big" style="font-size:60px;margin:18px 0 2px;color:#C8402E">R$ 62,50</b><span>por hora trabalhada</span></div>
  <div class="card" style="background:#FFF7DD;border-color:#FFC83D"><span class="mono" style="font-size:22px;text-transform:uppercase;letter-spacing:.06em">Custo-hora do escritório</span><b class="big" style="font-size:74px;margin:10px 0 2px">R$ 66,07</b><span>o que cada hora custa</span><b class="big" style="font-size:60px;margin:18px 0 2px;color:#1E7A3E">R$ 110,00</b><span>hora mínima a cobrar</span></div>
</div>
<div class="card" style="position:absolute;left:72px;right:72px;top:872px;display:flex;align-items:center;justify-content:space-between;gap:24px;padding:24px 34px"><span style="font-size:29px;line-height:1.25;color:#5A4A78">O mesmo caso, pela hora<br>mínima do exemplo:</span><b class="big" style="font-size:72px;margin:0;color:#3B1F5E">R$ 4.400</b></div>
<div class="sub" style="top:1060px;font-size:29px">Quarenta horas abaixo do custo, sem ninguém perceber. Números do escritório de exemplo da planilha Custo-Hora; o seu, você confere na sua.</div>'''),
 ('creme',f'''
<div class="eyebrow">A solução</div>
<div class="t h" style="font-size:70px">20 planilhas em 5 núcleos: prazos, honorários, caixa, carteira <em>e painel.</em></div>
<div class="sub" style="top:440px;font-size:28px">Telas reais do kit, no computador e no celular:</div>
{dispositivos(72,486,0.66,DA/'tela-17.png',DA/'tela-01.png','Painel do Escritório','Agenda de Prazos')}
{chips(['Semáforo: o que vence primeiro','Custo-hora: quanto cobrar','Caixa: o seu e o do escritório'],1096)}'''),
 ('lav',f'''
<div class="eyebrow">O que vem dentro</div>
<div class="t h" style="font-size:70px;top:190px">Cinco núcleos, <em>vinte planilhas.</em></div>
{inventario(300,[(AS/'advogados'/'mock-prazos.webp','1 · Prazos'),(AS/'advogados'/'mock-honorarios.webp','2 · Honorários'),(AS/'advogados'/'mock-caixa.webp','3 · Caixa'),(AS/'advogados'/'mock-carteira.webp','4 · Carteira'),(AS/'advogados'/'mock-painel.webp','5 · Painel'),
  ('txt','<b style="font-size:28px;margin-bottom:10px">E mais</b>'+lista_txt(['40 prompts e 8 aulas curtas','Manual de 4 semanas','3 modelos de slides e 3 bônus'],25))],h=240)}
<div class="nota" style="position:absolute;left:72px;top:1080px">Nada de peça ou orientação jurídica: é gestão do escritório.<br>Telas reais · escritório de exemplo</div>'''),
 ('creme',f'''
<div class="eyebrow">Faça a conta</div>
<div class="t h" style="font-size:80px">Mensalidade ou <em>uma vez?</em></div>
{comparacao(400,('Software jurídico','Com o kit'),[('Preço','A partir de R$ 220 por mês*','R$ 497, uma vez'),('Em 12 meses','R$ 2.640 ou mais','R$ 497'),('Arquivos','Acesso enquanto paga','Seus, para sempre'),('Custo-hora','Você calcula na mão','A planilha calcula'),('Impostos','Provisão no susto','Separada todo mês')])}
<div class="nota" style="position:absolute;left:72px;right:72px;top:1120px;font-size:21px">*Menor plano público de um software de gestão jurídica, consultado em set/2026. Software cuida de publicação e petição; o kit cuida do dinheiro e do tempo do escritório. Um não substitui o outro.</div>'''),
 ('uva',preco('R$ 497','ou 12× no cartão · acesso imediato após a aprovação',['20 planilhas em 5 núcleos (Excel, Sheets e celular)','40 prompts do escritório com exemplo','8 aulas curtas + manual de implantação','3 modelos de apresentação e 3 bônus','7 dias para desistir, sem explicar'],'Comprar por R$ 497','Pix ou 12× no cartão · 7 dias para desistir')),
]),
'medicos':dict(nome='Kit de Gestão para Médicos',url='seusociogestor.com.br/medicos',cartoes=[
 ('uva',f'''
<div class="eyebrow">Kit de Gestão para Médicos</div>
<div class="t h" style="font-size:92px;top:210px">Você atende o dia inteiro. A clínica, <em>quem administra?</em></div>
<div class="sub" style="top:670px;font-size:36px">Agenda com buraco, tabela do convênio sem calcular, imposto no susto. Vinte planilhas prontas cuidam do dinheiro e do tempo da clínica.</div>
<div class="pill" style="position:absolute;right:72px;top:1120px;height:96px;font-size:38px;padding:0 40px">Arraste para ver <span style="margin-left:16px">→</span></div>'''),
 ('creme',f'''
<div class="eyebrow">O custo de aceitar a tabela</div>
<div class="t h" style="font-size:80px">A consulta custa R$ 131. O convênio paga <em>R$ 120.</em></div>
<div style="position:absolute;left:72px;right:72px;top:500px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
  <div class="card"><span class="mono" style="font-size:22px;text-transform:uppercase;letter-spacing:.06em">Convênio · consulta</span><b class="big" style="font-size:70px;margin:10px 0 2px">R$ 120</b><span>tabela, paga em 30 dias</span><b class="big" style="font-size:58px;margin:18px 0 2px;color:#C8402E">R$ 101,85</b><span>líquido após glosa e imposto</span></div>
  <div class="card" style="background:#FFF7DD;border-color:#FFC83D"><span class="mono" style="font-size:22px;text-transform:uppercase;letter-spacing:.06em">Custo cheio da consulta</span><b class="big" style="font-size:70px;margin:10px 0 2px">R$ 130,67</b><span>estrutura, hora e material</span><b class="big" style="font-size:58px;margin:18px 0 2px;color:#1E7A3E">R$ 221,47</b><span>preço mínimo com margem</span></div>
</div>
<div class="card" style="position:absolute;left:72px;right:72px;top:872px;display:flex;align-items:center;justify-content:space-between;gap:24px;padding:24px 34px"><span style="font-size:29px;line-height:1.25;color:#5A4A78">Cada consulta desse convênio,<br>no exemplo:</span><b class="big" style="font-size:72px;margin:0;color:#C8402E">−R$ 28,82</b></div>
<div class="sub" style="top:1060px;font-size:29px">Prazo, glosa e imposto fora da conta, e ninguém percebe. Números da clínica de exemplo, planilhas Custo da Hora e Simulador; os seus, você confere nas suas.</div>'''),
 ('creme',f'''
<div class="eyebrow">A solução</div>
<div class="t h" style="font-size:70px">20 planilhas em 5 núcleos: agenda, preço, caixa, recebíveis <em>e painel.</em></div>
<div class="sub" style="top:440px;font-size:28px">Telas reais do kit, no computador e no celular:</div>
{dispositivos(72,486,0.66,DM/'tela-17.png',DM/'tela-01.png','Painel da Clínica','Agenda e Ocupação')}
{chips(['Agenda: ocupação e faltas','Custo da hora: quanto cobrar','Caixa: repasse e imposto separados'],1096)}'''),
 ('lav',f'''
<div class="eyebrow">O que vem dentro</div>
<div class="t h" style="font-size:70px;top:190px">Cinco núcleos, <em>vinte planilhas.</em></div>
{inventario(300,[(AS/'medicos'/'mock-agenda.webp','1 · Agenda'),(AS/'medicos'/'mock-preco.webp','2 · Preço'),(AS/'medicos'/'mock-caixa.webp','3 · Caixa'),(AS/'medicos'/'mock-convenios.webp','4 · Recebíveis'),(AS/'medicos'/'mock-painel.webp','5 · Painel'),
  ('txt','<b style="font-size:28px;margin-bottom:10px">E mais</b>'+lista_txt(['41 prompts e 8 aulas curtas','Manual de 4 semanas','3 modelos de slides e 3 bônus'],25))],h=240)}
<div class="nota" style="position:absolute;left:72px;top:1080px">Nada clínico, nada de prontuário: é gestão da clínica.<br>Telas reais · clínica de exemplo</div>'''),
 ('creme',f'''
<div class="eyebrow">Faça a conta</div>
<div class="t h" style="font-size:80px">Mensalidade ou <em>uma vez?</em></div>
{comparacao(400,('Software de clínica','Com o kit'),[('Preço','A partir de R$ 62 por mês*','R$ 697, uma vez'),('Em 12 meses','R$ 744 ou mais','R$ 697'),('Arquivos','Acesso enquanto paga','Seus, para sempre'),('Custo da hora','Você calcula na mão','A planilha calcula'),('Convênio','Glosa só no extrato','Prazo e glosa na conta')])}
<div class="nota" style="position:absolute;left:72px;right:72px;top:1120px;font-size:21px">*Menor plano público de um software de clínica, consultado em set/2026. Software cuida de agenda online e prontuário; o kit cuida do dinheiro e do tempo da clínica. Um não substitui o outro.</div>'''),
 ('uva',preco('R$ 697','ou 12× no cartão · acesso imediato após a aprovação',['20 planilhas em 5 núcleos (Excel, Sheets e celular)','41 prompts da clínica com exemplo','8 aulas curtas + manual de implantação','3 modelos de apresentação e 3 bônus','7 dias para desistir, sem explicar'],'Comprar por R$ 697','Pix ou 12× no cartão · 7 dias para desistir')),
]),
}
NOMES_ETAPA=['A dor','O custo','A solução','O que vem dentro','Faça a conta','Preço']
# ---------------- montagem e render ----------------
OUT.mkdir(exist_ok=True); TRAB.mkdir(exist_ok=True)
alvo=sys.argv[1] if len(sys.argv)>1 else None; jobs=[]
for slug,P in PRODUTOS.items():
    if alvo and slug!=alvo: continue
    for i,(tema,corpo) in enumerate(P['cartoes'],1):
        dots=''.join(f'<i class="{"on" if k==i else ""}"></i>' for k in range(1,N+1))
        html_=f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{tema}">
<div class="topo">{LOGOB if tema=="uva" else LOGO}</div>
<div class="cont"><span class="dots">{dots}</span><span>{i}/{N}</span></div>
{corpo}
<div class="rod"><span>{P['url']}</span><span>{P['nome']}</span></div></body></html>'''
        nome=f'{slug}-{i:02d}-1080x1350'; (TRAB/f'{nome}.html').write_text(html_); jobs.append(nome)
js=f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox']}});
for(const n of {json.dumps(jobs)}){{ const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}}); await p.goto('file://{TRAB}/'+n+'.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
 const probs=await p.evaluate(()=>{{
   const out=[]; const all=[...document.querySelectorAll('body *')];
   for(const e of all){{ if(e.closest('.scr')) continue; const r=e.getBoundingClientRect(); if(r.width>0&&(r.right>{W}+1||r.bottom>{H}+1||r.left<-1||r.top<-1)) out.push('ESTOURO '+e.className+' '+Math.round(r.right)+'x'+Math.round(r.bottom)); }}
   for(const e of all){{ const cs=getComputedStyle(e); if(cs.whiteSpace==='nowrap'&&e.scrollWidth>e.clientWidth+1) out.push('CORTE nowrap '+e.className+' '+e.textContent.trim().slice(0,40)); }}
   for(const e of all){{ if(e.scrollHeight>e.clientHeight+2&&getComputedStyle(e).overflow==='hidden'&&!e.classList.contains('scr')&&!e.classList.contains('m')) out.push('OVERFLOW '+e.className+' '+e.textContent.trim().slice(0,40)); }}
   // sobreposição entre elementos com texto direto (ignorando ancestral/descendente)
   const tx=all.filter(e=>[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim())).map(e=>({{e,r:e.getBoundingClientRect()}})).filter(o=>o.r.width>0);
   for(let i=0;i<tx.length;i++)for(let j=i+1;j<tx.length;j++){{const a=tx[i],b=tx[j]; if(a.e.contains(b.e)||b.e.contains(a.e)) continue;
     const ox=Math.min(a.r.right,b.r.right)-Math.max(a.r.left,b.r.left), oy=Math.min(a.r.bottom,b.r.bottom)-Math.max(a.r.top,b.r.top);
     if(ox>4&&oy>4) out.push('SOBREPOSTO "'+a.e.textContent.trim().slice(0,25)+'" x "'+b.e.textContent.trim().slice(0,25)+'"'); }}
   return out; }});
 for(const x of probs) console.log(n,x);
 await p.screenshot({{path:'{OUT}/'+n+'.png'}}); await p.close(); }} await b.close(); console.log('ok');}})();"""
(TRAB/'shot.js').write_text(js)
subprocess.run(['node',str(TRAB/'shot.js')],check=True,env={**os.environ,'NODE_PATH':str(S/'pw'/'node_modules')})
# prévia em tira (6 cartões lado a lado)
from PIL import Image
for slug in PRODUTOS:
    if alvo and slug!=alvo: continue
    ims=[Image.open(OUT/f'{slug}-{i:02d}-1080x1350.png').resize((432,540)) for i in range(1,N+1)]
    g=Image.new('RGB',(N*432+(N-1)*8,540),'#fff')
    for i,im in enumerate(ims): g.paste(im,(i*440,0))
    g.save(OUT/f'previa-{slug}.jpg',quality=88); print('prévia',slug)
