import sys
from os import getlogin
from tkinter import *

import win32com.client as win32


class teste:
    def __init__(self):
        self.var = ""

    def printar(self, texto):
        if texto == "sair":
            sys.exit(0)
        print(texto)

    def chamar_valor(self):
        try:
            self.tela_chat()
        except BaseException:
            self.pegar_valor()
        return self.var

    def pegar_valor(self):
        try:
            self.var = self.entradac.get()
        except BaseException:
            self.var = None
        self.janelac.destroy()

    def tela_chat(self):
        self.janelac = Tk()
        self.janelac.title("Roxxane por chat")
        textoc = Label(self.janelac, text="Digite o nome do arquivo: ")
        textoc.grid(column=0, row=1, padx=25, pady=50)
        self.entradac = Entry(self.janelac)
        self.entradac.grid(column=0, row=2, padx=60, pady=10)
        botaoc = Button(self.janelac, text="OK", command=self.pegar_valor)
        botaoc.grid(column=0, row=3, padx=60, pady=10)
        self.janelac.geometry("270x200")
        self.janelac.resizable(0, 0)
        self.janelac.mainloop()


outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)
email.To = "jhonattan246rocha@gmail.com"
email.Subject = "aNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHN"
conteudo = 'aNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHNaNHASDNASDHN'
nada = 'aline.txt'
anexo = rf"C:\Users\{getlogin()}\Desktop\{nada}"
email.Attachments.Add(anexo)

css = ''' 
    <style>
    .email p {
        font-size: 20px;
        color: gray;
        font-family: Arial, Helvetica, sans-serif;
    }
    </style>
    '''
email.HTMLBody = f'''
    <!DOCTYPE html>
    <html>
    <html lang="pt-BR">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        {css}
        </head>
        <body>
            <section class="email">
                <p>{conteudo}</p>
            </section>
        </body>
    </html>
    '''
email.Send()

