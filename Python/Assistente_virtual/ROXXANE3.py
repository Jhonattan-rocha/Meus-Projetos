from json import loads
from math import pow
from os import getlogin, listdir
from os.path import exists
from pickle import load, dump
from random import randint
from sys import exit
import threading
import webbrowser
from subprocess import check_output
from datetime import datetime, date
# from time import sleep
from tkinter import Tk, Button, PhotoImage, Label, Entry, Toplevel
# from tkinter import messagebox
import pandas as pd
from psutil import cpu_percent, virtual_memory
from pyaudio import PyAudio, paInt16
import pyautogui
from pyperclip import copy
from pyttsx3 import init
import qrcode
from requests import exceptions, get
import speech_recognition as sr
from wikipedia import set_lang, summary
from plyer import notification
# from tqdm import tqdm
from vosk import Model, KaldiRecognizer
from multiprocessing.pool import ThreadPool
import numpy as np
from pybrain import TanhLayer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers.backprop import BackpropTrainer
from pybrain.datasets.supervised import SupervisedDataSet
import win32com.client as win32
import re

engine = init()
model = Model("../model")
rec = KaldiRecognizer(model, 16000)
p = PyAudio()
stream = p.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
despedidas = ['tchal', 'adeus', 'te vejo mais tarde', 'até', 'até logo']
pacoteOffice = ['word', 'excel', 'powerpoint', 'access', 'teams']
opcoes = ['word', 'excel', 'powerpoint', 'access', 'teams', 'genshin impact', 'chrome', 'microsoft edge']


