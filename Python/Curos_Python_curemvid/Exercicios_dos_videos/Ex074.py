from random import randint

escolha = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = 0
menor = 0
for c in range(0, 5):
    if c == 0:
        maior = escolha[c]
        menor = escolha[c]
    else:
        if maior < escolha[c]:
            maior = escolha[c]
        elif menor > escolha[c]:
            menor = escolha[c]
for c in range(0, 5):
    print("O ", (c+1), f"° elemento é: {escolha[c]}")
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")