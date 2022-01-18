from math import sqrt
c1 = float(input("Digite o comprimento de um dos catetos: "))
c2 = float(input("Digite o comprimento do segundo cateto: "))

h = c1**2 + c2**2
h = sqrt(h)

print("A hipotenusa do triangulo é: {}".format(h))
