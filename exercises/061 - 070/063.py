# escreva um programa q leia um numero N inteiro e mostra na tela os N primeiros elementos de uma sequenca de fibonacci.
# ex 0 - 1 - 1 - 2 - 3 - 5 - 8

print('SEQUENCIA DE FIBONACCI')
termo = int(input('Quantos termos deseja mostrar: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3

while cont <= termo:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' -> Fim')