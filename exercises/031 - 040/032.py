# Programa que leia um ano e indique se é bissexto ou nao

year = int(input('Informe o ano: '))
div4 = year % 4
div100 = year % 100
div400 = year % 400

if (div4 == 0 and div100 != 0) or (div400 == 0):
    bissext = 'é um ano bissexto'
else:
    bissext = 'não é um ano bissexto'

print('O ano de {} {}.'.format(year, bissext))