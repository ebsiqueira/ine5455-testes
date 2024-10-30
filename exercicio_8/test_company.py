import unittest
from Empresa import Empresa
from Funcionario import Funcionario
from Projeto import Projeto
from Ocorrencia import *

def criar_e_associar_dez_ocorrencias(projeto, responsavel):
    for i in range(11):
        tarefa_sobre_trabalho = projeto.criar_ocorrencia('Trabalho do dia {}'.format(i))
        tarefa_sobre_trabalho.adicionar_responsavel(responsavel)

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
        joao = figueirense.criar_funcionario('Joao')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        with self.assertRaises(Exception):
            treinamento_novos_jogadores.adicionar_responsavel(joao)
    
    # Ocorrencia tem que ter responsavel em projeto
    def test_atibui_funcionario_de_projeto_a_ocorrencia(self):
        figueirense = Empresa('Figueirense S.A.')
        joao = figueirense.criar_funcionario('Joao')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        treinamento_novos_jogadores.adicionar_responsavel(joao)
        self.assertEqual(treinamento_novos_jogadores.responsavel.nome, 'Joao')
    
    # Ocorrencia não pode receber funcionário de projeto diferente
    def test_atribui_funcionario_de_projeto_diferente(self):
        figueirense = Empresa('Figueirense S.A.')
        figueirense.criar_projeto('Libertadores 2028')
        serie_b = figueirense.criar_projeto('Serie B 2026')
        joao = figueirense.criar_funcionario('Joao')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        treinamento_novos_jogadores = serie_b.criar_ocorrencia('Treinamento de novos jogadores')
        with self.assertRaises(Exception):
            treinamento_novos_jogadores.adicionar_responsavel(joao)
  
    # Funcionário pode fechar ocorrencia
    def test_fecha_ocorrencia(self):
        figueirense = Empresa('Figueirense S.A.')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        treinamento_novos_jogadores.fechar_ocorrencia()
        self.assertEqual(treinamento_novos_jogadores.aberta, False)
    
    # Ocorrencia pode mudar de resónsável quando aberta
    def test_ocorrencia_muda_responsavel(self):
        figueirense = Empresa('Figueirense S.A.')
        joao = figueirense.criar_funcionario('Joao')
        jose = figueirense.criar_funcionario('Jose')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Jose', 'Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        treinamento_novos_jogadores.adicionar_responsavel(joao)
        treinamento_novos_jogadores.adicionar_responsavel(jose)
        self.assertEqual(treinamento_novos_jogadores.responsavel.nome, 'Jose')
    
    # Ocorrencia não pode mudar de responsável quando fechada
    def test_ocorrencia_muda_responsavel_fechada(self):
        figueirense = Empresa('Figueirense S.A.')
        joao = figueirense.criar_funcionario('Joao')
        jose = figueirense.criar_funcionario('Jose')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Jose', 'Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        treinamento_novos_jogadores.adicionar_responsavel(joao)
        treinamento_novos_jogadores.fechar_ocorrencia()
        with self.assertRaises(Exception):
            treinamento_novos_jogadores.adicionar_responsavel(jose)

    # Funcionário pode ter até 10 ocorrencias abertas
    def test_funcionario_com_onze_ocorrencias_abertas(self):
        figueirense = Empresa('Figueirense S.A.')
        joao = figueirense.criar_funcionario('Joao')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        figueirense.alocar_funcionario_em_projeto('Joao', 'Libertadores 2028')
        criar_e_associar_dez_ocorrencias(libertadores, joao)
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        with self.assertRaises(Exception):
            treinamento_novos_jogadores.adicionar_responsavel(joao)

    # Ocorrencia possui três tipos e possui uma prioridade associada
    def test_tipo_e_prioridade_da_ocorrencia(self):    
        figueirense = Empresa('Figueirense S.A.')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        self.assertEqual(treinamento_novos_jogadores.tipo, Tipo.TAREFA)
        self.assertEqual(treinamento_novos_jogadores.prioridade, Prioridade.BAIXA)
    
    # Ocorrencia pode mudar prioridade quando aberta
    def test_muda_prioridade_da_ocorrencia_aberta(self):    
        figueirense = Empresa('Figueirense S.A.')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        treinamento_novos_jogadores.mudar_prioridade(Prioridade.MEDIA)
        self.assertEqual(treinamento_novos_jogadores.prioridade, Prioridade.MEDIA)
    
    # Ocorrencia não pode mudar de prioridade quando fechada
    def test_muda_prioridade_da_ocorrencia_fechada(self):    
        figueirense = Empresa('Figueirense S.A.')
        libertadores = figueirense.criar_projeto('Libertadores 2028')
        treinamento_novos_jogadores = libertadores.criar_ocorrencia('Treinamento de novos jogadores')
        treinamento_novos_jogadores.fechar_ocorrencia()
        with self.assertRaises(Exception):
            treinamento_novos_jogadores.mudar_prioridade(Prioridade.MEDIA)

if __name__ == '__main__':
    unittest.main()