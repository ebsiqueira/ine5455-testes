import unittest
from banco import Banco
from agencia import Agencia
from dinheiro import Moeda

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
        self.assertEqual("001", identificador)
        
    def test_banco_agencia(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # EXERCISE SUT
        banco_da_agencia = agencia.banco
        # RESULT VERIFICATION
        self.assertEqual("BancoDoBrasil", banco_da_agencia.nome)
        
    def test_criar_conta(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # EXERCISE SUT
        conta = agencia.criar_conta("Eduardo")
        # RESULT VERIFICATION
        self.assertEqual("Eduardo", conta.titular)
        
    def test_obter_conta(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # INLINE FIXTURE SETUP
        agencia.criar_conta("Eduardo")
        # EXERCISE SUT
        conta = agencia.obter_conta("0001-7")
        # RESULT VERIFICATION
        self.assertEqual("Eduardo", conta.titular)
        
    def test_obter_contas(self):
        # DELEGATED FIXTURE SETUP
        agencia = TestHelper.criar_banco(self)
        # INLINE FIXTURE SETUP
        agencia.criar_conta("Eduardo")
        agencia.criar_conta("Pedro")
        # EXERCISE SUT
        contas = agencia.obter_contas()
        # RESULT VERIFICATION
        self.assertEqual("Eduardo", contas[0].titular)
        self.assertEqual("Pedro", contas[1].titular)

if __name__ == '__main__':
    unittest.main()
