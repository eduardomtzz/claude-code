#!/usr/bin/env python3
"""Revisão geral dos produtos 1 a 4 antes das conexões externas.

Confere o que dá para conferir por máquina: o que a página promete existe no
pacote, os números batem entre oferta/copy/página/LEIA-ME, não sobrou marcador
de rascunho, os links internos apontam para arquivo que existe, os vídeos têm
duração e volume dentro do padrão, e as planilhas abrem sem erro de fórmula.

Uso: python3 verifica_lancamento.py [--rapido]   (--rapido pula recálculo e vídeo)
"""
import re, sys, json, pathlib, subprocess, zipfile
R = pathlib.Path(__file__).resolve().parent
RAPIDO = '--rapido' in sys.argv
falhas, avisos, ok = [], [], []
def F(cat, msg): falhas.append((cat, msg))
def A(cat, msg): avisos.append((cat, msg))
def O(msg): ok.append(msg)

KITS = {
 'essencial': dict(pagina='kit.html',      kit='kit-essencial', preco='R$ 37',
                   planilhas=3,  prompts=40, aulas=3,  slides=1),
 'completo':  dict(pagina='completo.html', kit='kit-completo',  preco='R$ 197',
                   planilhas=10, prompts=80, aulas=8,  slides=3),
 'advogados': dict(pagina='advogados.html',kit='kit-advogados', preco='R$ 497',
                   planilhas=20, prompts=40, aulas=8,  slides=3),
 'medicos':   dict(pagina='medicos.html',  kit='kit-medicos',   preco='R$ 697',
                   planilhas=20, prompts=41, aulas=8,  slides=3),
}

# ---------------------------------------------------------------- 1. entregáveis
for nome, k in KITS.items():
    ent = R/'produto'/k['kit']/'entrega'
    if not ent.is_dir(): F('entrega', f'{nome}: pasta entrega/ não existe'); continue
    xlsx = sorted(ent.glob('*.xlsx'))
    if len(xlsx) != k['planilhas']:
        F('entrega', f'{nome}: {len(xlsx)} planilhas em entrega/, a oferta diz {k["planilhas"]}')
    else: O(f'{nome}: {len(xlsx)} planilhas conferem')
    vids = sorted((ent/'videos').glob('*.mp4'))
    if len(vids) != k['aulas']:
        F('entrega', f'{nome}: {len(vids)} vídeos em entrega/videos, a página diz {k["aulas"]}')
    else: O(f'{nome}: {len(vids)} vídeos conferem')
    for obrig in ('LEIA-ME.txt',):
        if not (ent/obrig).exists(): F('entrega', f'{nome}: falta {obrig}')
    pptx = list(ent.glob('*.pptx'))
    if len(pptx) != k['slides']:
        F('entrega', f'{nome}: {len(pptx)} .pptx, a página promete {k["slides"]} modelo(s)')
    # legendas: todo vídeo entregue precisa da legenda ao lado
    for v in vids:
        if not v.with_suffix('.vtt').exists() and not v.with_suffix('.srt').exists():
            A('legenda', f'{nome}: {v.name} sem legenda .vtt/.srt')

# ------------------------------------------------------------------- 2. o zip
for nome, k in KITS.items():
    zs = list((R/'produto'/k['kit']).glob('*.zip'))
    if not zs: F('zip', f'{nome}: nenhum .zip de entrega'); continue
    z = max(zs, key=lambda p: p.stat().st_mtime)
    ent = R/'produto'/k['kit']/'entrega'
    with zipfile.ZipFile(z) as zf: dentro = {pathlib.Path(n).name for n in zf.namelist()}
    faltando = [p.name for p in ent.rglob('*') if p.is_file() and p.name not in dentro]
    if faltando: F('zip', f'{nome}: {z.name} não tem {len(faltando)} arquivo(s): {faltando[:4]}')
    else: O(f'{nome}: zip cobre entrega/ inteira')

