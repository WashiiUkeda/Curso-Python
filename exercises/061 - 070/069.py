# Crie um programa q leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuario quer ou não continuar.
# No final mostre: A) quantas pessoas tem mais de 18 anos / B) quantos homens foram cadastrados / C) quantas mulheres tem menos de 20 anos.

cont = older = youngerwoman = man = 0

while True:
    age = int(input('Idade: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Sexo: [M/F] ')).strip().upper()[0]
    cont += 1
    if age >= 18:
        older += 1
    if gender == 'M':
        man += 1
    if age < 20 and gender == 'F':
        youngerwoman += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir mais dados: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Você inseriu {cont} pessoas. Dessas pessoas:\n'
      f'{older} pessoas tem mais de 18 anos;\n'
      f'{man} são homens;\n'
      f'{youngerwoman} mulher(es) com menos de 20 anos.')
