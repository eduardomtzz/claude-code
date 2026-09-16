#!/usr/bin/env python3
"""Lote de anúncios 9:16 para triagem de ângulo no Meta Ads.

Direção aplicada: parecer do GPT-6 Astra de 16/09/2026, com as minhas discordâncias
registradas em ganchos/direcao-gpt-decisoes.md. O que mudou em relação ao rascunho:
nenhum número de hora inventado, demonstração do arquivo real em vez de lista
animada, preço em etiqueta discreta no meio do vídeo e cartão de fechamento curto.

Estrutura: Essencial 22 s em 5 cenas (etiqueta de preço aos 8 s);
           Completo 30 s em 6 cenas (etiqueta de preço aos 12 s).

Uso:  python3 build_ganchos.py [essencial|completo|todos] [codigo]
Saída: ganchos/<produto>-<codigo>-9x16.mp4 + .srt + tira de frames.
"""
import sys, pathlib, subprocess
import criativo_cenas as C

ROOT = pathlib.Path(__file__).resolve().parent
SAIDA = ROOT / 'ganchos'; SAIDA.mkdir(exist_ok=True)
E = 'kit-essencial/docs/'          # telas do Essencial
K = 'kit-completo/docs/'           # telas do Completo

# Recortes legíveis: x, y, largura, altura em fração da imagem.
# A cena abre com o arquivo inteiro e entra neste recorte depois de ~0,7 s.
F = {
 # O motor limita o zoom a 3x o tamanho de ajuste. Como sx = 960/(largura*fração),
 # a fração 0.33 é exatamente onde o recorte enche o quadro com o zoom máximo.
 # Recorte mais largo que isso quase não aumenta nada. Páginas de texto usam 0.50,
 # onde o aumento é menor mas a linha não fica cortada no meio.
 'rel-linhas':   '0,0.045,0.33,0.10',     # Indicador / Mês / Mês anterior
 'rel-situacao': '0.30,0.045,0.33,0.10',  # Variação / Meta / Vs. meta / Situação
 'rel-resumo':   '0.02,0.10,0.50,0.20',   # frases da aba Resumo
 'semana-campos':'0.02,0.08,0.33,0.12',   # colunas que a pessoa preenche
 'semana-hoje':  '0,0.02,0.33,0.08',      # Atrasadas / Para hoje / Esta semana
 'ganhos':       '0,0.03,0.33,0.10',
 'prompt-campos':'0.08,0.14,0.50,0.16',   # campos entre colchetes
 'manual':       '0.08,0.14,0.50,0.16',
 'orc-painel':   '0,0.055,0.33,0.095',    # Categoria / Tipo / Previsto / Realizado
 'orc-desvio':   '0.28,0.055,0.33,0.095', # Desvio em R$, em % e Situação
 'orc-previsto': '0,0.06,0.33,0.18',
 'proj-painel':  '0,0.05,0.33,0.10',
 'proj-prazo':   '0.26,0.05,0.33,0.10',
 'proj-etapas':  '0,0.06,0.33,0.16',
 'metas':        '0,0.05,0.33,0.11',
 'metas-result': '0.26,0.05,0.33,0.11',
 'ata':          '0,0.05,0.33,0.10',
 'funil':        '0,0.05,0.33,0.10',
}


