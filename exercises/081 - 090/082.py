# crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso crie duas listas extras que vao conter apenas
# os valores pares e os impares respectivamentes. Ao final mostre o conteudo das 3 listas.

valores_par = []
valores_impar = []
valores_total = []

while True:
    num = int(input('Digite um valor: '))
    if num in valores_total:
        print('Valor duplicado! Não adicionado!')
    else:
        valores_total.append(num)
        if num % 2 == 0:
            valores_par.append(num)
        else:
            valores_impar.append(num)

    resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break

print(f'Os {len(valores_total)} elementos válidos digitados foram adicionados a lista principal {valores_total}.')
print(f'Lista de números pares {valores_par}')
print(f'Lista de números ímpares {valores_impar}')
