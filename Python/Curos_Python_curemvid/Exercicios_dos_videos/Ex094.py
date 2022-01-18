dados = dict()
registros = list()
escolha = ''
mediaidade = 0
while escolha != 'N':
    dados['nome'] = str(input("Digite seu nome: "))
    dados['sexo'] = str(input("Digite seu sexo [S/N]: ")).upper()
    dados['idade'] = int(input("Digite sua idade: \n"))
    mediaidade += dados['idade']
    registros.append(dados.copy())
    dados.clear()
    escolha = input("Deseja continuar:     [S/N]").upper()
print(f"Foram registradas {len(registros)} pessoas")
print(f'\nA média de idade é: {(mediaidade/len(registros)):.2f}\n')
cont = 1
print("As pessoas com idade acima da média é: \n")
for c in range(0, len(registros)):
    if registros[c]['idade'] > (mediaidade/len(registros)):
        print(f'{cont}° pessoa é: {registros[c]["nome"]}')
        cont += 1
print("\nAs mulheres registradas são: ")
for c in range(0, len(registros)):
    if registros[c]['sexo'] == 'F':
        print(f'{cont}° mulher é: {registros[c]["nome"]}')
        cont += 1
