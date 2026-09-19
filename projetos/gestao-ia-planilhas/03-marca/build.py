import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import RecordingPen

FONT='Bricolage.ttf'; UVA='#3B1F5E'; LILAS='#7A5AA8'; SOL='#FFC83D'; BRANCO='#FFFFFF'
tt=TTFont(FONT); upem=tt['head'].unitsPerEm; gs=tt.getGlyphSet(); order=tt.getGlyphOrder()
blob=hb.Blob.from_file_path(FONT); face=hb.Face(blob); font=hb.Font(face); font.scale=(upem,upem)

def shape(text, size):
    buf=hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern":True,"liga":True})
    k=size/upem; x=0; out=[]
    for info,pos in zip(buf.glyph_infos, buf.glyph_positions):
        name=order[info.codepoint]
        pen=RecordingPen(); gs[name].draw(TransformPen(pen,(k,0,0,-k,x+pos.x_offset*k,-pos.y_offset*k)))
        sp=SVGPathPen(gs); pen.replay(sp); d=sp.getCommands()
        out.append((info.cluster, x, x+pos.x_advance*k, d)); x+=pos.x_advance*k
    return out, x, k

TEXT='Seu Sócio Gestor'; SIZE=100
glyphs,width,k=shape(TEXT,SIZE)
asc=tt['hhea'].ascent*k; desc=-tt['hhea'].descent*k
gi=TEXT.index('Gestor'); gx0=min(g[1] for g in glyphs if g[0]>=gi); gx1=width
paths=''.join(f'<path d="{d}"/>' for _,_,_,d in glyphs if d)
cap=tt['OS/2'].sCapHeight*k if hasattr(tt['OS/2'],'sCapHeight') else 0.7*SIZE

def symbol(x,y,s,c1,c2,c3):
    # three stepped bars + dot; s = scale (design unit 72)
    u=s/72
    return f'''<g transform="translate({x},{y}) scale({u})">
<rect x="0" y="46" width="30" height="11" rx="5.5" fill="{c2}"/>
<rect x="9" y="31" width="30" height="11" rx="5.5" fill="{c1}"/>
<rect x="18" y="16" width="30" height="11" rx="5.5" fill="{c1}"/>
<circle cx="44" cy="52" r="6" fill="{c3}"/></g>'''

def horizontal(c_text,c_bar1,c_bar2,c_dot,c_under,bg=None,name='logo'):
    vis_h=42.0; vis_w=50.0; u=(cap*1.32)/vis_h; sym_w=vis_w*u; sym_h=vis_h*u
    gap=SIZE*0.30; tx=sym_w+gap
    under_h=SIZE*0.085; pad=SIZE*0.12
    H=max(sym_h,cap)+pad*2+under_h+SIZE*0.16; W=tx+width+pad*0.5
    base=pad+max(sym_h,cap)/2+cap/2
    cy=pad+max(sym_h,cap)/2  # vertical center
    sym_y=cy-sym_h/2-16*u    # symbol drawn from y=16 in 72-box
    under_y=base+SIZE*0.13
    bgrect=f'<rect width="{W:.1f}" height="{H:.1f}" fill="{bg}"/>' if bg else ''
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}" width="{W:.0f}" height="{H:.0f}" role="img" aria-label="Seu Sócio Gestor">
{bgrect}{symbol(0,sym_y,72*u,c_bar1,c_bar2,c_dot)}
<g transform="translate({tx:.1f},{base:.1f})" fill="{c_text}">{paths}</g>
<rect x="{tx+gx0:.1f}" y="{under_y:.1f}" width="{gx1-gx0:.1f}" height="{under_h:.1f}" rx="{under_h/2:.1f}" fill="{c_under}"/>
</svg>'''
    open(f'{name}.svg','w').write(svg); return W,H

def stacked(c_text,c_bar1,c_bar2,c_dot,c_under,name):
    u=(SIZE*1.9)/42.0; sym_w=50*u; sym_h=42*u; pad=SIZE*0.2
    W=max(width,sym_w)+pad*2; sx=(W-sym_w)/2; sym_y=pad-16*u
    base=pad+sym_h+SIZE*0.45+cap; H=base+SIZE*0.13+SIZE*0.085+pad; tx=(W-width)/2
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}" width="{W:.0f}" height="{H:.0f}" role="img" aria-label="Seu Sócio Gestor">
{symbol(sx,sym_y,72*u,c_bar1,c_bar2,c_dot)}
<g transform="translate({tx:.1f},{base:.1f})" fill="{c_text}">{paths}</g>
<rect x="{tx+gx0:.1f}" y="{base+SIZE*0.13:.1f}" width="{gx1-gx0:.1f}" height="{SIZE*0.085:.1f}" rx="{SIZE*0.0425:.1f}" fill="{c_under}"/>
</svg>'''
    open(f'{name}.svg','w').write(svg)

def simbolo(c1,c2,c3,bg,name,rounded=16):
    bgrect=f'<rect width="72" height="72" rx="{rounded}" fill="{bg}"/>' if bg else ''
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 72 72" width="72" height="72" role="img" aria-label="Símbolo Seu Sócio Gestor">{bgrect}
<rect x="12" y="46" width="30" height="11" rx="5.5" fill="{c2}"/>
<rect x="21" y="31" width="30" height="11" rx="5.5" fill="{c1}"/>
<rect x="30" y="16" width="30" height="11" rx="5.5" fill="{c1}"/>
<circle cx="56" cy="52" r="6" fill="{c3}"/></svg>'''
    open(f'{name}.svg','w').write(svg)

W,H=horizontal(UVA,UVA,LILAS,SOL,SOL,None,'logo-horizontal')
horizontal(UVA,UVA,UVA,UVA,UVA,None,'logo-mono-uva')
horizontal(BRANCO,BRANCO,'#B89BE0',SOL,SOL,None,'logo-branco')
horizontal(BRANCO,BRANCO,BRANCO,BRANCO,BRANCO,None,'logo-mono-branco')
stacked(UVA,UVA,LILAS,SOL,SOL,'logo-empilhado')
stacked(BRANCO,BRANCO,'#B89BE0',SOL,SOL,'logo-empilhado-branco')
simbolo(UVA,LILAS,SOL,None,'simbolo')
simbolo(BRANCO,'#B89BE0',SOL,UVA,'simbolo-fundo-uva')
simbolo(UVA,UVA,BRANCO,SOL,'simbolo-fundo-sol')
simbolo(BRANCO,'#B89BE0',SOL,UVA,'simbolo-avatar',rounded=36)
print('ok', round(W), round(H), 'glyphs', len(glyphs))
