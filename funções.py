import random
import inquirer


def dicas(pais):
    sorteada = pais
    
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
        
        

def documentacao():
    
    print("""Toda a documentação do jogo""")
    
def menu():
    questions = [
    inquirer.List('option',
                message="O que você quer fazer?",
                choices=['JOGAR', 'VER DOCUMENTAÇÃO', 'SAIR'],
            ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def menu_temas():
    questions = [
        inquirer.List('option',
                    message="Escolha um tema para jogar",
                    choices=['PAÍSES', 'ANIMAIS', 'VOLTAR'],
                ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def menu_dificuldade():
    questions = [
        inquirer.List('option',
                    message="Escolha a dificuldade",
                    choices=['FÁCIL', 'DIFÍCIL'],
                ),
            ]
    answers = inquirer.prompt(questions)
    return answers['option']

def lista_paises():
    paises = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Colômbia']
    return paises

def sorteia_pais(paises):
    sorteado = random.choice(paises)
    return sorteado

def mensagem():
    print('='*41)
    print("SEJA BEM VINDO AO JOGO DA ADIVINHAÇÃO!\n")
    print("Você tem 5 chances para acertar a palavra \nque estou pensando")
    print('='*41)
    
def paises():
    
    lista = lista_paises()
    sorteado = sorteia_pais(paises=lista)
    lista.remove(sorteado)
    dica = dicas(pais=sorteado)
    chances = 5
    pontos = 5
    print('dica:',dica[0])
    acabou = False
    
    while acabou == False:
        
        print(sorteado)

        tentativa = str(input("Digite sua tentativa: ")).strip()
        
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
                
            else:
                print("Ops.. Acabaram suas chances!\nVocê não ganhou nenhum ponto")
                acabou = True
                
        else:
            print(f"Parabéns, você acertou!\nPontos ganhos: {pontos}")
            acabou = True
            
        if acabou == True:
            return pontos

def jogo():

    while True:
        pontos = paises()
        print(pontos)
jogo()
        
