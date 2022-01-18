maior = 0
menor = 0
media = 0
cont = 0
escolha = ''
while escolha != "N":
    num = float(input("Digite um número: "))
    cont += 1
    media += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    escolha = str(input("Deseja continuar a digitar(S/N)")).upper()
print("O maior número foi: {}".format(maior))
print("O menor número foi: {}".format(menor))
print("A media é: {}".format(media/cont))
