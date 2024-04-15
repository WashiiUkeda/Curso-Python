# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
turma = list()

while True:    
    aluno['Aluno(a)'] = str(input('Nome do aluno: '))
    aluno['Media'] = float(input('Média: '))
    if aluno['Media'] >= 7:
        aluno['Situação'] = 'Aprovado'
    elif 5 <= aluno['Media'] < 7:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
    turma.append(aluno.copy())
    print(30*'-=-')
    resp = str(input('Deseja inserir mais usuários? [S/N] '))
    if resp in 'Nn':
        break

print(turma)
print(30*'-=-')

for t in turma:
    for k, v in t.items():
        print(f'{k}: {v}')
    print(30*'-=-')
    print()
