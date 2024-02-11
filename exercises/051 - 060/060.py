# crie um programa q leia um numero qualquer e mostre o seu fatorial. ex 5! = 5x4x3x2x1 = 120

# from math import factorial
# num = int(input('Informe um número: '))
# f = factorial(num)
# print('O fatorial de {} é {}.'.format(num, f))


# num = int(input('Digite um número para calcular seu fatorial: '))
# c = num
# f = 1
# print('Calculando {}!'.format(num))

# while c > 0:
#     print('{}'.format(c), end='')
#     if c > 1:
#         print(' x ', end='')
#     else:
#         print(' = ', end='')
#     f *= c
#     c -= 1

# print('{}.'.format(f))

num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print('Calculando {}!'.format(num))

for c in range(num, f, -1):
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1

print('{}.'.format(f))