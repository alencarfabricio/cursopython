#import random Aqui estou importando o modulo todo (nao e muito bom fazer isso)
from random import randint   # importe somente a funcao randint do modulo random
print("Bem vindo!!!")
#print (numero_sorteado)
novo_jogo = True
while novo_jogo != False:
    numero_sorteado = randint (1,100)
    contador = 1
    while True:
        chute = int(input("Chute um numero: "))
        if chute == numero_sorteado:
            print("Parabens, voce e foda.")
            break
        else:
            print("Alto" if chute > numero_sorteado else "Baixo")
        contador += 1
    print ("Fim de jogo!!!")
    print ("Numero sorteado: " + str(numero_sorteado))
    print ("Numero chutado: " + str(chute))
    print ("Numero de tentativas: " + str(contador))
    novo_jogo = int(input("Jogar novamente? 1 - Sim ou 0 - Nao:"))
