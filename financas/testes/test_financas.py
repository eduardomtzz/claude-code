"""Testes do pipeline, com dados sinteticos -- nenhum numero real da casa."""

from __future__ import annotations

import datetime as _dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from financas.analise import analisar, montar_series
from financas.modelo import Lancamento, extrair_parcela, limpar_descricao, redigir
from financas.planilha import competencias_das_abas, numero
from financas.regras import EQUIPE, SAUDE, SEM_CATEGORIA, classificar
from financas.texto import conciliar, ler_texto, valor_brasileiro


def lanc(competencia, descricao, valor, **extra):
    item = Lancamento(competencia=competencia, descricao=descricao, valor=valor, **extra)
    return classificar(item)


class TestRedacao(unittest.TestCase):
    def test_remove_cpf_cnpj_e_telefone(self):
        self.assertNotIn("123", redigir("Fulano CPF 123.456.789-00"))
        self.assertNotIn("5499", redigir("PIX: 54994724000127"))
        self.assertNotIn("34191", redigir("34191.09636 05863.790746 10554.380005"))

    def test_preserva_texto_comum(self):
        self.assertEqual(redigir("Balet Duda"), "Balet Duda")
        self.assertEqual(redigir("Natacao (01 de 06)"), "Natacao (01 de 06)")


class TestValores(unittest.TestCase):
    def test_formato_brasileiro(self):
        self.assertEqual(valor_brasileiro("3.000,00"), 3000.0)
        self.assertEqual(valor_brasileiro("2.410"), 2410.0)
        self.assertEqual(valor_brasileiro("19.261,22"), 19261.22)

    def test_virgula_no_lugar_do_ponto(self):
        """"2,077,42" e erro de digitacao, mas o valor pretendido e claro."""
        self.assertEqual(valor_brasileiro("2,077,42"), 2077.42)

    def test_celula_da_planilha(self):
        self.assertEqual(numero("618.92999999999995"), 618.93)
        self.assertIsNone(numero("Cartao Cred"))
        self.assertIsNone(numero(""))


class TestParcelas(unittest.TestCase):
    def test_reconhece_formatos(self):
        self.assertEqual(extrair_parcela("Natacao (01 de 06)"), (1, 6))
        self.assertEqual(extrair_parcela("Projeto (02/03)"), (2, 3))
        self.assertEqual(extrair_parcela("Persianas (parc 02)"), (2, None))

    def test_ignora_pares_improvaveis(self):
        self.assertEqual(extrair_parcela("Comgas casa"), (None, None))
        self.assertEqual(extrair_parcela("MDF preto trama de 18mm"), (None, None))

    def test_limpa_o_rotulo(self):
        self.assertEqual(limpar_descricao("Natacao (01 de 06)"), "Natacao")
        self.assertEqual(limpar_descricao("Henrique (pintura Ilha)"),
                         "Henrique (pintura Ilha)")


class TestCompetencias(unittest.TestCase):
    def test_ano_avanca_quando_o_mes_retrocede(self):
        abas = ["Agosto", "Setembro", "Dezembro", "Janeiro", "Julho", "Agosto25"]
        mapa = competencias_das_abas(abas)
        self.assertEqual(mapa["Agosto"], "2024-08")
        self.assertEqual(mapa["Janeiro"], "2025-01")
        self.assertEqual(mapa["Agosto25"], "2025-08")

    def test_ano_explicito_manda(self):
        mapa = competencias_das_abas(["Marco2026", "Abril2026"])
        self.assertEqual(mapa["Marco2026"], "2026-03")

    def test_ignora_aba_sem_mes(self):
        self.assertNotIn("Contatos", competencias_das_abas(["Janeiro26", "Contatos"]))


class TestClassificacao(unittest.TestCase):
    def test_especifico_vence_generico(self):
        self.assertEqual(lanc("2026-09", "Plano de saude Leidi", 1499.46).pessoa, "Leidi")
        self.assertEqual(lanc("2026-09", "Plano de saude filho Ana", 701.8).pessoa,
                         "Filho da Ana")

    def test_encargo_vai_para_equipe(self):
        item = lanc("2026-09", "E-Social", 2793.04)
        self.assertEqual(item.categoria, EQUIPE)
        self.assertEqual(item.subcategoria, "Encargos (GPS/DAE)")

    def test_absorve_erro_de_digitacao(self):
        for grafia in ("Hipica", "Hioica", "Hipica Paulista"):
            self.assertEqual(lanc("2026-09", grafia, 1901).subcategoria, "Hípica")

    def test_aplicacao_nao_e_despesa(self):
        self.assertEqual(lanc("2026-09", "Aplicacao Victor", 1000).natureza, "poupanca")

    def test_desconhecido_fica_sem_categoria(self):
        self.assertEqual(lanc("2026-09", "Fulano de Tal", 900).categoria, SEM_CATEGORIA)


