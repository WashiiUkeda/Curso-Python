# Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*args):
    maior = None
    for elemento in args:
        print(elemento, end= ' ')
        if maior is None or elemento > maior:
            maior = elemento
    print(f'\n{len(args)} valores informados')
    print(f'O maior valor é {maior}')


maior(1, 2, 3, 34523, 454, 222342)
