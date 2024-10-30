from enum import Enum

class Tipo(Enum):
    TAREFA = 1
    BUG = 2
    MELHORIA = 3
    
class Prioridade(Enum):
    BAIXA = 1
    MEDIA = 2    
    ALTA = 3

class Ocorrencia():
    def __init__(self, id, descricao, projeto):
        self.descricao = descricao
        self.id = id
        self.projeto = projeto
        self.responsavel = None
        self.aberta = True
        self.tipo = Tipo.TAREFA
        self.prioridade = Prioridade.BAIXA
        
    def adicionar_responsavel(self, novo_responsavel):
        if(len(novo_responsavel.ocorrencias_abertas) > 10) or not(self.aberta):
            raise Exception
        
        for funcionario in self.projeto.funcionarios:
            if(funcionario.nome == novo_responsavel.nome):
                novo_responsavel.ocorrencias_abertas.append(self)
                self.responsavel = novo_responsavel
                return self.responsavel.nome

        raise Exception
    
    def mudar_prioridade(self, nova_prioridade):
        if isinstance(nova_prioridade, Prioridade) and self.aberta:
            self.prioridade = nova_prioridade
        else:
            raise Exception
            
        
    def fechar_ocorrencia(self):
        self.aberta = False
    