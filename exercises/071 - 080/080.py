# Crie um programa onde o usuário possa digitar cinco valores e cadastre-os em uma lista, já na posição correta de inserção
# sem utilizar o sort. No final, mostre a lista ordenada na tela.

valores = []

for c in range(0,5):
    num = int(input('Informe um número: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break                
            pos += 1

print(f'O valores digitados em ordem foram {valores}.')
