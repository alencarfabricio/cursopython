class Pessoa(object):
    # Declaraçao de atributo da classe
    nome = " "
    idade = 0
    
    # Criando um construtor onde eu defino que agora terei q passar um parametro nome
    def __init__(self, nome):
        self.nome = nome

    # Criando meu metodo 
    def andar(self):
        print("A pessoa esta andando...")
    
#Instanciamos o objeto
#p = Pessoa()
 p = Pessoa ("Francisco Andre")       
# definimos o valor do atributo nome
#p.nome = "Francisco Andre"
# definimos o valor do atributo idade
p.idade = 34
# faz a impressao dos valores do atributos
print ("NOme:",p.nome, "Idade:", p.idade)
print (p.idade)
p.andar()
