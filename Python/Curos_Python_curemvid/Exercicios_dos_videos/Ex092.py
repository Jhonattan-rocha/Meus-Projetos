from datetime import datetime  # bibliotec que busca a data do computado

registro = dict()

registro['nome'] = input('Digite o seu nome: ')
registro['ano de nascimento'] = int(input("Digite seu ano de nascimento: "))
registro['carteira de trabalho'] = int(input("Digite o numero da sua carteira de trabalho"
                                             "(0 - para primeiro emprego): "))
registro['idade'] = int(datetime.now().year - int(registro['ano de nascimento']))
if registro['carteira de trabalho'] != 0:
    registro['salario'] = float(input("Digite seu salário: "))
    registro['ano de contratação'] = int(input("Digite o ano em que foi contratado: "))
    registro['aposentadoria'] = int(registro['idade'] + ((registro['ano de contratação'] + 35) - datetime.now().year))

for k, v in registro.items():
    print(f'O campo {k} tem como valor {v}')
