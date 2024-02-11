# Criar um programa que leia um número e informe seu antecessor e sucessor

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1

print('O número {} tem como antecessor {} e seu sucessor é {}.'.format(num, ant, suc))
