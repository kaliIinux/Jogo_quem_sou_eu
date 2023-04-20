class Jogador:
    
    def __init__(self, nome: str, pontos: int) -> None:
        self.__nome = nome
        self.__pontos = pontos
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
        
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, value):
        self.__pontos = value
        
    @classmethod
    def criar_jogador(cls, nome):
        return cls(nome, 0)

#nomes = ['angelo', 'kadu']
#pessoas = []

#p = Jogador.criar_jogador(nomes)
#pessoas.append(vars(p))

    
#print('\n\n', pessoas)
#print(pessoas[0]['_Jogador__nome'])  
#print(pessoas[0]['_Jogador__pontos'])    
    
        
