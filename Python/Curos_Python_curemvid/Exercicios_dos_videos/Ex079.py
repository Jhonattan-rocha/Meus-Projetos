valores = []
escolha = ''
num = 0
c = 0
while escolha != 'N':
    num = int(input("Digite um valor(lembrar de sempre digitar valores diferentes): "))
    if num in valores and c > 0:
        print("Valor duplicado")
        valores.remove(num)
    valores.append(num)
    escolha = input("Deseja continuar(S/N): ").upper()
    c += 1
valores.sort()
print("O valores digitados em ordem é:", end='\n')
for c in range(0, len(valores)):
    print("O ", (c+1), f"° valore é: {valores[c]}")
