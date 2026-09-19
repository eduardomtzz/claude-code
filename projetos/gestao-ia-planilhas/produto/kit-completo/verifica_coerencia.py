#!/usr/bin/env python3
"""Verifica a coerência das dez planilhas do Kit IA no Trabalho Completo.

As 01, 02 e 03 são as mesmas do Essencial e usam o verificador dele. As 04 a 10
compartilham um exemplo só — a agência Prisma Comunicação — então aqui há dois tipos
de afirmação:

  · INTERNA: todo número do painel é recalculado em Python a partir das linhas
    digitadas e comparado com o que a fórmula devolveu.
  · ENTRE ARQUIVOS: a proposta ganha na 08 tem de ser o projeto da 09 pelo mesmo
    valor; o projeto da 04 tem de existir na 09 com as mesmas datas; a pendência da
    05 tem de apontar para uma reunião que existe. Sem isso, o cliente abre dois
    arquivos e vê a mesma agência com números diferentes.

Uso: python3 verifica_coerencia.py <pasta com as cópias recalculadas>
     (nunca recalcule os originais entregues)
"""
import sys, pathlib, datetime
from collections import defaultdict
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
sys.path.insert(0, str(AQUI.parent / "kit-essencial"))
from vc import Verificador, abrir, num, dt, txt, linhas
import verifica_coerencia as ess   # as checagens das 01, 02 e 03

MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


# ---------------------------------------------------------------- 04 projetos
def checa_04(pasta, V):
    wb = abrir(pasta, "04")
    cfg, et, p = wb["Config"], wb["Etapas"], wb["Painel"]
    HOJE = dt(cfg["B5"].value); AVISO = num(cfg["B6"].value)
    V.check("04 data de referência é literal (não =HOJE())", isinstance(HOJE, datetime.date), True)

    E = [dict(proj=txt(a), etapa=txt(b), resp=txt(c), ini=dt(d), fim=dt(e), pct=num(f),
              sit=txt(g), dias=h, real=dt(i), ordem=num(k), efet=num(l))
         for a, b, c, d, e, f, g, h, i, j, k, l
         in linhas(et, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], chave=1)]
    V.check("04 Etapas tem 20 exemplos", len(E), 20)

    for x in E:
        if x["pct"] >= 1 or x["real"] is not None:
            esp = "Concluída"
        elif x["fim"] < HOJE:
            esp = "Atrasada"
        elif (x["fim"] - HOJE).days <= AVISO:
            esp = "Vence em breve"
        elif x["ini"] <= HOJE:
            esp = "Em andamento"
        else:
            esp = "A iniciar"
        V.check(f"04 situação de {x['etapa'][:26]!r}", x["sit"], esp)
        # fim real preenchido vale 100 %, como o "Como usar" promete
        V.check(f"04 % efetivo de {x['etapa'][:26]!r}", x["efet"],
                1 if x["real"] is not None else x["pct"], tol=1e-9)
        V.check(f"04 etapa {x['etapa'][:26]!r} começa antes de terminar", x["ini"] <= x["fim"], True)

    proj = []
    for i in range(10):
        r = 10 + i
        nome = txt(cfg.cell(row=r, column=1).value)
        if not nome: continue
        proj.append(dict(nome=nome, cliente=txt(cfg.cell(row=r, column=2).value),
                         resp=txt(cfg.cell(row=r, column=3).value),
                         ini=dt(cfg.cell(row=r, column=4).value),
                         fim=dt(cfg.cell(row=r, column=5).value),
                         sit=txt(cfg.cell(row=r, column=6).value)))
    V.check("04 Config tem 4 projetos", len(proj), 4)

    for x in E:
        V.check(f"04 projeto {x['proj'][:26]!r} da etapa existe em Config",
                x["proj"] in [q["nome"] for q in proj], True)

    # KPIs
    ativos = sum(1 for q in proj if q["sit"] in ("No prazo", "Com atraso"))
    V.check("04 Painel Projetos ativos", p["A5"].value, ativos)
    V.check("04 Painel Etapas atrasadas", p["C5"].value, sum(1 for x in E if x["sit"] == "Atrasada"))
    V.check("04 Painel Vencem em breve", p["E5"].value, sum(1 for x in E if x["sit"] == "Vence em breve"))
    V.check("04 Painel Concluído (média)", num(p["G5"].value),
            sum(x["efet"] for x in E) / len(E), tol=1e-9)

    for i, q in enumerate(proj):
        r = 9 + i
        meus = [x for x in E if x["proj"] == q["nome"]]
        V.check(f"04 {q['nome'][:22]!r} nome no painel", txt(p.cell(row=r, column=1).value), q["nome"])
        V.check(f"04 {q['nome'][:22]!r} responsável", txt(p.cell(row=r, column=2).value), q["resp"])
        V.check(f"04 {q['nome'][:22]!r} prazo final", dt(p.cell(row=r, column=3).value), q["fim"])
        V.check(f"04 {q['nome'][:22]!r} etapas", p.cell(row=r, column=4).value, len(meus))
        V.check(f"04 {q['nome'][:22]!r} concluídas", p.cell(row=r, column=5).value,
                sum(1 for x in meus if x["sit"] == "Concluída"))
        V.check(f"04 {q['nome'][:22]!r} atrasadas", p.cell(row=r, column=6).value,
                sum(1 for x in meus if x["sit"] == "Atrasada"))
        V.check(f"04 {q['nome'][:22]!r} % médio", num(p.cell(row=r, column=7).value),
                sum(x["efet"] for x in meus) / len(meus) if meus else 0, tol=1e-9)
        # situação do projeto: a regra está em Config, o painel só repete
        conc = all(x["sit"] == "Concluída" for x in meus)
        esp = ("Sem etapas" if not meus else "Com atraso" if any(x["sit"] == "Atrasada" for x in meus)
               else "Concluído" if conc else "No prazo")
        V.check(f"04 {q['nome'][:22]!r} situação", q["sit"], esp)
        V.check(f"04 {q['nome'][:22]!r} situação repetida no painel",
                txt(p.cell(row=r, column=8).value), q["sit"])
        # nenhuma etapa fora da janela do projeto
        for x in meus:
            V.check(f"04 etapa {x['etapa'][:22]!r} dentro da janela do projeto",
                    q["ini"] <= x["ini"] and x["fim"] <= q["fim"], True)

    # fila "o que fazer primeiro"
    fila = sorted([x for x in E if x["ordem"] > 0], key=lambda x: -x["ordem"])[:12]
    for k in range(12):
        r = 23 + k
        V.check(f"04 fila #{k+1}", txt(p.cell(row=r, column=3).value),
                fila[k]["etapa"] if k < len(fila) else "")

    # carga por responsável (a coluna "Próximo fim" usa SUMPRODUCT/MIN em vez de MINIFS)
    for i in range(10):
        r = 38 + i
        pessoa = txt(p.cell(row=r, column=1).value)
        if not pessoa: continue
        meus = [x for x in E if x["resp"] == pessoa]
        abertas = [x for x in meus if x["sit"] != "Concluída"]
        V.check(f"04 {pessoa} etapas abertas", p.cell(row=r, column=2).value, len(abertas))
        V.check(f"04 {pessoa} atrasadas", p.cell(row=r, column=3).value,
                sum(1 for x in meus if x["sit"] == "Atrasada"))
        V.check(f"04 {pessoa} vencem em breve", p.cell(row=r, column=4).value,
                sum(1 for x in meus if x["sit"] == "Vence em breve"))
        pf = p.cell(row=r, column=5).value
        esperado = min((x["fim"] for x in abertas), default=None)
        # o SUMPRODUCT/MIN tem de devolver data ou vazio; 1E+10 ou 1900 seria o defeito
        V.check(f"04 {pessoa} próximo fim", dt(pf) if pf not in (None, "") else None, esperado)
    return proj, E


