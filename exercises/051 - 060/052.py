# crie um programa q leia um numero inteiro e diga se ele é ou não numero primo.
# numero primo divisivel por 1 e por ele mesmo.

num = int(input('Informe um número: '))
cont = 0

for c in range (1, num+1):
    if num % c == 0:
        cont += 1
        print('\33[33m', end=' ')
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')

if cont == 2:
    primo = 'é um número primo'
else:
    primo = 'não é um número primo'

print('\n\033[mO número {} {}.'.format(num, primo))