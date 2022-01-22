import json
import random
import time
import webbrowser
from tkinter import *
from datetime import datetime, date
import pyaudio
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
from plyer import notification
from vosk import Model, KaldiRecognizer


class Virtual_assit:

    def __init__(self, assist_name, person):
        self.engine = pyttsx3.init()
        self.voice_data = ''
        self.person = person
        self.assit_name = assist_name
        self.text_janela_m = ''
        if requests.get("https://www.google.com"):
            self.r = sr.Recognizer()
        if not requests.get("https://www.google.com"):
            # inicializando o vosk como meio emergencial
            self.model = Model("../model")
            self.rec = KaldiRecognizer(self.model, 8000)
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=8000, input=True,
                                      frames_per_buffer=8000)
            self.stream.start_stream()

    def engine_speak(self, text):
        """
        fala da assitente virtual
        """
        text = str(text)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('voice', 'pt+f7')
        # rate = self.engine.getProperty('rate')
        # self.engine.setProperty('rate', rate - 50)
        self.engine.say(text)
        self.engine.runAndWait()

    # def engine_speak(self, audio):
    #     tts = gTTS(audio, lang='pt-br')
    #     num = random.randint(0, 2000)
    #     tts.save(f'audios/aud{num}.mp3')
    #     playsound(f'audios/aud{num}.mp3')

    def engine_speaker_audio_emergency(self):
        while True:
            data = self.stream.read(8000)
            if len(data) == 0:
                return
            if self.rec.AcceptWaveform(data):
                resultado = self.rec.Result()
                resultado = json.loads(resultado)
                if resultado is not None:
                    texto = str(resultado['text'])
                    self.text_janela_m = '>>', texto
                    self.voice_data = texto

    def record_audio(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source, 10, 10)  # pega dados de auido
            try:
                self.voice_data = self.r.recognize_google(audio, language='pt-br')  # converte audio para texto
            except sr.UnknownValueError:
                self.engine_speak(f"'Desculpe {self.person}, eu não entendi o que você falou, pode repetir?")
                self.voice_data = ''

            except sr.RequestError:
                self.engine_speak(
                    f'Desculpe {self.person}, não há conexão com a internet, irei usar outro reconhecedor')  # Erro
                # caso não tenha
                # internet
                self.engine_speaker_audio_emergency()

            self.voice_data = self.voice_data.lower()
            text_janela_m = ('>>', self.voice_data)
            return self.voice_data.lower()

    def there_exist(self, terms):
        """
        função para identificar se o termo existe
        """
        for term in terms:
            if term in self.voice_data:
                return True

    def respond(self, voice_data_r=''):
        if self.there_exist(['hey', 'hi', 'hello', 'oi', 'holla']):
            greetigns = [f'Oi {self.person}, o que você está fazendo hoje?',
                         f'Oi {self.person}, como eu posso te ajudar?',
                         f'Oi {self.person}, você precisa de algo?',
                         f'Oi {self.person}, como vai você?']

            greet = greetigns[random.randint(0, len(greetigns) - 1)]
            self.engine_speak(greet)
            self.voice_data = ''

        # google
        elif self.there_exist(['pesquise por']):
            search_term = voice_data_r.split("por")[-1]
            url = "http://google.com/search?q=" + str(search_term)
            webbrowser.get().open(url)
            self.voice_data = ''
            self.engine_speak("Aqui está o que você pediu sobre " + search_term + 'no google')

        # youtube
        elif self.there_exist(["pesquise no youtube por"]):
            search_term = voice_data_r.split("por")[-1]
            url = "http://www.youtube.com/results?search_query=" + str(search_term)
            webbrowser.get().open(url)
            self.voice_data = ''
            self.engine_speak("Aqui está o que você pediu sobre" + search_term + 'no youtube')

        # open something
        elif self.there_exist(["abrir "]):
            search_term = voice_data_r.split(" ")[-1]
            self.open_something(search_term)
            self.voice_data = ''
            self.engine_speak("O " + search_term + " está aberto, pronto.")

        # close tab of Chrome
        elif self.there_exist(["fechar aba"]):
            pyautogui.PAUSE = 1
            pyautogui.hotkey('ctrl', 'w')
            self.engine_speak("ready.")

        elif self.there_exist(['aperte ']):
            tecla = voice_data_r[-1]
            pyautogui.press(tecla)
        elif self.there_exist(['escreva ']):
            pyautogui.write(str(voice_data_r[1:]).strip('[]').replace("'", "").replace(',', ''))
        elif self.there_exist(['que horas são?']):
            horario()

    @staticmethod
    def open_something(name):
        pacoteOffice = ['word', 'excel', 'powerpoint', 'access']
        pyautogui.PAUSE = 1
        pyautogui.press('win')
        pyautogui.write(name)
        pyautogui.press('backspace')
        pyautogui.press('enter')
        for l in pacoteOffice:
            if l == name:
                pyautogui.PAUSE = 1.8
                pyautogui.press('enter')

    @staticmethod
    def startar():
        while True:
            voice_data = assistent.record_audio()
            assistent.respond(voice_data)
            time.sleep(0.5)
            despedidas = ['tchal', 'adeus', 'te vejo mais tarde', 'até', 'até logo']
            if assistent.there_exist(despedidas):
                assistent.engine_speak(f"Tenha um bom dia! até logo!")
                break


def write(textow=''):
    pyautogui.write(textow)


def notificar(text=''''''):
    notification.notify(title="R.O.X.X.A.N.E", message=text, timeout=10)


def horario():
    hora = datetime.now()
    assistent.engine_speak('Agora ' + hora.strftime('São %H horas e %M minutos'))


def datahj():
    data = date.today()
    semana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    meses = (
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
        'Novembro', 'Dezembro')
    mesatual = (meses[data.month])
    ano = data.strftime(" de %Y")
    assistent.engine_speak("Hoje é " + semana[data.weekday()])
    assistent.engine_speak('Dia ' + str(data.day) + mesatual + ano)


assistent = Virtual_assit('R.o.x.x.a.n.e', 'Jhonattan')


