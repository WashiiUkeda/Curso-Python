# crie um programa q leia dois valores e mostre um menu na tela
# 1 somar, 2 multi, 3 maior, 4 novos numeros, 5 sair
# seu programa devera realizar a operação solicitada em cada caso

import time

print('O que deseja fazer a seguir:')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
op = 0

while op != 5:
    op = int(input('O que deseja fazer a seguir:\n'
    '[1] Somar / [2] Multiplicar / [3] Maior Número / [4] Inserir novos números / [5] Sair\n'))
    if op == 1:
        soma = n1 + n2
        print('A soma de {}+{} é {}.'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('O produto de {}x{} é {}.'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        else:
            print('O maior número é {}.'.format(n2))
    elif op == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Favor inserir uma opção válida.')
time.sleep(1)
print('Programa encerrado.')
