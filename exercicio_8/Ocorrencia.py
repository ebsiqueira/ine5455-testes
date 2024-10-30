class Ocorrencia():
    def __init__(self, id, descricao, projeto):
        self.descricao = descricao
        self.id = id
        self.projeto = projeto
        self.responsavel = None
        self.aberta = True
        
    def adicionar_responsavel(self, responsavel):
        for funcionario in self.projeto.funcionarios:
            if(funcionario.nome == responsavel):
                self.responsavel = responsavel
                return self.responsavel
        raise Exception
    
    def fechar_ocorrencia(self):
        self.aberta = False
    