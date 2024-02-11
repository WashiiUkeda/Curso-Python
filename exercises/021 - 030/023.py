# Programa que leia um número de 0 a 9999 e mostre cada um dos digito separados
# Ex: 1834
# unidade: 4 / dezena: 3 / centena: 8 / milhar: 1

num = int(input("Informe um número entre 0 e 9999: "))
n = str(num).strip().zfill(4)
tam = len(n)



if tam > 4:
    print('O número precisa estar entre 0 e 9999. Por favor, tente novamente!')
else:
    print('O número digitado {} tem como\n'
    'Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(num, n[0], n[1], n[2], n[3]))
