import re
from pprint import pprint

# findall - encontra todas as ocorrencias do padrão falado
# search - encontra a primeira ocorrencia de um padrão e retorna um objeto match
# sub - subistitui coisas em texto
# compile - compila regex

string = "Este é um teste de regex"

print(re.search(r'teste', string))
print(re.findall(r'teste', string))  # retorna uma lista com todas as palavras encrontradas
print(re.sub(r'teste', "abcd", string, count=1))  # count limita o número de substituições, 0 substitui todos
print('-'*100)
regex = re.compile(r'teste') # compilando expressões regulares
print(regex.search(string))
print(regex.findall(string))
print(regex.sub("teste2", string))

"----------------------------------------------------------------"

# metacaracteres
# ^ $ * + ? { } [ ] \ | ( )
# | - siginifica OU em regex
# . - qualquer caractere(menos quebra de linha)
# [] - conjunto de caracteres, em determinada parte da string, vc coloca os caracteres que podem estar ali tudo junto
# quantificadores: - são aplicados ao caractere que estiver a esquerda dele
# * - significa 0 ou n vezes - por padrão, esse é greed
# + - significa 1 ou n vezes - por padrão, esse é greed
# ? - significa 0 ou 1 vezes - coloando esse aqui do lado de outro quantificador, faz ele trabalhar de forma não lazy
# {} - pode colocar para procurar n repetições, ou limitar o min e o max, se tiver apenas um número, é especificamente
# aquele numero
# para que um conjunto considere mais de uma letra, é preciso colocar o quantificador com a quantidade de
# letras que vc quer procurar
# () - grupos - procura especificamente o que for colocado, se usar isso, ele acaba fazendo com que retorne
# apenas o que foi agrupado, para acessar um grupo, usa-se retrovisores, que começa a contar do 1(\1, \2, \3...)
# conta-se da esquerda para a direita, e não conta de dentro para fora, não faz diferença
# caso eu queria não salvar um grupo, coloca dentro dele na frede do conteudo ?:
# em python, é possível criar grupos nomeados usando ?P<(nome do grupo)>
# para acessar o grupo pelo nomé usa (?P=(nome do grupo))
# ^ - começa com, com isso vc fala que a expressão começa obrigatóriamente o que estiver a direita
# este operador dentro de um conjunto, torna-se negação, ex: [^a-z] isso traz qualquer coisa que não esteja entre a e z
loren = """<p>Fasê 1</p> <p>eita</p> <p>Qualquer fráse</p> <div></div> opo"""

print(re.findall(r'Então|s[a-z]', loren))
print(re.findall(r'm....', loren))
print(re.findall(r's....', loren))
print(re.findall(r'[a-z]tindo', loren))
print(re.findall(r'[a-z]...', loren))
# dessa forma, é possível mandar um intervalo de caracteres inteiro
# é possível mandar mais de um range de uma vez

print(re.findall(r'Nu[a-zA-z]', loren, flags=re.IGNORECASE))  # ou apenas re.I
# flags mudam o comportamento das regex
print(re.findall(r'apó+s|pare+c+e', loren, flags=re.I))
print(re.findall(r'apó{1,}s|pare{1,}c{1,}e', loren, flags=re.I))
print("-"*100)
# quantificadores greed e non-greed(lazy)
print(re.findall(r"<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>", loren))
print(re.findall(r"<([dpiv]{1,3})>.*?<\/\1>", loren))
pprint(re.findall(r"(<([dpiv]{1,3})>.*?<\/\2>)", loren))
pprint(re.findall(r"(<([dpiv]{1,3})>(.*?)<\/\2>)", loren))
pprint(re.findall(r"(<([dpiv]{1,3})>(.*?)<\/\2>)", loren))

print("-"*100)
pprint(re.sub(r"(<(.+?)>)(.+?)(</\2>)", r"\1'\3'\4", loren))
cpf = '111.222.333-44'
print(re.findall(r"((?:[0-9]{3}[.-]){3}[0-9]{2})", cpf, flags=re.I))
print(re.findall(r"^((?:[0-9]{3}[.-]){3}[0-9]{2})$", cpf, flags=re.I))

# como pegar letras acentuadas com re
print(re.findall(r"[a-zA-ZÀ-ú]+", loren))
# isso aqui inclui quase todos os caracteres de alfabeto do mundo
print(re.findall(r"\w+", loren))
# essa flag pega apenas os caracteres da tabel ascii
print(re.findall(r"\w+", loren, flags=re.ASCII))
# esse aqui é a negação do anterior
print(re.findall(r"\W+", loren, flags=re.I))
# esse aqui pega os numeros
print(re.findall(r"\d+", loren, flags=re.I))
# esse aqui é a negação
print(re.findall(r"\D+", loren, flags=re.I))
# esse aqui reconhece qualquer espaço
print(re.findall(r"\s+", loren, flags=re.I))
# esse aqui é a negação
print(re.findall(r"\S+", loren, flags=re.I))
# esse aqui encontra uma string vazia no começou ou no fim de cada palavra
print(re.findall(r"\be\w+", loren, flags=re.I))  # procura palavra que termina com e
print(re.findall(r"\w+e\b", loren, flags=re.I))  # procura palavras que comece por e
print(re.findall(r"\b\w{4}\b", loren, flags=re.I))  # procura palavras com 4 letras
# esse aqui é a negação
print(re.findall(r"\w+\Be", loren, flags=re.I)) # tem que ter letras antes, não pode ter uma borda, e tem que acabar com e
print(re.findall(r"\w+\Bp\w+", loren, flags=re.I))

"----------------------------------------------------------"

# re.A - ascii
# re.I - ignorecase
# re.M - multiple - altera esses caracteres ^ $, em vez de ser fim e começo da string, viram começo e fim de cada linha
# re.S - dotall - reconhece as quebras de linha

cpfs = """
111.222.333-22 teste
111.222.333-22 teste2
112.222.333-22 teste
111.222.333-22 teste2
111.222.333-22 teste
"""

print(re.findall(r"((?:\d{3}[.-]){3}\d{2})", cpfs, flags=re.I | re.S))
# positive lookeahead
# lookeahead e lookbehind
print(re.findall(r'\d+\.(\d+)\.\d+-\d+\s+(?=teste2)', cpfs, flags=re.S))
# negative lookeahead
# lookeahead e lookbehind
print(re.findall(r'\d+\.(\d+)\.\d+-\d+\s+(?!teste2)', cpfs, flags=re.S))

# positive lookbehind
# lookeahead e lookbehind
print(re.findall(r'\d+\.(?<=111\.)\d+\.\d+-\d+\s+\w+', cpfs, flags=re.S))
# negative lookbehind
# lookeahead e lookbehind
print(re.findall(r'\d+\.(?<!111\.)\d+\.\d+-\d+\s+\w+', cpfs, flags=re.S))
regex = re.compile(r"""""", flags=re.VERBOSE)  # permite cometar na expressão
