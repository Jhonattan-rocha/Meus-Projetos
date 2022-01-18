num = int(input('Digite um número para a quantidade de número que deseja ver: '))

aux = 0
aux2 = 1
cont = 3
print(aux+1, "° termo = ", aux)
print(aux+2, "° termo = ", aux2)
while cont <= num:
    aux3 = aux + aux2
    print(cont, "° termo = ", aux3)
    aux = aux2
    aux2 = aux3
    cont += 1
