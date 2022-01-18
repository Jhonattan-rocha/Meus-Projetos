def notas(*nums, situacao=False):
    notasA = []
    cont = 0
    maior = 0
    menor = 0
    media = 0
    for c in range(0, len(nums)):
        cont += 1
        notasA.append(nums[c])
        media += nums[c]
        if c == 0:
            maior = nums[c]
            menor = nums[c]
        else:
            if maior < nums[c]:
                maior = nums[c]
            if menor > nums[c]:
                menor = nums[c]
    dados = dict()
    dados['Quantidade de Alunos'] = cont
    dados['Notas'] = notasA.copy()
    dados['Maior nota'] = maior
    dados['Menor nota'] = menor
    dados['Média'] = media/cont
    if situacao:
        if media/cont >= 7:
            dados["Situação"] = 'Boa'
        else:
            dados["Situação"] = 'Ruim'
    print(dados)


print("!!!Sistema de notas!!!")
print("As notas dos alunos da sala é: ")
notas(10, 20, 50, 90, 60, 7, 6, 8)
