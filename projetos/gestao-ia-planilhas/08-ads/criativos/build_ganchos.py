#!/usr/bin/env python3
"""Lote de ganchos 9:16 para teste de ângulo no Meta Ads.

Cada variação é um anúncio curto e completo (18-22 s) com TRÊS cenas:
gancho (o que muda entre as variações) -> apoio -> fecho de preço (igual dentro
do mesmo produto, para o teste isolar o ângulo e não a oferta).

Uso:  python3 build_ganchos.py [essencial|completo|todos] [codigo-do-gancho]
Saída: ganchos/<produto>-<codigo>-9x16.mp4 + .srt + tira de frames.
Narração por Piper (troca para Google TTS quando a chave entrar).
"""
import sys, pathlib, subprocess, json
import criativo_cenas as C

ROOT = pathlib.Path(__file__).resolve().parent
SAIDA = ROOT / 'ganchos'; SAIDA.mkdir(exist_ok=True)

# ---------------------------------------------------------------- fechos fixos
# Fecho = reversão de risco + CTA único e verbal. Igual dentro do produto: o teste
# precisa isolar o ângulo do gancho, não a oferta nem a chamada.
FIM = {
 'essencial': {'tipo':'fim','min':6.0,
   'fala':'Kit IA no Trabalho Essencial: trinta e sete reais, uma vez. Se não servir, você tem sete dias para pedir o dinheiro de volta, sem explicar. Toque em comprar.',
   'tt':'Kit IA no Trabalho <em>Essencial</em>','preco':'Comprar por R$ 37',
   'nota':'3 planilhas · 40 prompts · manual e vídeos<br>Pix ou cartão · acesso imediato · 7 dias para desistir'},
 'completo': {'tipo':'fim','min':6.5,
   'fala':'Kit IA no Trabalho Completo: cento e noventa e sete reais, uma vez, ou doze vezes no cartão. Sete dias para pedir o dinheiro de volta, sem explicar. Toque em comprar.',
   'tt':'Kit IA no Trabalho <em>Completo</em>','preco':'Comprar por R$ 197',
   'nota':'10 planilhas · 80 prompts · 8 aulas · 3 modelos<br>Pix ou 12× · acesso imediato · 7 dias para desistir'},
}
# Apoio = especificidade. Número exato, nome exato, onde abre. Nada de adjetivo.
PROVA = {
 'essencial': {'tipo':'prova','min':6.0,
   'fala':'Três planilhas prontas, quarenta prompts, mini-manual e três vídeos curtos. Abre no Excel, no Google Planilhas e no celular.',
   'selos':['3 planilhas prontas','40 prompts de IA','Mini-manual','3 vídeos curtos']},
 'completo': {'tipo':'prova','min':6.5,
   'fala':'Dez planilhas prontas, oitenta prompts, oito aulas curtas e três modelos de apresentação. Abre no Excel, no Google Planilhas e no celular.',
   'selos':['10 planilhas prontas','80 prompts de IA','8 aulas curtas','3 modelos de slides']},
}

# ---------------------------------------------------------------- 5 do Essencial
ESSENCIAL = {
 'e1-rapidinho': dict(
   tecnica='Callout + agitação. Nomeia a cena exata em que a pessoa se reconhece e mostra o tamanho real do "pequeno".',
   gancho={'tipo':'dor','min':6.5,
     'fala':'Rapidinho. Rapidinho é juntar os números, explicar o mês e montar os slides. Lá se foi a tarde.',
     'h':'"Um relatório <em>rapidinho.</em>"',
     'itens':['Juntar os números','Explicar o mês','Montar os slides'],
     'rod':'rapidinho leva a tarde inteira'}),
 'e2-300-horas': dict(
   tecnica='Custo da inação quantificado. Tira a decisão do "quero" e põe no "quanto já está me custando".',
   gancho={'tipo':'custo','min':7.0,
     'fala':'Seis horas por semana montando do zero. Em um ano, trezentas horas. Você não está economizando trinta e sete reais: está pagando em tempo.',
     'h':'O que já está te custando',
     'num':300,'passo':6,'unid':'h','small':'por ano montando do zero',
     'leg':'6 horas por semana × 50 semanas. Você paga isso todo ano, em tempo.'}),
 'e3-ia-sem-dado': dict(
   tecnica='Mecanismo único. Explica por que a tentativa anterior falhou e por que esta é diferente.',
   gancho={'tipo':'fluxo','min':9.0,
     'fala':'Você já tentou usar a inteligência artificial e o texto saiu genérico. O motivo é simples: prompt sem planilha não tem dado para trabalhar. O kit junta os dois.',
     'h':'Já tentou e saiu <em>genérico?</em>',
     'passos':[('Preencher','a planilha já vem montada'),
               ('Perguntar','cola os seus números no prompt'),
               ('Entregar','a IA escreve com dado, você revisa')],
     't':[1.9,4.3,6.5],'rod':'o que faltava era o dado, não o prompt'}),
 'e4-sexta-17h': dict(
   tecnica='Future pacing. Mostra a pessoa vivendo o depois, com hora marcada, antes de falar em preço.',
   gancho={'tipo':'dor','min':7.0,
     'fala':'Imagine sexta, cinco da tarde. O relatório já foi. Os slides estão prontos. E você fecha o computador na hora.',
     'h':'Sexta, <em>17h.</em>',
     'itens':['O relatório já foi','Os slides estão prontos','Você fecha o computador'],'positivo':True,
     'rod':'é isso que muda quando a estrutura já existe'}),
 'e5-faca-a-conta': dict(
   tecnica='Ancoragem de preço. Compara com o custo que a pessoa já aceita pagar, e fecha com reversão de risco.',
   gancho={'tipo':'valor','min':7.0,
     'fala':'Seis horas por semana, toda semana, montando do zero. Ou trinta e sete reais, uma vez, e a estrutura fica sua para sempre.',
     'h':'Faça a conta.',
     'c1':('do zero','6 h','por semana, toda semana'),
     'c2':('o kit','R$ 37','uma vez, seu para sempre'),
     'rod':'Pagamento único. Sem mensalidade.'}),
}

