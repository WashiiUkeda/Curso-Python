# crie um programa onde o usuário possa digitar varios valores numericos e cadastre-os em uma lista
# caso o número ja exista, ele nao será adicionado. No final serão exibitos todos os valores unicos digitados em ordem crescente.

valores = []

while True:
    num = int(input('Informe um número para adicionar na lista: '))
    if num in valores:
        print(f'Número duplicado! O número {num} já se encontra na lista e por isso não foi adicionado!')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    resp = str(input('Deseja inserir mais números: [S/N] ')).strip()[0]
    if resp in 'Nn':
        break

valores.sort()
print(f'Foram digitados os valores {valores}.')