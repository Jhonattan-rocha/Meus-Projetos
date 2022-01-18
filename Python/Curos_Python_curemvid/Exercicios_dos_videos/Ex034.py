salario = float(input("Digite o salário: "))

if salario > 1250:
    salario = salario*1.10
else:
    salario = salario*1.15

print("O seu novo salário é: {}".format(salario))
