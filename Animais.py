import random
from Dicas import Dicas

class AnimaisFacil(Dicas):
    
    """
    Classe do tema "Animais", na dificuldade
    fácil, possui o método construtor da lista,
    o getter e o método para  sortear.
    """
    
    def __init__(self):
        self.__facil = ['Vaca', 'Cavalo', 'Ovelha', 'Galinha', 'Porco']
        
    @property
    def animal_facil(self):
        return self.__facil    
       
    def sorteia_animal_facil(self):
        sorteado = random.choice(self.__facil)
        return sorteado
        
class AnimaisDificil(Dicas):
    
    """
    Classe do tema "Animais", na dificuldade
    difícil, possui o método construtor da lista,
    o getter e o método para sortear.
    """
    
    def __init__(self) :
        self.__dificil = ['Baleia', 'Cobra', 'Rinoceronte', 'Gato', 'Girafa']
        
    @property
    def animal_dificil(self):
        return self.__dificil    
       
    def sorteia_animal_dificil(self):
        sorteado = random.choice(self.__dificil)
        return sorteado