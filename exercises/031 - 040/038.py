# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela: O primeiro valor é maior; O segundo valor é maior; Ambos os valores são iguais.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print('O número {} é maior que o número {}.'.format(num1, num2))
elif num1 < num2:
    print('O número {} é menor que o número {}.'.format(num1, num2))
else:
    print('Os números informados são iguais.')
