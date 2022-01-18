import random

compara = 0
numero = 1
cont = 0
while compara != numero:
    numero = random.randint(1, 11)

    print("Tente descobrir qual o número sorteado ")
    compara = int(input("Digite a sua tentativa:\n "))

    if compara == numero:
        print("parabens, acertou, você precisou de {} chances para vencer!!!!\n".format(cont))
    else:
        print("Errou, tente de novo\n")
        cont += 1
