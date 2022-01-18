def metade(num):
    return float(num/2)


def dobro(num):
    return num*2


def aumentar(num, p):
    p = 1+(p/100)
    return float(num*p)


def diminuir(num, p):
    p = p/100
    return float(num - (num*p))
