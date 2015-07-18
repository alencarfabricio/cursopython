class Pessoa(object):

    def __init__(self, nome, mae):   # O construtor sempre vem com __init__
        self.nome = nome
        self.mae = mae
        print("Método construtor da super classe")

    def andar (self):
        print("Aprendendo a caminha!")

    def chorar(self):
        print("Muleque chorando pq caiu!!!")
        
