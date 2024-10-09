import unittest
from banco import Banco
from dinheiro import Moeda
from agencia import Agencia
from conta import Conta
from dinheiro import Dinheiro
from sistema_bancario import SistemaBancario

class TesteConta(unittest.TestCase):   
    
    def setUp(self):
        self.banco = Banco("BancoDoBrasil", Moeda.BRL)
        self.agencia = Agencia("Agencia 1", 1, self.banco)
        self.conta_eduardo = Conta("Eduardo", 1, self.agencia)
 
    def test_codigo_conta(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        identificador = self.conta_eduardo.obter_identificador()
        # RESULT VERIFICATION
        self.assertEqual("0001-7", identificador)
        
    def test_titular_conta(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        titular = self.conta_eduardo.titular
        # RESULT VERIFICATION
        self.assertEqual("Eduardo", titular)
        
    def test_transferir_dinheiro(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        conta_pedro = Conta("Pedro", 2, self.agencia)
        
        sistema_bancario = SistemaBancario()
        sistema_bancario.criar_banco(self.banco.nome, self.banco.moeda)
        sistema_bancario.depositar(conta_pedro, Dinheiro(Moeda.BRL, 10, 0))
        sistema_bancario.depositar(self.conta_eduardo, Dinheiro(Moeda.BRL, 20, 0))
        # EXERCISE SUT
        sistema_bancario.transferir(self.conta_eduardo, conta_pedro, Dinheiro(Moeda.BRL, 5, 0))
        # RESULT VERIFICATION
        self.assertEqual(1500, conta_pedro.calcular_saldo().obter_quantia().obter_quantia_em_escala())
        self.assertEqual(1500, self.conta_eduardo.calcular_saldo().obter_quantia().obter_quantia_em_escala())

if __name__ == '__main__':
    unittest.main()
