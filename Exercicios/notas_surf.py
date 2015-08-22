f = open ("surf.txt", "r")
notas = {}  # Criando um dicionario

for linha in f:
    nome, pontos = linha.split()  # Pegando a linha do arquivo.
    notas[float(pontos)] = nome   #Acessando o dicionario e o float e pra trazer as casas decimais
f.close()
for nota in sorted(notas, reverse=True):   # reverse mudar a cor da fonte
    print("%s tem %4.2f" % (notas[nota], nota))
    
