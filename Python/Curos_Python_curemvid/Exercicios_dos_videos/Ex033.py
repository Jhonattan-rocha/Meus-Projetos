n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número"))

if n3 < n1 > n2:
    print("O maior número é {}".format(n1))
    if n2 > n3:
        print("O menor número é: {}".format(n3))
    else:
        print("O menor número é: {}".format(n2))
elif n3 < n2 > n1:
    if n1 > n3:
        print("O menor número é: {}".format(n3))
    else:
        print("O menor número é: {}".format(n1))
else:
    if n2 > n1:
        print("O menor número é: {}".format(n1))
    else:
        print("O menor número é: {}".format(n2))
