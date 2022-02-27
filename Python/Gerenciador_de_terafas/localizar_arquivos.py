import os
from tkinter import Tk, Label, Entry, Button


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
    def procurar(procura='', tipo='arquivo', unidade='C:', pasta=''):
        if not pasta:
            pasta = str(os.path.join(f"{unidade}:", "\\"))
        caminhos = []
        pastas = []
        subpas = []
        for diretorio, subpastas, arquivos in os.walk(pasta):
            if tipo == "pastas":
                for pasta in diretorio:
                    if procura in pasta:
                        pastas.append(os.path.join(os.path.realpath(diretorio), pasta))
            elif tipo == "subpastas":
                for subpasta in subpastas:
                    if procura in subpasta:
                        subpas.append(os.path.join(os.path.realpath(diretorio), subpasta))
            elif tipo == "arquivo":
                for arquivo in arquivos:
                    if procura in arquivo:
                        caminhos.append(os.path.join(os.path.realpath(diretorio), arquivo))
        return caminhos if tipo == "arquivo" else pastas if tipo == "pastas" else subpas

    @staticmethod
    def tela_aviso(texto):
        janelac = Tk()
        janelac.title(f"Caminhos encontrados")
        textoc = Label(janelac, text=f"{texto:-^100}".upper())
        textoc.place(x=200, y=50, anchor="center")
        janelac.geometry("400x400")
        janelac.resizable(0, 0)
        janelac.mainloop()


local = Localizar_aquivos()
sair = True
while sair:
    procurar = local.chamar_valor("Digite o arquivo ou pasta que você quer procurar")
    retorno = local.procurar(procura=procurar, pasta="C:\\Users\\User\\Desktop\\")
    Localizar_aquivos.tela_aviso(retorno[0])