class TestSeries(unittest.TestCase):
    def test_grafias_diferentes_viram_uma_serie(self):
        series = montar_series([
            lanc("2026-05", "Akuguel e IPTU", 19261.22),
            lanc("2026-06", "Aluguel e IPTU", 19261.22),
            lanc("2026-07", "Aluguel / IPTU", 19261.22),
        ])
        self.assertEqual(len(series), 1)
        self.assertEqual(len(series[0].por_mes), 3)

    def test_grafia_dominante_nomeia_a_serie(self):
        series = montar_series(
            [lanc(f"2026-0{m}", "Paula - assistente", 5000) for m in range(1, 7)]
            + [lanc("2026-07", "Paula", 5000)]
        )
        self.assertEqual(series[0].rotulo, "Paula - assistente")

    def test_fixo_e_variavel(self):
        meses = [f"2026-0{m}" for m in range(1, 7)]
        fixo = montar_series([lanc(m, "Claro", 411.57) for m in meses])[0]
        variavel = montar_series(
            [lanc(m, "Comgas casa", 100 + i * 220) for i, m in enumerate(meses)]
        )[0]
        self.assertEqual(fixo.tipo_em(meses), "fixo")
        self.assertEqual(variavel.tipo_em(meses), "recorrente variavel")

    def test_falha_meses_e_eventual(self):
        meses = [f"2026-0{m}" for m in range(1, 7)]
        serie = montar_series([lanc("2026-01", "Dentista", 800),
                               lanc("2026-04", "Dentista", 800)])[0]
        self.assertEqual(serie.tipo_em(meses), "eventual")


class TestTexto(unittest.TestCase):
    CONTROLE = """SETEMBRO

PAGAMENTOS PIX - DIA 1 DO MES

- Adriano Jardineiro R$ 600,00
PIX: 11974226896

-Lory R$ 600,00
2 dias / R$ 300
PIX: 34217780869

PAGAMENTOS BOLETO - DIA 1 DO MES

- Claro R$ 411,57
84870000004-1 11570162202-9 60901173208-5 46005621123-5
"""

    def test_le_itens_e_formas(self):
        leitura = ler_texto(self.CONTROLE, "2026-09")
        self.assertEqual(len(leitura.lancamentos), 3)
        formas = {l.descricao: l.forma for l in leitura.lancamentos}
        self.assertEqual(formas["Adriano Jardineiro"], "pix")
        self.assertEqual(formas["Claro"], "boleto")

    def test_continuacao_nao_vira_lancamento(self):
        leitura = ler_texto(self.CONTROLE, "2026-09")
        self.assertNotIn(300.0, [l.valor for l in leitura.lancamentos])

    def test_nao_guarda_identificador(self):
        leitura = ler_texto(self.CONTROLE, "2026-09")
        texto = " ".join(l.descricao + l.observacao for l in leitura.lancamentos)
        self.assertNotIn("11974226896", texto)
        self.assertNotIn("84870000004", texto)

    def test_sem_linhas_perdidas(self):
        self.assertEqual(ler_texto(self.CONTROLE, "2026-09").ignoradas, [])


class TestConciliacao(unittest.TestCase):
    def test_encontra_o_par_com_nome_diferente(self):
        divergencias = conciliar(
            [lanc("2026-09", "Deposito Victor", 1000)],
            [lanc("2026-09", "Aplicacao Victor", 1000)],
        )
        self.assertEqual(divergencias, [])

    def test_aponta_o_que_falta_na_planilha(self):
        divergencias = conciliar(
            [lanc("2026-09", "Convenio Marcia", 2410)],
            [],
        )
        self.assertEqual([d.tipo for d in divergencias], ["so_no_texto"])
        self.assertEqual(divergencias[0].valor_texto, 2410)

    def test_aponta_valor_diferente(self):
        divergencias = conciliar(
            [lanc("2026-09", "Claro", 411.57)],
            [lanc("2026-09", "Claro", 413.60)],
        )
        self.assertEqual(divergencias[0].tipo, "valor_diferente")
        self.assertAlmostEqual(divergencias[0].diferenca, -2.03, places=2)


