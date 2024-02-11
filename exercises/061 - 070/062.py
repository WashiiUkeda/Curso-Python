# Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quando ele falar que quer mostrar 0 termos

num = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = num
cont = 1
newterm = 10
total = 0

while newterm != 0:
    total = total + newterm
    while cont <= total:
        print('{}'.format(termo), end=' ')
        cont += 1
        termo += razao
    print('Pausa')
    newterm = int(input('Deseja mostrar mais termos? Caso sim, digite a quantidade. Caso não digite 0: '))
print('Programa finalizado mostrando {} termos da progressão.'.format(total))

