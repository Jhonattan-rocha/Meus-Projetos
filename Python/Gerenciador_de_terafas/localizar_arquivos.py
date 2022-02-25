import os
from copy import deepcopy

procurar = ''
saida = []
dirs = os.listdir(os.path.join("C:", "\\", "Users", "\\", f"{os.getlogin()}", '\\', "Downloads"))
dirs_aux = deepcopy(dirs)
sair = True

while sair:
    for path in dirs:
        if os.path.isdir(path):
            dirs_aux = os.path.join(dirs_aux, path)
            for arquivo in dirs_aux:
                if procurar in arquivo:
                    saida.append(dirs_aux)
