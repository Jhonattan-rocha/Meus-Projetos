from django.db import models
from django.contrib.auth.models import User  # importa a tabela de usuários do Django padrão
from datetime import datetime, timedelta
from math import trunc


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)  # para instanciar um campo, utiliza-se o
    # models com o tipo do campo, max_lenght é o limite do campo
    descicao = models.TextField(blank=True, null=True)  # mesma coisa do outro só que esse tem parâmetro que
    # permite ser em branco ou nulo o campo
    data_evento = models.DateTimeField(verbose_name='Data do Evento')  # esse parâmetro troca o nome do campo que
    # aparece na aba admin
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de criação')  # insere automaticamente a
    # hora que foi criado um registro
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # esse parãmetro cascade diz para que se o usuário for

    # apagado, apague tudo dele

    class Meta:  # exige que o nome da tabela seja o que vc falou
        db_table = 'evento'

    def __str__(self):  # essa def diz que sempre chamarem esse objeto titulo, ele vai trazer o nome do titulo
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')  # para retornar hora, tem que ser nesse formato

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False

    def get_evento_adiantado(self):
        if not (self.data_evento < datetime.now()):
            return True
        else:
            return False


def Enumero(argumento=""):
        veredito = True
        for c in range(0, len(argumento)):
            if argumento[c] not in "0123456789":
                veredito = False
                break
        return veredito


def Einteiro(numero=float()):
    verifica = False
    numero = float(numero)
    compara = trunc(numero)
    if compara == numero:
        verifica = True
    else:
        verifica = False
    return verifica


def Validar(numero="", LimiteMaior=16, LimiteMenor=2, TesteEnumero=False):
    verifica = True
    if TesteEnumero:
        if not Enumero(numero):
            verifica = False
            return verifica
    numero = int(numero)
    if numero > LimiteMaior:
        verifica = False
        return verifica
    else:
        verifica = True
    if numero < LimiteMenor:
        verifica = False
        return verifica
    else:
        verifica = True
    return verifica


def QuantidadeDeNotas(v=int(0)):
    total = v
    ced = 50
    totalced = 0
    retorno = dict()
    while True:
        if total >= ced:
            total -= ced
            totalced += 1
        else:
            if totalced > 0:
                retorno[f'Quantidade de notas R${totalced}'] = ced
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totalced = 0
            if total == 0:
                break
    return retorno


def Ordenar(quantidadeNumeros=0, numeros=None):
    if numeros is None:
        numeros = []
    valores = []
    c = 0
    for num in numeros:
        if c == 0 or num > valores[-1]:
            valores.append(num)
        else:
            aux = 0
            while aux < len(valores):
                if num <= valores[aux]:
                    valores.insert(aux, num)
                    break
                aux += 1
        c += 1
    return valores


def Conversor(num=''.upper(), basenum=10, base=2):
    resto = 0
    div = 0
    div2 = 0
    resultado = 0
    convbase10 = 0
    conv = ""
    hexadecimal = ['A', 'B', 'C', 'D', 'E', 'F']
    num2 = 0
    indice = len(num) - 1

    # calculando o corespondente do número digitado para ser convertido, na base 10
    for c in range(0, len(num)):
        cont = 10
        if num[c] in 'ABCDEF':
            for l in range(0, 6):
                if num[c] == hexadecimal[l]:
                    num2 = cont
                cont += 1
        if num[c] not in 'ABCDEF':
            num2 = int(num[c])
        convbase10 += (num2 * (basenum ** indice))
        indice -= 1
    # covertendo o número para a base que foi solicitada
    div = convbase10
    div2 = convbase10
    while div > 0:
        resto = int(div2 % base)
        cont = 10
        for c in range(0, 6):
            if resto == cont:
                resto = str(hexadecimal[c])
            cont += 1
        div = div // base
        div2 = div
        conv = str(resto) + conv
    return conv


# Tradutor de Texto para binário e vice versa

def LetraNumero(text=''):
    arquivo = open('C:/Users/User/Documents/projeto_curso_2/core/Asciiz.txt',
                   'r',
                   encoding='utf-8')
    tabela = arquivo.read()
    tabela = tabela.split()
    retorno = ''
    for y in range(0, len(text)):
        if text[y] == ' ':
            retorno += ('00100000' + ' ')
            continue
        for x in range(0, len(tabela)):
            if text[y] == tabela[x]:
                retorno += (tabela[x - 1] + ' ')
    return retorno


def NumeroLetra(text=''''''):
    text = text.split()
    arquivo = open('C:/Users/User/Documents/projeto_curso_2/core/Asciiz.txt',
                   'r',
                   encoding='utf-8')
    tabela = arquivo.read()
    tabela = tabela.split()
    re = ''
    for c in range(0, len(text)):
        if len(text[c]) // 8 == 1:
            for l in range(0, len(tabela)):
                if tabela[l] == text[c]:
                    re += (tabela[l + 1])
        else:
            if len(text[c]) // 8 > 1:
                cont = 0
                for t2 in range(0, len(text[c]) // 8):
                    for t in range(0, len(tabela)):
                        if text[c][cont:cont + 8] == tabela[t]:
                            re += (tabela[t + 1])
                            cont += 8
            else:
                return '\nAlgum dado é inválido'
    return re


def Eletras(text=''):
    veredito = True
    for c in range(0, len(text)):
        if text[c] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáÁãÃâÂàÀéÉêÊíÍóÓõÕôÔúÚüÜçÇ ':
            veredito = False
            break
    return veredito


def Eletras_numeros(arg=''):
    veredito = False
    veredito2 = False
    retorno = True
    for c in range(0, len(arg)):
        if arg[c] in '0123456789':
            veredito2 = True
    for c in range(0, len(arg)):
        if arg[c] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáÁãÃâÂàÀéÉêÊíÍóÓõÕôÔúÚüÜçÇ ':
            veredito = True
    if veredito == True and veredito2 == True:
        return retorno
    else:
        retorno = False
        return retorno


def Validar_CPF(cpf=''):
    validar = []
    validar_digitos = 0
    resto = 0

    if len(cpf) > 14:
        return 'Você digitou algo errado, digite novamente!!!'
    else:
        for c2 in cpf:
            if not Enumero(c2):
                continue
            validar.append(c2)
        if len(validar) < 11:
            validar.clear()
            return 'Falta algo no cpf digitado, digite novamente!!!'
    comparar = validar[0:len(validar) - 2]
    for l in range(1, -1, -1):
        validar_digitos = 0
        cont = len(validar) - l
        for c3 in range(0, len(validar) - (l + 1)):
            validar_digitos += (int(validar[c3]) * cont)
            cont -= 1
        resto = (validar_digitos * 10) % 11
        if resto == 10:
            resto = 0
        comparar.append(str(resto))
    if validar == comparar:
        return True
    else:
        return False
