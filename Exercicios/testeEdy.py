 
class CalculoReal(object):

    def __init__(self,cotacao,valorReal):
        self.valorReal = valorReal
        self.cotacao = cotacao
        if self.cotacao <= 0:
            raise ("Cotacao Invalida")
        print("chegou aqui...")
    
    def converter(self):
        print (self.valorReal / self.cotacao) 

if __name__ == "__main__":

    cotacao = 0.00
    p = CalculoReal (cotacao,120.00)
    p.converter()

