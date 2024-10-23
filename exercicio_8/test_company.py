# Dois funcionarios em um projeto

# Nao felizes:

# Criar funcionario em uma empresa e cadastrar ele em um projeto de outra empresa

import unittest
from Empresa import Empresa
from Funcionario import Funcionario
from Projeto import Projeto

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
        
    def test_criar_funcionario_sem_empresa(self):
        with self.assertRaises(Exception):
            funcionario = Funcionario('Joao')
            
    def test_criar_dois_funcionarios_iguais(self):
        empresa = Empresa('Figueirense S.A.')
        empresa.criar_funcionario('Joao')
        with self.assertRaises(Exception):
            empresa.criar_funcionario('Joao')
            
    def test_criar_projeto(self):
        empresa = Empresa('Figueirense S.A.')
        empresa.criar_projeto('Libertadores 2028')
        self.assertEqual(empresa.projetos[0].nome, 'Libertadores 2028')
        
    def test_criar_projeto_sem_empresa(self):
        with self.assertRaises(Exception):
            projeto = Projeto('Libertadores 2028')
    
    def test_criar_dois_projetos_iguais(self):
        empresa = Empresa('Figueirense S.A.')
        empresa.criar_projeto('Libertadores 2028')
        with self.assertRaises(Exception):
            empresa.criar_projeto('Libertadores 2028')
        
    def test_alocar_funcionario_em_projeto(self):
        empresa = Empresa('Figueirense S.A.')
        empresa.criar_funcionario('Joao')
        empresa.criar_projeto('Libertadores 2028')
        empresa.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        self.assertEqual(empresa.projetos[0].funcionarios[0].nome, 'Joao')
        self.assertEqual(empresa.funcionarios[0].projetos[0].nome, 'Libertadores 2028')
        
    def test_alocar_funcionario_em_dois_projetos(self):
        empresa = Empresa('Figueirense S.A.')
        empresa.criar_funcionario('Joao')
        empresa.criar_projeto('Libertadores 2028')
        empresa.criar_projeto('Mundial 2029')
        empresa.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        empresa.alocar_funcionario_em_projeto('Joao', 'Mundial 2029')
        self.assertEqual(empresa.projetos[0].funcionarios[0].nome, 'Joao')
        self.assertEqual(empresa.funcionarios[0].projetos[0].nome, 'Libertadores 2028')
        self.assertEqual(empresa.projetos[1].funcionarios[0].nome, 'Joao')
        self.assertEqual(empresa.funcionarios[0].projetos[1].nome, 'Mundial 2029')
        
    def test_alocar_dois_funcionario_em_projeto(self):
        empresa = Empresa('Figueirense S.A.')
        empresa.criar_funcionario('Joao')
        empresa.criar_funcionario('Jose')
        empresa.criar_projeto('Libertadores 2028')
        empresa.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        empresa.alocar_funcionario_em_projeto('Jose', 'Libertadores 2028')
        self.assertEqual(empresa.projetos[0].funcionarios[0].nome, 'Joao')
        self.assertEqual(empresa.projetos[0].funcionarios[1].nome, 'Jose')
        self.assertEqual(empresa.funcionarios[0].projetos[0].nome, 'Libertadores 2028')
    
if __name__ == '__main__':
    unittest.main()