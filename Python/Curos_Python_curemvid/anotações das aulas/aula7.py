n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

print("A soma é: {} ".format(n1 + n2), end='')
print("A subtração é: {} ".format(n1 - n2))
print("A multiplicação é: {} ".format(n1 * n2))
print("A divisão é: {:.2f} ".format(n1 / n2))  # essa é a formatação para as casas decimais limitadas
print("A potenciação é: {} ".format(n1 ** n2))
print("A divisão inteira é: {} ".format(n1 // n2))
