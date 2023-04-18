class Jogador:
    
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__pontos = 0
        
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
        
