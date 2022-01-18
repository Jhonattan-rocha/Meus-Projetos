import random

n1 = input("Digite o primeiro nome: ")
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
n4 = input("Digite o quarto nome: ")
em = [n1, n2, n3, n4]
random.shuffle(em)
print("A ordem sorteada é:")  # metodo que embaralha uma lista de valores
print(em)
