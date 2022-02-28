import os
import tkinter
from tkinter import Tk, Label, Entry, Button, Text
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
    def procurar(procura='', unidade='C:', pasta=''):
        if not pasta:
            pasta = str(os.path.join(f"{unidade}:", "\\"))
        caminhos = []
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                if procura in arquivo:
                    caminhos.append(os.path.join(os.path.realpath(diretorio), arquivo))
        return caminhos

    @staticmethod
    def tela_aviso(texto):
        janelac = Tk()
        janelac.title(f"Caminhos encontrados")
        textoc = Text(janelac)
        textoc.insert(tkinter.INSERT, texto)
        textoc.place(x=200, y=50, anchor="center")
        textoc.grid(column=1)
        janelac.resizable(0, 0)
        janelac.geometry("655x400")
        janelac.mainloop()


local = Localizar_aquivos()
sair = True
while sair:
    procurar = local.chamar_valor("Digite o arquivo que você quer procurar: ")
    if procurar == "exit":
        exit(0)
    if str(procurar).strip() == "":
        alert(text="Digite algo", title="Error")
        continue
    pasta = local.chamar_valor("Digite a pasta onde deseja procurar: ")
    if str(pasta).strip() == "":
        alert(text="Digite algo", title="Error")
        continue
    retorno = local.procurar(procura=procurar, pasta=pasta)
    if len(retorno) == 0:
        alert(text="Não foi encontrado o arquivo digitado", title="Error")
        continue
    else:
        texto = ''
        for i in [i for i in retorno]:
            texto += i + "\n\n"
        local.tela_aviso(texto)
