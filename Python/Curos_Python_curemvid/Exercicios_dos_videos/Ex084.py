dados = list()
pessoas = list()
cont = 0
leve = 0
pesado = 0
escolha = ''

while escolha != 'N':
    dados.append(str(input("Digite o seu nome: ")))
    dados.append(float(input("Digite seu peso: ")))
    if cont == 0:
        leve = pesado = dados[1]
    else:
        if int(dados[1]) > pesado:
            pesado = dados[1]
        if int(dados[1] < leve):
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    escolha = input("Deseja cotinuar(S/N)?").upper()
print(f"{len(pessoas)} pessoas foram cadastradas: ")
print("as pessoas mais pesadas registraodas são:", end=' ')
for p in pessoas:
    if p[1] == pesado:
        print(f"{p[0]}", end=' ')
print("\nOs mais leves registrados são: ", end=' ')
for p in pessoas:
    if p[1] == leve:
        print(f"{p[0]}", end=' ')