# ---------------------------------------------------------------- 05 ata
def checa_05(pasta, V):
    wb = abrir(pasta, "05")
    cfg, re_, pe, p = wb["Config"], wb["Reuniões"], wb["Pendências"], wb["Em aberto"]
    HOJE = dt(cfg["B5"].value)
    V.check("05 data de referência é literal (não =HOJE())", isinstance(HOJE, datetime.date), True)

    R = [dict(cod=txt(a), data=dt(b), assunto=txt(c), part=txt(d), dec=txt(e),
              abertas=num(f), atrasadas=num(g))
         for a, b, c, d, e, f, g in linhas(re_, 5, [1, 2, 3, 4, 5, 6, 7], chave=2)]
    P = [dict(reu=txt(a), pend=txt(b), dono=txt(c), prazo=dt(d), prio=txt(e), status=txt(f),
              feita=dt(g), sit=txt(h), dias=i, ordem=num(j))
         for a, b, c, d, e, f, g, h, i, j in linhas(pe, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], chave=1)]
    V.check("05 tem 4 reuniões", len(R), 4)
    V.check("05 tem 12 pendências", len(P), 12)

    for i, x in enumerate(R):
        V.check(f"05 código da reunião {i+1}", x["cod"], f"R-{i+1:03d}")
        minhas = [q for q in P if q["reu"] == x["cod"]]
        V.check(f"05 {x['cod']} pendências abertas", x["abertas"],
                sum(1 for q in minhas if q["status"] != "Feito"))
        V.check(f"05 {x['cod']} pendências atrasadas", x["atrasadas"],
                sum(1 for q in minhas if q["sit"] == "Atrasada"))

    codigos = {x["cod"] for x in R}
    for x in P:
        V.check(f"05 pendência {x['pend'][:26]!r} aponta para reunião existente",
                x["reu"] in codigos, True)
        if x["status"] == "Feito":
            esp = "Feita"
        elif x["prazo"] is None:
            esp = "Sem prazo"
        else:
            d = (x["prazo"] - HOJE).days
            esp = "Atrasada" if d < 0 else "Hoje" if d == 0 else "Esta semana" if d <= 7 else "No prazo"
        V.check(f"05 situação de {x['pend'][:26]!r}", x["sit"], esp)
        if x["status"] == "Feito":
            V.check(f"05 {x['pend'][:26]!r} feita tem data de conclusão", x["feita"] is not None, True)

    V.check("05 Abertas", p["A5"].value, sum(1 for x in P if x["status"] != "Feito"))
    V.check("05 Atrasadas", p["C5"].value, sum(1 for x in P if x["sit"] == "Atrasada"))
    V.check("05 Para hoje", p["E5"].value, sum(1 for x in P if x["sit"] == "Hoje"))
    V.check("05 Feitas no total", p["G5"].value, sum(1 for x in P if x["status"] == "Feito"))

    fila = sorted([x for x in P if x["ordem"] > 0], key=lambda x: -x["ordem"])[:15]
    for k in range(15):
        r = 10 + k
        V.check(f"05 fila #{k+1}", txt(p.cell(row=r, column=2).value),
                fila[k]["pend"] if k < len(fila) else "")

    for i in range(12):
        r = 28 + i
        pessoa = txt(p.cell(row=r, column=1).value)
        if not pessoa: continue
        meus = [x for x in P if x["dono"] == pessoa]
        abertas = [x for x in meus if x["status"] != "Feito"]
        V.check(f"05 {pessoa} abertas", p.cell(row=r, column=2).value, len(abertas))
        V.check(f"05 {pessoa} atrasadas", p.cell(row=r, column=3).value,
                sum(1 for x in meus if x["sit"] == "Atrasada"))
        V.check(f"05 {pessoa} esta semana (+hoje)", p.cell(row=r, column=4).value,
                sum(1 for x in meus if x["sit"] in ("Esta semana", "Hoje")))
        V.check(f"05 {pessoa} feitas", p.cell(row=r, column=5).value,
                sum(1 for x in meus if x["status"] == "Feito"))
        pp = p.cell(row=r, column=6).value
        V.check(f"05 {pessoa} próximo prazo",
                dt(pp) if pp not in (None, "") else None,
                min((x["prazo"] for x in abertas if x["prazo"] is not None), default=None))


