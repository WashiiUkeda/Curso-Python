#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
#na tela o nome do escolhido.

import random

al1 = input('Insira o nome do Aluno: ')
al2 = input('Insira o nome do Aluno: ')
al3 = input('Insira o nome do Aluno: ')
al4 = input('Insira o nome do Aluno: ')
al5 = input('Insira o nome do Aluno: ')
aluno = [al1, al2, al3, al4]
if al5 != '':
    aluno.append(al5)
    print(aluno)
    esc = random.choice(aluno)
    print('O aluno escolhido foi {}.'.format(esc))
else:
    print(aluno)
    esc = random.choice(aluno)
    print('O aluno escolhido foi {}.'.format(esc))
