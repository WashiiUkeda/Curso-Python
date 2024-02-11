# crie um programa que leia o peso e altura de uma pessoa e calcule o IMC.
# abaixo de 18,5 = abaixo do peso / entre 18,5 e 25 = peso ideal / 25 até 30 sobrepeso
# 30 até 40 obesidade / acima de 40 obesidade morbida


weight = float(input('Informe seu peso em KG: '))
heigh = float(input('infomre sua altura em metros: '))
imc = weight / pow(heigh, 2)

if imc < 18.5:
    result = 'abaixo do peso'
elif imc >= 18.5 and imc < 25:
    result = 'no peso ideal'
elif imc >= 25 and imc < 30:
    result = 'com sobrepeso'
elif imc >= 30 and imc < 40:
    result = 'com obesidade'
else:
    result = 'com obesidade morbida'

print('O seu peso é de {}kg e sua altura {}m. Seu IMC é {:.1f}. Você está {}.'.format(weight, heigh, imc, result))
