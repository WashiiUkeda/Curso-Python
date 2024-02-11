# crie um programa q leia o primeiro termo e a razao de uma progressao aritimetica
# no final mostre os 10 primeiros termos dessa progressao


termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decterm = termo + (10 - 1) * razao 
for c in range (termo, decterm + razao, razao):
    print(c, end=' ')

