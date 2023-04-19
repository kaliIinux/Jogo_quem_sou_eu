from funções import logica_jogo, menu, documentacao, menu_temas, menu_dificuldade, mensagem
from Jogador import Jogador
from Paises import Paises
from Animais import Animais
from Jogo import jogo

def main():
    
    jogadores = []
    placar = []
    
    escolha = menu()
    
    player = Jogador(nome= input("Insira um nome de usuário: "))
    
    while escolha == "JOGAR":
        temas = menu_temas()
        
        if temas == 'PAÍSES':
            dificuldade = menu_dificuldade()
            
            if dificuldade == 'FÁCIL':
                mensagem()
                pontos = jogo('Paises')
                player.pontos = pontos
                placar.append(pontos)
                jogadores.append(player.nome)
                print(f'jogador: {player.nome}\n',f'placar: {placar}')
                
            elif dificuldade == 'DIFÍCIL':
                mensagem()
                
            else:
                break
        elif temas == 'ANIMAIS':
            dificuldade = menu_dificuldade()
            
            if dificuldade == 'FÁCIL':
                mensagem()
                pontos = jogo('Animais')
                player.pontos = pontos
                placar.append(pontos)
                jogadores.append(player.nome)
                print(f'jogador: {player.nome}\n',f'placar: {placar}')
                
            else:
                pass
    
if __name__ == "__main__":
    main()
