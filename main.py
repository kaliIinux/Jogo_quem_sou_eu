from funções import jogo, menu, documentacao, menu_temas, menu_dificuldade, mensagem, menu_jogadores
from jogador import Jogador

def main():
    """
    Função principal onde serão
    chamadas todas as outras funções
    e realizado a lógica final do jogo
    """
    jogadores = []
    placar = []
    
    while True:
        escolha = menu()
    
        if escolha == 'JOGAR':
            temas = menu_temas()
            
            if temas == 'PAÍSES':
                modo = menu_jogadores()
        
                if modo == 'UM JOGADOR':
                    dificuldade = menu_dificuldade()
                    if dificuldade == 'FÁCIL':
                        player = Jogador(nome= input("Insira um nome de usuário: "))
                        mensagem()
                        pontos = jogo('Países','Fácil')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                        
                    else:
                        player = Jogador(nome= input("Insira um nome de usuário: "))
                        mensagem()
                        pontos = jogo('Países', 'Difícil')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        input('Pressione ENTER para continuar')
                elif modo == 'MULTIJOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        #Multijogador
                        player1 = Jogador(nome= input("Insira o nome do jogador 1: "))
                        player2 = Jogador(nome= input("Insira o nome do jogador 2: "))
                        mensagem()
                        print(f'Vez do jogador {player1.nome}')
                        pontos_j1 = jogo('Países', 'Fácil')
                        print(f'Vez do jogador {player2.nome}')
                        pontos_j2 = jogo('Países', 'Fácil')
                        print('-'*10)
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}\n')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}')
                        print('-'*10)
                        input('Pressione ENTER para continuar')
                    
            elif temas == 'ANIMAIS':
                dificuldade = menu_dificuldade()
            
                if dificuldade == 'FÁCIL':
                    player = Jogador(nome= input("Insira um nome de usuário: "))
                    mensagem()
                    pontos = jogo('Animais', 'Fácil')
                    print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                    input('Pressione ENTER para continuar')
                else:
                    player = Jogador(nome= input("Insira um nome de usuário: "))
                    mensagem()
                    pontos = jogo('Animais', 'Difícil')
                    print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                    input('Pressione ENTER para continuar')
            else:
                menu()
        elif escolha == 'VER DOCUMENTAÇÃO':
            documentacao()
            input('Pressione ENTER para continuar')
    
if __name__ == "__main__":
    main()
