# Crie um programa que leia o nome de uma cidade e diga se começa ou não com SANTO

city = str(input('Informe o nome da cidade: ')).strip().title()
santo = city.find('Santo')

if santo != 0:
    print('Que pena! Sua cidade não começa com o nome Santo :(')
else:
    print('Que maravilha! Sua cidade esta apta para seguir adiante.')