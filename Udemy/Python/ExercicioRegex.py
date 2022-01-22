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
telefones = """
998765432
22345678
9.9876.5432
2234.5678
22.34.5678
99876-5432
2234-5678
998-765-432
998.765.432
2234 5678
998 765 432
9 9876 5432

11998765432
1122345678
5511998765432
551122345678
+5511998765432
+551122345678
11 9.9876.5432
11 2234.5678
11 22.34.5678
11 99876-5432
11 9-9876-5432
11 2234-5678
11 998-765-432
11 998.765.432
11 2234 5678
11 22 34 5678
11 998 765 432
11 9 9876 5432

011 9.9876.5432
011 2234.5678
011 22.34.5678
011 99876-5432
011 2234-5678
011 998-765-432
011 998.765.432

(11)9.9876.5432
(11)2234.5678
(11)22.34.5678
(11)99876-5432
(11)2234-5678
(11)998-765-432
(11)998.765.432

(011)9.9876.5432
(011)2234.5678
(011)22.34.5678
(011)99876-5432
(011)2234-5678
(011)998-765-432
(011)998.765.432

(11)9.9876.5432
(11)2234.5678
(11)22.34.5678
(11)99876-5432
(11)2234-5678
(11)998-765-432
(11)998.765.432

(011) 9.9876.5432
(011) 2234.5678
(011) 22.34.5678
(011) 99876-5432
(011) 2234-5678
(011) 2234 5678
(011) 2234 56 78
(011) 22 34 56 78
(011) 998-765-432
(011) 998.765.432
(011) 998 765 432

(0xx11) 9.9876.5432
(0xx11) 2234.5678
(0xx11) 22.34.5678
(0xx11) 99876-5432
(0xx11) 2234-5678
(0xx11) 2234 5678
(0xx11) 2234 56 78
(0xx11) 22 34 56 78
(0xx11) 998-765-432
(0xx11) 998.765.432
(0xx11) 998 765 432

+55(11)9.9876.5432
+55(11)2234.5678
+55(11)22.34.5678
+55(11)99876-5432
+55(11)2234-5678
+55(11)998-765-432
+55(11)998.765.432

+55 (11) 9.9876.5432
+55 (11) 2234.5678
+55 (11) 22.34.5678
+55 (11) 99876-5432
+55 (11) 2234-5678
+55 (11) 2234 5678
+55 (11) 2234 56 78
+55 (11) 22 34 56 78
+55 (11) 998-765-432
+55 (11) 998.765.432
+55 (11) 998 765 432
"""

regex = re.compile(r'((?:\+?\s?5?5?\s?\(?0?x?x?1?1?\)?\s?)\d+[.\s-]?\d+[.\s-]?\d+\s?\d+)', flags=re.M)
tele = telefones.split("\n")

for c in range(len(tele)):
    reg = regex.findall(tele[c])
    print(tele[c], reg, tele[c] in reg[:])