# ---------------------------------------------------------------------- comuns
PROVA = {
 'essencial': {'tipo':'prova','min':4.5,
   'fala':'Três planilhas, quarenta prompts, mini-manual e três demonstrações.',
   'h':'O que vem no kit','selos':['3 planilhas','40 prompts','Mini-manual','3 demonstrações'],
   'rod':'Abre no Excel e no Google Planilhas'},
 'completo': {'tipo':'prova','min':5.0,
   'fala':'Dez planilhas, oitenta prompts, oito aulas curtas e três modelos de apresentação.',
   'h':'O que vem no kit','selos':['10 planilhas','80 prompts','8 aulas curtas','3 modelos'],
   'rod':'Abre no Excel e no Google Planilhas'},
}
FIM = {
 'essencial': {'tipo':'fim','min':4.5,
   'fala':'Trinta e sete reais, uma vez. Sete dias para desistir. Toque em comprar.',
   'tt':'Kit IA no Trabalho <em>Essencial</em>','preco':'Comprar por R$ 37',
   'nota':'Pagamento único · Pix ou cartão · acesso imediato<br>7 dias para desistir, sem explicar'},
 'completo': {'tipo':'fim','min':5.0,
   'fala':'Cento e noventa e sete reais, uma vez, sem mensalidade. Sete dias para desistir. Veja o que vem no kit.',
   'tt':'Kit IA no Trabalho <em>Completo</em>','preco':'Ver o que vem no kit',
   'nota':'R$ 197 à vista ou 12× no cartão · sem mensalidade<br>7 dias para desistir, sem explicar'},
}
def tela(img, foco, h, fala, minimo=4.5, leg=None, selo=None, hsize=72):
    return {'tipo':'tela','img':img,'foco':foco,'h':h,'fala':fala,'min':minimo,
            'leg':leg,'selo':selo,'hsize':hsize}

# ------------------------------------------------------------------- Essencial
ESSENCIAL = {
 'e1-arquivo-aberto': dict(
   tecnica='Inspeção do produto. A prova mais forte que temos é deixar a pessoa ver o arquivo.',
   cenas=[
     tela(E+'tela-relatorio-painel.png', F['rel-linhas'], 'O relatório do mês, <em>por dentro</em>',
          'Veja esta planilha de relatório por dentro.', 4.0, selo='sem corte'),
     tela(E+'tela-relatorio-painel.png', F['rel-situacao'], 'Ele compara e classifica',
          'Mês, mês anterior, variação e se ficou dentro da meta. A planilha classifica cada indicador.', 5.5),
     tela(E+'tela-relatorio-resumo.png', F['rel-resumo'], 'A aba Resumo já escreve',
          'E a aba Resumo monta o bloco de frases do mês com os seus próprios números.', 5.0),
   ]),
 'e2-rapidinho': dict(
   tecnica='Callout com o produto já na tela, para não virar só reclamação.',
   cenas=[
     tela(E+'tela-relatorio-painel.png', F['rel-linhas'], '"Um relatório <em>rapidinho</em>"',
          'Pedem um relatório rapidinho. Você começa do zero?', 4.0),
     tela(E+'tela-relatorio-painel.png', F['rel-situacao'], 'Os campos que se repetem',
          'Os campos que se repetem todo mês já estão montados aqui.', 5.0),
     tela(E+'tela-relatorio-resumo.png', F['rel-resumo'], 'O texto sai dos seus números',
          'Você preenche, e o texto do mês sai dos seus próprios números.', 5.0),
   ]),
 'e3-numeros-no-prompt': dict(
   tecnica='Mecanismo demonstrado, sem afirmar exclusividade nem dizer que planilha é obrigatória.',
   cenas=[
     tela(E+'tela-relatorio-resumo.png', F['rel-resumo'], 'Seu prompt tem <em>os números?</em>',
          'Seu prompt tem os números do trabalho?', 4.0),
     tela(E+'preview-04-biblioteca-de-prompts-p3.png', F['prompt-campos'], 'Onde os seus dados <em>entram</em>',
          'Cada prompt do kit tem o campo onde os seus dados entram.', 5.5),
     tela(E+'tela-relatorio-resumo.png', F['rel-resumo'], 'O bloco já sai pronto',
          'E a planilha já entrega esse bloco pronto para colar.', 5.0),
   ]),
 'e4-onde-preencher': dict(
   tecnica='Primeiro uso guiado. Derruba a objeção de comprar e não saber por onde começar.',
   cenas=[
     tela(E+'tela-semana-tarefas.png', F['semana-campos'], 'Preencha os <em>campos indicados</em>',
          'Veja onde preencher. As fórmulas já estão prontas.', 4.0, selo='campos em amarelo'),
     tela(E+'tela-semana-hoje.png', F['semana-hoje'], 'O painel se atualiza sozinho',
          'Você digita a tarefa e o prazo. O painel de hoje se atualiza sozinho.', 5.0),
     tela(E+'tela-ganhos-painel.png', F['ganhos'], 'As três funcionam igual',
          'As três planilhas funcionam do mesmo jeito: campo amarelo você preenche, o resto é fórmula.', 5.5),
   ]),
 'e5-o-que-se-compra': dict(
   tecnica='Clareza do que se compra. Derruba "é assinatura?", "é plataforma?", "é curso?".',
   cenas=[
     {'tipo':'prova','min':4.5,'fala':'Você compra os arquivos. Não paga mensalidade.',
      'h':'Arquivos prontos. <em>Pagamento único.</em>','selos':['Planilhas','Prompts','Mini-manual'],
      'rod':'Não é software, não é assinatura, não é curso ao vivo'},
     tela(E+'tela-relatorio-painel.png', F['rel-linhas'], 'Os arquivos são estes',
          'São planilhas de verdade, que abrem no Excel e no Google Planilhas.', 5.0),
     tela(E+'preview-05-mini-manual-p4.png', F['manual'], 'E o manual explica',
          'O mini-manual explica como preencher e o que conferir antes de enviar.', 5.0),
   ]),
 'e6-quantas-vezes': dict(
   tecnica='Custo da inação sem número inventado: quem responde faz a própria conta. '
           'Este é o meu desacordo registrado com o GPT, que cortaria o ângulo inteiro.',
   cenas=[
     {'tipo':'dor','min':5.5,'fala':'Quantas vezes, este ano, você montou a mesma coisa do zero?',
      'h':'Quantas vezes, <em>este ano?</em>',
      'itens':['O mesmo relatório do zero','A mesma planilha do zero','Os mesmos slides do zero'],
      't':[0.5,1.9,3.3],'rod':'faça a sua própria conta'},
     tela(E+'tela-relatorio-painel.png', F['rel-situacao'], 'Da próxima, já está montado',
          'Da próxima vez a estrutura já existe: os campos, as fórmulas e a classificação.', 5.5),
     tela(E+'tela-relatorio-resumo.png', F['rel-resumo'], 'O texto sai dos seus números',
          'Você troca os dados pelos seus e o texto do mês sai daí.', 4.5),
   ]),
}

