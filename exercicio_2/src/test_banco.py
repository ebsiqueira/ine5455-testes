import unittest
from banco import Banco
from dinheiro import Moeda

class TesteBanco(unittest.TestCase):   
 
    def setUp(self):
        self.banco = Banco("BancoDoBrasil", Moeda.BRL)
 
    def test_criar_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.banco.criar_agencia("Agencia 1")
        # RESULT VERIFICATION
        self.assertEqual("Agencia 1", self.banco.obter_agencia("Agencia 1").nome)
        
    def test_obter_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        self.banco.criar_agencia("Agencia 1")
        # EXERCISE SUT
        agencia = self.banco.obter_agencia("Agencia 1")
        # RESULT VERIFICATION
        self.assertTrue(agencia)
        
    def test_obter_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        self.banco.criar_agencia("Agencia 1")
        self.banco.criar_agencia("Agencia 2")
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        self.assertEqual("Agencia 1", agencias[0].nome)
        self.assertEqual("Agencia 2", agencias[1].nome)

if __name__ == '__main__':
    unittest.main()
