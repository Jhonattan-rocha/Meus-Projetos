import threading
from random import randint

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


print(f"Soma da {soma[1]}° linha: {soma[0]}")
print(f"Soma da {soma[3]}° linha: {soma[2]}")
print(f"Soma da {soma[5]}° linha: {soma[4]}")
