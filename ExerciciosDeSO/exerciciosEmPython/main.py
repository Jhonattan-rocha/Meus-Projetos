import threading
from random import randint
import time


# Exer1


class ExerUm(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        print(self.native_id, self.name, self.ident)


# executando
# for i in range(5):
#     Thread = ExerUm()
#     Thread.start()

# ----------------------------------------------------------

soma = []


# Exer2
class Calculo_matriz(threading.Thread):
    def __init__(self, matriz, linha):
        threading.Thread.__init__(self)
        self.linha = linha
        self.matriz = matriz

    def run(self) -> None:
        self.calcula_soma_linhas(self.matriz, self.linha)

    @staticmethod
    def calcula_soma_linhas(matriz, linha):
        somar = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i == linha:
                    somar += matriz[i][j]
        soma.append(somar)
        soma.append(linha + 1)


# Executando
matriz = [[],
          [],
          []]
for i in range(3):
    for j in range(5):
        matriz[i].append(randint(1, 100))

# pprint(matriz)
for i in range(1, 4):
    calculo = Calculo_matriz(matriz=matriz, linha=i - 1)
    calculo.start()


# print(f"Soma da {soma[1]}° linha: {soma[0]}")
# print(f"Soma da {soma[3]}° linha: {soma[2]}")
# print(f"Soma da {soma[5]}° linha: {soma[4]}")


# --------------------------------------------------------------

# Exer3

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
            print(f"{(time_final - time_inicial)/1000000000:,.10f}")
        elif self.valor % 2 == 1:
            time_inicial = time.perf_counter_ns()
            for k in self.vetor:
                pass
            time_final = time.perf_counter_ns()
            print(f"{(time_final - time_inicial)/1000000000:,.10f}")


# Executando
vetor = []
for i in range(0, 999):
    vetor.append(randint(1, 100))

t1 = ThreadVetor(2, vetor)
t2 = ThreadVetor(1, vetor)
t1.start()
t2.start()
