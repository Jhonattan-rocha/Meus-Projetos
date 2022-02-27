import os
import platform
import psutil as ps
import re


class Gerenciador_De_tarefas:
    def __init__(self):
        self.OS = platform.system()
        self.__tela = ""
        self.__regex = re.compile(r"[WindowsLux]+")
        self.tabela_resumida = None

    def tarefas(self):
        if "windows" in str(self.__regex.findall(self.OS)[0]).lower():
            self.__tela = f'|{"Nome":<30}{"PID":<20}{"STATUS":<20}{"PRIORIDADE":<30}{"MEMÓRIA(em %)":<20}{"Usuário":<20}|\n'
            self.tamanho = len(self.__tela)
            self.__tela = f'{"-" * (self.tamanho - 1)}\n|{"Nome":<30}{"PID":<20}{"STATUS":<20}{"PRIORIDADE":<30}{"MEMÓRIA(em %)":<20}{"Usuário":<20}|\n{"-" * (self.tamanho - 1)}\n'
            for proc in ps.process_iter():
                infos = dict(proc.as_dict(attrs=['pid', 'name', 'status', 'username', 'nice', 'memory_percent']))
                if infos["username"] is None:
                    infos["username"] = "My computer"
                if infos['memory_percent'] is None:
                    infos["memory_percent"] = "0"
                if infos['nice'] is None:
                    infos["nice"] = "max"
                if self.tabela_resumida is not None:
                    if resumo[1].lower() == "nome":
                        if resumo[2] in infos['name']:
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "pid":
                        if resumo[2] in str(infos["pid"]):
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "status":
                        if resumo[2] in infos["status"]:
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "prioridade":
                        if resumo[2] in str(infos["nice"]):
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "username":
                        if resumo[2] in infos["username"]:
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                else:
                    self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
            self.__tela += f'{"-" * (self.tamanho - 1)}'
        if "linux" in str(self.__regex.findall(self.OS)[0]).lower():
            self.__tela = f'|{"Nome":<30}{"PID":<20}{"PPID":<20}{"STATUS":<20}{"PRIORIDADE":<30}{"MEMÓRIA(em %)":<20}{"Usuário":<20}|\n'
            self.tamanho = len(self.__tela)
            self.__tela = f'{"-" * (self.tamanho - 1)}\n|{"Nome":<30}{"PID":<20}{"PPID":<20}{"STATUS":<20}{"PRIORIDADE":<30}{"MEMÓRIA(em %)":<20}{"Usuário":<20}|\n{"-" * (self.tamanho - 1)}\n'
            for proc in ps.process_iter():
                infos = dict(proc.as_dict(attrs=['pid', "ppid", 'name', 'status', 'username', 'nice', 'memory_percent']))
                if infos["username"] is None:
                    infos["username"] = "My computer"
                if infos['memory_percent'] is None:
                    infos["memory_percent"] = "0"
                if infos['nice'] is None:
                    infos["nice"] = "max"
                if self.tabela_resumida is not None:
                    if resumo[1].lower() == "nome":
                        if resumo[2] in infos['name']:
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["ppid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "pid":
                        if resumo[2] in str(infos["pid"]):
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["ppid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "ppid":
                        if resumo[2] in str(infos["ppid"]):
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["ppid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "status":
                        if resumo[2] in infos["status"]:
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["ppid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "prioridade":
                        if resumo[2] in str(infos["nice"]):
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["ppid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                    elif resumo[1].lower() == "username":
                        if resumo[2] in infos["username"]:
                            self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["ppid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
                else:
                    self.__tela += f'|{infos["name"]:<30}{infos["pid"]:<20}{infos["ppid"]:<20}{infos["status"]:<20}{infos["nice"]:<30}{round(float(infos["memory_percent"]), 2):<20}{infos["username"]:<20}|\n'
            self.__tela += f'{"-" * (self.tamanho - 1)}'
        print(self.__tela)
        self.tabela_resumida = None

    def matar_processo(self, nome=" ", pid=0, ppid=0):
        pids = []

        def aux():
            if not nome.isspace():
                for proc in ps.process_iter():
                    infos = dict(proc.as_dict(attrs=["name", 'pid']))
                    if nome.lower() in infos['name']:
                        pids.append(infos['pid'])
                for piD in pids:
                    os.kill(piD, 9)
            elif pid != 0:
                os.kill(pid, 9)

        if "windows" in str(self.__regex.findall(self.OS)[0]).lower():
            aux()
            os.system("cls")
            self.tarefas()
        if "linux" in str(self.__regex.findall(self.OS)[0]).lower():
            aux()
            if ppid != 0:
                os.kill(ppid, 9)
            os.system("clear")
            self.tarefas()

    def alterar(self, altera='', pid=0, ppid=0):
        alterar = pid if pid != 0 else ppid
        if altera == "sempre":
            ps.Process(alterar).nice(ps.REALTIME_PRIORITY_CLASS)
        elif altera == "alta":
            ps.Process(alterar).nice(ps.HIGH_PRIORITY_CLASS)
        elif altera == "acima":
            ps.Process(alterar).nice(ps.ABOVE_NORMAL_PRIORITY_CLASS)
        elif altera == "normal":
            ps.Process(alterar).nice(ps.NORMAL_PRIORITY_CLASS)
        elif altera == "baixa":
            ps.Process(alterar).nice(ps.BELOW_NORMAL_PRIORITY_CLASS)
        elif altera == "ocioso":
            ps.Process(alterar).nice(ps.IDLE_PRIORITY_CLASS)


def matar():
    for m in ["matar", "processo", "parar", "acabar"]:
        yield m


def alterar():
    for a in ["alterar", "mudar", "substituir", "prioridade"]:
        yield a


OS = platform.system()
Gdt = Gerenciador_De_tarefas()
Gdt.tarefas()
regex_acao = re.compile(r"[matrpocesbidn]+")
regex_retorno = re.compile(r"[matrpocesbidn\s]+\s(\w+)")
resumo = []

sair = True

while sair:
    acao = input("Digite o que você quer fazer: ")
    if "resumo" in acao.lower():
        Gdt.tabela_resumida = " "
        resumo = list(acao.split(" "))
        Gdt.tarefas()
        continue
    if "reload" in acao:
        Gdt.tarefas()
        continue
    if "exit" in acao:
        sair = False
        continue
    if acao != "" and "matar processo" in acao or "acabar" in acao or "parar" in acao:
        vetor_acao = regex_acao.findall(acao)
        for p in range(len(vetor_acao)):
            if p > 2:
                vetor_acao.pop()
        vetor_retorno = regex_retorno.findall(acao)[0]
        for palavra in vetor_acao:
            for _palavra in matar():
                if palavra == _palavra:
                    if vetor_acao[-1] == 'pid' and str(vetor_retorno).isnumeric():
                        Gdt.matar_processo(pid=int(vetor_retorno))
                    if vetor_acao[-1] == 'ppid' and str(vetor_retorno).isnumeric():
                        Gdt.matar_processo(ppid=int(vetor_retorno))
                    if vetor_acao[-1] == 'nome':
                        Gdt.matar_processo(nome=vetor_retorno)
                    acao = ""
        continue
    if acao != "" and "alterar processo" in acao:
        regex_altera = re.compile(r"[alterpiodmusbxcn]+")
        regex_id = re.compile(r"[pid]+\s([0-9]+)")
        vetor_altera = regex_altera.findall(acao)
        pid = regex_id.findall(acao)
        for palavra in vetor_altera:
            for _palavra in alterar():
                if palavra == _palavra:
                    if vetor_altera[-1] == 'pid':
                        Gdt.alterar(vetor_altera[-2], pid=int(pid[0]))
                    if vetor_altera[-1] == 'ppid':
                        Gdt.alterar(vetor_altera[-2], ppid=int(pid[0]))
                    acao = ""
