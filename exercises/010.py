#Criar um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar.

cart = float(input('Informe o valor: '))
dol = 3.27
r = cart * dol

print('Com o valor de R$ {:.2f} você poderá obter U$ {:.2f}.'.format(cart, r))
