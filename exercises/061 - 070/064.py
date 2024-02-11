# crie um programa q leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
#  no final mostre quantos numeors foram digitados e qual foi a soma entre eles, desconsiderando o Flag (999)

num = int(input('Informe um número [999 para parar]: '))
count = soma = 0

while num != 999:
    count += 1
    soma += num
    num = int(input('Informe um número [999 para parar]: '))

if count < 1:
    print('Programa encerrado')
elif count == 1:
    print('Você digitou apenas um número. Não há soma. O seu valor é {}.'.format(soma))
else:
    print('Você digitou {} números. A soma entre eles é {}.'.format(count, soma))