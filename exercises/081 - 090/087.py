# Aprimore o desafio anterior (86) mostrando no final: A) a soma de todos os valores pares
# B) a soma dos valores da terceira coluna / C) o maior valor da segunda linha


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = mai = tc = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end ='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f'A soma dos valores pares da matriz é {soma_par}')

for l in range(0, 3):
    tc += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {tc}')

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
    	mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
