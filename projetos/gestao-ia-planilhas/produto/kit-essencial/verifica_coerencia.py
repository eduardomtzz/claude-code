#!/usr/bin/env python3
"""Verifica a coerência das três planilhas do Kit IA no Trabalho Essencial.

Diferente dos kits Advogados e Médicos, aqui não há um exemplo único atravessando os
arquivos: a 01 e a 02 usam a Prisma Comunicação (empresa), a 03 usa a Rafa Design
(pessoa), de propósito — a 03 serve também para dinheiro pessoal. Então o que se
verifica é a coerência INTERNA de cada arquivo: todo número do painel é recalculado
em Python a partir das linhas digitadas e comparado com o que a fórmula devolveu.

Foi assim que apareceram os dois defeitos de 18/09: o total de "Para onde foi o
dinheiro" não batia com o KPI "Saiu no mês" (R$ 362 de contas não pagas) e o
"Acumulado" da 02 somava ticket médio.

Uso: python3 verifica_coerencia.py <pasta com as cópias recalculadas>
     (nunca recalcule os originais entregues)
"""
import sys, pathlib, datetime
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from vc import Verificador, abrir, num, dt, txt, linhas

MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


def checa_01(pasta, V):
    """01 Semana Organizada: aba Hoje contra as linhas da aba Tarefas."""
    wb = abrir(pasta, "01")
    cfg, t, h = wb["Config"], wb["Tarefas"], wb["Hoje"]
    HOJE = dt(cfg["B4"].value)
    CAP = num(cfg["B6"].value)
    T = [dict(tarefa=txt(a), proj=txt(b), resp=txt(c), prazo=dt(d), imp=num(e), urg=num(f),
              horas=num(g), status=txt(i), prio=txt(j), dias=k, sit=txt(l), ordem=num(m))
         for a, b, c, d, e, f, g, i, j, k, l, m in linhas(t, 4, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])]
    V.check("01 Tarefas tem 20 exemplos", len(T), 20)

    # situação e prioridade, linha por linha
    for x in T:
        if x["status"] in ("Feito", "Cancelado"):
            esperado = x["status"]
        elif x["prazo"] is None:
            esperado = "Sem prazo"
        else:
            d = (x["prazo"] - HOJE).days
            esperado = "Atrasada" if d < 0 else "Hoje" if d == 0 else "Esta semana" if d <= 6 else "Depois"
        V.check(f"01 situação de {x['tarefa'][:28]!r}", x["sit"], esperado)
        p = x["imp"] * x["urg"]
        V.check(f"01 prioridade de {x['tarefa'][:28]!r}", x["prio"],
                "Alta" if p >= 6 else "Média" if p >= 3 else "Baixa")

    # KPIs
    abertas = [x for x in T if x["status"] not in ("Feito", "Cancelado")]
    V.check("01 Hoje Atrasadas", h["A5"].value, sum(1 for x in T if x["sit"] == "Atrasada"))
    V.check("01 Hoje Para hoje", h["C5"].value, sum(1 for x in T if x["sit"] == "Hoje"))
    V.check("01 Hoje Esta semana", h["E5"].value, sum(1 for x in T if x["sit"] == "Esta semana"))
    V.check("01 Hoje Abertas no total", h["G5"].value, len(abertas))
    V.check("01 Hoje Feitas", h["I5"].value, sum(1 for x in T if x["status"] == "Feito"))

    # "O que fazer primeiro": as 12 de maior ordem, na ordem
    fila = sorted([x for x in T if x["ordem"] > 0], key=lambda x: -x["ordem"])[:12]
    for k in range(12):
        r = 10 + k
        nome = txt(h.cell(row=r, column=2).value)
        V.check(f"01 fila #{k+1}", nome, fila[k]["tarefa"] if k < len(fila) else "")
        if k < len(fila):
            V.check(f"01 fila #{k+1} situação", txt(h.cell(row=r, column=4).value), fila[k]["sit"])
            V.check(f"01 fila #{k+1} horas", h.cell(row=r, column=7).value, fila[k]["horas"], tol=0.001)
    V.check("01 fila só tem tarefa aberta com prazo",
            all(x["sit"] in ("Atrasada", "Hoje", "Esta semana") for x in fila), True)

    # carga dos próximos 7 dias
    for i in range(7):
        r = 25 + i
        d = dt(h.cell(row=r, column=2).value)
        V.check(f"01 carga dia {i} é hoje+{i}", d, HOJE + datetime.timedelta(days=i))
        dia = [x for x in abertas if x["prazo"] == d]
        V.check(f"01 carga {d} tarefas", h.cell(row=r, column=3).value, len(dia))
        hrs = sum(x["horas"] for x in dia)
        V.check(f"01 carga {d} horas", h.cell(row=r, column=4).value, hrs, tol=0.001)
        V.check(f"01 carga {d} % da capacidade", num(h.cell(row=r, column=5).value),
                hrs / CAP if CAP else 0, tol=1e-9)

    # por responsável
    for i in range(8):
        r = 36 + i
        pessoa = txt(h.cell(row=r, column=1).value)
        if not pessoa: continue
        meus = [x for x in abertas if x["resp"] == pessoa]
        V.check(f"01 {pessoa} abertas", h.cell(row=r, column=3).value, len(meus))
        V.check(f"01 {pessoa} atrasadas", h.cell(row=r, column=4).value,
                sum(1 for x in T if x["resp"] == pessoa and x["sit"] == "Atrasada"))
        V.check(f"01 {pessoa} para hoje", h.cell(row=r, column=5).value,
                sum(1 for x in T if x["resp"] == pessoa and x["sit"] == "Hoje"))
        V.check(f"01 {pessoa} horas abertas", h.cell(row=r, column=6).value,
                sum(x["horas"] for x in meus), tol=0.001)


