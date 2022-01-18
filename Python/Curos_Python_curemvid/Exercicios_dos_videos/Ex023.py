n = int(input("Digite um número entre 0 e 99999: "))
m = int(n/1000)
c = int((n-(1000*m))/100)
d = int((n-(1000*m)-(100*c))/10)
u = int((n-(1000*m)-(100*c)-(10*d)))

print("Milhar: {} \ncentena: {} \ndesena: {} \nunidade: {}".format(m, c, d, u))


