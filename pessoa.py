#Criando uma classe Pessoa 
class Pessoa(object):

    # O construtor sempre vem com __init__
    def __init__(self, nome, mae):   
        self.nome = nome
        self.mae = mae
        print("Método construtor da super classe")

    def andar (self):
        print("Aprendendo a caminha!")

    def chorar(self):
        print("Muleque chorando pq caiu!!!")
        
