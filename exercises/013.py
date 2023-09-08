#Criar um algoritmo que leia o salário de um funcionário
#mostrar seu novo salário com aumento de 15%

sal = float(input('Informe seu salário: '))
newsal1 = sal*1.15
newsal2 = sal*1.10

if sal >= 1500:
    print('Seu salário de R$ {:.2f} terá aumento de 10%. '
    'Seu novo salário será de R$ {:.2f}.'.format(sal, newsal2))
else:
    print('Seu salário de R$ {:.2f} terá aumento de 15%. '
    'Seu novo salário será de R$ {:.2f}.'.format(sal, newsal1))
