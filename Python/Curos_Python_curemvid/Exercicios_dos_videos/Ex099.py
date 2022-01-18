def maior(*num):
    print("Analisando os valores passados: ")
    print("Foram informados os valores: ", end=' ')
    cont = 0
    for c in range(0, len(num)):
        print(f"{num[c]}", end=' ')
        if c == 0:
            maiorNUM = num[c]
        else:
            if maiorNUM < num[c]:
                maiorNUM = num[c]
        cont += 1
    print(f"\nForam informados {cont} valores")
    print(f"O maior número é: {maiorNUM}")


maior(1, 2, 3, 5)
maior(1, 5, 9, 6, 8, 6, 5, 3, 2, 5)
maior(9, 9, 6, 5, 3, 4, 8, 1, 2)
maior(0)
