# Funções parte 2

# Interactive help
help() #função de ajuda interativa / quit sai do console de help
print(input.__doc__)


# Docstrings
# string de documentação - usa aspas tripas para poder criar um resumo de um mini help para a função
def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end= ' ')
        c += p
    print('Fim')

contador(0, 10, 2)


# argumentos opcionais
def somar(x, b=0, c=0):
    s = x + b + c
    print(f'A soma é igual a {s}')
somar(3, 2, 5)
somar(4, 8)
somar()


# escopo de variaveis / escopo de declarações
def teste(b):
    global a
    a = 8
    b = a + b
    c = 2
    print(f'Valores de teste: {a}, {b} e {c}')
#principal
a = 5
print(f'O valor de A é {a}.')


# retorno de resultados
def somar(y=0, b=0, c=0):
    s = y + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(4, 8)
r3 = somar()

print(f'Os valores das somas são {r1}, {r2} e {r3}')
