escolha = ''
valores = list()
cont = 0
posicoes = []
while escolha != 'N':
    valores.append(int(input("Digite um número: ")))

    escolha = input("Deseja continuar(S/N): ").upper()

    if valores[cont] == 5:
        posicoes.append(cont)
    cont += 1
if len(posicoes) == 0:
    print(f"O número 5 faz parte da lista e aparece primeiramente na posição {(valores.index(5)+1)}")
elif len(posicoes) > 0:
    print("O número 5 faz parte da lista e aparece nas posição ", end=' ')
    for c in range(0, len(posicoes)):
        print(f"{posicoes[c]:.<4}", end=' ')
else:
    print("O número 5 não faz parte da lista, logo, ele não foi digitado")
print(f"\nA quantidade de números digitado é {cont}")
valores.sort(reverse=True)
print(f"A lista em ordem decrescente é {valores}")
