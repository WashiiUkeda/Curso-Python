# Programa que leia o comprimento de 3 retas e diga se podem ou não formar um triangulo e mostre o tipo de triangulo que será formado.
# equilatero todos os lados iguais / isosceles dois lados iguais / escaleno todos os lados diferentes

import time

grade = '-=-'*10
print('{}\nLeitor de Triangulos\n{}'.format(grade, grade))

r1 = int(input('Informe a primeira reta: '))
r2 = int(input('Informe a segunda reta: '))
r3 = int(input('Informe a terceira reta: '))

sum1 = r1 + r2
sum2 = r2 + r3
sum3 = r1 + r3

if r1 == r2 and r1 == r3:
    forma = 'equilátero'
elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
    forma = 'isósceles'
else:
    forma = 'escaleno'

print('Caululando o resultado, por favor aguarde...')
time.sleep(2)

if sum1 <= r3 or sum2 <= r1 or sum3 <= r2:
    print('Para as retas informadas {}, {} e {}, não é possível criar um triângulo.'.format(r1, r2, r3))
else:
    print('Para as retas informadas {}, {} e {}, é possível criar um triângulo {}.'.format(r1, r2, r3, forma))

