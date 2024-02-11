# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte qual será o valor a ser sacado (inteiro) e o programa vai informar
# quantas cedulas de cada valor serão entregues. Considere q o caixa possua cedulas de 50, 20, 10 e 1.

valor = int(input('Informe o valor do saque: R$ '))
total = valor
ced = 50
contced = 0

while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} cédulas de R$ {ced:.2f}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break
print('fim')
