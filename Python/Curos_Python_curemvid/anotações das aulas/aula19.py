filmes = {'Titulo': 'star wars', 'Ano': 1977, 'Diretor': 'George locas'}

for k, v in filmes.items():
    print(f"O {k} é {v}")

pessoa = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 23}
print(pessoa)
print(pessoa['Nome'])

print(f'O {pessoa["Nome"]} tem {pessoa["Idade"]} anos')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
for k in pessoa.values():
    print(k)
for k in pessoa.keys():
    print(k)
for k, v in pessoa.items():
    print(f'{k} = {v}')
pessoa['peso'] = 98.5
print(pessoa)

brasil = []
estado = {'UF': 'Rio de janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São paulo', 'Sigla': 'SP'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[1]['Sigla'])

brasil = []
estado = {}

for c in range(0, 3):
    estado['UF'] = str(input("Digite o nome do estado: "))
    estado['Sigla'] = str(input("DIgite a sigla: "))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
