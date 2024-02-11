# Programa que leia o comprimento de 3 retas e diga se podem ou não
# formar um triangulo.

import time


grade = '-=-'*10
print('{}\nLeitor de Triangulos\n{}'.format(grade, grade))

r1 = int(input('Informe a primeira reta: '))
r2 = int(input('Informe a segunda reta: '))
r3 = int(input('Informe a terceira reta: '))

sum1 = r1 + r2
sum2 = r2 + r3
sum3 = r1 + r3

print('Caululando o resultado, por favor aguarde...')
time.sleep(2)

if sum1 <= r3 or sum2 <= r1 or sum3 <= r2:
    triang = 'não é possível'
else:
    triang = 'é possível'

print('Para as retas informadas {}, {} e {}, {} criar um triângulo.'.format(r1, r2, r3, triang))
