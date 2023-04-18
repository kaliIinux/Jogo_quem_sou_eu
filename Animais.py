import random

class Animais:
    
    """
    Classe do tema "Animais", possui a 
    lista de palavras do tema e os métodos
    para manipular essa lista
    """
    
    def __init__(self) -> None:
        self.animais = ['Vaca', 'Cavalo', 'Ovelha', 'Galinha', 'Porco']
        
    def sorteia(self):
        sorteado = random.choice(self.animais)
        return sorteado
    
    def remover(self):
        sorteado = self.sorteia()
        nova_lista = self.animais.remove(sorteado)
        return nova_lista
    
    def dicas(self, animal: str):
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
            porco = ['Começa com a letra C\n','É um animal mamífero\n', 'Tem uma coloração rosada\n',  'Possui patas curtas\n', 'Tem um rabinho enrolado']
            return porco
        