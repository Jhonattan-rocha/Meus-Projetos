import pickle

import numpy as np
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers.backprop import BackpropTrainer
from pybrain.datasets.supervised import SupervisedDataSet


class BagOfWords:
    def __init__(self):
        self.vocab = []

    def build_vocab(self, sentences):
        for sentence in sentences:
            for word in sentence.split(" "):
                if word not in self.vocab:
                    self.vocab.append(word)
        self.vocab.sort()

    def toArray(self, sentences):
        words = sentences.split(' ')
        vector = np.zeros(len(self.vocab))

        for word in words:
            for i, _word in enumerate(self.vocab):
                if _word == word:
                    vector[i] = 1
        return list(vector)

    def get_len(self):
        return len(self.vocab)


sentences = ['eu gosto disso', 'eu odeio isso', 'aquilo era bom', 'aquilo era mal']

bag = BagOfWords()
bag.build_vocab(sentences)

outputs = [[1], [0], [1], [0]]
inputs = []
# print(bag.vocab)
for sentence in sentences:
    vector = bag.toArray(sentence)

    passe = []
    for num in vector:
        passe.append(num)
    inputs.append(passe)

# esse dataset começa com o tamanho, depois o número de saídas
ds = SupervisedDataSet(bag.get_len(), 1)
for i, j in zip(inputs, outputs):
    ds.addSample(i, j)
# neuronios de entrada, depois a quantidade de neurônios da cama intermediária, camada de saida
netWork = buildNetwork(bag.get_len(), 5, 1, bias=True)
back = BackpropTrainer(netWork, ds)  # rede, database
# esse for treina a rede neural
for i in range(1000):
    back.train()

print(netWork.activate(bag.toArray("que horas que é"))[0])  # comando para ativar a rede neural
