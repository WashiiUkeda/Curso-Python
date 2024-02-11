# refaça o ex 51 lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos usando o While.

num = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = num
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' ')
    cont += 1
    termo += razao
print('Fim')
