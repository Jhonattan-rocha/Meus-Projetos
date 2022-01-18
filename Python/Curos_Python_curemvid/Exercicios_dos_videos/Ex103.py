def ficha(nome, gol=0):
    print(f"O jogador {nome} fez {gol} gol(s) no campeonato")


nomej = str(input("Digite o nome do jogador: "))
if nomej == '':
    nomej = "<desconhecido>"
gols = str(input("Digite os gols do jogador: "))
if gols == '':
    gols = 0
ficha(nome=nomej, gol=gols)
