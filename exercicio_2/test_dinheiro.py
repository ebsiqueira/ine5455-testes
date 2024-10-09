import unittest
from src.dinheiro import Dinheiro, Moeda

class TesteDinheiro(unittest.TestCase): 
 
    def test_quantia_em_escala_de_um_real_e_um_centavo(self):
        # INLINE FIXTURE SETUP
        um_real_e_um_centavo = Dinheiro(Moeda.BRL, 1, 1)
        # EXERCISE SUT
        quantia_em_escala = um_real_e_um_centavo.obter_quantia_em_escala()
        # RESULT VERIFICATION
        self.assertEqual(101, quantia_em_escala)
 
    def test_negativo_50_reais(self):
        # INLINE FIXTURE SETUP
        cinquenta_reais = Dinheiro(Moeda.BRL, 50, 0)
        # EXERCISE SUT
        valor_cinquenta_negativo = cinquenta_reais.negativo()
        # RESULT VERIFICATION
        self.assertTrue(valor_cinquenta_negativo.negativo())
        self.assertEqual(5000, int(valor_cinquenta_negativo.obter_quantia().obter_quantia_em_escala()))
        
    def test_moeda_50_reais(self):
        # INLINE FIXTURE SETUP
        cinquenta_reais = Dinheiro(Moeda.BRL, 50, 0)
        # EXERCISE SUT
        moeda_cinquenta_reais = cinquenta_reais.moeda
        # RESULT VERIFICATION
        self.assertEqual("R$", moeda_cinquenta_reais.simbolo())
        
    def test_formatar_50_reais_com_moeda(self):
        # INLINE FIXTURE SETUP
        cinquenta_reais = Dinheiro(Moeda.BRL, 50, 0)
        # EXERCISE SUT
        valor_cinquenta_formatado = cinquenta_reais.formatar_com_moeda()
        # RESULT VERIFICATION
        self.assertEqual("50,00 BRL", valor_cinquenta_formatado)
        
    def test_se_eh_zero_reais(self):
        # INLINE FIXTURE SETUP
        zero_reais = Dinheiro(Moeda.BRL, 0, 0)
        # EXERCISE SUT
        valor_zero = zero_reais.zero()
        # RESULT VERIFICATION
        self.assertTrue(valor_zero)

if __name__ == '__main__':
    unittest.main()
