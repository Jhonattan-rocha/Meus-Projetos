m = float(input("Digite um valor em metros: "))

km = float(m/1000)
hm = float(m/100)
dam = float(m/10)
dm = float(m*10)
c = float(m*100)
mm = float(m*1000)

print("O valr em centimetros é {}, o valor em milimetros é {} ".format(c, mm))
print("O valor em dm é {}, O valor em dam é {}, o valor em hm é {}, o valor em km é {}".format(dm, dam, hm, km))