class TestAnalise(unittest.TestCase):
    def test_janela_ignora_o_mes_corrente(self):
        lancamentos = [lanc(f"2026-{m:02d}", "Claro", 411.57) for m in range(1, 10)]
        analise = analisar(lancamentos, _dt.date(2026, 9, 16))
        self.assertNotIn("2026-09", analise.janela)
        self.assertEqual(analise.janela[-1], "2026-08")

    def test_mes_futuro_e_previsao(self):
        lancamentos = [lanc("2026-09", "Claro", 411.57), lanc("2026-10", "Claro", 411.57)]
        analise = analisar(lancamentos, _dt.date(2026, 9, 16))
        self.assertEqual(analise.previstas, ["2026-10"])

    def test_poupanca_fica_fora_da_renegociacao(self):
        lancamentos = [lanc(f"2026-{m:02d}", "Aplicacao Victor", 5000)
                       for m in range(1, 10)]
        analise = analisar(lancamentos, _dt.date(2026, 9, 16))
        titulos = " ".join(o.titulo for o in analise.oportunidades)
        self.assertNotIn("Aplicacao", titulos)


if __name__ == "__main__":
    unittest.main(verbosity=2)


class TestBaseline(unittest.TestCase):
    """O baseline responde "quanto sai no mes que vem sem eu decidir nada"."""

    def _base(self, extra=None):
        from financas import baseline
        meses = [f"2026-{m:02d}" for m in range(5, 10)]
        lancamentos = [lanc(m, "Claro", 411.57) for m in meses]
        lancamentos += [lanc(m, "Salario Ana", 5025) for m in meses]
        lancamentos += [lanc("2026-05", "Dentista", 900),
                        lanc("2026-08", "Dentista", 900)]
        lancamentos += extra or []
        analise = analisar(lancamentos, _dt.date(2026, 9, 16))
        return baseline.montar(analise, regime_inicio="2026-05")

    def test_piso_soma_o_que_se_repete(self):
        base = self._base()
        rotulos = {c.rotulo for c in base.comprometidos}
        self.assertIn("Claro", rotulos)
        self.assertIn("Salario Ana", rotulos)
        self.assertAlmostEqual(base.piso, 5436.57, places=2)

    def test_esporadico_fica_fora_do_piso(self):
        base = self._base()
        self.assertNotIn("Dentista", {c.rotulo for c in base.comprometidos})

    def test_anual_entra_como_provisao_rateada(self):
        base = self._base([lanc("2026-01", "13 Salario Ana", 12000)])
        provisoes = {c.rotulo: c.valor for c in base.sazonais}
        self.assertIn("13 Salario Ana", provisoes)
        self.assertAlmostEqual(provisoes["13 Salario Ana"], 1000.0, places=2)

    def test_nada_e_contado_duas_vezes(self):
        base = self._base()
        chaves = [(c.categoria, c.subcategoria, c.pessoa)
                  for c in base.comprometidos + base.variaveis + base.sazonais]
        self.assertEqual(len(chaves), len(set(chaves)))

    def test_poupanca_aparece_separada_dentro_do_piso(self):
        meses = [f"2026-{m:02d}" for m in range(5, 10)]
        base = self._base([lanc(m, "Aplicacao Victor", 1000) for m in meses])
        self.assertAlmostEqual(base.poupanca, 1000.0, places=2)
        self.assertGreater(base.piso, base.poupanca)


def pdf_sintetico(linhas: list[str]) -> bytes:
    """Monta um PDF minimo com uma pagina de texto, para testar o extrator."""
    import zlib

    corpo = ["BT /F1 9 Tf"]
    for i, linha in enumerate(linhas):
        texto = linha.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")
        corpo.append(f"1 0 0 1 40 {700 - i * 14} Tm ({texto}) Tj")
    corpo.append("ET")
    fluxo = zlib.compress("\n".join(corpo).encode("latin-1"))

    objetos = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /Resources << /Font << /F1 5 0 R >> >>"
        b" /Contents 4 0 R >>",
        b"<< /Length %d /Filter /FlateDecode >>\nstream\n" % len(fluxo)
        + fluxo + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    saida = b"%PDF-1.5\n"
    for numero, objeto in enumerate(objetos, 1):
        saida += b"%d 0 obj\n" % numero + objeto + b"\nendobj\n"
    return saida + b"trailer << /Root 1 0 R >>\n%%EOF"


class TestPDF(unittest.TestCase):
    def test_le_as_linhas_na_ordem(self):
        from financas.pdf import DocumentoPDF

        doc = DocumentoPDF(pdf_sintetico(["primeira linha", "segunda linha"]))
        self.assertEqual(doc.linhas()[0], ["primeira linha", "segunda linha"])

    def test_recusa_arquivo_que_nao_e_pdf(self):
        from financas.pdf import DocumentoPDF, ErroDePDF

        with self.assertRaises(ErroDePDF):
            DocumentoPDF(b"isto nao e um pdf")


