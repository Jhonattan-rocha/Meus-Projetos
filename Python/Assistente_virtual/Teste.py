import os
import threading
import tkinter as tk
import json
import time
import pyautogui
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from plyer import notification
from tqdm import tqdm
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.say("Oi tudo bem")
# engine.runAndWait()
#
# engine = pyttsx3.init()
#
#
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# model = Model("model")
# rec = KaldiRecognizer(model, 16000)
#
# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
# stream.start_stream()
#
# while True:
#     data = stream.read(8000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         resultado = rec.Result()
#         resultado = json.loads(resultado)
#         if resultado is not None:
#             speak(resultado['text'])
#             print(resultado['text'])

# class asistente:
#     def __init__(self, assist_name, person):
#         self.person = person
#         self.assit_name = assist_name
#         self.voice_data = ''
#         self.engine = pyttsx3.init()
#         self.model = Model("model")
#         self.rec = KaldiRecognizer(self.model, 16000)
#         self.p = pyaudio.PyAudio()
#         self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
#         self.stream.start_stream()
#
#     def engine_speak(self, text):
#         """
#         fala da assitente virtual
#         """
#         text = str(text)
#         voices = self.engine.getProperty('voices')
#         self.engine.setProperty('voice', voices[0].id)
#         self.engine.say(text)
#         self.engine.runAndWait()
#
#     def engine_speaker(self):
#         while True:
#             data = self.stream.read(8000)
#             if len(data) == 0:
#                 return
#             if self.rec.AcceptWaveform(data):
#                 resultado = self.rec.Result()
#                 resultado = json.loads(resultado)
#                 if resultado is not None:
#                     texto = str(resultado['text'])
#                     self.voice_data = texto
#                     print(texto)
#
# virtual_asistente = asistente('Jarvez', "Jhonattan")
# virtual_asistente.engine_speak(virtual_asistente.engine_speaker())
# print(virtual_asistente.voice_data)
# pyautogui.PAUSE = 1
# distance = 200
# time.sleep(3)
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.5)  # move right
#     distance -= 5
#     pyautogui.drag(0, distance, duration=0.5)  # move down
#     pyautogui.drag(-distance, 0, duration=0.5)  # move left
#     distance -= 5
#     pyautogui.drag(0, -distance, duration=0.5)  # move up
# pyautogui.mouseUp(x=1000, y=200)
# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter'])
# pyautogui.confirm('Confirma?')
# nada = pyautogui.prompt('start cmd')
#
# print(nada)
#
# pyautogui.screenshot('teste.png')

# .strftime('%Y-%m-%dT%H:%M')
# .strftime('%d/%m/%Y %H:%M Hrs')
voz_data = 'aaaaaaaaaa'
index = 4
for c in range(len(voz_data) - index, 0, -1):
    if voz_data[c].isalpha():
        print(c)

