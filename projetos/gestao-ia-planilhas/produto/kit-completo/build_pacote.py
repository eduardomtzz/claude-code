#!/usr/bin/env python3
"""Monta o pacote de entrega do Kit Completo (zip) a partir dos arquivos gerados."""
import pathlib, shutil, subprocess, zipfile
ROOT=pathlib.Path(__file__).resolve().parent; ESS=ROOT.parent/'kit-essencial'; E=ROOT/'entrega'
E.mkdir(exist_ok=True)
# planilhas 1-3 do Essencial, 4-10 daqui
for f in ['01-semana-organizada.xlsx','02-relatorio-mensal-pronto.xlsx','03-ganhos-e-gastos.xlsx']: shutil.copy2(ESS/'entrega'/f, E/f)
for f in sorted(ROOT.glob('0[4-9]-*.xlsx'))+sorted(ROOT.glob('10-*.xlsx')): shutil.copy2(f, E/f.name)
# bibliotecas: A (do Essencial) e B; txt para copiar
shutil.copy2(ESS/'entrega'/'04-biblioteca-de-prompts.pdf', E/'11-biblioteca-de-prompts-a.pdf')
shutil.copy2(ESS/'entrega'/'04-biblioteca-de-prompts.txt', E/'11-biblioteca-de-prompts-a.txt')
(E/'11-biblioteca-de-prompts-b.txt').write_text((ROOT/'11-biblioteca-de-prompts-b.md').read_text())
# modelo de 8 slides do Essencial
shutil.copy2(ESS/'entrega'/'06-modelo-apresentacao-8-slides.pptx', E/'15-modelo-relatorio-mensal-8-slides.pptx')
(E/'LEIA-ME.txt').write_text("""Kit IA no Trabalho · Completo · Seu Sócio Gestor · versão 1.0 (setembro de 2026)

Comece por aqui: 14-manual-do-metodo.pdf (40 minutos de leitura) e a aula 1.

Planilhas (Excel e Google Sheets):
  01-semana-organizada.xlsx            02-relatorio-mensal-pronto.xlsx      03-ganhos-e-gastos.xlsx
  04-projetos-e-prazos.xlsx            05-ata-e-pendencias.xlsx             06-metas-do-trimestre.xlsx
  07-orcamento-previsto-x-realizado.xlsx   08-funil-de-propostas.xlsx       09-horas-e-custo-por-projeto.xlsx
  10-base-limpa.xlsx
Prompts: 11-biblioteca-de-prompts-a (40, dia a dia) e 11-biblioteca-de-prompts-b (40, estruturar e produzir), em PDF e txt.
Referência: 12-dicionario-de-formulas.pdf · 13-checklists-de-revisao.pdf · 14-manual-do-metodo.pdf
Modelos de apresentação: 15 (relatório mensal, 8 slides) · 16 (resultado do trimestre, 12) · 17 (proposta comercial, 10)
Aulas (pasta videos/): 8 aulas em mp4, com legenda .srt. Ordem: 01 a 08.

Regras de ouro: preencha só as células amarelas; nunca cole dados pessoais de terceiros em IA pública; confira cada número
que a IA escrever. Prisma Comunicação e todas as pessoas citadas são fictícias.

Suporte: suporte@seusociogestor.com.br (até 5 dias úteis). Arrependimento em 7 dias pelo mesmo e-mail ou pela página do pedido.
ZTRAINING SERVICE LTDA · CNPJ 68.796.613/0001-10 · seusociogestor.com.br
""")
zipf=ROOT/'kit-ia-no-trabalho-completo-v1.zip'
with zipfile.ZipFile(zipf,'w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(E.rglob('*')):
        if f.is_file(): z.write(f, f.relative_to(E))
print('pacote:', zipf, round(zipf.stat().st_size/1e6,1),'MB'); print('\n'.join(sorted(str(p.relative_to(E)) for p in E.rglob('*') if p.is_file())))
