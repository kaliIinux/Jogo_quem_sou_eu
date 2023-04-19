from Paises import Paises
from Animais import Animais

def jogo(tema: str):
    
    if tema == 'Paises':
        chances = 5
        pontos = 5
        lista_ponto = []
        objeto = Paises()
        sorteado = objeto.sorteia()
        lista = objeto.paises
        dica = objeto.dica_países(país=sorteado)
        print(sorteado)
        print('dica:',dica[0])
        pass
    
    elif tema == 'Animais':
        chances = 5
        pontos = 5
        lista_ponto = []
        objeto = Animais()
        sorteado = objeto.sorteia_animal()
        lista = objeto.animais
        dica = objeto.dica_animais(animal=sorteado)
        print(sorteado)
        print('dica:',dica[0])
        pass
        
        
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
                pontos = 5
                chances = 5
                if tema == 'Paises':
                    sorteado = objeto.sorteia()
                    dica = objeto.dica_países(país=sorteado)
                    
                elif tema == 'Animais':
                    sorteado = sorteado = objeto.sorteia_animal()
                    dica = objeto.dica_animais(animal=sorteado)
                
                print(lista)
                print(lista_ponto)
                print('dica:',dica[0])
    except:
        print('Obrigado por jogar!\nPontuação final: ', sum(lista_ponto))
        return sum(lista_ponto)
    

