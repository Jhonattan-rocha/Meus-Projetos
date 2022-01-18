escolha = ''
valores = list()
impares = list()
pares = list()
num = 0
while escolha != 'N':
    num = int(input("Digite um número: "))
    valores.append(num)
    escolha = input("Deseja continuar(S/N): ").upper()

for c in range(0, len(valores)):
    if int(valores[c]) % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])
print(f"A lista digitada é: {valores}")
print(f"Os números pares digitados é: {pares}")
print(f"Os números ímpares digitados é: {impares}")
