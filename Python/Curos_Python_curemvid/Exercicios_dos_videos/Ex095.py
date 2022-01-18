dados = dict()
Partidas = list()
dadosRegistrados = list()
escolha = ''

while escolha != 'N':
    dados['nome'] = str(input("Digite o nome do jogador: "))
    dados['quantidade de partidas'] = int(input("Digite a quantidade de partidas que o jogador teve: "))
    golsTotal = 0
    for c in range(0, dados['quantidade de partidas']):
        gols = int(input(f"Digite a quantidade de gols na {(c + 1)}° partida: "))
        Partidas.append(gols)
        golsTotal += gols
    dados['Goslt'] = golsTotal
    dados['Partidas'] = Partidas.copy()
    dadosRegistrados.append(dados.copy())
    Partidas.clear()
    dados.clear()
    escolha = str(input("Deseja continuar:   [S/N]")).upper()

print("-" * 60)
print(f"{'Lista de jogadores e seus respectivos pontos':-^60}")
print("-" * 60)
for c in range(0, len(dadosRegistrados)):
    print(f"Código - {c:.^} \nnome - {dadosRegistrados[c]['nome']} \nGols - {dadosRegistrados[c]['Partidas']}"
          f" \nTotal de Gols - {dadosRegistrados[c]['Goslt']}\n")
num = 0
while True:
    num = str(input("Digite o código do jogador que deseja ver os dados(999 - saí do programa): "))
    if num == '999':
        break
    if num in 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ':
        print("Dado digitado é inválido, digite novamente")
        continue
    cont2 = 0
    for p in range(0, len(dadosRegistrados[int(num)]['Partidas'])):
        print(f"A partida {(cont2 + 1)}, teve {dadosRegistrados[int(num)]['Partidas'][cont2]} gols")
        cont2 += 1
