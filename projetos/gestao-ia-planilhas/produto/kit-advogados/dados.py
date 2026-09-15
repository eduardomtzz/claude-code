"""Escritório fictício compartilhado por todas as planilhas do Kit de Gestão para Advogados (fonte única do exemplo).
Ferraz & Lima Advocacia: 2 sócios, 1 estagiária, 18 clientes, 38 casos (30 ativos + 8 encerrados), 20 propostas.
Tudo inventado; números de processo seguem o formato CNJ mas não existem.

Referência do exemplo: HOJE = segunda-feira 14/09/2026; a "sexta do painel" é 11/09/2026. Nenhum lançamento pago
(caixa, parcela, horas) tem data depois de 11/09/2026. Datas de prazo/próxima ação/vencimento em aberto são relativas a
HOJE (fórmula =HOJE()+n, via prazo_formula); histórico (abertura, parcelas pagas, caixa, horas) é fixo.

Regra do dinheiro: cada caso tem um cronograma de PARCELAS (paga / a vencer / vencida). Parcela paga <=> entrada no
caixa (09) na data do pagamento (as pagas em 2025 estão no saldo inicial). Recebido do caso (13) = soma das pagas.
Êxito só recebe ao fim (caso encerrado). Recebido <= contratado. Horas gastas <= 1,3 x estimadas."""
import random
from datetime import date, timedelta

ESCRITORIO="Ferraz & Lima Advocacia"
HOJE=date(2026,9,14)          # segunda-feira de referência
SEXTA=date(2026,9,11)         # última sexta (painel da semana)
ANO=2026
ALIQ=0.08                     # alíquota efetiva de impostos do exemplo (única em todo o kit)
MARGEM=0.30                   # margem mínima sobre o preço (05/06/08)
MARGEM_ALVO=0.45              # margem alvo (08)
FOLGA_HORAS=0.20              # folga para horas não previstas (06/08)
SALDO_INICIAL=22000           # caixa em 01/01/2026 (já com honorários recebidos em 2025)
PESSOAS=[  # nome, papel, custo mensal (pró-labore ou bolsa), horas faturáveis/mês (meta)
 ("Marina Ferraz","Sócia · cível e empresarial",6000,110),
 ("Rafael Lima","Sócio · trabalhista e previdenciário",6000,110),
 ("Júlia Prado","Estagiária",1400,60),
]
HORAS_TRABALHO={"Marina Ferraz":160,"Rafael Lima":160,"Júlia Prado":120}
CUSTOS_FIXOS=[("Aluguel e condomínio",2800),("Contador",600),("Sistemas e assinaturas",450),("Telefone e internet",220),
 ("Anuidades OAB e cursos",250),("Marketing e site",400),("Estagiária (bolsa)",1400),("Material, correio e outros",380)]
DIA_FIXO={"Aluguel e condomínio":5,"Contador":10,"Sistemas e assinaturas":8,"Telefone e internet":12,"Anuidades OAB e cursos":15,
          "Marketing e site":20,"Estagiária (bolsa)":5,"Material, correio e outros":18}
CUSTOS_FIXOS_TOTAL=sum(v for _,v in CUSTOS_FIXOS)                                   # 6.500
PRO_LABORE=[(n,v) for n,p,v,_ in PESSOAS if p.startswith("Sóci")]                   # 6.000 + 6.000
PRO_LABORE_TOTAL=sum(v for _,v in PRO_LABORE)                                        # 12.000
CUSTO_TOTAL_MES=CUSTOS_FIXOS_TOTAL+PRO_LABORE_TOTAL                                  # 18.500 (a bolsa já está nos fixos)
HORAS_FATURAVEIS_MES=sum(h for _,_,_,h in PESSOAS)                                   # 280
CUSTO_HORA=round(CUSTO_TOTAL_MES/HORAS_FATURAVEIS_MES,4)                             # 66,0714
HORA_MINIMA_EXATA=round(CUSTO_HORA/(1-MARGEM-ALIQ),2)                                # 106,57
HORA_MINIMA=110                                                                       # arredondada para múltiplo de 5 (05)
HORA_MINIMA_FOLGA=round(CUSTO_HORA*(1+FOLGA_HORAS)/(1-ALIQ-MARGEM),2)                # 127,88 (08: com 20 % de horas não previstas)
HORA_ALVO_FOLGA=round(CUSTO_HORA*(1+FOLGA_HORAS)/(1-ALIQ-MARGEM_ALVO),2)             # 168,70 (08)
CUSTOS_SEM_EQUIPE=sum(v for n,v in CUSTOS_FIXOS if not n.startswith("Estagiária"))  # 5.100 (16)
VALOR_HORA_COBRADA=180                                                                # hora cobrada nos casos por hora do exemplo
AREAS=["Cível","Trabalhista","Previdenciário","Empresarial","Família"]
FASES=["Consultivo","Inicial","Instrução","Sentença","Recurso","Execução","Acordo","Encerrado"]
TIPOS_HON=["Fixo","Hora","Êxito","Misto"]
CAT_ENTRADA=["Honorários fixos","Honorários por hora","Honorários de êxito","Consultoria e pareceres","Reembolso de custas","Outras entradas"]
CAT_SAIDA=["Pró-labore dos sócios"]+[c for c,_ in CUSTOS_FIXOS]+["Impostos e taxas","Custas e despesas de processo","Deslocamento e viagens","Outras saídas"]
CLIENTES=[("Padaria do Sol Ltda","PJ","Empresarial"),("Ana Beatriz Moreira","PF","Trabalhista"),("Construtora Horizonte","PJ","Cível"),
 ("Carlos Eduardo Nunes","PF","Previdenciário"),("Loja Verde Comércio","PJ","Empresarial"),("Fernanda Castro","PF","Família"),
 ("Bistrô 42","PJ","Trabalhista"),("Roberto Almeida","PF","Cível"),("Clínica Bem-Estar","PJ","Empresarial"),("Marcos Vinícius Teles","PF","Previdenciário"),
 ("Transportadora Rota Sul","PJ","Trabalhista"),("Patrícia Gomes","PF","Família"),("Escola Aurora","PJ","Cível"),("José Antônio Ribeiro","PF","Previdenciário"),
 ("Oficina Mecânica Central","PJ","Trabalhista"),("Luciana Farias","PF","Cível"),("Agência Prisma","PJ","Empresarial"),("Helena Duarte","PF","Trabalhista")]
CLI={n:(n,t,a) for n,t,a in CLIENTES}
MAR,RAF,JUL=[p[0] for p in PESSOAS]
# fase -> próximas ações possíveis (o exemplo só usa combinações desta tabela)
ACOES_POR_FASE={"Inicial":["Contestação","Réplica","Juntada de documentos","Audiência de conciliação"],
 "Instrução":["Audiência de instrução","Manifestação sobre laudo","Alegações finais"],
 "Sentença":["Embargos de declaração","Recurso de apelação"],
 "Recurso":["Contrarrazões","Manifestação sobre o recurso"],
 "Execução":["Cumprimento de sentença","Manifestação sobre a penhora","Impugnação"],
 "Acordo":["Minuta de acordo","Homologação do acordo","Reunião com cliente"],
 "Consultivo":["Entrega de parecer","Reunião com cliente"]}
AUDIENCIAS=("Audiência de conciliação","Audiência de instrução")   # audiência passada não é "prazo atrasado"
TIPOS_PRAZO=["Contestação","Réplica","Audiência de conciliação","Audiência de instrução","Manifestação sobre laudo","Alegações finais",
 "Embargos de declaração","Recurso de apelação","Contrarrazões","Manifestação sobre o recurso","Cumprimento de sentença",
 "Manifestação sobre a penhora","Impugnação","Minuta de acordo","Homologação do acordo","Entrega de parecer","Juntada de documentos","Reunião com cliente","Prazo interno"]

def D(y,m,d): return date(y,m,d)
def prazo_formula(dias):
    """Prazo do exemplo como fórmula relativa a hoje (não envelhece)."""
    return "=TODAY()" if dias==0 else f"=TODAY(){dias:+d}"
def dias(d): return (d-HOJE).days
def _cnj(rng,ano): return f"{rng.randint(1000000,9999999):07d}-{rng.randint(10,99)}.{ano}.8.26.{rng.randint(1,700):04d}"

