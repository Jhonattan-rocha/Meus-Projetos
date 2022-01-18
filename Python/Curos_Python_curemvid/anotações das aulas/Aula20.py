def mostralinha(nome):
    print("-" * 30)
    print(nome)
    print('-' * 30)


def soma(a2, b2):
    s = a2 + b2
    print(f'A soma de A = {a2} + B = {b2}, é {s}')


def contador(*num):
    for c in range(0, len(num)):
        print(f"O número {num[c]} é o {(c + 1)}° número")


# nome2 = 'Jhonattan'
# for c in range(0, 101):
#     mostralinha(nome2)

# a = 3
# b = 4
# s = a + b
# print(s)
# a = 4
# b = 5
# s = a + b
# print(s)
# a = 8
# b = 9
# s = a + b

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

soma(a2=b, b2=a)
contador(1, 2, 3, 4, 5, 8, 9, 10, 75, 15)

help(print())
