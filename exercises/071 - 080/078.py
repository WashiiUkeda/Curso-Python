# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = []
mai = 0
men = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

print(f'Os números digitados foram {valores}')
print(f'O maior valor digitado foi {mai} na(s) posição(ões) ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} na(s) posição(ões) ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