# ---------------------------------------------------------------------------------------------------------------
# CASOS. Cada tupla: chave, cliente, área, fase, modalidade, valor fixo, êxito esperado, abertura, encerramento,
# horas estimadas, horas gastas até hoje, (dias do prazo, descrição, observação), dias desde a última atualização,
# plano de pagamento, custas do caso.
# plano: ("entrada", valor_entrada, data_pgto_entrada, [(vencimento, valor, data_pgto|None), ...])  parcelas do valor fixo
#        ("faturas", [(vencimento, valor, data_pgto|None), ...])  casos por hora: faturas mensais das horas do mês anterior
#        ("exito", data_pgto|None)  honorários de êxito, pagos só ao fim (caso encerrado)
#        ("nenhum",)  êxito de caso ativo: nada a parcelar ainda
# ---------------------------------------------------------------------------------------------------------------
_C=[]
def _c(chave,cliente,area,fase,tipo,fixo,exito,abertura,encerramento,hest,hg,prazo,ult,plano,custas=()):
    _C.append(dict(chave=chave,cliente=cliente,area=area,fase=fase,tipo_hon=tipo,valor_fixo=fixo,valor_exito=exito,abertura=abertura,
                   encerramento=encerramento,horas_estimadas=hest,horas_gastas=hg,prazo=prazo,ultima_atualizacao_dias=ult,plano=plano,custas=list(custas)))
P=lambda *a: a
# ---- ativos (30) ----
_c("A01","Padaria do Sol Ltda","Empresarial","Consultivo","Fixo",18000,0,D(2026,6,29),None,72,16,(9,"Reunião com cliente","Reunião mensal da assessoria"),6,
   ("entrada",0,None,[(D(2026,7,5),1500,D(2026,7,6))]+[(D(2026,8,5),1500,D(2026,8,5)),(D(2026,9,5),1500,D(2026,9,8))]+[(D(2026,m,5),1500,None) for m in (10,11,12)]+[(D(2027,m,5),1500,None) for m in (1,2,3,4,5,6)]))
_c("A02","Ana Beatriz Moreira","Trabalhista","Inicial","Êxito",0,6000,D(2026,7,7),None,70,22,(2,"Audiência de conciliação","Cliente confirmou presença"),4,("nenhum",))
_c("A03","Construtora Horizonte","Cível","Inicial","Misto",10500,5000,D(2026,7,22),None,90,34,(-3,"Réplica","Confirmar com o cliente ainda hoje"),3,
   ("entrada",4200,D(2026,7,29),[(D(2026,8,28),2100,D(2026,8,28)),(D(2026,9,28),2100,None),(D(2026,10,28),2100,None)]))
_c("A04","Carlos Eduardo Nunes","Previdenciário","Inicial","Fixo",5400,0,D(2026,7,28),None,40,15,(6,"Juntada de documentos","Pedir 2 comprovantes ao cliente"),5,
   ("entrada",2400,D(2026,7,31),[(D(2026,8,31),1500,D(2026,8,31)),(D(2026,9,30),1500,None)]))
_c("A05","Loja Verde Comércio","Empresarial","Consultivo","Fixo",8400,0,D(2026,8,11),None,45,24,(4,"Entrega de parecer","Rascunho começado"),2,
   ("entrada",0,None,[(D(2026,8,18),2800,D(2026,8,18)),(D(2026,9,17),2800,None),(D(2026,10,19),2800,None)]))
_c("A06","Marcos Vinícius Teles","Previdenciário","Consultivo","Fixo",4500,0,D(2026,8,19),None,24,16,(0,"Entrega de parecer","Parecer revisado; enviar hoje"),1,
   ("entrada",0,None,[(D(2026,8,26),2250,D(2026,8,27)),(D(2026,9,25),2250,None)]))
_c("A07","Escola Aurora","Cível","Consultivo","Fixo",13200,0,D(2026,8,3),None,72,9,(3,"Reunião com cliente","Reunião mensal da assessoria"),9,
   ("entrada",0,None,[(D(2026,8,10),1100,D(2026,8,10)),(D(2026,9,10),1100,D(2026,9,10))]+[(D(2026,m,10),1100,None) for m in (10,11,12)]+[(D(2027,m,10),1100,None) for m in (1,2,3,4,5,6,7)]))
_c("A08","Bistrô 42","Trabalhista","Instrução","Fixo",9500,0,D(2026,1,12),None,80,70,(9,"Audiência de instrução","Sala 3, 14h; testemunha avisada"),12,
   ("entrada",3200,D(2026,1,19),[(D(2026,2,18),2100,D(2026,2,20)),(D(2026,3,18),2100,None),(D(2026,4,17),2100,None)]),[(D(2026,6,8),"Certidões e cópias",95)])
_c("A09","Bistrô 42","Trabalhista","Execução","Êxito",0,4000,D(2025,8,18),None,45,50,(15,"Cumprimento de sentença",""),41,("nenhum",))
_c("A10","Roberto Almeida","Cível","Sentença","Fixo",15000,0,D(2025,12,1),None,95,88,(-1,"Embargos de declaração","Minuta pronta; protocolar hoje"),2,
   ("entrada",6000,D(2025,12,8),[(D(2026,1,7),3000,D(2026,1,12)),(D(2026,2,6),3000,D(2026,2,9)),(D(2026,3,9),3000,D(2026,3,9))]))
_c("A11","Roberto Almeida","Cível","Recurso","Misto",7200,3000,D(2026,5,4),None,60,48,(8,"Contrarrazões",""),7,
   ("entrada",3000,D(2026,5,11),[(D(2026,6,10),2100,D(2026,6,10)),(D(2026,7,10),2100,D(2026,7,17))]),[(D(2026,7,13),"Custas de recurso",310)])
_c("A12","Clínica Bem-Estar","Empresarial","Consultivo","Hora",21600,0,D(2025,11,10),None,120,107,(5,"Reunião com cliente","Revisão semestral do contrato"),8,
   ("faturas",[(D(2025,12,10),1800,D(2025,12,10)),(D(2026,1,12),2520,D(2026,1,12)),(D(2026,2,10),1980,D(2026,2,10)),(D(2026,3,10),2340,D(2026,3,10)),
               (D(2026,4,10),1800,D(2026,4,10)),(D(2026,5,11),2160,D(2026,5,11)),(D(2026,6,10),1620,D(2026,6,10)),(D(2026,7,10),1980,D(2026,7,14)),
               (D(2026,8,10),1440,D(2026,8,10)),(D(2026,9,10),1620,D(2026,9,11))]))
_c("A13","Clínica Bem-Estar","Empresarial","Inicial","Fixo",18000,0,D(2026,5,18),None,110,45,(0,"Contestação","Pasta separada na mesa"),1,
   ("entrada",7200,D(2026,5,25),[(D(2026,6,24),2700,D(2026,6,24)),(D(2026,7,24),2700,D(2026,7,30)),(D(2026,8,24),2700,D(2026,8,28)),(D(2026,9,24),2700,None)]))
_c("A14","Transportadora Rota Sul","Trabalhista","Instrução","Fixo",13500,0,D(2025,12,1),None,90,78,(4,"Manifestação sobre laudo","Levar via impressa"),6,
   ("entrada",5500,D(2025,12,8),[(D(2026,1,7),2000,D(2026,1,7)),(D(2026,2,6),2000,D(2026,2,6)),(D(2026,3,9),2000,D(2026,3,20)),(D(2026,4,8),2000,D(2026,4,8))]),
   [(D(2026,3,3),"Diligência de oficial de justiça",130)])
_c("A15","Transportadora Rota Sul","Trabalhista","Inicial","Êxito",0,9000,D(2026,4,13),None,80,30,(20,"Audiência de conciliação",""),13,("nenhum",))
_c("A16","Transportadora Rota Sul","Trabalhista","Consultivo","Fixo",4400,0,D(2026,7,13),None,28,24,(-5,"Reunião com cliente","Cliente pediu para remarcar; sem nova data"),18,
   ("entrada",0,None,[(D(2026,7,20),2200,D(2026,7,20)),(D(2026,8,19),2200,D(2026,8,19))]))
_c("A17","Patrícia Gomes","Família","Acordo","Fixo",9000,0,D(2026,3,16),None,55,48,(0,"Minuta de acordo","Enviar a minuta para a outra parte"),1,
   ("entrada",3600,D(2026,3,23),[(D(2026,4,22),1800,D(2026,4,22)),(D(2026,5,22),1800,D(2026,5,22)),(D(2026,6,22),1800,D(2026,8,10))]))
