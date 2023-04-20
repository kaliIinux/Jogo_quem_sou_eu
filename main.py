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
                        player = Jogador.criar_jogador(nome= input('Insira seu nome de usuário: '))
                        mensagem()
                        pontos = jogo('Países','Fácil')
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                    else:
                        player = Jogador.criar_jogador(nome= input('Insira seu nome de usuário: '))
                        mensagem()
                        pontos = jogo('Países', 'Difícil')
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                elif modo == 'MULTIJOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        player1 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 1: '))
                        player2 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 2: '))
                        mensagem()
                        print(f'Vez do jogador {player1.nome}\n')
                        pontos_j1 = jogo('Países', 'Fácil')
                        print(f'Vez do jogador {player2.nome}\n')
                        pontos_j2 = jogo('Países', 'Fácil')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}\n')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}\n')
                    
                    else:
                        player1 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 1: '))
                        player2 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 2: '))
                        mensagem()
                        print(f'Vez do jogador {player1.nome}\n')
                        pontos_j1 = jogo('Países', 'Difícil')
                        print(f'Vez do jogador {player2.nome}\n')
                        pontos_j2 = jogo('Países', 'Difícil')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}\n')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}\n')
                    
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
                        player = Jogador.criar_jogador(nome= input('Insira seu nome de usuário: '))
                        mensagem()
                        pontos = jogo('Animais','Fácil')
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                    else:
                        player = Jogador.criar_jogador(nome= input('Insira seu nome de usuário: '))
                        mensagem()
                        pontos = jogo('Animais', 'Difícil')
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                elif modo == 'MULTIJOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        player1 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 1: '))
                        mensagem()
                        print(f'Vez do jogador {player1.nome}\n')
                        pontos_j1 = jogo('Animais', 'Fácil')
                        player2 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 2: '))
                        print(f'Vez do jogador {player2.nome}\n')
                        pontos_j2 = jogo('Animais', 'Fácil')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}\n')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}')
                    
                    else:
                        player1 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 1: '))
                        mensagem()
                        print(f'Vez do jogador {player1.nome}\n')
                        pontos_j1 = jogo('Animais', 'Difícil')
                        player2 = Jogador.criar_jogador(nome= input('Insira o nome do jogador 2: '))
                        print(f'Vez do jogador {player2.nome}\n')
                        pontos_j2 = jogo('Animais', 'Difícil')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}\n')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}')
                    
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
