import Minha_Biblioteca
validar = []
validar_digitos = 0
resto = 0
while True:
    cpf = input('Digite seu cpf(com ou sem a pontuação): ')

    if len(cpf) > 14:
        print("Você digitou algo errado, digite novamente!!!")
        continue
    else:
        for c in cpf:
            if not Minha_Biblioteca.Enumero(c):
                continue
            validar.append(c)
        if len(validar) < 11:
            print('Falta algo no cpf digitado, digite novamente!!!')
            validar.clear()
            continue
        break
comparar = validar[0:len(validar) - 2]
for l in range(1, -1, -1):
    validar_digitos = 0
    cont = len(validar) - l
    for c in range(0, len(validar) - (l+1)):
        validar_digitos += (int(validar[c]) * cont)
        cont -= 1
    resto = (validar_digitos * 10) % 11
    if resto == 10:
        resto = 0
    comparar.append(str(resto))
    print(validar_digitos)
if validar == comparar:
    print('O cpf digitado é válido!!!!')
else:
    print('O cpf digitado é inválido!!!')
