from hamcrest import assert_that, equal_to, is_, raises, calling, greater_than
from src.dinheiro import Dinheiro, Moeda, ValorMonetario
import unittest

class TesteValorMonetario(unittest.TestCase):   
 
    def test_soma_com_mesma_moeda(self):
        # INLINE FIXTURE SETUP
        dez_reais = ValorMonetario(Moeda.BRL, 1000)
        vinte_reais = Dinheiro(Moeda.BRL, 20, 00)
        # EXERCISE SUT
        soma_em_reais = dez_reais.somar(vinte_reais)
        # RESULT VERIFICATION
        assert_that(soma_em_reais.obter_quantia().obter_quantia_em_escala(), is_(equal_to(3000)))
        
    def test_subtrair_com_mesma_moeda(self):
        # INLINE FIXTURE SETUP
        vinte_reais = ValorMonetario(Moeda.BRL, 2000)
        dez_reais = Dinheiro(Moeda.BRL, 10, 00)
        # EXERCISE SUT
        subtrair_em_reais = vinte_reais.subtrair(dez_reais)
        # RESULT VERIFICATION
        assert_that(subtrair_em_reais.obter_quantia().obter_quantia_em_escala(), is_(equal_to(1000)))
        
    def test_soma_com_moedas_diferentes(self):
        # INLINE FIXTURE SETUP
        dez_reais = ValorMonetario(Moeda.BRL, 1000)
        vinte_reais = Dinheiro(Moeda.USD, 20, 00)
        # EXERCISE SUT
        assert_that(calling(dez_reais.somar).with_args(vinte_reais), raises(Exception))
        # RESULT VERIFICATION
        
    def test_subtrair_com_resultado_negativo(self):
        # INLINE FIXTURE SETUP
        dez_reais = ValorMonetario(Moeda.BRL, 1000)
        vinte_reais = Dinheiro(Moeda.BRL, 20, 00)
        # EXERCISE SUT
        subtrair_em_reais = dez_reais.subtrair(vinte_reais)
        # RESULT VERIFICATION
        assert_that(subtrair_em_reais.obter_quantia().obter_quantia_em_escala(), is_(greater_than(0))) # Number matcher

if __name__ == '__main__':
    unittest.main() 