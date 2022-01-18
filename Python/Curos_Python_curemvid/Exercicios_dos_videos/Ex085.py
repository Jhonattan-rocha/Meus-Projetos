valores = [[], []]
for c in range(0, 7):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(f"Os valores digitados pares: {valores[0]}")
print(f"Os valores digitados ímpares: {valores[1]}")
valores[0].sort()
valores[1].sort()
print(f"Os valores digitados pares em ordem crscente: {valores[0]}")
print(f"Os valores digitados ímpares em ordem crescente: {valores[1]}")
