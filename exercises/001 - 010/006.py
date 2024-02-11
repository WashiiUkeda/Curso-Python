# Criar um programa que leia um número e mostre o dobro, triplo e raiz quadrada

n = float(input('Informe um número: '))
dob = n * 2
tri = n * 3
raiz = n ** (1/2)

print('Número digitado: {:.2f} \nSeu dobro é {:.2f} \nSeu triplo é {:.2f} \n'
    'Sua raiz quadrada é {:.2f}'.format(n, dob, tri, raiz))