_c("A18","Patrícia Gomes","Família","Execução","Fixo",6600,0,D(2026,6,8),None,45,33,(-2,"Impugnação","Aguardando documentos do cliente"),4,
   ("entrada",2400,D(2026,6,15),[(D(2026,7,15),2100,D(2026,7,20)),(D(2026,8,14),2100,None)]),[(D(2026,8,5),"Custas de execução",380)])
_c("A19","Escola Aurora","Cível","Sentença","Misto",6000,4000,D(2025,10,20),None,90,100,(2,"Recurso de apelação","Cliente decidiu recorrer"),3,
   ("entrada",2400,D(2025,10,27),[(D(2025,11,26),1200,D(2025,11,26)),(D(2025,12,26),1200,D(2025,12,29)),(D(2026,1,26),1200,D(2026,2,2))]),[(D(2026,9,4),"Certidões",70)])
_c("A20","José Antônio Ribeiro","Previdenciário","Instrução","Êxito",0,4000,D(2026,1,26),None,40,30,(-4,"Manifestação sobre laudo","Laudo recebido; rascunho começado"),5,("nenhum",),
   [(D(2026,1,14),"Custas iniciais",260)])
_c("A21","Oficina Mecânica Central","Trabalhista","Instrução","Fixo",15000,0,D(2025,11,17),None,95,86,(10,"Alegações finais",""),9,
   ("entrada",5000,D(2025,11,24),[(D(2025,12,23),2000,D(2025,12,23)),(D(2026,1,23),2000,D(2026,1,23)),(D(2026,2,23),2000,D(2026,3,2)),(D(2026,3,23),2000,D(2026,3,23)),(D(2026,4,23),2000,D(2026,4,23))]))
_c("A22","Oficina Mecânica Central","Trabalhista","Inicial","Misto",6000,3000,D(2026,4,13),None,60,27,(12,"Audiência de conciliação",""),36,
   ("entrada",3000,D(2026,4,20),[(D(2026,5,20),1500,D(2026,5,27)),(D(2026,6,19),1500,None)]),[(D(2026,5,6),"Custas de distribuição",310)])
_c("A23","Luciana Farias","Cível","Inicial","Fixo",12000,0,D(2026,5,25),None,75,45,(-6,"Juntada de documentos","Pedir 2 comprovantes ao cliente"),4,
   ("entrada",4500,D(2026,6,1),[(D(2026,7,1),2500,D(2026,7,1)),(D(2026,7,31),2500,D(2026,8,7)),(D(2026,8,31),2500,D(2026,8,31))]))
_c("A24","Luciana Farias","Cível","Acordo","Misto",3600,4000,D(2026,6,29),None,40,34,(18,"Homologação do acordo","Minuta assinada; aguardando homologação"),33,
   ("entrada",2400,D(2026,7,6),[(D(2026,8,5),1200,D(2026,8,5))]))
_c("A25","Agência Prisma","Empresarial","Recurso","Hora",24000,0,D(2025,12,8),None,133,126,(27,"Contrarrazões",""),11,
   ("faturas",[(D(2026,1,12),2880,D(2026,1,12)),(D(2026,2,10),3240,D(2026,2,10)),(D(2026,3,10),2520,D(2026,3,10)),(D(2026,4,10),3060,D(2026,4,10)),
               (D(2026,5,11),2160,D(2026,5,11)),(D(2026,6,10),2700,D(2026,6,10)),(D(2026,7,10),2340,D(2026,7,15)),(D(2026,8,10),1800,None),(D(2026,9,10),1980,None)]),
   [(D(2026,4,16),"Custas de recurso",540)])
_c("A26","Agência Prisma","Empresarial","Consultivo","Fixo",7000,0,D(2026,4,6),None,30,26,(16,"Entrega de parecer","Parecer sobre o novo contrato"),15,
   ("entrada",0,None,[(D(2026,4,13),3500,D(2026,4,13)),(D(2026,5,13),3500,D(2026,5,20))]))
_c("A27","Helena Duarte","Trabalhista","Execução","Êxito",0,7000,D(2025,7,14),None,70,58,(22,"Cumprimento de sentença",""),47,("nenhum",))
_c("A28","Helena Duarte","Trabalhista","Inicial","Fixo",7500,0,D(2026,6,22),None,55,24,(1,"Réplica",""),2,
   ("entrada",3000,D(2026,6,29),[(D(2026,7,29),1500,D(2026,7,29)),(D(2026,8,28),1500,None),(D(2026,9,28),1500,None)]))
_c("A29","Carlos Eduardo Nunes","Previdenciário","Sentença","Misto",3600,4000,D(2026,3,9),None,40,40,(3,"Embargos de declaração",""),3,
   ("entrada",1800,D(2026,3,16),[(D(2026,4,15),1800,D(2026,4,15))]))
_c("A30","Marcos Vinícius Teles","Previdenciário","Recurso","Fixo",5400,0,D(2026,6,1),None,35,30,(-1,"Manifestação sobre o recurso","Aguardando documentos do cliente"),2,
   ("entrada",2400,D(2026,6,8),[(D(2026,7,8),1000,D(2026,7,8)),(D(2026,8,7),1000,D(2026,8,7)),(D(2026,9,7),1000,D(2026,9,8))]))
# ---- encerrados (8) ----
_c("E01","Padaria do Sol Ltda","Empresarial","Encerrado","Fixo",12000,0,D(2025,11,3),D(2026,3,25),60,64,None,None,
   ("entrada",3000,D(2025,11,17),[(D(2025,12,17),2250,D(2025,12,17)),(D(2026,1,19),2250,D(2026,1,19)),(D(2026,2,17),2250,D(2026,2,17)),(D(2026,3,17),2250,D(2026,3,17))]))
_c("E02","Construtora Horizonte","Cível","Encerrado","Misto",9000,9000,D(2025,6,2),D(2026,4,30),110,120,None,None,
   ("entrada",3000,D(2025,6,9),[(D(2025,7,9),2000,D(2025,7,9)),(D(2025,8,8),2000,D(2025,8,8)),(D(2025,9,9),2000,D(2025,9,9))],D(2026,5,8)),
   [(D(2026,2,9),"Honorários periciais adiantados",780)])
_c("E03","Marcos Vinícius Teles","Previdenciário","Encerrado","Êxito",0,6500,D(2025,2,14),D(2026,1,30),45,50,None,None,("exito",D(2026,2,6)))
_c("E04","Loja Verde Comércio","Empresarial","Encerrado","Fixo",6000,0,D(2025,9,15),D(2026,6,12),45,40,None,None,
   ("entrada",2000,D(2025,9,22),[(D(2025,10,22),1000,D(2025,10,22)),(D(2025,11,21),1000,D(2025,11,21)),(D(2025,12,22),1000,D(2025,12,22)),(D(2026,1,22),1000,D(2026,1,22))]))
_c("E05","Oficina Mecânica Central","Trabalhista","Encerrado","Fixo",12000,0,D(2025,5,5),D(2026,7,31),95,100,None,None,
   ("entrada",2400,D(2025,5,12),[(D(2025,6,12),800,D(2025,6,12)),(D(2025,7,11),800,D(2025,7,11)),(D(2025,8,12),800,D(2025,8,12)),(D(2025,9,12),800,D(2025,9,12)),
    (D(2025,10,13),800,D(2025,10,13)),(D(2025,11,12),800,D(2025,11,12)),(D(2025,12,12),800,D(2025,12,12)),(D(2026,1,12),800,D(2026,1,12)),(D(2026,2,12),800,D(2026,2,12)),
    (D(2026,3,12),800,D(2026,3,12)),(D(2026,4,13),800,D(2026,4,13)),(D(2026,5,12),800,D(2026,5,12))]))
_c("E06","Fernanda Castro","Família","Encerrado","Fixo",7000,0,D(2025,10,6),D(2026,8,14),55,58,None,None,
   ("entrada",2800,D(2025,10,13),[(D(2025,11,13),1400,D(2025,11,13)),(D(2025,12,15),1400,D(2025,12,15)),(D(2026,1,13),1400,D(2026,1,15)),(D(2026,2,13),1400,None)]))
_c("E07","José Antônio Ribeiro","Previdenciário","Encerrado","Êxito",0,6000,D(2025,4,1),D(2026,6,26),40,44,None,None,("exito",D(2026,6,30)))
_c("E08","Ana Beatriz Moreira","Trabalhista","Encerrado","Misto",3000,5500,D(2025,1,20),D(2026,3,13),70,76,None,None,
   ("entrada",3000,D(2025,1,27),[],D(2026,3,20)))
