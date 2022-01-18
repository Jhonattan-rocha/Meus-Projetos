valores = [[], [], []]

for b in range(0, 3):
    for c in range(0, 3):
        num = int(input(f"Digite um número para a posição [{b}, {c}]  da matriz: "))
        valores[b].append(num)
print("\nA matriz ficará assim: ")
for b in range(0, 3):
    print()
    for c in range(0, 3):
        print(f" [{valores[b][c]}] ", end=' ')
