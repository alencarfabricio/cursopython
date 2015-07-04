# Desafios - POO 04.07.2015
# 1 - Crie um programa que calcule valores reais em dolares;
# 2 - Converta em pes a altura de uma pessoa;
# 3 - Calcule a capacidade maxima de pessoas dentro de uma sala;

######################################################################
# Aplicativo para converter valores de real para dólar               #
# converterRealDolar.py - versão 0.1                                 #
# Por: Fabricio Alencar                                              #
# Data : 04.07.2015                                                  #
# Obs : USANDO CLASSE E METODO                                       #
######################################################################

class CalculoReal(object):

    def converter(self):
        #print(valor = float(raw_input("Informe valor em Real :")))
        valord = float(raw_input('Qual a cotação atual do dólar em reais? '))
        valorr = float(raw_input('Qual valore em real que deseja converter para dolar ? '))
        total = valorr / valord
        print 'Seu valor em dólares fica: U$ %.2f' %total     #% mascara e 2f duas casas decimais.

    def pesxaltura(self);
        #falta criar o metodo

    def capacixsala(self):
        #falta criar o metodo
        
       
p = CalculoReal()
p.converter()
        
"""
######################################################################
# Aplicativo para converter valores de real para dólar ou vice versa #
# converterRealDolar.py - versão 0.1                                 #
# Por: Fabricio Alencar                                              #
# Data : 04.07.2015                                                  #
# Obs : USANDO WHILE E IF                                            #
######################################################################                    


import os

while 1:
   os.system('clear')
   print ("Bem vindo ao converte!")
   print "Digite o numero da opcao desejada: \n","1- Converter de dólar para real \n",      "2- Converter de real para dolar \n",     "3- Sair"
   opcao = int(raw_input('Digite aqui: '))
   if opcao == 1:
      dolar = float(raw_input('Qual a cotação atual do dólar em reais? '))
      valor = float(raw_input('Qual o valor em dólar do produto que você deseja converter para reais? '))
      total = dolar * valor
      print 'Seu valor em reais fica: R$ %.2f.' %total
      raw_input('Pressione qualquer tecla para continuar')
      
   if opcao == 2:
      dolar = float(raw_input('Qual a cotação atual do dólar em reais? '))
      valor = float(raw_input('Qual o valor em reais do produto que você deseja converter para dólares? '))
      total = valor / dolar
      print 'Seu valor em dólares fica: U$ %.2f.' %total
      raw_input('Pressione qualquer tecla para continuar')
   if opcao == 3:
      print 'Encerrando.......'
      break
"""

