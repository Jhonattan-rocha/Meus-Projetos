def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print("Digite um número válido")
    return valor


num = leiaint("digite um número inteiro: ")
print(f"Você digitou o número {num}")
