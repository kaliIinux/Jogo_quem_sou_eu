import inquirer
from Paises import Paises

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
                    choices=['FÁCIL', 'DIFÍCIL', 'VOLTAR'],
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
    print()
    
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
            
            tentativa = str(input("Digite sua tentativa: \n")).strip().title()
            
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
        print('Obrigado por jogar!\nPontuação final: ', sum(lista_ponto))
        return sum(lista_ponto)