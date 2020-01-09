
class Player():
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.opcao = ''
    
    def setPontuacao(self, valor):
        self.pontuacao += valor
    
    def setOpcao(self, op):
        self.opcao = op
    
    def getOpcao(self):
        return self.opcao

    def getPontuacao(self):
        return self.pontuacao
    
    def getNome(self):
        return self.nome