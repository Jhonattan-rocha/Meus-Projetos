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


def leiadinheiro(msg):
    num = str(input(msg)).replace(',', '.')
    while True:
        if num.isalpha():
            num = input("Digite novamento: ")
        else:
            num = float(num)
            break
    return num


def checapor(por):
    por = str(input(por)).replace(',', '.')
    while True:
        if por.isnumeric() or por.isdecimal():
            por = float(por)
            break
        else:
            por = input("Digite novamento: ")
            if float(por) <= 0 or float(por) > 100:
                por = input("Digite novamento: ")
    return por