class ROXXANE(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)  # thread da Roxxane
        self.voz_data = ''
        self.aux = ''
        # falas
        self.arquivoR = open(r"../databaseR.txt", 'r', encoding='utf-8')
        self.arquivoR = self.arquivoR.read()
        self.arquivoR = self.arquivoR.split()
        self.pessoa = self.arquivoR[1]
        self.nome_assistente = self.arquivoR[3]
        self.arquivoF = open(r"../databaseF.txt", 'r', encoding='utf-8')
        self.arquivoF = self.arquivoF.read()
        self.arquivoF = self.arquivoF.split()
        self.pool = ThreadPool(processes=1)
        # netWork
        self.arquivoC = open(r'../databaseC.txt', 'r', encoding='utf-8')
        self.arquivoC = self.arquivoC.read()
        self.arquivoC = self.arquivoC.split()
        self.codigos = [[int(i)] for i in self.arquivoC if i.isnumeric()]
        self.frases = [str(i).replace("_", " ") for i in self.arquivoC if not i.isnumeric()]
        self.vocabulario = []
        self.var = ""
        self.is_run = True

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
        self.construir_vocabulario(self.frases)
        entradas = []
        for sentence in self.frases:
            vetor = self.criar_array(sentence)
            passe = []
            for num in vetor:
                passe.append(num)
            entradas.append(passe)
        self.ds = SupervisedDataSet(self.get_len(), 1)
        for i, j in zip(entradas, self.codigos):
            self.ds.addSample(i, j)

    def treinar_rede(self):
        self.netWork = buildNetwork(self.get_len(), 5, 5, 1, bias=True, hiddenclass=TanhLayer)
        back = BackpropTrainer(self.netWork, self.ds)
        for i in range(2000):
            back.train()
        with open('../rede_neural.xml', 'wb') as fa:
            dump(self.netWork, fa, 0)

    def retornar_valor_previsto(self, texto):
        num = f"{float(self.netWork.activate(self.criar_array(texto))):,.0f}"
        return float(num)

    def get_len(self):
        return len(self.vocabulario)

    # daqui para cima é da redeneural

    def existe(self, termos):
        for termo in termos:
            if termo in self.voz_data:
                return True

    @staticmethod
    def pegar_comandos_separados():
        while True:
            rec.pause_threshold = 1
            data = stream.read(10000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                resultado = rec.FinalResult()
                resultado = loads(resultado)
                if resultado is not None:
                    return resultado['text'].lower()

    def conversas(self):
        if self.existe(['hey', 'hi', 'hello', 'oi', 'holla']):
            saudacoes = [f'Oi {self.pessoa}, o que você está fazendo hoje?',
                         f'Oi {self.pessoa}, como eu posso te ajudar?',
                         f'Oi {self.pessoa}, você precisa de algo?',
                         f'Oi {self.pessoa}, como vai você?']
            resposta = saudacoes[randint(0, len(saudacoes) - 1)]
            self.engine_fala(resposta)
            self.voz_data = ' '
            return
        elif self.existe(['tudo bem', 'como você está', 'está tudo bem', 'está tude bem com você']):
            frases = [f'eu estou bem, {self.pessoa}, obrigada',
                      f'estou bem, muito obrigada, {self.pessoa}',
                      f'eu estou bem {self.pessoa}, como vai você?']
            fala = frases[randint(0, len(frases) - 1)]
            self.engine_fala(fala)
            self.voz_data = ' '
            return
        elif self.existe(['qual é seu nome', 'me dia seu nome', 'seu nome é', 'seu nome']):
            self.engine_fala(f'Meu nome é {self.nome_assistente}')
            return
        elif self.existe(['como você está', 'está tudo bem com você', 'está feliz']):
            falas = [f'eu estou bem {self.pessoa}, obrigada por se preocupar',
                     f'eu estou ótima, {self.pessoa}, obrigada'
                     f'eu estou muito feliz como estou hoje, {self.pessoa}']
            fala = falas[randint(0, len(falas) - 1)]
            self.engine_fala(fala)
            self.voz_data = ' '
            return
        elif self.existe(['cu', 'caralho', 'porra', 'tá surda', 'cú']):
            self.engine_fala('Olha a boca menino')
            self.engine_fala('tenha modas')
            self.voz_data = ' '
            return
        elif self.existe(despedidas):
            self.fechar_assistente()
        elif self.existe(['bom dia', 'boa tarde', 'boa noite']):
            self.Boas_vindas()
            self.voz_data = ' '
            return
        elif self.existe(['funcionando bem', 'bem', 'como você tem estado', 'você tem estado', 'tem estado']):
            self.engine_fala(f'Eu estou funcionando bem e sem problemas, {self.pessoa}, obrigada por perguntar')
            self.engine_fala('como você está?')
            while True:
                voz = self.pegar_comandos_separados()
                if 'bem' in voz:
                    self.engine_fala('Que bom, espero que continue assim!')
                    break
                if 'mal' in voz or 'mau' in voz:
                    self.engine_fala('que pena, eu sei que logo logo vai passar')
                    break
            self.voz_data = ' '
            return
        else:
            self.respostas()
            if self.voz_data.isspace():
                self.run()
            if self.voz_data != " ":
                if self.retornar_fala_de_txt_resposta(str(self.voz_data)) is None:
                    self.escrever_em_txt_dados(str(self.voz_data))
                    self.voz_data = ' '
                    self.run()
                else:
                    self.engine_fala(self.retornar_fala_de_txt_resposta(str(self.voz_data)))
                    self.voz_data = ' '
                    self.run()

    # comandos
    def respostas(self):
        cod = float(self.retornar_valor_previsto(self.voz_data))
        for c in self.voz_data.split(" "):
            if c not in self.vocabulario:
                cod = -1
        # pesquisar no google
        if self.existe(['pesquise por', 'pesquisar por', 'pesquise no google por']) or int(cod) == 3:
            regex = re.compile(r"\s[porsbequialcnd]+(\s.*)", flags=re.I)
            termo = regex.findall(self.voz_data)
            url = "http://google.com/search?q=" + str(termo[0]).strip()
            webbrowser.get().open(url)
            self.voz_data = ' '
            self.engine_fala(f"Aqui está o que você pediu sobre {termo[0]} no google")
            self.voz_data = " "
            return
        # alterar nome
        elif self.existe(["mudar nome", "nome", "mudar"]):
            self.engine_fala("Beleza, digita para mim o novo nome")
            novo_nome = self.chamar_valor("Digite o novo nome: ")
            self.arquivoR[1] = novo_nome
            self.engine_fala("Pronto, nome alterado")
            self.voz_data = " "
            return
        # gmail
        elif self.existe(['email', 'entrar no gmail', 'gmail']) or int(cod) == 4:
            url = "https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            self.engine_fala("O gmail está aberto")
            self.voz_data = ' '
            return
        # youtube
        elif self.existe(["pesquise no youtube"]) or int(cod) == 5:
            regex = re.compile(r"\s[youtbepralgs]+\s(?:[porsbealgcind]+)?\s(?:[porsbealg]+)?(.*)", flags=re.I)
            termo = regex.findall(self.voz_data)
            url = "http://www.youtube.com/results?search_query=" + str(termo[0]).strip()
            webbrowser.get().open(url)
            self.voz_data = ' '
            self.engine_fala(f"Aqui está o que você pediu sobre no {str(termo[0])} youtube")
            return
        # abrir algo
        elif self.existe(["abrir "]) or int(cod) == 6:
            regex = re.compile(r"[abrie]+\s(?:\w+)?(.*)", flags=re.I)
            termo = regex.findall(self.voz_data)
            self.abrir_algo(str(termo[0]))
            self.voz_data = ' '
            self.engine_fala(f"O {str(termo[0])} está aberto, pronto.")
            return
        # abrir google
        elif self.existe(['abra o google']) or int(cod) == 7:
            open('www.google.com')
            self.engine_fala('pronto')
            self.voz_data = ' '
            return
        # fechar aba do chrome
        elif self.existe(["fechar aba", 'fechar a', 'aba']) or int(cod) == 8:
            pyautogui.PAUSE = 1
            pyautogui.hotkey('ctrl', 'w')
            self.engine_fala("Pronto.")
            self.voz_data = ' '
            return
        # fechar tudo
        elif self.existe(["fechar abas", 'fechar todas as abas', 'fechar tudo']) or int(cod) == 9:
            pyautogui.PAUSE = 1
            pyautogui.hotkey('alt', 'f4')
            self.engine_fala("Pronto.")
            self.voz_data = ' '
            return
        # escrever algo
        elif self.existe(['escreva para mim', 'escreva']) or int(cod) == 10:
            if self.existe(['assunto copiado', 'assunto', 'copiado', 'escrever dados copiado']):
                pyautogui.PAUSE = 1
                copy(self.aux)
                pyautogui.hotkey('ctrl', 'v')
                return
            escrever = self.voz_data
            regex = re.compile(r"\s?[escrvapmiof]+\s?(?:[escrvapmiof]+)?\s?(?:[escrvapmiof]+)?\s?(.*)", flags=re.I)
            find = regex.findall(escrever)
            copy(str(find[0]))
            pyautogui.hotkey('ctrl', 'v')
            self.voz_data = ' '
            return
        # falar hora
        elif self.existe(['me fale as horas', 'fale as horas', 'horas', 'que horas são']) or int(cod) == 0:
            self.horario()
            self.voz_data = ' '
            return
        # falar data
        elif self.existe(['me fale o dia de hoje', 'fale a data de hoje', 'que dia é hoje', 'data']) or int(cod) == 1:
            self.datahj()
            self.voz_data = ' '
            return
        # parar
        elif self.existe(['parar', 'descansar', 'pausar', 'dar um tempo']) or int(cod) == 11:
            self.engine_fala('Beleza')
            self.engine_fala('estou aqui te esperando')
            self.engine_fala('se precisar de algo, só dizer para voltar')
            while True:
                voz = self.pegar_comandos_separados()
                if "está" in voz or "aí" in voz:
                    self.notificar("Estou aqui sim, esperando você chamar, para chamar basta dizer 'voltar' ou "
                                   "'retornar'")
                elif 'voltar' in voz:
                    self.engine_fala('Ok')
                    self.engine_fala('Voltando')
                    self.engine_fala('Não me deixe sozinha por muito tempo')
                    self.engine_fala('vamos fazer alguma coisa logo')
                    self.run()
                elif 'retornar' in voz:
                    self.engine_fala('Ok')
                    self.engine_fala('Retornando')
                    self.engine_fala('Ficar em silencio é chato')
                    self.engine_fala('Me fale algo para fazer')
                    self.run()
        # pesquisar na wikipedia
        elif self.existe(['assunto', 'wikipedia', 'pesquise um assunto']) or int(cod) == 12:
            try:
                self.engine_fala('Beleza, me fale qual o assunto que você quer que eu pesquise?')
                voz = self.engine_reconition_online()
                if voz is None:
                    voz = self.pegar_comandos_separados()
                set_lang("pt")
                if self.existe(["grande", "bastante", "maior"]):
                    resultadowik = summary(voz, sentences=10)
                else:
                    resultadowik = summary(voz, sentences=2)
                self.engine_fala('Você deseja ouvir o assunto ou escrever em outro lugar:')
                while True:
                    voza = str(self.pegar_comandos_separados())
                    if 'ouvir' in voza:
                        self.engine_fala(resultadowik)
                        return
                    elif 'escrever' in voza:
                        self.aux = resultadowik
                        break
                    elif 'escrever em' in voza:
                        self.aux = resultadowik
                        break
                    elif 'escrever em outro lugar' in voza:
                        self.aux = resultadowik
                        break
            except:
                self.engine_fala('Desculpe, não consegui me conectar a internet')
            self.voz_data = ' '
            return
        # tempo
        elif self.existe(['me diga o clima', 'clima', 'me diga o tempo de hoje', 'tempo de hoje', 'tempo']) or int(
                cod) == 2:
            try:
                url = get('https://api.hgbrasil.com/weather')
                url_json = url.json()
                # hoje

                cida = url_json['results']['city']
                temperatura = url_json['results']['temp']
                condicao = url_json['results']['description']
                humidade = url_json['results']['humidity']
                velocidade_vento = url_json['results']['wind_speedy']

                self.engine_fala("O tempo")
                self.engine_fala("na cidade de " + cida + ":")
                self.engine_fala("A temperatura é igual a " + str(temperatura) + "°C")
                self.engine_fala("A condição de hoje é: " + condicao)
                self.engine_fala("A humidade é de " + str(humidade) + '%')
                self.engine_fala("A velocidade do vento é de " + str(velocidade_vento))
                self.engine_fala('Você deseja ver um resumo dos próximos 10 dias?')
                while True:
                    voz = str(self.pegar_comandos_separados())
                    aux = ''
                    if 'sim' in voz:
                        for c in range(10):
                            data = url_json['results']['forecast'][c]['date']
                            dia = url_json['results']['forecast'][c]['weekday']
                            maxi = url_json['results']['forecast'][c]['max']
                            mini = url_json['results']['forecast'][c]['min']
                            descricao = url_json['results']['forecast'][c]['description']
                            aux += ("Data: " + str(data) + ", Dia da semana: " + str(dia) + ", Temp. máxima: " + str(
                                maxi) + ', Temp. mínima:' + str(mini) + ", Clima: " + str(descricao) + "\n")
                        pyautogui.alert(aux, title='Resumo dos próximos dias')
                        break
                    if 'não' in voz or "não quero" in voz:
                        self.engine_fala("Beleza, vamos fazer o que agora?")
                        break
            except exceptions:
                self.engine_fala('Desculpe, mas não consegui me conectar a a internet')
            self.voz_data = ' '
            return
        elif self.existe(['faça uma conta para mim', 'calculadora', 'calcular', 'faça uma conta']) or int(cod) == 13:
            self.calculadora()
            self.voz_data = ' '
            return
        elif self.existe(['qr code', 'code', 'faça um qr code', 'faça um code']) or int(cod) == 14:
            self.criar_qrcode()
            self.voz_data = ' '
            return
        elif self.existe(["tirar foto da tela", "tirar foto", "foto da tela"]) or int(cod) == 15:
            pyautogui.screenshot(rf"C:\Users\{getlogin()}\Desktop\my_screenshot.png")
            self.engine_fala("Pronto, foto salva na área de trabalho")
            self.voz_data = ' '
            return
        elif self.existe(["me mande uma notificação", "mande uma notificação", "notificação"]) or int(cod) == 16:
            if self.existe(['assunto', "assunto copiado"]):
                self.notificar(self.aux)
                self.voz_data = ' '
                return
            self.engine_fala("Qual o assunto da notificação: ")
            while True:
                vozNoti = self.engine_reconition_online()
                if vozNoti is None:
                    vozNoti = self.pegar_comandos_separados()
                if vozNoti is not None:
                    break
            self.notificar(vozNoti)
            self.voz_data = ' '
            return
        elif self.existe(["analisar dados", "dados", "fazer uma análise", 'análise', 'tabela', 'excel']) or int(
                cod) == 17:
            self.engine_fala("Certo, digita para mim o nome do arquivo em Excel(o arquivo tem que está na área de "
                             "trabalho)")
            nome = self.chamar_valor(text="Digite o nome do arquivo: ")
            dirs = listdir(rf"C:\\Users\\{getlogin()}\\Desktop")
            saber_se_existe = 0
            for dire in dirs:
                if nome in dire:
                    if ".xlsx" in dire or ".xlsm" in dire:
                        saber_se_existe += 1
                    else:
                        self.engine_fala("O nome informado não é de um arquivo em excel")
                        self.engine_fala("Digite novamente")
            if saber_se_existe == 0:
                while True:
                    nome = self.chamar_valor(text="Digite novamente o nome do arquivo")
                    for dire in dirs:
                        if nome in dire:
                            if ".xlsx" in dire or ".xlsm" in dire:
                                self.engine_fala("Pronto, agora foi encontrado")
                                saber_se_existe = 0
                                break
                            else:
                                self.engine_fala("O nome informado não é de um arquivo em excel")
                                self.engine_fala("Digite novamente")
                                break
                    if saber_se_existe == 0:
                        break
            tabela = pd.read_excel(rf"C:\\Users\\{getlogin()}\\Desktop\\{nome}.xlsx")
            colunas = tabela.columns
            resultado = pd.DataFrame()

            op = ""
            cont = 1
            for coluna in colunas:
                op += f"{cont}° coluna: {coluna}\n"
                cont += 1
            self.engine_fala("Digita para mim o que você quer fazer(Exemplo: ColunaTal vezes ColunaTal2)?")
            cont = 1
            while True:
                self.engine_fala("Digite break para parar, digite o p para saber as opções")
                oq = self.chamar_valor(text="Digite a expressão que deseja fazer:")
                try:
                    if "+" in oq:
                        conta = oq
                        oq = oq.split("+")
                        for i in range(len(oq)):
                            oq[i] = oq[i].replace("_", " ")
                        resultado[f"{cont}° modificação:"] = tabela[oq[0].strip()] + tabela[oq[1].strip()]
                        tabela[f"{cont}° modificação:"] = resultado[f"{cont}° modificação:"]
                        op += f"{cont}° conta entre colunas: {conta}, nome registrado: {cont}° modificação:\n"
                        self.engine_fala("Pronto")
                        cont += 1
                    elif "/" in oq:
                        conta = oq
                        oq = oq.split("/")
                        for i in range(len(oq)):
                            oq[i] = oq[i].replace("_", " ")
                        resultado[f"{cont}° modificação:"] = tabela[oq[0].strip()] / tabela[oq[1].strip()]
                        tabela[f"{cont}° modificação:"] = resultado[f"{cont}° modificação:"]
                        op += f"{cont}° conta entre colunas: {conta}, nome registrado: {cont}° modificação:\n"
                        self.engine_fala("Pronto")
                        cont += 1
                    elif "*" in oq:
                        conta = oq
                        oq = oq.split("*")
                        for i in range(len(oq)):
                            oq[i] = oq[i].replace("_", " ")
                        resultado[f"{cont}° modificação:"] = tabela[oq[0].strip()] * tabela[oq[1].strip()]
                        tabela[f"{cont}° modificação:"] = resultado[f"{cont}° modificação:"]
                        op += f"{cont}° conta entre colunas: {conta}, nome registrado: {cont}° modificação:\n"
                        self.engine_fala("Pronto")
                        cont += 1
                    elif "-" in oq:
                        conta = oq
                        oq = oq.split("-")
                        for i in range(len(oq)):
                            oq[i] = oq[i].replace("_", " ")
                        resultado[f"{cont}° modificação:"] = tabela[oq[0].strip()] - tabela[oq[1].strip()]
                        tabela[f"{cont}° modificação:"] = resultado[f"{cont}° modificação:"]
                        op += f"{cont}° conta entre colunas: {conta}, nome registrado: {cont}° modificação:\n"
                        self.engine_fala("Pronto")
                        cont += 1
                    elif "^" in oq or "**" in oq:
                        conta = oq
                        oq = oq.split("^")
                        for i in range(len(oq)):
                            oq[i] = oq[i].replace("_", " ")
                        resultado[f"{cont}° modificação:"] = tabela[oq[0].strip()] ** tabela[oq[1].strip()]
                        tabela[f"{cont}° modificação:"] = resultado[f"{cont}° modificação:"]
                        op += f"{cont}° conta entre colunas: {conta}, nome registrado: {cont}° modificação:\n"
                        self.engine_fala("Pronto")
                        cont += 1
                    elif "agrupar_por" in oq:
                        self.engine_fala("Vou avisando que não é possível integrar outras colunas ou linhas para este"
                                         "resultado")
                        self.engine_fala("Apenas exportar para alguma extensão(Excel, csv, json, etc)")
                        # agrupar_por coluna o_que_fazer quais_colunas_querver
                        # 0             1       2           3 para frente
                        if "soma" in oq:
                            oq = oq.split()
                            coluns = []
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            for c in range(3, len(oq)):
                                coluns.append(oq[c])
                            resultado = tabela.groupby(by=str(oq[1])).sum().loc[:, coluns]
                            resultado.to_excel(fr"C:\Users\{getlogin()}\Desktop\resultado agrupado.xlsx")
                            self.engine_fala("Pronto, arquivo salvo na área de trabalho")
                            continue
                        if "media" in oq or "média" in oq:
                            oq = oq.split()
                            coluns = []
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            for c in range(3, len(oq)):
                                coluns.append(oq[c])
                            resultado = tabela.groupby(by=oq[1]).mean().loc[:, coluns]
                            resultado.to_excel(fr"C:\Users\{getlogin()}\Desktop\resultado agrupado.xlsx")
                            self.engine_fala("Pronto, arquivo salvo na área de trabalho")
                            continue
                        if "mediana" in oq:
                            oq = oq.split()
                            coluns = []
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            for c in range(3, len(oq)):
                                coluns.append(oq[c])
                            resultado = tabela.groupby(by=oq[1]).median().loc[:, coluns]
                            resultado.to_excel(fr"C:\Users\{getlogin()}\Desktop\resultado agrupado.xlsx")
                            self.engine_fala("Pronto, arquivo salvo na área de trabalho")
                            continue
                    elif "ordenar_por" in oq:
                        oq.split()
                        for i in range(len(oq)):
                            oq[i] = oq[i].replace("_", " ")
                        try:
                            resultado = resultado.sort_values(by=oq[1], ascending=oq[2])
                        except IndexError:
                            resultado = resultado.sort_values(by=oq[1])
                        except exceptions:
                            resultado = resultado.sort_values(by=oq[1])
                    elif "menor_valor" in oq:
                        pyautogui.alert(title="Menor valor da tabela em memória", text=resultado.min())
                    elif "maior_valor" in oq:
                        pyautogui.alert(title="Menor valor da tabela em memória", text=resultado.max())
                    elif "descrição" in oq or "descricao" in oq:
                        pyautogui.alert(
                            title="Descrição das duas tabelas:", text="Tabela resultado:\n" + resultado.describe())
                        pyautogui.alert(text="Tabela que você subiu:\n" + tabela.describe(), title="Descrição das duas "
                                                                                                   "tabelas:")
                    # aplicar trocar coluna/nome_da_tabela_que_usou dado1 dado2
                    elif "aplicar" in oq:
                        if "trocar" in oq:
                            if nome in oq:
                                oq.split()
                                for i in range(len(oq)):
                                    oq[i] = oq[i].replace("_", " ")
                                tabela.apply(lambda x: x.replace(oq[3], oq[4]))
                            else:
                                oq.split()
                                for i in range(len(oq)):
                                    oq[i] = oq[i].replace("_", " ")
                                tabela[oq[2]].apply(lambda x: x.replace(oq[3], oq[4]))
                        self.engine_fala("Pronto, conta feita")

                    # mudar conta onde_fazer o_que_fazer numero
                    elif "mudar" in oq and "conta" in oq:
                        if nome in oq and "somar" in oq:
                            oq.split()
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            tabela.add(int(oq[4]))
                        else:
                            if "somar" in oq:
                                oq.split()
                                for i in range(len(oq)):
                                    oq[i] = oq[i].replace("_", " ")
                                resultado[oq[2]].add(int(oq[4]))
                        if nome in oq and "subtrair" in oq:
                            oq.split()
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            tabela.sub(int(oq[4]))
                        else:
                            if "subtrair" in oq:
                                oq.split()
                                for i in range(len(oq)):
                                    oq[i] = oq[i].replace("_", " ")
                                resultado[oq[2]].sub(int(oq[4]))
                        if nome in oq and "multiplicar" in oq:
                            oq.split()
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            tabela.mul(int(oq[4]))
                        else:
                            if "multiplicar" in oq:
                                oq.split()
                                for i in range(len(oq)):
                                    oq[i] = oq[i].replace("_", " ")
                                resultado[oq[2]].mul(int(oq[4]))
                        if nome in oq and "dividir" in oq:
                            oq.split()
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            tabela.div(int(oq[4]))
                        else:
                            if "dividir" in oq:
                                oq.split()
                                for i in range(len(oq)):
                                    oq[i] = oq[i].replace("_", " ")
                                resultado[oq[2]].div(int(oq[4]))
                        self.engine_fala("Pronto, conta feita")

                    # pesquisar (expressão que deseja usar para pesquisa)
                    elif "pesquisar" in oq:
                        if nome in oq:
                            oq.split()
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            pd.set_option("max_columns", None)
                            pd.set_option("max_rows", None)
                            pyautogui.PAUSE = 1.5
                            pyautogui.press("win")
                            pyautogui.write("Bloco de notas")
                            pyautogui.press("backspace")
                            pyautogui.press("enter")
                            copy(str(tabela.query(oq[1])))
                            pyautogui.hotkey("ctrl", "v")
                        else:
                            oq.split()
                            for i in range(len(oq)):
                                oq[i] = oq[i].replace("_", " ")
                            pd.set_option("max_columns", None)
                            pd.set_option("max_rows", None)
                            pyautogui.PAUSE = 1.5
                            pyautogui.press("win")
                            pyautogui.write("Bloco de notas")
                            pyautogui.press("backspace")
                            pyautogui.press("enter")
                            copy(str(resultado.query(oq[1])))
                            pyautogui.hotkey("ctrl", "v")
                    elif "op" in oq:
                        pyautogui.alert(title="Opções de colunas para contas", text=op)
                    elif "break" in oq:
                        resultado.to_excel(fr"C:\Users\{getlogin()}\Desktop\resultado.xlsx")
                        tabela.to_excel(fr"C:\Users\{getlogin()}\Desktop\tabela_usada.xlsx")
                        self.engine_fala("Pronto, o arquivo gerado como resultado foi salvo na área de trabalho com o "
                                         "nome resultado.xlsx")
                        break
                    else:
                        self.engine_fala("Você digitou algo errado ou fora das minhas configurações, por favor tente "
                                         "novamente")
                except Exception:
                    self.engine_fala("Você digitou algo errado ou fora das minhas configurações, por favor tente "
                                     "novamente")
                except BaseException:
                    self.engine_fala("Você digitou algo errado ou fora das minhas configurações, por favor tente "
                                     "novamente")
            self.voz_data = ' '
            return
        elif self.existe(["senha do wifi", "wifi", "descobrir senha", "senha"]) or int(cod) == 18:
            self.engine_fala("Digite o nome do wifi registrado")
            nome = self.chamar_valor(text="Digite o noem da wifi:")
            informacoes = check_output(["netsh", "wlan", "show", "profile", nome, "key", "=", "clear"],
                                       encoding='cp858')
            for c in informacoes.split("\n"):
                if "Conteúdo da chave" in c:
                    pos = c.find(":")
                    senha = c[pos + 2:]
                    self.notificar(senha)
            self.voz_data = ' '
            return
        elif self.existe(["memória ram usada", "usada", "memória ram", "ram", "memória"]) or int(cod) == 19:
            ram_usada = f"{virtual_memory().percent:,.2f}"
            ram_disponivel = f"{virtual_memory().available * 100 / virtual_memory().total:,.2f}"
            self.engine_fala(f"Memória ram usada: {ram_usada}%, Memória ram disponível: {ram_disponivel}%")
            self.voz_data = ' '
            return
        elif self.existe(["mandar email", "mandar e-mail", "email", 'e-mail', "mandar", "enviar", "enviar email",
                          "enviar email"]) or int(cod) == 20:
            self.engine_fala("Certo, digita para mim o email da pessoa que vai recever")
            outlook = win32.Dispatch('outlook.application')
            email = outlook.CreateItem(0)
            email.To = self.chamar_valor("Digite o email da pessoa que vai receber: ")
            self.engine_fala("agora digita o assunto")
            email.Subject = self.chamar_valor("Qual o assunto do email: ")

            global conteudo

            while True:
                self.engine_fala("Você quer escrever o conteúdo ou importar de um txt?")
                importar = self.pegar_comandos_separados()
                if "importar" in importar or 'texto' in importar or 'arquivo' in importar or 'txt' in importar:
                    conteudo = str(open(fr"C:\Users\{getlogin()}\Desktop\{importar}"))
                    break
                if "digitar" in importar or 'texto' in importar:
                    conteudo = self.chamar_valor("Digite o conteúdo: ")
                    break

            while True:
                self.engine_fala("O email tem anexo")
                anexo_sim_nao = self.pegar_comandos_separados()
                if "sim" in anexo_sim_nao:
                    self.engine_fala("Qual o nome do arquivo(ele precisa estar na área de trabalho)")
                    self.engine_fala("Ou digite o caminho inteiro do arquivo, com extensão")
                    arquivo = self.chamar_valor("Digite: ")
                    if "C:" in arquivo or ":" in arquivo or "\"" in arquivo:
                        email.Attachments.Add(arquivo)
                        break
                    else:
                        nome_arquivo = arquivo
                        anexo = rf"C:\Users\{getlogin()}\Desktop\{nome_arquivo}"
                        email.Attachments.Add(anexo)
                        break
                if "não" in anexo_sim_nao:
                    break
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
            self.voz_data = ' '
            return
        else:
            # options apps
            if self.existe(opcoes):
                self.abrir_algo(self.voz_data.lower())
            elif self.existe(['fale as opções', 'opções de aplicativos', 'opções']):
                self.engine_fala('beleza, vou te falar as opções, por favor diga apenas o número da opção que você '
                                 'quer '
                                 'depois de fechar a janela.')
                self.engine_fala('As opções são: ')
                aux = ''
                cont = 1
                for op in opcoes:
                    aux += f'{cont}° opção é: {op}\n'
                    cont += 1
                pyautogui.alert(aux, title='Opções')
                self.engine_fala('qual opção você quer?')
                while True:
                    vozn = self.pegar_comandos_separados()
                    vozn = self.ajeitar_numero(vozn)
                    if type(vozn) == int:
                        self.abrir_algo(opcoes[vozn])
            return

    @staticmethod
    def ajeitar_numero(numero):
        nums = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
        for n in nums:
            if n in numero:
                return nums.index(n) + 1

    def escrever_em_txt_dados(self, lista_palavras):
        lista_frases = []
        contR = int(self.arquivoF[-2]) + 1
        with open(r"../databaseF.txt", 'a', encoding='utf-8') as Fd:
            lista_palavras = lista_palavras.replace(" ", "_")
            Fd.write('\n')
            Fd.write(f'{contR} ')
            Fd.write(f'{lista_palavras} ')
        self.engine_fala("Quais são as possíveis respostas para essa pergunta?")
        self.engine_fala("fale 'break'/'parar' para parar!!!")
        while True:
            aux = self.engine_reconition_online()
            if aux is None:
                aux = self.pegar_comandos_separados()
            if aux is not None:
                if 'break' == aux:
                    break
                if 'parar' == aux:
                    break
                self.engine_fala("Pronto, frase salva no banco de dados")
                lista_frases.append(aux)
        self.escrever_em_txt_resposta(lista_frases, contR)
        self.engine_fala("Pronto, frases salvas no banco de dados")

    @staticmethod
    def escrever_em_txt_resposta(lista_palavras, cont):
        with open(r"../databaseR.txt", 'a', encoding='utf-8') as R:
            for passw in lista_palavras:
                passw = passw.replace(" ", "_")
                R.write('\n')
                R.write(f'{cont} ')
                R.write(f'{passw} ')

    def retornar_fala_de_txt_resposta(self, fala):
        try:
            index = int(self.arquivoF[self.arquivoF.index(fala.replace(" ", "_")) - 1])
            resposta = []
            for c in range(0, len(self.arquivoR), 2):
                if int(self.arquivoR[c]) == int(index):
                    resposta.append(self.arquivoR[c + 1])
            if len(resposta) > 1:
                return resposta[randint(0, len(resposta) - 1)].replace("_", " ")
            return resposta[0].replace("_", " ")
        except ValueError:
            return None

    def fechar_assistente(self):
        self.engine_fala("Tenha um bom dia! até logo!")
        with open('../rede_neural.xml', 'wb') as fi:
            dump(self.netWork, fi)
        janela.attributes("-topmost", True)
        self.is_run = False
        janela_aparecer.fechar()
        exit(0)

    def run(self):
        while self.is_run:
            try:
                self.voz_data = self.engine_reconition_online()
                if self.voz_data is None:
                    data = stream.read(8000)
                    if len(data) == 0:
                        break
                    if rec.AcceptWaveform(data):
                        resultado = rec.FinalResult()
                        resultado = loads(resultado)
                        if resultado is not None:
                            self.voz_data = resultado['text'].lower()
                            self.conversas()
                else:
                    self.conversas()
            except sr.WaitTimeoutError:
                self.engine_fala('Por favor, não fique muito tempo sem falar')
                continue

    def criar_qrcode(self):
        self.engine_fala("Você deseja criar vários qr codes ou apenas um?")
        try:
            while True:
                voz = self.engine_reconition_online()
                if voz is None:
                    voz = self.pegar_comandos_separados()
                if voz is not None:
                    break
            if 'apenas um' in voz or 'um' in voz or 'apenas' in voz:
                self.engine_fala('Beleza, digita para mim o link que você deseja usar para criar o QR code')
                link = self.chamar_valor(text="Digite o link: ")
                self.engine_fala('Agora digite para mim o nome do arquivo: ')
                nome = self.chamar_valor(text="Digite o nome do arquivo: ")
                self.engine_fala('Certo, espera um pouco aí...')
                meu_qrcode = qrcode.make(link)
                meu_qrcode.save(fr"C:\Users\{getlogin()}\Desktop\qrcode_{nome}.png")
                self.engine_fala("Pronto, já está na sua área de trabalho")
            else:
                self.engine_fala('Beleza, quantos você quer fazer?')
                while True:
                    vozq = self.engine_reconition_online()
                    if vozq is None:
                        vozq = self.pegar_comandos_separados()
                        vozq = self.ajeitar_numero(vozq)
                    if vozq is not None:
                        break
                links = {}
                for c in range(int(vozq)):
                    nome = self.chamar_valor(text=f"{(c + 1)}°: Digite o nome do arquivo: ")
                    link = self.chamar_valor(text=f"{(c + 1)}°: Digite o link: ")
                    links[f'{nome}'] = str(link)
                for produto in links:
                    meu_qrcode = qrcode.make(links[produto])
                    meu_qrcode.save(rf"C:\Users\{getlogin()}\Desktop\qrcode_{produto}.png")
                self.engine_fala('Pronto, qr codes feitos')
        except BaseException:
            self.engine_fala('Desculpe, não pude realizar o processo, algo deu errado')

    def calculadora(self):
        self.engine_fala('Beleza, o que você deseja calcular?')
        self.engine_fala('Por favor, falar apenas equações simples, afinal estou em fase de desenvolvimento')
        try:
            while True:
                voz = str(self.engine_reconition_online().lower())
                if voz is None:
                    voz = self.pegar_comandos_separados().lower()
                    break
                if voz is not None:
                    break
            voz = voz.split()
            while True:
                indexAux = ''
                if str(voz).count("fatorial"):
                    nums = self.separar(voz, (voz.index("fatorial")))
                    num = nums[1]
                    valor_total = 1
                    for c in range(1, num + 1):
                        valor_total *= c
                    valor_total = int(valor_total)
                    voz.insert(int(voz.index("fatorial")), str(valor_total))
                    voz.remove("fatorial")
                    voz.remove("de")
                    voz.remove(str(nums[1]))
                    continue
                if str(voz).count('elevado') != 0:
                    if '^' in voz:
                        indexAux = '^'
                    if 'elevado' in voz:
                        indexAux = 'elevado'
                    nums = self.separar(voz, (voz.index(indexAux)))
                    valor_total = pow(nums[0], nums[1])
                    valor_total = int(valor_total)
                    voz.insert(int(voz.index(indexAux)), str(valor_total))
                    voz.remove(indexAux)
                    if indexAux == 'elevado':
                        voz.remove('a')
                    voz.remove(str(nums[0]))
                    voz.remove(str(nums[1]))
                    continue
                if str(voz).count('x') != 0 or str(voz).count('vezes') != 0:
                    if 'x' in voz:
                        indexAux = 'x'
                    if 'vezes' in voz:
                        indexAux = 'vezes'
                    nums = self.separar(voz, voz.index(indexAux))
                    valor_total = (nums[0] * nums[1])
                    voz.insert(int(voz.index(indexAux)), str(valor_total))
                    voz.remove(indexAux)
                    voz.remove(str(nums[0]))
                    voz.remove(str(nums[1]))
                    continue
                if str(voz).count('/') != 0 or str(voz).count('dividido') != 0 or str(voz).count("÷"):
                    if '÷' in voz:
                        indexAux = '÷'
                    if 'dividido' in voz:
                        indexAux = 'dividido'
                    if '/' in voz:
                        indexAux = '/'
                    nums = self.separar(voz, voz.index(indexAux))
                    valor_total = (nums[0] / nums[1])
                    voz.insert(int(voz.index(indexAux)), str(valor_total))
                    voz.remove(indexAux)
                    if indexAux == "dividido":
                        voz.remove("por")
                    voz.remove(str(nums[0]))
                    voz.remove(str(nums[1]))
                    continue
                if str(voz).count('somado') != 0 or str(voz).count('+') != 0:
                    if '+' in voz:
                        indexAux = '+'
                    if 'somado' in voz:
                        indexAux = 'somado'
                    nums = self.separar(voz, voz.index(indexAux))
                    valor_total = (nums[0] + nums[1])
                    voz.insert(int(voz.index(indexAux)), str(valor_total))
                    voz.remove(indexAux)
                    if indexAux == 'somado':
                        voz.remove('a')
                    voz.remove(str(nums[0]))
                    voz.remove(str(nums[1]))
                    continue
                if str(voz).count('subtraido') != 0 or str(voz).count('-') != 0:
                    if '-' in voz:
                        indexAux = '-'
                    if 'subtraido' in voz:
                        indexAux = 'subtraido'
                    nums = self.separar(voz, voz.index(indexAux))
                    valor_total = (nums[0] - nums[1])
                    voz.insert(int(voz.index(indexAux)), str(valor_total))
                    voz.remove(indexAux)
                    if indexAux == 'subtraido':
                        voz.remove('de')
                    voz.remove(str(nums[0]))
                    voz.remove(str(nums[1]))
                    continue
                if not str(voz).isalnum():
                    self.engine_fala('Deseja ouvir o resultado ou colar em algum lugar?')
                    while True:
                        vozsair = self.engine_reconition_online()
                        if vozsair is None:
                            vozsair = self.pegar_comandos_separados().lower()
                            break
                        if vozsair is not None:
                            vozsair = vozsair.lower()
                            break
                    if 'colar' in vozsair:
                        self.aux = vozsair
                        break
                    if 'ouvir' in vozsair:
                        self.engine_fala('O resultado é:' + str(voz).strip('[]').replace("'", ""))
                        break
                if not str(voz).isalpha():
                    self.engine_fala("Pronto")
                    self.engine_fala("Retornando ao módulo principal")
        except BaseException:
            self.engine_fala("Desculpe, algo deu errado")
            self.engine_fala("Pode ter sido a conexão, ou algum valor inválido")

    @staticmethod
    def separar(voz_data, index=0):
        aux1 = 0
        aux2 = 0
        for c in range(index, -1, -1):
            if voz_data[c].isnumeric():
                aux1 = voz_data[c]
                break
        for c2 in range(index, len(voz_data)):
            if voz_data[c2].isnumeric():
                aux2 = voz_data[c2]
                break
        return [int(aux1), int(aux2)]

    @staticmethod
    def engine_fala(text):
        """
        fala da assitente virtual
        """
        text = str(text)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()

    def engine_reconition_online(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, 5, 5)
            try:
                self.voz_data = r.recognize_google(audio, language='pt')
                return self.voz_data.lower()
            except sr.UnknownValueError:
                self.engine_fala('Por favor, fale novamente, eu não entendi o que você falou')
            except sr.RequestError:
                return None

    def Boas_vindas(self):
        hora = int(datetime.now().hour)
        if 0 < hora < 12:
            self.engine_fala('Olá')
            self.engine_fala('Bom dia')
        elif 12 <= hora < 18:
            self.engine_fala('Agora não é mais de manhã')
            self.engine_fala('Já passou do meio dia')
            self.engine_fala('Estamos no período da tarde')
            self.engine_fala('Boa tarde')
        else:
            self.engine_fala('Agora não é de manhã')
            self.engine_fala('Já estamos no período noturno')
            self.engine_fala('Boa noite')
        self.engine_fala(f'Oi {self.pessoa}, como você está?')
        voz = self.pegar_comandos_separados()
        if 'estou' in voz or 'obrigado' in voz or 'bem' in voz:
            self.engine_fala('que bom, então, vamos fazer alguma coisa?')
            voz = self.pegar_comandos_separados()
            if 'bora' in voz:
                self.engine_fala('Beleza, bora')
                self.run()
            elif 'beleza' in voz:
                self.engine_fala('Beleza, bora')
                self.run()
            elif 'claro' in voz:
                self.engine_fala('Beleza, bora')
                self.run()
            elif "vamor" in voz:
                self.engine_fala('Beleza, bora')
                self.run()

    @staticmethod
    def notificar(text=''''''):
        notification.notify(title="R.O.X.X.A.N.E", message=text, timeout=20)

    def horario(self):
        hora = datetime.now()
        self.engine_fala('Agora ' + hora.strftime('São %H horas e %M minutos'))

    def datahj(self):
        data = date.today()
        semana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                 'Novembro', 'Dezembro')
        mesatual = (meses[data.month])
        ano = data.strftime(" de %Y")
        self.engine_fala("Hoje é " + semana[data.weekday()])
        self.engine_fala("Dia " + str(data.day) + mesatual + ano)

    def abrir_algo(self, name):
        pyautogui.PAUSE = 1.2
        pyautogui.press('win')
        pyautogui.write(name)
        pyautogui.press('backspace')
        pyautogui.press('enter')
        for l in pacoteOffice:
            if l == name:
                pyautogui.PAUSE = 1.8
                pyautogui.press('enter')
        self.run()

    def chamar_valor(self, text=''):
        try:
            self.tela_valor_digitado(texto=text)
        except BaseException:
            self.pegar_valor()
        return self.var

    def pegar_valor(self):
        try:
            self.var = self.entradac.get()
        except BaseException:
            self.var = None
        self.janelac.destroy()

    def tela_valor_digitado(self, texto):
        self.janelac = Tk()
        self.janelac.title(f"{self.nome_assistente} por chat")
        textoc = Label(self.janelac, text=texto)
        textoc.grid(column=0, row=1, padx=25, pady=50)
        self.entradac = Entry(self.janelac)
        self.entradac.grid(column=0, row=2, padx=60, pady=10)
        botaoc = Button(self.janelac, text="OK", command=self.pegar_valor)
        botaoc.grid(column=0, row=3, padx=60, pady=10)
        self.janelac.geometry("270x200")
        self.janelac.resizable(0, 0)
        self.janelac.mainloop()


