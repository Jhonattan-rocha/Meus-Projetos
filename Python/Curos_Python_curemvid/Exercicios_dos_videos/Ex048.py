soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma = soma + c
print("A soma dos números ímpares de 1 a 500 e que são multiplos de 3 é: {}".format(soma))

