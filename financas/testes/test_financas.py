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
