class Funcionario():
    def __init__(self, nome, empresa):
        self.nome = nome
        self.empresa = empresa
        self.projetos = list()
        self.ocorrencias_abertas = list()