def checa_02(pasta, V):
    """02 Relatório Mensal: Painel e Resumo contra a aba Indicadores."""
    wb = abrir(pasta, "02")
    cfg, ind, p, rs = wb["Config"], wb["Indicadores"], wb["Painel"], wb["Resumo"]
    M = int(num(cfg["B7"].value))
    V.check("02 número do mês == posição do nome do mês", M, MESES.index(txt(cfg["B6"].value)) + 1)
    V.check("02 mês anterior", txt(cfg["B8"].value), MESES[M - 2] if M > 1 else "")

    I = []
    for i in range(12):
        r = 5 + i
        nome = txt(ind.cell(row=r, column=1).value)
        if not nome: continue
        I.append(dict(r=r, nome=nome, un=txt(ind.cell(row=r, column=2).value),
                      casas=num(ind.cell(row=r, column=3).value),
                      meta=num(ind.cell(row=r, column=4).value),
                      maior=txt(ind.cell(row=r, column=5).value),
                      vals=[ind.cell(row=r, column=6 + j).value for j in range(12)],
                      acum=ind.cell(row=r, column=18).value,
                      media=ind.cell(row=r, column=19).value,
                      como=txt(ind.cell(row=r, column=20).value)))
    V.check("02 tem 12 indicadores", len(I), 12)

    for x in I:
        cheios = [num(v) for v in x["vals"] if v not in (None, "")]
        # Acumulado: "Soma" empilha, "Média" faz média. Somar razão não significa nada —
        # doze meses de ticket médio somados não são o ticket do ano.
        V.check(f"02 como acumular {x['nome']!r} é Soma ou Média", x["como"] in ("Soma", "Média"), True)
        esperado = sum(cheios) if x["como"] == "Soma" else (sum(cheios) / len(cheios) if cheios else "")
        V.check(f"02 acumulado {x['nome']!r}", num(x["acum"]), num(esperado), tol=0.01)
        V.check(f"02 média {x['nome']!r}", num(x["media"]),
                sum(cheios) / len(cheios) if cheios else 0, tol=0.01)
        if x["un"] in ("%", "pts"):
            V.check(f"02 razão {x['nome']!r} não é somada", x["como"], "Média")

        r = x["r"]
        mes = num(x["vals"][M - 1]); ant = num(x["vals"][M - 2]) if M > 1 else 0
        V.check(f"02 Painel mês {x['nome']!r}", num(p.cell(row=r, column=2).value), mes, tol=0.001)
        V.check(f"02 Painel mês anterior {x['nome']!r}", num(p.cell(row=r, column=3).value), ant, tol=0.001)
        V.check(f"02 Painel variação {x['nome']!r}", num(p.cell(row=r, column=4).value),
                (mes - ant) / abs(ant) if ant else 0, tol=1e-9)
        V.check(f"02 Painel meta {x['nome']!r}", num(p.cell(row=r, column=5).value), x["meta"], tol=0.001)
        V.check(f"02 Painel vs. meta {x['nome']!r}", num(p.cell(row=r, column=6).value),
                (mes - x["meta"]) / abs(x["meta"]) if x["meta"] else 0, tol=1e-9)
        sit = ("No alvo" if (mes <= x["meta"] if x["maior"] == "Não" else mes >= x["meta"])
               else ("Acima da meta" if x["maior"] == "Não" else "Abaixo da meta"))
        V.check(f"02 Painel situação {x['nome']!r}", txt(p.cell(row=r, column=7).value), sit)
        V.check(f"02 Painel acumulado {x['nome']!r}", num(p.cell(row=r, column=8).value),
                num(x["acum"]), tol=0.01)
        V.check(f"02 Painel unidade {x['nome']!r}", txt(p.cell(row=r, column=9).value), x["un"])

    # Resumo: uma frase por indicador, e o bloco único contém todas
    bloco = txt(rs.cell(row=6 + 12 + 1 + 6 + 1, column=1).value) or ""
    for i, x in enumerate(I):
        frase = txt(rs.cell(row=6 + i, column=1).value)
        V.check(f"02 Resumo cita {x['nome']!r}", x["nome"] in frase, True)
        V.check(f"02 bloco único contém a frase de {x['nome']!r}", frase and frase in bloco, True)
    no_alvo = sum(1 for x in I
                  if (num(x["vals"][M - 1]) <= x["meta"] if x["maior"] == "Não"
                      else num(x["vals"][M - 1]) >= x["meta"]))
    V.check("02 Resumo 'indicadores no alvo' == Painel",
            f"no alvo: {no_alvo} de {len(I)}" in bloco.lower(), True)
    # o indicador do gráfico tem de existir na lista
    V.check("02 indicador do gráfico existe em Indicadores",
            txt(p.cell(row=18, column=2).value) in [x["nome"] for x in I], True)


