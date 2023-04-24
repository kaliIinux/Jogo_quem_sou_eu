from funções import jogo, menu, documentacao, menu_temas, menu_dificuldade, mensagem, menu_jogadores, menu_ranking
from Jogador import Jogador
import time

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
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}\n')
                        print('-'*20)
                        player.adicionar_jogador(pontos=pontos)
                        print("=====Ranking=====")
                        Jogador.ler_ranking()
                        input('Pressione ENTER para continuar')
                        
                    else:
                        player = Jogador(nome= input('Insira seu nome de usuário: '), idade=input("Idade: "))
                        mensagem()
                        pontos = jogo('Países', 'Difícil', player.nome)
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}\n')
                        print('-'*20)
                        player.adicionar_jogador(pontos=pontos)
                        print("=====Ranking=====")
                        Jogador.ler_ranking()
                        input('Pressione ENTER para continuar')
                        
                elif modo == 'MULTIJOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        player1 = Jogador(nome= input('Jogador 1: '), idade=input("Idade: "))
                        player2 = Jogador(nome=input("Jogador 2: "), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Países', 'Fácil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Países', 'Fácil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                        
                    else:
                        player1 = Jogador(nome= input('Jogador 1: '), idade=input("Idade: "))
                        player2 = Jogador(nome= input('Jogador 2: '), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Países', 'Difícil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Países', 'Difícil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                        
                    if pontos_j1 > pontos_j2:
                        print(f'Vitória de {player1.nome}')
                        
                    elif pontos_j2 > pontos_j1:
                        print(f'Vitória de {player2.nome}')
                    
                    else:
                        print('Empate!')
                    print('-'*20)
                    print("=====Ranking=====")
                    Jogador.ler_ranking()
                    input('Pressione ENTER para continuar')
                
            elif temas == 'ANIMAIS':
                modo = menu_jogadores()
                
                if modo == 'UM JOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        player = Jogador(nome= input('Insira seu nome de usuário: '), idade=input("Idade: "))
                        mensagem()
                        pontos = jogo('Animais','Fácil',player.nome)
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        player.adicionar_jogador(pontos=pontos)
                        print("=====Ranking=====")
                        Jogador.ler_ranking()
                        input('Pressione ENTER para continuar')
                        
                    else:
                        player = Jogador(nome= input('Insira seu nome de usuário: '), idade=input("Idade: "))
                        mensagem()
                        pontos = jogo('Animais', 'Difícil', player.nome)
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player.nome}\nPontuação: {pontos}')
                        player.adicionar_jogador(pontos=pontos)
                        print("=====Ranking=====")
                        Jogador.ler_ranking()
                        input('Pressione ENTER para continuar')
                        
                elif modo == 'MULTIJOGADOR':
                    dificuldade = menu_dificuldade()
                    
                    if dificuldade == 'FÁCIL':
                        player1 = Jogador(nome= input('Jogador 1: '), idade=input("Idade: "))
                        player2 = Jogador(nome= input('Jogador 2: '), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Animais', 'Fácil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Animais', 'Fácil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}\n')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                    
                    else:
                        player1 = Jogador(nome= input('Jogador 1: '), idade=input("Idade: "))
                        player2 = Jogador(nome= input('Jogador 2: '), idade=input("Idade: "))
                        mensagem()
                        pontos_j1 = jogo('Animais', 'Difícil', f'\033[31m{player1.nome}\033[0;0m')
                        pontos_j2 = jogo('Animais', 'Difícil', f'\033[32m{player2.nome}\033[0;0m')
                        print('-'*20)
                        print(f'Obrigado por jogar!\n')
                        print(f'Jogador: {player1.nome}\nPontuação: {pontos_j1}\n')
                        print(f'Jogador: {player2.nome}\nPontuação: {pontos_j2}\n')
                        player1.adicionar_jogador(pontos=pontos_j1)
                        player2.adicionar_jogador(pontos=pontos_j2)
                    
                    if pontos_j1 > pontos_j2:
                        print(f'Vitória de {player1.nome}')
                        
                    elif pontos_j2 > pontos_j1:
                        print(f'Vitória de {player2.nome}')
                    
                    else:
                        print('Empate!')
                    print('-'*20)
                    print("=====Ranking=====")
                    Jogador.ler_ranking()
                    input('Pressione ENTER para continuar')
            else:
                menu()
                
        elif escolha == 'DOCUMENTAÇÃO':
            documentacao()
            input('Pressione ENTER para continuar')
        
        elif escolha == 'RANKING':
            escolha = menu_ranking()
            
            if escolha == 'VER RANKING':
                try:
                    Jogador.ler_ranking()
                
                except:
                    print("Erro, escolha a opção NOVO RANKING")
                    time.sleep(3)
                
                else:
                    input('Pressione ENTER para continuar')
            
            elif escolha == 'NOVO RANKING':
                try:
                    Jogador.cria_planilha()
                    
                except:
                    print("Algo inesperado ocorreu.")
                    time.sleep(2.5)
                    
                else:
                    print("Ranking criado com sucesso!")
                    time.sleep(2.5)
            
            else:
                menu()
        else:
            exit()
    
if __name__ == "__main__":
    main()