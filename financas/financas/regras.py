"""Taxonomia de categorias e regras de classificacao dos lancamentos.

As regras sao avaliadas em ordem: a primeira que casar vence. Por isso o que e
mais especifico ("plano de saude leidi") vem antes do que e mais generico
("plano de saude"). O casamento e feito sobre a forma canonica da descricao
(minuscula, sem acento, sem pontuacao), o que absorve boa parte dos erros de
digitacao da planilha.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .modelo import Lancamento, chave, limpar_descricao

# --------------------------------------------------------------------------
# Categorias
# --------------------------------------------------------------------------

MORADIA = "Moradia"
CONTAS = "Contas da casa"
SEGURANCA = "Segurança"
EQUIPE = "Equipe doméstica"
EDUCACAO = "Educação"
ATIVIDADES = "Atividades e esportes"
SAUDE = "Saúde"
ALIMENTACAO = "Alimentação"
SERVICOS = "Serviços da casa"
MANUTENCAO = "Manutenção e reformas"
PETS = "Pets"
VEICULOS = "Veículos"
IMPOSTOS = "Impostos e taxas"
FINANCEIRO = "Financeiro"
JURIDICO = "Jurídico e contábil"
LAZER = "Lazer, festas e presentes"
TRABALHO = "Trabalho"
AVULSOS = "Avulsos"
SEM_CATEGORIA = "Não classificado"

#: Ordem de exibicao no painel.
CATEGORIAS = [
    MORADIA, EQUIPE, EDUCACAO, SAUDE, FINANCEIRO, ATIVIDADES, CONTAS,
    SERVICOS, SEGURANCA, JURIDICO, MANUTENCAO, ALIMENTACAO, VEICULOS,
    IMPOSTOS, LAZER, PETS, TRABALHO, AVULSOS, SEM_CATEGORIA,
]

# --------------------------------------------------------------------------
# Pessoas
# --------------------------------------------------------------------------

CASA = "Casa"

#: pessoa -> papel. Usado para separar filhos de equipe no painel.
PAPEIS = {
    "Eduarda": "filha",
    "Victor": "filho",
    "Eduardo": "titular",
    "Leidi": "equipe",
    "Ana": "equipe",
    "Paula": "equipe",
    "Fran": "equipe",
    "Lori": "equipe",
    "Regiane": "equipe",
    "Pais": "pais",
    "Guilherme": "familiar de equipe",
    "Filha da Leidi": "familiar de equipe",
    "Filho da Ana": "familiar de equipe",
    CASA: "casa",
}


@dataclass(frozen=True)
class Regra:
    padrao: str
    categoria: str
    subcategoria: str = ""
    pessoa: str = CASA
    natureza: str = "despesa"

    def casa_com(self, texto: str) -> bool:
        return re.search(self.padrao, texto) is not None


# As regras usam a descricao ja canonizada: minuscula, sem acento e sem
# pontuacao. "Balet Duda (01 de 03)" vira "balet duda 01 de 03".
REGRAS: list[Regra] = [
    # ---- Equipe domestica: encargos, beneficios e verbas ------------------
    Regra(r"\bgps\b|\bdae\b|e social|esocial", EQUIPE, "Encargos (GPS/DAE)"),
    Regra(r"rescisao leidi", EQUIPE, "Rescisão", "Leidi"),
    Regra(r"rescisao ana|rescisao anna", EQUIPE, "Rescisão", "Ana"),
    Regra(r"(13|decimo).*(leidi)|leidi.*13", EQUIPE, "13º e férias", "Leidi"),
    Regra(r"(13|decimo).*(ana|anna)|ann?a.*13", EQUIPE, "13º e férias", "Ana"),
    Regra(r"(13|decimo).*paula|paula.*13", EQUIPE, "13º e férias", "Paula"),
    Regra(r"fran.*13|13.*fran", EQUIPE, "13º e férias", "Fran"),
    Regra(r"ferias leidi", EQUIPE, "13º e férias", "Leidi"),
    Regra(r"ferias ana|ferias anna", EQUIPE, "13º e férias", "Ana"),
    Regra(r"vale ceia leidi", EQUIPE, "Benefícios", "Leidi"),
    Regra(r"vale ceia ana", EQUIPE, "Benefícios", "Ana"),
    Regra(r"plano de saude leidi filha", EQUIPE, "Benefícios", "Filha da Leidi"),
    Regra(r"plano de saude leidi", EQUIPE, "Benefícios", "Leidi"),
    Regra(r"plano de saude (ana )?(filho|2)\b|plano de saude filho ana",
          EQUIPE, "Benefícios", "Filho da Ana"),
    Regra(r"plano de saude ana", EQUIPE, "Benefícios", "Ana"),
    Regra(r"escola guilherme", EQUIPE, "Benefícios", "Guilherme"),
    Regra(r"adiantamento ana|extra ana", EQUIPE, "Salários", "Ana"),
    Regra(r"salario\s*leidi|leidi mensal", EQUIPE, "Salários", "Leidi"),
    Regra(r"salario\s*(ana|anna)|ana mensal", EQUIPE, "Salários", "Ana"),
    Regra(r"\bpaula\b", EQUIPE, "Prestadores", "Paula"),
    Regra(r"\bfran\b", EQUIPE, "Prestadores", "Fran"),
    Regra(r"\blor[iy]\b", EQUIPE, "Prestadores", "Lori"),
    Regra(r"regiane", EQUIPE, "Prestadores", "Regiane"),
    Regra(r"copeira|passadeira", EQUIPE, "Prestadores"),

    # ---- Moradia ---------------------------------------------------------
    Regra(r"a?[kl]uguel.*iptu|aluguel e iptu", MORADIA, "Aluguel e IPTU"),
    Regra(r"\baluguel\b(?!.*brinquedo)", MORADIA, "Aluguel e IPTU"),
    Regra(r"condominio", MORADIA, "Condomínio"),
    Regra(r"extra apto", MORADIA, "Apartamento"),
    Regra(r"\biptu\b", MORADIA, "IPTU"),

    # ---- Contas da casa --------------------------------------------------
    Regra(r"comgas", CONTAS, "Gás"),
    Regra(r"\benel\b", CONTAS, "Energia"),
    Regra(r"sabesp", CONTAS, "Água"),
    Regra(r"\bnet\b", CONTAS, "Internet e TV"),
    Regra(r"claro", CONTAS, "Telefonia"),

    # ---- Seguranca -------------------------------------------------------
    Regra(r"elite|camera", SEGURANCA, "Câmeras"),
    Regra(r"peter graber|monitoramento", SEGURANCA, "Monitoramento"),
    Regra(r"\bvgm\b|seguranca rua|vigilancia", SEGURANCA, "Vigilância da rua"),

    # ---- Educacao --------------------------------------------------------
    Regra(r"escola eduarda", EDUCACAO, "Escola", "Eduarda"),
    Regra(r"escola victor|escola vitor", EDUCACAO, "Escola", "Victor"),
    Regra(r"matricula", EDUCACAO, "Matrícula"),
    Regra(r"formatura duda|formatura eduarda", EDUCACAO, "Formatura", "Eduarda"),
    Regra(r"aula de reforco|reforco duda", EDUCACAO, "Reforço escolar", "Eduarda"),
    Regra(r"\bescola\b|\bcolegio\b", EDUCACAO, "Escola"),

    # ---- Atividades e esportes ------------------------------------------
    Regra(r"balet|ballet", ATIVIDADES, "Balé", "Eduarda"),
    Regra(r"apresentacao", ATIVIDADES, "Apresentações", "Eduarda"),
    Regra(r"teatro vitor|teatro victor", ATIVIDADES, "Teatro", "Victor"),
    Regra(r"futebol", ATIVIDADES, "Futebol", "Victor"),
    Regra(r"natacao", ATIVIDADES, "Natação"),
    Regra(r"hi[po]ica", ATIVIDADES, "Hípica"),
    Regra(r"aula de surfe|aula skate", ATIVIDADES, "Surfe e skate"),

    # ---- Saude -----------------------------------------------------------
    Regra(r"dr vi[ck]tor|dr viktor", SAUDE, "Dr Viktor", "Eduardo"),
    Regra(r"nott?o", SAUDE, "Saúde mental", "Eduardo"),
    Regra(r"dra marcela", SAUDE, "Dra Marcela"),
    Regra(r"\bfono\b", SAUDE, "Fonoaudiologia", "Victor"),
    Regra(r"dentista victor e duda", SAUDE, "Dentista"),
    Regra(r"dentista", SAUDE, "Dentista"),
    Regra(r"oftalmo", SAUDE, "Oftalmologia"),
    Regra(r"fisioter", SAUDE, "Fisioterapia"),
    Regra(r"plano de saude familia", SAUDE, "Plano de saúde da família"),
    Regra(r"convenio", SAUDE, "Convênio dos pais", "Pais"),
    Regra(r"plano de saude", SAUDE, "Plano de saúde"),

    # ---- Financeiro ------------------------------------------------------
    Regra(r"consorcio", FINANCEIRO, "Consórcio"),
    Regra(r"aplicacao eduarda|deposito eduarda", FINANCEIRO, "Aplicação dos filhos", "Eduarda", "poupanca"),
    Regra(r"aplicacao victor|deposito victor", FINANCEIRO, "Aplicação dos filhos", "Victor", "poupanca"),
    Regra(r"\bz2\b", FINANCEIRO, "Aporte na empresa (Z2)"),

    # ---- Juridico e contabil --------------------------------------------
    Regra(r"alisson|advogad", JURIDICO, "Advogados"),
    Regra(r"\birpf\b|gaap|corpservice", JURIDICO, "Contabilidade e IRPF"),
    Regra(r"realiza", JURIDICO, "Contabilidade e IRPF"),

    # ---- Veiculos e impostos --------------------------------------------
    Regra(r"\bipva\b", VEICULOS, "IPVA"),
    Regra(r"multa", VEICULOS, "Multas"),
    Regra(r"conserto audi|cadeira extra carro", VEICULOS, "Manutenção"),
    Regra(r"taxa certificado", IMPOSTOS, "Taxas"),

    # ---- Servicos da casa ------------------------------------------------
    Regra(r"piscineiro|capa piscina", SERVICOS, "Piscina"),
    Regra(r"jardineiro", SERVICOS, "Jardim"),
    Regra(r"lavanderia|lavagem (sofa|tapete)", SERVICOS, "Lavanderia"),
    Regra(r"enjoy house", SERVICOS, "Enjoy House"),
    Regra(r"dedetiza", SERVICOS, "Dedetização"),
    Regra(r"limpeza iporanga|vistoria casa", SERVICOS, "Avulsos"),

    # ---- Manutencao e reformas ------------------------------------------
    Regra(r"conserto|ajuste portao|manutencao|reparo", MANUTENCAO, "Consertos"),
    Regra(r"pintura|p[ni]tura|tinta", MANUTENCAO, "Pintura"),
    Regra(r"armario|persian|persina|esquadria|\bmdf\b", MANUTENCAO, "Marcenaria"),
    Regra(r"climatiza|aquecedor", MANUTENCAO, "Climatização"),
    Regra(r"\bprojeto\b", MANUTENCAO, "Projeto"),

    # ---- Alimentacao -----------------------------------------------------
    Regra(r"cesta organica|spazio|santa adelaide|hortifruti", ALIMENTACAO, "Orgânicos e hortifruti"),
    Regra(r"peixe|carne", ALIMENTACAO, "Açougue e peixaria"),
    Regra(r"biscoito|docinho|doces|bolo", ALIMENTACAO, "Encomendas"),

    # ---- Pets ------------------------------------------------------------
    Regra(r"\bpets?\b|veterinar|foxvet", PETS, "Pets"),

    # ---- Lazer, festas e presentes --------------------------------------
    Regra(r"presente", LAZER, "Presentes"),
    Regra(r"recreacao|palhaco|animador|fotografo|brinquedo|make e penteado",
          LAZER, "Festas"),
    Regra(r"bar da|aeroporto|viagem", LAZER, "Lazer e viagens"),

    # ---- Trabalho --------------------------------------------------------
    Regra(r"regus", TRABALHO, "Escritório", "Eduardo"),
]


def classificar(lancamento: Lancamento) -> Lancamento:
    """Preenche categoria, subcategoria, pessoa e natureza do lancamento."""
    texto = chave(lancamento.descricao)
    for regra in REGRAS:
        if regra.casa_com(texto):
            lancamento.categoria = regra.categoria
            lancamento.subcategoria = regra.subcategoria or regra.categoria
            lancamento.pessoa = regra.pessoa
            lancamento.natureza = regra.natureza
            return lancamento
    # Sem regra que case, o proprio nome do pagamento vira a subcategoria: e o
    # unico rotulo que existe, e e o que mantem cada pendencia separada das
    # outras em vez de somar todas num "nao classificado" anonimo.
    lancamento.categoria = SEM_CATEGORIA
    lancamento.subcategoria = limpar_descricao(lancamento.descricao)
    lancamento.pessoa = CASA
    return lancamento


#: Ate quantos meses distintos um pagamento sem regra pode aparecer e ainda
#: ser considerado avulso, e nao um recorrente que falta mapear.
MESES_PARA_SER_AVULSO = 2


def marcar_avulsos(lancamentos: list[Lancamento]) -> list[Lancamento]:
    """Separa o gasto de uma vez so do recorrente que falta mapear.

    Um pagamento sem regra que aparece em um ou dois meses da base inteira e
    um avulso: entra no total, mas nao no piso mensal. Um que se repete mes a
    mes sem regra e uma lacuna da taxonomia, e continua marcado como nao
    classificado para ser resolvido.
    """
    meses: dict[str, set[str]] = {}
    for l in lancamentos:
        if l.categoria == SEM_CATEGORIA:
            meses.setdefault(chave(l.rotulo), set()).add(l.competencia)
    for l in lancamentos:
        if l.categoria != SEM_CATEGORIA:
            continue
        if len(meses.get(chave(l.rotulo), ())) <= MESES_PARA_SER_AVULSO:
            l.categoria = AVULSOS
    return lancamentos


def classificar_todos(lancamentos: list[Lancamento]) -> list[Lancamento]:
    return marcar_avulsos([classificar(l) for l in lancamentos])


def papel_de(pessoa: str) -> str:
    return PAPEIS.get(pessoa, "casa")
