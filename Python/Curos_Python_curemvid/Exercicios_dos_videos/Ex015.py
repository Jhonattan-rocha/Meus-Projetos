dias = int(input("Digite quantos dias o carro foi alugado: "))
km = float(input("Digite quantos KM você rodou: "))

preco = (dias * 60) + (km*0.15)

print("O valor a ser pago de aluguel é: {:.2f}".format(preco))
