# Programa que pergunte o salário de um funcionário e calcule o valor do aumento
# Acima de R$1250,00 aumento de 10%
# Menor ou igual a R$1250,00 aumento de 15%

sal = float(input('Informe o salário: '))

if sal <= 1250:
    pct = 15
    aumento = pct / 100
    newSal = sal + sal * aumento
else:
    pct = 10
    aumento = pct / 100
    newSal = sal + sal * aumento

print('O salário de R$ {:.2f} receberá um aumento de {}%.\n'
      'O novo salário será de R$ {:.2f}.'.format(sal, pct, newSal))
