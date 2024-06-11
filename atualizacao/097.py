# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uam mensagem com tamanho adaptavel.
# ex: escreva('olá mundo')
# saída: ~~~~~~~~~~~Olá Mundo~~~~~~~~~~~

def mensagem(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

mensagem('shinigami')
mensagem('só come')
mensagem('maçã')
