# Criar empresa
# Criar funcionario
# Criar projeto
# Criar um funcionario na empresa
# Criar projeto na empresa
# Um funcionario em um projeto
# Um funcionaro em dois projetos
# Dois funcionarios em um projeto

# Nao felizes:
# Criar projeto sem empresa
# Criar funcionario sem empresa
# Criar dois funcionarios iguais

# Criar funcionario em uma empresa e cadastrar ele em um projeto de outra empresa

import unittest
from Empresa import Empresa

class TestBoard(unittest.TestCase):
    
    def test_criar_empresa(self):
        empresa = Empresa('Figueirense S.A')
        self.assertEqual(empresa.nome, 'Figueirense S.A')

if __name__ == '__main__':
    unittest.main()