import os
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import Minha_Biblioteca
import numpy
"""
import sklearn
from sklearn.model_selection import train_test_split

modelo = sklearn.svm.LinearSVC()  # modelo básico para machining learning
modelo.fit(x, y)  # comando para mandar o modelo treinar
# x é os dados, y é as respostas providas baseadas nesses dados
# print(sklearn.metrics.accuracy_score(teste_x, previcoes))
# sample() no pandas traz linhas aleatórias

modelo = sklearn.svm.LinearSVC()  # modelo básico para machining learning
# isso aqui separa os dados em teste e treino para que não vicio o algoritmo
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y)
modelo.fit(treino_x, treino_y)
modelo.predict(teste_x)  # comando para prever usando a variável teste_x do train_test_split
# print(sklearn.metrics.accuracy_score(teste_y, previcoes))
from pybrain.tools.shortcuts import buildNetwork 
"""

# arquivo = open(r"databaseF.txt", 'r', encoding='utf-8')
# arquivo = arquivo.read()
# arquivo = arquivo.split()


def ajeitar(texto=''):
    texto = texto.split()
    retorno = ' '
    for c in texto:
        retorno += c
    return numpy.float64(retorno)


teste1 = [ajeitar(Minha_Biblioteca.LetraNumero("me fala as horas"))]
teste2 = [ajeitar(Minha_Biblioteca.LetraNumero("que horas são"))]
teste3 = [ajeitar(Minha_Biblioteca.LetraNumero("me diga as horas"))]
teste4 = [ajeitar(Minha_Biblioteca.LetraNumero("fale as horas"))]
teste5 = [ajeitar(Minha_Biblioteca.LetraNumero("horas, por favor"))]
teste6 = [ajeitar(Minha_Biblioteca.LetraNumero("me fala a data"))]
teste7 = [ajeitar(Minha_Biblioteca.LetraNumero("que dia é hoje"))]
teste8 = [ajeitar(Minha_Biblioteca.LetraNumero("me diga a data"))]
teste9 = [ajeitar(Minha_Biblioteca.LetraNumero("fale a data"))]
teste10 = [ajeitar(Minha_Biblioteca.LetraNumero("tempo"))]
teste11 = [ajeitar(Minha_Biblioteca.LetraNumero("me diga o clima"))]
teste12 = [ajeitar(Minha_Biblioteca.LetraNumero("qual é o clima de hoje"))]
teste13 = [ajeitar(Minha_Biblioteca.LetraNumero("qual a previsão do clima para hoje"))]
teste14 = [ajeitar(Minha_Biblioteca.LetraNumero("qual o clima para hoje"))]
teste15 = [ajeitar(Minha_Biblioteca.LetraNumero("clima"))]

x = [teste1, teste2, teste3, teste4, teste5, teste6, teste7, teste8, teste9, teste10, teste11, teste12, teste13,
     teste14, teste15]
# x = [["me fala as horas"], ["que horas são"], ["me diga as horas"], ["fale as horas"], ["horas, por favor"],
#      ["me fala a data"], ["que dia é hoje"], ["me diga a data"], ["fale a data"], ["tempo"],
#      ["me diga o clima"], ["qual é o clima de hoje"], ["qual a previsão do clima para hoje"], ["qual o clima para hoje"], ["clima"]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

modelo = SVC(max_iter=1000000, random_state=10, kernel="linear")
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size=0.5, train_size=0.5)
modelo.fit(treino_x, treino_y)
print(modelo.predict([[ajeitar(Minha_Biblioteca.LetraNumero("qual o clima"))]]))
