# Crie um programa q leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9 / B) Em que posição foi digitado o valor 3 / C) Quais foram os números pares.

cont = par = 0
tup = ('')

for c in range(1, 5):
    num = int(input(f'Favor digite o {c}° valor: '))
    tup = (*tup, num)
    cont +=1
    if num % 2 == 0 and num != 0:
        par += 1

print(f'Os valores digitados foram {tup}')

if 9 in tup:
    if tup.count(9) == 1:
        print(f'O número 9 foi digitado uma vez apenas.')
    elif tup.count(9) > 1:
        print(f'O número 9 apareceu {tup.count(9)} vezes.')
else:
    print(f'O número 9 não foi digitado.')

if 3 in tup:
    if tup.count(3) == 1:
        print(f'O número 3 foi digitado uma vez apenas e aparece a primeira vez na {tup.index(3)+1}ª posição')
    elif tup.count(3) > 1:
        print(f'O número 3 foi digitado {tup.count(3)} vezes e aparece a primeira vez na {tup.index(3)+1}ª posição.')
else:
    print(f'O número 3 não foi digitado.')   

if par == 1:
    print(f'Foi digitado apenas um valor par, sendo ele o número ', end='')
    for n in tup:
        if n % 2 == 0 and n != 0:
            print(n)
elif par >= 1:
    print(f'Foram digitados {par} números pares, sendo eles: ', end='')
    for n in tup:
        if n % 2 == 0 and n != 0:
            print(n, end=' ')
else:
    print('Não foi digitado nenhum número par.')