from random import randint
from time import sleep
from operator import itemgetter

valores = {'1° jogador': randint(1, 6), '2° jogador': randint(1, 6), '3° jogador': randint(1, 6),
           '4° jogador': randint(1, 6)}
rank = dict()
print('Os jogadores tiveram os seguintes resultados:')
for k, v in valores.items():
    print(f"O {k} teve o resultado {v}")
    sleep(1)
rank = sorted(valores.items(), key=itemgetter(1), reverse=True)# itemgetter ecolhe qual o dado que será usado como
# referencia na ordenação
print()
for i, v in enumerate(rank):
    print(f'O {(i+1)}° colocado é {v[0]}, com {v[1]} pontos')
print(f"O vencedor o foi o {rank[0]}")
