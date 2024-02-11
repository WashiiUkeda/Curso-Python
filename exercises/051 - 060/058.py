# melhorar o jogo do ex 28. Só que agora o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessarios para acertar

import random
import time
import emoji


grade = '-=-'*20
print('{}\nVou pensar em um número entre 0 e 10. Tente adivinhar rs...\n{}'.format(grade, grade))
time.sleep(1)
maq = random.randint(0, 10)
win = emoji.emojize(':fireworks: :trophy: :fireworks:')
tries = 0
acertou = False

while not acertou:
    entry = int(input('Em que número pensei: '))
    tries += 1
    if entry == maq:
        acertou = True
    else:
        if entry < maq:
            print('Tente um pouco mais alto.')
        if entry > maq:
            print('Tente um pouco mais baixo.')
        
if tries == 1:
    print('{} Uau, você acertou de primeira, parabéns! O número que escolhi foi {}. {}'.format(win, entry, win))
elif tries > 1 and tries <= 5:
    print('Parabéns! O número que escolhi foi {}. Você precisou de {} tentativas.'.format(entry, tries))
else:
    print('Tente melhorar! O número que escolhi foi {}. Você precisou de {} tentativas.'.format(entry, tries))