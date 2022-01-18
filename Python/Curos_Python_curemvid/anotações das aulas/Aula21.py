def contador(i, f, p=0):
    """
    Resumo: realiza uma contagem de acordo com a necessídade do programador.
    :param i: - ínicio da sua contagem
    :param f: - final da sua contagem
    :param p: - passo em que a contagem ocorrerá(exemplo: p = 2, a contagem será de 2 em 2)
    :return: - sem retorno
    """
    arruma = +1
    if p == 0:
        p = 1
    if p < 0:
        p = (p * (-1))
    if i > f:
        p = (p * (-1))
        arruma = -1
    for c in range(i, (f + arruma), p):
        print(f"{c}", end=' ')


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f"O FATORIAL DE {n} É {fatorial(n)}")
help(contador)

contador(10, 0, -2)

resp = soma(3, 2) or print(soma(3, 2))

print(resp)
