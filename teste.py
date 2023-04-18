class Pessoa:
    
    def exibe_cpf(self):
        return '019201209030'

class Secretaria(Pessoa):
    
    pass

se = Secretaria()
print(se.exibe_cpf())

