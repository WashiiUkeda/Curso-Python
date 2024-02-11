# Ler um número e dizer se é par ou impar

num = int(input('Informe um numero: '))
div = num % 2

if div == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))