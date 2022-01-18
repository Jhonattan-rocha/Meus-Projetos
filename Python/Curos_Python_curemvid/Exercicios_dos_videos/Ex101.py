from datetime import datetime


def votacao(ano):
    if idade < 16:
        return "Voto negado"
    elif 16 <= idade < 18 or idade >= 65:
        return "Voto opcional"
    else:
        return "Voto obrigatório"


anoN = int(input("Digite seu ano de nascimento: "))
idade = (datetime.now().year - anoN)
print(f"A sua situação em relação a votação é, com {idade} anos de idade, é: {votacao(anoN)}")
