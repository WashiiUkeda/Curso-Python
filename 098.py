# Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo, e realize a contagem.
# seu programa tem que realizar três contagens através da função criada:
# A) de 1 até 10, de 1 em 1 / B) de 10 até 0 de 2 em 2 / C) uma contagem personalizada.

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} seguindo o passo de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(f'{c}', end= ' ')
        print('Fim!')
    else:
        for c in range(inicio, fim-1, -passo):
            print(f'{c}', end= ' ')
        print('Fim!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize a sua contagem.')
inicio = int(input('Informe o inicio: '))
fim = int(input('Informe o fim: '))
passo = int(input('Informe o passo: '))
contador(inicio, fim, passo)
