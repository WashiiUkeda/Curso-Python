# crie um programa q leia 6 numeros inteiros e mostre a soma apenas dos numeros pares

soma = 0
for c in range(0, 6):
    num = int(input('Informe um número: '))
    if num % 2 == 0:
        soma += num
print(soma)