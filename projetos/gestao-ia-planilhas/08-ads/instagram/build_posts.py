#!/usr/bin/env python3
"""12 posts de feed do Instagram (1080×1350) com direção visual única: 6 institucionais, 3 do Essencial, 3 do Completo.
Também gera a prévia do feed (3 colunas, ordem de publicação invertida). Uso: python3 build_posts.py [n]"""
import pathlib, base64, subprocess, os, sys, json
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parents[1]
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
DE=PROJ/'produto'/'kit-essencial'/'docs'; DC=PROJ/'produto'/'kit-completo'/'docs'; DA=PROJ/'produto'/'kit-advogados'/'docs'; FONTS=PROJ/'site'/'public'/'assets'/'fonts'
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text(); LOGOB=(PROJ/'03-marca'/'logo'/'logo-branco.svg').read_text()
EMP=(PROJ/'03-marca'/'logo'/'logo-empilhado.svg').read_text(); EMPB=(PROJ/'03-marca'/'logo'/'logo-empilhado-branco.svg').read_text()
SIMB=(PROJ/'03-marca'/'logo'/'simbolo.svg').read_text()
W,H=1080,1350
CSS=f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600 800;src:url(data:font/woff2;base64,{b64(FONTS/'bricolage-grotesque.woff2')}) format('woff2')}}
@font-face{{font-family:'Figtree';font-weight:400 700;src:url(data:font/woff2;base64,{b64(FONTS/'figtree.woff2')}) format('woff2')}}
@font-face{{font-family:'IBM Plex Mono';font-weight:500;src:url(data:font/woff2;base64,{b64(FONTS/'ibm-plex-mono-500.woff2')}) format('woff2')}}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;font-family:Figtree,sans-serif;position:relative}}
body.creme{{background:#FFFAF0;color:#1F1235}} body.uva{{background:#3B1F5E;color:#fff}} body.lav{{background:#F3EEFB;color:#1F1235}}
.topo{{position:absolute;left:72px;top:64px;width:300px}} .topo svg{{width:300px;height:auto}}
.eyebrow{{position:absolute;right:72px;top:74px;font-family:'IBM Plex Mono';font-size:22px;letter-spacing:.08em;text-transform:uppercase;color:#7A5AA8}} .uva .eyebrow{{color:#D9C8F5}}
.rod{{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;font-family:'IBM Plex Mono';font-size:22px;color:#7A5AA8}} .uva .rod{{color:#D9C8F5}}
.t{{font-family:'Bricolage Grotesque';font-weight:800;letter-spacing:-.025em;line-height:.98;color:#3B1F5E}} .uva .t{{color:#fff}}
.t em{{font-style:normal;background:linear-gradient(transparent 60%,#FFC83D 60%)}} .uva .t em{{color:#FFC83D;background:none}}
.h{{position:absolute;left:72px;right:72px;top:200px;font-size:88px}}
.sub{{position:absolute;left:72px;right:72px;font-size:36px;line-height:1.3;color:#5A4A78}} .uva .sub{{color:#D9C8F5}}
.pill{{display:inline-flex;align-items:center;justify-content:center;background:#FFC83D;color:#3B1F5E;border-radius:999px;font-family:'Bricolage Grotesque';font-weight:800;padding:0 44px;height:104px;font-size:42px}}
.mono{{font-family:'IBM Plex Mono'}}
/* cards */
.card{{background:#fff;border:2px solid #DCD2EC;border-radius:28px;padding:34px 36px}} .uva .card{{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.18)}}
.card b{{display:block;font-family:'Bricolage Grotesque';font-weight:700;font-size:38px;color:#3B1F5E;line-height:1.1;margin-bottom:8px}} .uva .card b{{color:#fff}}
.card span{{font-size:28px;color:#5A4A78;line-height:1.3}} .uva .card span{{color:#D9C8F5}}
.num{{width:72px;height:72px;border-radius:50%;background:#FFC83D;color:#3B1F5E;font-family:'Bricolage Grotesque';font-weight:800;font-size:38px;display:inline-flex;align-items:center;justify-content:center;flex:none}}
.ok,.x{{width:56px;height:56px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;flex:none}}
.ok{{background:#DDF3E4;color:#1E7A3E}} .x{{background:#FBE4E4;color:#C8402E}}
.uva .ok{{background:#FFC83D;color:#3B1F5E}} .uva .x{{background:rgba(255,255,255,.14);color:#fff}}
.lin{{display:flex;align-items:center;gap:24px;font-size:34px;font-weight:600;padding:22px 0;border-top:2px solid #DCD2EC}} .uva .lin{{border-color:rgba(255,255,255,.16)}}
/* dispositivos */
.lap{{position:absolute;background:#1F1235;border-radius:26px 26px 6px 6px;padding:22px 22px 30px;box-shadow:0 60px 100px -50px rgba(31,18,53,.6)}}
.lap .scr{{background:#fff;border-radius:10px;overflow:hidden;position:relative}} .lap .scr img{{position:absolute;left:0;top:0;width:100%}}
.lap .base{{position:absolute;left:-6%;right:-6%;bottom:-26px;height:26px;background:linear-gradient(#2B1B45,#1F1235);border-radius:0 0 18px 18px}}
.lap .base::after{{content:'';position:absolute;left:44%;right:44%;top:0;height:8px;background:#3B1F5E;border-radius:0 0 8px 8px}}
.fone{{position:absolute;background:#1F1235;border-radius:46px;padding:14px;box-shadow:0 50px 90px -40px rgba(31,18,53,.7)}}
.fone .scr{{background:#fff;border-radius:34px;overflow:hidden;position:relative}} .fone .scr img{{position:absolute;left:0;top:0}}
.fone .notch{{position:absolute;left:50%;top:14px;transform:translateX(-50%);width:36%;height:26px;background:#1F1235;border-radius:0 0 18px 18px;z-index:2}}
.tag{{position:absolute;background:#3B1F5E;color:#fff;font-family:'IBM Plex Mono';border-radius:999px;z-index:5;white-space:nowrap}} .uva .tag{{background:#FFC83D;color:#3B1F5E}}
.uva .lap,.uva .fone{{background:#120A22}} .uva .lap .base{{background:linear-gradient(#1F1235,#120A22)}}
"""
def dispositivos(x,y,escala,lap,fone,tag1,tag2,fone_zoom=2.0):
    lw=int(1100*escala); lh=int(660*escala); fw=int(330*escala); fh=int(680*escala); ft=max(22,int(22*escala))
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{lw+int(180*escala)}px;height:{lh+int(200*escala)}px">
      <div class="lap" style="left:0;top:0;width:{lw}px"><div class="scr" style="height:{lh-int(52*escala)}px"><img src="data:image/png;base64,{b64(lap)}"></div><div class="base"></div></div>
      <div class="fone" style="left:{lw-int(150*escala)}px;top:{int(140*escala)}px;width:{fw}px;height:{fh}px"><div class="notch"></div><div class="scr" style="height:100%"><img src="data:image/png;base64,{b64(fone)}" style="width:{int(fw*fone_zoom)}px;left:{-int(fw*0.02)}px;top:0"></div></div>
      <div class="tag" style="left:{int(40*escala)}px;top:{lh-int(20*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag1}</div>
      <div class="tag" style="right:0;top:{int(140*escala)+fh+int(16*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag2}</div>
    </div>'''
def fone_so(x,y,w,img,zoom=2.0,tag=None):
    h=int(w*2.06)
    t=f'<div class="tag" style="left:{x-10}px;top:{y+h+18}px;font-size:24px;padding:11px 20px">{tag}</div>' if tag else ''
    return f'''<div class="fone" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="notch"></div><div class="scr" style="height:100%"><img src="data:image/png;base64,{b64(img)}" style="width:{int(w*zoom)}px;left:{-int(w*0.02)}px;top:0"></div></div>{t}'''
def barra(label,val,pct,cor='#3B1F5E'):
    return f'<div style="display:flex;align-items:center;gap:20px;margin:18px 0"><div style="width:250px;font-size:30px;font-weight:600">{label}</div><div style="flex:1;height:52px;background:rgba(122,90,168,.12);border-radius:999px;overflow:hidden"><div style="width:{pct}%;height:100%;background:{cor};border-radius:999px"></div></div><div class="mono" style="width:120px;text-align:right;font-size:28px">{val}</div></div>'
POSTS=[]
def post(n,tema,eyebrow,rod_dir,corpo):
    POSTS.append((n,tema,f'<div class="topo">{LOGOB if tema=="uva" else LOGO}</div><div class="eyebrow">{eyebrow}</div>{corpo}<div class="rod"><span>seusociogestor.com.br</span><span>{rod_dir}</span></div>'))
# ---------- 6 institucionais ----------
post(1,'creme','01 · quem somos','Kits de gestão prontos',f'''
<div class="t h" style="font-size:96px">Você sabe fazer o seu trabalho. A gestão dele <em>veio sem manual.</em></div>
<div class="sub" style="top:640px;font-size:38px">O Seu Sócio Gestor é o sócio que cuida da parte que ninguém te ensinou: planilhas prontas, prompts de IA e manual. Você baixa, preenche e fecha o mês.</div>
<div style="position:absolute;left:72px;top:920px;display:flex;gap:18px;flex-wrap:wrap">
  <span class="pill" style="height:84px;font-size:32px;padding:0 34px">Planilhas + IA</span><span class="pill" style="height:84px;font-size:32px;padding:0 34px;background:#fff;border:3px solid #3B1F5E">Pagamento único</span><span class="pill" style="height:84px;font-size:32px;padding:0 34px;background:#fff;border:3px solid #3B1F5E">Sem mensalidade</span>
</div>''')
post(2,'uva','02 · como funciona','Planilha pronta + prompt pronto',f'''
<div class="t h">Como um kit <em>trabalha</em> por você</div>
<div style="position:absolute;left:72px;right:72px;top:440px;display:grid;gap:22px">
  <div class="card" style="display:flex;gap:28px;align-items:center"><div class="num">1</div><div><b>Preencher</b><span>A planilha já vem montada, com exemplo. Você troca pelos seus números. Só as células amarelas.</span></div></div>
  <div style="text-align:center;color:#FFC83D;font-size:40px;margin:-6px 0">▼</div>
  <div class="card" style="display:flex;gap:28px;align-items:center"><div class="num">2</div><div><b>Perguntar</b><span>Copia o prompt pronto, cola o bloco de números e a IA devolve o texto, a análise ou o roteiro.</span></div></div>
  <div style="text-align:center;color:#FFC83D;font-size:40px;margin:-6px 0">▼</div>
  <div class="card" style="display:flex;gap:28px;align-items:center"><div class="num">3</div><div><b>Entregar</b><span>Revisa com o checklist e manda: relatório, e-mail, apresentação.</span></div></div>
</div>''')
post(3,'lav','03 · sem surpresa','O que o kit é, e o que não é',f'''
<div class="t h" style="font-size:84px">Antes de você pagar, <em>o que é e o que não é.</em></div>
<div style="position:absolute;left:72px;right:72px;top:470px">
  <div class="lin"><span class="ok">✓</span>Planilhas prontas, com fórmulas protegidas</div>
  <div class="lin"><span class="ok">✓</span>Prompts de IA com exemplo e o que conferir</div>
  <div class="lin"><span class="ok">✓</span>Arquivos seus para sempre: Excel, Sheets e celular</div>
  <div class="lin"><span class="x">✕</span>Software com login e mensalidade</div>
  <div class="lin"><span class="x">✕</span>Curso longo ou mentoria</div>
  <div class="lin" style="border-bottom:2px solid #DCD2EC"><span class="x">✕</span>Promessa de lucro</div>
</div>''')
post(4,'creme','04 · faça a conta','Tempo que não volta',f'''
<div class="t h" style="font-size:84px">Quanto custa montar <em>tudo do zero?</em></div>
<div style="position:absolute;left:72px;right:72px;top:470px">
  {barra('Planilha da semana','1 h',17)}{barra('Relatório do mês','2 h',33)}{barra('Slides da reunião','2 h',33)}{barra('Controle do dinheiro','1 h',17)}
  <div style="display:flex;align-items:baseline;gap:20px;margin-top:40px"><span class="t" style="font-size:150px">300 h</span><span style="font-size:34px;color:#5A4A78;line-height:1.2">por ano montando<br>o que já podia estar pronto</span></div>
</div>
<div style="position:absolute;left:72px;top:1120px" class="sub">6 horas por semana × 50 semanas. Um kit pronto custa menos que uma hora do seu trabalho.</div>''')
post(5,'uva','05 · o método','Estruturar · Preencher · Perguntar · Entregar',f'''
<div class="t h" style="font-size:84px">Quatro passos. <em>Um método.</em></div>
<div style="position:absolute;left:72px;right:72px;top:440px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
  <div class="card"><div class="mono" style="font-size:24px;color:#FFC83D;margin-bottom:10px">01</div><b>Estruturar</b><span>Quem lê, quando, para decidir o quê. Antes de abrir o Excel.</span></div>
  <div class="card"><div class="mono" style="font-size:24px;color:#FFC83D;margin-bottom:10px">02</div><b>Preencher</b><span>A planilha já vem pronta. Você troca os exemplos pelos seus números.</span></div>
  <div class="card"><div class="mono" style="font-size:24px;color:#FFC83D;margin-bottom:10px">03</div><b>Perguntar</b><span>Prompt pronto, com o campo certo para colar o bloco da planilha.</span></div>
  <div class="card"><div class="mono" style="font-size:24px;color:#FFC83D;margin-bottom:10px">04</div><b>Entregar</b><span>Modelo de slides e checklist. O que sai passou por você.</span></div>
</div>
<div class="sub" style="top:1110px">O Essencial tem os três últimos passos. O Completo tem os quatro.</div>''')
post(6,'lav','06 · quem faz','Empresa de dados, não guru',f'''
<div class="t h" style="font-size:84px">Feito por uma empresa de dados, <em>não por um guru.</em></div>
<div style="position:absolute;left:72px;right:72px;top:500px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
  <div class="card"><b>Sem apresentador</b><span>O produto funciona sozinho, com manual e demonstração em tela.</span></div>
  <div class="card"><b>7 dias para desistir</b><span>Sem explicar. O valor volta pelo mesmo meio.</span></div>
  <div class="card"><b>Pix ou cartão</b><span>Acesso imediato após a aprovação. Nota fiscal.</span></div>
  <div class="card"><b>CNPJ no rodapé</b><span>ZTRAINING SERVICE LTDA, Barueri/SP. Suporte por e-mail.</span></div>
</div>
<div class="sub" style="top:1090px">Sem depoimento inventado. Quando houver avaliações de compradores, elas aparecem com autorização.</div>''')
# ---------- 3 do Essencial ----------
post(7,'creme','07 · kit essencial','Kit IA no Trabalho · Essencial',f'''
<div class="t h" style="font-size:80px">3 planilhas prontas + 40 prompts de IA. <em>R$ 37, uma vez.</em></div>
{dispositivos(72,470,0.7,DE/'tela-relatorio-painel.png',DE/'tela-ganhos-painel.png','Relatório Mensal Pronto','Ganhos e Gastos',2.6)}
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 37</div>
<div class="mono" style="position:absolute;left:520px;top:1170px;font-size:24px;color:#7A5AA8;line-height:1.35">Pix ou cartão<br>7 dias para desistir</div>''')
post(8,'uva','08 · o que vem','Kit IA no Trabalho · Essencial',f'''
<div class="t h" style="font-size:84px">Sete arquivos, <em>todos seus.</em></div>
<div style="position:absolute;left:72px;right:72px;top:420px">
  <div class="lin"><span class="num" style="width:60px;height:60px;font-size:30px">1</span>Semana Organizada · o que fazer primeiro</div>
  <div class="lin"><span class="num" style="width:60px;height:60px;font-size:30px">2</span>Relatório Mensal Pronto · painel e resumo</div>
  <div class="lin"><span class="num" style="width:60px;height:60px;font-size:30px">3</span>Ganhos e Gastos · quanto sobrou, para onde foi</div>
  <div class="lin"><span class="num" style="width:60px;height:60px;font-size:30px">4</span>40 prompts com exemplo e o que conferir</div>
  <div class="lin"><span class="num" style="width:60px;height:60px;font-size:30px">5</span>Mini-manual: comece em 15 minutos</div>
  <div class="lin"><span class="num" style="width:60px;height:60px;font-size:30px">6</span>3 vídeos de demonstração, tela real</div>
  <div class="lin" style="border-bottom:2px solid rgba(255,255,255,.16)"><span class="num" style="width:60px;height:60px;font-size:30px">7</span>Modelo de 8 slides + checklist</div>
</div>
<div style="position:absolute;left:72px;top:1150px" class="pill">R$ 37 · pagamento único</div>''')
post(9,'lav','09 · tela real','Kit IA no Trabalho · Essencial',f'''
<div class="t h" style="font-size:80px">Você digita as tarefas. A aba Hoje <em>decide a ordem.</em></div>
{fone_so(600,440,340,DE/'tela-semana-hoje.png',2.1,'Tela real. Dados fictícios.')}
<div style="position:absolute;left:72px;top:520px;width:440px;display:grid;gap:18px">
  <div class="card" style="padding:26px 28px"><b style="font-size:32px">Atrasadas, hoje, esta semana</b><span style="font-size:26px">contadas sozinhas</span></div>
  <div class="card" style="padding:26px 28px"><b style="font-size:32px">O que fazer primeiro</b><span style="font-size:26px">impacto × urgência × prazo</span></div>
  <div class="card" style="padding:26px 28px"><b style="font-size:32px">Carga dos 7 dias</b><span style="font-size:26px">aviso quando o dia não cabe</span></div>
</div>
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 37</div>''')
# ---------- 3 do Completo ----------
post(10,'creme','10 · kit completo','Kit IA no Trabalho · Completo',f'''
<div class="t h" style="font-size:80px">10 planilhas, 80 prompts e 8 aulas curtas. <em>Método, não braço.</em></div>
{dispositivos(72,470,0.7,DC/'tela-metas-painel.png',DC/'tela-projetos-painel.png','Metas do Trimestre','Projetos e Prazos',2.6)}
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 197</div>
<div class="mono" style="position:absolute;left:560px;top:1170px;font-size:24px;color:#7A5AA8;line-height:1.35">Pix ou 12× no cartão<br>7 dias para desistir</div>''')
tiles=['Semana Organizada','Relatório Mensal','Ganhos e Gastos','Projetos e Prazos','Ata e Pendências','Metas do Trimestre','Orçamento Previsto × Realizado','Funil de Propostas','Horas e Custo por Projeto','Base Limpa']
tile_html=''.join(f'<div class="card" style="padding:24px 26px;display:flex;gap:18px;align-items:center"><span class="mono" style="font-size:24px;color:#FFC83D">{i+1:02d}</span><b style="font-size:30px;margin:0">{t}</b></div>' for i,t in enumerate(tiles))
post(11,'uva','11 · as dez planilhas','Kit IA no Trabalho · Completo',f'''
<div class="t h" style="font-size:84px">Dez planilhas, <em>uma pergunta cada.</em></div>
<div style="position:absolute;left:72px;right:72px;top:420px;display:grid;grid-template-columns:1fr 1fr;gap:18px">{tile_html}</div>
<div class="sub" style="top:1130px;font-size:32px">Todas com exemplo preenchido, fórmulas protegidas e aba "Como usar". Excel, Google Sheets e celular.</div>''')
post(12,'lav','12 · para quem é','Kit IA no Trabalho · Completo',f'''
<div class="t h" style="font-size:84px">É para você se <em>entrega para alguém.</em></div>
<div style="position:absolute;left:72px;right:72px;top:460px">
  <div class="lin"><span class="ok">✓</span>Entrega planilha, relatório ou apresentação para chefe, cliente ou sócio</div>
  <div class="lin"><span class="ok">✓</span>Já usa Excel ou Sheets "no braço" e sabe que dá para fazer melhor</div>
  <div class="lin"><span class="ok">✓</span>Já abriu o ChatGPT e sentiu que podia usar para mais do que e-mail</div>
  <div class="lin" style="border-bottom:2px solid #DCD2EC"><span class="ok">✓</span>Quer método e arquivo pronto, não teoria</div>
</div>
<div style="position:absolute;left:72px;top:1060px;display:flex;align-items:center;gap:28px"><span class="pill">R$ 197 · uma vez</span><span class="mono" style="font-size:26px;color:#7A5AA8;line-height:1.3">ou 12× de R$ 19,90<br>7 dias para desistir</span></div>''')
# ---------- 3 do Kit para Advogados ----------
post(13,'creme','13 · para advogados','Kit de Gestão para Advogados',f'''
<div class="t h" style="font-size:80px">Você advoga o dia inteiro. O escritório, <em>quem administra?</em></div>
{dispositivos(72,470,0.7,DA/'tela-17.png',DA/'tela-01.png','Painel do Escritório','Agenda de Prazos',2.6)}
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 497</div>
<div class="mono" style="position:absolute;left:560px;top:1170px;font-size:24px;color:#7A5AA8;line-height:1.35">Pix ou 12× no cartão<br>7 dias para desistir</div>''')
post(14,'uva','14 · cinco núcleos','Kit de Gestão para Advogados',f'''
<div class="t h" style="font-size:84px">Cinco núcleos, <em>vinte planilhas.</em></div>
<div style="position:absolute;left:72px;right:72px;top:430px;display:grid;gap:18px">
  <div class="card" style="display:flex;gap:24px;align-items:center;padding:20px 30px"><div class="num" style="width:60px;height:60px;font-size:30px">1</div><div><b style="font-size:34px">Prazos</b><span>agenda com semáforo, andamento, rotina, checklist</span></div></div>
  <div class="card" style="display:flex;gap:24px;align-items:center;padding:20px 30px"><div class="num" style="width:60px;height:60px;font-size:30px">2</div><div><b style="font-size:34px">Honorários</b><span>custo-hora, simulador, proposta, tabela de referência</span></div></div>
  <div class="card" style="display:flex;gap:24px;align-items:center;padding:20px 30px"><div class="num" style="width:60px;height:60px;font-size:30px">3</div><div><b style="font-size:34px">Caixa</b><span>caixa, provisão de impostos, pró-labore, reserva</span></div></div>
  <div class="card" style="display:flex;gap:24px;align-items:center;padding:20px 30px"><div class="num" style="width:60px;height:60px;font-size:30px">4</div><div><b style="font-size:34px">Carteira</b><span>clientes e casos, parcelas e cobrança, funil, horas</span></div></div>
  <div class="card" style="display:flex;gap:24px;align-items:center;padding:20px 30px"><div class="num" style="width:60px;height:60px;font-size:30px">5</div><div><b style="font-size:34px">Painel</b><span>painel de sexta, resultado, metas, resumo para a IA</span></div></div>
</div>
<div class="sub" style="top:1185px;font-size:28px">Nada de peça ou orientação jurídica. É gestão do escritório. R$ 497, uma vez.</div>''')
post(15,'lav','15 · custo-hora','Kit de Gestão para Advogados',f'''
<div class="t h" style="font-size:80px">Quanto custa <em>a sua hora?</em></div>
{fone_so(600,440,340,DA/'tela-05.png',2.2,'Tela real. Escritório fictício.')}
<div style="position:absolute;left:72px;top:520px;width:440px;display:grid;gap:18px">
  <div class="card" style="padding:26px 28px"><b style="font-size:32px">Custos + pró-labore</b><span style="font-size:26px">divididos pelas horas faturáveis</span></div>
  <div class="card" style="padding:26px 28px"><b style="font-size:32px">Hora mínima a cobrar</b><span style="font-size:26px">com impostos e margem</span></div>
  <div class="card" style="padding:26px 28px"><b style="font-size:32px">Proposta com margem</b><span style="font-size:26px">fixo, hora, êxito ou misto</span></div>
</div>
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 497</div>''')
# ---------- render ----------
out=ROOT/'trabalho'; out.mkdir(exist_ok=True); alvo=int(sys.argv[1]) if len(sys.argv)>1 else None; jobs=[]
for n,tema,corpo in POSTS:
    if alvo and n!=alvo: continue
    (out/f'post-{n:02d}.html').write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{tema}">{corpo}</body></html>')
    jobs.append([f'post-{n:02d}',W,H])
js=f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox']}});
for(const [n,w,h] of {json.dumps(jobs)}){{ const p=await b.newPage({{viewport:{{width:w,height:h}}}}); await p.goto('file://{out}/'+n+'.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
 const over=await p.evaluate(()=>[...document.querySelectorAll('body *')].filter(e=>{{const r=e.getBoundingClientRect();return r.width>0&&(r.right>1080+1||r.bottom>1350+1)}}).map(e=>e.className+':'+Math.round(e.getBoundingClientRect().bottom)).slice(0,3));
 if(over.length) console.log('ESTOURO',n,JSON.stringify(over));
 await p.screenshot({{path:'{ROOT}/'+n+'-1080x1350.png'}}); await p.close(); }} await b.close(); console.log('ok');}})();"""
(out/'shot.js').write_text(js)
subprocess.run(['node',str(out/'shot.js')],check=True,env={**os.environ,'NODE_PATH':str(S/'pw'/'node_modules')})
# prévia do feed: 3 colunas, do mais recente (12) ao mais antigo (1)
if not alvo:
    from PIL import Image
    N=len(POSTS); ims=[Image.open(ROOT/f'post-{n:02d}-1080x1350.png').resize((360,450)) for n in range(N,0,-1)]
    rows=(N+2)//3; g=Image.new('RGB',(3*360+2*6,rows*450+(rows-1)*6),'#fff')
    for i,im in enumerate(ims): g.paste(im,((i%3)*366,(i//3)*456))
    g.save(ROOT/'previa-feed.jpg',quality=85); print('prévia ok')