# pendências do checklist (04): índice do item de abertura / encerramento -> "Não" ou "" (vazio)
PEND_ABERTURA={"A02":{0:"Não"},"A05":{4:""},"A15":{4:"Não"},"A20":{2:"Não"},"A22":{7:"",8:""},"A24":{1:"Não"},"A28":{3:"Não"}}
PEND_ENCERRAMENTO={"E06":{0:"Não",5:"Não"},"E05":{2:"",5:"Não"},"E02":{3:"Não"}}
# observações da aba Processos (02) para os casos parados ou aguardando algo
OBS_ANDAMENTO={"A09":"Aguardando andamento da execução (penhora)","A22":"Aguardando designação da audiência","A24":"Aguardando homologação do acordo pelo juízo",
               "A27":"Aguardando andamento da execução","A16":"Cliente pediu para remarcar a reunião","A30":"Aguardando documentos do cliente","A18":"Aguardando documentos do cliente"}

def _monta_casos():
    rng=random.Random(2026); out=[]; nseq=0
    for c in _C:
        cli,tipo_cli,_=CLI[c["cliente"]]
        fase=c["fase"]; area=c["area"]
        resp=MAR if area in ("Cível","Empresarial","Família") else RAF
        if fase=="Consultivo": nseq+=1; numero=f"CONS-{c['abertura'].year}-{nseq:02d}"
        else: numero=_cnj(rng,c["abertura"].year)
        # parcelas do cronograma contratado
        parcelas=[]; plano=c["plano"]; k=0
        def add(venc,valor,pago,desc):
            nonlocal k
            k+=1; parcelas.append(dict(n=k,vencimento=venc,valor=valor,pago=pago is not None,pagamento=pago,descricao=desc))
        if plano[0]=="entrada":
            _,ent,dpe,lst=plano[:4]
            if ent: add(c["abertura"]+timedelta(days=7),ent,dpe,"Entrada")
            for venc,val,pg in lst: add(venc,val,pg,"Parcela")
            if len(plano)>4 and plano[4] is not None: add(plano[4],c["valor_exito"],plano[4],"Honorários de êxito")
        elif plano[0]=="faturas":
            for venc,val,pg in plano[1]: add(venc,val,pg,"Fatura de horas")
        elif plano[0]=="exito":
            add(plano[1],c["valor_exito"],plano[1],"Honorários de êxito")
        recebido=sum(p["valor"] for p in parcelas if p["pago"])
        valor=c["valor_fixo"]+c["valor_exito"]
        assert recebido<=valor, (c["chave"],recebido,valor)
        assert c["horas_gastas"]<=1.3*c["horas_estimadas"], (c["chave"],c["horas_gastas"],c["horas_estimadas"])
        for p in parcelas:
            assert p["pagamento"] is None or p["pagamento"]<=SEXTA, (c["chave"],p)
            assert p["pagamento"] is None or p["pagamento"]>=c["abertura"], (c["chave"],p)
        pd=None; desc=""; obs=""
        if c["prazo"]:
            pd,desc,obs=c["prazo"]
            assert desc in ACOES_POR_FASE[fase], (c["chave"],fase,desc)
            if desc in AUDIENCIAS: assert pd>=0, (c["chave"],"audiência passada não é prazo atrasado")
        if c["tipo_hon"]=="Êxito" and fase!="Encerrado": assert recebido==0, c["chave"]
        if fase=="Encerrado": assert c["encerramento"] is not None
        out.append(dict(chave=c["chave"],numero=numero,cliente=cli,tipo_cliente=tipo_cli,area=area,fase=fase,responsavel=resp,tipo_hon=c["tipo_hon"],
                        valor_contratado=valor,valor_fixo=c["valor_fixo"],valor_exito=c["valor_exito"],recebido=recebido,
                        horas_estimadas=c["horas_estimadas"],horas_gastas=c["horas_gastas"],abertura=c["abertura"],encerramento=c["encerramento"],
                        proximo_prazo_dias=pd,descricao_prazo=desc,obs_prazo=obs,ultima_atualizacao_dias=c["ultima_atualizacao_dias"],parcelas=parcelas,custas=c["custas"]))
    return out
CASOS=_monta_casos()
CASO={c["chave"]:c for c in CASOS}
def caso_por_numero(n): return next(c for c in CASOS if c["numero"]==n)

def status_parcela(p,ref=HOJE):
    if p["pago"] and p["pagamento"]<=ref: return "Paga"
    return "Vencida" if p["vencimento"]<ref else "A vencer"
def PARCELAS():
    """Lista plana das parcelas de todos os casos (ordem: caso, nº)."""
    return [dict(caso=c,**p) for c in CASOS for p in c["parcelas"]]
def categoria_entrada(c,p):
    if p["descricao"]=="Honorários de êxito": return "Honorários de êxito"
    if c["fase"]=="Consultivo" or (c["fase"]=="Encerrado" and c["numero"].startswith("CONS")): return "Consultoria e pareceres"
    if c["tipo_hon"]=="Hora": return "Honorários por hora"
    return "Honorários fixos"

# ---------------------------------------------------------------------------------------------------------------
# AGENDA (01): um prazo principal por caso ativo (o mesmo que a "próxima ação" da 02) + compromissos extras.
# ---------------------------------------------------------------------------------------------------------------
PRAZOS_EXTRAS=[  # chave do caso, tipo, dias, responsável (None = o do caso), feito?, observação
 ("A08","Juntada de documentos",5,JUL,False,"Ata da audiência anterior"),
 ("A21","Reunião com cliente",12,None,False,"Alinhar alegações finais"),
 ("A15","Juntada de documentos",16,JUL,False,"Procuração atualizada"),
 ("A02","Prazo interno",1,None,False,"Preparar o cliente para a audiência"),
 ("A25","Reunião com cliente",31,None,False,"Fechar as horas do recurso"),
 ("A12","Juntada de documentos",45,JUL,False,"Alteração contratual na junta"),
 ("A10","Juntada de documentos",-6,JUL,True,"Entregue no protocolo"),
 ("A17","Reunião com cliente",-10,None,True,"Feita por vídeo"),
]
def PRAZOS():
    """Linhas da aba Prazos da 01: (numero, cliente, tipo, dias, responsável, feito, observação)."""
    out=[]
    for c in CASOS:
        if c["proximo_prazo_dias"] is None: continue
        resp=JUL if c["descricao_prazo"]=="Juntada de documentos" else c["responsavel"]
        out.append((c["numero"],c["cliente"],c["descricao_prazo"],c["proximo_prazo_dias"],resp,False,c["obs_prazo"]))
    for ch,t,d,resp,feito,obs in PRAZOS_EXTRAS:
        c=CASO[ch]; out.append((c["numero"],c["cliente"],t,d,resp or c["responsavel"],feito,obs))
    return out
def resumo_prazos(alerta=7):
    """Contagens do painel da 01 em HOJE: atrasados, hoje, próximos N dias (só prazos não feitos)."""
    ab=[p for p in PRAZOS() if not p[5]]
    return dict(atrasados=sum(1 for p in ab if p[3]<0),hoje=sum(1 for p in ab if p[3]==0),semana=sum(1 for p in ab if 0<p[3]<=alerta),abertos=len(ab))

# ---------------------------------------------------------------------------------------------------------------
# PROPOSTAS (15 e 07): 20 propostas de maio a setembro de 2026. As fechadas em 2026 viraram casos (campo caso).
# datas: entrada (1º contato), proposta (envio; None se ainda não enviada), última movimentação, fechamento previsto,
# fechamento (fixo, se fechada/perdida). Datas futuras/abertas em dias relativos a HOJE (int); históricas em date.
# ---------------------------------------------------------------------------------------------------------------
PROPOSTAS=[]
def _p(numero,cliente,area,servico,origem,resp,valor,mod,etapa,entrada,proposta,ult,prev,fech,motivo,obs,caso=None):
    PROPOSTAS.append(dict(numero=numero,cliente=cliente,area=area,servico=servico,origem=origem,responsavel=resp,valor=valor,modalidade=mod,etapa=etapa,
                          entrada=entrada,proposta=proposta,ultima_mov=ult,fech_previsto=prev,fechamento=fech,motivo=motivo,obs=obs,caso=caso))
