class Carro():
    
    def __init__(self, cor, marca, ano) -> None:
        self.cor = cor
        self.marca = marca
        self.ano = ano
        
carro1 = Carro(cor='azul', marca='fiat', ano='2023')

print('Cor: ', carro1.cor)
print('Marca: ', carro1.marca)
print('Ano: ', carro1.ano)