class tela(threading.Thread, Label):
    def __init__(self, nome, master):
        threading.Thread.__init__(self)
        self.nome = nome
        self.master_tela = master
        self.texto_resposta = Label(self.master_tela, font=('Arial', 12), fg='Black', bg='white', height=1, width=20)
        self.texto_resposta.grid(column=0, row=1, padx=20, pady=20)
        self.texto_cpu = Label(self.master_tela, font=('Arial', 12), fg='black', bg='white', height=1, width=5)
        self.texto_cpu.grid(column=1, row=2, padx=190, pady=190)

    def run(self):
        self.atualizar()
        self.atualizar_cpu()

    def atualizar(self):
        dataatual = datetime.now().strftime(f'%d/%m/%Y - %H:%M:%S Hrs')
        self.texto_resposta['text'] = dataatual
        # threading.Thread(target=self.atualizar).start()
        self.master_tela.after(1, self.atualizar)

    def atualizar_cpu(self):
        porcentagem = str(cpu_percent())
        self.texto_cpu['text'] = porcentagem + "%"
        # threading.Thread(target=self.atualizar_cpu).start()
        self.master_tela.after(1000, self.atualizar_cpu)

    @staticmethod
    def fechar():
        pyautogui.PAUSE = 1.5
        try:
            locate = pyautogui.locateOnScreen('x.png', grayscale=True)
            locationCenter = pyautogui.center(locate)
        except TypeError:
            locate = pyautogui.locateOnScreen('x2.PNG', grayscale=True)
            locationCenter = pyautogui.center(locate)
        pyautogui.click(locationCenter)

    @staticmethod
    def fechamento_total():
        if virtual_assistente.is_run:
            pass
        else:
            janela.destroy()
            exit(0)


