import random

class Paises():
    
    """
    Classe do tema "Paises", possui a 
    lista de palavras do tema e os métodos
    para manipular essa lista
    """
    
    def __init__(self):
        self.paises = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia']
    
    def sorteia(self):
        sorteado = random.choice(self.paises)
        return sorteado
    
    def remover(self):
        sorteado = self.sorteia()
        nova_lista = self.paises.remove(sorteado)
        return nova_lista
    
    @staticmethod
    def dicas(país: str):
        sorteada = país
        
        if sorteada == 'Brasil':
            brasil = ['É um país que começa com a letra B\n','Possui a maior floresta do mundo, conhecida\ncomo floresta amazônica\n', 'A capital é Brasília\n',  'A língua mãe é o portugês\n', 'Atualmente, o presidente do país é Lula']
            return brasil
        
        elif sorteada == 'Argentina':
            argentina = ['É um país que começa com a letra A\n','País do tango\n', 'A capital do país é Bueno Aires\n', 'A língua mãe é o Espanhol\n', 'Atualmente, o presidente do país é Alberto Fernández\n']
            return argentina
        
        elif sorteada == 'Chile':
            chile = ['É um país que começa com a letra C', 'O deserto mais seco do mundo, está localizado\nnesse país (Deserto do Atacama)\n', 'A capital do país é Santiado\n', 'A língua mãe é o Espanhol\n', 'Atualmente, o presidente do país é Gabriel Boric\n']
            return chile
        
        elif sorteada == 'Peru':
            peru = ['É um país que começa com a letra P', 'É a civilização mais antiga da América Latina\n', 'A capital do país é Lima\n', 'A língua mãe é o Espanhol\n', 'Atualmente, a presidenta do país é Dina Boluarte']
            return peru
        
        else:
            colombia = ['É um país que começa com a letra C', 'Este país é responsável por 50%\nda produção mundial de esmeraldas', 'A capital do país é Bogotá\n', 'A língua mãe é o Espanhol', 'Atualmente, o presidente do país é Gustavo Petro']
            return colombia

        
        