cont = 1
somatudo = 0
num = 0
while num != 999:
    num = int(input("Digite um número: "))
    somatudo += num
    cont+=1
print("A soma de tudo é: {}".format(somatudo-999))
print("Você digitou {} números".format(cont))
