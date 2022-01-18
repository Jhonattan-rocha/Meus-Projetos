escola = {'Nome': (str(input("Digite o nome do aluno: ")))}
escola['Média'] = (float(input(f"Digit a média da(a) aluno(a) {escola['Nome']}: ")))
if escola['Média'] >= 7:
    escola['Situação'] = 'Aprovado'
else:
    escola['Situação'] = 'Reprovado'

print(f'O(a) aluno(a) {escola["Nome"]}, teve uma média de {escola["Média"]}, ficando com a situação {escola["Situação"]}')

