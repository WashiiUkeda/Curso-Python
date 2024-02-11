# Programa que leia 3 números e mostre qual o maior e o menor.

from email.errors import MultipartConversionError


grade = '-=-'*20
print('{}\nInforme 3 números abaixo!\n{}'.format(grade, grade))

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
n3 = int(input('Informe o terceiro numero: '))

#Define o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Define o maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 == n2 and n1 == n3:
    print('Os números digitados são iguais, não havendo menor ou maior.')
else:
    print('Os números digitados foram {}, {} e {}. \n'
        'O menor número é {} e o maior número é {}.'.format(n1, n2, n3, menor, maior))
    