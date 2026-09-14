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
    # frase sem vírgula e ainda longa: parte na palavra mais perto do meio
    def meio(t):
        if len(t)<=MAXC: return [t]
        i=t.rfind(' ',0,len(t)//2+1)
        if i<1: i=t.find(' ',len(t)//2)
        return [t] if i<1 else meio(t[:i])+meio(t[i+1:])
    out=[q for p in out for q in meio(p)]
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
def filtro(srt_path, margem=106, tamanho=28, altura=720):
    """Filtro -vf para gravar a legenda: branca com contorno, acima da barra de legenda das cenas.
    margem = distância da base do texto ao rodapé, em pixels do vídeo; tamanho = corpo da fonte em pixels;
    altura = altura do vídeo. O ffmpeg converte SRT em ASS com PlayResY=288, então os valores são
    convertidos para essa escala (senão MarginV/FontSize saem 2,5× maiores em 720p)."""
    k=288/altura
    p=str(srt_path).replace('\\','\\\\').replace(':','\\:').replace("'","\\'")
    estilo=(f"FontName=DejaVu Sans,FontSize={tamanho*k:.1f},PrimaryColour=&H00FFFFFF,OutlineColour=&H30000000,"
            f"BackColour=&H80000000,BorderStyle=1,Outline={1.6*k:.2f},Shadow=0,MarginV={round(margem*k)},"
            f"MarginL={round(40*k)},MarginR={round(40*k)},Alignment=2,WrapStyle=0")
    return f"subtitles='{p}':force_style='{estilo}'"
