# Programa que leia uma frase e mostre:
# * Quantas vezes aparece a letra A;
# * Em que posição ela aparece a primeira vez
# * Em que posição ela aparece a ultima vez
import time

frase = str(input('Coloque sua frase aqui: ')).strip()
time.sleep(1)

entry = str(input('Da frase "{}", escolha uma letra para analisar: '.format(frase))).lower()
letterCount = frase.lower().count(entry)

print('waiting please...')

time.sleep(3)

if letterCount == 0:
    print('A letra escolhida "{}" não aparece nenhuma vez na frase. Por favor, tente novamente!\n'
          'Lembre-se o programa diferencia letras com acentuação.'.format(entry))
elif letterCount == 1:
    print('A letra escolhida "{}" aparece {} vez na frase. \n'
      'Aparece na posição {}.'.format(entry, letterCount, frase.find(entry)+1))
else:
    print('A letra escolhida "{}" aparece {} vezes na frase. \n'
    'Aparece pela primeira vez na posição {} e pela última vez na posição {}.'.format(entry, letterCount, frase.find(entry)+1, frase.rfind(entry)+1))
