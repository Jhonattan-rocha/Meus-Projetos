from Curos_Python_curemvid.Uteis import Exer107M

numero = int(input("Digite quanto dinheiro você tem: "))
print(f"O dobro de {numero} é: {Exer107M.dobro(numero)}")
print(f"A metade do {numero} é: {Exer107M.metade(numero)}")
por = float(input("Digite o número da porcentagem que deseja aumentar o número: "))
print(f"{numero} com {por}% de aumento é: {Exer107M.aumentar(numero, por)}")
por = float(input("Digite o número da porcentagem que deseja diminuir o número: "))
print(f"{numero} com {por}% de desconto é: {Exer107M.diminuir(numero, por)}")
