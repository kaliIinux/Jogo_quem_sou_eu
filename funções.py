import random, inquirer
    
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
    
    def dicas(self, país: str):
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
        

def documentacao():
    
    """
    Exibe toda a documentação da aplicação
    """
    
    print("""Toda a documentação do jogo""")
    
def menu():
    
    """
    Menu geral
    """
    
    questions = [
    inquirer.List('option',
                message="O que você quer fazer?",
                choices=['JOGAR', 'VER DOCUMENTAÇÃO', 'SAIR'],
            ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def menu_temas():
    
    """
    Menu para definir o tema
    do jogo
    """
    
    questions = [
        inquirer.List('option',
                    message="Escolha um tema para jogar",
                    choices=['PAÍSES', 'ANIMAIS', 'VOLTAR'],
                ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def menu_dificuldade():
    
    """
    Menu para definir a dificuldade
    do jogo
    """
    
    questions = [
        inquirer.List('option',
                    message="Escolha a dificuldade",
                    choices=['FÁCIL', 'DIFÍCIL'],
                ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def mensagem():
    
    """
    Exibe a mensagem de Bbem vindo
    """
    
    print('='*41)
    print("SEJA BEM VINDO AO JOGO DA ADIVINHAÇÃO!\n")
    print("Você tem 5 chances para acertar a palavra \nque estou pensando")
    print('='*41)  
    
def logica_jogo():
    
    """
    Função onde será realizada a lógica do jogo,
    alterando apenas os valores das variáveis para
    executar a mesma lógica em diferentes condições.
    
    Returns:
        lista: retorna a lista com a soma dos pontos
        que o jogador fez na partida.
    """
    
    chances = 5
    pontos = 5
    lista_ponto = []
    objeto = Paises()
    lista = objeto.paises
    sorteado = objeto.sorteia()
    dica = objeto.dicas(país=sorteado)
    print(sorteado)
    print('dica:',dica[0])
    
    try:
        while True:
            
            tentativa = str(input("Digite sua tentativa: ")).strip().title()
            
            if tentativa != sorteado:
                chances -= 1
                
                if chances == 4:
                    print(f'Ops, você errou... \nchances: {chances}')
                    print('dica:',dica[1])
                    pontos -= 1
                    
                elif chances == 3:
                    print(f'Ops, você errou...\nchances: {chances}')
                    print('dica:',dica[2])
                    pontos -= 1
                
                elif chances == 2:
                    print(f'Ops, você errou...\nchances: {chances}')
                    print('dica:',dica[3])
                    pontos -= 1
                    
                elif chances == 1:
                    print(f'Ops, você errou...\nchances: {chances}')
                    print('dica:',dica[4])
                    pontos -= 1
                    
                elif chances == 0:
                    print("Ops.. Acabaram suas chances!\nVocê não ganhou nenhum ponto")
                    
            else:
                print(f"Parabéns, você acertou!\nPontos ganhos: {pontos}")
                lista_ponto.append(pontos)
                lista.remove(sorteado)
                sorteado = objeto.sorteia()
                dica = objeto.dicas(país=sorteado)
                pontos = 5
                chances = 5
                print(lista)
                print(lista_ponto)
                print('dica:',dica[0])
    except:
        return sum(lista_ponto)

def jogo():

    pontos = logica_jogo()
    print('Obrigado por jogar!\n Pontuação final: ', pontos)
