from funções import jogo, menu, documentacao, menu_temas, menu_dificuldade, mensagem

def main():
    
    while True:
        escolha = menu()
        
        if escolha == "JOGAR":
            temas = menu_temas()
            
            if temas == 'PAÍSES':
                dificuldade = menu_dificuldade()
                
                if dificuldade == 'FÁCIL':
                    mensagem()
                    jogo()
                    menu_temas()
                    
                elif dificuldade == 'DIFÍCIL':
                    mensagem()
                    
                else:
                    menu_temas()
            
            elif temas == 'ANIMAIS':
                pass
            
            else:
                menu()

        elif escolha == "VER DOCUMENTAÇÃO":
            documentacao()
            
        else:
            exit()
    
if __name__ == "__main__":
    main()

