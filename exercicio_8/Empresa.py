from Funcionario import Funcionario
from Projeto import Projeto

class Empresa():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = list()
        self.projetos = list()
        
    def criar_funcionario(self, nome):
        funcionario = Funcionario(nome, self)
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                raise('Funcionario já existe')
        self.funcionarios.append(funcionario)
        
    def criar_projeto(self, nome):
        projeto = Projeto(nome, self)
        for projeto in self.projetos:
            if projeto.nome == nome:
                raise('Projeto já existe')
        self.projetos.append(projeto)
        
    def alocar_funcionario_em_projeto(self, nome_funcionario, nome_projeto):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome_funcionario:
                associado = funcionario
                break
        for projeto in self.projetos:
            if projeto.nome == nome_projeto:
                associado.projetos.append(projeto)
                projeto.funcionarios.append(associado)
                break