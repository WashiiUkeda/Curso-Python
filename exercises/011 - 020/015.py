#Escreva um programa que pergunte a quantidade de Km percorridos por um carro
#alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dist = float(input('Informe a quilometragem percorrida: '))
dias = int(input('Informe a quantidade de dias do aluguel do carro: '))

total = dist * 0.15 + dias * 60

if dias < 1:
    print('Valor inválido.\nO número mínimo de dias é 1.')
elif dias == 1:
    print('O Carro foi alugado por {} dia e rodou {}km.'.format(dias, dist))
    print('O valor a ser pago é R$ {:.2f}.'.format(total))
else:
    print('O Carro foi alugado por {} dias e rodou {}km.'.format(dias, dist))
    print('O valor a ser pago é R$ {:.2f}.'.format(total))
