from Curos_Python_curemvid.Uteis import Exer108M

numero = int(input("Digite quanto dinheiro você tem: "))
print(f"O dobro de {Exer108M.formatar(numero)} é: {Exer108M.formatar(Exer108M.dobro(numero))}")
print(f"A metade do {Exer108M.formatar(numero)} é: {Exer108M.formatar(Exer108M.metade(numero))}")
por = float(input("Digite o número da porcentagem que deseja aumentar o número: "))
print(f"{Exer108M.formatar(numero)} com {por}% de aumento é: {Exer108M.formatar(Exer108M.aumentar(numero, por))}")
por = float(input("Digite o número da porcentagem que deseja diminuir o número: "))
print(f"{Exer108M.formatar(numero)} com {por}% de desconto é: {Exer108M.formatar(Exer108M.diminuir(numero, por))}")
