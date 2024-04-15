# Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloquei esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from operator import itemgetter
from random import randint
import time

players = {'Player1': randint(1, 6),
           'Player2': randint(1, 6),
           'Player3': randint(1, 6),
           'Player4': randint(1, 6)}
ranking = list()

for k, v in players.items():
    time.sleep(1)
    print(f'O {k} tirou {v}')
print(30*'-=-')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    time.sleep(1)
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}.')
