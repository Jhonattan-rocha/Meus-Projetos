from Curos_Python_curemvid.Uteis import Exer109M

numero = int(input("Digite quanto dinheiro você tem: R$"))
print(f"O dobro de R${numero} é: {Exer109M.dobro(numero, True)}")
print(f"A metade do R${numero} é: {Exer109M.metade(numero, True)}")
por = float(input("Digite o número da porcentagem que deseja aumentar o número: "))
print(f"R${numero} com {por}% de aumento é: {Exer109M.aumentar(numero, por, True)}")
por = float(input("Digite o número da porcentagem que deseja diminuir o número: "))
print(f"R${numero} com {por}% de desconto é: {Exer109M.diminuir(numero, por, True)}")
