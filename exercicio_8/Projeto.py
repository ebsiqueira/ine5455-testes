from Ocorrencia import Ocorrencia

class Projeto():
    def __init__(self, nome, empresa):
        self.nome = nome
        self.empresa = empresa
        self.funcionarios = list()
        self.ocorrencias = list()
        
    def criar_ocorrencia(self, descricao):
        id_ocorrencia = len(self.ocorrencias)
        ocorrencia = Ocorrencia(id_ocorrencia, descricao)
        self.ocorrencias.append(ocorrencia)
        return ocorrencia