from Funcionario import Funcionario

class Empresa():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = list()
        
    def criar_funcionario(self, nome):
        id_funcionario = len(self.funcionarios)
        funcionario = Funcionario(nome, id_funcionario)
        self.funcionarios.append(funcionario)