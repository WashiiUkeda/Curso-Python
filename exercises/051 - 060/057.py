# crie um programa q leia o sexo de uma pessoa mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até o valor correto

gender = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while gender not in 'MmFf':
    gender = str(input('Dados inválidos!\nPor favor, informe o seu sexo [M/F]: ')).strip().upper()[0]
if gender == 'M':
    gender = 'masculino'
if gender == 'F':
    gender = 'feminino'

print('O seu sexo é {}.'.format(gender))