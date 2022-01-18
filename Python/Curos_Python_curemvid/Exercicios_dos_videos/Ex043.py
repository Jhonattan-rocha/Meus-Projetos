Altura = float(input("Digite sua altura: "))
Peso = float(input("Digite seu peso: "))

IMC = Peso / (Altura * Altura)

print("Seu IMC é: {:.2f}".format(IMC))

if IMC < 18.5:
    print("E você está abaixo do peso.")
elif 18.5 < IMC < 25:
    print("peso ideal")
elif 25 < IMC > 30:
    print("Gordo")
elif 30 < IMC > 40:
    print("Gordo para caramba")
else:
    print("Tu tá vivo ainda ?")