_p("2026-005","Padaria do Sol Ltda","Empresarial","Assessoria mensal (12 meses)","Cliente antigo",MAR,18000,"Fixo","Fechada",D(2026,6,8),D(2026,6,15),D(2026,6,29),D(2026,7,3),D(2026,6,29),"","R$ 1.500 por mês","A01")
_p("2026-006","Ana Beatriz Moreira","Trabalhista","Ação trabalhista","Indicação de cliente",RAF,6000,"Êxito","Fechada",D(2026,6,15),D(2026,6,24),D(2026,7,7),D(2026,7,10),D(2026,7,7),"","Valor estimado; recebe no fim","A02")
_p("2026-007","Construtora Horizonte","Cível","Cobrança judicial","Cliente antigo",MAR,15500,"Misto","Fechada",D(2026,7,1),D(2026,7,8),D(2026,7,22),D(2026,7,31),D(2026,7,22),"","Fixo de R$ 10.500 mais êxito estimado em R$ 5.000","A03")
_p("2026-008","Carlos Eduardo Nunes","Previdenciário","Revisão de benefício","Site e Google",RAF,5400,"Fixo","Fechada",D(2026,7,13),D(2026,7,17),D(2026,7,28),D(2026,8,5),D(2026,7,28),"","","A04")
_p("2026-009","Escola Aurora","Cível","Assessoria mensal (12 meses)","Cliente antigo",MAR,13200,"Fixo","Fechada",D(2026,7,14),D(2026,7,21),D(2026,8,3),D(2026,8,7),D(2026,8,3),"","R$ 1.100 por mês","A07")
_p("2026-010","Bistrô 42","Trabalhista","Defesa em reclamação trabalhista","Indicação de cliente",RAF,5200,"Hora","Perdida",D(2026,6,22),D(2026,6,30),D(2026,7,14),D(2026,7,17),D(2026,7,14),"Preço","Estimativa de 35 horas; preferiu valor fixo de outro escritório")
_p("2026-011","Fernanda Castro","Família","Divórcio e partilha","Site e Google",MAR,6500,"Fixo","Perdida",D(2026,7,6),D(2026,7,10),D(2026,7,27),D(2026,7,31),D(2026,7,27),"Fechou com outro escritório","")
_p("2026-012","Loja Verde Comércio","Empresarial","Contratos e consultoria","Parceria (contador, imobiliária)",MAR,8400,"Fixo","Fechada",D(2026,7,20),D(2026,7,23),D(2026,8,11),D(2026,8,14),D(2026,8,11),"","Três pareceres e revisão dos contratos com fornecedores","A05")
_p("2026-013","Marcos Vinícius Teles","Previdenciário","Planejamento previdenciário","Instagram",RAF,4500,"Fixo","Fechada",D(2026,8,3),D(2026,8,6),D(2026,8,19),D(2026,8,28),D(2026,8,19),"","","A06")
_p("2026-014","Oficina Mecânica Central","Trabalhista","Ação trabalhista","Evento ou palestra",RAF,4400,"Êxito","Perdida",D(2026,8,4),D(2026,8,6),D(2026,8,25),D(2026,8,28),D(2026,8,25),"Sem resposta","")
_p("2026-015","Agência Prisma","Empresarial","Contratos e consultoria","Instagram",MAR,11000,"Fixo","Perdida",D(2026,8,12),D(2026,8,14),D(2026,9,2),D(2026,9,4),D(2026,9,2),"Preço","Cliente questiona as horas do recurso em andamento")
_p("2026-016","Transportadora Rota Sul","Trabalhista","Assessoria mensal (12 meses)","Cliente antigo",RAF,14400,"Fixo","Negociação",D(2026,8,17),D(2026,8,20),-4,6,None,"","Pediu parcela mensal menor")
_p("2026-017","Clínica Bem-Estar","Empresarial","Contratos com convênios","Cliente antigo",MAR,6800,"Fixo","Negociação",D(2026,8,24),D(2026,8,26),-17,-2,None,"","Reunião de apresentação feita; sem retorno")
_p("2026-018","Patrícia Gomes","Família","Inventário","Indicação de cliente",MAR,10500,"Fixo","Proposta enviada",D(2026,8,26),D(2026,8,29),-16,12,None,"","")
_p("2026-019","José Antônio Ribeiro","Previdenciário","Revisão de benefício","Site e Google",RAF,4200,"Fixo","Proposta enviada",D(2026,8,28),D(2026,8,31),-14,-6,None,"","Sem retorno; ligar")
_p("2026-020","Helena Duarte","Trabalhista","Ação trabalhista","Indicação de cliente",RAF,5800,"Êxito","Reunião feita",D(2026,9,2),None,-3,20,None,"","")
_p("2026-021","Luciana Farias","Cível","Cobrança judicial","Parceria (contador, imobiliária)",MAR,7900,"Misto","Reunião feita",D(2026,9,4),None,-2,25,None,"","")
_p("2026-022","Construtora Horizonte","Empresarial","Assessoria mensal (12 meses)","Cliente antigo",MAR,13200,"Fixo","Contato",D(2026,9,9),None,-1,30,None,"","")
_p("2026-023","Roberto Almeida","Cível","Discussão de contrato de prestação de serviços","Cliente antigo",MAR,4500,"Misto","Proposta enviada",D(2026,9,9),0,0,15,None,"","Mais 15% de êxito · é a proposta da aba Proposta da planilha 07")
_p("2026-024","Marcos Vinícius Teles","Família","Divórcio e partilha","Cliente antigo",MAR,5600,"Fixo","Contato",D(2026,9,11),None,-3,35,None,"","")
for _pp in PROPOSTAS:
    if _pp["caso"]:
        _cc=CASO[_pp["caso"]]; assert _cc["abertura"]==_pp["fechamento"] and _cc["valor_contratado"]==_pp["valor"] and _cc["cliente"]==_pp["cliente"], _pp["numero"]
PROP_NUM_ATUAL="2026-023"   # proposta da aba Proposta da 07 (Roberto Almeida)
def propostas_registro_07(n=10):
    """As n propostas mais recentes já enviadas (data de envio mais recente primeiro), como aparecem no Registro da 07."""
    def dt(p): return HOJE+timedelta(days=p["proposta"]) if isinstance(p["proposta"],int) else p["proposta"]
    env=[p for p in PROPOSTAS if p["proposta"] is not None]
    env.sort(key=lambda p:(dt(p),p["numero"]),reverse=True)
    return env[:n]
SIT_07={"Fechada":"Fechada","Perdida":"Perdida"}   # demais etapas com proposta enviada = "Enviada"