def tela_aviso(texto):
    janelac = Toplevel()
    janelac.title(f"Aviso")
    image_w = PhotoImage(file="../warning.png")
    imagem_label = Label(janelac, image=image_w)
    imagem_label.place(x=0, y=0, relwidth=1, relheight=1)
    textoc = Label(janelac, text=f"{texto:-^60}".upper())
    textoc.place(x=200, y=50, anchor="center")
    janelac.geometry("400x400")
    janelac.resizable(0, 0)
    janelac.mainloop()


# validando arquivos necessários
dependencias = ["model", "Nome.PNG", "Iron-Man-Jarvis.png", "Python.ico", "x.png", "x2.PNG", "databaseC.txt",
                "databaseF.txt", "databaseR.txt"]
for dependencia in dependencias:
    if not exists(dependencia):
        tela_aviso("Alguma dependência não foi satisfeita")
        exit(-1)

model_dependences = ['disambig_tid.int', 'final.mdl', 'Gr.fst', 'HCLr.fst',
                     'ivector', 'mfcc.conf', 'phones.txt', 'README', 'word_boundary.int']
for model_dependence in model_dependences:
    if not exists(f"model/{model_dependence}"):
        tela_aviso("Alguma dependência não foi satisfeita")
        exit(-1)

ivectors = ['final.dubm', 'final.ie', 'final.mat', 'global_cmvn.stats', 'online_cmvn.conf', 'splice.conf']
for ivector in ivectors:
    if not exists(f"model/ivector/{ivector}"):
        tela_aviso("Alguma dependência não foi satisfeita")
        exit(-1)

if not exists(rf"../rede_neural.xml"):


# criando a tela
janela = Tk()
janela.iconbitmap("Python.ico")
background_image = PhotoImage(file="../Nome.PNG")
background_label = Label(janela, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
virtual_assistente = ROXXANE()
if exists(rf"../rede_neural.xml"):
    with open('../rede_neural.xml', 'rb') as f:
        virtual_assistente.netWork = load(f)
virtual_assistente.criar_dataset()
janela.title(f"{virtual_assistente.nome_assistente}")
janela_aparecer = tela(virtual_assistente.nome_assistente, janela)
janela.protocol("WM_DELETE_WINDOW", janela_aparecer.fechamento_total)
janela.geometry('500x300')
janela_aparecer.start()
virtual_assistente.start()
janela.resizable(0, 0)
janela.mainloop()
