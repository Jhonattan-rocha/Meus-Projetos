def metade(num, formata=False):
    if formata:
        return f"R${float(num / 2):.2f}"
    return float(num/2)


def dobro(num, formata=False):
    if formata:
        return f"R${float(num*2):.2f}"
    return num*2


def aumentar(num, p, formata=False):
    p = 1+(p/100)
    if formata:
        return f"R${float(num*p):.2f}"
    return float(num*p)


def diminuir(num, p, formata=False):
    p = p/100
    if formata:
        return f"R${float(num - (num*p)):.2f}"
    return float(num - (num*p))
