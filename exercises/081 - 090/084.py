# faça um programa que leia um nome e peso de várias pessoas guardando tudo em uma lista. No final mostre:
# A) quantas pessoas foram cadastradas / B) uma listagem com as mais pesadas / C) Uma listagem com as mais leves

import time


users = []
data = []
mai = men = 0

while True:
    print(30*'-=-')
    data.append(str(input('Informe o nome: ')))
    data.append(float(input('Informe o peso (kg): ')))
    if len(users) == 0:
        mai = men = data[1]
    else:
        if data[1] > mai:
            mai = data[1]
        if data[1] < men:
            men =  data[1]
    users.append(data[:])
    data.clear()
    print(30*'-=-')
    resp = str(input('Deseja inserir mais usuários? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break

print('Aguarde um instante enquanto processamos os dados...')
time.sleep(2)

print(f'Foram cadastrados {len(users)} usuários.')
print(f'O maior peso foi {mai}kg, peso de ', end='')
for p in users:
    if p[1] == mai:
        print(f'{p[0]}', end='')

print()
print(f'O menor peso foi {men}kg, peso de ', end='')
for p in users:
    if p[1] == men:
        print(f'{p[0]}', end='')
