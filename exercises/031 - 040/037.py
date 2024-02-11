# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 binário, 2 octal, 3 hexadecimal

num = int(input("Infomre um número inteiro: "))

print("Escolha uma das bases para conversão:\n"
      '[1] Binário\n[2] Octal\n[3] Hexadecimal')
conv = int(input('Base: '))

if conv == 1:
    print('O número {} é igual a {} na base {}.'.format(num, bin(num), 'binária'))
elif conv == 2:
    print('O número {} é igual a {} na base {}.'.format(num, oct(num), 'octal'))
elif conv == 3:
    print('O número {} é igual a {} na base {}.'.format(num, hex(num), 'hexadecimal'))
else:
    print('Por favor, escolha uma opção válida!')
