import re


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^-?[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^-?[0-9]+$', val):
        return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


# faça a pontuação ser opcional
cpf = '77284380934'
regex_sem_tem_pontuacao = re.findall(r'(\d+\.?\d+\.?\d+-?\d+)', cpf, flags=re.I)
print(regex_sem_tem_pontuacao)
print('-'*50)
# faça a pontuação aceitar espaços e uma barra antes dos dois ultimos numeros
cpf = '772.843.809-34'
regex_sem_tem_pontuacao = re.findall(r'(\d+[.\s]?\d+[.\s]?\d+[-/]?\d+)', cpf, flags=re.I)
print(regex_sem_tem_pontuacao)
print('-'*50)
# Escreva uma regex capaz de encontrar no texto deste parágrafo todas as palavras que teriminam com a letra “o”
paragrafo = 'Escreva uma regex capaz de encontrar no texto deste parágrafo todas as palavras que teriminam com a letra'
regex = re.findall(r'\w+o\b', paragrafo, flags=re.IGNORECASE)
print(regex)
print('-'*50)
# Escreva uma regex capas de encontrar no parágrafo acima todas as palavras que começam e terminam com vogais
paragrafo = 'Escreva uma regex capaz de encontrar no texto deste parágrafo todas as palavras que teriminam com a letra'
regex = re.findall(r'\w*[aeiou]\b', paragrafo, flags=re.IGNORECASE)
print(regex)
print('-'*50)
# Na seção Algums exemplos da Introdução foi apresentada a expressão regular [012]\d:[0-5]\d para validar horas
# e minutos no formato HH:MM. Porém esta regex aceita o texto 25:00 que não é uma hora válida. Modifique a regex para
# corrigir esta falha. A solução envolve o uso
hora = '23:59'
regex = re.findall(r'^[012][0-3]:[0-5]\d$', hora, flags=re.IGNORECASE)
print(regex)
print('-'*50)
# Escreva uma regex que valide um octeto em ipv4
octeto = '255'
regex = re.findall(r'\b(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])(?:\.?|$)\b', octeto)
print(regex)
print('-'*50)
# Faça a validação de um IPV4, Ex: 192.168.0.1
octetos = '255.268.0.1'
regex = re.findall(r'\b(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])(?:\.?|$)\b', octetos, flags=re.IGNORECASE)
print(regex)
print('-'*50)

print(is_int("-1.0"), is_float("-1"), is_number("145"))
