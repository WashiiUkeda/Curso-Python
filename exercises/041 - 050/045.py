# crie um programa que faça o computador jogar jokenpo com você

from platform import win32_edition
from random import shuffle
import random
import time


print('JO KEN PO dos brabos')

jogada = ['pedra', 'papel', 'tesoura']
maq = random.randint(0, 2)
print('''Faça sua jogada:
[0] Pedra
[1] Papel
[2] Tesoura''')
player1 = int(input(' '))

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')

print('-=' * 12)
print('Máquina jogou {}'.format(jogada[maq]))
print('Player1 jogou {}'.format(jogada[player1]))
print('-=' * 12)

if maq == 0:
    if player1 == 0:
        print('Empate!')
    elif player1 == 1:
        print('Parabéns, você ganhou!')
    elif player1 == 2:
        print('Que pena, você perdeu! Mais sorte na próxima.')
    else:
        print('Jogada inválida!')
elif maq == 1:
    if player1 == 0:
        print('Que pena, você perdeu! Mais sorte na próxima.')
    elif player1 == 1:
        print('Empate!')
    elif player1 == 2:
        print('Parabéns, você ganhou!')
    else:
        print('Jogada inválida!')

elif maq == 2:
    if player1 == 0:
        print('Parabéns, você ganhou!')
    elif player1 == 1:
        print('Que pena, você perdeu! Mais sorte na próxima.')
    elif player1 == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
