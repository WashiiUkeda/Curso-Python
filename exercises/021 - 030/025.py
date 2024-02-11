# Crie um programa que leia o nome de uma pessoa e diga se tem SILVA no nome

name = str(input('Informe seu nome completo: ')).strip().title()
silva = 'Silva' in name

if silva == True:
    print('O seu nome atende os requisitos.')
else:
    print('O seu nome não possui Silva, portanto não atende os requisitos.')
