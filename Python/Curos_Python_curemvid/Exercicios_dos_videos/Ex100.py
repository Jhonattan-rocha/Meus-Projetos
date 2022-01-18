from random import randint
from time import sleep


def sorteia(numeros):
    print("Sorteando os valores: ", end=' ')
    for c in range(0, 5):
        numeros.append(randint(0, 100))
        print(f"{numeros[c]}", end=' ')
        sleep(1)


def somapar(numerossoma):
    soma = 0
    for c in range(0, 5):
        if numerossoma[c] % 2 == 0:
            soma += numerossoma[c]
    print(f"\nA soma dos números pares entre os números:{numerossoma}, é {soma}")


Numeros = list()
sorteia(Numeros)
somapar(Numeros)
