import re

# python é uma linguagens de tipagem dinâmica
# caractere de escaoe, exemplo: "\
# qualquer dado vazio retornam false caso faça um casting para bool, e retorna true se não for vazio
print(bool(""), bool("jhonattan"))
# ** potência
# // divisão inteira
print('Teste {0} de {0} format {0}'.format("Nada"))
# é possível nomear as casas com seus indices para caso queira repetir um dado mais de uma vez
# é possível nomear com outros tipos de dados,como textos por exemplo, mas você vai ter que especificar
# qual dado vai para qual variável
b = 0


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


# essas defs o professor disponibilizou para contornar o problema dos metodos que já vem no python
# isdecimal é uma função que checa com mais abrangencia uma string, pois o isnumeric retorna false se for menor que zero
# isdecimal não verifica ponto flutuante

"""
formatando valores:

:s - strings
:d - int
:f - float
:(numero)f - limita as casas decimais
:(caractere)(> ou < or ^)(Quantidade)(tipo - s, d, f)

> - esquerda
< - direita
^ - centro

"""

print(f"{1:0>10}")
var = 'as'
print(f"{var:#^50}")

print(is_int(var), is_number(var), is_float(var))

print("{n}".format(n="Nome"))

var = var.ljust(20, "%")
print(var)
print(var.title())
print(var.casefold())

# [começo:fim:passo] - como funciona o fatiamento de strings
# no python, as classes iteraveis sempre contam até o indice -1 do que vc colocou

num = 1
while num <= 10:
    print(num)
    num += 1
else:
    print("esse bloco é executado quando a expressão for falsa, no for a mesma coisa")
    print("ele só passa por aqui se a expressão for falsa, logo se for parado por outro motivo, isso não é executado")

lista = [1]
lista.append(0)
print(lista)
lista.insert(0, 5)
print(lista)
lista.pop(1)
print(lista)
del (lista[0])
print(lista)
lista = [0, 1, 2, 2, 2]
lista.clear()
print(lista)
lista.extend("asdasdad")  # junta duas listas
print(lista)

lista = [str(i) for i in range(0, 100)]
# print(min(lista))
# print(max(lista))

# como inverter uma lista de forma simples
print(lista[::-1])

print(list(range(0, 10)))

varss = ' '.join(lista)  # o join junta uma lista em uma str
print(varss)

# é possível colocar mais de uma varável no for caso a variável iterável que estiver utilizando, ter outros objetos dentro
# em vez de apenas o valor, por exemplo

listas = [
    [0, 1],
    [0, 2],
    [0, 3]
]

for p, s in listas:
    print(p, s)

# exemplo com enumerate

for p, s in enumerate(listas):
    print(p, s[0])

*lista1, lista2, lista3, ultimo, ultimo2 = lista

print(lista1)
print(lista2)
print(lista3)
print(ultimo)
print(ultimo2)

# esse desempacotamento vai alocuando so valores nas variáveis postas, quando chega em uma com o *, ele vai pegando
# todos os valores possíveis mas se tiver mais variáveis depois do *, ele separa a quantidade de dados necessário
# para preencher as outras variáveis


# como inverter o valor de variáveis de forma simples

x = 1
y = 2

x, y = y, x
print(x, y)

teste = "true" if x == 2 else "false"
print(teste)

nome = "luiz"

print(nome or "você não digitou nada")

# em python, se a variável tem algum valor, em booleano é considerada True, se não é false, operações com or permite
# você criar condições simplificadas, como por exemplo o print a cima, que o or decide qual será exibido,
# o nome se tiver algum valor, ou a string ao lado
# essas expressões para na primeira condição True

# 0 None [] {} "" são considerados False no tipo booleano
