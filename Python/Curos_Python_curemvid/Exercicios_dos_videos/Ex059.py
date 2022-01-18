
escolha = 0
while escolha != 5:
    num1 = int(input("\nDigite um número: "))
    num2 = int(input("\nDigite outro número: "))
    result = 0
    escolha = int(input("""Escolha uma das opções e digite: 
                        [1] - soma
                        [2] - subtrair
                        [3] - multiplicar
                        [4] - dividir
                        
                        Digite sua escolha: """))
    if escolha == 1:
        result = num1 + num2
    elif escolha == 2:
        result = num1 - num2
    elif escolha == 3:
        result = num1 * num2
    elif escolha == 4:
        result = num1 / num2
    print("O resultado da conta é: {}".format(result))
    escolha = int(input("Deseja sair do programa[5 para sair]: "))
