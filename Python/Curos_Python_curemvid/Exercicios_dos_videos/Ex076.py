lista = ('Pão', 1, "Nada", 1000, "GTA V", 25000, "PC gamer", "A sua vida", "Computador da positivo", -100)

print("-"*40)
print(f"{'Lista de compras':-^40}")
print("-"*40)
c2 = 1
for c in range(0, len(lista)):
    if c % 2 == 0 and c2 % 2 == 1:
        print(f"{lista[c]:.<30}R$ {lista[c2]}")
    c2 += 1