# ----------------------------------------------------- 3. números nas páginas
NUM = {'planilhas': r'(\d+)\s+planilhas', 'prompts': r'(\d+)\s+prompts'}
for nome, k in KITS.items():
    pag = R/'site'/'src'/'pages'/k['pagina']
    if not pag.exists(): F('pagina', f'{nome}: {k["pagina"]} não existe'); continue
    h = pag.read_text()
    if k['preco'] not in h: F('preco', f'{nome}: {k["preco"]} não aparece em {k["pagina"]}')
    else: O(f'{nome}: preço {k["preco"]} na página')
    for campo, rx in NUM.items():
        esperado = k[campo]
        achados, outros = set(), set()
        for m in re.finditer(rx, h):
            n = int(m.group(1)); achados.add(n)
            if n == esperado or n <= 2: continue
            # Uma contagem só é suspeita se fala DESTE produto. Frase que compara com o
            # Essencial ("o Essencial tem 3 planilhas") ou número seguido de "por "
            # ("8 prompts por núcleo") é comparação ou subtotal, não promessa — e eram
            # os três avisos que voltavam a cada rodada sem nada para corrigir.
            ini = h.rfind('.', 0, m.start()) + 1; fim = h.find('.', m.end())
            frase = h[ini:fim if fim > 0 else m.end() + 200]
            if nome != 'essencial' and 'Essencial' in frase: continue
            if 'acrescenta' in frase: continue          # "acrescenta ... 40 prompts" é delta, não total
            if h[m.end():m.end() + 5].lstrip().startswith('por '): continue
            outros.add(n)
        if esperado not in achados:
            A('numero', f'{nome}: "{esperado} {campo}" não aparece literalmente em {k["pagina"]}')
        # O aviso traz a linha: sem ela dá dois minutos de busca para descobrir que era
        # comparação legítima ("o Essencial tem 3 planilhas", "8 prompts por núcleo").
        for n in sorted(outros):
            linhas = [i for i, L in enumerate(h.split("\n"), 1)
                      if re.search(rf'\b{n}\s+{campo}', L)]
            A('numero', f'{nome}: {k["pagina"]} também cita "{n} {campo}" '
                        f'(linha {", ".join(map(str, linhas))})')

# ------------------------------------------- 4. marcadores de rascunho
# "TODO" e "FIXME" só contam em maiúsculas: em português "todo mês" e "todo dia"
# são texto normal. "empresa fictícia" NÃO entra aqui: rotular o dado de exemplo é
# obrigação nossa, não rascunho.
RASCUNHO = re.compile(r'\bTODO\b|\bFIXME\b|XXX+')
RASCUNHO_I = re.compile(r'lorem ipsum|\[inserir|preencher aqui|produzido com IA|'
                        r'testado em empresa fict[íi]cia', re.I)
for pag in sorted((R/'site'/'src').rglob('*.html')):
    for n, linha in enumerate(pag.read_text().split('\n'), 1):
        for rx in (RASCUNHO, RASCUNHO_I):
            for m in rx.finditer(linha):
                F('rascunho', f'{pag.name}:{n} contém "{m.group(0)}"')
for md in sorted((R/'04-copy').glob('*.md')):
    for n, linha in enumerate(md.read_text().split('\n'), 1):
        if RASCUNHO.search(linha) or re.search(r'\[inserir', linha, re.I):
            F('rascunho', f'04-copy/{md.name}:{n}: {linha.strip()[:70]}')

# --------------------------------------------- 5. links internos e imagens
pub = R/'site'/'public'
if pub.is_dir():
    for pag in sorted(pub.rglob('*.html')):
        h = pag.read_text()
        for alvo in set(re.findall(r'(?:href|src|poster)="(/[^"#?]+)"', h)):
            dest = pub/alvo.lstrip('/')
            if dest.is_dir() or (dest/'index.html').exists() or dest.exists(): continue
            F('link', f'{pag.relative_to(pub)} aponta para {alvo}, que não existe')
        for cand in set(re.findall(r'srcset="([^"]*)"', h)):
            for item in cand.split(','):
                cam = item.strip().split(' ')[0]
                if cam.startswith('/') and not (pub/cam.lstrip('/')).exists():
                    F('link', f'{pag.relative_to(pub)} srcset aponta para {cam}, que não existe')
    O('links internos e srcset conferidos no site publicado')
else:
    A('link', 'site/public não existe: rode site/build.py antes da revisão')

# ------------------------------------------------ 6. páginas obrigatórias
for obrig in ('termos.html','privacidade.html','cookies.html','reembolso.html','suporte.html','sobre.html'):
    if not (R/'site'/'src'/'pages'/obrig).exists(): F('legal', f'falta {obrig}')
# O rodapé com Termos, Privacidade e Suporte vem do layout, então a conferência
# tem de ser no HTML gerado, não no arquivo da página.
for nome, k in KITS.items():
    saida = pub/('' if k['pagina']=='index.html' else k['pagina'].replace('.html',''))/'index.html'
    if not saida.exists():
        A('legal', f'{nome}: {saida} não existe, rode site/build.py'); continue
    h = saida.read_text()
    for alvo, rot in (('/termos','Termos'), ('/privacidade','Privacidade'), ('/suporte','Suporte')):
        if alvo not in h: F('legal', f'{nome}: página gerada não linka {rot}')
    else: O(f'{nome}: rodapé legal presente na página gerada')

