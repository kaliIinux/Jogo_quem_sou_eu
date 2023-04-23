import random
from Dicas import Dicas

class PaisesFacil(Dicas):
    
    """
    Classe do tema "Países", na dificuldade
    fácil, possui o método construtor da lista,
    o getter e o método para  sortear.
    """
    
    def __init__(self):
        self.__facil = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia']
    
    @property
    def pais_facil(self):
        return self.__facil
        
    
    def sorteia_facil(self):
        sorteado = random.choice(self.__facil)
        return sorteado
        
class PaisesDificil(Dicas):

    """
    Classe do tema "Países", na dificuldade
    difícil, possui o método construtor da lista,
    o getter e o método para  sortear.
    """
    
    def __init__(self):
        self.__dificil = ['Alemanha', 'Jamaica', 'Rússia', 'Itália', 'Portugal']
   
    @property
    def dificil(self):
        return self.__dificil
    
    def sorteia_dificil(self):
        sorteado = random.choice(self.__dificil)
        return sorteado