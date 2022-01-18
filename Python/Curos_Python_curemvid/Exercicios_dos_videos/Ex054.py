frase = input("Digite alguma coisa: ")
frase = frase.replace(' ', ',')
aux = ''
for c in range(0, len(frase)):
    aux += frase[len(frase)-(1+c)]
if aux == frase:
    print("A frase é um palindromo")
else:
    print("a frasse não é um palindromo")