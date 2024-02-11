# Programa que faz o computador pensar em um número inteiro entre 0 e 5
# e pede para o usuário tentar adivinhar o número escolhido pela máquina

import random
import time
import emoji

grade = '-=-'*20
print('{}\nVou pensar em um número entre 0 e 5. Tente adivinhar rs...\n{}'.format(grade, grade))
time.sleep(1)
print('Aguarde um instante, estou escolhendo o número.')
time.sleep(2)
maq = int(random.randint(0,5))
win = emoji.emojize(':fireworks: :trophy: :fireworks:')
lose = emoji.emojize(':cross_mark:')

entry = int(input('Pronto, já pensei em um número.\nEm que número pensei: '))

if entry < 0 or entry > 5:
    print('Número inválido! Por favor, insira um número entre 0 e 5.')
else:
    time.sleep(2)
    print('O número que escolhi foi {}.'.format(entry))
    if entry == maq:
        print('{} Parabéns!! Você ganhou!! {}'.format(win, win))
    else:
        print('{} Que pena! Mais sorte na próxima vez.{}'.format(lose, lose))
