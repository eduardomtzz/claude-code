#!/usr/bin/env python3
"""Deriva as imagens de produto do site (cards das planilhas, miniaturas de PDF/slides) das capturas
docs/tela-*.png e dos PDFs de entrega. Rodar depois de produto/telas.py e dos build_pdfs.
Uso: python3 assets_produto.py"""
import pathlib, fitz
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parent; PROJ=ROOT.parent; A=ROOT/'public'/'assets'
DE=PROJ/'produto'/'kit-essencial'; DC=PROJ/'produto'/'kit-completo'
def card(src,dst,w=1200,h=654):
    im=Image.open(src).convert('RGB'); ch=int(im.width*h/w); im=im.crop((0,0,im.width,min(ch,im.height)))
    im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS); im.save(dst,quality=82,optimize=True,progressive=True); print(dst.name,im.size)
def pagina(pdf,dst,pag,w):
    doc=fitz.open(pdf); p=doc[pag]; pix=p.get_pixmap(matrix=fitz.Matrix(2,2)); im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS); im.save(dst,quality=82,optimize=True,progressive=True); print(dst.name,im.size,'pág.',pag+1)
def thumb(src,box,out):
    im=Image.open(src).crop(box).resize((300,400),Image.LANCZOS); im.save(out,quality=82,optimize=True,progressive=True); print(out.name)
# cards das planilhas (recorte do topo do painel, 1200×654)
for nome,tela in [('semana','tela-semana-hoje'),('relatorio','tela-relatorio-painel'),('ganhos','tela-ganhos-painel')]:
    card(DE/'docs'/f'{tela}.png',A/'kit'/f'{nome}.jpg')
card(DE/'docs'/'tela-relatorio-resumo.png',A/'kit'/'relatorio-resumo.jpg',1200,628)
for nome,tela,h in [('projetos','tela-projetos-painel',676),('ata','tela-ata-aberto',676),('metas','tela-metas-painel',676),('orcamento','tela-orcamento-painel',673),('funil','tela-funil-painel',673),('horas','tela-horas-painel',673),('base','tela-base-base',586)]:
    card(DC/'docs'/f'{tela}.png',A/'completo'/f'{nome}.jpg',1200,h)
# miniaturas de PDF (página com conteúdo, não a capa)
pagina(DE/'entrega'/'04-biblioteca-de-prompts.pdf',A/'kit'/'prompts.jpg',2,579)
pagina(DE/'entrega'/'05-mini-manual.pdf',A/'kit'/'manual.jpg',3,496)
pagina(DE/'entrega'/'07-checklist-antes-de-enviar.pdf',A/'kit'/'checklist.jpg',0,496)
pagina(DC/'entrega'/'12-dicionario-de-formulas.pdf',A/'completo'/'dicionario.jpg',0,600)
pagina(DC/'entrega'/'14-manual-do-metodo.pdf',A/'completo'/'manual.jpg',3,600)
# Kit Advogados: cards por núcleo, miniaturas dos bônus e herói
DA=PROJ/'produto'/'kit-advogados'
if (DA/'docs'/'tela-17.png').exists():
    (A/'advogados').mkdir(exist_ok=True)
    for nome,tela in [('prazos','tela-01'),('honorarios','tela-05'),('caixa','tela-09'),('carteira','tela-13'),('painel','tela-17')]:
        card(DA/'docs'/f'{tela}.png',A/'advogados'/f'{nome}.jpg',1200,675)
    for nome,pdf in [('cobranca','22-mensagens-de-cobranca-e-confirmacao'),('lgpd','23-guia-lgpd-escritorio-pequeno'),('contador','24-roteiro-reuniao-com-o-contador')]:
        src=DA/'entrega'/f'{pdf}.pdf'
        if src.exists():
            pagina(src,A/'advogados'/f'{nome}.jpg',1,600)
            thumb(A/'advogados'/f'{nome}.jpg',(0,0,450,600),A/'advogados'/f'thumb-{nome}.jpg')
# Kit Médicos: cards por núcleo e miniaturas dos bônus (PDFs 22 a 24, página 2). Só roda quando as telas existirem.
DM=PROJ/'produto'/'kit-medicos'
if (DM/'docs'/'tela-17.png').exists():
    (A/'medicos').mkdir(exist_ok=True)
    for nome,tela in [('agenda','tela-01'),('preco','tela-05'),('caixa','tela-09'),('convenios','tela-13'),('painel','tela-17')]:
        if (DM/'docs'/f'{tela}.png').exists(): card(DM/'docs'/f'{tela}.png',A/'medicos'/f'{nome}.jpg',1200,675)
    for nome,num in [('mensagens','22'),('lgpd','23'),('contador','24')]:
        achados=sorted((DM/'entrega').glob(f'{num}-*.pdf'))  # nome do arquivo definido pelo empacotador do kit
        if achados:
            pagina(achados[0],A/'medicos'/f'{nome}.jpg',1,600)
            thumb(A/'medicos'/f'{nome}.jpg',(0,0,450,600),A/'medicos'/f'thumb-{nome}.jpg')
# grades de slides (pptx → pdf via LibreOffice → grade)
import subprocess, tempfile
SOFFICE='/root/.claude/skills/synced/196a43ae-ea62-4685-8684-e86dad1734fb_be351cae-a2b1-428f-a734-2c8f11d7ae5e/pptx/scripts/office/soffice.py'
def grade(pptx,dst,cols,cw):
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['python3',SOFFICE,'--headless','--convert-to','pdf','--outdir',td,str(pptx)],check=True,capture_output=True)
        doc=fitz.open(pathlib.Path(td)/(pptx.stem+'.pdf')); ims=[]
        for pg in doc:
            pix=pg.get_pixmap(matrix=fitz.Matrix(1.5,1.5)); im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples); ims.append(im.resize((cw,int(im.height*cw/im.width)),Image.LANCZOS))
    ch=ims[0].height; rows=(len(ims)+cols-1)//cols; gap=10
    g=Image.new('RGB',(cols*cw+(cols-1)*gap,rows*ch+(rows-1)*gap),'#EDE7F6')
    for i,im in enumerate(ims): g.paste(im,((i%cols)*(cw+gap),(i//cols)*(ch+gap)))
    g.save(dst,quality=82,optimize=True,progressive=True); print(dst.name,g.size,len(ims),'slides')
grade(DE/'entrega'/'06-modelo-apresentacao-8-slides.pptx',A/'kit'/'slides.jpg',2,560)
grade(DC/'entrega'/'16-modelo-resultado-do-trimestre-12-slides.pptx',A/'completo'/'slides-trimestre.jpg',3,393)
# miniaturas 3:4 dos bônus do Completo
thumb(A/'completo'/'slides-trimestre.jpg',(0,0,300,400),A/'completo'/'thumb-slides.jpg')
thumb(A/'completo'/'dicionario.jpg',(0,120,450,720),A/'completo'/'thumb-dicionario.jpg')
thumb(A/'completo'/'manual.jpg',(0,0,450,600),A/'completo'/'thumb-manual.jpg')
