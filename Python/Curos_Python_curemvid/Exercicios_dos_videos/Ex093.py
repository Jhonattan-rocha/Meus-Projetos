dados = dict()

dados['nome'] = str(input("Digite o nome do jogador: "))
dados['quantidade de partidas'] = int(input("Digite a quantidade de partidas que o jogador teve: "))
golsTotal = 0
for c in range(0, dados['quantidade de partidas']):
    gols = int(input(f"Digite a quantidade de gols na {(c+1)}° partida: "))
    dados[f'Partida {c}'] = gols
    golsTotal += gols
dados['gols total'] = golsTotal
print(f"O jogador {dados['nome']} teve {dados['quantidade de partidas']} partidas, logo a baixo a tabela de gols:")
print(f"O total de gols feitos no campeonato foi {dados['gols total']}, sendo dividos nas segunites partidas: ")
for c in range(0, dados['quantidade de partidas']):
    print(f"A partida {(c+1)}, o jogador teveve {dados[f'Partida {c}']} gol")

