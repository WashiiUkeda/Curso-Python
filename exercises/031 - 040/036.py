# Escreva um programa para aprovar emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, salário e quantos anos pretende pagar.
# calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário senão o emprestimo será negado.

house = float(input("Favor informar o valor do imóvel: "))
sal = float(input("Agora informe o sua renda bruta mensal: "))
years = int(input("Em quantos anos pretende pagar o imóvel: "))
month = years * 12
parc = house / month
pct = sal * 0.30

print("O valor do imóvel que deseja é R$ {:.2f}. \nPagando em {} anos terá a quantidade de {} parcelas com o valor de R$ {:.2f} por parcela."
.format(house, years, month, parc))

if parc <= pct:
    print("O valor da parcela está de acordo com a sua renda bruta mensal. \nParabéns!! O seu empréstimo foi aprovado.")
else:
    print("O valor da parcela excede 30% da sua renda bruta mensal. Infelizmente não podemos conceder o empréstimo!")
