import math
am = int(input("Digite o ângulo: "))

s = math.sin(math.radians(am))
c = math.cos(math.radians(am))
t = math.tan(math.radians(am))

print("O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(am, s, c, t))
