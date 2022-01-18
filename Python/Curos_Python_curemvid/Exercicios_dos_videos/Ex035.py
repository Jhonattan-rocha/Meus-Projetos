l1 = float(input("Digite o valor de uma reta: "))
l2 = float(input("Digite o valor da outra reta: "))
l3 = float(input("Digite o valor da outra reta: "))

if l1+l2 >= l3:
    if l2 + l3 >= l1:
        if l3 + l1 >= l2:
            print("Pode ser feito um triangulos com essas retas")
        else:
            print("Não é possível fazer um triangulo")
    else:
        print("Não é possível fazer um triangulo")
else:
    print("Não é possível fazer um triangulo")

