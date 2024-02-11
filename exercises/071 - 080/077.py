# Crie um programa que tenha uma tupla com várias palavras (nao usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

travel = ('haeundae', 'busan', 'hongdae', 'myeondong', 'chungmu-ro', 'coreia do sul')

for p in travel:
    print(f'\nA palavra {p.capitalize()} tem as vogais ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
