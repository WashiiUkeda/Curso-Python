# crie um tupla preenchida com os 20 primeiros colocados do campeonato brasileiro na ordem de colocação depois mostre:
# A) os 5 primeiros / B) o Z4 / C) lista com os times em ordem alfabética / D) em que posição está o time Cuiabá (chape ta na segundona rs)

tabela = ('Palmeiras', 'Gremio', 'Atletico-Mg', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Athletico-Pr', 'Internacional', 'Fortaleza',
         'Sao-Paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro', 'Vasco',
         'Bahia', 'Santos', 'Goias', 'Coritiba', 'America-Mg')

grade = '-=' *40

# for time in tabela:
#     print(time)
# print(grade)

print(f'Tabela: {(tabela)}\n{grade}')

print(f'Times do G5: {tabela[:5]}\n{grade}')

print(f'Times do Z4: {tabela[-4:]}\n{grade}')

print(f'Tabela em ordem alfabética: {sorted(tabela)}\n{grade}')

print(f'O flamengo está na {tabela.index("Flamengo")+1}a posição.')


# cont = 0

# while True:
#     print('[1] Times do G5\n[2] Times do Z4\n[3] Tabela em ordem alfabética\n[4] Em que posição está o time escolhido')
#     esc = int(input('O que gostaria de saber: '))
#     if esc == 1:
#         print('Times do G5:')
#         print(f'1° ----- {tabela[0]}')
#         print(f'2° ----- {tabela[1]}')
#         print(f'3° ----- {tabela[2]}')
#         print(f'4° ----- {tabela[3]}')
#         print(f'5° ----- {tabela[4]}')
#         resp = ' '
#         while resp not in 'SN':
#             resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
#         if resp == 'N':
#             break
#     if esc == 2:
#         print('Times do Z4:')
#         print(f'17° ----- {tabela[16]}')
#         print(f'18° ----- {tabela[17]}')
#         print(f'19° ----- {tabela[18]}')
#         print(f'20° ----- {tabela[19]}')
#         resp = ' '
#         while resp not in 'SN':
#             resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
#         if resp == 'N':
#             break
#     if esc == 3:
#         print(sorted(tabela))
#         resp = ' '
#         while resp not in 'SN':
#             resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
#         if resp == 'N':
#             break
#     if esc == 4:
#         time = ' '
#         while time not in tabela:
#             time = str(input('Informe o time: ')).capitalize().strip()
#         ind = tabela.index(time)+1
#         print(f'{ind}° ----- {time}')
#         resp = ' '
#         while resp not in 'SN':
#             resp = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
#         if resp == 'N':
#             break
#     else:
#         print('Opção inválida. Escolha novamente.')

# print('Fim')

