velocidade = float(input("Digite a sua velocidade em Km/h: "))
if velocidade > 80:
    amais = velocidade - 80
    amais = amais*7
    print("Você foi multado, devera pagar uma multa de: R${:.2f}".format(amais))
print("FIM, não se mate")
