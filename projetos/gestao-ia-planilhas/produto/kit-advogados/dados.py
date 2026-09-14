"""Escritório fictício compartilhado por todas as planilhas do Kit de Gestão para Advogados.
Ferraz & Lima Advocacia: 2 sócios, 1 estagiária, 18 clientes, 38 casos. Tudo inventado; números de processo
seguem o formato CNJ mas não existem. Datas de prazo são fórmulas relativas a HOJE() (não envelhecem);
datas de contrato/lançamento são fixas em 2026 (histórico). Painel de referência: 14/09/2026."""
import random
from datetime import date, timedelta
ESCRITORIO="Ferraz & Lima Advocacia"
HOJE=date(2026,9,14)  # referência dos exemplos históricos
PESSOAS=[  # nome, papel, custo mensal (pró-labore ou salário+encargos), horas faturáveis/mês
 ("Marina Ferraz","Sócia · cível e empresarial",6000,110),
 ("Rafael Lima","Sócio · trabalhista e previdenciário",6000,110),
 ("Júlia Prado","Estagiária",1400,60),
]
CUSTOS_FIXOS=[("Aluguel e condomínio",2800),("Contador",600),("Sistemas e assinaturas",450),("Telefone e internet",220),
 ("Anuidades OAB e cursos",250),("Marketing e site",400),("Estagiária (bolsa)",1400),("Material, correio e outros",380)]
AREAS=["Cível","Trabalhista","Previdenciário","Empresarial","Família"]
FASES=["Consultivo","Inicial","Instrução","Sentença","Recurso","Execução","Acordo","Encerrado"]
TIPOS_HON=["Fixo","Hora","Êxito","Misto"]
CLIENTES=[("Padaria do Sol Ltda","PJ","Empresarial"),("Ana Beatriz Moreira","PF","Trabalhista"),("Construtora Horizonte","PJ","Cível"),
 ("Carlos Eduardo Nunes","PF","Previdenciário"),("Loja Verde Comércio","PJ","Empresarial"),("Fernanda Castro","PF","Família"),
 ("Bistrô 42","PJ","Trabalhista"),("Roberto Almeida","PF","Cível"),("Clínica Bem-Estar","PJ","Empresarial"),("Marcos Vinícius Teles","PF","Previdenciário"),
 ("Transportadora Rota Sul","PJ","Trabalhista"),("Patrícia Gomes","PF","Família"),("Escola Aurora","PJ","Cível"),("José Antônio Ribeiro","PF","Previdenciário"),
 ("Oficina Mecânica Central","PJ","Trabalhista"),("Luciana Farias","PF","Cível"),("Agência Prisma","PJ","Empresarial"),("Helena Duarte","PF","Trabalhista")]
def _cnj(rng,ano):
    return f"{rng.randint(1000000,9999999):07d}-{rng.randint(10,99)}.{ano}.8.26.{rng.randint(1,700):04d}"
def casos():
    """38 casos: dict com numero, cliente, area, fase, responsavel, tipo_hon, valor_contratado, recebido, horas_estimadas,
    horas_gastas, abertura (date), proximo_prazo_dias (int relativo a hoje; None se consultivo/encerrado), descricao_prazo."""
    rng=random.Random(2026); out=[]
    prazos=["Contestação","Réplica","Audiência de instrução","Recurso ordinário","Manifestação sobre laudo","Alegações finais",
            "Cumprimento de sentença","Juntada de documentos","Audiência de conciliação","Embargos","Contrarrazões","Reunião com cliente"]
    for i in range(38):
        cli,tipo,area=CLIENTES[i%18]
        if i>=18: area=rng.choice(AREAS)
        fase=rng.choice(FASES) if i<34 else "Encerrado"
        resp="Marina Ferraz" if area in("Cível","Empresarial","Família") else "Rafael Lima"
        th=rng.choice(TIPOS_HON); base={"Cível":9000,"Trabalhista":6000,"Previdenciário":5000,"Empresarial":12000,"Família":7000}[area]
        valor=int(base*rng.uniform(0.6,1.8)/100)*100
        abertura=HOJE-timedelta(days=rng.randint(20,540))
        hest=int(valor/280)+rng.randint(5,25); hg=int(hest*rng.uniform(0.2,1.3)) if fase!="Consultivo" else rng.randint(2,12)
        if fase in("Encerrado","Acordo"): rec=valor
        elif th=="Êxito": rec=0  # êxito só recebe no fim
        else: rec=int(valor*rng.choice([0,0.3,0.5,0.6,1.0]))
        pd=None; desc=""
        if fase not in("Consultivo","Encerrado"):
            pd=rng.choice([-3,-1,0,1,2,3,4,6,8,10,13,15,18,22,27,35,42,60]); desc=rng.choice(prazos)
        out.append(dict(numero=_cnj(rng,abertura.year),cliente=cli,tipo_cliente=tipo,area=area,fase=fase,responsavel=resp,tipo_hon=th,
                        valor_contratado=valor,recebido=rec,horas_estimadas=hest,horas_gastas=hg,abertura=abertura,proximo_prazo_dias=pd,descricao_prazo=desc))
    return out
CASOS=casos()
def prazo_formula(dias):
    """Prazo do exemplo como fórmula relativa a hoje (não envelhece)."""
    return "=TODAY()" if dias==0 else f"=TODAY(){dias:+d}"
if __name__=="__main__":
    c=CASOS; print(len(c),"casos;", sum(x["valor_contratado"] for x in c),"contratado;", sum(x["recebido"] for x in c),"recebido")
    print(sum(1 for x in c if x["proximo_prazo_dias"] is not None and x["proximo_prazo_dias"]<0),"atrasados;",sum(1 for x in c if x["proximo_prazo_dias"] is not None and 0<=x["proximo_prazo_dias"]<=7),"esta semana")
    print(c[0])