# ------------------------------------------------------- 7. vídeos entregues
if not RAPIDO:
    for nome, k in KITS.items():
        for v in sorted((R/'produto'/k['kit']/'entrega'/'videos').glob('*.mp4')):
            d = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration',
                                '-of','csv=p=0',str(v)],capture_output=True,text=True).stdout.strip()
            try: dur = float(d)
            except ValueError: F('video', f'{nome}/{v.name}: ffprobe não leu a duração'); continue
            # o Essencial entrega demonstrações de 45 a 60 s por desenho da oferta;
            # os outros kits entregam aulas de 2 a 3 min
            lim = (40, 90) if nome == 'essencial' else (60, 400)
            if not lim[0] <= dur <= lim[1]:
                A('video', f'{nome}/{v.name}: {dur:.0f}s fora de {lim[0]} a {lim[1]}s')
            r = subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',str(v),
                                '-af','loudnorm=I=-16:TP=-1:print_format=json','-f','null','-'],
                               capture_output=True,text=True)
            m = re.search(r'"input_i"\s*:\s*"(-?[\d.]+)"', r.stderr)
            if not m: A('video', f'{nome}/{v.name}: não deu para medir o volume')
            elif not -19 <= float(m.group(1)) <= -13:
                F('video', f'{nome}/{v.name}: {float(m.group(1)):.1f} LUFS, alvo -16')
    O('duração e volume de todas as aulas conferidos')

# ------------------------------------------------- 8. fórmulas das planilhas
if not RAPIDO:
    rc = R/'produto'/'recalc_todos.py'
    if not rc.exists():
        A('formula', 'produto/recalc_todos.py não existe: fórmulas não reconferidas')
    else:
        p = subprocess.run([sys.executable, str(rc)], capture_output=True, text=True, timeout=3600)
        m = re.search(r'TOTAL: (\d+) f[óo]rmulas, (\d+) erro', p.stdout)
        if not m: F('formula', 'recalc_todos.py não devolveu o total')
        elif int(m.group(2)): F('formula', f'{m.group(2)} erro(s) de fórmula em {m.group(1)} fórmulas')
        else: O(f'{m.group(1)} fórmulas nos quatro kits, zero erro')
    for nome in ('advogados','medicos'):
        v = R/'produto'/f'kit-{nome}'/'verifica_coerencia.py'
        if not v.exists(): A('coerencia', f'{nome}: sem verifica_coerencia.py'); continue
        p = subprocess.run([sys.executable, str(v)], cwd=str(v.parent),
                           capture_output=True, text=True, timeout=1800)
        if p.returncode != 0: F('coerencia', f'{nome}: verifica_coerencia.py falhou')
        else: O(f'{nome}: coerência entre planilhas OK')
    for nome in ('essencial','completo'):
        if not (R/'produto'/f'kit-{nome}'/'verifica_coerencia.py').exists():
            A('coerencia', f'{nome}: não tem verificação de coerência entre planilhas '
                           '(só Advogados e Médicos têm)')

# ------------------------------------------------------ 9. checkout e pixel
cfg = json.loads((R/'site'/'config.json').read_text())
for chave, valor in cfg.get('checkout', {}).items():
    if chave.startswith('_'): continue
    if not str(valor).startswith('http'):
        A('externo', f'checkout.{chave} = "{valor}" (espera link da Kiwify)')
if not cfg.get('meta_pixel_id'): A('externo', 'meta_pixel_id vazio (espera o ID da Meta)')

# ---------------------------------------------------------------- relatório
print('\n' + '='*72)
print(f'REVISÃO DE LANÇAMENTO · produtos 1 a 4')
print('='*72)
print(f'\n{len(ok)} verificações passaram.\n')
if falhas:
    print(f'--- {len(falhas)} FALHA(S): resolver antes de publicar ---')
    for cat, msg in falhas: print(f'  [{cat}] {msg}')
else:
    print('--- nenhuma falha ---')
if avisos:
    print(f'\n--- {len(avisos)} aviso(s): olhar, não necessariamente corrigir ---')
    for cat, msg in avisos: print(f'  [{cat}] {msg}')
print()
sys.exit(1 if falhas else 0)
