text = str(input("Digite o seu nome completo: "))

print("O nome completo com todas as lestras maiúsculas é: {}".format(text.upper()))
print("O nome completo com todas as letras minúsculas é: {}".format(text.lower()))

divido = text.split()
quant = int(len(text) - len(divido) + 1)

print("A quantidade de letras sem espaço é: {}".format(quant))
print("O primeiro nome tem {} letras".format(len(divido[0])))
