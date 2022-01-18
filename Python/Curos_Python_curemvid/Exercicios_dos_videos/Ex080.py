valores = []
for c in range(0, 10):
    num = int(input('Digite um número: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
    else:
        aux = 0
        while aux < len(valores):
            if num <= valores[aux]:
                valores.insert(aux, num)
                break
            aux += 1
print(f"O valores digitados em ordem é: {valores}", end='\n')

