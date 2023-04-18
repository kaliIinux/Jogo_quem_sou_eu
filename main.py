from funções import logica_jogo, menu, documentacao, menu_temas, menu_dificuldade, mensagem
from Jogador import Jogador
from Paises import Paises
from Jogador import Jogador

def main():
    
    jogadores = []
    placar = []
    
    while True:
        escolha = menu()
        
        if escolha == "JOGAR":
            player = Jogador(nome= input("Insira um nome de usuário: "))
            temas = menu_temas()
            
            while temas == 'PAÍSES':
                dificuldade = menu_dificuldade()
                
                if dificuldade == 'FÁCIL':
                    mensagem()
                    pontos = logica_jogo()
                    player.pontos = pontos
                    placar.append(pontos)
                    jogadores.append(player.nome)
                    print(f'jogador: {player.nome}\n',f'placar: {placar}')
                    print(jogadores)
                    print(placar)
                    
                elif dificuldade == 'DIFÍCIL':
                    mensagem()
                    
                else:
                    break
        else:
            if temas == 'ANIMAIS':
                pass
            
            else:
                menu()

        
    
if __name__ == "__main__":
    main()

