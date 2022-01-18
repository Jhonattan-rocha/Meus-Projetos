from random import randint

print("""As opções são: 
    
        1 - Tesoura
        2 - Pedra
        3 - Papel\n""")

es = int(input("Digite sua escolha: "))

esc = randint(1, 3)

print("JO")
print("KEN")
print("PO")

if esc == 1:
    mostrar = "Tesoura"
elif esc == 2:
    mostrar = "Pedra"
elif esc == 3:
    mostrar = "Papel"
else:
    mostrar = "{}".format(esc)

print("Computador jogou {}\n".format(mostrar))

if es == esc:
    print("Empate")
elif es == 1 and esc == 2 or es == 2 and esc == 3 or es == 3 and esc == 1:
    print("Você perdeu, o computador ganhou!!!!!!!!!!")
elif es == 1 and esc == 3 or es == 2 and esc == 1 or es == 3 and esc == 2:
    print("Parabens, você ganhou!!!!!!!!!!!!")
else:
    print("Número digitado é inválido")
