# crie um programa que calcule o valor a ser pago, considerando o seu preço normal e condiçao de pagamento
# a vista dinheiro 10% / a vista cartao 5% / em até 2x preço normal / 3x ou mais 20% juros

price = float(input('Informe o valor do produto: R$ '))
print('[1] A vista Dinheiro/Pix\n[2] A vista cartão\n[3] Cartão parcelado')
pgt = int(input('informe a condição de pagamento: '))

if pgt == 1:
    desc = 10
    valfin = price - desc / 100 * price
    print('O valor do produto é R$ {:.2f}. Para esta forma de pagamento você terá {}% de desconto. O valor final será de R$ {:.2f}.'.format(price, desc, valfin))
elif pgt == 2:
    desc = 5
    valfin = price - desc / 100 * price
    print('O valor do produto é R$ {:.2f}. Para esta forma de pagamento você terá {}% de desconto. O valor final será de R$ {:.2f}.'.format(price, desc, valfin))
elif pgt == 3:
    parc = int(input('Informe a quantidade de parcelas: '))
    if parc == 2:
        print('O valor do produto é R$ {:.2f}. Para esta forma de pagamento você não terá desconto. O valor final será de R$ {:.2f}.'.format(price, price))
    elif parc > 2 and parc <= 10:
        juros = 20
        valfin = price + juros / 100 * price
        print('O valor do produto é R$ {:.2f}. Para esta forma de pagamento você terá {}% de juros. O valor final será de R$ {:.2f}.'.format(price, juros, valfin))
    else:
        print('Por favor escolha uma opção de parcelamento válida.')
