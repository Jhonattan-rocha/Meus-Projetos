# from pybrain.tools.shortcuts import buildNetwork
# import pickle
# from pybrain.tools.customxml.networkwriter import NetworkWriter
# from pybrain.tools.customxml.networkreader import NetworkReader
#
# net = buildNetwork(2, 4, 1)
# fileObject = open('filename.pkl', 'a')
# pickle.dump(net, fileObject)
# fileObject.close()
# # fileObject = open('filename.pkl', 'w')
# # net = pickle.load(fileObject)
# # net = buildNetwork(2, 4, 1)
# # NetworkWriter.writeToFile(net, 'filename.pkl')
# # net = NetworkReader.readFrom('filename.pkl')

import subprocess

informacoes = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='cp860')
print(informacoes)
nome = 'jhonattan'
informacoes = subprocess.check_output(["netsh", "wlan", "show", "profile", nome, "key", "=", "clear"], encoding='cp858')
for c in informacoes.split("\n"):
    if "Conteúdo da chave" in c:
        pos = c.find(":")
        senha = c[pos+2:]
        print(senha)

