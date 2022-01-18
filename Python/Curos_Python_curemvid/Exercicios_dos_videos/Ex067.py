cont = 1
while True:
    n = int(input("Digite um número: "))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {cont} = {n*cont}")
        cont += 1
        if c == 10:
            cont = 1
