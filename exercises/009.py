#Criar um programa que leia um número inteiro e mostre sua tabuada

num = int(input('Informe um número: '))

for count in range(10):
    print('{} x {} = {}'.format(num, count+1, num*(count+1)))