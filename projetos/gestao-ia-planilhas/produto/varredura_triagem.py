"""Triagem da varredura: separa ruído conhecido (colunas auxiliares ocultas, predicados de Config que
viram "Não", eco de texto digitado) das mudanças silenciosas que precisam de decisão."""
import json,glob,re,sys
pref=sys.argv[1]
AUX=re.compile(r'^(Pessoas!K|Equipe!K|Precificação![TUVW]\d|Simulador!J5[2-5]:)')
# eco: a célula só mostra a entrada (margem da Config no Painel, horas da pessoa) ou a lista dos 8 casos mais abaixo do mínimo, que se reordena com os dados
ECO=re.compile(r'^(Painel!B1[45]:|Painel!C2[6-9]:|Painel!D2[6-9]:|Referência![A-I](7[8-9]|8[0-5]):)')
PRED=re.compile(r'^Config!B1[0-5]: (Sim→Não|Não→Sim)')
# decisões de produto: vazio = "não se aplica"
DEC={('08-tabela-de-referencia',r'Config!E\d+','texto'):'renomear uma área deixa os casos dela fora da lista: os cartões gerais avisam caso incompleto; a área nova aparece sem casos',
     ('08-tabela-de-referencia',r'Nossos casos!C\d+','vazio'):'caso sem área: os cartões gerais avisam; a área de origem não é conhecida',
     ('08-tabela-de-referencia',r'Nossos casos!C\d+','texto'):'caso com área fora da lista: os cartões gerais avisam; a área de origem não é conhecida',('06-precificacao',r'Precificação![LNPR]\d+','vazio'):'preço de convênio em branco = convênio não atende',
     ('08-tabela-de-precos',r'Tabela![IJKLM]\d+','vazio'):'preço de convênio em branco = convênio não atende',
     ('07-simulador-convenio-x-particular',r'Simulador!B(19|2[0-4])$','vazio'):'valor de tabela em branco = pagador não atende',
     ('07-simulador-convenio-x-particular',r'Simulador!B4[3-8]$','vazio'):'atendimentos em branco = sem volume no mês'}
TEXTCOL=re.compile(r'^(Pessoas![AB]|Equipe![ABC]|Nossos casos![ABDE]|Referência![ABE]\d|Config![ACE]\d|Simulador!A(1[9]|2\d|3\d)|Custos fixos![AC]|Precificação!A|Tabela!(A|T)\d)')
tot=0
for f in sorted(glob.glob(f'/tmp/claude-0/-home-user-claude-code/a6ac5a85-3495-54eb-8ee2-ee26ae091f81/scratchpad/fz/{pref}-*.json')):
    nome=f.split(pref+'-')[1].replace('.json','').split('-',2)[-1]
    linhas=[]
    for r in json.load(open(f)):
        ent,modo=r['entrada'],r['modo']
        dec=[v for (arq,pat,m),v in DEC.items() if arq in f and m==modo and re.match(pat,ent)]
        num=[x for x in r['NUM'] if not AUX.match(x) and not PRED.match(x) and not (ECO.match(x) and (modo=='negativo' or 'Referência' in x))]
        cls=[x for x in r['CLS'] if not PRED.match(x) and not x.endswith('→abc') and not ECO.match(x)]
        if TEXTCOL.match(ent) and modo=='texto': cls=[]; num=[x for x in num if 'Painel!A2' not in x]
        if dec: continue
        if r['ERR'] or num or cls:
            linhas.append(f"  {ent:24} {modo:8} ERR{len(r['ERR'])} NUM{len(num)} CLS{len(cls)} | "+'; '.join(r['ERR'][:2]+num[:3]+cls[:2])[:230])
    print(f'== {nome}: {len(linhas)} caso(s) a triar'); print('\n'.join(linhas)); tot+=len(linhas)
print('TOTAL a triar:',tot)
