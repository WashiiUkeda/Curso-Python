# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 a 20.
# seu programa deverá ler um número pelo teclado (0 a 20) e mostrá-lo por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numeros[n]}')
        resp = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]
        if resp == 'N':
            break
    else:
        print('Número inválido, tente novamente.', end=' ')
print('Fim')
