escolha = ''
totalgasto = 0
quantidade1000 = 0
maisbarato = ''
precomaisbarato = 0
cont = 0
while escolha != "N":
    nomeProd = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    cont += 1
    escolha = input("Deseja continuar(s/n): ").upper()

    totalgasto += preco
    if preco > 1000:
        quantidade1000 += 1
    if cont == 1:
        maisbarato = nomeProd
        precomaisbarato = preco
    else:
        if preco < precomaisbarato:
            maisbarato = nomeProd
            precomaisbarato = preco
print(f"O total de gastos com os produtos é: R${totalgasto}")
print(f"Você irá comprar {quantidade1000} produtos que custam mais que mil reais")
print(f"o nome do produto mais barato digitado é: {maisbarato}")
