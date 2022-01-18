from Curos_Python_curemvid.Uteis.Cursoemvídeo.resumo import resumoprecos

numero = int(input("Digite quanto dinheiro você tem: R$"))
pora = float(input("Digite o número da porcentagem que deseja aumentar o número: "))
pord = float(input("Digite o número da porcentagem que deseja diminuir o número: "))
resumoprecos(preco=numero, PorA=pora, Pord=pord)
