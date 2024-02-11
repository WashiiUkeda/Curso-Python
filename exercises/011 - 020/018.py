#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Informe o valor do angulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno, cosseno e tangente do angulo de {}° são:\n'
      'Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, sen, cos, tan))
