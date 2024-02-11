# crie um programa q leia o nome, idade e sexo de 4 pessoas e no final mostre
# media de idade do grupo / qual o nome do homem mais velho / quantas mulheres tem menos de 20 anos

soma = 0
med = 0
maiorhomem = 0
nomevelho = ''
contfem = 0

for c in range (1, 5):
    print('------- {}ª pessoa --------'.format(c))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip()
    soma += age
    if c == 1 and gender in 'Mm':
        maiorhomem = age
        nomevelho = name
    if gender in 'Mm' and age > maiorhomem:
        maiorhomem = age
        nomevelho = name
    if gender in 'Ff' and age < 20:
        contfem += 1

med = soma / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(med))
print('O homem mais velho é o {} que possui {} anos.'.format(nomevelho, maiorhomem))
print('Ao todo temos {} mulheres.'.format(contfem))
