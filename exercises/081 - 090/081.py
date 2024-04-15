# crie um programa que leia varios números e coloque-os em uma lista, depois disso mostre:
# A) Quantos numeros foram digitados / B) lista em ordem decrescente / C) se o valor 5 foi digitado e está ou não na lista.


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

valores.sort(reverse=True)

print(f'Foram digitados {len(valores)} elementos os quais foram adicionados à lista a seguir {valores}.')

if 5 in valores:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')
