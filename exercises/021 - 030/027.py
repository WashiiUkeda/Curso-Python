# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza / Primeiro = Ana / Ultimo = Souza

name = str(input('Informe seu nome completo: ')).strip().title().split()

print('Seu primeiro nome é {} e seu último nome é {}.'.format(name[0], name[len(name)-1]))
