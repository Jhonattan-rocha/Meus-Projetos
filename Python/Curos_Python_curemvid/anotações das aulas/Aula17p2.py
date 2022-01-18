gente = list()
dados = list()

for c in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    gente.append(dados[:])
    dados.clear()

for p in gente:

    print(f'{p[0]} tem {p[1]} anos de idade')

