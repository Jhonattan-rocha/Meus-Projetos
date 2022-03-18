import threading
from random import random, randint
from time import sleep

colocados = []


class Sapo(threading.Thread):
    def __init__(self, dist=20, ids=randint(1, 10)):
        threading.Thread.__init__(self)
        self.idente = ids
        self.dist = dist
        self.pulo = randint(1, 5)

    def run(self) -> None:
        distancia = 0
        for i in range(self.dist):
            print(f"{self.idente}° sapo")
            distancia += self.pulo
            if distancia >= self.dist:
                colocados.append(self.idente)
                return
            print(f"Pulou {self.pulo} metro, percorreu até o momento {distancia} metros")


for i in range(5):
    sapo1 = Sapo(10, i+1)
    sapo1.start()

sleep(0.5)
for i in range(len(colocados)):
    print(f"O {i+1}° colocado foi o {colocados[i]}")
