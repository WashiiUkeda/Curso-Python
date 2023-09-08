# Crie um programa que leia a largura e altura de uma parede em metros
#e calcule a sua área e a quantidade de tinta necessária para pintar
#sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input('Informe a largura da parede em metros: '))
alt = float(input('Informe a altura da parede em metros: '))
area = larg * alt

tinta = area / 2

print('Você precisará de {:.2f} litros de tinta para pintar a parede.'.format(tinta))
