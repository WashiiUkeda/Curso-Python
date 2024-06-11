# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = list ()

def sorteio():
    cont = 1
    while True:
        num = randint(1, 100)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont > 5:
            break
    print(f'Os números adicionados a lista foram: {numeros}.')

def somaPar(valores):
    par = 0
    for c in valores:
        if c % 2 == 0:
            par += c
    print(f'A soma dos valores pares escolhidos sorteados é {par}')

sorteio()
somaPar(numeros)



