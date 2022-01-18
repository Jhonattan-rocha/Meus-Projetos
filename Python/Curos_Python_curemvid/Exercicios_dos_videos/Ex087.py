valores = [[], [], []]
somapar = 0
somaTer = 0
maiorSegu = 0
for b in range(0, 3):
    for c in range(0, 3):
        num = int(input(f"Digite um número para a posição [{b}, {c}]  da matriz: "))
        valores[b].append(num)
        if num % 2 == 0:
            somapar += num
        if c == 2:
            somaTer += num
        if c == 1 and b == 0:
            maiorSegu = num
        else:
            if maiorSegu < num and c == 1:
                maiorSegu = num
print("\nA matriz ficará assim: ")
for b in range(0, 3):
    print()
    for c in range(0, 3):
        print(f" [{valores[b][c]}] ", end=' ')

print(f"\nA soma dos números pares é: {somapar}")
print(f"A soma dos números da terceira coluna é: {somaTer}")
print(f"O maior valor da segunda coluna é: {maiorSegu}")
