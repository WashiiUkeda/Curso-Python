# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno é de {a:.1f}m².')

larg = float(input('Largura: '))
comp = float(input('Comprimento: '))

area(larg, comp)
