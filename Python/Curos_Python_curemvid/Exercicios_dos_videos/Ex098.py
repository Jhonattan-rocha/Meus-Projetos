def contador(i, f, p):
    arruma = +1
    if p == 0:
        p = 1
    if p < 0:
        p = (p*(-1))
    if i > f:
        p = (p*(-1))
        arruma = -1
    for c in range(i, (f+arruma), p):
        print(f"{c}", end=' ')


print("!!!Este é um programa de contador!!!")
print("A primeira contagem é pré definida, sendo de 1 ao 10, inde de 1 em 1: ")
print("A contagem é: ", end=' ')
contador(1, 10, 1)
print("\nA segunda contagem também é pré definida, sendo de 10 ao 0, inde de 2 em 2: ")
print("A contagem é: ", end=' ')
contador(10, 0, 2)
print("\nA terceira contagem é personalizada!!!")
inicio = int(input("Digite um número inteiro para ser o ínicio: "))
fim = int(input("Digite um número inteiro para ser o fim: "))
passo = int(input("Digite um número inteiro para ser o passo: "))
print("A contagem é: ", end=' ')
contador(inicio, fim, passo)
