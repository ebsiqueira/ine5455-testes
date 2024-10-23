from Funcionario import Funcionario
from Projeto import Projeto

class Empresa():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = list()
        self.projetos = list()
        
    def criar_funcionario(self, nome):
        id_funcionario = len(self.funcionarios)
        funcionario = Funcionario(nome, id_funcionario, self)
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                raise('Funcionario já existe')
        self.funcionarios.append(funcionario)
        
    def criar_projeto(self, nome):
        id_projeto = len(self.projetos)
        projeto = Projeto(nome, id_projeto, self)
        for projeto in self.projetos:
            if projeto.nome == nome:
                raise('Projeto já existe')
        self.projetos.append(projeto)