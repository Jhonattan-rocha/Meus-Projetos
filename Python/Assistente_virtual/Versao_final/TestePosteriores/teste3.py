import pickle
import numpy as np
from pybrain.structure import TanhLayer, SoftmaxLayer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers.backprop import BackpropTrainer
from pybrain.datasets.supervised import SupervisedDataSet
import Minha_Biblioteca

# import pybrain  # biblioteca para redes neuráis
# nltk.download('averaged_perceptron_tagger')
#
# x = [["me fala as horas"], ["que horas são"]]
#
# frases = nltk.tokenize.word_tokenize("me fala as horas")
# words = nltk.pos_tag(x[1])
# print(frases)
# print(words)
#
# entidades = nltk.ne_chunk(words)
# print(entidades)


arquivoC = open(r'../databaseC.txt', 'r', encoding='utf-8')
arquivoC = arquivoC.read()
arquivoC = arquivoC.split()

codigos = [[int(i)] for i in arquivoC if i.isnumeric()]
frases = [str(i).replace("_", " ") for i in arquivoC if not i.isnumeric()]


class BagOfWords:
    def __init__(self):
        self.vocabulario = []

    def construir_vocabulario(self, sentences):
        for sentence in sentences:
            for palavra in sentence.split(" "):
                if palavra not in self.vocabulario:
                    self.vocabulario.append(palavra)

    def criar_array(self, sentences):
        palavras = sentences.split(' ')
        vetor = np.zeros(len(self.vocabulario))
        for palavra in palavras:
            for i, _palavra in enumerate(self.vocabulario):
                if _palavra == palavra:
                    vetor[i] = 1
        return list(vetor)

    def criar_dataset(self):
        self.construir_vocabulario(frases)
        entradas = []
        for sentence in frases:
            vetor = bag.criar_array(sentence)
            passe = []
            for num in vetor:
                passe.append(num)
            entradas.append(passe)
        self.ds = SupervisedDataSet(bag.get_len(), 1)
        for i, j in zip(entradas, codigos):
            self.ds.addSample(i, j)

    def treinar_rede(self):
        self.netWork = buildNetwork(bag.get_len(), 5, 1, bias=True, hiddenclass=TanhLayer)
        back = BackpropTrainer(self.netWork, self.ds)
        for i in range(2000):
            back.train()
        with open('../rede_neural.xml', 'wb') as f:
            pickle.dump(self.netWork, f, 0)

    def retornar_valor_previsto(self, texto):
        num = f"{float(self.netWork.activate(bag.criar_array(texto))):,.0f}"
        return float(num)

    def get_len(self):
        return len(self.vocabulario)


# sentences = ['eu gosto disso', 'eu odeio isso', 'aquilo era bom', 'aquilo era mal']
# sentences = ["me fala as horas", "que horas são", "me diga as horas", "fale as horas", "horas, por favor",
#              "me fala a data", "que dia é hoje", "me diga a data", "fale a data", "tempo",
#              "me diga o clima", "qual é o clima de hoje", "qual a previsão do clima para hoje",
#              "qual o clima para hoje",
#              "clima"]

bag = BagOfWords()
bag.criar_dataset()
bag.treinar_rede()
print(bag.vocabulario)
# with open('rede_neural.xml', 'rb') as f:
#     bag.netWork = pickle.load(f)

print(bag.retornar_valor_previsto("me diga a data"))
