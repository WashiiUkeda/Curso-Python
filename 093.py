# crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome e quantas partidas ele jogou
# depois vai ler a quant de gols feitos em cada partida. No final tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato
# os gols tem q ser guardados em uma lista dentro da chave gols no dicionario


dados = dict()
tot_gols = list()
cont = 0

dados['jogador'] = str(input('Insira o nome do jogador: ')).title()
dados['partidas'] = int(input(f'Quantas pardidas {dados["jogador"]} jogou: '))
if dados['partidas'] != 0:
    while cont < dados['partidas']:
        gols = int(input(f'Gols na {cont+1}a partida: '))
        tot_gols.append(gols)
        cont += 1
    dados['gols'] = tot_gols
dados['gols temporada'] = sum(tot_gols)
print(30*'-=')

print(dados)

print(30*'-=')

for k, v in dados.items():
    print(f'{k}: {v}')
print(30*'-=')

print(f'O {dados["jogador"]} jogou {dados["partidas"]} partidas.')
for i, v in enumerate(tot_gols):
    print(f'{i+1}a partida: {v} gols')
print(f'Gols na temporada: {dados["gols temporada"]}')
