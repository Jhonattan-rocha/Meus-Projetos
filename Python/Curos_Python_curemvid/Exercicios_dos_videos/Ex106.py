from time import sleep


def ajuda(msg):
    print('\33[31m' + ("--" * 20) + '\33[m')
    print(f"{'Sitema de ajuda dp Python':-^40}")
    print('\33[31m' + ("--" * 20) + '\33[m')
    print("Buscando dados")
    sleep(2)
    help(msg)
    print("PRONTO!!")


comando = ''
while True:
    comando = input("Digite um comando ou função que deseja buscar(ou fim para sair):").lower()
    if comando == 'fim':
        break
    ajuda(comando)
