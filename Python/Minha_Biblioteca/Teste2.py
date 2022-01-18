def Enumero(digitado=""):
    veredito = True
    digitado = str(digitado)
    for c in range(0, len(digitado)):
        for l in range(0, 10):
            if digitado[c] not in " 0123456789":
                veredito = False
                break
        if not veredito:
            break
    return veredito


def LetraNumero(text=''):
    arquivo = open('Asciiz.txt', 'r', encoding='utf-8')
    tabela = arquivo.read()
    tabela = tabela.split()
    re = ''
    for y in range(0, len(text)):
        if text[y] == ' ':
            re += ('00100000' + ' ')
            continue
        for x in range(0, len(tabela)):
            if text[y] == tabela[x]:
                re += (tabela[x - 1] + ' ')
    return re


def NumeroLetra(text=''):
    text = text.split()
    arquivo = open('Asciiz.txt', 'r', encoding='utf-8')
    tabela = arquivo.read()
    tabela = tabela.split()
    re = ''
    for c in range(0, len(text)):
        if len(text[c]) // 8 == 1:
            for l in range(0, len(tabela)):
                if tabela[l] == text[c]:
                    re += (tabela[l+1])
        else:
            if len(text[c]) // 8 > 1:
                cont = 0
                for t2 in range(0, len(text[c]) // 8):
                    for t in range(0, len(tabela)):
                        if text[c][cont:cont + 8] == tabela[t]:
                            re += (tabela[t+1])
                            cont += 8
            else:
                return '\nAlgum dado é inválido'
    return re


if __name__ == '__main__':
    texto = str(input('Digite alguma coisa: '))
    print(NumeroLetra(texto))
    print(LetraNumero(texto))
