ano = int(input("Digite o ano de nascimento: "))

idade = 2021 - ano

if idade <= 9:
    print("MIRIM")
elif 9 < idade <= 14:
    print("INFANTIL")
elif 14 < idade <= 19:
    print("JUNIOR")
elif idade == 20:
    print("SêNIOR")
else:
    print("MASTER")