def checa_03(pasta, V):
    """03 Ganhos e Gastos: painel de caixa contra as linhas de Lançamentos."""
    wb = abrir(pasta, "03")
    cfg, lan, p = wb["Config"], wb["Lançamentos"], wb["Painel"]
    M = int(num(cfg["B7"].value)); Y = int(num(cfg["B5"].value))
    SALDO0 = num(cfg["B8"].value); META = num(cfg["B9"].value); RES = txt(cfg["B10"].value)
    V.check("03 número do mês == posição do nome do mês", M, MESES.index(txt(cfg["B6"].value)) + 1)

    L = [dict(data=dt(a), tipo=txt(b), cat=txt(c), desc=txt(d), valor=num(e),
              forma=txt(f), pago=txt(g), mes=num(i), ano=num(j))
         for a, b, c, d, e, f, g, h_, i, j in linhas(lan, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
    V.check("03 tem 46 lançamentos de exemplo", len(L), 46)
    for x in L:
        V.check(f"03 mês calculado de {x['desc'][:24]!r}", x["mes"], x["data"].month)
        V.check(f"03 ano calculado de {x['desc'][:24]!r}", x["ano"], x["data"].year)
        V.check(f"03 Pago? de {x['desc'][:24]!r} é Sim ou Não", x["pago"] in ("Sim", "Não"), True)

    # Regra do painel: só entra Pago? = Sim.
    def soma(tipo, mes=None, cat=None, ate=None, pago="Sim"):
        return sum(x["valor"] for x in L
                   if x["tipo"] == tipo
                   and (pago is None or x["pago"] == pago)
                   and (mes is None or (x["data"].month == mes and x["data"].year == Y))
                   and (cat is None or x["cat"] == cat)
                   and (ate is None or x["data"] <= ate))

    def primeiro(ano, mes):
        """DATE(ano;mês;1) como o Excel faz: mês 0 é dezembro do ano anterior, mês 13
        é janeiro do seguinte. Sem isso a conferência quebrava com o painel em janeiro."""
        return datetime.date(ano + (mes - 1) // 12, (mes - 1) % 12 + 1, 1)
    fim_mes = primeiro(Y, M + 1) - datetime.timedelta(days=1)
    entrou = soma("Receita", mes=M); saiu = soma("Despesa", mes=M)
    V.check("03 Entrou no mês", p["A5"].value, entrou)
    V.check("03 Saiu no mês", p["C5"].value, saiu)
    V.check("03 Sobrou", p["E5"].value, entrou - saiu)
    V.check("03 Saldo em caixa", p["G5"].value,
            SALDO0 + soma("Receita", ate=fim_mes) - soma("Despesa", ate=fim_mes))
    V.check("03 A receber (não recebido)", p["I5"].value, soma("Receita", pago="Não"))
    V.check("03 A pagar (não pago)", p["K5"].value, soma("Despesa", pago="Não"))

    # reserva
    ini = primeiro(Y, M - 2)
    desp3 = sum(x["valor"] for x in L if x["tipo"] == "Despesa" and x["pago"] == "Sim"
                and ini <= x["data"] <= fim_mes)
    res3 = sum(x["valor"] for x in L if x["tipo"] == "Despesa" and x["pago"] == "Sim"
               and x["cat"] == RES and ini <= x["data"] <= fim_mes)
    V.check("03 média de despesas de 3 meses (sem reserva)", p["C8"].value, (desp3 - res3) / 3, tol=0.01)
    guardado = soma("Despesa", cat=RES, ate=fim_mes)
    V.check("03 guardado na reserva (acumulado)", p["C9"].value, guardado)
    media = num(p["C8"].value)
    V.check("03 meses de reserva", num(p["C10"].value),
            (num(p["G5"].value) + guardado) / media if media else 0, tol=1e-6)
    V.check("03 meta de reserva == Config", p["C11"].value, META)
    m10 = num(p["C10"].value)
    V.check("03 situação da reserva", txt(p["C12"].value),
            "Meta de reserva atingida" if m10 >= META
            else "No caminho: metade da meta" if m10 >= META / 2
            else "Reserva baixa: priorize guardar")

    # "Para onde foi o dinheiro" (linhas 17-28, total na 29) e "De onde veio" (33-44)
    tot_d = tot_d_ant = 0
    mes_ant, ano_ant = (12, Y - 1) if M == 1 else (M - 1, Y)
    for i in range(12):
        r = 17 + i
        cat = txt(p.cell(row=r, column=1).value)
        if not cat: continue
        V.check(f"03 despesa {cat!r} no mês", p.cell(row=r, column=2).value, soma("Despesa", mes=M, cat=cat))
        ant = sum(x["valor"] for x in L if x["tipo"] == "Despesa" and x["pago"] == "Sim"
                  and x["cat"] == cat and x["data"].month == mes_ant and x["data"].year == ano_ant)
        V.check(f"03 despesa {cat!r} no mês anterior", p.cell(row=r, column=4).value, ant)
        pc = p.cell(row=r, column=3).value
        if pc not in (None, ""):
            V.check(f"03 % do total de {cat!r}", num(pc),
                    num(p.cell(row=r, column=2).value) / saiu if saiu else 0, tol=1e-9)
        tot_d += num(p.cell(row=r, column=2).value); tot_d_ant += ant
    # a razão de ser desta verificação: o KPI e este total discordavam em R$ 362
    V.check("03 Total de 'Para onde foi o dinheiro' == KPI Saiu no mês", p.cell(row=29, column=2).value, saiu)
    V.check("03 Total == soma das 12 categorias", p.cell(row=29, column=2).value, tot_d)
    V.check("03 Total do mês anterior == soma das categorias", p.cell(row=29, column=4).value, tot_d_ant)

    tot_r = 0
    for i in range(12):
        r = 33 + i
        cat = txt(p.cell(row=r, column=1).value)
        if not cat: continue
        V.check(f"03 receita {cat!r} no mês", p.cell(row=r, column=2).value, soma("Receita", mes=M, cat=cat))
        pc = p.cell(row=r, column=3).value
        if pc not in (None, ""):
            V.check(f"03 % do total de {cat!r}", num(pc),
                    num(p.cell(row=r, column=2).value) / entrou if entrou else 0, tol=1e-9)
        tot_r += num(p.cell(row=r, column=2).value)
    V.check("03 receitas por categoria == KPI Entrou no mês", tot_r, entrou)

    # "O ano, mês a mês" (linhas 48-59)
    for i in range(12):
        r = 48 + i
        V.check(f"03 ano: nome do mês {i+1}", txt(p.cell(row=r, column=1).value), MESES[i])
        e = soma("Receita", mes=i + 1); s = soma("Despesa", mes=i + 1)
        V.check(f"03 ano: entrou em {MESES[i]}", p.cell(row=r, column=2).value, e)
        V.check(f"03 ano: saiu em {MESES[i]}", p.cell(row=r, column=3).value, s)
        V.check(f"03 ano: sobrou em {MESES[i]}", p.cell(row=r, column=4).value, e - s)
        ate = primeiro(Y, i + 2) - datetime.timedelta(days=1)
        V.check(f"03 ano: saldo ao fim de {MESES[i]}", p.cell(row=r, column=5).value,
                SALDO0 + soma("Receita", ate=ate) - soma("Despesa", ate=ate))
    V.check("03 saldo de setembro no ano == KPI Saldo em caixa",
            p.cell(row=48 + M - 1, column=5).value, p["G5"].value)

    # categorias usadas nos lançamentos existem nas listas de Config
    cats_rec = {txt(cfg.cell(row=5 + i, column=4).value) for i in range(12)} - {""}
    cats_des = {txt(cfg.cell(row=5 + i, column=6).value) for i in range(12)} - {""}
    for x in L:
        V.check(f"03 categoria {x['cat']!r} está na lista de Config",
                x["cat"] in (cats_rec if x["tipo"] == "Receita" else cats_des), True)
    V.check("03 categoria de reserva está na lista de despesas", RES in cats_des, True)


if __name__ == "__main__":
    pasta = sys.argv[1] if len(sys.argv) > 1 else "."
    V = Verificador("Kit Essencial")
    checa_01(pasta, V); checa_02(pasta, V); checa_03(pasta, V)
    sys.exit(V.fim())
