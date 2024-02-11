# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor q estao na tupla.


from random import randint
cont =  0
tup = ('')

while cont < 5:
    choice = randint(0, 100)
    tup = (*tup, choice)
    cont += 1

print(tup)
print(f'O maior número da tupla é {max(tup)} e o menor número é {min(tup)}')