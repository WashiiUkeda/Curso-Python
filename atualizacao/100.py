# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

valores = list()

def sorteio(lista):
    for cont in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n}', end= ' ', flush=True)
        sleep(0.3)
    
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando valores pares de {lista}, temos {soma}.')

# def sorteio():
#     cont = 1
#     while cont < 6:
#         num = randint(0, 100)
#         valores.append(num)
#         cont += 1
#     print(valores)
    
# def somaPar(valores):
#     soma = 0
#     for c in valores:
#         if c % 2 == 0:
#             soma += c
#     print(f'A soma dos valores pares é {soma}.')

sorteio(valores)
somaPar(valores)
