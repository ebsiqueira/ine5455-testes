import unittest
from src.dinheiro import Dinheiro, Moeda, ValorMonetario

class TesteValorMonetario(unittest.TestCase):   
 
    def test_soma_com_mesma_moeda(self):
        # INLINE FIXTURE SETUP
        dez_reais = ValorMonetario(Moeda.BRL, 1000)
        vinte_reais = Dinheiro(Moeda.BRL, 20, 00)
        # EXERCISE SUT
        soma_em_reais = dez_reais.somar(vinte_reais)
        # RESULT VERIFICATION
        self.assertEqual(3000, soma_em_reais.obter_quantia().obter_quantia_em_escala())
        
    def test_subtrair_com_mesma_moeda(self):
        # INLINE FIXTURE SETUP
        vinte_reais = ValorMonetario(Moeda.BRL, 2000)
        dez_reais = Dinheiro(Moeda.BRL, 10, 00)
        # EXERCISE SUT
        subtrair_em_reais = vinte_reais.subtrair(dez_reais)
        # RESULT VERIFICATION
        self.assertEqual(1000, subtrair_em_reais.obter_quantia().obter_quantia_em_escala())
        
    def test_soma_com_moedas_diferentes(self):
        # INLINE FIXTURE SETUP
        dez_reais = ValorMonetario(Moeda.BRL, 1000)
        vinte_reais = Dinheiro(Moeda.USD, 20, 00)
        # EXERCISE SUT
        with self.assertRaises(Exception):
            soma_em_reais = dez_reais.somar(vinte_reais)
        # RESULT VERIFICATION
        
    def test_subtrair_com_resultado_negativo(self):
        # INLINE FIXTURE SETUP
        dez_reais = ValorMonetario(Moeda.BRL, 1000)
        vinte_reais = Dinheiro(Moeda.BRL, 20, 00)
        # EXERCISE SUT
        subtrair_em_reais = dez_reais.subtrair(vinte_reais)
        # RESULT VERIFICATION
        self.assertTrue(subtrair_em_reais.obter_quantia().negativo())
        self.assertEqual(1000, subtrair_em_reais.obter_quantia().obter_quantia_em_escala())

if __name__ == '__main__':
    unittest.main()
