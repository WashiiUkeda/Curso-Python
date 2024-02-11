#Criar um programa que leia uma temperatura e converta ela para outras.

c = float(input('Informe a temperatura em °C: '))

fah = 1.8 * c + 32
kel = c + 273

print('Convertendo a temperatura de {:.1f}°C:\nFahrenheit: {:.1f}°F\nKelvin: {:.1f}K.'.format(c, fah, kel))
