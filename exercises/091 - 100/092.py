# crie um programa que leia o nome, ano de nasc e carteira de trab e cadastre-os (com idade) em um dicionario se por acaso
# a ctps for diferente de zero, o dicionario receberá tbm o ano de contratacao e o salario.
# calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

cad = dict()

cad['Nome'] = str(input('Nome: ')).title()
nascimento = int(input('Ano de Nascimento: '))
if nascimento < 1920:
    print('Ano inválido! Por favor, digite novamente')
    nascimento = int(input('Ano de Nascimento: '))
cad['Idade'] = date.today().year - nascimento  
cad['CTPS'] = int(input('Número da CTPS: '))
if cad['CTPS'] < 0:
    print('Por favor digite um número válido!')
    cad['CTPS'] = int(input('Número da CTPS: '))
elif cad['CTPS'] > 0:
    cad['Ano de contratação'] = int(input('Ano que foi contratado: '))
    if 1920 < cad['Ano de contratação'] <= nascimento:
        print('Ano inválido! Por favor, digite novamente')
        cad['Ano de contratação'] = int(input('Ano que foi contratado: '))
    cad['Idade'] = date.today().year - nascimento   
    cad['Salário'] = float(input('Salário: R$ '))
    cad['Idade para aposentadoria'] = cad['Idade'] + ((cad['Ano de contratação'] + 35) - date.today().year)
    
print(30*'-=-')

for k, v in cad.items():
    print(f'{k}: {v}')
print(30*'-=-')
print()
