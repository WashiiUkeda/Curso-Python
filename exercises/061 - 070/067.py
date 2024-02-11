# Crie um programa que mostre a tabuada de varios números, um de cada vez.
# O programa será interrompido quando o número for negativo

while True:
    n = int(input('Informe um número para calcular sua tabuada: '))
    if n < 0:
        print('Não fazemos tabuada de números negativos.')
        break
    if n == 0:
        print('O número 0 multiplicado por qualquer outro número tem como resultado 0.')
        break
    for exp in range (1, 11):
        print(f'{n} x {exp} = {n*exp}')
        exp += 1

print('Fim do programa!')