# ---------------------------------------------------------------- 5 do Completo
COMPLETO = {
 'c1-mesma-semana': dict(
   tecnica='Callout + agitação por acúmulo. Empilha três cobranças diferentes para mostrar que o problema é a semana, não a tarefa.',
   gancho={'tipo':'dor','min':7.5,
     'fala':'Segunda, o relatório. Quarta, o projeto do cliente. Sexta, a reunião de resultados. Não é uma planilha: é a semana inteira montada do zero.',
     'h':'Tudo na <em>mesma semana.</em>',
     'itens':['Segunda: o relatório','Quarta: o projeto do cliente','Sexta: a reunião de resultados'],
     'rod':'e a planilha de metas continua em branco'}),
 'c2-estruturar': dict(
   tecnica='Mecanismo único com nome. O passo que ninguém faz vira o motivo de o kit funcionar.',
   gancho={'tipo':'fluxo','min':9.5,
     'fala':'O retrabalho não nasce na planilha: nasce antes dela. Por isso o Completo começa em estruturar, e só depois preencher, perguntar e entregar.',
     'h':'O erro acontece <em>antes</em> do Excel.',
     'passos':[('Estruturar','quem lê, quando, para decidir o quê'),
               ('Preencher','as 10 planilhas já vêm prontas'),
               ('Perguntar','80 prompts com os seus números'),
               ('Entregar','modelos de slides e checklists')],
     't':[1.7,3.9,6.1,8.1],'rod':'Kit IA no Trabalho · Completo'}),
 'c3-40-horas': dict(
   tecnica='Custo da inação quantificado, com a dor secundária (inconsistência) logo atrás do número.',
   gancho={'tipo':'custo','min':7.5,
     'fala':'Montar essas dez planilhas do zero leva umas quarenta horas. E no fim, cada uma calcula de um jeito, o que custa mais tempo ainda.',
     'h':'O que custa montar as dez',
     'num':40,'passo':1,'unid':'h','small':'só para montar, sem usar',
     'leg':'Metas, projetos, orçamento, funil, horas. E cada uma calculando de um jeito.'}),
 'c4-nao-e-para-todo-mundo': dict(
   tecnica='Desqualificação honesta (takeaway). Diz para quem não serve, o que aumenta a credibilidade de tudo que vem depois.',
   gancho={'tipo':'dor','min':7.5,
     'fala':'O Completo não serve para quem precisa de uma planilha. Ele serve para a semana que tem projeto, meta, orçamento e funil ao mesmo tempo.',
     'h':'Não é para <em>uma planilha.</em>',
     'itens':['Projeto e prazo','Meta e orçamento','Funil e horas'],
     'rod':'se for uma coisa só, o Completo é grande demais'}),
 'c5-faca-a-conta': dict(
   tecnica='Ancoragem de preço em horas de trabalho, fechando com pagamento único contra mensalidade.',
   gancho={'tipo':'valor','min':7.5,
     'fala':'Quarenta horas montando do zero, sem método, cada arquivo de um jeito. Ou cento e noventa e sete reais, uma vez, em até doze vezes no cartão.',
     'h':'Faça a conta.',
     'c1':('do zero','40 h','do seu tempo, sem método'),
     'c2':('o kit','R$ 197','uma vez, ou 12× no cartão'),
     'rod':'Pagamento único. Sem mensalidade.'}),
}

LOTES = {'essencial': ESSENCIAL, 'completo': COMPLETO}

def monta(prod, codigo, spec):
    C.usa_produto(prod)
    cenas = [dict(spec['gancho']), dict(PROVA[prod]), dict(FIM[prod])]
    saida = SAIDA / f'{prod}-{codigo}-9x16.mp4'
    trab = ROOT / 'trabalho-ganchos' / f'{prod}-{codigo}'
    total = C.renderiza(cenas, saida, trab)
    tira = SAIDA / f'frames-{prod}-{codigo}.jpg'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(saida),
                    '-vf','fps=1,scale=-1:420,tile=8x3:padding=6:color=white',
                    '-frames:v','1','-q:v','3',str(tira)],check=True)
    print(f'{prod}/{codigo}: {total:.1f}s -> {saida.name}')
    return total

if __name__ == '__main__':
    alvo = sys.argv[1] if len(sys.argv)>1 else 'todos'
    filtro = sys.argv[2] if len(sys.argv)>2 else None
    prods = ['essencial','completo'] if alvo=='todos' else [alvo]
    for prod in prods:
        for codigo, spec in LOTES[prod].items():
            if filtro and filtro not in codigo: continue
            monta(prod, codigo, spec)
