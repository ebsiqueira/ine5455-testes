from hamcrest import assert_that, equal_to, is_, instance_of, contains_string
from src.dinheiro import Dinheiro, Moeda, ValorMonetario
import unittest

class TesteDinheiro(unittest.TestCase): 
    def test_quantia_em_escala_de_um_real_e_um_centavo(self):
        # INLINE FIXTURE SETUP
        um_real_e_um_centavo = Dinheiro(Moeda.BRL, 1, 1)
        # EXERCISE SUT
        quantia_em_escala = um_real_e_um_centavo.obter_quantia_em_escala()
        # RESULT VERIFICATION
        assert_that(quantia_em_escala, is_(equal_to(101)))

    def test_negativo_50_reais(self):
        # INLINE FIXTURE SETUP
        cinquenta_reais = Dinheiro(Moeda.BRL, 50, 0)
        # EXERCISE SUT
        valor_cinquenta_negativo = cinquenta_reais.negativo()
        # RESULT VERIFICATION
        assert_that(valor_cinquenta_negativo, instance_of(ValorMonetario)) # Object matcher
        assert_that(valor_cinquenta_negativo.negativo(), is_(True))
        assert_that(int(valor_cinquenta_negativo.obter_quantia().obter_quantia_em_escala()), is_(equal_to(5000)))

    def test_moeda_50_reais(self):
        # INLINE FIXTURE SETUP
        cinquenta_reais = Dinheiro(Moeda.BRL, 50, 0)
        # EXERCISE SUT
        moeda_cinquenta_reais = cinquenta_reais.moeda
        # RESULT VERIFICATION
        assert_that(moeda_cinquenta_reais.simbolo(), contains_string("R$")) # Text matcher

    def test_formatar_50_reais_com_moeda(self):
        # INLINE FIXTURE SETUP
        cinquenta_reais = Dinheiro(Moeda.BRL, 50, 0)
        # EXERCISE SUT
        valor_cinquenta_formatado = cinquenta_reais.formatar_com_moeda()
        # RESULT VERIFICATION
        assert_that(valor_cinquenta_formatado, is_(equal_to("50,00 BRL")))

    def test_se_eh_zero_reais(self):
        # INLINE FIXTURE SETUP
        zero_reais = Dinheiro(Moeda.BRL, 0, 0)
        # EXERCISE SUT
        valor_zero = zero_reais.zero()
        # RESULT VERIFICATION
        assert_that(valor_zero, is_(True))
        
if __name__ == '__main__':
    unittest.main()