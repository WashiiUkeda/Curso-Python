

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Informe o nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} fez na temporada: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {c+1}a partida: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' *30)

print(jogador)
print('-' *30)

for k, v in jogador.items():
    print(f'{k}: {v}')
print('-' *30)

print(f'O jogador {jogador["nome"]} tem {len(jogador["gols"])} partidas na temporada.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} fez {v} gol(s).')
print(f'Na temporada fez um total de {jogador["total"]}')
