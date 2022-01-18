resto = 0
div = 0
div2 = 0
resultado = 0
convbase10 = 0
conv = "."
hexadecimal = ['A', 'B', 'C', 'D', 'E', 'F']
num2 = 0
sinalNegativo = False

num = str(input("Digite um número para ser convertido: ")).upper()
if num[0] == "-":
    num = num[1:]
    sinalNegativo = True
basenum = int(input("Digite a base do número: "))
if basenum < 2 or basenum > 16:
    print("A base do número está errada, digite novamente")
    exit()
base = int(input("Digite a base que deseja converter o numero: "))
if basenum < 2 or basenum > 16:
    print("A base para conversão está errada, digite novamente")
    exit()
indice = len(num) - 1

# calculando o corespondente do número digitado para ser convertido, na base 10
for c in range(0, len(num)):
    cont = 10
    if num[c] in 'ABCDEF':
        for l in range(0, 6):
            if num[c] == hexadecimal[l]:
                num2 = cont
            cont += 1
    if num[c] not in 'ABCDEF':
        num2 = int(num[c])
    convbase10 += (num2 * (basenum ** indice))
    indice -= 1
if basenum != 10:
    if sinalNegativo:
        print(f"O número na base 10 é -{convbase10}")
    else:
        print(f"O número na base 10 é {convbase10}")
# covertendo o número para a base que foi solicitada
if base != 10:
    div = convbase10
    div2 = convbase10
    while div > 0:
        resto = int(div2 % base)
        cont = 10
        for c in range(0, 6):
            if resto == cont:
                resto = str(hexadecimal[c])
            cont += 1
        div = div // base
        div2 = div
        conv = str(resto) + conv
    print(f"O número na base {base} é {conv}")