# ---------------------------------------------------------------- 06 metas
def checa_06(pasta, V):
    wb = abrir(pasta, "06")
    cfg, m, w, mz, p = wb["Config"], wb["Metas"], wb["Semanas"], wb["Meses"], wb["Painel"]
    HOJE = dt(cfg["B8"].value); INI = dt(cfg["B6"].value); FIM = dt(cfg["B7"].value)
    V.check("06 data de referência é literal (não =HOJE())", isinstance(HOJE, datetime.date), True)
    V.check("06 semana atual do trimestre", cfg["B9"].value,
            0 if HOJE < INI else min(13, (HOJE - INI).days // 7 + 1))
    V.check("06 % do trimestre decorrido", num(cfg["B10"].value),
            max(0, min(1, (HOJE - INI).days / (FIM - INI).days)), tol=1e-9)

    K = []
    for i in range(20):
        r = 5 + i
        kr = txt(m.cell(row=r, column=2).value)
        if not kr: continue
        K.append(dict(r=r, i=i, kr=kr, dono=txt(m.cell(row=r, column=3).value),
                      part=num(m.cell(row=r, column=5).value),
                      meta=num(m.cell(row=r, column=6).value),
                      atual=num(m.cell(row=r, column=7).value),
                      prog=m.cell(row=r, column=8).value,
                      esp=m.cell(row=r, column=9).value,
                      sem=txt(m.cell(row=r, column=10).value),
                      sentido=txt(m.cell(row=r, column=11).value)))
    V.check("06 tem 9 resultados-chave", len(K), 9)

    dec = num(cfg["B10"].value)
    for x in K:
        # mesma regra da planilha: no alvo = 1; fora, caminho entre partida e meta; partida já
        # dentro da meta (teto/piso) = meta ÷ atual (rodada 5)
        E, Fm, G = x["part"], x["meta"], x["atual"]
        if G in ("", None): prog = ""
        elif x["sentido"] == "Menor é melhor":
            prog = 1 if G <= Fm else (max(0, (E - G) / (E - Fm)) if E > Fm else (0 if G == 0 else max(0, Fm / G)))
        else:
            prog = 1 if G >= Fm else (max(0, (G - E) / (Fm - E)) if E < Fm else (0 if Fm == 0 else max(0, G / Fm)))
        V.check(f"06 progresso de {x['kr'][:30]!r}", num(x["prog"]), num(prog), tol=1e-9)
        V.check(f"06 esperado de {x['kr'][:30]!r}", num(x["esp"]), dec, tol=1e-9)
        pr = num(x["prog"])
        esp = ("Atingido" if pr >= 1 else "No ritmo" if pr >= dec - 0.1
               else "Atenção" if pr >= dec - 0.25 else "Em risco")
        V.check(f"06 semáforo de {x['kr'][:30]!r}", x["sem"], esp)
        V.check(f"06 sentido de {x['kr'][:30]!r} é declarado",
                x["sentido"] in ("Maior é melhor", "Menor é melhor"), True)

        # Semanas: a linha espelha a meta e a última semana preenchida é o valor atual
        rr = 5 + x["i"]
        V.check(f"06 Semanas repete o KR {x['kr'][:26]!r}", txt(w.cell(row=rr, column=1).value), x["kr"])
        V.check(f"06 Semanas repete a meta de {x['kr'][:26]!r}", num(w.cell(row=rr, column=2).value),
                x["meta"], tol=1e-9)
        semanas = [w.cell(row=rr, column=3 + s).value for s in range(13)]
        cheias = [num(v) for v in semanas if v not in (None, "")]
        V.check(f"06 última semana de {x['kr'][:26]!r} == valor atual em Metas",
                cheias[-1] if cheias else None, x["atual"], tol=1e-9)
        V.check(f"06 semanas de {x['kr'][:26]!r} preenchidas sem furo",
                all(v not in (None, "") for v in semanas[:len(cheias)]), True)

        # Meses: cada faixa é o último valor lançado das suas semanas (S1-4, S5-9, S10-13)
        faixas = [(0, 4), (4, 9), (9, 13)]
        for j, (a, b) in enumerate(faixas):
            trecho = [num(v) for v in semanas[a:b] if v not in (None, "")]
            mv = mz.cell(row=rr, column=3 + j).value
            V.check(f"06 Meses mês {j+1} de {x['kr'][:22]!r}",
                    num(mv) if mv not in (None, "") else None,
                    trecho[-1] if trecho else None, tol=1e-9)
        m3 = mz.cell(row=rr, column=5).value
        if m3 not in (None, ""):
            V.check(f"06 Meses ganho no trimestre de {x['kr'][:22]!r}",
                    num(mz.cell(row=rr, column=6).value), num(m3) - x["part"], tol=1e-9)
            V.check(f"06 Meses falta para a meta de {x['kr'][:22]!r}",
                    num(mz.cell(row=rr, column=7).value), x["meta"] - num(m3), tol=1e-9)

    V.check("06 Painel Resultados-chave", p["A5"].value, len(K))
    V.check("06 Painel Atingidos", p["C5"].value, sum(1 for x in K if x["sem"] == "Atingido"))
    V.check("06 Painel Em risco", p["E5"].value, sum(1 for x in K if x["sem"] == "Em risco"))
    V.check("06 Painel Progresso médio", num(p["G5"].value),
            sum(num(x["prog"]) for x in K) / len(K), tol=1e-9)

    # por objetivo: blocos de 4 linhas em Metas
    for o in range(5):
        r = 9 + o
        obj = txt(p.cell(row=r, column=1).value)
        if not obj: continue
        bloco = [x for x in K if 5 + o * 4 <= x["r"] <= 5 + o * 4 + 3]
        V.check(f"06 {obj[:26]!r} resultados-chave", p.cell(row=r, column=2).value, len(bloco))
        V.check(f"06 {obj[:26]!r} progresso médio", num(p.cell(row=r, column=3).value),
                sum(num(x["prog"]) for x in bloco) / len(bloco) if bloco else 0, tol=1e-9)
        V.check(f"06 {obj[:26]!r} atingidos", p.cell(row=r, column=4).value,
                sum(1 for x in bloco if x["sem"] == "Atingido"))
        V.check(f"06 {obj[:26]!r} em risco", p.cell(row=r, column=5).value,
                sum(1 for x in bloco if x["sem"] == "Em risco"))
    for x in K:
        rr = 17 + x["i"]
        V.check(f"06 lista repete {x['kr'][:26]!r}", txt(p.cell(row=rr, column=1).value), x["kr"])
        V.check(f"06 lista atual de {x['kr'][:26]!r}", num(p.cell(row=rr, column=3).value),
                x["atual"], tol=1e-9)
        V.check(f"06 lista semáforo de {x['kr'][:26]!r}", txt(p.cell(row=rr, column=7).value), x["sem"])


# ---------------------------------------------------------------- 07 orçamento
def checa_07(pasta, V):
    wb = abrir(pasta, "07")
    cfg, pv, re_, p = wb["Config"], wb["Previsto"], wb["Realizado"], wb["Painel"]
    M = int(num(cfg["B7"].value)); Y = int(num(cfg["B5"].value)); AL = num(cfg["B8"].value)
    V.check("07 número do mês == posição do nome", M, MESES.index(txt(cfg["B6"].value)) + 1)

    C = []
    for i in range(20):
        r = 12 + i
        nome = txt(cfg.cell(row=r, column=1).value)
        if not nome: continue
        C.append(dict(i=i, nome=nome, tipo=txt(cfg.cell(row=r, column=2).value),
                      resp=txt(cfg.cell(row=r, column=3).value)))
    V.check("07 tem 13 categorias", len(C), 13)
    for x in C:
        V.check(f"07 tipo de {x['nome']!r} é Receita ou Despesa",
                x["tipo"] in ("Receita", "Despesa"), True)

    prev = {}
    for x in C:
        r = 5 + x["i"]
        V.check(f"07 Previsto repete {x['nome']!r}", txt(pv.cell(row=r, column=1).value), x["nome"])
        vals = [num(pv.cell(row=r, column=2 + j).value) for j in range(12)]
        prev[x["nome"]] = vals
        V.check(f"07 Previsto total de {x['nome']!r}", num(pv.cell(row=r, column=14).value),
                sum(vals), tol=0.01)
    for j in range(12):
        V.check(f"07 Previsto receitas do mês {j+1}", num(pv.cell(row=25, column=2 + j).value),
                sum(prev[x["nome"]][j] for x in C if x["tipo"] == "Receita"), tol=0.01)
        V.check(f"07 Previsto despesas do mês {j+1}", num(pv.cell(row=26, column=2 + j).value),
                sum(prev[x["nome"]][j] for x in C if x["tipo"] == "Despesa"), tol=0.01)
        V.check(f"07 Previsto resultado do mês {j+1}", num(pv.cell(row=27, column=2 + j).value),
                num(pv.cell(row=25, column=2 + j).value) - num(pv.cell(row=26, column=2 + j).value),
                tol=0.01)

    Rz = [dict(data=dt(a), cat=txt(b), desc=txt(c), valor=num(d), mes=num(f), ano=num(g), tipo=txt(h))
          for a, b, c, d, e, f, g, h in linhas(re_, 5, [1, 2, 3, 4, 5, 6, 7, 8])]
    # 110 = 9 meses × 13 categorias, menos os 7 meses em que Equipamentos foi previsto zero
    V.check("07 Realizado tem 110 lançamentos", len(Rz), 110)
    tipos = {x["nome"]: x["tipo"] for x in C}
    for x in Rz:
        V.check(f"07 categoria {x['cat']!r} do realizado existe em Config", x["cat"] in tipos, True)
        V.check(f"07 tipo do lançamento {x['desc'][:22]!r}", x["tipo"], tipos.get(x["cat"], "?"))
        V.check(f"07 mês do lançamento {x['desc'][:22]!r}", x["mes"], x["data"].month)

    def real(cat=None, tipo=None, mes=None, ate=None):
        return sum(x["valor"] for x in Rz
                   if (cat is None or x["cat"] == cat) and (tipo is None or x["tipo"] == tipo)
                   and x["ano"] == Y
                   and (mes is None or x["mes"] == mes) and (ate is None or x["mes"] <= ate))

    V.check("07 Receita prevista", p["A5"].value,
            sum(prev[x["nome"]][M - 1] for x in C if x["tipo"] == "Receita"), tol=0.01)
    V.check("07 Receita realizada", p["C5"].value, real(tipo="Receita", mes=M), tol=0.01)
    V.check("07 Despesa prevista", p["E5"].value,
            sum(prev[x["nome"]][M - 1] for x in C if x["tipo"] == "Despesa"), tol=0.01)
    V.check("07 Despesa realizada", p["G5"].value, real(tipo="Despesa", mes=M), tol=0.01)
    V.check("07 Resultado do mês (realizado)", p["I5"].value,
            num(p["C5"].value) - num(p["G5"].value), tol=0.01)

    for x in C:
        r = 9 + x["i"]
        pr = prev[x["nome"]][M - 1]; rl = real(cat=x["nome"], mes=M)
        V.check(f"07 {x['nome']!r} previsto", num(p.cell(row=r, column=3).value), pr, tol=0.01)
        V.check(f"07 {x['nome']!r} realizado", num(p.cell(row=r, column=4).value), rl, tol=0.01)
        V.check(f"07 {x['nome']!r} desvio R$", num(p.cell(row=r, column=5).value), rl - pr, tol=0.01)
        if pr:
            V.check(f"07 {x['nome']!r} desvio %", num(p.cell(row=r, column=6).value),
                    (rl - pr) / pr, tol=1e-9)
        if x["tipo"] == "Despesa":
            esp = ("Estourou" if pr > 0 and (rl - pr) / pr > AL else "Acima" if rl > pr else "Dentro")
        else:
            esp = ("Abaixo da meta" if pr > 0 and (rl - pr) / pr < -AL
                   else "Meta batida" if rl >= pr else "Perto da meta")
        V.check(f"07 {x['nome']!r} situação", txt(p.cell(row=r, column=7).value), esp)
        V.check(f"07 {x['nome']!r} acumulado previsto", num(p.cell(row=r, column=8).value),
                sum(prev[x["nome"]][:M]), tol=0.01)
        V.check(f"07 {x['nome']!r} acumulado realizado", num(p.cell(row=r, column=9).value),
                real(cat=x["nome"], ate=M), tol=0.01)

    for j in range(12):
        r = 32 + j
        V.check(f"07 ano: nome do mês {j+1}", txt(p.cell(row=r, column=1).value), MESES[j])
        rp = sum(prev[x["nome"]][j] for x in C if x["tipo"] == "Receita")
        dp = sum(prev[x["nome"]][j] for x in C if x["tipo"] == "Despesa")
        rr = real(tipo="Receita", mes=j + 1); dr = real(tipo="Despesa", mes=j + 1)
        V.check(f"07 ano: receita prevista {MESES[j]}", num(p.cell(row=r, column=2).value), rp, tol=0.01)
        V.check(f"07 ano: receita realizada {MESES[j]}", num(p.cell(row=r, column=3).value), rr, tol=0.01)
        V.check(f"07 ano: despesa prevista {MESES[j]}", num(p.cell(row=r, column=4).value), dp, tol=0.01)
        V.check(f"07 ano: despesa realizada {MESES[j]}", num(p.cell(row=r, column=5).value), dr, tol=0.01)
        V.check(f"07 ano: resultado previsto {MESES[j]}", num(p.cell(row=r, column=6).value), rp - dp, tol=0.01)
        V.check(f"07 ano: resultado realizado {MESES[j]}", num(p.cell(row=r, column=7).value), rr - dr, tol=0.01)
    V.check("07 setembro no bloco do ano == KPI receita realizada",
            p.cell(row=32 + M - 1, column=3).value, p["C5"].value, tol=0.01)


# ---------------------------------------------------------------- 08 funil
def checa_08(pasta, V):
    wb = abrir(pasta, "08")
    cfg, pr, p = wb["Config"], wb["Propostas"], wb["Painel"]
    HOJE = dt(cfg["B5"].value); META = num(cfg["B6"].value); PAR = num(cfg["B7"].value)
    V.check("08 data de referência é literal (não =HOJE())", isinstance(HOJE, datetime.date), True)
    ETAPAS = {txt(cfg.cell(row=11 + i, column=1).value): num(cfg.cell(row=11 + i, column=2).value)
              for i in range(6)}

    P = [dict(cli=txt(a), prop=txt(b), origem=txt(c), resp=txt(d), valor=num(e), etapa=txt(f),
              entrada=dt(g), mov=dt(h), prev=dt(i), fech=dt(j), motivo=txt(k),
              prob=num(l), pond=num(m_), paradaa=n, sit=txt(o))
         for a, b, c, d, e, f, g, h, i, j, k, l, m_, n, o
         in linhas(pr, 5, list(range(1, 16)))]
    V.check("08 tem 14 propostas", len(P), 14)

    for x in P:
        V.check(f"08 etapa de {x['cli']!r} existe em Config", x["etapa"] in ETAPAS, True)
        V.check(f"08 probabilidade de {x['cli']!r}", x["prob"], ETAPAS[x["etapa"]], tol=1e-9)
        V.check(f"08 valor ponderado de {x['cli']!r}", x["pond"], x["valor"] * x["prob"], tol=0.01)
        if x["etapa"] in ("Ganha", "Perdida"):
            esp = "Fechada" if x["etapa"] == "Ganha" else "Perdida"
            V.check(f"08 {x['cli']!r} fechada tem data de fechamento", x["fech"] is not None, True)
        else:
            dias = (HOJE - (x["mov"] or x["entrada"])).days
            V.check(f"08 dias parada de {x['cli']!r}", num(x["paradaa"]), dias, tol=0.001)
            esp = ("Fechamento vencido" if x["prev"] is not None and x["prev"] < HOJE
                   else "Parada" if dias > PAR else "Ativa")
        V.check(f"08 situação de {x['cli']!r}", x["sit"], esp)
        if x["etapa"] == "Perdida":
            V.check(f"08 {x['cli']!r} perdida tem motivo", x["motivo"] != "", True)

    abertas = [x for x in P if x["etapa"] not in ("Ganha", "Perdida")]
    V.check("08 Em aberto (R$)", p["A5"].value, sum(x["valor"] for x in abertas), tol=0.01)
    V.check("08 Previsão ponderada", p["C5"].value, sum(x["pond"] for x in abertas), tol=0.01)
    tri = 3 * ((HOJE.month - 1) // 3) + 1
    ini_tri = datetime.date(HOJE.year, tri, 1)
    fim_tri = (datetime.date(HOJE.year + (tri + 3 > 12), 1 if tri + 3 > 12 else tri + 3, 1))
    ganho = sum(x["valor"] for x in P
                if x["etapa"] == "Ganha" and x["fech"] and ini_tri <= x["fech"] < fim_tri)
    V.check("08 Ganho no trimestre", p["E5"].value, ganho, tol=0.01)
    V.check("08 % da meta", num(p["G5"].value), ganho / META if META else 0, tol=1e-9)

    ordem = ["Contato", "Reunião feita", "Proposta enviada", "Negociação", "Ganha", "Perdida"]
    for i in range(4):
        r = 9 + i
        et = txt(p.cell(row=r, column=1).value)
        V.check(f"08 etapa da linha {r}", et, ordem[i])
        nela = [x for x in P if x["etapa"] == et]
        V.check(f"08 {et} propostas", p.cell(row=r, column=2).value, len(nela))
        V.check(f"08 {et} valor", p.cell(row=r, column=3).value, sum(x["valor"] for x in nela), tol=0.01)
        V.check(f"08 {et} ponderado", p.cell(row=r, column=4).value, sum(x["pond"] for x in nela), tol=0.01)
        adiante = sum(1 for x in P if x["etapa"] in ordem[i + 1:])
        V.check(f"08 {et} taxa de passagem", num(p.cell(row=r, column=5).value),
                adiante / (len(nela) + adiante) if (len(nela) + adiante) else 0, tol=1e-9)
    g = [x for x in P if x["etapa"] == "Ganha"]; pd = [x for x in P if x["etapa"] == "Perdida"]
    V.check("08 Ganhas (total) quantidade", p.cell(row=13, column=2).value, len(g))
    V.check("08 Ganhas (total) valor", p.cell(row=13, column=3).value, sum(x["valor"] for x in g), tol=0.01)
    V.check("08 Perdidas (total) quantidade", p.cell(row=14, column=2).value, len(pd))
    V.check("08 Perdidas (total) valor", p.cell(row=14, column=3).value, sum(x["valor"] for x in pd), tol=0.01)
    V.check("08 taxa de conversão", num(p.cell(row=15, column=2).value),
            len(g) / (len(g) + len(pd)) if (g or pd) else 0, tol=1e-9)
    V.check("08 ticket médio das ganhas", p.cell(row=16, column=2).value,
            sum(x["valor"] for x in g) / len(g) if g else 0, tol=0.01)

    for i in range(8):
        r = 36 + i
        org = txt(p.cell(row=r, column=1).value)
        if not org: continue
        nela = [x for x in P if x["origem"] == org]
        gg = [x for x in nela if x["etapa"] == "Ganha"]; pp = [x for x in nela if x["etapa"] == "Perdida"]
        V.check(f"08 origem {org!r} propostas", p.cell(row=r, column=2).value, len(nela))
        V.check(f"08 origem {org!r} ganhas", p.cell(row=r, column=3).value, len(gg))
        V.check(f"08 origem {org!r} conversão", num(p.cell(row=r, column=4).value),
                len(gg) / (len(gg) + len(pp)) if (gg or pp) else 0, tol=1e-9)
        V.check(f"08 origem {org!r} valor ganho", p.cell(row=r, column=5).value,
                sum(x["valor"] for x in gg), tol=0.01)
    for i in range(8):
        r = 36 + i
        mot = txt(p.cell(row=r, column=7).value)
        if not mot: continue
        nela = [x for x in pd if x["motivo"] == mot]
        V.check(f"08 motivo {mot!r} perdidas", p.cell(row=r, column=8).value, len(nela))
        V.check(f"08 motivo {mot!r} valor perdido", p.cell(row=r, column=9).value,
                sum(x["valor"] for x in nela), tol=0.01)
    V.check("08 soma das origens == total de propostas",
            sum(num(p.cell(row=36 + i, column=2).value) for i in range(8)), len(P))
    V.check("08 soma dos motivos == perdidas",
            sum(num(p.cell(row=36 + i, column=8).value) for i in range(8)), len(pd))
    return P


# ---------------------------------------------------------------- 09 horas
def checa_09(pasta, V):
    wb = abrir(pasta, "09")
    cfg, h, p = wb["Config"], wb["Horas"], wb["Painel"]
    M = int(num(cfg["B7"].value)); Y = int(num(cfg["B5"].value))
    V.check("09 número do mês == posição do nome", M, MESES.index(txt(cfg["B6"].value)) + 1)

    PES = []
    for i in range(10):
        r = 11 + i
        nome = txt(cfg.cell(row=r, column=1).value)
        if not nome: continue
        PES.append(dict(i=i, nome=nome, custo=num(cfg.cell(row=r, column=2).value),
                        disp=num(cfg.cell(row=r, column=3).value),
                        ch=num(cfg.cell(row=r, column=4).value)))
    V.check("09 tem 4 pessoas", len(PES), 4)
    for x in PES:
        V.check(f"09 custo-hora de {x['nome']}", x["ch"], x["custo"] / x["disp"], tol=1e-9)

    PRJ = []
    for i in range(12):
        r = 24 + i
        nome = txt(cfg.cell(row=r, column=1).value)
        if not nome: continue
        PRJ.append(dict(i=i, nome=nome, cliente=txt(cfg.cell(row=r, column=2).value),
                        orcadas=num(cfg.cell(row=r, column=3).value),
                        cobrado=num(cfg.cell(row=r, column=4).value),
                        status=txt(cfg.cell(row=r, column=5).value)))
    V.check("09 tem 7 projetos", len(PRJ), 7)

    H = [dict(data=dt(a), pessoa=txt(b), proj=txt(c), ativ=txt(d), horas=num(e),
              custo=num(f), mes=num(g), ano=num(i), fat=txt(j))
         for a, b, c, d, e, f, g, i, j in linhas(h, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])]
    V.check("09 tem 559 lançamentos de hora", len(H), 559)
    ch = {x["nome"]: x["ch"] for x in PES}
    nomes_prj = {x["nome"] for x in PRJ}
    for x in H[:80] + H[-80:]:   # amostra: 800 linhas × 9 checagens seria ruído
        V.check(f"09 pessoa {x['pessoa']!r} existe em Config", x["pessoa"] in ch, True)
        V.check(f"09 projeto {x['proj'][:22]!r} existe em Config", x["proj"] in nomes_prj, True)
        V.check(f"09 custo de {x['pessoa']} em {x['data']}", x["custo"],
                x["horas"] * ch[x["pessoa"]], tol=0.01)
        V.check(f"09 mês de {x['data']}", x["mes"], x["data"].month)
    # projeto com status Proposta não tem hora lançada: o "Como usar" promete isso
    for q in PRJ:
        if q["status"] == "Proposta":
            V.check(f"09 {q['nome'][:26]!r} (Proposta) não tem hora lançada",
                    sum(1 for x in H if x["proj"] == q["nome"]), 0)

    hmes = sum(x["horas"] for x in H if x["mes"] == M and x["ano"] == Y)
    V.check("09 Horas no mês", p["A5"].value, hmes, tol=0.01)
    V.check("09 Custo no mês", p["C5"].value,
            sum(x["custo"] for x in H if x["mes"] == M and x["ano"] == Y), tol=0.01)
    V.check("09 Horas faturáveis (%)", num(p["E5"].value),
            sum(x["horas"] for x in H if x["mes"] == M and x["ano"] == Y and x["fat"] == "Sim") / hmes,
            tol=1e-9)
    V.check("09 Ocupação da equipe", num(p["G5"].value),
            hmes / sum(x["disp"] for x in PES), tol=1e-9)

    # o Painel ganhou o aviso de custo incompleto em A7: a tabela por projeto desceu
    # uma linha (cabeçalho 9, projetos a partir da 10)
    V.check("09 Painel sem aviso de custo incompleto no exemplo", txt(p["A7"].value), "")
    for q in PRJ:
        r = 10 + q["i"]
        usadas = sum(x["horas"] for x in H if x["proj"] == q["nome"])
        custo = sum(x["custo"] for x in H if x["proj"] == q["nome"])
        V.check(f"09 {q['nome'][:26]!r} nome", txt(p.cell(row=r, column=1).value), q["nome"])
        V.check(f"09 {q['nome'][:26]!r} cliente", txt(p.cell(row=r, column=2).value), q["cliente"])
        V.check(f"09 {q['nome'][:26]!r} horas orçadas", num(p.cell(row=r, column=3).value), q["orcadas"])
        V.check(f"09 {q['nome'][:26]!r} horas usadas", num(p.cell(row=r, column=4).value), usadas, tol=0.01)
        if q["orcadas"]:
            V.check(f"09 {q['nome'][:26]!r} % do orçado", num(p.cell(row=r, column=5).value),
                    usadas / q["orcadas"], tol=1e-9)
        V.check(f"09 {q['nome'][:26]!r} custo", num(p.cell(row=r, column=6).value), custo, tol=0.01)
        V.check(f"09 {q['nome'][:26]!r} valor cobrado", num(p.cell(row=r, column=7).value), q["cobrado"])
        V.check(f"09 {q['nome'][:26]!r} margem R$", num(p.cell(row=r, column=8).value),
                q["cobrado"] - custo, tol=0.01)
        if q["cobrado"]:
            V.check(f"09 {q['nome'][:26]!r} margem %", num(p.cell(row=r, column=9).value),
                    (q["cobrado"] - custo) / q["cobrado"], tol=1e-9)
        pcorc = usadas / q["orcadas"] if q["orcadas"] else None
        mg = (q["cobrado"] - custo) / q["cobrado"] if q["cobrado"] else None
        esp = ("Interno" if q["status"] == "Interno" else "Proposta" if q["status"] == "Proposta"
               else "Estourou as horas" if pcorc is not None and pcorc > 1
               else "Margem baixa" if mg is not None and mg < 0.2
               else "Perto do limite" if pcorc is not None and pcorc > 0.85 and q["status"] == "Em andamento"
               else "Saudável")
        V.check(f"09 {q['nome'][:26]!r} situação", txt(p.cell(row=r, column=10).value), esp)

    for x in PES:
        r = 25 + x["i"]
        lan = sum(q["horas"] for q in H if q["pessoa"] == x["nome"] and q["mes"] == M and q["ano"] == Y)
        V.check(f"09 {x['nome']} horas lançadas no mês", num(p.cell(row=r, column=2).value), lan, tol=0.01)
        V.check(f"09 {x['nome']} disponíveis", num(p.cell(row=r, column=3).value), x["disp"])
        V.check(f"09 {x['nome']} ocupação", num(p.cell(row=r, column=4).value),
                lan / x["disp"] if x["disp"] else 0, tol=1e-9)
        fat = sum(q["horas"] for q in H if q["pessoa"] == x["nome"] and q["mes"] == M
                  and q["ano"] == Y and q["fat"] == "Sim")
        V.check(f"09 {x['nome']} faturáveis", num(p.cell(row=r, column=5).value),
                fat / lan if lan else 0, tol=1e-9)
        V.check(f"09 {x['nome']} custo no mês", num(p.cell(row=r, column=6).value),
                sum(q["custo"] for q in H if q["pessoa"] == x["nome"] and q["mes"] == M
                    and q["ano"] == Y), tol=0.01)
        V.check(f"09 {x['nome']} custo-hora", num(p.cell(row=r, column=7).value), x["ch"], tol=1e-9)
    V.check("09 horas do mês == soma das pessoas", hmes,
            sum(num(p.cell(row=25 + x["i"], column=2).value) for x in PES), tol=0.01)
    return PRJ, H


# ---------------------------------------------------------------- 10 base
def checa_10(pasta, V):
    wb = abrir(pasta, "10")
    ls, b, ck, s = wb["Listas"], wb["Base"], wb["Checklist"], wb["Resumo"]
    cats = [txt(ls.cell(row=5 + i, column=1).value) for i in range(30)]
    clis = [txt(ls.cell(row=5 + i, column=5).value) for i in range(30)]
    B = [dict(data=dt(b_), cli=txt(c), cat=txt(d), canal=txt(e), resp=txt(f), desc=txt(g),
              qtd=num(h), vu=num(i), total=num(j), status=txt(k), mes=num(l), ano=num(m_))
         for a, b_, c, d, e, f, g, h, i, j, k, l, m_
         in linhas(b, 2, list(range(1, 14)), chave=1)]
    V.check("10 Base tem 180 registros", len(B), 180)
    for x in B:
        V.check(f"10 valor total de {x['desc'][:22]!r} em {x['data']}", x["total"],
                x["qtd"] * x["vu"], tol=0.01)
        V.check(f"10 mês de {x['data']}", x["mes"], x["data"].month)
        V.check(f"10 ano de {x['data']}", x["ano"], x["data"].year)
        V.check(f"10 categoria {x['cat']!r} está em Listas", x["cat"] in cats, True)
        V.check(f"10 cliente {x['cli']!r} está em Listas", x["cli"] in clis, True)

    # o checklist tem de estar zerado no exemplo: base suja de fábrica ensina errado
    V.check("10 Checklist linhas preenchidas", ck["B5"].value, len(B))
    for r in range(6, 15):
        rot = txt(ck.cell(row=r, column=1).value)
        V.check(f"10 Checklist {rot[:44]!r} = 0", num(ck.cell(row=r, column=2).value), 0)
        V.check(f"10 Checklist {rot[:44]!r} situação OK", txt(ck.cell(row=r, column=3).value), "OK")
    V.check("10 Checklist 'Base pronta?'", txt(ck["B16"].value), "Sim: pode analisar")

    ANO = int(num(s["B4"].value)); ST = txt(s["B5"].value)
    for i in range(30):
        r = 8 + i
        cat = txt(s.cell(row=r, column=1).value)
        if not cat: continue
        for m_ in range(12):
            V.check(f"10 Resumo {cat!r} mês {m_+1}", num(s.cell(row=r, column=2 + m_).value),
                    sum(x["total"] for x in B if x["cat"] == cat and x["mes"] == m_ + 1
                        and x["ano"] == ANO and x["status"] == ST), tol=0.01)
        V.check(f"10 Resumo total de {cat!r}", num(s.cell(row=r, column=14).value),
                sum(num(s.cell(row=r, column=2 + m_).value) for m_ in range(12)), tol=0.01)
    V.check("10 Resumo total geral", num(s.cell(row=38, column=14).value),
            sum(x["total"] for x in B if x["ano"] == ANO and x["status"] == ST), tol=0.01)
    for i in range(30):
        r = 42 + i
        cli = txt(s.cell(row=r, column=1).value)
        if not cli: continue
        meus = [x for x in B if x["cli"] == cli and x["ano"] == ANO and x["status"] == ST]
        V.check(f"10 Resumo {cli!r} registros", num(s.cell(row=r, column=2).value), len(meus))
        V.check(f"10 Resumo {cli!r} valor no ano", num(s.cell(row=r, column=3).value),
                sum(x["total"] for x in meus), tol=0.01)
        if meus:
            V.check(f"10 Resumo {cli!r} ticket médio", num(s.cell(row=r, column=4).value),
                    sum(x["total"] for x in meus) / len(meus), tol=0.01)
        # último registro: SUMPRODUCT/MAX no lugar de MAXIFS; tem de virar data
        todos = [x["data"] for x in B if x["cli"] == cli]
        ur = s.cell(row=r, column=5).value
        V.check(f"10 Resumo {cli!r} último registro",
                dt(ur) if ur not in (None, "") else None, max(todos) if todos else None)


# ------------------------------------------------------- entre arquivos
def checa_02_x_07(pasta, V):
    """A Prisma tem de contar UMA história por mês. Esta afirmação faltava e por isso o
    G-25 passou: o relatório mensal dizia resultado 41.400 em setembro e o orçamento,
    14.171,85 — a mesma empresa, o mesmo mês, R$ 27.228,15 de diferença."""
    ind = abrir(pasta, "02")["Indicadores"]
    p7 = abrir(pasta, "07")["Painel"]
    rot = {txt(ind.cell(row=5 + i, column=1).value): 5 + i for i in range(12)}
    for j in range(12):
        mes = MESES[j]
        r02 = ind.cell(row=rot["Receita"], column=6 + j).value
        if r02 in (None, ""): continue        # mês ainda não preenchido no exemplo
        d02 = ind.cell(row=rot["Despesas"], column=6 + j).value
        s02 = ind.cell(row=rot["Resultado (receita - despesas)"], column=6 + j).value
        V.check(f"02→07 receita realizada de {mes}", num(p7.cell(row=32 + j, column=3).value), num(r02), tol=0.01)
        V.check(f"02→07 despesa realizada de {mes}", num(p7.cell(row=32 + j, column=5).value), num(d02), tol=0.01)
        V.check(f"02→07 resultado realizado de {mes}", num(p7.cell(row=32 + j, column=7).value), num(s02), tol=0.01)
        V.check(f"02 resultado de {mes} == receita − despesas", num(s02), num(r02) - num(d02), tol=0.01)


def checa_entre_arquivos(pasta, V, proj04, etapas04, props08, prj09, horas09):
    """O que só aparece comparando dois arquivos. É aqui que mora o valor real desta
    verificação: o cliente abre a 04, a 08 e a 09 e vê a mesma agência."""
    # 1. proposta ganha na 08 == projeto na 09, pelo mesmo valor
    ganhas = {x["prop"] + " · " + x["cli"]: x for x in props08 if x["etapa"] == "Ganha"}
    por_valor = defaultdict(list)
    for q in prj09: por_valor[q["cobrado"]].append(q)
    for chave, x in ganhas.items():
        iguais = [q for q in por_valor.get(x["valor"], []) if x["cli"] in q["nome"] or x["cli"] == q["cliente"]]
        V.check(f"08→09 proposta ganha {chave[:40]!r} é projeto na 09 pelo mesmo valor",
                len(iguais) == 1, True)
    # proposta enviada com valor também tem de existir na 09 como Proposta
    enviadas = [x for x in props08 if x["etapa"] == "Proposta enviada"]
    for x in enviadas:
        iguais = [q for q in prj09 if q["cobrado"] == x["valor"] and q["status"] == "Proposta"]
        if iguais:
            V.check(f"08→09 proposta aberta de {x['cli']!r} entra na 09 como Proposta",
                    iguais[0]["status"], "Proposta")

    # 2. os 4 projetos da 04 existem na 09 com o mesmo nome
    nomes09 = {q["nome"]: q for q in prj09}
    for q in proj04:
        V.check(f"04→09 projeto {q['nome'][:30]!r} existe na 09", q["nome"] in nomes09, True)
        if q["nome"] in nomes09:
            V.check(f"04→09 cliente de {q['nome'][:30]!r}", q["cliente"], nomes09[q["nome"]]["cliente"])
            # nenhuma hora lançada antes do início do projeto na 04
            minhas = [x["data"] for x in horas09 if x["proj"] == q["nome"]]
            if minhas:
                V.check(f"04→09 primeira hora de {q['nome'][:26]!r} não antecede o início",
                        min(minhas) >= q["ini"], True)
                # projeto concluído na 09 não tem hora depois do prazo final da 04
                if nomes09[q["nome"]]["status"] == "Concluído":
                    V.check(f"04→09 última hora de {q['nome'][:26]!r} (concluído) não passa do prazo",
                            max(minhas) <= q["fim"], True)

    # 3. o valor cobrado na 09 dos 4 projetos da 04 == valor ganho na 08
    for q in proj04:
        if q["nome"] not in nomes09: continue
        cobrado = nomes09[q["nome"]]["cobrado"]
        casa = [x for x in props08 if x["etapa"] == "Ganha" and x["valor"] == cobrado]
        V.check(f"04→08→09 {q['nome'][:26]!r} tem proposta ganha de R$ {cobrado:.0f}",
                len(casa) >= 1, True)

    # 4. as etapas da 04 e as horas da 09 falam do mesmo período
    for q in proj04:
        suas = [x["fim"] for x in etapas04 if x["proj"] == q["nome"]]
        V.check(f"04 última etapa de {q['nome'][:26]!r} == prazo final do projeto",
                max(suas) if suas else None, q["fim"])


if __name__ == "__main__":
    pasta = sys.argv[1] if len(sys.argv) > 1 else "."
    V = Verificador("Kit Completo")
    ess.checa_01(pasta, V); ess.checa_02(pasta, V); ess.checa_03(pasta, V)
    proj04, etapas04 = checa_04(pasta, V)
    checa_05(pasta, V)
    checa_06(pasta, V)
    checa_07(pasta, V)
    props08 = checa_08(pasta, V)
    prj09, horas09 = checa_09(pasta, V)
    checa_10(pasta, V)
    checa_02_x_07(pasta, V)
    checa_entre_arquivos(pasta, V, proj04, etapas04, props08, prj09, horas09)
    sys.exit(V.fim())
