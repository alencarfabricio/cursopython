"""
pessoa e o modulo onde esta criada a classe Pessoa.
Pessoa maisculo e a classe q estou herdando.
Quando eu faço uma herança eu herdei os metodos da classe em questao, neste exemplo agora eu tenho
os metodos andar e chorar da clase Pessoa e mais o metodo bicicleta q fiz na classe BB.
"""

# Realizando a importaçao da classe Pessoa
from pessoa import Pessoa

#Herdamos da classe Pessoa
class BB (Pessoa):            

    def __init__(self, nome, mae):
        print("Método construtor da sub classe")
        super().__init__(nome, mae) #Acessa o metodo construtor da super classe Pessoa q estou herdando.  
        self.nome = nome
        self.mae = mae
        
    # Especializacao da classe
    def bicicleta (self):
        print("Agora aprendendo a pedalar...")
        
