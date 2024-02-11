# Programa que pergunte a distancia de uma viagem em KM.
# passagem até 200km valor R$0,50 por KM / acima de 200km valor R$0,45

entry = int(input('Informe a distancia, em KM, da sua viagem: '))

if entry <= 200:
    valor = 0.50
    ticket = entry * valor
else:
    valor = 0.45
    ticket = entry * valor

print('Para a distancia informada, sua passagem custará R$ {:.2f}'.format(ticket))
