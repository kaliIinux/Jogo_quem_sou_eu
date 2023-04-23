class Dicas:
    
    """
    Classe com todas as dicas, da qual as
    classes de cada tema vão herdar os métodos 
    de seus respectivos temas e dificuldades.
    """
    
    @staticmethod
    def dica_países_dificil(país: str):
        sorteada = país
        
        if sorteada == 'Alemanha':
            alemanha = ['É um país que começa com a letra A\n','Está situado na Europa Ocidental\n', 'A capital é Berlim\n',  'A língua mãe é o alemão\n', 'Atualmente, o presidente do país é Frank-Walter Steinmeier\n']
            return alemanha
        
        elif sorteada == 'Jamaica':
            jamaica = ['É um país que começa com a letra J\n','Abriga um museu dedicado ao\ncantor Bob Marley\n', 'A capital do país é Kingston\n', 'A língua mãe é o patoá jamaicano\n', 'Atualmente, o chefe de estado do país é Rei Carlos III\n']
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
    
    @staticmethod
    def dica_países_facil(país: str):
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
        
    @staticmethod
    def dica_animais_facil(animal: str):
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
        
    @staticmethod
    def dica_animais_dificil(animal: str):
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
        