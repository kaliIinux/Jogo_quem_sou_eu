import inquirer
from Paises import PaisesFácil, PaisesDifícil
from Animais import AnimaisFacil, AnimaisDificil
import time

def documentacao():
    
    """
    Exibe toda a documentação da aplicação
    """
    
    print("""COMO JOGAR:\n
O jogo possui alguns temas e dificuldades para cada um desses temas,
os temas são:

- Países
- Animais
- *****

Você pode jogar na dificuldade fácil ou difícil.

No tema países por exemplo, o modo fácil irá conter 
paises da américa latina, enquanto no modo difícil,
serão paises do resto do mundo.

No tema Animais, o modo fácil contêm animais que são
típicos de fazenda e ambientes rurais, enquanto o modo
difícil, serão animais muito distintos, onde não há
co-relação entre eles, dificultando a possibilidade de
chutes.

Cada tema dificuldade possui 5 palavras, você terá 5 chances
para acertar cada uma delas, o número de chances será o
número de pontos que você irá ganhar, portanto:

Acertou de primeira: 5 pontos
Para cada erro: perde 1 ponto
Se não acertar após 5 tentativas: Não ganha ponto e
sorteia outra palavra

Boa jogatina!""")
    
def menu():
    
    """
    Menu geral
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
    questions = [
    inquirer.List('option',
                message="O que você quer fazer?",
                choices=['JOGAR', 'VER DOCUMENTAÇÃO', 'SAIR'],
            ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def menu_jogadores():
    
    """
    Menu para escolher quantos
    jogadores irão jogar
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
    questions = [
    inquirer.List('option',
                message="Jogadores: ",
                choices=['UM JOGADOR', 'MULTIJOGADOR'],
            ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def menu_temas():
    
    """
    Menu para definir o tema
    do jogo
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
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
    
    print("\x1b[2J\x1b[1;1H", end="")
    questions = [
        inquirer.List('option',
                    message="Escolha a dificuldade",
                    choices=['FÁCIL', 'DIFÍCIL', 'VOLTAR'],
                ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def mensagem():
    
    """
    Exibe a mensagem de Bem vindo
    """
    
    print("\x1b[2J\x1b[1;1H", end="")
    print('='*41)
    print("SEJA BEM VINDO AO JOGO DA ADIVINHAÇÃO!\n")
    print("Você tem 5 chances para acertar a palavra \nque estou pensando")
    print('='*41)
    print()
    
    
def jogo(tema: str, dificuldade: str):
    
    chances = 5
    pontos = 5
    lista_ponto = []
    
    if tema == 'Países' and dificuldade == 'Fácil': 
        objeto = PaisesFácil()
        sorteado = objeto.sorteia_facil()
        lista = objeto.pais_facil
        dica = objeto.dica_países_facil(país=sorteado)
        print(sorteado)
        print('dica:',dica[0])
    
    elif tema == 'Países' and dificuldade == 'Difícil':
        objeto = PaisesDifícil()
        sorteado = objeto.sorteia_dificil()
        lista = objeto.dificil
        dica = objeto.dica_países_dificil(país=sorteado)
        print(sorteado)
        print('dica:',dica[0])
        
    elif tema == 'Animais' and dificuldade == 'Fácil':
        objeto = AnimaisFacil()
        sorteado = objeto.sorteia_animal_facil()
        lista = objeto.animal_facil
        dica = objeto.dica_animais_facil(animal=sorteado)
        print(sorteado)
        print('dica:',dica[0])
    
    elif tema == 'Animais' and dificuldade == 'Difícil':
        objeto = AnimaisDificil()
        sorteado = objeto.sorteia_animal_dificil()
        lista = objeto.animal_dificil
        dica = objeto.dica_animais_dificil(animal=sorteado)
        print(sorteado)
        print('dica:',dica[0])
        
    try:
        while True:
            
            tentativa = str(input("Digite sua tentativa: \n")).strip().title()
            
            print("\x1b[2J\x1b[1;1H", end="")
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
                print(f"Parabéns, você acertou!\nPontos ganhos: {pontos}\n")
                time.sleep(2)
                lista_ponto.append(pontos)
                lista.remove(sorteado)
                pontos = 5
                chances = 5
                if tema == 'Países' and dificuldade == 'Fácil':
                    sorteado = objeto.sorteia_facil()
                    dica = objeto.dica_países_facil(país=sorteado)
                    
                elif tema == 'Países' and dificuldade == 'Difícil':
                    sorteado = objeto.sorteia_dificil()
                    dica = objeto.dica_países_dificil(país=sorteado)
                    
                elif tema == 'Animais' and dificuldade == 'Fácil':
                    sorteado = objeto.sorteia_animal_facil()
                    dica = objeto.dica_animais_facil(animal=sorteado)
                    
                elif tema == 'Animais' and dificuldade == 'Difícil':
                    sorteado = objeto.sorteia_animal_dificil()
                    dica = objeto.dica_animais_dificil(animal=sorteado)    
                print(lista)
                print(lista_ponto)
                print('dica:',dica[0])
    except:
        print("\x1b[2J\x1b[1;1H", end="")
        print(f'Obrigado por jogar!\n')
        return sum(lista_ponto)
