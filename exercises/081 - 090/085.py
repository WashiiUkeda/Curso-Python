# crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# no final mostre os valores pares e impares em ordem crescente

# valor = []
# temp_par = []
# temp_impar = []

# for n in range(1,8):
#     num = int(input(f'Digite o {n} número: '))
#     if num % 2 == 0:
#         temp_par.append(num)
#     else:
#         temp_impar.append(num)

# temp_par.sort()
# temp_impar.sort()
# valor.append(temp_par[:])
# valor.append(temp_impar[:])
# temp_par.clear()
# temp_impar.clear()

# print(valor)

num = [[], []]
valor = 0

for n in range (1, 8):
    valor = int(input(f'Digite o {n}o. número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')
