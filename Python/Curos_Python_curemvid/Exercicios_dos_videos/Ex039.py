anoN = int(input("Digite o ano do seu aniversário: "))
anoA = int(input("Digite o ano atual: "))

idade = anoA - anoN

if idade < 18:
    print("Não está na hora de se alistar, faltam {} anos".format(18-idade))
elif idade == 18:
    print("Tá fodido parceiro, tem que se alistar e logo se não vc se fode")
else:
    print("Se ferrou parceiro, perdeu as datas de inscrição faz {} ano(s)".format(idade - 18))
