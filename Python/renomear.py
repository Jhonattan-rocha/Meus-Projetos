import os


def aux():
    arquivosXML = []
    arquivos = os.listdir()
    for arquivo in arquivos:
        if '.xml' in arquivo:
            arquivosXML.append(arquivo)
    return arquivosXML


novo = 'settingsNovo.xml'
velho = 'settingsVelho.xml'
normal = 'settings.xml'

arquivosXML = aux()

newpath = os.path.realpath(arquivosXML[0])
oldpath = os.path.realpath(arquivosXML[1])

if arquivosXML[1] == normal:
    os.rename(newpath, novo)
    os.rename(oldpath, velho)
    arquivosXML = aux()
    newpath = os.path.realpath(arquivosXML[0])
    os.rename(newpath, normal)
if arquivosXML[0] == normal:
    os.rename(oldpath, novo)
    os.rename(newpath, velho)
    arquivosXML = aux()
    oldpath = os.path.realpath(arquivosXML[1])
    os.rename(oldpath, normal)
