n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = float((n1 + n2 + n3 + n4) / 4)

if media >= 6:
    print("Afrovado")
else:
    if 6 >= media >= 3:
        print("Exame")
    else:
        print("Reprovado")

print("parabens" if media > 9 else "estude mais, se mate de estudar")

print("Continue estudando bastante")
