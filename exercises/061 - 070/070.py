# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai continuar.
# No final mostre: A) qual o total gasto / B) quantos produtos custam mais de 1000 / C) qual o nome do protudo mais barato.

cont = soma = over = cheapestprice = 0
cheapestprod = ' '
grade = '-'*30

while True:
    prod = str(input('Nome do Produto: ')).strip().lower()
    price = float(input('Valor: R$ '))
    cont += 1
    soma += price
    if price > 1000:
        over += 1
    if cont == 1 or price < cheapestprice:
        cheapestprice = price
        cheapestprod = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja inserir mais dados: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print(f'Fim!\n{grade}')
        break
print(f'Você passou {cont} produtos.\n'
      f'O valor total da compra foi de R$ {soma:.2f}.\n'
      f'Acima de R$ 1.000,00 tivemos {over} produto(s).\n'
      f'O produto mais barato foi o(a) {cheapestprod}, custando R$ {cheapestprice:.2f}.')
