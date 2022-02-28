from os import walk
from sys import exit as ex
from os.path import join, realpath
from pyautogui import alert, prompt


class Localizar_aquivos:
    def __init__(self):
        pass

    @staticmethod
    def procurar(procura='', unidade='C:', pasta=''.lower()):
        if not pasta:
            pasta = str(join(f"{unidade}:", "\\")).lower()
        caminhos = []
        for diretorio, subpastas, arquivos in walk(pasta):
            for arquivo in arquivos:
                if procura.lower() in arquivo.lower():
                    caminhos.append(join(realpath(diretorio), arquivo))
        return caminhos


local = Localizar_aquivos()
sair = True
while sair:
    procurar = prompt(text="Digite o arquivo que você quer procurar: ", title="Arquivo")
    if str(procurar).strip() == "exit":
        ex(0)
    if str(procurar).strip() == "":
        alert(text="Digite algo", title="Error")
        continue
    pasta = prompt(text="Digite a pasta onde deseja procurar: ", title="Pasta")
    retorno = local.procurar(procura=procurar, pasta=pasta)
    if len(retorno) == 0:
        alert(text="Não foi encontrado o arquivo digitado", title="Error")
        continue
    else:
        texto = ''
        for i in [i for i in retorno]:
            texto += i + "\n\n"
        alert(text=texto, title="Resultado: ")
