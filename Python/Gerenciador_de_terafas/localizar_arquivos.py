import os
from copy import deepcopy

procurar = ''
saida = []
user = os.getlogin()
dirs = os.listdir(os.path.join("C:", "\\", "Users", "\\"))
print(dirs)
dirs_aux = deepcopy(dirs)
sair = False

while sair:
    for path in dirs:
        if os.path.isdir(path):
            dirs_aux = os.path.join(dirs_aux, path)
            for arquivo in dirs_aux:
                if procurar in arquivo:
                    saida.append(dirs_aux)
