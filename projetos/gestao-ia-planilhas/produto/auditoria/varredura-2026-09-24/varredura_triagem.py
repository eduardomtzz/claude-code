"""Triagem da varredura: separa ruído conhecido (colunas auxiliares ocultas, predicados de Config que
viram "Não", eco de texto digitado) das mudanças silenciosas que precisam de decisão."""
import json,glob,re,sys
pref=sys.argv[1]
AUX=re.compile(r'^(Pessoas!K|Equipe!K|Precificação![TUVW]\d|Simulador!J5[2-5]:)')
# eco: a célula só mostra a entrada (margem da Config no Painel, horas da pessoa) ou a lista dos 8 casos mais abaixo do mínimo, que se reordena com os dados
ECO=re.compile(r'^(Painel!B1[45]:|Painel!C2[6-9]:|Painel!D2[6-9]:|Referência![A-I](7[8-9]|8[0-5]):)')
# eco do nome numérico digitado numa linha nova (Painel por pessoa, quadro por área)
NOME=re.compile(r'^(Painel!A(2[6-9]|3\d)|Referência!A(5[4-9]|6\d|7[0-3])|Precificação![LNPR]4|Tabela![H-M]7|Tabela![A-M]26):')
PRED=re.compile(r'^Config!B1[0-5]: (Sim→Não|Não→Sim)')
# decisões de produto: vazio = "não se aplica"
# Auditoria final-6: a decisão não pula mais o cenário inteiro. Cada decisão diz QUAIS saídas podem mudar
# (regex em SAI); o resto continua triado, e erro de fórmula nunca é pulado.
DEC={('08-tabela-de-referencia',r'Config!E\d+','texto'):'renomear uma área deixa os casos dela fora da lista: os cartões gerais avisam caso incompleto; a área nova aparece sem casos',
     ('08-tabela-de-referencia',r'Config!E\d+','novo-texto'):'área nova sem casos: 0 casos, R$ 0 e 0 h no quadro por área são o valor verdadeiro',('08-tabela-de-referencia',r'Config!E\d+','novo-num'):'área nova sem casos (nome numérico)',
     ('08-tabela-de-referencia',r'Nossos casos!C\d+','vazio'):'caso sem área: os cartões gerais avisam; a área de origem não é conhecida',
     ('08-tabela-de-referencia',r'Nossos casos!C\d+','texto'):'caso com área fora da lista: os cartões gerais avisam; a área de origem não é conhecida',('06-precificacao',r'Precificação![LNPR]\d+','vazio'):'preço de convênio em branco = convênio não atende',
     ('06-precificacao',r'Precificação![LNPR]\d+','novo-num'):'preço de convênio digitado numa linha completa é dado válido: a margem da célula, a contagem e o maior prejuízo mudam de verdade',
     ('08-tabela-de-precos',r'Tabela![IJKLM]\d+','vazio'):'preço de convênio em branco = convênio não atende',
     ('08-tabela-de-precos',r'Tabela![IJKLM]\d+','novo-num'):'preço de convênio digitado numa linha completa é dado válido: contagem e hora por pagador mudam de verdade',
     ('08-tabela-de-precos',r'Tabela!A\d+','novo-texto'):'procedimento novo só com nome: o quadro de hora por pagador mostra a hora mínima e a alvo da Config, iguais para todas as linhas',
     ('08-tabela-de-precos',r'Tabela!A\d+','novo-num'):'procedimento novo só com nome (numérico): idem',
     ('06-precificacao',r'Precificação!A6$','texto'):'renomear a linha do Retorno tira a exceção (auditoria final-7): a tabela 0 dela passa a contar como prejuízo',
     ('08-tabela-de-precos',r'Tabela!A9$','texto'):'renomear a linha do Retorno tira a exceção (auditoria final-7): a tabela 0 dela passa a contar',
     ('07-simulador-convenio-x-particular',r'Simulador!B(19|2[0-4])$','vazio'):'valor de tabela em branco = pagador não atende',
     ('07-simulador-convenio-x-particular',r'Simulador!B4[3-8]$','vazio'):'atendimentos em branco = sem volume no mês'}
