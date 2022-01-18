num = int(input("Digite um número para verificar se ele é ou não primo: "))
cont = 0
for c in range(num-1, 1, -1):
    if num % c == 0:
        cont += 1
        break
if cont == 0:
    print("É um número primo")
else:
    print("Não é um número primo")
