"""Legendas dos vídeos dos kits: quebra a narração de cada cena em cues curtos (≤ 2 linhas de até 46
caracteres, entre 1 s e 7 s) e devolve o filtro do ffmpeg para gravar a legenda na imagem (acima da barra roxa)."""
import re
MAXC=84; LINHA=46; MIN_DUR=1.0; MAX_DUR=7.0; CURTO=14
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
    # pedaço muito curto (ex.: "No ano:", "Risco baixo.") piscaria: funde com o vizinho que couber
    i=0
    while i<len(juntas):
        p=juntas[i]
        if len(p)<CURTO and len(juntas)>1:
            if i>0 and len(juntas[i-1])+1+len(p)<=2*LINHA: juntas[i-1]+=' '+p; del juntas[i]; continue
            if i+1<len(juntas) and len(p)+1+len(juntas[i+1])<=2*LINHA: juntas[i+1]=p+' '+juntas[i+1]; del juntas[i]; continue
        i+=1
    return juntas
def _duas_linhas(t):
    """Uma linha se couber; senão duas, partindo na palavra que deixa as linhas mais equilibradas, ambas ≤ LINHA."""
    if len(t)<=LINHA: return t
    melhor=None
    for m in re.finditer(' ',t):
        i=m.start(); a,b=i,len(t)-i-1
        if a<=LINHA and b<=LINHA and (melhor is None or abs(a-b)<abs(melhor[1]-melhor[2])): melhor=(i,a,b)
    if melhor is None:  # não cabe em duas linhas de LINHA: parte no meio mesmo
        i=t.rfind(' ',0,len(t)//2+1); return t if i<1 else t[:i]+'\n'+t[i+1:]
    i=melhor[0]; return t[:i]+'\n'+t[i+1:]
def ts(x):
    h=int(x//3600); m=int(x%3600//60); s=x%60; return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.',',')
def cues(cenas, pausa):
    """cenas: lista de dicts com 'fala' e 'dur'. Devolve o texto do .srt. Nenhum cue dura menos de MIN_DUR."""
    srt=[]; n=0; t=0.0
    for c in cenas:
        ini=t; fim=t+c['dur']-pausa; t+=c['dur']
        peds=_pedacos(c['fala']); tot=sum(len(p) for p in peds) or 1
        durs=[(fim-ini)*len(p)/tot for p in peds]
        # cue curto demais: pega tempo do vizinho mais longo (sem deixar o vizinho abaixo de MIN_DUR)
        for k in range(len(durs)):
            while durs[k]<MIN_DUR-1e-6:
                viz=[j for j in (k-1,k+1) if 0<=j<len(durs) and durs[j]>MIN_DUR+0.05]
                if not viz: break
                j=max(viz,key=lambda j:durs[j]); d=min(MIN_DUR-durs[k],durs[j]-MIN_DUR); durs[j]-=d; durs[k]+=d
        cur=ini
        for p,d in zip(peds,durs):
            n+=1; srt.append(f"{n}\n{ts(cur)} --> {ts(min(cur+min(d,MAX_DUR),fim))}\n{_duas_linhas(p)}\n"); cur+=d
    return '\n'.join(srt)
def confere(srt_texto):
    """Devolve a lista de problemas (cue < MIN_DUR, linha > LINHA); vazia se está tudo certo."""
    probs=[]
    for bloco in srt_texto.strip().split('\n\n'):
        ls=bloco.split('\n')
        if len(ls)<3: continue
        a,b=ls[1].split(' --> ')
        conv=lambda s: sum(float(x)*m for x,m in zip(s.replace(',','.').split(':'),(3600,60,1)))
        if conv(b)-conv(a)<MIN_DUR-0.01: probs.append(f'cue {ls[0]} dura {conv(b)-conv(a):.2f}s')
        for l in ls[2:]:
            if len(l)>LINHA: probs.append(f'cue {ls[0]} linha com {len(l)} caracteres')
    return probs
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
