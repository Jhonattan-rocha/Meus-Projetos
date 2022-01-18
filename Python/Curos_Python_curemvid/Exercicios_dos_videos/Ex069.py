escolha = ''
maioresdeidade = 0
quantidadeHomens = 0
MulheresMais20 = 0
idade = 0
sexo = ''

while escolha != "N":
    idade = int(input("Digite sua idade: "))
    if idade > 110 or idade < 0:
        print("Dado digitado é inválido, digite novamente")
        continue
    sexo = str(input("Digite seu sexo: ")).upper()
    if sexo != "M" and sexo != "F":
        print("Dado digitado é inválido, digite novamente")
        continue
    escolha = input("Deseja continuar(s/n): ").upper()

    if idade > 18:
        maioresdeidade += 1
    if sexo == "M":
        quantidadeHomens += 1
    if sexo == "F" and idade > 20:
        MulheresMais20 += 1
print(f"A quantidade de pessoas maiores de idade é: {maioresdeidade}")
print(f"A quantidade de homens cadastrados é: {quantidadeHomens}")
print(f"A quantidade de mulheres com mais de 20 anos é: {MulheresMais20}")
