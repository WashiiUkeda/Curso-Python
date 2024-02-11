# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas.

from random import randint
cont = 0

while True:
    player = int(input('Escolha um número de 0 a 10: '))
    maq = randint(0, 10)
    total = maq + player
    result = total % 2
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha entre par ou impar: ')).upper().strip()[0]
    print(f'O jogador escolheu {player} e a máquina {maq}. Total de {total}.')
    print('Deu Par.' if total % 2 == 0 else 'Deu Ímpar.')
    if tipo == 'P':
        if result == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if result == 1:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Jogar novamente...')     
print(f'Game over! Você venceu {cont} seguidas.')