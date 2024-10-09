from hamcrest import assert_that, equal_to, is_, not_none, has_length
from banco import Banco
from dinheiro import Moeda
import unittest

class TesteBanco(unittest.TestCase):   
 
    def setUp(self):
        self.banco = Banco("BancoDoBrasil", Moeda.BRL)
 
    def test_criar_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        self.banco.criar_agencia("Agencia 1")
        # RESULT VERIFICATION
        assert_that(self.banco.obter_agencia("Agencia 1").nome, is_(equal_to("Agencia 1")))
        
    def test_obter_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        self.banco.criar_agencia("Agencia 1")
        # EXERCISE SUT
        agencia = self.banco.obter_agencia("Agencia 1")
        # RESULT VERIFICATION
        assert_that(agencia, is_(not_none()))
        
    def test_obter_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        self.banco.criar_agencia("Agencia 1")
        self.banco.criar_agencia("Agencia 2")
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        assert_that(agencias, has_length(2)) # Sequence matcher
        assert_that(agencias[0].nome, is_(equal_to("Agencia 1")))
        assert_that(agencias[1].nome, is_(equal_to("Agencia 2")))

if __name__ == '__main__':
    unittest.main()