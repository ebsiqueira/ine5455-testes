# Criar empresa
# Criar funcionario
# Criar projeto
# Criar um funcionario na empresa
# Criar projeto na empresa
# Um funcionario em um projeto
# Um funcionaro em dois projetos
# Dois funcionarios em um projeto

# Nao felizes:
# Criar empresa sem nome
# Criar projeto sem empresa
# Criar funcionario sem empresa
# Criar dois funcionarios iguais

# Criar funcionario em uma empresa e cadastrar ele em um projeto de outra empresa

import unittest
from Empresa import Empresa

class TestBoard(unittest.TestCase):
    
    def test_criar_empresa(self):
        empresa = Empresa('Figueirense S.A.')
        self.assertEqual(empresa.nome, 'Figueirense S.A.')
        
    def test_criar_empresa_sem_nome(self):
        with self.assertRaises(Exception):
            empresa = Empresa()
            
    def test_criar_funcionario(self):
        empresa = Empresa('Figueirense S.A.')
        empresa.criar_funcionario('Joao')
        self.assertEqual(empresa.funcionarios[0].nome, 'Joao')
        self.assertEqual(empresa.funcionarios[0].id, 0)
        
if __name__ == '__main__':
    unittest.main()