# Faça um programa que leia o ano de nascimento e informe: se vai se alistar, se é hora de se alistar, se ja passou do tempo de alistamento.
# Mostrar tbm o tempo que falta ou que passou do prazo.

from datetime import date

birth = int(input('Informe seu ano de nascimento: '))
hoje = date.today().year
age = hoje - birth
alist = 17

if age < 17:
    tempo = alist - age
    print('Você está perto de completar {} anos. Ainda falta(m) {} ano(s) para você se alistar.'.format(age, tempo))
elif age >= 17 and age <= 18:
    print('Você está perto de completar {} anos. Está na hora de se alistar.'.format(age))
else:
    tempo = (alist - age) * -1
    print('Você está perto de completar {} anos. O período de alistamento passou em {} ano(s).'.format(age, tempo))
