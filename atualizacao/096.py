# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(larg, comp):
    a = larg
    b = comp
    area = a * b
    print(f'A área é de {area}m2.')

larg = int(input('Largura: '))
comp = int(input('Comprimento: '))

area(larg, comp)