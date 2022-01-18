v = float(input("Digite o valor da casa: "))
s = float(input("Digite o valor do seu salário: "))
a = float(input("Digite em quantos anos você planeja pagar o empréstimo: "))

am = float(a*12)
mensalidade = v / am

if mensalidade > (s*0.3):
    print("O empréstimo foi negado pois passou a taxa limite de 30%")
    print("A mensalidade ficou em R${:.2f}, impossibilitando o pagamento.".format(mensalidade))
else:
    print("O empréstimo foi aprovado, senda as mensalidades da casa R${:.2f}".format(mensalidade))
