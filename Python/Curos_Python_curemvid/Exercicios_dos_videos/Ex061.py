pa = int(input("Digite o primeiro termo da PA: "))
ra = int(input("Digite a razão da PA: "))

soma = pa
cont = 1
while cont != 11:
    print(cont, "° termo é = ", soma)
    soma = soma + ra
    cont += 1
