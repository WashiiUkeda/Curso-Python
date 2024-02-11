# # crie um programa que leia o ano de nascimento do atleta e mostre sua categoria.
# 9 anos mirim / até 14 infantil / até 19 junior / até 20 senior / acima master

from datetime import date

birth = int(input('Informe seu ano de nascimento: '))
hoje = date.today().year
age = hoje - birth

if age < 9:
    cat = 'mirim'
elif age >= 9 and age < 14:
    cat = 'infantil'
elif age >= 14 and age < 19:
    cat = 'junior'
elif age >= 19 and age <= 20:
    cat = 'senior'
else:
    cat = 'master'

print('A idade do atleta é {}. Para esta idade o atleta será incluído na categoria {}.'.format(age, cat))