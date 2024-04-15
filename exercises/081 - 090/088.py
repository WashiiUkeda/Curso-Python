# faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serao gerados
# e vai sortear 6 num entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

mega = list()
mega_temp = list()
tot = 1

print(30*'-')
print(f'{"MEGA SENA":^30}')
print(30*'-')
games = int(input('Quantos jogos deseja sortear? '))

while tot <= games:
    cont = 0
    while True:
        c = randint(1, 60)
        if c not in mega_temp:
            mega_temp.append(c)
            cont += 1
        if cont >= 6:
            break
    mega_temp.sort()
    mega.append(mega_temp[:])
    mega_temp.clear()
    tot += 1

print('-' * 2, 'Gerando os jogos, aguarde.', '-' * 2)
sleep(2)
for i, l in enumerate(mega):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-' * 10, 'Boa Sorte!', '-' * 10)
