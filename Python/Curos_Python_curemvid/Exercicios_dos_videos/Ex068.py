from random import randint
cont = 0
while True:
    escolha = input("Qual você escolhe, par ou impar(p/i)? ").upper()
    if escolha != "P" and escolha != "I":
        print("Dado digitado é incorreto, digite novamente")
        continue
    n = int(input("Digite um número: "))
    cn = randint(1, 10)

    descobre = (n + cn) % 2

    if escolha == "P" and descobre == 0:
        print("Parabens, você ganhou")
        cont += 1
        continue
    if escolha == "I" and descobre == 1:
        print("Parabens, você ganhou")
        cont += 1
        continue
    if escolha == "P" and descobre == 1:
        print("YOUR LOSER")
        print(f"Você ganhou {cont} vezes")
        break
    if escolha == "I" and descobre == 0:
        print("YOUR LOSER")
        print(f"Você ganhou {cont} vezes")
        break
