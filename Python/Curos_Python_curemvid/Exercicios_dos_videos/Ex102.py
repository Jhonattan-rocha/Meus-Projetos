def fatorial(num=1, show=0):
    """
    Resumo do programa: cálculo do fatorial do número n
    :param num: - parâmetro que vai receber o valor de n
    :param show: - parâmetro de valor, sendo s ou n, que vai definir se irá ser mostrado ou não a conta
    :return: - retorna o print com o valor do fatorial de n, ou retorna a conta junto com o valor de n
    """
    if show == 0:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        f = 1
        for c in range(num, 0, -1):
            print(f"{c} x {f} = ", end=' ')
            f *= c
            print(f)
            if c == 1:
                print(f"O fatorial de {num} é {f}")
        return f


print("Programa para cálculo de fatorial!!!")
n = int(input("Digite um número para saber seu fatorial: "))
escolha = ''
while escolha != 'S' and escolha != 'N':
    escolha = str(input("Deseja saber o cálculo do fatorial: ")).upper()
    if escolha == 'S':
        escolha = int(1)
        break
    else:
        escolha = int(0)
        break
if escolha == 0:
    print(f"O faotial do número é:{fatorial(n, escolha)}")
else:
    print("O cálculo é: ")
    fatorial(n, escolha)
