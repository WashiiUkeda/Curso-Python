# crie um programa q leia o ano de nascimento de 7 pessoas e no final mostre quantas pessoas ainda
# nao atingiram a maioridade e quantas ja sao maiores

from datetime import date

cont = 0
now = date.today().year
menor = 0
maior = 0

for c in range (1, 8):
    birth = int(input('Informe ano de nascimento da {}ª pessoa: '.format(c)))
    age = now - birth
    if age >= 18:
        maior += 1
    else:
        menor += 1

print('Temos um total de {} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade.'.format(maior, menor))
