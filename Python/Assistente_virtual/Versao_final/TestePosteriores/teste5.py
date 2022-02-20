# import os
# import sys
# import threading
#
#
# class Teste(threading.Thread):
#     def __init__(self, texto):
#         threading.Thread.__init__(self)
#         self._active = threading.Event()
#         self.texto = texto
#         self.cont = 1
#
#     def run(self):
#         for c in range(10):
#             print(self.texto, self.cont)
#             self.cont += 1
#             if c == 8:
#                 # self._active.wait()
#                 sys.exit(0)
#
#
# teste = Teste("Férias")
# teste2 = Teste("Férias2")
#
# print(os.listdir())
# # teste.start()
# # teste2.start()
# #
# # for c in [teste, teste2]:
# #     c.join()
import math

c = 2

for i in range(1, 100):
    print(f"{c} elvado a {i} é: ", math.pow(c, i))
