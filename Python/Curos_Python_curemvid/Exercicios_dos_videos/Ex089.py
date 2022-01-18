valores = []
aluno = []
escolha = ''
cont = 0
notas = 0
while escolha != 'N':
    aluno.append(input("Nome: "))
    aluno.append(int(input("Nota 1: ")))
    aluno.append(int(input("Nota 2: ")))
    aluno.append(float((aluno[1] + aluno[2])/2))
    valores.append(aluno[:])
    aluno.clear()
    escolha = input("Deseja continuar? [S/N]").upper()

print("-"*50)
print(f"{'Lista de médias dos alunos':-^50}")
print("-"*50)
for c in range(0, len(valores)):
    li = 0
    print(f"{c} - {valores[c][li]:.<40}", end='')
    li += 3
    print(f"{valores[c][li]}")


escolha = ''
while escolha != 'N':
    notas = int(input("Digite qual aluno você deseja verifiar as notas: "))
    for c in range(0, 2):
        print(f'{valores[notas][c+1]}')
    escolha = input("Deseja continuar? [S/N]").upper()
