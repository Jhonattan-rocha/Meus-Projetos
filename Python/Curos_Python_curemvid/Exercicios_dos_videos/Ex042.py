l1 = float(input("Digite o valor de uma reta: "))
l2 = float(input("Digite o valor da outra reta: "))
l3 = float(input("Digite o valor da outra reta: "))

if l1+l2 >= l3 and l2 + l3 >= l1 and l3 + l1 >= l2:
    print("Pode ser feito um triangulos com essas retas")
    if l1 == l2 == l3:
        print("O triângulo é equilátero")
    elif l1 != l2 != l3 != l1:
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isósceles")
else:
    print("Não é possível fazer um triangulo")


