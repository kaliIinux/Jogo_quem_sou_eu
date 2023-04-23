from funções import jogo, menu, documentacao, menu_temas, menu_dificuldade, mensagem, menu_jogadores
from Jogador import Jogador

def main():
    
    """
    Função principal onde serão
    chamadas todas as outras funções
    e realizado a lógica final do jogo
    """
    
    while True:
        escolha = menu()
    
        if escolha == 'JOGAR':
            temas = menu_temas()
            
            if temas == 'PAÍSES':
                modo = menu_jogadores()
        
                if modo == 'UM JOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        player = Jogador(nome= input('Insira seu nome de usuário: '), idade=input("Idade: "))
                        mensagem()
                        pontos = jogo('Países','Fácil', player.nome)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                    else:
                        player = Jogador(nome= input('Insira seu nome de usuário: '), idade=input("Idade: "))
                        mensagem()
                        pontos = jogo('Países', 'Difícil', player.nome)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                elif modo == 'MULTIJOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        Jogador.cria_planilha()
                        player1 = Jogador(nome=input("Jogador 1: "), idade=input("Idade: "))
                        player2 = Jogador(nome=input("Jogador 2: "), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Países', 'Fácil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Países', 'Fácil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                        Jogador.ler()
                        
                    else:
                        Jogador.cria_planilha()
                        player1 = Jogador(nome= input('Jogador 1: '), idade=input("Idade: "))
                        player2 = Jogador(nome= input('Jogador 2: '), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Países', 'Difícil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Países', 'Difícil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                        Jogador.ler()
                        
                    if pontos_j1 > pontos_j2:
                        print(f'Vitória de {player1.nome}')
                        
                    elif pontos_j2 > pontos_j1:
                        print(f'Vitória de {player2.nome}')
                    
                    else:
                        print('Empate!')
                    print('-'*20)
                    input('Pressione ENTER para continuar')
                    
            elif temas == 'ANIMAIS':
                modo = menu_jogadores()
                
                if modo == 'UM JOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        player = Jogador(nome= input('Insira seu nome de usuário: '), idade=input("Idade: "))
                        mensagem()
                        pontos = jogo('Animais','Fácil',player.nome)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                    else:
                        player = Jogador(nome= input('Insira seu nome de usuário: '))
                        mensagem()
                        pontos = jogo('Animais', 'Difícil', player.nome)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                elif modo == 'MULTIJOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        Jogador.cria_planilha()
                        player1 = Jogador(nome= input('Jogador 1: '), idade=input("Idade: "))
                        player2 = Jogador(nome= input('Jogador 2: '), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Animais', 'Fácil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Animais', 'Fácil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                        Jogador.ler()
                    
                    else:
                        Jogador.cria_planilha()
                        player1 = Jogador(nome= input('Jogador 1: '), idade=input("Idade: "))
                        player2 = Jogador(nome= input('Jogador 2: '), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Animais', 'Difícil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Animais', 'Difícil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                        Jogador.ler()
                    
                    if pontos_j1 > pontos_j2:
                        print(f'Vitória de {player1.nome}')
                        
                    elif pontos_j2 > pontos_j1:
                        print(f'Vitória de {player2.nome}')
                    
                    else:
                        print('Empate!')
                    print('-'*20)
                    input('Pressione ENTER para continuar')
                    
            else:
                menu()
                
        elif escolha == 'VER DOCUMENTAÇÃO':
            documentacao()
            input('Pressione ENTER para continuar')
    
if __name__ == "__main__":
    main()