# -------------------------------------------------------------------- Completo
COMPLETO = {
 'c1-pergunta-orcamento': dict(
   tecnica='Uma pergunta concreta respondida pela tela. Dá utilidade ao produto no primeiro segundo.',
   cenas=[
     tela(K+'tela-orcamento-painel.png', F['orc-painel'], 'Previsto <em>versus realizado</em>',
          'Em qual categoria o orçamento passou do previsto?', 4.0),
     tela(K+'tela-orcamento-painel.png', F['orc-desvio'], 'A planilha responde',
          'A planilha mostra categoria, previsto, realizado e a diferença.', 4.5),
     tela(K+'tela-orcamento-previsto.png', F['orc-previsto'], 'E de onde veio o número',
          'E a aba Previsto mostra de onde veio cada valor.', 4.5),
     tela(K+'tela-metas-painel.png', F['metas'], 'A mesma lógica nas outras',
          'Metas, projetos, funil e horas seguem a mesma lógica.', 5.0),
   ]),
 'c2-demandas-da-semana': dict(
   tecnica='Acúmulo com prova: cada cobrança da semana aparece com o arquivo que a resolve.',
   cenas=[
     {'tipo':'dor','min':5.0,'fala':'Relatório, projeto, reunião. De novo, toda semana.',
      'h':'Relatório. Projeto. <em>Reunião.</em>',
      'itens':['Segunda: o relatório','Quarta: o projeto','Sexta: a reunião'],
      't':[0.5,1.9,3.3],'rod':'e cada um montado do zero'},
     tela(K+'tela-relatorio-painel.png', F['rel-situacao'], 'Relatório: já montado',
          'O relatório tem planilha própria, com comparação e classificação prontas.', 4.5),
     tela(K+'tela-projetos-painel.png', F['proj-painel'], 'Projeto: já montado',
          'O acompanhamento de projeto tem etapa, prazo e responsável.', 4.5),
     tela(K+'tela-ata-aberto.png', F['ata'], 'Reunião: já montada',
          'E a ata guarda o que ficou pendente, com dono e data.', 4.5),
   ]),
 'c3-uma-das-dez': dict(
   tecnica='Inspeção do produto. A R$ 197 a pessoa precisa avaliar antes de decidir.',
   cenas=[
     tela(K+'tela-projetos-painel.png', F['proj-painel'], 'Uma das dez, <em>por dentro</em>',
          'Veja uma das dez planilhas por dentro.', 4.0, selo='sem corte'),
     tela(K+'tela-projetos-etapas.png', F['proj-prazo'], 'Etapa, prazo e responsável',
          'Você lança a etapa, o prazo e o responsável.', 4.5),
     tela(K+'tela-projetos-linha.png', F['proj-etapas'], 'O atraso aparece sozinho',
          'O painel mostra o que está atrasado sem você calcular nada.', 4.5),
     tela(K+'tela-funil-painel.png', F['funil'], 'As outras nove são assim',
          'As outras nove funcionam do mesmo jeito.', 4.5),
   ]),
 'c4-quem-vai-ler': dict(
   tecnica='Destinatário demonstrado no prompt de estruturação, em vez da abstração "o erro vem antes do Excel".',
   cenas=[
     tela(K+'preview-11-biblioteca-de-prompts-b-p4.png', F['prompt-campos'], 'Quem vai <em>ler</em> o seu relatório?',
          'Quem vai ler o seu próximo relatório?', 4.0),
     tela(K+'preview-11-biblioteca-de-prompts-b-p4.png', F['prompt-campos'], 'O prompt pergunta antes',
          'O prompt de estruturação pergunta quem lê, quando, e para decidir o quê.', 5.0),
     tela(K+'tela-relatorio-resumo.png', F['rel-resumo'], 'Depois vêm os números',
          'Só depois entram os números da planilha.', 4.5),
     tela(K+'tela-metas-painel.png', F['metas'], 'Vale para toda entrega',
          'Vale para o relatório, para a reunião e para a apresentação.', 4.5),
   ]),
 'c5-escopo': dict(
   tecnica='Qualificação por escopo, começando pelo que a pessoa faz em vez da negativa.',
   cenas=[
     tela(K+'tela-projetos-painel.png', F['proj-painel'], 'Projetos, metas e <em>orçamento?</em>',
          'Você cuida de projetos, metas e orçamento?', 4.0),
     tela(K+'tela-metas-painel.png', F['metas-result'], 'Meta do trimestre, acompanhada',
          'Cada meta do trimestre com o realizado ao lado.', 4.5),
     tela(K+'tela-orcamento-painel.png', F['orc-painel'], 'Orçamento, linha por linha',
          'Cada categoria do orçamento com previsto, realizado e diferença.', 4.5),
     tela(K+'tela-horas-painel.png', F['funil'], 'E as horas por projeto',
          'E quanto cada projeto consumiu de hora e de custo.', 4.5),
   ]),
}

