valores = list()
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
    if c == 0:
        maior = int(valores[c])
        menor = int(valores[c])
    else:
        if maior < int(valores[c]):
            maior = int(valores[c])
        elif menor > int(valores[c]):
            menor = int(valores[c])
print(f"O maior número é {maior} e sua posição é ", end='')
for c, i in enumerate(valores):
    if i == maior:
        print(f'{c:.<3}', end='')
print(f"\nO menor número é {menor} e sua posição é ", end='')
for c2, i2 in enumerate(valores):
    if i2 == menor:
        print(f'{c2:.<3}', end='')
