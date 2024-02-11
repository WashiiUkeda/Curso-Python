# crie um programa que leia varios numeros inteiros. O programa só vai parar quando o usuario digitar 999.
# No final mostre quantos numeros foram digitados e qual foi a soma desconsiderando a flag.

cont = soma = 0

while True:
    n = int(input('Informe um número (999 para encerrar): '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Foram digitados {cont} números. A soma entre eles é {soma}.')
