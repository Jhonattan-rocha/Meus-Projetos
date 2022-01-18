num = int(input("Digite um número: "))
aux = num - 1
while aux != 0:
    num = aux * num
    aux = aux - 1
print("O fatorial desse número é: {}".format(num))
