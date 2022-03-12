import subprocess
from os import walk
from sys import exit as ex
from os.path import join, realpath
from tkinter import Tk, Label, Entry, Button, Text, INSERT
from pyautogui import alert


class Localizar_aquivos:
    def __init__(self):
        self.entradac = None
        self.janelac = None
        self.var = None

    def chamar_valor(self, text=''):
        try:
            self.__tela_valor_digitado(texto=text)
        except BaseException:
            self.__pegar_valor()
        return self.var

    def __pegar_valor(self):
        try:
            self.var = self.entradac.get()
        except BaseException:
            self.var = None
        self.janelac.destroy()

    def __tela_valor_digitado(self, texto):
        self.janelac = Tk()
        self.janelac.title(f"Localizar aquivos")
        textoc = Label(self.janelac, text=texto)
        textoc.grid(column=0, row=1, padx=25, pady=50)
        self.entradac = Entry(self.janelac)
        self.entradac.grid(column=0, row=2, padx=60, pady=10)
        botaoc = Button(self.janelac, text="OK", command=self.__pegar_valor)
        botaoc.grid(column=0, row=3, padx=60, pady=10)
        self.janelac.geometry("310x200")
        self.janelac.resizable(0, 0)
        self.janelac.mainloop()

    @staticmethod
    def procurar(procura=''.lower(), unidade='C:'.lower(), pasta=''.lower()):
        if not pasta:
            pasta = str(join(f"{unidade}:", "\\"))
        caminhos = []
        for diretorio, subpastas, arquivos in walk(pasta):
            for arquivo in arquivos:
                if procura.lower() in arquivo.lower():
                    caminhos.append(join(realpath(diretorio), arquivo))
        return caminhos

    @staticmethod
    def tela_aviso(texto):
        janelac = Tk()
        janelac.title(f"Caminhos encontrados")
        textoc = Text(janelac)
        textoc.insert(INSERT, texto)
        textoc.place(x=200, y=50, anchor="center")
        textoc.grid(column=1)
        janelac.resizable(0, 0)
        janelac.geometry("655x400")
        janelac.mainloop()


local = Localizar_aquivos()
sair = True
while sair:
    procurar = local.chamar_valor("Digite o arquivo que você quer procurar: ")
    if str(procurar).strip() == "exit":
        ex(0)
    if str(procurar).strip() == "":
        alert(text="Digite algo", title="Error")
        continue
    pasta = local.chamar_valor("Digite a pasta onde deseja procurar: ")
    retorno = local.procurar(procura=procurar, pasta=pasta)
    if len(retorno) == 0:
        alert(text="Não foi encontrado o arquivo digitado", title="Error")
        continue
    else:
        texto = ''
        for i in [i for i in retorno]:
            texto += i + "\n\n"
        local.tela_aviso(texto)
        try:
            for i in retorno:
                subprocess.run(f"{i}")
        except:
            local.tela_aviso("Algum caminho encontrado não foi executado corretamente")
