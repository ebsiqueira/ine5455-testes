from hamcrest import assert_that, equal_to, is_, all_of, greater_than
from banco import Banco
from dinheiro import Moeda
from agencia import Agencia
from conta import Conta
from dinheiro import Dinheiro
from sistema_bancario import SistemaBancario
import unittest

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
        assert_that(identificador, is_(equal_to("0001-7")))
        
    def test_titular_conta(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        titular = self.conta_eduardo.titular
        # RESULT VERIFICATION
        assert_that(titular, is_(equal_to("Eduardo")))
        
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
        assert_that(conta_pedro.calcular_saldo().obter_quantia().obter_quantia_em_escala(), is_(equal_to(1500)))
        assert_that(self.conta_eduardo.calcular_saldo().obter_quantia().obter_quantia_em_escala(), is_(equal_to(1500)))
        assert_that(conta_pedro.calcular_saldo().obter_quantia().obter_quantia_em_escala(), all_of(greater_than(0), equal_to(1500))) # Logical matcher

if __name__ == '__main__':
    unittest.main()