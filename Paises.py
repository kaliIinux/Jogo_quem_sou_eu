import random

class PaisesFácil():
    
    """
    Classe do tema "Paises", possui a 
    lista de palavras do tema e os métodos
    para manipular essa lista
    """
    
    def __init__(self):
        self.__facil = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia']
        
    @property
    def pais_facil(self):
        return self.__facil
        
    
    def sorteia_facil(self):
        sorteado = random.choice(self.__facil)
        return sorteado
    
    def remover(self):
        sorteado = self.sorteia_facil()
        nova_lista = self.__facil.remove(sorteado)
        return nova_lista
    
    def dica_países_facil(self, país: str):
        sorteada = país
        
        if sorteada == 'Brasil':
            brasil = ['É um país que começa com a letra B\n','Possui a maior floresta do mundo, conhecida\ncomo floresta amazônica\n', 'A capital é Brasília\n',  'A língua mãe é o portugês\n', 'Atualmente, o presidente do país é Lula\n']
            return brasil
        
        elif sorteada == 'Argentina':
            argentina = ['É um país que começa com a letra A\n','País do tango\n', 'A capital do país é Bueno Aires\n', 'A língua mãe é o Espanhol\n', 'Atualmente, o presidente do país é Alberto Fernández\n']
            return argentina
        
        elif sorteada == 'Chile':
            chile = ['É um país que começa com a letra C\n', 'O deserto mais seco do mundo, está localizado\nnesse país (Deserto do Atacama)\n', 'A capital do país é Santiado\n', 'A língua mãe é o Espanhol\n', 'Atualmente, o presidente do país é Gabriel Boric\n']
            return chile
        
        elif sorteada == 'Peru':
            peru = ['É um país que começa com a letra P\n', 'É a civilização mais antiga da América Latina\n', 'A capital do país é Lima\n', 'A língua mãe é o Espanhol\n', 'Atualmente, a presidenta do país é Dina Boluarte\n']
            return peru
        
        else:
            colombia = ['É um país que começa com a letra C\n', 'Este país é responsável por 50%\nda produção mundial de esmeraldas\n', 'A capital do país é Bogotá\n', 'A língua mãe é o Espanhol\n', 'Atualmente, o presidente do país é Gustavo Petro\n']
            return colombia
        
class PaisesDifícil():
          
    def __init__(self):
        self.__dificil = ['Alemanha', 'Jamaica', 'Rússia', 'Itália', 'Portugal']
   
    @property
    def dificil(self):
        return self.__dificil
    
    def sorteia_dificil(self):
        sorteado = random.choice(self.__dificil)
        return sorteado
    
    def remover(self):
        sorteado = self.__dificil()
        nova_lista = self.__dificil.remove(sorteado)
        return nova_lista
    
    def dica_países_dificil(self, país: str):
        sorteada = país
        
        if sorteada == 'Alemanha':
            alemanha = ['É um país que começa com a letra A\n','Está situado na Europa Ocidental\n', 'A capital é Berlim\n',  'A língua mãe é o alemão\n', 'Atualmente, o presidente do país é Frank-Walter Steinmeier\n']
            return alemanha
        
        elif sorteada == 'Jamaica':
            jamaica = ['É um país que começa com a letra J\n','Abriga um museu dedicado ao\ncantor Bob Marley', 'A capital do país é Kingston\n', 'A língua mãe é o patoá jamaicano\n', 'Atualmente, o chefe de estado do país é Rei Carlos III\n']
            return jamaica
        
        elif sorteada == 'Rússia':
            russia = ['É um país que começa com a letra R\n', 'É o país com maior território do mundo\n', 'A capital do país é Moscou\n', 'A língua mãe é o russo\n', 'Atualmente, o presidente do país é Vladimir Putin\n']
            return russia
        
        elif sorteada == 'Itália':
            italia = ['É um país que começa com a letra I\n', 'É a civilização mais antiga da América Latina\n', 'A capital do país é Roma\n', 'A língua mãe é o italiano\n', 'Atualmente, o presidente do país é Sergio Mattarella\n']
            return italia
        
        else:
            portugal = ['É um país que começa com a letra P\n', 'Existem muitos castelos medievais neste país\n', 'A capital do país é Lisboa\n', 'A língua mãe é o português\n', 'Atualmente, o presidente do país é Marcelo Rebelo de Sousa\n']
            return portugal