# ---------------------------------------------------------------------------------------------------------------
# CAIXA (09): lançamentos gerados das parcelas + custos fixos, pró-labore, impostos, custas, movimentos dos sócios.
# ---------------------------------------------------------------------------------------------------------------
DISTRIB=0.5          # parte do lucro do trimestre distribuída aos sócios (regra da 11)
LUCRO_MINIMO=3000    # lucro mínimo do trimestre para distribuir (11)
def lancamentos():
    """Lista de tuplas (data, tipo, categoria, cliente, caso, descrição, valor, forma, pago) de jan a set/2026 (pagos até 11/09)."""
    ex=[]
    def add(d,t,c,cli,caso,desc,v,f="Pix",p="Sim"):
        assert not (p=="Sim" and d>SEXTA), (d,desc)
        ex.append((d,t,c,cli,caso,desc,v,f,p))
    fim_mes=date(2026,9,30)
    for c in CASOS:
        for p in c["parcelas"]:
            desc={"Entrada":"Honorários · entrada","Parcela":f"Honorários · parcela {p['n']}","Fatura de horas":f"Fatura de horas · {p['n']}","Honorários de êxito":"Honorários de êxito (fim do caso)"}[p["descricao"]]
            if p["descricao"]=="Parcela" and c["parcelas"][0]["descricao"]=="Entrada": desc=f"Honorários · parcela {p['n']-1}"
            if p["pago"]:
                if p["pagamento"].year==ANO: add(p["pagamento"],"Entrada",categoria_entrada(c,p),c["cliente"],c["numero"],desc,p["valor"],"Boleto" if p["descricao"]=="Fatura de horas" else "Pix")
            elif p["vencimento"]<=fim_mes:   # já faturada e não paga: vencida ou vence até o fim do mês
                add(p["vencimento"],"Entrada",categoria_entrada(c,p),c["cliente"],c["numero"],desc+(" (vencida)" if p["vencimento"]<HOJE else " (a receber)"),p["valor"],"Boleto","Não")
        for d,desc,v in c["custas"]: add(d,"Saída","Custas e despesas de processo",c["cliente"],c["numero"],desc,v,"Boleto")
    # reembolsos de custas (o cliente devolve o que o escritório adiantou)
    for ch,d,v,desc in (("E02",D(2026,3,9),780,"Reembolso das custas periciais"),("A25",D(2026,7,15),540,"Reembolso das custas de recurso"),("A11",D(2026,8,12),310,"Reembolso das custas de recurso")):
        add(d,"Entrada","Reembolso de custas",CASO[ch]["cliente"],CASO[ch]["numero"],desc,v,"Transferência")
    for m in range(1,10):
        for c,v in CUSTOS_FIXOS:
            d=date(2026,m,DIA_FIXO[c]); pago="Sim" if d<=SEXTA else "Não"
            add(d,"Saída",c,"","",{"Contador":"Honorários do contador","Estagiária (bolsa)":"Bolsa da estagiária · Júlia Prado","Aluguel e condomínio":"Aluguel e condomínio da sala"}.get(c,c),v,"Boleto" if c in("Aluguel e condomínio","Contador","Telefone e internet") else "Cartão",pago)
        for n_,v in PRO_LABORE: add(date(2026,m,28),"Saída","Pró-labore dos sócios","","",f"Pró-labore · {n_}",v,"Transferência","Sim" if m<9 else "Não")
    for m,d,v in ((2,17,240),(5,12,310),(8,19,180)): add(date(2026,m,d),"Saída","Deslocamento e viagens","","","Combustível e estacionamento (audiências)",v,"Cartão")
    # imposto do exemplo: guia paga dia 20 sobre as entradas de honorários e reembolsos do mês anterior (8 %); janeiro sobre dezembro/2025 (fictício)
    for m in range(1,10):
        base=base_imposto(ex,m-1) if m>1 else 20600
        add(date(2026,m,20),"Saída","Impostos e taxas","","","Guia de impostos do mês anterior (alíquota efetiva combinada com o contador)",round(base*ALIQ),"Boleto","Sim" if m<9 else "Não")
    # movimentos sócio × escritório (detalhados na 11)
    for m in (2,5,8): add(date(2026,m,6),"Saída","Outras saídas","","","Despesa pessoal · Marina Ferraz · plano de saúde particular (a acertar)",480,"Boleto")
    for m in (3,7): add(date(2026,m,11),"Saída","Outras saídas","","","Despesa pessoal · Rafael Lima · combustível particular (a acertar)",300,"Cartão")
    add(date(2026,4,14),"Entrada","Outras entradas","","","Devolução de despesa pessoal · Marina Ferraz",480,"Pix")
    add(date(2026,3,16),"Saída","Pró-labore dos sócios","","","Retirada extra · Rafael Lima · adiantamento para viagem",1500,"Transferência")
    add(date(2026,6,19),"Saída","Pró-labore dos sócios","","","Retirada extra · Marina Ferraz · reforma em casa",2000,"Transferência")
    # distribuição de lucro: 50 % do resultado do trimestre fechado (após pró-labore fixo), meio a meio, paga no dia 10 do mês seguinte
    for q,(m_ini,m_pag) in enumerate(((1,4),(4,7)),start=1):
        lucro=sum(v if t=="Entrada" else -v for d,t,c,cli,caso,desc,v,f,p in ex if p=="Sim" and m_ini<=d.month<=m_ini+2 and not desc.startswith(("Retirada extra","Despesa pessoal","Devolução","Distribuição")))
        if lucro>=LUCRO_MINIMO:
            total=round(lucro*DISTRIB); cotas=[total//2,total-total//2]   # soma exata (a 11 compara com o distribuível)
            for (n_,_),cota in zip(PRO_LABORE,cotas): add(date(2026,m_pag,10),"Saída","Pró-labore dos sócios","","",f"Distribuição de lucro · {q}º trimestre · {n_}",cota,"Transferência")
    ex.sort(key=lambda x:(x[0],x[1],x[2]))
    return ex
def base_imposto(ex,m):
    """Entradas pagas do mês m sem 'Outras entradas' (devolução de sócio não paga imposto)."""
    return sum(v for d,t,c,cli,caso,desc,v,f,p in ex if t=="Entrada" and p=="Sim" and d.month==m and d.year==ANO and c!="Outras entradas")
LANCAMENTOS=lancamentos()

def totais_mensais(ex=None):
    """Mês -> dict com o que está Pago? = Sim (jan..dez/2026): ent, devol, sai, pessoal, pro, extra, distrib, fixo, imp,
    por_cat (categoria -> valor), ent_sem_devol, saldo (acumulado ao fim do mês)."""
    ex=ex or LANCAMENTOS; out={}; saldo=SALDO_INICIAL
    fixos={c for c,_ in CUSTOS_FIXOS}
    for m in range(1,13):
        L_=[x for x in ex if x[0].month==m and x[0].year==ANO and x[8]=="Sim"]
        pro=sum(x[6] for x in L_ if x[5].startswith("Pró-labore"))
        por_cat={}
        for x in L_: por_cat[x[2]]=por_cat.get(x[2],0)+x[6]
        ent=sum(x[6] for x in L_ if x[1]=="Entrada"); sai_tot=sum(x[6] for x in L_ if x[1]=="Saída"); saldo+=ent-sai_tot
        out[m]=dict(ent=ent,devol=sum(x[6] for x in L_ if x[5].startswith("Devolução")),ent_sem_devol=ent-sum(x[6] for x in L_ if x[2]=="Outras entradas"),
                    sai_total=sai_tot,sai=sum(x[6] for x in L_ if x[1]=="Saída" and x[2]!="Pró-labore dos sócios"),pessoal=sum(x[6] for x in L_ if x[5].startswith("Despesa pessoal")),
                    pro=pro,extra=sum(x[6] for x in L_ if x[5].startswith("Retirada extra")),distrib=sum(x[6] for x in L_ if x[5].startswith("Distribuição")),
                    fixo=sum(x[6] for x in L_ if x[2] in fixos)+pro,imp=sum(x[6] for x in L_ if x[2]=="Impostos e taxas"),por_cat=por_cat,saldo=saldo)
    return out
TOTAIS=totais_mensais()
def a_pagar(): return sum(v for d,t,c,cli,caso,desc,v,f,p in LANCAMENTOS if t=="Saída" and p=="Não")
def a_receber_caixa(): return sum(v for d,t,c,cli,caso,desc,v,f,p in LANCAMENTOS if t=="Entrada" and p=="Não")

# ---------------------------------------------------------------------------------------------------------------
# HORAS (16): lançamentos de 01/07 a 11/09/2026. Horas gastas do caso = horas antes de julho + lançadas aqui.
# Casos por hora: a fatura do dia 10 cobra as horas faturáveis do mês anterior (valor = horas x R$ 150).
# ---------------------------------------------------------------------------------------------------------------
ATIVIDADES=["Reunião com cliente","Audiência","Elaboração de documento","Pesquisa e estudo do caso","Análise de documentos","Atendimento por telefone ou WhatsApp",
            "Diligência externa","Deslocamento","Administrativo do caso","Gestão do escritório","Captação e propostas"]
INTERNOS=[("Gestão do escritório","Escritório (sem cliente)"),("Captação e propostas","Escritório (sem cliente)")]
def _horas():
    rng=random.Random(16); J1=date(2026,7,1); rows=[]; antes={}
    def dia_util(a,b):
        while True:
            d=a+timedelta(days=rng.randint(0,max(0,(b-a).days)))
            if d.weekday()<5: return d
    for c in CASOS:
        ab=c["abertura"]; fim=SEXTA if c["fase"]!="Encerrado" else c["encerramento"]
        ini=max(J1,ab); alvo=0
        if fim>=ini: alvo=round(c["horas_gastas"]*min(1,((fim-ini).days+1)/max(1,(fim-ab).days+1))*(0.9 if ab<J1 else 1.0)*2)/2
        if c["tipo_hon"]=="Hora":
            # meses fechados: fatura do dia 10 do mês seguinte = horas faturáveis do mês / 150; setembro: até dia 11
            alvo_mes={}
            for p in c["parcelas"]:
                v=p["vencimento"]; mprev=(v.month-1) or 12
                if v.year==ANO and mprev in (7,8): alvo_mes[mprev]=p["valor"]/VALOR_HORA_COBRADA
            alvo_mes[9]=round(alvo-sum(alvo_mes.values()))
            for mes,h in alvo_mes.items():
                soma=0; a=date(2026,mes,1); b=min(SEXTA,date(2026,mes+1,1)-timedelta(days=1))
                while soma<h:
                    hrs=min(rng.choice([1,1.5,2,2.5,3]),h-soma)
                    rows.append((dia_util(a,b),c["responsavel"],c["numero"],rng.choice(["Elaboração de documento","Análise de documentos","Reunião com cliente","Pesquisa e estudo do caso"]),hrs,"Sim")); soma+=hrs
            antes[c["numero"]]=c["horas_gastas"]-sum(r[4] for r in rows if r[2]==c["numero"])
        else:
            soma=0
            while soma<alvo:
                hrs=min(rng.choice([1.5,2,2.5,3,3,3.5,4]),alvo-soma)
                if c["responsavel"]==MAR: pessoa=rng.choices([MAR,RAF,JUL],[55,15,30])[0]
                else: pessoa=rng.choices([RAF,JUL],[75,25])[0]
                if c["fase"]=="Consultivo": atv=rng.choice(["Reunião com cliente","Análise de documentos","Elaboração de documento","Pesquisa e estudo do caso"])
                else: atv=rng.choice(ATIVIDADES[:9])
                fat="Não" if atv in ("Deslocamento","Administrativo do caso") and rng.random()<0.7 else "Sim"
                rows.append((dia_util(ini,fim),pessoa,c["numero"],atv,hrs,fat)); soma+=hrs
            antes[c["numero"]]=c["horas_gastas"]-soma
        assert antes[c["numero"]]>=0,(c["chave"],antes[c["numero"]])
    d=J1; semana=0
    while d<=SEXTA:
        if d.weekday()==0:
            for pessoa in (MAR,RAF,JUL):
                rows.append((dia_util(d,min(SEXTA,d+timedelta(days=4))),pessoa,"Gestão do escritório","Gestão do escritório",rng.choice([1,1.5,2,2.5]),"Não"))
                if pessoa!=JUL and semana%2==0:
                    rows.append((dia_util(d,min(SEXTA,d+timedelta(days=4))),pessoa,"Captação e propostas","Captação e propostas",rng.choice([1,1.5,2]),"Não"))
            semana+=1
        d+=timedelta(days=1)
    rows.sort(key=lambda x:(x[0],x[1],x[2]))
    for r in rows: assert r[0]<=SEXTA
    return rows,antes
HORAS,HORAS_ANTES=_horas()
def custo_hora_pessoa(nome):
    """Custo-hora de cada pessoa como a 16 calcula: custo mensal ÷ meta de horas + rateio dos custos fixos sem equipe."""
    custo,horas=next((c,h) for n,_,c,h in PESSOAS if n==nome)
    return custo/horas+CUSTOS_SEM_EQUIPE/HORAS_FATURAVEIS_MES
def horas_mes(m,ate=SEXTA):
    """(horas, faturáveis) lançadas no mês m até a data."""
    L_=[r for r in HORAS if r[0].month==m and r[0]<=ate]
    return sum(r[4] for r in L_),sum(r[4] for r in L_ if r[5]=="Sim")
def horas_pessoa_mes(nome,m,ate=SEXTA):
    L_=[r for r in HORAS if r[0].month==m and r[0]<=ate and r[1]==nome]
    return sum(r[4] for r in L_),sum(r[4] for r in L_ if r[5]=="Sim")
def custo_horas_caso(c,ate=SEXTA):
    return HORAS_ANTES[c["numero"]]*CUSTO_HORA+sum(r[4]*custo_hora_pessoa(r[1]) for r in HORAS if r[2]==c["numero"] and r[0]<=ate)
def casos_consomem_mais(ate=SEXTA):
    return sum(1 for c in CASOS if custo_horas_caso(c,ate)>c["valor_contratado"])

# ---------------------------------------------------------------------------------------------------------------
# ESTADO DA CARTEIRA em uma data (para Histórico da 17, indicadores da 20 e semanas da 19).
# ---------------------------------------------------------------------------------------------------------------
def estado(ref):
    """Carteira, parcelas e propostas como estavam na data ref (usa as mesmas parcelas; vencimentos futuros valem como estão)."""
    abertos=[c for c in CASOS if c["abertura"]<=ref]
    ativos=[c for c in abertos if c["encerramento"] is None or c["encerramento"]>ref]
    contratado=sum(c["valor_contratado"] for c in abertos)
    pago=0; vencido=0; em_aberto=0; nvenc=0
    for c in abertos:
        for p in c["parcelas"]:
            s=status_parcela(p,ref)
            if s=="Paga": pago+=p["valor"]
            elif s=="Vencida": vencido+=p["valor"]; nvenc+=1; em_aberto+=p["valor"]
            else: em_aberto+=p["valor"]
    inad=vencido/(pago+vencido) if pago+vencido else 0
    def dt(x): return HOJE+timedelta(days=x) if isinstance(x,int) else x
    props=[p for p in PROPOSTAS if p["entrada"]<=ref]
    abertas=[p for p in props if p["fechamento"] is None or p["fechamento"]>ref]
    return dict(casos_ativos=len(ativos),a_receber=contratado-pago,vencido=vencido,parcelas_vencidas=nvenc,pago=pago,inadimplencia=inad,em_aberto=em_aberto,
                propostas_n=len(abertas),propostas_valor=sum(p["valor"] for p in abertas),
                fechadas_tri=sum(1 for p in props if p["fechamento"] is not None and p["etapa"]=="Fechada" and date(2026,7,1)<=p["fechamento"]<=ref),
                fechado_tri=sum(p["valor"] for p in props if p["fechamento"] is not None and p["etapa"]=="Fechada" and date(2026,7,1)<=p["fechamento"]<=ref),
                fechado_mes=sum(p["valor"] for p in props if p["fechamento"] is not None and p["etapa"]=="Fechada" and p["fechamento"].month==ref.month and p["fechamento"].year==ref.year))
def fim_mes(m): return date(2026,m+1,1)-timedelta(days=1) if m<12 else date(2026,12,31)
def historico():
    """Mês -> dict do Histórico da 17 (jan..set; setembro = estado em 11/09, mês em andamento)."""
    out={}
    for m in range(1,10):
        ref=min(fim_mes(m),SEXTA); e=estado(ref); t=TOTAIS[m]
        h,f=horas_mes(m) if m>=7 else (None,None)
        out[m]=dict(entrou=t["ent"],saiu=t["sai_total"],horas=h,faturaveis=f,a_receber=e["a_receber"],vencido=e["vencido"],inadimplencia=e["inadimplencia"],
                    propostas_n=e["propostas_n"],propostas_valor=e["propostas_valor"],casos_ativos=e["casos_ativos"],fechado_mes=e["fechado_mes"])
    return out
HISTORICO=historico()

# ---------------------------------------------------------------------------------------------------------------
# DRE (18): receita por categoria do caixa, custos fixos, despesas de casos, pró-labore, impostos provisionados (8 %).
# ---------------------------------------------------------------------------------------------------------------
def dre(m):
    pc=TOTAIS[m]["por_cat"]
    rec={c:pc.get(c,0) for c in CAT_ENTRADA}
    fixos={c:pc.get(c,0) for c,_ in CUSTOS_FIXOS}
    var={c:pc.get(c,0) for c in ("Custas e despesas de processo","Deslocamento e viagens")}
    pro={n:v for n,v in PRO_LABORE}
    receita=sum(rec.values()); imp=round(receita*ALIQ)
    saidas=sum(fixos.values())+sum(var.values())+sum(pro.values())+imp
    return dict(receita=rec,fixos=fixos,variaveis=var,pro_labore=pro,receita_total=receita,impostos=imp,saidas=saidas,resultado=receita-saidas,margem=(receita-saidas)/receita if receita else 0)

# ---------------------------------------------------------------------------------------------------------------
# PROVISÃO (10): 13º dos sócios e férias/recesso da estagiária, como a planilha 10 calcula.
# ---------------------------------------------------------------------------------------------------------------
def provisao_10():
    """Mês -> dict(entradas, imp, dec13, ferias, separar, usado, saldo) até setembro."""
    dec13=sum(v/12 for n,p,v,_ in PESSOAS if p.startswith("Sóci")); ferias=sum(v*(1+1/3)/12 for n,p,v,_ in PESSOAS if not p.startswith("Sóci"))
    out={}; sep=0; usado=0
    for m in range(1,10):
        ent=TOTAIS[m]["ent_sem_devol"]; imp=ent*ALIQ; sep+=imp+dec13+ferias; usado+=TOTAIS[m]["imp"]
        out[m]=dict(entradas=ent,imp=imp,dec13=dec13,ferias=ferias,separar=imp+dec13+ferias,usado=TOTAIS[m]["imp"],saldo=sep-usado)
    return out

# ---------------------------------------------------------------------------------------------------------------
# RESERVA E METAS (12 e 19)
# ---------------------------------------------------------------------------------------------------------------
RESERVA_GUARDADA=12000; RESERVA_INICIO_TRI=6000; APORTE_RESERVA=3000
PROVISAO_SEPARADA=9400          # o que já está na conta de provisão (12 e 19)
META_FECHADO_TRI=60000          # meta de honorários fechados no trimestre (15 e 19)
SEXTAS_TRI=[date(2026,7,3)+timedelta(days=7*i) for i in range(11)]   # S1..S11 do 3º trimestre (até 11/09)
def reserva_em(ref):
    """Reserva guardada na data: aporte de R$ 3.000 no fechamento de cada mês (julho e agosto)."""
    return RESERVA_INICIO_TRI+APORTE_RESERVA*sum(1 for m in (7,8) if ref>=fim_mes(m))

if __name__=="__main__":
    c=CASOS; print(len(c),"casos;",sum(x["valor_contratado"] for x in c),"contratado;",sum(x["recebido"] for x in c),"recebido;",
                   sum(1 for x in c if x["fase"]!="Encerrado"),"ativos")
    print("prazos:",resumo_prazos())
    for m,t in TOTAIS.items():
        if t["ent"] or t["sai_total"]: print(f"{m:2d} entrou {t['ent']:8.0f} saiu {t['sai_total']:8.0f} sobrou {t['ent']-t['sai_total']:8.0f} saldo {t['saldo']:8.0f} fixo {t['fixo']} imp {t['imp']}")
    e=estado(HOJE); print("hoje:",e)
    print("a pagar",a_pagar(),"a receber (caixa)",a_receber_caixa())
    print("horas jul/ago/set:",horas_mes(7),horas_mes(8),horas_mes(9),"| lançamentos:",len(HORAS))
    for m in (7,8): print("DRE",m,dre(m)["receita_total"],dre(m)["saidas"],dre(m)["resultado"],round(dre(m)["margem"]*100,1))
    print("consomem mais:",casos_consomem_mais())
    print("propostas 07:",[(p["numero"],p["cliente"],p["valor"]) for p in propostas_registro_07()])
    print("hist:",{m:(h["a_receber"],h["vencido"],round(h["inadimplencia"]*100,1),h["casos_ativos"],h["propostas_n"]) for m,h in HISTORICO.items()})

# ---------------------------------------------------------------------------------------------------------------
# METAS DO TRIMESTRE (19): 3 objetivos, resultados-chave que existem nos dados; série semanal S1..S11 (sextas do 3º tri).
# ---------------------------------------------------------------------------------------------------------------
def semaforo_16(c,ate=SEXTA):
    """Situação do caso como a planilha 16 calcula (todo o período)."""
    if c["tipo_hon"]=="Interno": return "Interno"
    gastas=HORAS_ANTES[c["numero"]]+sum(r[4] for r in HORAS if r[2]==c["numero"] and r[0]<=ate)
    if gastas==0: return "Sem horas"
    custo=custo_horas_caso(c,ate); contr=c["valor_contratado"]
    if custo>contr: return "Consome mais do que paga"
    pct=gastas/c["horas_estimadas"] if c["horas_estimadas"] else None
    if pct is not None and pct>1: return "Estourou as horas"
    if contr and (contr-custo)/contr<0.2: return "Margem baixa"
    if pct is not None and pct>0.85: return "Perto do limite"
    return "Saudável"
def casos_alerta_16(ate=SEXTA):
    """Casos com alerta de horas na 16: consome mais do que paga, estourou as horas ou margem baixa."""
    return sum(1 for c in CASOS if semaforo_16(c,ate) in ("Consome mais do que paga","Estourou as horas","Margem baixa"))   # como a lista "Casos para olhar primeiro" da 16 (todo o período, inclui encerrados)
def pct_faturavel_mes_ate(ref):
    h,f=horas_mes(ref.month,ref); return round(f/h*100,1) if h else 0
def faturaveis_tri(ref):
    """Horas faturáveis lançadas de 01/07 até a data (3º trimestre)."""
    return sum(r[4] for r in HORAS if r[5]=="Sim" and date(2026,7,1)<=r[0]<=ref)
def propostas_paradas(ref=HOJE,limite=14):
    """Propostas abertas paradas há mais de N dias (última movimentação), como a 15 calcula na data de referência."""
    n=0
    for p in PROPOSTAS:
        if p["fechamento"] is not None or p["entrada"]>ref: continue
        ult=p["ultima_mov"]; ult=HOJE+timedelta(days=ult) if isinstance(ult,int) else ult
        if ult is None: ult=p["entrada"]
        prev=p["fech_previsto"]; prev=HOJE+timedelta(days=prev) if isinstance(prev,int) else prev
        if prev is not None and prev<ref: continue      # na 15, "Previsão vencida" tem precedência sobre "Parada"
        if (ref-ult).days>limite: n+=1
    return n
def metas_19():
    """[(objetivo, [(resultado-chave, dono, unidade, partida, meta, atual, sentido, observação, série S1..S11)])]"""
    ini=date(2026,6,30); S=SEXTAS_TRI
    e0=estado(ini); e1=estado(HOJE)
    inad=lambda r: round(estado(r)["inadimplencia"]*100,1)
    prov=provisao_10()
    return [
     ("Caixa mais previsível",[
       ("Inadimplência: vencido ÷ (pago + vencido) (%)",RAF,"%",inad(ini),3.0,inad(HOJE),"Menor é melhor","Painel da planilha 14. Piorou com Bistrô 42, Agência Prisma e Patrícia Gomes: cobrar primeiro (régua).",[inad(r) for r in S]),
       ("Reserva guardada em conta separada (R$)",MAR,"R$",RESERVA_INICIO_TRI,CUSTO_TOTAL_MES,RESERVA_GUARDADA,"Maior é melhor","Meta = 1 mês de custo fixo com pró-labore (planilha 12). Aporte de R$ 3.000 no fechamento de cada mês.",[reserva_em(r) for r in S]),
       ("Conta de provisão de impostos, 13º e férias (R$)",MAR,"R$",6200,round(prov[9]["saldo"]),PROVISAO_SEPARADA,"Maior é melhor","Meta = saldo provisionado de setembro na planilha 10; atual = o que já está na conta separada (planilha 12).",
        [6200,6200,6200,6200,7800,7800,7800,7800,7800,9400,9400])]),
     ("Horas que viram honorário",[
       ("Horas faturáveis no mês (%)",RAF,"%",pct_faturavel_mes_ate(fim_mes(7)),80.0,pct_faturavel_mes_ate(SEXTA),"Maior é melhor","Painel da planilha 16 (mês do painel). Partida = julho fechado; atual = setembro até 11/09.",[pct_faturavel_mes_ate(r) for r in S]),
       ("Horas faturáveis lançadas no trimestre (h)",MAR,"h",0,700,faturaveis_tri(SEXTA),"Maior é melhor","Soma das horas faturáveis de julho, agosto e setembro na planilha 16 (Painel, trocando o mês em Config). Meta = 2,5 meses × 280 h.",[faturaveis_tri(r) for r in S])]),
     ("Fechar mais propostas",[
       ("Propostas fechadas no trimestre",MAR,"propostas",0,8,e1["fechadas_tri"],"Maior é melhor","Painel da planilha 15 (funil). Fechadas de julho a setembro.",[estado(r)["fechadas_tri"] for r in S]),
       ("Honorários fechados no trimestre (R$)",MAR,"R$",0,META_FECHADO_TRI,e1["fechado_tri"],"Maior é melhor","KPI \"Fechado no trimestre\" da planilha 15; meta = Config da 15.",[estado(r)["fechado_tri"] for r in S]),
       ("Propostas paradas há mais de 14 dias",RAF,"propostas",2,0,propostas_paradas(),"Menor é melhor","Situação \"Parada\" na planilha 15. Retomar contato na sexta.",[2,2,1,1,2,1,1,2,2,3,propostas_paradas()])])]
if __name__=="__main__":
    for obj,krs in metas_19():
        print(obj)
        for kr in krs: print("  ",kr[0][:45],kr[3],kr[4],kr[5],kr[8])
    print("semaforos 16:",{c["chave"]:semaforo_16(c) for c in CASOS if c["fase"]!="Encerrado"})
