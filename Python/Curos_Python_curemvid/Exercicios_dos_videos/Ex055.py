cont = 0
for c in range(1, 8):
    ano = int(input("Digite o ano de nascimento da pessoa: "))
    if 2021 - ano >= 21:
        cont += 1
print("A quantidade de pessoas que atigiram a maior idade é {}, e as que não é {}".format(cont, 7-cont))
