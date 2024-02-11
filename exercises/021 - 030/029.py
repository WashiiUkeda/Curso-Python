# Escreva um programa que leia a velocidade de um carro.
# Se ultrapassar 80km/h, mostre que ele foi multado.
# Valor da multa R$7,00 por cada KM acima do limite.

import random


radar = random.randint(1,100)
multa = 7
limit = 80
exceed = radar - limit

print('Velocidade do carro: {}km/h'.format(radar))

if radar > limit:
    payment = multa * exceed
    print('O carro passou {}km/h acima do permitido na via. Será cobrado R$ 7,00 para cada km/h excedido.\n'
         'O valor da multa aplicada é de R$ {:.2f}.'.format(exceed , payment))
else:
    print('Velocidade dentro do permitido na via.')