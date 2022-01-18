from random import randint
from time import sleep
valores = list()
jogo = list()
aux = 0
escolha = int(input("Digite quantos jogos serão feitos: "))

for c in range(0, escolha):
    for c2 in range(0, 6):
        aux = randint(1, 60)
        if aux in valores and c2 > 0:
            print("Valor duplicado")
            jogo.pop(c2)
        else:
            jogo.append(aux)
    valores.append(jogo[:])
    jogo.clear()

for b in range(0, escolha):
    print()
    sleep(1)
    print(f'O {(b+1)}° é para palpite é: ', end=' ')
    print(f" {valores[b]} ", end=' ')
