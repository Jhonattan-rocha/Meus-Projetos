import random
numero = random.randint(0, 5)

print("Tente descobrir qual o número sorteado: ")
compara = int(input("Digite a sua tentativa: "))

if compara == numero:
    print("parabens, acertou")
else:
    print("Errou, tente de novo")
