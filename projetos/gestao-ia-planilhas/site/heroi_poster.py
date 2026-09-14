#!/usr/bin/env python3
"""Herói da página (mockup notebook+celular, 1200×812 webp) e poster do vídeo da aula 5 (1280×720 jpg).
Fontes: 08-ads/criativos/<kit>-produto-hero-1600x1000.png e o mp4 da aula 5 em produto/kit-<kit>/entrega/videos/.
Padrão para todos os kits. Uso: python3 heroi_poster.py [kit|completo|advogados|medicos|todos]"""
import pathlib, subprocess, sys
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent; PROJ = ROOT.parent
CRI = PROJ / '08-ads' / 'criativos'
# kit do site -> (prefixo do criativo, pasta do produto, trecho do nome do vídeo da aula 5)
KITS = {'kit': ('essencial', 'kit-essencial', '01-semana'), 'completo': ('completo', 'kit-completo', 'aula-05'),
        'advogados': ('advogados', 'kit-advogados', 'aula-05'), 'medicos': ('medicos', 'kit-medicos', 'aula-05')}

def heroi(kit, prefixo):
    src = CRI / f'{prefixo}-produto-hero-1600x1000.png'
    if not src.exists(): print('sem mockup', kit); return
    im = Image.open(src).convert('RGBA'); im = im.crop(im.getbbox())
    im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
    dest = ROOT / 'public' / 'assets' / kit / 'hero-mockup.webp'; dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, 'WEBP', quality=88, method=6); print(kit, 'herói', im.size, dest.stat().st_size // 1024, 'KB')

def poster(kit, pasta, trecho, segundo=None):
    vids = sorted((PROJ / 'produto' / pasta / 'entrega' / 'videos').glob(f'*{trecho}*.mp4')) if (PROJ / 'produto' / pasta / 'entrega' / 'videos').is_dir() else []
    if not vids: print('sem vídeo', kit); return
    v = vids[0]; dest = ROOT / 'public' / 'assets' / kit / 'poster-aula-05.jpg'
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(v)],
                               capture_output=True, text=True).stdout.strip())
    t = segundo if segundo is not None else min(dur * 0.35, 60)  # cena de tela, já passada a capa
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{t:.2f}', '-i', str(v), '-frames:v', '1',
                    '-vf', 'scale=1280:720', '-q:v', '4', str(dest)], check=True)
    print(kit, 'poster', f'{t:.0f}s', dest.stat().st_size // 1024, 'KB')

alvo = sys.argv[1] if len(sys.argv) > 1 else 'todos'
for k, (prefixo, pasta, trecho) in KITS.items():
    if alvo in (k, 'todos'): heroi(k, prefixo); poster(k, pasta, trecho)
