import threading
import time
from random import randint


class ThreadVetor(threading.Thread):
    def __init__(self, valor, vetor):
        threading.Thread.__init__(self)
        self.valor = valor
        self.vetor = vetor

    def run(self) -> None:
        cabaia = ''
        if self.valor % 2 == 0:
            time_inicial = time.perf_counter_ns()
            for h in range(len(self.vetor)):
                pass
            time_final = time.perf_counter_ns()
            print(f"{(time_final - time_inicial) / 1000000000:,.10f}")
        elif self.valor % 2 == 1:
            time_inicial = time.perf_counter_ns()
            for k in self.vetor:
                pass
            time_final = time.perf_counter_ns()
            print(f"{(time_final - time_inicial) / 1000000000:,.10f}")


# Executando
vetor = []
for i in range(0, 999):
    vetor.append(randint(1, 100))

t1 = ThreadVetor(2, vetor)
t2 = ThreadVetor(1, vetor)
t1.start()
t2.start()