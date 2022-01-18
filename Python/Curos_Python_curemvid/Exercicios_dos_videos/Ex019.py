import random
n1 = input("Digite o primeiro nome: ")
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
n4 = input("Digite o quarto nome: ")

print("O nome sorteado é: {} ".format(random.choice([n1, n2, n3, n4]))) # método randomico para uma determinada lista
# de valores de qualquer tipo
