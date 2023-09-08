#Criar um programa que leia um valor em metros e converta para cm e mm.

valor = float(input('Informe o valor da medida em metros: '))

dm = valor * 10
cm = valor * 100
mm = valor * 1000
dc = valor / 10
hc = valor / 100
km = valor / 1000

print('Tabela de conversão da medida informada {:.2f} metros:'.format(valor))
print('Decímetro: {:.1f} \nCentímetro: {:.0f}\nMilímetro: {:.0f}\n'
    'Decâmetro: {:.1f}\nHectômetro: {:.2f}\nQuilômetro: {:.3f}'.format(dm,cm,mm,dc,hc,km))