LOTES = {'essencial': ESSENCIAL, 'completo': COMPLETO}
TAG = {'essencial':('R$ 37 · uma vez', 8), 'completo':('R$ 197 · uma vez', 12)}

def monta(prod, codigo, spec):
    C.usa_produto(prod)
    cenas = [dict(c) for c in spec['cenas']] + [dict(PROVA[prod]), dict(FIM[prod])]
    cenas[0]['tagpreco'], cenas[0]['tagpreco_em'] = TAG[prod]
    saida = SAIDA / f'{prod}-{codigo}-9x16.mp4'
    total = C.renderiza(cenas, saida, ROOT / 'trabalho-ganchos' / f'{prod}-{codigo}')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(saida),
                    '-vf','fps=1,scale=-1:420,tile=8x4:padding=6:color=white',
                    '-frames:v','1','-q:v','3',str(SAIDA/f'frames-{prod}-{codigo}.jpg')],check=True)
    print(f'{prod}/{codigo}: {total:.1f}s -> {saida.name}', flush=True)

if __name__ == '__main__':
    alvo = sys.argv[1] if len(sys.argv)>1 else 'todos'
    filtro = sys.argv[2] if len(sys.argv)>2 else None
    for prod in (['essencial','completo'] if alvo=='todos' else [alvo]):
        for codigo, spec in LOTES[prod].items():
            if filtro and filtro not in codigo: continue
            monta(prod, codigo, spec)
