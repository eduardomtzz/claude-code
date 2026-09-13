#!/usr/bin/env python3
"""Monta site/public a partir de site/src. Sem dependências. Uso: python3 build.py"""
import json, re, os, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent
cfg = json.loads((ROOT / 'config.json').read_text(encoding='utf-8'))
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
    html = render(layout, {'content': render(raw, meta), 'title': meta.get('title', cfg['marca']),
                           'description': meta.get('description', ''), 'path': slug,
                           'body_class': meta.get('body_class', '')})
    out = ROOT / 'public' / (slug.strip('/') + ('/index.html' if slug.endswith('/') else '')) if slug != '/' else ROOT / 'public' / 'index.html'
    if slug == '/404.html': out = ROOT / 'public' / '404.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    if p.stem != '404': sitemap.append(cfg['url'] + slug)
    print('ok', slug, '->', out.relative_to(ROOT))

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
