NumEscritos0a11 = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

num = int(input("Digite um número entre 0 e 20: "))
while num > 20 or num < -1:
    num = int(input("Digite novamente um número entre 0 e 20: "))

num = NumEscritos0a11[num]
print(f"O número digitado é: {num}")
