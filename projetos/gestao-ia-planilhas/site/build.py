#!/usr/bin/env python3
"""Monta site/public a partir de site/src. Sem dependências. Uso: python3 build.py"""
import json, re, os, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent
cfg = json.loads((ROOT / 'config.json').read_text(encoding='utf-8'))
if os.environ.get('META_PIXEL_ID'): cfg['meta_pixel_id'] = os.environ['META_PIXEL_ID']  # nunca gravar o ID no repositório; vem do ambiente do deploy
layout = (ROOT / 'src' / 'layout.html').read_text(encoding='utf-8')

def flat(d, prefix=''):
    out = {}
    for k, v in d.items():
        key = f'{prefix}{k}'
        if isinstance(v, dict): out.update(flat(v, key + '.'))
        else: out[key] = str(v)
    return out
vars_ = flat(cfg)

def render(tpl, extra):
    ctx = dict(vars_); ctx.update(extra)
    return re.sub(r'\{\{\s*([\w.]+)\s*\}\}', lambda m: ctx.get(m.group(1), ''), tpl)

pages = sorted((ROOT / 'src' / 'pages').glob('*.html'))
sitemap = []
for p in pages:
    raw = p.read_text(encoding='utf-8')
    m = re.match(r'\s*<!--\s*(.*?)\s*-->', raw, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1); meta[k.strip()] = v.strip()
        raw = raw[m.end():]
    slug = meta.get('path', '/' + p.stem + '/')
    if p.stem == 'index': slug = '/'
    if p.stem == '404': slug = '/404.html'
    ctx = dict(meta); ctx.update({'content': render(raw, meta), 'title': meta.get('title', cfg['marca']),
                                  'description': meta.get('description', ''), 'path': slug,
                                  'body_class': meta.get('body_class', '')})
    html = render(layout, ctx)
    out = ROOT / 'public' / (slug.strip('/') + ('/index.html' if slug.endswith('/') else '')) if slug != '/' else ROOT / 'public' / 'index.html'
    if slug == '/404.html': out = ROOT / 'public' / '404.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    if p.stem != '404' and 'noindex' not in meta.get('robots', ''): sitemap.append(cfg['url'] + slug)
    print('ok', slug, '->', out.relative_to(ROOT))

# Vídeos de demonstração: copiados do pacote do produto (não ficam no git dentro de site/)
import shutil
for VID_SRC, VID_DST in [(ROOT.parent / 'produto' / 'kit-essencial' / 'entrega' / 'videos', ROOT / 'public' / 'assets' / 'kit' / 'videos'),
                         (ROOT.parent / 'produto' / 'kit-completo' / 'entrega' / 'videos', ROOT / 'public' / 'assets' / 'completo' / 'videos'),
                         (ROOT.parent / 'produto' / 'kit-advogados' / 'entrega' / 'videos', ROOT / 'public' / 'assets' / 'advogados' / 'videos')]:
    if not VID_SRC.is_dir(): continue
    VID_DST.mkdir(parents=True, exist_ok=True)
    for f in sorted(VID_SRC.iterdir()):
        if f.suffix == '.mp4':
            dst = VID_DST / f.name
            if not dst.exists() or dst.stat().st_mtime < f.stat().st_mtime: shutil.copy2(f, dst)
        elif f.suffix == '.srt':
            vtt = 'WEBVTT\n\n' + re.sub(r'(\d{2}:\d{2}:\d{2}),(\d{3})', r'\1.\2', f.read_text(encoding='utf-8'))
            (VID_DST / (f.stem + '.vtt')).write_text(vtt, encoding='utf-8')
    print('vídeos copiados de', VID_SRC.relative_to(ROOT.parent))

# Otimização de imagens (padrão para todas as páginas): JPG/PNG de produto viram WebP, imagens largas ganham
# variante 640 px com srcset (celular baixa 1/3), posters de vídeo são reduzidos a 960 px, imagens lazy recebem
# decoding=async e o CSS das fontes vai inline no <head> (uma requisição a menos no caminho crítico).
def otimizar_imagens():
    try: from PIL import Image
    except ImportError: print('AVISO: Pillow ausente, imagens não otimizadas'); return
    PUB = ROOT / 'public'
    def webp(src, dst, largura=None, q=82):
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime: return
        im = Image.open(src); im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
        if largura and im.width > largura: im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
        im.save(dst, 'WEBP', quality=q, method=6)
    def caminho(url): return PUB / url.lstrip('/')
    fontes_css = (PUB / 'assets' / 'css' / 'fonts.css').read_text(encoding='utf-8').strip()
    for html in PUB.rglob('*.html'):
        t = html.read_text(encoding='utf-8')
        def img(m):
            tag = m.group(0)
            src = re.search(r' src="(/assets/[^"]+)"', tag)
            if not src or '/assets/img/' in src.group(1): return tag
            url = src.group(1); f = caminho(url)
            if not f.exists(): return tag
            if f.suffix.lower() in ('.jpg', '.jpeg', '.png'):
                novo = f.with_suffix('.webp'); webp(f, novo); url2 = url.rsplit('.', 1)[0] + '.webp'
                tag = tag.replace(f'src="{url}"', f'src="{url2}"'); url, f = url2, novo
            w = re.search(r' width="(\d+)"', tag)
            if w and int(w.group(1)) >= 900 and 'srcset=' not in tag:
                p640 = f.with_name(f.stem + '-640.webp'); webp(f, p640, 640); u640 = url[:-5] + '-640.webp'
                sizes = '(max-width: 859px) calc(100vw - 32px), 560px' if 'fetchpriority="high"' in tag else '(max-width: 639px) calc(100vw - 32px), (max-width: 979px) 50vw, 380px'
                tag = tag.replace(f'src="{url}"', f'src="{url}" srcset="{u640} 640w, {url} {w.group(1)}w" sizes="{sizes}"')
            if 'loading="lazy"' in tag and 'decoding=' not in tag: tag = tag.replace('loading="lazy"', 'loading="lazy" decoding="async"')
            return tag
        t = re.sub(r'<img [^>]*>', img, t)
        def poster(m):
            url = m.group(1); f = caminho(url)
            if not f.exists() or f.suffix.lower() == '.webp': return m.group(0)
            novo = f.with_name(f.stem + '-960.webp'); webp(f, novo, 960)
            return f'poster="{url.rsplit(".", 1)[0]}-960.webp"'
        t = re.sub(r'poster="(/assets/[^"]+)"', poster, t)
        t = t.replace('<link rel="stylesheet" href="/assets/css/fonts.css">', f'<style>{fontes_css}</style>')
        html.write_text(t, encoding='utf-8')
    print('imagens otimizadas (webp, srcset 640, posters 960, fontes inline)')
otimizar_imagens()

(ROOT / 'public' / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'  <url><loc>{u}</loc></url>\n' for u in sitemap) + '</urlset>\n', encoding='utf-8')
(ROOT / 'public' / 'robots.txt').write_text(f"User-agent: *\nAllow: /\nSitemap: {cfg['url']}/sitemap.xml\n", encoding='utf-8')
(ROOT / 'public' / '_headers').write_text(
"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
/assets/*
  Cache-Control: public, max-age=31536000, immutable
""", encoding='utf-8')
print('sitemap, robots e _headers gerados')
