#Criar um programa que leia o preço de um produto e mostre seu novo preço
#de 5% de desconto

price = float(input('Informe o valor do produto: '))
desc = (100-5)/100
newprice = price * desc

print('O novo valor após aplicado o desconto de 5% é de R$ {:.2f}.'.format(newprice))
