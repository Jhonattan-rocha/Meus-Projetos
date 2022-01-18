palavras = ('Programar', 'Aprender', 'andar', 'Colo', 'Pe', 'Fe', 'Carlos', 'Ferro', 'Comido')
compara = ''
for c in range(0, 9):
    compara = str(palavras[c]).lower()
    print(f"\nA palavra {str(compara)} tem tais vogáis: ", end="")
    for c2 in range(0, len(str(compara))):
        if compara[c2] == 'a':
            print(" a ", end="")
        elif compara[c2] == 'e':
            print(" e ", end="")
        elif compara[c2] == 'i':
            print(" i ", end="")
        elif compara[c2] == 'o':
            print(" o ", end="")
        elif compara[c2] == 'u':
            print(" u ", end="")

