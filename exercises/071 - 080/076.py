# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# pc = ('Ryzen 5 3600', 999, 'X570 TUF Gaming', 1000, '2x D50 8GB 3200mhz', 470, '2x D41 TUF Gaming', 540,
#       'SSD S40G 512GB', 420, 'SSD X70 Blade', 1500, 'RTX3060 TUF Gaming', 5100, 'Core Reactor 650W', 640)

# cont = 0

# while cont < len(pc):
#     print(f'{pc[cont]:.<30}',end='')
#     cont += 1
#     print(f'R$ {pc[cont]:>9.2f}')
#     cont += 1

# for pos in range(0, len(pc)):
#     if pos % 2 == 0:
#         print(f'{pc[pos]:.<30}',end='')
#     else:
#         print(f'R$ {pc[pos]:>9.2f}')

tup = ('')

while True:
    prod = str(input('Nome do Produto: ')).strip().capitalize()
    valor = float(input('Valor: R$ '))
    tup = (*tup, prod)
    tup = (*tup, valor)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir mais dados: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

grade = '-' * 42

print(f'{grade}\n{"Listagem de Preços":^42}\n{grade}')

for pos in range(0, len(tup)):
    if pos % 2 == 0:
        print(f'{tup[pos]:.<30}',end='')
    else:
        print(f'R$ {tup[pos]:>8.2f}')
print(grade)
