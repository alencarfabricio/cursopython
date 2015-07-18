#Realizando a importacao das classes Pessoa e pessoa_bb q herda da classe Pessoa.
from pessoa import Pessoa
from pessoa_bb import BB
from pessoa_vovo import Vovo

#Instanciando um objeto do tipo BB
bb1 = BB ("FABRICIO","EDNA")    #bb1 não é uma variavel, ele é uma instancia da classe BB.
#Imprime o BB criado...
print("Nome: " + bb1.nome)
print("Mãe: " + bb1.mae)
#Método definido na super classe Pessoa
bb1.andar()
#Método definido na sub-classe BB
bb1.bicicleta()
#Método chorar da super classe
bb1.chorar()
print("-------------------------------------")
#Instanciando um objeto do tipo Pessoa
p1 = Pessoa ("João Miguel", "Emanuela Carvalho")
#Imprime a pessoa criada...
print("Nome: " +  p1.nome)
print("Mãe: " + p1.mae)
#Método definido na própria classe
p1.andar()
p1.chorar()
#isso vai dá merda federal!!!
#p1.bicicleta() # este método está definido na sub-classe, por isso nao funciona.
print("---------------------------------------")
#Instanciando uma nova vovo...
vo = Vovo()
#Setando o nome da vovo
vo.nome ="Maria do Amparo"
#Imprime o nome da vovo
print(vo.nome)
#Chamada ao metodo da sub-classe Vovo
vo.idade(59)
#Acesssando metodo sobrescrito da super classe
vo.andar()
