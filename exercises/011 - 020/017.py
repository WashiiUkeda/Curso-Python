#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retangulo e mostre o comprimento da hipotenusa

import math

catopo = int(input('Informe o cateto oposto: '))
catadj = int(input('Informe o cateto adjacente: '))
hipot = math.hypot(catopo, catadj)

print('Valor da hipotenusa é {}'.format(hipot))
