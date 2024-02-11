# crie um programa q leia o peso de 5 pessoas e mostra qual foi o maior e o menor

maior = 0
menor = 0

for c in range (1, 6):
    peso = float(input('Informe o peso da {}ª pessoa em KG: '.format(c)))
    if  c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi {}kg e o menor peso foi {}kg.'.format(maior, menor))
