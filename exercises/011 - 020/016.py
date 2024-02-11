#Crie um programa que leia um número e mostre sua parte inteira.

'''import math
num = float(input('Informe um número decimal: '))
ptint = math.trunc(num)
print('A parte inteira do número {:.2f} é {}.'.format(num, ptint))'''

num = float(input('Informe um número decimal: '))
print('A parte inteira do número {:.2f} é {}.'.format(num, int(num)))