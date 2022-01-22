# primeira biblioteca, SpeechRecognition, pipwin, PyAudio, VOSK, model do vosk em português, pyttsx3
# import speech_recognition as sr
#
# # criar um reconhecedor
# r = sr.Recognizer()
#
# # abrir um microfone para capitura
# with sr.Microphone() as source:
#     while True:
#         audio = r.listen(source)  # define o microfone como fonte de áudio
#         print(r.recognize_google(audio, language='pt').lower())
import json
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import pyautogui


class Virtual_assitente:
    def __init__(self, assist_name, person):
        self.person = person
        self.assit_name = assist_name
        self.voice_data = ''
        self.engine = pyttsx3.init()
        self.model = Model("../model")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.stream.start_stream()

    # falar o que foi dito
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def there_exist(self, terms):
        """
        função para identificar se o termo existe
        """
        for term in terms:
            if term in self.voice_data:
                return True


def init__voz():
    asistente = Virtual_assitente('Roxana', "Jhonattan")
    # loop do reconhecimento de voz
    while True:
        data = asistente.stream.read(16000)
        if len(data) == 0:
            break
        if asistente.rec.AcceptWaveform(data):
            resultado = asistente.rec.Result()
            resultado = json.loads(resultado)

            if resultado is not None:
                texto = resultado['text']
                print(texto)
                asistente.speak(texto)


if __name__ == '__main__':
    init__voz()
