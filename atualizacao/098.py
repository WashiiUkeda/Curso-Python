# Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo, e realize a contagem.
# seu programa tem que realizar três contagens através da função criada:
# A) de 1 até 10, de 1 em 1 / B) de 10 até 0 de 2 em 2 / C) uma contagem personalizada.

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} avançando de {passo} em {passo}.')
    # if fim > inicio:
    #     for c in range(inicio, fim+1, passo):
    #         print(f'{c}', end= ' ')
    #     print('Fim!')
    # else:
    #     for c in range(inicio, fim-1, -passo):
    #         print(f'{c}', end= ' ')
    #     print('Fim!')
    if fim > inicio:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end= ' ', flush=True)
            sleep(0.5)
            cont += passo
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end= ' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('Fim')
            
contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
