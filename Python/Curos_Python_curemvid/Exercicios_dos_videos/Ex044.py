preco = float(input("Digite o preço do produto: "))
tipo = int(input("""Digite a forma de pagamentos:
                1 - Dinheiro/Cheque:
                2 - Cartão a vista:
                3 - para 2x no cartão:
                4 - para 3x ou mais no cartão:\n"""))
if tipo == 1:
    preco = preco - (preco*0.1)
    print("O novo preço a ser pago com 10% de desconto é: {}".format(preco))
elif tipo == 2:
    preco = preco - (preco * 0.05)
    print("O novo preço a ser pago com 5% de desconto é: {}".format(preco))
elif tipo == 3:
    print("O preço a ser pago é o mesmo")
else:
    preco = preco * 1.2
    print("O novo preço a ser pago com 20% de juros é: {}".format(preco))
