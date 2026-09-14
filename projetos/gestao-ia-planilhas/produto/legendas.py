"""Legendas dos vídeos dos kits: quebra a narração de cada cena em cues curtos (≤ 2 linhas de ~42
caracteres, ≤ 7 s) e devolve o filtro do ffmpeg para gravar a legenda na imagem (acima da barra roxa)."""
import re
MAXC=84; LINHA=42
def _pedacos(texto):
    frases=re.split(r'(?<=[.!?])\s+',texto.strip())
    out=[]
    for f in frases:
        if len(f)<=MAXC: out.append(f); continue
        # quebra em vírgulas/ponto e vírgula, juntando até MAXC
        partes=re.split(r'(?<=[,;:])\s+',f); atual=''
        for p in partes:
            if atual and len(atual)+1+len(p)>MAXC: out.append(atual); atual=p
            else: atual=(atual+' '+p).strip()
        if atual: out.append(atual)
    # junta frases curtas seguidas quando cabem
    juntas=[]
    for p in out:
        if juntas and len(juntas[-1])+1+len(p)<=MAXC and len(juntas[-1])<40: juntas[-1]=juntas[-1]+' '+p
        else: juntas.append(p)
    return juntas
def _duas_linhas(t):
    if len(t)<=LINHA: return t
    i=t.rfind(' ',0,LINHA+1)
    if i<20: i=t.find(' ',LINHA)
    return t if i<0 else t[:i]+'\n'+t[i+1:]
def ts(x):
    h=int(x//3600); m=int(x%3600//60); s=x%60; return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.',',')
def cues(cenas, pausa):
    """cenas: lista de dicts com 'fala' e 'dur'. Devolve o texto do .srt."""
    srt=[]; n=0; t=0.0
    for c in cenas:
        ini=t; fim=t+c['dur']-pausa; t+=c['dur']
        peds=_pedacos(c['fala']); tot=sum(len(p) for p in peds) or 1; cur=ini
        for p in peds:
            d=(fim-ini)*len(p)/tot; d=min(d,7.0) if len(peds)>1 else min(fim-ini,7.0)
            n+=1; srt.append(f"{n}\n{ts(cur)} --> {ts(min(cur+d,fim))}\n{_duas_linhas(p)}\n"); cur+=d
    return '\n'.join(srt)
def filtro(srt_path, margem=112, tamanho=20):
    """Filtro -vf para gravar a legenda: branca com contorno, acima da barra de legenda das cenas."""
    p=str(srt_path).replace('\\','\\\\').replace(':','\\:').replace("'","\\'")
    estilo=f"FontName=DejaVu Sans,FontSize={tamanho},PrimaryColour=&H00FFFFFF,OutlineColour=&HA0000000,BackColour=&H80000000,BorderStyle=1,Outline=1.3,Shadow=0,MarginV={margem},Alignment=2,WrapStyle=0"
    return f"subtitles='{p}':force_style='{estilo}'"
