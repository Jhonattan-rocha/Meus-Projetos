def area(l, c):
    a = l * c
    print(f"A área do terreno({l}x{c}) é {a} m^2")


print("!!!Programa para cálculo de uma área retangular!!!")
la = float(input("Digite a largura do terreno(M): "))
co = float(input("Digite o comprimento do terreno(M): "))

area(la, co)
