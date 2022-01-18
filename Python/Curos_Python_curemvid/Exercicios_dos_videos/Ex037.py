
num = int(input("Digite o número a ser convertido: "))
base = int(input("Digite a base que deseja converter(2, 8 ou 16): "))

if base == 2:
    print("O número em binário é: {}".format(bin(num)))
elif base == 8:
    print("O número em octal é: {}".format(oct(num)))
else:
    print("O número em hexadecimal é: {}".format(hex(num)))
