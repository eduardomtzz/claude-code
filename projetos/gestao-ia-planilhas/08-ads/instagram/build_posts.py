#!/usr/bin/env python3
"""18 posts de feed do Instagram (1080×1350) com direção visual única: 6 institucionais, 3 do Essencial, 3 do Completo,
3 do Kit para Advogados, 3 do Kit para Médicos. Também gera a prévia do feed (3 colunas, ordem de publicação invertida).

Uso:
  python3 build_posts.py [n]            feed 4:5   -> post-NN-1080x1350.png + previa-feed.jpg
  python3 build_posts.py --stories [n]  stories 9:16 -> stories/story-NN-1080x1920.png + stories/previa-stories.jpg

Stories/Reels: as mesmas 18 peças (mesmos títulos e blocos de conteúdo), em 1080×1920, com zona segura de 250 px no
topo e 340 px na base (áreas cobertas pela interface do Instagram). Elementos maiores, mockups maiores, e rodapé de CTA
"Link na bio · seusociogestor.com.br" com o preço nos posts de produto. O render avisa (ESTOURO / PILULA) quando algo
sai da zona segura ou quando uma pílula/tag quebra linha."""
import pathlib, base64, subprocess, os, sys, json
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parents[1]
S=pathlib.Path('/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad')
DE=PROJ/'produto'/'kit-essencial'/'docs'; DC=PROJ/'produto'/'kit-completo'/'docs'; DA=PROJ/'produto'/'kit-advogados'/'docs'; DM=PROJ/'produto'/'kit-medicos'/'docs'; FONTS=PROJ/'site'/'public'/'assets'/'fonts'
b64=lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO=(PROJ/'03-marca'/'logo'/'logo-horizontal.svg').read_text(); LOGOB=(PROJ/'03-marca'/'logo'/'logo-branco.svg').read_text()
EMP=(PROJ/'03-marca'/'logo'/'logo-empilhado.svg').read_text(); EMPB=(PROJ/'03-marca'/'logo'/'logo-empilhado-branco.svg').read_text()
SIMB=(PROJ/'03-marca'/'logo'/'simbolo.svg').read_text()
ARGS=sys.argv[1:]; STORY='--stories' in ARGS; alvo=next((int(a) for a in ARGS if a.isdigit()),None)
W,H=(1080,1920) if STORY else (1080,1350)
TOPO_SEG,BASE_SEG=(250,340) if STORY else (0,0)   # zona coberta pela interface (stories)
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
.pill{{display:inline-flex;align-items:center;justify-content:center;background:#FFC83D;color:#3B1F5E;border-radius:999px;font-family:'Bricolage Grotesque';font-weight:800;padding:0 44px;height:104px;font-size:42px;white-space:nowrap}}
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
# Stories 9:16: logo e eyebrow logo abaixo da zona coberta do topo; .area é a coluna útil (flex) entre 352 e 1520 px;
# rodapé "Link na bio" em cima da zona coberta da base. Tudo maior que no feed.
CSS_STORY=f"""
.topo{{top:250px;width:340px}} .topo svg{{width:340px}} .eyebrow{{top:266px;font-size:24px}}
.rod{{bottom:352px;font-size:24px}}
.area{{position:absolute;left:72px;right:72px;top:352px;height:{1520-352}px;display:flex;flex-direction:column}}
.area>*{{flex:none}} .area .t{{font-size:100px}}
.meio{{flex:1 0 auto;display:flex;flex-direction:column;justify-content:center;padding:28px 0}}
.cta{{display:flex;align-items:center;gap:32px}} .cta .pill{{height:112px;font-size:44px;padding:0 48px}}
.cta .mono{{font-size:26px;color:#7A5AA8;line-height:1.35;white-space:nowrap}} .uva .cta .mono{{color:#D9C8F5}}
.compacto .lin{{font-size:36px;padding:22px 0}}
.sub{{position:static;font-size:40px}}
.card{{padding:36px 40px;border-radius:32px}} .card b{{font-size:42px}} .card span{{font-size:31px}}
.lin{{font-size:38px;padding:26px 0}} .ok,.x{{width:64px;height:64px;font-size:34px}} .num{{width:80px;height:80px;font-size:42px}}
"""
def dispositivos(x,y,escala,lap,fone,tag1,tag2,fone_zoom=2.0,fone_off=150):
    """Notebook + celular sobreposto. fone_off: quanto o celular avança sobre o notebook (px antes da escala)."""
    lw=int(1100*escala); lh=int(660*escala); fw=int(330*escala); fh=int(680*escala); ft=max(22,int(22*escala))
    ch=max(lh+int(200*escala),int(140*escala)+fh+int(16*escala)+int(ft*1.9)+4)
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{lw-int(fone_off*escala)+fw}px;height:{ch}px">
      <div class="lap" style="left:0;top:0;width:{lw}px"><div class="scr" style="height:{lh-int(52*escala)}px"><img src="data:image/png;base64,{b64(lap)}"></div><div class="base"></div></div>
      <div class="fone" style="left:{lw-int(fone_off*escala)}px;top:{int(140*escala)}px;width:{fw}px;height:{fh}px"><div class="notch"></div><div class="scr" style="height:100%"><img src="data:image/png;base64,{b64(fone)}" style="width:{int(fw*fone_zoom)}px;left:{-int(fw*0.02)}px;top:0"></div></div>
      <div class="tag" style="left:{int(40*escala)}px;top:{lh-int(20*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag1}</div>
      <div class="tag" style="right:0;top:{int(140*escala)+fh+int(16*escala)}px;font-size:{ft}px;padding:{int(ft*.45)}px {int(ft*.8)}px">{tag2}</div>
    </div>'''
def fone_so(x,y,w,img,zoom=2.0,tag=None,tag_fs=24):
    h=int(w*2.06)
    t=f'<div class="tag" style="left:{x-10}px;top:{y+h+18}px;font-size:{tag_fs}px;padding:{tag_fs*11//24}px {tag_fs*20//24}px">{tag}</div>' if tag else ''
    return f'''<div class="fone" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="notch"></div><div class="scr" style="height:100%"><img src="data:image/png;base64,{b64(img)}" style="width:{int(w*zoom)}px;left:{-int(w*0.02)}px;top:0"></div></div>{t}'''
def barra(label,val,pct,cor='#3B1F5E',lw=250,fs=30,h=52,vfs=28,m=18):
    return f'<div style="display:flex;align-items:center;gap:20px;margin:{m}px 0"><div style="width:{lw}px;font-size:{fs}px;font-weight:600">{label}</div><div style="flex:1;height:{h}px;background:rgba(122,90,168,.12);border-radius:999px;overflow:hidden"><div style="width:{pct}%;height:100%;background:{cor};border-radius:999px"></div></div><div class="mono" style="width:120px;text-align:right;font-size:{vfs}px">{val}</div></div>'
# ---------- blocos de conteúdo compartilhados entre feed e stories ----------
T={1:'Você sabe fazer o seu trabalho. A gestão dele <em>veio sem manual.</em>',2:'Como um kit <em>trabalha</em> por você',
   3:'Antes de você pagar, <em>o que é e o que não é.</em>',4:'Quanto custa montar <em>tudo do zero?</em>',5:'Quatro passos. <em>Um método.</em>',
   6:'Feito por uma empresa de dados, <em>não por um guru.</em>',7:'3 planilhas prontas + 40 prompts de IA. <em>R$ 37, uma vez.</em>',
   8:'Sete arquivos, <em>todos seus.</em>',9:'Você digita as tarefas. A aba Hoje <em>decide a ordem.</em>',
   10:'10 planilhas, 80 prompts e 8 aulas curtas. <em>Método, não braço.</em>',11:'Dez planilhas, <em>uma pergunta cada.</em>',
   12:'É para você se <em>entrega para alguém.</em>',13:'Você advoga o dia inteiro. O escritório, <em>quem administra?</em>',
   14:'Cinco núcleos, <em>vinte planilhas.</em>',15:'Quanto custa <em>a sua hora?</em>',
   16:'Você atende o dia inteiro. A clínica, <em>quem administra?</em>',17:'Agenda, preço, caixa, convênios <em>e painel.</em>',18:'O convênio paga em 60 dias. <em>Vale a pena?</em>'}
SUB1='O Seu Sócio Gestor é o sócio que cuida da parte que ninguém te ensinou: planilhas prontas, prompts de IA e manual. Você baixa, preenche e fecha o mês.'
def pills1(h=84,fs=32,p=34):
    st=f'height:{h}px;font-size:{fs}px;padding:0 {p}px'
    return f'<span class="pill" style="{st}">Planilhas + IA</span><span class="pill" style="{st};background:#fff;border:3px solid #3B1F5E">Pagamento único</span><span class="pill" style="{st};background:#fff;border:3px solid #3B1F5E">Sem mensalidade</span>'
PASSOS2=[('Preencher','A planilha já vem montada, com exemplo. Você troca pelos seus números. Só as células amarelas.'),
         ('Perguntar','Copia o prompt pronto, cola o bloco de números e a IA devolve o texto, a análise ou o roteiro.'),
         ('Entregar','Revisa com o checklist e manda: relatório, e-mail, apresentação.')]
def passos2(seta=40):
    s=f'<div style="text-align:center;color:#FFC83D;font-size:{seta}px;margin:-6px 0">▼</div>'
    return s.join(f'<div class="card" style="display:flex;gap:28px;align-items:center"><div class="num">{i+1}</div><div><b>{b}</b><span>{t}</span></div></div>' for i,(b,t) in enumerate(PASSOS2))
def linhas(itens,fecha,num=None):
    """itens: lista de (classe, texto) com classe ok/x, ou textos (numerados quando num=(w,fs))."""
    out=[]
    for i,it in enumerate(itens):
        ult=f' style="border-bottom:2px solid {fecha}"' if i==len(itens)-1 else ''
        if num: out.append(f'<div class="lin"{ult}><span class="num" style="width:{num[0]}px;height:{num[0]}px;font-size:{num[1]}px">{i+1}</span>{it}</div>')
        else: out.append(f'<div class="lin"{ult}><span class="{it[0]}">{"✓" if it[0]=="ok" else "✕"}</span>{it[1]}</div>')
    return ''.join(out)
LIN3=[('ok','Planilhas prontas, com fórmulas protegidas'),('ok','Prompts de IA com exemplo e o que conferir'),('ok','Arquivos seus para sempre: Excel, Sheets e celular'),
      ('x','Software com login e mensalidade'),('x','Curso longo ou mentoria'),('x','Promessa de lucro')]
LIN8=['Semana Organizada · o que fazer primeiro','Relatório Mensal Pronto · painel e resumo','Ganhos e Gastos · quanto sobrou, para onde foi','40 prompts com exemplo e o que conferir',
      'Mini-manual: comece em 15 minutos','3 vídeos de demonstração, tela real','Modelo de 8 slides + checklist']
LIN12=[('ok','Entrega planilha, relatório ou apresentação para chefe, cliente ou sócio'),('ok','Já usa Excel ou Sheets "no braço" e sabe que dá para fazer melhor'),
       ('ok','Já abriu o ChatGPT e sentiu que podia usar para mais do que e-mail'),('ok','Quer método e arquivo pronto, não teoria')]
PASSOS5=[('Estruturar','Quem lê, quando, para decidir o quê. Antes de abrir o Excel.'),('Preencher','A planilha já vem pronta. Você troca os exemplos pelos seus números.'),
         ('Perguntar','Prompt pronto, com o campo certo para colar o bloco da planilha.'),('Entregar','Modelo de slides e checklist. O que sai passou por você.')]
def cards5(fs=24): return ''.join(f'<div class="card"><div class="mono" style="font-size:{fs}px;color:#FFC83D;margin-bottom:10px">0{i+1}</div><b>{b}</b><span>{t}</span></div>' for i,(b,t) in enumerate(PASSOS5))
SUB5='O Essencial tem os três últimos passos. O Completo tem os quatro.'
CARDS6=''.join(f'<div class="card"><b>{b}</b><span>{t}</span></div>' for b,t in [('Sem apresentador','O produto funciona sozinho, com manual e demonstração em tela.'),
        ('7 dias para desistir','Sem explicar. O valor volta pelo mesmo meio.'),('Pix ou cartão','Acesso imediato após a aprovação. Nota fiscal.'),('CNPJ no rodapé','ZTRAINING SERVICE LTDA, Barueri/SP. Suporte por e-mail.')])
SUB6='Sem depoimento inventado. Quando houver avaliações de compradores, elas aparecem com autorização.'
BARRAS4=[('Planilha da semana','1 h',17),('Relatório do mês','2 h',33),('Slides da reunião','2 h',33),('Controle do dinheiro','1 h',17)]
SUB4='6 horas por semana × 50 semanas. Um kit pronto custa menos que uma hora do seu trabalho.'
CARDS9=[('Atrasadas, hoje, esta semana','contadas sozinhas'),('O que fazer primeiro','impacto × urgência × prazo'),('Carga dos 7 dias','aviso quando o dia não cabe')]
CARDS15=[('Custos + pró-labore','divididos pelas horas faturáveis'),('Hora mínima a cobrar','com impostos e margem'),('Proposta com margem','fixo, hora, êxito ou misto')]
def cards_lado(itens,bfs=32,sfs=26,pad='26px 28px'): return ''.join(f'<div class="card" style="padding:{pad}"><b style="font-size:{bfs}px">{b}</b><span style="font-size:{sfs}px">{s}</span></div>' for b,s in itens)
tiles=['Semana Organizada','Relatório Mensal','Ganhos e Gastos','Projetos e Prazos','Ata e Pendências','Metas do Trimestre','Orçamento Previsto × Realizado','Funil de Propostas','Horas e Custo por Projeto','Base Limpa']
def tiles_html(pad='24px 26px',nfs=24,bfs=30): return ''.join(f'<div class="card" style="padding:{pad};display:flex;gap:18px;align-items:center"><span class="mono" style="font-size:{nfs}px;color:#FFC83D">{i+1:02d}</span><b style="font-size:{bfs}px;margin:0">{t}</b></div>' for i,t in enumerate(tiles))
SUB11='Todas com exemplo preenchido, fórmulas protegidas e aba "Como usar". Excel, Google Sheets e celular.'
NUCLEOS14=[('Prazos','agenda com semáforo, andamento, rotina, checklist'),('Honorários','custo-hora, simulador, proposta, tabela de referência'),('Caixa','caixa, provisão de impostos, pró-labore, reserva'),
           ('Carteira','clientes e casos, parcelas e cobrança, funil, horas'),('Painel','painel de sexta, resultado, metas, resumo para a IA')]
def nucleos14(pad='20px 30px',num=(60,30),bfs=34,sfs=None,itens=None):
    s=f' style="display:block;font-size:{sfs}px"' if sfs else ''
    return ''.join(f'<div class="card" style="display:flex;gap:24px;align-items:center;padding:{pad}"><div class="num" style="width:{num[0]}px;height:{num[0]}px;font-size:{num[1]}px">{i+1}</div><div><b style="font-size:{bfs}px">{b}</b><span{s}>{t}</span></div></div>' for i,(b,t) in enumerate(itens or NUCLEOS14))
SUB14='Nada de peça ou orientação jurídica. É gestão do escritório. R$ 497, uma vez.'
NUCLEOS17=[('Agenda','ocupação por sala, faltas, lista de retorno, rotina'),('Preço','custo da hora, precificação, simulador de convênio'),('Caixa','caixa, provisão de impostos e 13º, repasse, reserva'),
           ('Recebíveis','convênios e glosa, parcelas, orçamentos, cartão'),('Painel','painel de sexta, resultado, metas, resumo para a IA')]
SUB17='Nada clínico, nada de prontuário: é gestão da clínica. R$ 697, uma vez.'
CARDS18=[('Custo cheio da consulta','hora de atendimento + material'),('Tabela, prazo e glosa','o líquido real de cada convênio'),('Líquido por hora','contra a hora mínima a cobrar')]
POSTS=[]
def post(n,tema,eyebrow,rod_dir,corpo):
    POSTS.append((n,tema,f'<div class="topo">{LOGOB if tema=="uva" else LOGO}</div><div class="eyebrow">{eyebrow}</div>{corpo}<div class="rod"><span>seusociogestor.com.br</span><span>{rod_dir}</span></div>'))
# ---------- 6 institucionais ----------
post(1,'creme','01 · quem somos','Kits de gestão prontos',f'''
<div class="t h" style="font-size:96px">{T[1]}</div>
<div class="sub" style="top:640px;font-size:38px">{SUB1}</div>
<div style="position:absolute;left:72px;top:920px;display:flex;gap:18px;flex-wrap:wrap">
  {pills1()}
</div>''')
post(2,'uva','02 · como funciona','Planilha pronta + prompt pronto',f'''
<div class="t h">{T[2]}</div>
<div style="position:absolute;left:72px;right:72px;top:440px;display:grid;gap:22px">
  {passos2()}
</div>''')
post(3,'lav','03 · sem surpresa','O que o kit é, e o que não é',f'''
<div class="t h" style="font-size:84px">{T[3]}</div>
<div style="position:absolute;left:72px;right:72px;top:470px">
  {linhas(LIN3,'#DCD2EC')}
</div>''')
post(4,'creme','04 · faça a conta','Tempo que não volta',f'''
<div class="t h" style="font-size:84px">{T[4]}</div>
<div style="position:absolute;left:72px;right:72px;top:470px">
  {''.join(barra(*b) for b in BARRAS4)}
  <div style="display:flex;align-items:baseline;gap:20px;margin-top:40px"><span class="t" style="font-size:150px">300 h</span><span style="font-size:34px;color:#5A4A78;line-height:1.2">por ano montando<br>o que já podia estar pronto</span></div>
</div>
<div style="position:absolute;left:72px;top:1120px" class="sub">{SUB4}</div>''')
post(5,'uva','05 · o método','Estruturar · Preencher · Perguntar · Entregar',f'''
<div class="t h" style="font-size:84px">{T[5]}</div>
<div style="position:absolute;left:72px;right:72px;top:440px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
  {cards5()}
</div>
<div class="sub" style="top:1110px">{SUB5}</div>''')
post(6,'lav','06 · quem faz','Empresa de dados, não guru',f'''
<div class="t h" style="font-size:84px">{T[6]}</div>
<div style="position:absolute;left:72px;right:72px;top:500px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
  {CARDS6}
</div>
<div class="sub" style="top:1090px">{SUB6}</div>''')
# ---------- 3 do Essencial ----------
post(7,'creme','07 · kit essencial','Kit IA no Trabalho · Essencial',f'''
<div class="t h" style="font-size:80px">{T[7]}</div>
{dispositivos(72,470,0.7,DE/'tela-relatorio-painel.png',DE/'tela-ganhos-painel.png','Relatório Mensal Pronto','Ganhos e Gastos',2.6)}
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 37</div>
<div class="mono" style="position:absolute;left:520px;top:1170px;font-size:24px;color:#7A5AA8;line-height:1.35">Pix ou cartão<br>7 dias para desistir</div>''')
post(8,'uva','08 · o que vem','Kit IA no Trabalho · Essencial',f'''
<div class="t h" style="font-size:84px">{T[8]}</div>
<div style="position:absolute;left:72px;right:72px;top:420px">
  {linhas(LIN8,'rgba(255,255,255,.16)',num=(60,30))}
</div>
<div style="position:absolute;left:72px;top:1150px" class="pill">R$ 37 · pagamento único</div>''')
post(9,'lav','09 · tela real','Kit IA no Trabalho · Essencial',f'''
<div class="t h" style="font-size:80px">{T[9]}</div>
{fone_so(600,440,340,DE/'tela-semana-hoje.png',2.1,'Tela real. Dados fictícios.')}
<div style="position:absolute;left:72px;top:520px;width:440px;display:grid;gap:18px">
  {cards_lado(CARDS9)}
</div>
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 37</div>''')
# ---------- 3 do Completo ----------
post(10,'creme','10 · kit completo','Kit IA no Trabalho · Completo',f'''
<div class="t h" style="font-size:80px">{T[10]}</div>
{dispositivos(72,470,0.7,DC/'tela-metas-painel.png',DC/'tela-projetos-painel.png','Metas do Trimestre','Projetos e Prazos',2.6)}
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 197</div>
<div class="mono" style="position:absolute;left:560px;top:1170px;font-size:24px;color:#7A5AA8;line-height:1.35">Pix ou 12× no cartão<br>7 dias para desistir</div>''')
post(11,'uva','11 · as dez planilhas','Kit IA no Trabalho · Completo',f'''
<div class="t h" style="font-size:84px">{T[11]}</div>
<div style="position:absolute;left:72px;right:72px;top:420px;display:grid;grid-template-columns:1fr 1fr;gap:18px">{tiles_html()}</div>
<div class="sub" style="top:1130px;font-size:32px">{SUB11}</div>''')
post(12,'lav','12 · para quem é','Kit IA no Trabalho · Completo',f'''
<div class="t h" style="font-size:84px">{T[12]}</div>
<div style="position:absolute;left:72px;right:72px;top:460px">
  {linhas(LIN12,'#DCD2EC')}
</div>
<div style="position:absolute;left:72px;top:1060px;display:flex;align-items:center;gap:28px"><span class="pill">R$ 197 · uma vez</span><span class="mono" style="font-size:26px;color:#7A5AA8;line-height:1.3">ou 12× de R$ 19,90<br>7 dias para desistir</span></div>''')
# ---------- 3 do Kit para Advogados ----------
post(13,'creme','13 · para advogados','Kit de Gestão para Advogados',f'''
<div class="t h" style="font-size:80px">{T[13]}</div>
{dispositivos(72,470,0.7,DA/'tela-17.png',DA/'tela-01.png','Painel do Escritório','Agenda de Prazos',2.6)}
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 497</div>
<div class="mono" style="position:absolute;left:560px;top:1170px;font-size:24px;color:#7A5AA8;line-height:1.35">Pix ou 12× no cartão<br>7 dias para desistir</div>''')
post(14,'uva','14 · cinco núcleos','Kit de Gestão para Advogados',f'''
<div class="t h" style="font-size:84px">{T[14]}</div>
<div style="position:absolute;left:72px;right:72px;top:430px;display:grid;gap:18px">
  {nucleos14()}
</div>
<div class="sub" style="top:1185px;font-size:28px">{SUB14}</div>''')
post(15,'lav','15 · custo-hora','Kit de Gestão para Advogados',f'''
<div class="t h" style="font-size:80px">{T[15]}</div>
{fone_so(600,440,340,DA/'tela-05.png',2.2,'Tela real. Escritório fictício.')}
<div style="position:absolute;left:72px;top:520px;width:440px;display:grid;gap:18px">
  {cards_lado(CARDS15)}
</div>
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 497</div>''')
# ---------- 3 do Kit para Médicos ----------
post(16,'creme','16 · para médicos','Kit de Gestão para Médicos',f'''
<div class="t h" style="font-size:80px">{T[16]}</div>
{dispositivos(72,470,0.7,DM/'tela-17.png',DM/'tela-01.png','Painel da Clínica','Agenda e Ocupação',2.6)}
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 697</div>
<div class="mono" style="position:absolute;left:560px;top:1170px;font-size:24px;color:#7A5AA8;line-height:1.35">Pix ou 12× no cartão<br>7 dias para desistir</div>''')
post(17,'uva','17 · cinco núcleos','Kit de Gestão para Médicos',f'''
<div class="t h" style="font-size:84px">{T[17]}</div>
<div style="position:absolute;left:72px;right:72px;top:430px;display:grid;gap:18px">
  {nucleos14(itens=NUCLEOS17)}
</div>
<div class="sub" style="top:1185px;font-size:28px">{SUB17}</div>''')
post(18,'lav','18 · convênio na conta','Kit de Gestão para Médicos',f'''
<div class="t h" style="font-size:80px">{T[18]}</div>
{fone_so(600,440,340,DM/'tela-07.png',2.2,'Tela real. Clínica de exemplo.')}
<div style="position:absolute;left:72px;top:520px;width:440px;display:grid;gap:18px">
  {cards_lado(CARDS18)}
</div>
<div style="position:absolute;left:72px;top:1150px" class="pill">Comprar por R$ 697</div>''')

# ---------- Stories 9:16: mesmas peças, coluna útil de 352 a 1520 px ----------
STORIES=[]
def story(n,tema,eyebrow,rod_dir,meio,cta,tsize=100,titulo=None):
    STORIES.append((n,tema,f'<div class="topo">{LOGOB if tema=="uva" else LOGO}</div><div class="eyebrow">{eyebrow}</div>'
        f'<div class="area"><div class="t" style="font-size:{tsize}px">{titulo or T[n]}</div><div class="meio">{meio}</div><div class="cta">{cta}</div></div>'
        f'<div class="rod"><span>Link na bio · seusociogestor.com.br</span><span>{rod_dir}</span></div>'))
def cta(pill,mono): return f'<span class="pill">{pill}</span><span class="mono">{mono}</span>'
CTA_INST=cta('Conhecer os kits','a partir de R$ 37<br>pagamento único')
CTA_ESS=cta('Comprar por R$ 37','Pix ou cartão<br>7 dias para desistir')
CTA_COMP=cta('Comprar por R$ 197','Pix ou 12× no cartão<br>7 dias para desistir')
CTA_ADV=cta('Comprar por R$ 497','Pix ou 12× no cartão<br>7 dias para desistir')
story(1,'creme','01 · quem somos','Kits de gestão prontos',f'<div class="sub">{SUB1}</div><div style="display:flex;gap:18px;flex-wrap:wrap;margin-top:56px">{pills1(92,34,36)}</div>',CTA_INST,tsize=100)
story(2,'uva','02 · como funciona','Planilha + prompt',f'<div style="display:grid;gap:22px">{passos2(44)}</div>',CTA_INST)
story(3,'lav','03 · sem surpresa','O que é e o que não é',linhas(LIN3,'#DCD2EC'),CTA_INST,tsize=92)
story(4,'creme','04 · faça a conta','Tempo que não volta',
      ''.join(barra(*b,lw=300,fs=34,h=60,vfs=32,m=20) for b in BARRAS4)
      +'<div style="display:flex;align-items:baseline;gap:24px;margin-top:44px"><span class="t" style="font-size:170px">300 h</span><span style="font-size:36px;color:#5A4A78;line-height:1.2">por ano montando<br>o que já podia estar pronto</span></div>'
      +f'<div class="sub" style="margin-top:36px;font-size:36px">{SUB4}</div>',CTA_INST)
story(5,'uva','05 · o método','Quatro passos',f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{cards5(26)}</div><div class="sub" style="margin-top:40px">{SUB5}</div>',CTA_INST)
story(6,'lav','06 · quem faz','Empresa de dados',f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{CARDS6}</div><div class="sub" style="margin-top:40px;font-size:36px">{SUB6}</div>',CTA_INST,tsize=92)
def mock_story(lap,fone,t1,t2):
    e=0.78; ch=max(int(660*e)+int(200*e),int(140*e)+int(680*e)+int(16*e)+int(22*e*1.9)+4)
    return f'<div style="position:relative;height:{ch}px">{dispositivos(0,0,e,lap,fone,t1,t2,2.6,fone_off=240)}</div>'
story(7,'creme','07 · kit essencial','Kit Essencial · R$ 37',mock_story(DE/'tela-relatorio-painel.png',DE/'tela-ganhos-painel.png','Relatório Mensal Pronto','Ganhos e Gastos'),CTA_ESS,tsize=84)
story(8,'uva','08 · o que vem','Kit Essencial · R$ 37',f'<div class="compacto">{linhas(LIN8,"rgba(255,255,255,.16)",num=(66,32))}</div>',cta('R$ 37 · pagamento único','Pix ou cartão<br>7 dias para desistir').replace('class="pill"','class="pill" style="font-size:40px"'),tsize=100)
def fone_story(img,zoom,tag,cards):
    w=360; h=int(w*2.06); ch=h+18+56
    return f'<div style="position:relative;height:{ch}px">{fone_so(480,0,w,img,zoom,tag,tag_fs=22)}<div style="position:absolute;left:0;top:{(h-3*150-2*20)//2}px;width:470px;display:grid;gap:20px">{cards_lado(cards,34,27,"28px 30px")}</div></div>'
story(9,'lav','09 · tela real','Kit Essencial · R$ 37',fone_story(DE/'tela-semana-hoje.png',2.1,'Tela real. Dados fictícios.',CARDS9),CTA_ESS,tsize=80)
story(10,'creme','10 · kit completo','Kit Completo · R$ 197',mock_story(DC/'tela-metas-painel.png',DC/'tela-projetos-painel.png','Metas do Trimestre','Projetos e Prazos'),CTA_COMP,tsize=84)
story(11,'uva','11 · as dez planilhas','Kit Completo · R$ 197',f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">{tiles_html("26px 30px",26,33)}</div><div class="sub" style="margin-top:40px;font-size:34px">{SUB11}</div>',CTA_COMP)
story(12,'lav','12 · para quem é','Kit Completo · R$ 197',linhas(LIN12,'#DCD2EC'),cta('R$ 197 · uma vez','ou 12× de R$ 19,90<br>7 dias para desistir'),tsize=92)
story(13,'creme','13 · para advogados','Kit Advogados · R$ 497',mock_story(DA/'tela-17.png',DA/'tela-01.png','Painel do Escritório','Agenda de Prazos'),CTA_ADV,tsize=84)
story(14,'uva','14 · cinco núcleos','Kit Advogados · R$ 497',f'<div style="display:grid;gap:14px">{nucleos14("16px 30px",(62,32),35,28)}</div><div class="sub" style="margin-top:30px;font-size:29px">{SUB14}</div>',CTA_ADV)
story(15,'lav','15 · custo-hora','Kit Advogados · R$ 497',fone_story(DA/'tela-05.png',2.2,'Tela real. Escritório fictício.',CARDS15),CTA_ADV,tsize=88)
CTA_MED=cta('Comprar por R$ 697','Pix ou 12× no cartão<br>7 dias para desistir')
story(16,'creme','16 · para médicos','Kit Médicos · R$ 697',mock_story(DM/'tela-17.png',DM/'tela-01.png','Painel da Clínica','Agenda e Ocupação'),CTA_MED,tsize=84)
story(17,'uva','17 · cinco núcleos','Kit Médicos · R$ 697',f'<div style="display:grid;gap:14px">{nucleos14("16px 30px",(62,32),35,28,itens=NUCLEOS17)}</div><div class="sub" style="margin-top:30px;font-size:29px">{SUB17}</div>',CTA_MED)
story(18,'lav','18 · convênio na conta','Kit Médicos · R$ 697',fone_story(DM/'tela-07.png',2.2,'Tela real. Clínica de exemplo.',CARDS18),CTA_MED,tsize=88)

# ---------- render ----------
out=ROOT/'trabalho'; out.mkdir(exist_ok=True); jobs=[]
PECAS=STORIES if STORY else POSTS; pref='story' if STORY else 'post'; dest=ROOT/'stories' if STORY else ROOT; dest.mkdir(exist_ok=True)
for n,tema,corpo in PECAS:
    if alvo and n!=alvo: continue
    (out/f'{pref}-{n:02d}.html').write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{CSS_STORY if STORY else ""}</style></head><body class="{tema}">{corpo}</body></html>')
    jobs.append([f'{pref}-{n:02d}',W,H])
js=f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch({{executablePath:'/opt/pw-browsers/chromium',headless:true,args:['--no-sandbox']}});
for(const [n,w,h] of {json.dumps(jobs)}){{ const p=await b.newPage({{viewport:{{width:w,height:h}}}}); await p.goto('file://{out}/'+n+'.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
 const over=await p.evaluate(([T,B,W])=>[...document.querySelectorAll('body *')].filter(e=>{{if(e.tagName==='IMG'||e.closest('svg'))return false;const r=e.getBoundingClientRect();const a=e.closest('.area');const lim=a?a.getBoundingClientRect().bottom:B;return r.width>0&&r.height>0&&(r.right>W+1||r.bottom>lim+1||r.top<T-1||r.left<-1)}}).map(e=>e.className+':'+Math.round(e.getBoundingClientRect().top)+'-'+Math.round(e.getBoundingClientRect().bottom)).slice(0,4),[{TOPO_SEG},{H-BASE_SEG},{W}]);
 if(over.length) console.log('ESTOURO',n,JSON.stringify(over));
 const quebra=await p.evaluate(()=>[...document.querySelectorAll('.pill,.tag,.num,.ok,.x')].filter(e=>{{const r=document.createRange();r.selectNodeContents(e);return r.getClientRects().length>1||e.scrollWidth>e.clientWidth+1}}).map(e=>e.className+':'+e.textContent.trim()));
 if(quebra.length) console.log('PILULA',n,JSON.stringify(quebra));
 await p.screenshot({{path:'{dest}/'+n+'-{W}x{H}.png'}}); await p.close(); }} await b.close(); console.log('ok');}})();"""
(out/'shot.js').write_text(js)
subprocess.run(['node',str(out/'shot.js')],check=True,env={**os.environ,'NODE_PATH':str(S/'pw'/'node_modules')})
if not alvo:
    from PIL import Image
    N=len(PECAS)
    if STORY:   # prévia dos stories: 5 colunas, ordem 1..N
        ims=[Image.open(dest/f'story-{n:02d}-1080x1920.png').resize((216,384)) for n in range(1,N+1)]
        rows=(N+4)//5; g=Image.new('RGB',(5*216+4*6,rows*384+(rows-1)*6),'#fff')
        for i,im in enumerate(ims): g.paste(im,((i%5)*222,(i//5)*390))
        g.save(dest/'previa-stories.jpg',quality=85); print('prévia stories ok')
    else:       # prévia do feed: 3 colunas, do mais recente (N) ao mais antigo (1)
        ims=[Image.open(ROOT/f'post-{n:02d}-1080x1350.png').resize((360,450)) for n in range(N,0,-1)]
        rows=(N+2)//3; g=Image.new('RGB',(3*360+2*6,rows*450+(rows-1)*6),'#fff')
        for i,im in enumerate(ims): g.paste(im,((i%3)*366,(i//3)*456))
        g.save(ROOT/'previa-feed.jpg',quality=85); print('prévia ok')
