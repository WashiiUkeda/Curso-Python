# crie um programa q leia varios numeros inteiros. no final da execucao mostre a media entre todos os valores e qual foi o maior e menor.
# o programa deve perguntar se ele quer ou nao continuar a digitar valores

resp = 'S'
soma = cont = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números. e a média foi {:.2f}.'.format(cont, media))
print('Desses números, o maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
