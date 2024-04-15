# crie um programa onde o usuario digite uma expressao matematica qualquer que use parenteses.
# seu app deverá analisar se a expressao passada está com os parenteses abertos e fechados na ordem correta.


exp = str(input('Informe sua expressão matemática: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
