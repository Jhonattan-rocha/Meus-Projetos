pa = int(input("Digite o primeiro termo da PA: "))
ra = int(input("Digite a razão da PA: "))

soma = pa
cont = 0
termos = 10
while cont != termos:
    print(cont+1, "° termo é = ", soma)
    soma = soma + ra
    cont += 1
    if cont == termos:
        escolha = int(input("Deseja continuar?(digite quantos termos quer ver o 0 para sair)"))
        termos += escolha

