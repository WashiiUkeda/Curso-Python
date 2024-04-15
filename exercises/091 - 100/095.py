# Aprimore o desafio 93 para q ele funcione com vários jogadores, incluindo um sistema de 
# visualizacao de detalhes do aproveitamento de cada jogador

jogador = dict()
jogos = list()
dados = list()

while True:
    jogador.clear()
    jogos.clear()
    jogador['nome'] = str(input('Insira o nome do jogador: ')).title()
    partidas = int(input(f'Quantas pardidas {jogador["nome"]} jogou: '))
    for c in range(0, partidas):
        jogos.append(int(input(f'Gols na {c+1}a partida: ')))
    jogador['gols'] = jogos[:]
    jogador['gols temporada'] = sum(jogos)
    dados.append(jogador.copy())
    while True:
        resp = str(input('Deseja inserir mais jogador? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Inválido! Responda somente S ou N.')
    if resp == 'N':
        break
print(30*'-=')
print(dados)

# for k, v in jogador.items():
#     print(f'{k}: {v}')
# print(30*'-=')

# print(f'O {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
# for i, v in enumerate(jogos):
#     print(f'{i+1}a partida: {v} gols')
# print(f'Gols na temporada: {jogador["gols temporada"]}')


