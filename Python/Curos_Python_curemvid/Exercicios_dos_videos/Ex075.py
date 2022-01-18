escolha = (int(input("Digite um valor: ")), int(input("Digite outro valor: ")), int(input("Digite outro valor: ")),
           int(input("Digite outro valor: ")))
print(f"O valor 9 apareceu {escolha.count(9)} vezes")
verifica = False
if 3 in escolha:
    print(f"O valor 3 aparece primeiramente na posição: {(escolha.index(3) + 1)}")
else:
    print("O valor 3 não foi digitado")
cont = 0
for c in range(0, 4):
    compara = int(escolha[c])
    if compara % 2 == 0:
        print("O ", (c + 1), "° valor é par")
        cont += 1
if cont == 0:
    print("Não foram digitados números que são pares")
