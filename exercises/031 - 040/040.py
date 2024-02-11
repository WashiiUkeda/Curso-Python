# Crie um programa que leia duas notas e calculoe a média mostrando: <5 Reprovado; entre 5 e <7 Recuperação; média >= 7 Aprovado.

av1 = float(input('Informe a nota da Av1: '))
av2 = float(input('Infomre a nota da Av2: '))
med = (av1 + av2) / 2

if med < 5:
    print('A média do aluno foi de {:.1f}. Está reprovado!'.format(med))
elif med >= 5 and med < 7:
    print('A média do aluno foi {:.1f}. Está em recuperação!'.format(med))
else:
    print('A média do aluno foi {:.1f}. Está aprovado!'.format(med))

