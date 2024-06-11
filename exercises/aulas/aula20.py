# Funções

# exemplo 1
def soma(a , b):
    s = a + b
    print(s)

# Programa principal
soma(4, 5)
soma(8, 9)
soma(b=2, a=1)


# exemplo 2 (empacotar)
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(2, 1, 7)
contador(3, 4, 5, 1)
contador(31, 134, 3242, 4)


#exemplo 3
def mensagem(msg):
    print(msg)

def linha():
    print('-' *10)

linha()
mensagem('TESTE')
linha()


# exemplo 4
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