AREA=r'Referência![B-H](5[4-9]|6\d|7[0-3])$'   # quadro por área (linhas 54 a 73)
SAI={('08-tabela-de-referencia',r'Config!E\d+','texto'):AREA,('08-tabela-de-referencia',r'Nossos casos!C\d+','vazio'):AREA,
     ('08-tabela-de-referencia',r'Nossos casos!C\d+','texto'):AREA,
     ('08-tabela-de-referencia',r'Config!E\d+','novo-texto'):AREA,('08-tabela-de-referencia',r'Config!E\d+','novo-num'):AREA,
     ('06-precificacao',r'Precificação![LNPR]\d+','vazio'):r'Precificação!([MOQS]\d+|E2[56])$',
     ('06-precificacao',r'Precificação![LNPR]\d+','novo-num'):r'Precificação!([MOQS]\d+|E2[56])$',
     ('07-simulador-convenio-x-particular',r'Simulador!B(19|2[0-4])$','vazio'):r'Simulador!([A-N](19|2[0-4])|[A-G]3[1-6]|[A-H]4[3-9]|[GJ]5)$',
     ('07-simulador-convenio-x-particular',r'Simulador!B4[3-8]$','vazio'):r'Simulador![A-H]4[3-9]$',
     ('08-tabela-de-precos',r'Tabela![IJKLM]\d+','vazio'):r'Tabela!(O\d+|E5|[A-M](2[7-9]|3\d))$',
     ('08-tabela-de-precos',r'Tabela![IJKLM]\d+','novo-num'):r'Tabela!(O\d+|E5|[A-M](2[7-9]|3\d))$',
     ('08-tabela-de-precos',r'Tabela!A\d+','novo-texto'):r'Tabela![A-M](2[7-9]|3\d)$',
     ('08-tabela-de-precos',r'Tabela!A\d+','novo-num'):r'Tabela![A-M](2[7-9]|3\d)$',
     ('06-precificacao',r'Precificação!A6$','texto'):r'Precificação!E2[56]$',('08-tabela-de-precos',r'Tabela!A9$','texto'):r'Tabela!(O9|E5)$'}
# colunas de nome/descrição livre: texto nelas é eco, não defeito (auditoria final-6: só nomes, não listas nem modalidades)
TEXTCOL=re.compile(r'^(Pessoas![AB]\d|Equipe![AB]\d|Nossos casos![AB]\d|Referência!B\d|Simulador!A(19|2\d|3\d)$|Custos fixos![AC]\d|Config!A1[0-5]$|Precificação!A\d|Tabela!(A|T)\d)')
tot=0
for f in sorted(glob.glob(f'/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad/fz/{pref}-*.json')):
    nome=f.split(pref+'-')[1].replace('.json','').split('-',2)[-1]
    linhas=[]
    for r in json.load(open(f)):
        ent,modo=r['entrada'],r['modo']
        dec=[(arq,pat,m) for (arq,pat,m) in DEC if arq in f and m==modo and re.match(pat,ent)]
        num=[x for x in r['NUM']+r.get('NEW',[]) if not AUX.match(x) and not PRED.match(x) and not (ECO.match(x) and (modo in ('negativo','novo-num') or 'Referência' in x)) and not (modo=='novo-num' and NOME.match(x))]
        cls=[x for x in r['CLS'] if not PRED.match(x) and not x.endswith('→abc') and not ECO.match(x) and 'sem nome' not in x]   # 'pagador sem nome' é aviso (mesma lista de avisos da varredura)
        inv=r.get('INV',[])   # regra de negócio violada: nunca é dispensada
        if modo in ('zero','x10'): num=[]; cls=[]   # dado válido: número mudar é o esperado; contam só ERR e INV
        if TEXTCOL.match(ent) and modo=='texto': cls=[]; num=[x for x in num if 'Painel!A2' not in x]
        if dec:
            ok=re.compile(SAI.get(dec[0],'$^'))
            num=[x for x in num if not ok.match(x.split(':')[0])]; cls=[x for x in cls if not ok.match(x.split(':')[0])]
        if r['ERR'] or num or cls or inv:
            linhas.append(f"  {ent:24} {modo:8} ERR{len(r['ERR'])} NUM/NEW{len(num)} CLS{len(cls)} INV{len(inv)} | "+'; '.join(r['ERR'][:2]+inv[:2]+num[:3]+cls[:2])[:230])
    print(f'== {nome}: {len(linhas)} caso(s) a triar'); print('\n'.join(linhas)); tot+=len(linhas)
print('TOTAL a triar:',tot)
