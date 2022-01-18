print("Banco")

v = int(input("Digite o valor que deseja sacar: "))
total = v
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"A quantidade de cédulos de {ced} reas é: {totalced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

v = int(input("Digite o valor que deseja sacar: "))
total = v
ced2 = 0
resto = 0
if total >= 50:
    ced2 = int(total / 50)
    resto = total - (ced2 * 50)
    print(f"A notas de 50 são {ced2} notas")
if resto >= 20:
    ced2 = int(resto / 20)
    resto = resto - (ced2 * 20)
    print(f"A notas de 20 são {ced2} notas")
if resto >= 10:
    ced2 = int(resto / 10)
    resto = resto - (ced2 * 10)
    print(f"A notas de 10 são {ced2} notas")
if resto != 0:
    ced2 = int(resto / 1)
    resto = resto - (ced2 * 1)
    print(f"A notas de 1 são {ced2} notas")
