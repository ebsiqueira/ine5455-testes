import unittest
from Empresa import Empresa
from Funcionario import Funcionario
from Projeto import Projeto
from Ocorrencia import Ocorrencia

class TestBoard(unittest.TestCase):
    
    def test_criar_empresa(self):
        figueirense = Empresa('Figueirense S.A.')
        self.assertEqual(figueirense.nome, 'Figueirense S.A.')
        
    def test_criar_empresa_sem_nome(self):
        with self.assertRaises(Exception):
            empresa_sem_nome = Empresa()
            
    def test_criar_funcionario(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        self.assertEqual(figueirense.funcionarios[0].nome, 'Joao')
        
    def test_criar_dois_funcionarios(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        figueirense.criar_funcionario('Jose')
        self.assertEqual(figueirense.funcionarios[0].nome, 'Joao')
        self.assertEqual(figueirense.funcionarios[1].nome, 'Jose')
        
    def test_criar_funcionario_sem_empresa(self):
        with self.assertRaises(Exception):
            funcionario = Funcionario('Joao')
            
    def test_criar_dois_funcionarios_iguais(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        with self.assertRaises(Exception):
            figueirense.criar_funcionario('Joao')
            
    def test_criar_projeto(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_projeto('Libertadores 2028')
        self.assertEqual(figueirense.projetos[0].nome, 'Libertadores 2028')
        
    def test_criar_dois_projetos(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_projeto('Libertadores 2028')
        figueirense.criar_projeto('Mundial 2029')
        self.assertEqual(figueirense.projetos[0].nome, 'Libertadores 2028')
        self.assertEqual(figueirense.projetos[1].nome, 'Mundial 2029')
        
    def test_criar_projeto_sem_empresa(self):
        with self.assertRaises(Exception):
            libertadores = Projeto('Libertadores 2028')
    
    def test_criar_dois_projetos_iguais(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_projeto('Libertadores 2028')
        with self.assertRaises(Exception):
            figueirense.criar_projeto('Libertadores 2028')
        
    def test_alocar_funcionario_em_projeto(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        figueirense.criar_projeto('Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        self.assertEqual(figueirense.projetos[0].funcionarios[0].nome, 'Joao')
        self.assertEqual(figueirense.funcionarios[0].projetos[0].nome, 'Libertadores 2028')
        
    def test_alocar_funcionario_em_dois_projetos(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        figueirense.criar_projeto('Libertadores 2028')
        figueirense.criar_projeto('Mundial 2029')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Mundial 2029')
        self.assertEqual(figueirense.projetos[0].funcionarios[0].nome, 'Joao')
        self.assertEqual(figueirense.funcionarios[0].projetos[0].nome, 'Libertadores 2028')
        self.assertEqual(figueirense.projetos[1].funcionarios[0].nome, 'Joao')
        self.assertEqual(figueirense.funcionarios[0].projetos[1].nome, 'Mundial 2029')
        
    def test_alocar_dois_funcionario_em_projeto(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        figueirense.criar_funcionario('Jose')
        figueirense.criar_projeto('Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Jose', 'Libertadores 2028')
        self.assertEqual(figueirense.projetos[0].funcionarios[0].nome, 'Joao')
        self.assertEqual(figueirense.projetos[0].funcionarios[1].nome, 'Jose')
        self.assertEqual(figueirense.funcionarios[0].projetos[0].nome, 'Libertadores 2028')
        
    # Projeto cria ocorrencia
    #   Ocorrencia tem ID e descrição
    def test_projeto_cria_ocorrencia(self):
        figueirense = Empresa('Figueirense S.A.')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        libertadores.criar_ocorrencia('Projeto para vencer a libertadores no ano de 2028.')
        self.assertEqual(figueirense.projetos[0].ocorrencias[0].id, 0)
        self.assertEqual(figueirense.projetos[0].ocorrencias[0].descricao, 'Projeto para vencer a libertadores no ano de 2028.')
    
    # Ocorrencia não pode ser cirada fora do projeto
    def test_ocorrencia_sem_projeto(self):
        with self.assertRaises(Exception):
            treinamento_novos_jogadores = Ocorrencia(0, 'Treinamento de novos jogadores')
    
    # Ocorrencia com funcionario fora do projeto
    def test_atibui_funcionario_a_ocorrencia(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        with self.assertRaises(Exception):
            treinamento_novos_jogadores.adicionar_responsavel('Joao')
    
    # Ocorrencia tem que ter responsavel em projeto
    def test_atibui_funcionario_de_projeto_a_ocorrencia(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_funcionario('Joao')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        treinamento_novos_jogadores.adicionar_responsavel('Joao')
        self.assertEqual(treinamento_novos_jogadores.responsavel, 'Joao')
    
    # Ocorrencia não pode receber funcionário de projeto diferente
    def test_atribui_funcionario_de_projeto_diferente(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_projeto('Libertadores 2028')
        serie_b = figueirense.criar_projeto('Serie B 2026')
        figueirense.criar_funcionario('Joao')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        treinamento_novos_jogadores = serie_b.criar_ocorrencia('Treinamento de novos jogadores')
        with self.assertRaises(Exception):
            treinamento_novos_jogadores.adicionar_responsavel('Joao')

    
    # Funcionário pode fechar ocorrencia
    # Ocorrencia pode mudar de resónsável quando aberta
    # Ocorrencia não pode mudar de responsável quando fechada
    # Funcionário pode ter até 10 ocorrencias abertas
    # Ocorrencia possui três tipos e possui uma prioridade associada
    # Ocorrencia pode mudar prioridade quando aberta
    # Ocorrencia não pode mudar de prioridade quando fechada
    
if __name__ == '__main__':
    unittest.main()