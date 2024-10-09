from hamcrest import assert_that, equal_to, is_, has_item
from banco import Banco
from agencia import Agencia
from dinheiro import Moeda
import unittest

class TestHelper:
    
    def criar_banco(self):
        banco = Banco("BancoDoBrasil", Moeda.BRL)
        agencia = Agencia("Agencia 1", 1, banco)
        return agencia
        

class TesteAgencia(unittest.TestCase):   
 
    def test_codigo_agencia(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # EXERCISE SUT
        identificador = agencia.obter_identificador()
        # RESULT VERIFICATION
        assert_that(identificador, is_(equal_to("001")))
        
    def test_banco_agencia(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # EXERCISE SUT
        banco_da_agencia = agencia.banco
        # RESULT VERIFICATION
        assert_that(banco_da_agencia.nome, is_(equal_to("BancoDoBrasil")))
        
    def test_criar_conta(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # EXERCISE SUT
        conta = agencia.criar_conta("Eduardo")
        # RESULT VERIFICATION
        assert_that(conta.titular, is_(equal_to("Eduardo")))
        
    def test_obter_conta(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # INLINE FIXTURE SETUP
        agencia.criar_conta("Eduardo")
        # EXERCISE SUT
        conta = agencia.obter_conta("0001-7")
        # RESULT VERIFICATION
        assert_that(conta.titular, is_(equal_to("Eduardo")))
        
    def test_obter_contas(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # INLINE FIXTURE SETUP
        agencia.criar_conta("Eduardo")
        agencia.criar_conta("Pedro")
        # EXERCISE SUT
        contas = agencia.obter_contas()
        # RESULT VERIFICATION
        assert_that(contas, has_item(contas[0])) # Sequence matcher
        assert_that(contas[0].titular, is_(equal_to("Eduardo")))
        assert_that(contas[1].titular, is_(equal_to("Pedro")))

if __name__ == '__main__':
    unittest.main() 