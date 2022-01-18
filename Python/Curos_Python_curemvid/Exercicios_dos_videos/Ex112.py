from Curos_Python_curemvid.Uteis.Cursoemvídeo.resumo import resumoprecos
from Curos_Python_curemvid.Uteis.Cursoemvídeo.Exer111M import leiadinheiro
from Curos_Python_curemvid.Uteis.Cursoemvídeo.Exer111M import checapor
numero = leiadinheiro('Digite um número: ')
pora = checapor("Digite o número da porcentagem que deseja aumentar o número: ")
pord = checapor("Digite o número da porcentagem que deseja diminuir o número: ")
resumoprecos(preco=numero, PorA=pora, Pord=pord)
