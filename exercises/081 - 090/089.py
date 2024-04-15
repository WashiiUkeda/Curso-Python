# crie um programa q leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final mostre um boletim contendo a média de cada um e permita q o usuário possa mostrar as notas de cada aluno individualmente.

geral = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar: [S/N] '))
    if resp in 'Nn':
        break

print('-' * 50)
print(f'{"No.":<10}{"NOME":<10}{"MÉDIA":<8}')
print('-' * 50)
for i, a in enumerate(geral):
    print(f'{i:<10}{a[0]:<10}{a[2]:<8.1f}')
print('-' * 50)

while True:
    print('Digitar 999 encerra o programa')
    aluno = int(input('Deseja mostrar as notas de qual aluno da lista? '))
    print('-' * 50)
    if aluno == 999:
        break        
    if aluno <= len(geral)-1:
        print(f'As notas de {geral[aluno][0]} são {geral[aluno][1]}')
    print('-' * 50)
print('Fim do programa!')
