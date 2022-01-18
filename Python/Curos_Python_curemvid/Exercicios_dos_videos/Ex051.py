pa = int(input("Digite o primeiro termo da PA: "))
ra = int(input("Digite a razão da PA: "))

soma = pa
for c in range(1, 11):
    print(c, "° = ", soma)
    soma = soma + ra
