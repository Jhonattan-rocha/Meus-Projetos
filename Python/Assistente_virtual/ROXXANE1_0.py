import datetime
import json
import math
import random
import threading
import tkinter as tk
import webbrowser
from datetime import *
from time import sleep
from tkinter import *
import pandas as pd
import psutil
import pyaudio
import pyautogui
import pyperclip
import pyttsx3
import qrcode
import requests
import speech_recognition as sr
import wikipedia
from plyer import notification
from tqdm import tqdm
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()
model = Model("../model")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
despedidas = ['tchal', 'adeus', 'te vejo mais tarde', 'até', 'até logo']
pacoteOffice = ['word', 'excel', 'powerpoint', 'access', 'teams']
opcoes = ['word', 'excel', 'powerpoint', 'access', 'teams', 'genshin impact', 'chrome', 'microsoft edge']


class ROXXANE(threading.Thread):
    def __init__(self, asist_name, person):
        threading.Thread.__init__(self)  # thread da Roxxane
        self.pessoa = person
        self.nome_assistente = asist_name
        self.voz_data = ''
        self.aux = ''
        self.arquivoR = open(r"../databaseR.txt", 'r', encoding='utf-8')
        self.arquivoR = self.arquivoR.read()
        self.arquivoR = self.arquivoR.split()
        self.arquivoF = open(r"../databaseF.txt", 'r', encoding='utf-8')
        self.arquivoF = self.arquivoF.read()
        self.arquivoF = self.arquivoF.split()

    def existe(self, termos):
        for termo in termos:
            if termo in self.voz_data:
                return True

    def pegar_comandos_separados(self):
        while True:
            rec.pause_threshold = 1
            data = stream.read(10000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                resultado = rec.FinalResult()
                resultado = json.loads(resultado)
                if resultado is not None:
                    return resultado['text'].lower()
        # rec.pause_threshold = 1
        # data_audio = stream.read(8000)
        # rec.AcceptWaveform(data_audio)
        # try:
        #     retorno = rec.FinalResult()
        # except:
        #     print('Fala mais alto')
        #     return 'none'
        # return retorno

    def conversas(self):
        if self.existe(['hey', 'hi', 'hello', 'oi', 'holla']):
            greetigns = [f'Oi {self.pessoa}, o que você está fazendo hoje?',
                         f'Oi {self.pessoa}, como eu posso te ajudar?',
                         f'Oi {self.pessoa}, você precisa de algo?',
                         f'Oi {self.pessoa}, como vai você?']
            greet = greetigns[random.randint(0, len(greetigns) - 1)]
            engine_speak(greet)
            self.voz_data = ''

        elif self.existe(['tudo bem', 'como você está', 'está tudo bem', 'está tude bem com você']):
            frases = [f'eu estou bem, {self.pessoa}, obrigada',
                      f'estou bem, muito obrigada, {self.pessoa}',
                      f'eu estou bem {self.pessoa}, como vai você?']
            fala = frases[random.randint(0, len(frases) - 1)]
            engine_speak(fala)
            self.voz_data = ''
        # name
        elif self.existe(['qual é seu nome', 'me dia seu nome', 'seu nome é', 'seu nome']):
            engine_speak(f'Meu nome é {self.nome_assistente}')
        elif self.existe(['como você está', 'está tudo bem com você', 'está feliz']):
            falas = [f'eu estou bem {self.pessoa}, obrigada por se preocupar',
                     f'eu estou ótima, {self.pessoa}, obrigada'
                     f'eu estou muito feliz como estou hoje, {self.pessoa}']
            fala = falas[random.randint(0, len(falas) - 1)]
            engine_speak(fala)
            self.voz_data = ''
        elif self.existe(['cu', 'caralho', 'porra', 'tá surda', 'cú']):
            engine_speak('Olha a boca menino')
            engine_speak('tenha modas')
        elif self.existe(despedidas):
            engine_speak("Tenha um bom dia! até logo!")
            exit(0)
        elif self.existe(['bom dia', 'boa tarde', 'boa noite']):
            hora = int(datetime.datetime.now().hour)
            if 0 <= hora < 12:
                engine_speak('Olá')
                engine_speak('Bom dia')

            elif 12 <= hora < 18:
                engine_speak('Agora não é mais de manhã')
                engine_speak('Já passou do meio dia')
                engine_speak('Estamos no período da tarde')
                engine_speak('boa tarde')

            elif 0 != hora >= 18:
                engine_speak('Agora não é de manhã')
                engine_speak('Já estamos no período noturno')
                engine_speak('Boa noite')
        elif self.existe(['funcionando bem', 'bem', 'como você tem estado', 'você tem estado', 'tem estado']):
            engine_speak(f'Eu estou funcionando bem e sem problemas, {self.pessoa}, obrigada por perguntar')
            engine_speak('como você está?')
            while True:
                voz = self.pegar_comandos_separados()
                if 'bem' in voz:
                    engine_speak('Que bom, espero que continue assim!')
                    break
                if 'mal' in voz or 'mau' in voz:
                    engine_speak('que pena, eu sei que logo logo vai passar')
                    break
        else:
            if self.retornar_fala_de_txt_resposta(str(self.voz_data)) is None:
                self.escrever_em_txt_dados(str(self.voz_data))
                self.voz_data = ''
            else:
                engine_speak(self.retornar_fala_de_txt_resposta(str(self.voz_data)))
                self.voz_data = ''

    # comandos
    def respostas(self):

        # google
        if self.existe(['pesquise por', 'pesquisar por', 'pesquise no google por']):
            search_term = self.voz_data.split("por")[-1]
            url = "http://google.com/search?q=" + str(search_term)
            webbrowser.get().open(url)
            self.voz_data = ''
            engine_speak("Aqui está o que você pediu sobre " + search_term + 'no google')

        # youtube
        elif self.existe(["pesquise no youtube por"]):
            search_term = self.voz_data.split("por")[-1]
            url = "http://www.youtube.com/results?search_query=" + str(search_term)
            webbrowser.get().open(url)
            self.voz_data = ''
            engine_speak("Aqui está o que você pediu sobre" + search_term + 'no youtube')

        # open something
        elif self.existe(["abrir "]):
            search_term = self.voz_data.split()
            search_term.remove('abrir')
            search_term = str(search_term).strip('[]').replace("'", "").replace(',', '')
            abrir_algo(search_term)
            self.voz_data = ''
            engine_speak("O " + search_term + " está aberto, pronto.")

        # open google
        elif self.existe(['abra o google']):
            webbrowser.open('www.google.com')
            engine_speak('pronto')

        # close tab of Chrome
        elif self.existe(["fechar aba", 'fechar a', 'aba']):
            pyautogui.PAUSE = 1
            pyautogui.hotkey('ctrl', 'w')
            engine_speak("Pronto.")

        # close all
        elif self.existe(["fechar abas", 'fechar todas as abas', 'fechar tudo']):
            pyautogui.PAUSE = 1
            pyautogui.hotkey('alt', 'f4')
            engine_speak("Pronto.")

        # write something
        elif self.existe(['escreva para mim', 'escreva']):
            if self.existe(['assunto copiado', 'assunto', 'copiado', 'escrever dados copiado']):
                pyautogui.PAUSE = 1
                pyperclip.copy(self.aux)
                pyautogui.hotkey('ctrl', 'v')
                return
            escrever = self.voz_data.split()
            if 'escreva' in escrever:
                escrever.remove('escreva')
            elif 'escreva' in escrever and escrever.index('escreva') == 0:
                escrever.remove('escreva')
                escrever.remove('para')
                escrever.remove('mim')
            escrever = str(escrever).strip('[]').replace("'", "").replace(',', '')
            pyperclip.copy(escrever)
            pyautogui.hotkey('ctrl', 'v')

        # speak hour
        elif self.existe(['me fale as horas', 'fale as horas', 'horas']):
            horario()

        # speak date
        elif self.existe(['me fale o dia de hoje', 'fale a data de hoje', 'que dia é hoje', 'data']):
            datahj()

        # stop
        elif self.existe(['parar', 'descansar', 'pausar', 'dar um tempo']):
            engine_speak('Beleza')
            engine_speak('estou aqui te esperando')
            engine_speak('se precisar de algo, só dizer para voltar')
            while True:
                voz = self.pegar_comandos_separados()
                if 'voltar' in voz:
                    engine_speak('Ok')
                    engine_speak('Voltando')
                    engine_speak('Não me deixe sozinha por muito tempo')
                    engine_speak('vamos fazer alguma coisa logo')
                    self.run()

                elif 'retornar' in voz:
                    engine_speak('Ok')
                    engine_speak('Retornando')
                    engine_speak('Ficar em silencio é chato')
                    engine_speak('Me fale algo para fazer')
                    self.run()

        # pesquisar na wikipedia
        elif self.existe(['assunto', 'wikipedia', 'pesquise sobre']):
            try:
                engine_speak('Beleza, me fale qual o assunto que você quer que eu pesquise?')
                voz = engine_reconition_online()
                if voz is None:
                    voz = self.pegar_comandos_separados()
                wikipedia.set_lang("pt")
                resultadowik = wikipedia.summary(voz, sentences=2)
                engine_speak('Você deseja ouvir o assunto ou escrever em outro lugar:')
                while True:
                    voz = str(self.pegar_comandos_separados())
                    if 'ouvir' in voz:
                        engine_speak(resultadowik)
                        return
                    elif 'escrever' in voz:
                        self.aux = resultadowik
                        break
                    elif 'escrever em' in voz:
                        self.aux = resultadowik
                        break
                    elif 'escrever em outro lugar' in voz:
                        self.aux = resultadowik
                        break
            except:
                engine_speak('Desculpe, não consegui me conectar a internet')
        # tempo
        elif self.existe(['me diga o clima', 'clima', 'me diga o tempo de hoje', 'tempo de hoje', 'tempo']):
            try:
                url = requests.get('https://api.hgbrasil.com/weather')
                url_json = url.json()
                # hoje

                cida = url_json['results']['city']
                temperatura = url_json['results']['temp']
                condicao = url_json['results']['description']
                humidade = url_json['results']['humidity']
                velocidade_vento = url_json['results']['wind_speedy']

                engine_speak("O tempo")
                engine_speak("na cidade de " + cida + ":")
                engine_speak("Temperatura igual a " + str(temperatura))
                engine_speak("A condição de hoje é: " + condicao)
                engine_speak("A humidade é de " + str(humidade) + '%')
                engine_speak("A velocidade do vento é de " + str(velocidade_vento))

                engine_speak('Você deseja ver um resumo dos próximos 10 dias?')
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
                            aux += (
                                    "Data: " + str(data) + ", Dia da semana: " + str(dia) + ", Temp. máxima: " + str(
                                maxi) + ', Temp. mínima:' + str(mini) + ", Clima: " + str(descricao) + "\n")
                        pyautogui.alert(aux, title='Resumo dos próximos dias')
                        break
                    if 'não' in voz:
                        break
            except requests.exceptions:
                engine_speak('Desculpe, mas não consegui me conectar a a internet')
        elif self.existe(['faça uma conta para mim', 'calculadora', 'calcular', 'faça uma conta']):
            calculadora()
        elif self.existe(['qr code', 'code', 'faça um qr code', 'faça um code']):
            criar_qrcode()
        elif self.existe(['faz uma análise', 'análise de dados', 'dados', 'análise de', 'fazer uma análise']):
            nome = pyautogui.prompt('Digite aqui o nome do arquivo', title='Nome do arquivo')
            tabela = pd.read_excel(rf"C:\\Users\\User\\Desktop\\{nome}.xlsx")

        else:
            # options apps
            if self.existe(opcoes):
                abrir_algo(self.voz_data.lower())
            elif self.existe(['fale as opções', 'opções de aplicativos', 'opções']):
                engine_speak('beleza, vou te falar as opções, por favor diga apenas o número da opção que você quer '
                             'depois de fechar a janela.')
                engine_speak('As opções são: ')
                aux = ''
                cont = 1
                for op in opcoes:
                    aux += f'{cont}° opção é: {op}\n'
                    cont += 1
                pyautogui.alert(aux, title='Opções')
                engine_speak('qual opção você quer?')
                while True:
                    vozn = self.pegar_comandos_separados()
                    vozn = self.ajeitar_numero(vozn)
                    if type(vozn) == int:
                        abrir_algo(opcoes[vozn])
            self.conversas()

    def ajeitar_numero(self, numero):
        nums = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
        for n in nums:
            if n in numero:
                return nums.index(n) + 1

    def escrever_em_txt_dados(self, lista_palavras):
        lista_frases = []
        contR = int(self.arquivoF[-2]) + 1
        with open(r"../databaseF.txt", 'a', encoding='utf-8') as F:
            lista_palavras = lista_palavras.replace(" ", "_")
            F.write('\n')
            F.write(f'{contR} ')
            F.write(f'{lista_palavras} ')
        engine_speak("Quais são as possíveis respostas para essa pergunta?")
        engine_speak("fale 'break'/'parar' para parar!!!")
        while True:
            # aux = pyautogui.prompt('Digite: ', title="Respostas(digite 'break' para parar)")
            aux = engine_reconition_online()
            if aux is None:
                aux = virtual_assistente.pegar_comandos_separados()
            if aux is not None:
                if 'break' == aux:
                    break
                if 'parar' == aux:
                    break
                lista_frases.append(aux)
        self.escrever_em_txt_resposta(lista_frases, contR)
        engine_speak("Pronto, frase salvo no banco de dados")

    def escrever_em_txt_resposta(self, lista_palavras, cont):
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
                return resposta[random.randint(0, len(resposta) - 1)].replace("_", " ")
            return resposta[0].replace("_", " ")
        except ValueError:
            return None

    def run(self):
        while True:
            try:
                virtual_assistente.voz_data = engine_reconition_online()
                if virtual_assistente.voz_data is None:
                    data = stream.read(8000)
                    if len(data) == 0:
                        break
                    if rec.AcceptWaveform(data):
                        resultado = rec.FinalResult()
                        resultado = json.loads(resultado)
                        if resultado is not None:
                            virtual_assistente.voz_data = resultado['text'].lower()
                            virtual_assistente.respostas()
                else:
                    virtual_assistente.respostas()
            except sr.WaitTimeoutError:
                engine_speak('Por favor, não fique muito tempo sem falar')
                continue


class tela(threading.Thread, tk.Label):
    def __init__(self, nome, master):
        threading.Thread.__init__(self)
        self.nome = nome
        self.master_tela = master
        self.texto_resposta = Label(self.master_tela, font=('Arial', 12), fg='Black', bg='white', height=1, width=20)
        self.texto_resposta.grid(column=0, row=1, padx=20, pady=20)
        self.texto_cpu = Label(self.master_tela, font=('Arial', 12), fg='black', bg='white', height=1, width=5)
        self.texto_cpu.grid(column=0, row=2, ipadx=1, pady=190)
        self.atualizar()
        self.atualizar_cpu()

    def atualizar(self):
        dataatual = datetime.now().strftime(f'%d/%m/%Y - %H:%M:%S Hrs')
        self.texto_resposta['text'] = dataatual
        # threading.Thread(target=self.atualizar).start()
        self.master_tela.after(1, self.atualizar)

    def atualizar_cpu(self):
        porcentagem = str(psutil.cpu_percent())
        self.texto_cpu['text'] = porcentagem
        # threading.Thread(target=self.atualizar_cpu).start()
        self.master_tela.after(1000, self.atualizar_cpu)


def comecar():
    engine_speak('Estou iniciando, espra um pouco aí...')
    for c in tqdm(range(10)):
        sleep(1)
        print('.', end='')
    engine_speak('preparando módulos...')
    for c in tqdm(range(10)):
        sleep(1)
        print('.', end='')
    engine_speak('finalizando...')
    for c in tqdm(range(10)):
        sleep(1)
        print('.', end='')
    engine_speak('Pronto, já vou aparecer...')


def criar_qrcode():
    engine_speak("Você deseja criar vários qr codes de vários links, ou apenas um?")
    try:
        while True:
            voz = engine_reconition_online()
            if voz is None:
                voz = virtual_assistente.pegar_comandos_separados()
            if voz is not None:
                break
        if 'apenas um' in voz or 'um' in voz or 'apenas' in voz:
            engine_speak('Beleza, digita para mim o link que você deseja usar para criar o QR code')
            link = pyautogui.prompt("Digite o link: ", title='Link')
            engine_speak('Agora digite para mim o nome do arquivo: ')
            nome = pyautogui.prompt("Nome do arquivo: ", title="Nome")
            engine_speak('Certo, espera um pouco aí...')
            meu_qrcode = qrcode.make(link)
            meu_qrcode.save(fr"C:\Users\User\Desktop\qrcode_{nome}.png")
            engine_speak("Pronto, já está na sua área de trabalho")
        else:
            engine_speak('Beleza, quantos você quer fazer?')
            while True:
                vozq = engine_reconition_online()
                if vozq is None:
                    vozq = virtual_assistente.pegar_comandos_separados()
                if vozq is not None:
                    break
            vozq = virtual_assistente.ajeitar_numero(vozq)
            links = {}
            for c in range(int(vozq)):
                nome = pyautogui.prompt("Nome: ", title="Nome do arquivo")
                link = pyautogui.prompt("Digite o link: ", title='Link')
                links[f'{nome}'] = str(link)
            for produto in links:
                meu_qrcode = qrcode.make(links[produto])
                meu_qrcode.save(f"qrcode_{produto}.png")
            engine_speak('Pronto, qr codes feitos')
    except sr.RequestError:
        engine_speak("Não foi possível conectar a internet")
    except BaseException:
        engine_speak('Desculpe, não pude realizar o processo, algo deu errado')


def calculadora():
    engine_speak('Beleza, o que você deseja calcular?')
    engine_speak('Por favor, falar apenas equações simples, afinal estou em fase de desenvolvimento')
    try:
        while True:
            voz = str(engine_reconition_online().lower())
            if voz is None:
                voz = virtual_assistente.pegar_comandos_separados().lower()
                break
            if voz is not None:
                break
        voz = voz.split()
        while True:
            indexAux = ''
            if str(voz).count("fatorial"):
                nums = separar(voz, (voz.index("fatorial")))
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
                nums = separar(voz, (voz.index(indexAux)))
                valor_total = math.pow(nums[0], nums[1])
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
                nums = separar(voz, voz.index(indexAux))
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
                nums = separar(voz, voz.index(indexAux))
                valor_total = (nums[0] / nums[1])
                voz.insert(int(voz.index(indexAux)), str(valor_total))
                voz.remove(indexAux)
                voz.remove(str(nums[0]))
                voz.remove(str(nums[1]))
                continue
            if str(voz).count('somado') != 0 or str(voz).count('+') != 0:
                if '+' in voz:
                    indexAux = '+'
                if 'somado' in voz:
                    indexAux = 'somado'
                nums = separar(voz, voz.index(indexAux))
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
                nums = separar(voz, voz.index(indexAux))
                valor_total = (nums[0] - nums[1])
                voz.insert(int(voz.index(indexAux)), str(valor_total))
                voz.remove(indexAux)
                if indexAux == 'subtraido':
                    voz.remove('de')
                voz.remove(str(nums[0]))
                voz.remove(str(nums[1]))
                continue
            if not str(voz).isalnum():
                engine_speak('Deseja ouvir o resultado ou colar em algum lugar?')
                while True:
                    vozsair = engine_reconition_online()
                    if vozsair is None:
                        vozsair = virtual_assistente.pegar_comandos_separados().lower()
                        break
                    if vozsair is not None:
                        vozsair = vozsair.lower()
                        break
                if 'colar' in vozsair:
                    virtual_assistente.aux = vozsair
                    break
                if 'ouvir' in vozsair:
                    engine_speak('O resultado é:' + str(voz).strip('[]').replace("'", ""))
                    break
            if not str(voz).isalpha():
                engine_speak('Deseja fazer mais alguma conta?')
                while True:
                    vozsair = engine_reconition_online()
                    if vozsair is None:
                        vozsair = virtual_assistente.pegar_comandos_separados().lower()
                        break
                    if vozsair is not None:
                        vozsair = vozsair.lower()
                        break
                if 'sim' in vozsair:
                    continue
                else:
                    break
    except:
        engine_speak("Desculpe, algo deu errado")
        engine_speak("Pode ter sido a conexão, ou algum valor inválido")


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


def engine_speak(text):
    """
    fala da assitente virtual
    """
    text = str(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()


def engine_reconition_online():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, 10, 10)  # define o microfone como fonte de áudio
        try:
            virtual_assistente.voz_data = r.recognize_google(audio, language='pt')
            return virtual_assistente.voz_data.lower()
        except sr.UnknownValueError:
            engine_speak('Por favor, fale novamente, eu não entendi o que você falou')
        except sr.RequestError:
            return None


def Boas_vindas():
    if 0 < datetime.now().hour > 12:
        engine_speak('Bom dia')
    elif 12 <= datetime.now().hour > 18:
        engine_speak('Boa tarde')
    else:
        engine_speak('Boa noite')
    engine_speak(f'Oi {virtual_assistente.pessoa}, como você está?')  # ['estou bem, obrigado', 'estou', 'sim
    # estou bem obrigado']
    voz = virtual_assistente.pegar_comandos_separados()
    if 'estou' in voz or 'obrigado' in voz or 'bem' in voz:
        engine_speak('que bom, então, vamos fazer alguma coisa?')
        voz = virtual_assistente.pegar_comandos_separados()
        if 'bora' in voz:
            engine_speak('Beleza, bora')
        elif 'beleza' in voz:
            engine_speak('Beleza, bora')
        elif 'claro' in voz:
            engine_speak('Beleza, bora')


def write(textow=''):
    pyperclip.copy(textow)
    pyautogui.hotkey('ctrl', 'v')


def notificar(text=''''''):
    notification.notify(title="R.O.X.X.A.N.E", message=text, timeout=20)


def horario():
    hora = datetime.now()
    engine_speak('Agora ' + hora.strftime('São %H horas e %M minutos'))


def datahj():
    data = date.today()
    semana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro')
    mesatual = (meses[data.month])
    ano = data.strftime(" de %Y")
    engine_speak("Hoje é " + semana[data.weekday()])
    engine_speak('Dia ' + str(data.day) + mesatual + ano)


def abrir_algo(name):
    pyautogui.PAUSE = 1.2
    pyautogui.press('win')
    pyautogui.write(name)
    pyautogui.press('backspace')
    pyautogui.press('enter')
    for l in pacoteOffice:
        if l == name:
            pyautogui.PAUSE = 1.8
            pyautogui.press('enter')
    virtual_assistente.run()


# inicializando
# comecar()

# Boas vindas
# Boas_vindas()

# instância das classes
virtual_assistente = ROXXANE('ROCSANE', "Jhonattan")

janela = Tk()
janela.title(f"Roxxane")
background_image = PhotoImage(file="../Nome.PNG")
background_label = Label(janela, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
janela.geometry('500x300')
janela_aparecer = tela('ROCSANE', janela)
virtual_assistente.start()
janela_aparecer.start()
janela.resizable(0, 0)
janela.mainloop()
