mediaidade = 0
nomeHM = ''
idadeMH = 0
quantiM = 0
for c in range(1, 5):
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo: ")
    idade = int(input("Digite sua idade: "))

    mediaidade += idade

    if c == 1 and sexo == 'Masculino':
        nomeHM = nome
        idadeMH = idade
    if c == 1 and sexo == 'Feminino' and idade < 20:
        quantiM += 1
    if sexo == 'Masculino' and idade > idadeMH:
        idadeMH = idade
    if sexo == 'Feminino' and idade < 20:
        quantiM += 1
print(f"A média de idade é: {mediaidade/4}")
print(f"A quantidade de mulheres com menos de 20 anos é {quantiM}")
print(f"O nome do homem mais velho é: {nomeHM}")
