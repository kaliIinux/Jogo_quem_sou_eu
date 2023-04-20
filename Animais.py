import random

class AnimaisFacil:
    
    """
    Classe do tema "Animais", possui a 
    lista de palavras do tema e os métodos
    para manipular essa lista
    """
    
    def __init__(self):
        self.__facil = ['Vaca', 'Cavalo', 'Ovelha', 'Galinha', 'Porco']
        
    @property
    def animal_facil(self):
        return self.__facil    
       
    def sorteia_animal_facil(self):
        sorteado = random.choice(self.__facil)
        return sorteado
    
    def remover(self):
        sorteado = self.__facil
        nova_lista = self.__facil.remove(sorteado)
        return nova_lista
    
    def dica_animais_facil(self, animal: str):
        sorteada = animal
        
        if sorteada == 'Vaca':
            vaca = ['Começa com a letra V\n','É um animal mamífero\n', 'É a fêmea do touro\n',  'Dá leite\n', 'É um animal que muge\n']
            return vaca
        
        elif sorteada == 'Cavalo':
            cavalo = ['Começa com a letra C\n','É um animal mamífero\n', '\n', 'É um animal herbívoro\n', 'Possui casco\n', 'É um animal que relincha\n']
            return cavalo
        
        elif sorteada == 'Ovelha':
            ovelha = ['Começa com a letra O', 'É um animal mamífero\n', 'Seu corpo é revestido de lã\n', 'Possui casco\n', 'É um animal que berra\n']
            return ovelha
        
        elif sorteada == 'Galinha':
            galinha = ['Começa com a letra G', 'É um animal ovíparo\n', 'Possui penas\n', 'É um animal que cacareja\n', 'Bota ovos']
            return galinha
        
        else:
            porco = ['Começa com a letra P\n','É um animal mamífero\n', 'Tem uma coloração rosada\n',  'Possui patas curtas\n', 'Tem um rabinho enrolado']
            return porco
        
class AnimaisDificil:
    def __init__(self) :
        self.__dificil = ['Baleia', 'Cobra', 'Rinoceronte', 'Gato', 'Girafa']
        
    @property
    def animal_dificil(self):
        return self.__dificil    
       
    def sorteia_animal_dificil(self):
        sorteado = random.choice(self.__dificil)
        return sorteado
    
    def dica_animais_dificil(self, animal: str):
        sorteada = animal
        
        if sorteada == 'Baleia':
            baleia = ['Começa com a letra B\n','É um animal mamífero\n', 'Possui cerca de 10 metros\n',  'Pode chegar a 8 e 9 toneladas\n', 'É um animal aquático\n']
            return baleia
        
        elif sorteada == 'Cobra':
            cobra = ['Começa com a letra C\n','Seu corpo é coberto por escamas\n', 'É um animal de sangue frio\n', 'É um animal rastejante\n', 'Algumas espécies são venenosas\n']
            return cobra
        
        elif sorteada == 'Rinoceronte':
            rinoceronte = ['Começa com a letra R\n', 'É um animal mamífero\n', 'Em sua cabeça pode haver de um a dois cornos\n', 'Corpo largo e perna curta\n', 'Possui uma pele grossa\n']
            return rinoceronte
        
        elif sorteada == 'Gato':
            gato = ['Começa com a letra G\n', 'É um animal mamífero\n', 'Tem pelo\n', 'É um animal doméstico\n', 'Mia\n']
            return gato
        
        else:
            girafa = ['Começa com a letra G\n','É um animal mamífero\n', 'Tem um pescoço grande\n',  'Passa maior parte do tempo zumbindo\n', 'Maior animal terrestre do mundo\n']
            return girafa
        