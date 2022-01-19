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

if not b:
    print(b)

# essa expressão é usada para saber se tem um valor na variável, o 0 e "" é considerado false, qualquer outra coisa, true

print("teste".__len__())  # funciona igual ao len()




def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^?[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^?[0-9]+$', val): return True

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

print()