class TestFatura(unittest.TestCase):
    LINHAS = [
        "Total de fatura Vencimento",
        "R$ 1.234,56 15 /09 /2026",
        "Numero do Cartao 4271 XXXX XXXX 5902",
        "(+)Compras/Debitos............R$ 1.234,56",
        "Total para as proximas faturas R$ 9.000,00",
        "Data Historico de Lancamentos Cidade US$ R$",
        "02/09 SUPERMERCADO SAO PAULO 234,56",
        "03/09 DROGARIA 05/10 SAO PAULO 100,00",
        "04/09 HOTEL EM MIAMI USD 100,00 MIAMI 100,00 5,4400 544,00",
        "05/09 AJUSTE A CREDITO 50,00 -",
        "06/09 PAG BOLETO BANCARIO 800,00 -",
        "07/09 ESCOLA PARTICULAR SAO PAULO 356,00",
    ]

    def _fatura(self):
        import tempfile
        from financas import fatura

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as arquivo:
            arquivo.write(pdf_sintetico(self.LINHAS))
            caminho = arquivo.name
        return fatura.ler(caminho)

    def test_le_cabecalho(self):
        f = self._fatura()
        self.assertEqual(f.competencia, "2026-09")
        self.assertEqual(f.cartao, "Visa final 5902")
        self.assertAlmostEqual(f.parcelado_futuro, 9000.0, places=2)

    def test_soma_bate_com_o_declarado(self):
        """A conferencia e o que separa uma leitura certa de uma plausivel."""
        f = self._fatura()
        self.assertTrue(f.confere, f"diferenca de {f.diferenca}")

    def test_compra_internacional_usa_o_valor_em_real(self):
        f = self._fatura()
        hotel = [l for l in f.lancamentos if "HOTEL" in l.descricao][0]
        self.assertAlmostEqual(hotel.valor, 544.0, places=2)

    def test_credito_nao_entra_como_compra(self):
        f = self._fatura()
        descricoes = " ".join(l.descricao for l in f.lancamentos)
        self.assertNotIn("AJUSTE", descricoes)
        self.assertNotIn("BOLETO", descricoes)
        self.assertEqual(len(f.creditos), 2)

    def test_reconhece_a_parcela(self):
        f = self._fatura()
        drogaria = [l for l in f.lancamentos if "DROGARIA" in l.descricao][0]
        self.assertEqual((drogaria.parcela, drogaria.parcela_total), (5, 10))


class TestParcelas(unittest.TestCase):
    def _parcelamentos(self, faturas):
        from financas import parcelas
        return parcelas.em_curso(faturas)

    def _fatura(self, cartao, competencia, itens):
        from financas.fatura import Fatura
        f = Fatura(arquivo="x.pdf", cartao=cartao, competencia=competencia)
        for descricao, valor, numero, total in itens:
            l = lanc(competencia, descricao, valor, forma="cartao")
            l.parcela, l.parcela_total = numero, total
            f.lancamentos.append(l)
        return f

    def test_conta_so_a_ultima_fatura_de_cada_cartao(self):
        """A mesma parcela aparece em toda fatura ate acabar."""
        faturas = [
            self._fatura("Visa", "2026-08", [("LOJA 02/04", 100.0, 2, 4)]),
            self._fatura("Visa", "2026-09", [("LOJA 03/04", 100.0, 3, 4)]),
        ]
        ps = self._parcelamentos(faturas)
        self.assertEqual(len(ps), 1)
        self.assertEqual(ps[0].restantes, 1)

    def test_cartao_substituido_nao_conta_duas_vezes(self):
        faturas = [
            self._fatura("Visa antigo", "2026-07", [("LOJA 01/04", 100.0, 1, 4)]),
            self._fatura("Visa novo", "2026-09", [("LOJA 03/04", 100.0, 3, 4)]),
        ]
        ps = self._parcelamentos(faturas)
        self.assertEqual([p.cartao for p in ps], ["Visa novo"])

    def test_cronograma_espalha_pelas_competencias(self):
        from financas import parcelas
        faturas = [self._fatura("Visa", "2026-09", [("LOJA 01/03", 100.0, 1, 3)])]
        crono = parcelas.cronograma(self._parcelamentos(faturas))
        self.assertEqual([c for c, _, _ in crono], ["2026-10", "2026-11"])
        self.assertEqual([v for _, v, _ in crono], [100.0, 100.0])

    def test_parcela_encerrada_nao_e_compromisso(self):
        faturas = [self._fatura("Visa", "2026-09", [("LOJA 04/04", 100.0, 4, 4)])]
        self.assertEqual(self._parcelamentos(faturas), [])
