#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

al1 = input('Insira o nome do Aluno: ')
al2 = input('Insira o nome do Aluno: ')
al3 = input('Insira o nome do Aluno: ')
al4 = input('Insira o nome do Aluno: ')
al5 = input('Insira o nome do Aluno: ')
aluno = [al1, al2, al3, al4]

if al5 != '':
    aluno.append(al5)
    random.shuffle(aluno)
    print('A ordem de apresentação será {}.'.format(aluno))
else:
    random.shuffle(aluno)
    print('A ordem de apresentação será {}.'.format(aluno))