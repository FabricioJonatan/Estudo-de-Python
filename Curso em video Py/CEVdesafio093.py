jogador = {}
gols = []
total = 0

jogador['nome'] = input('Nome do Jogador : ').capitalize().strip()
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for partida in range(jogos):
    gol = int(input(f'   Quantos gols na partida {jogos}? '))
    gols.append(gol)
    total += gol

jogador['gols'] = gols
jogador['total'] = total

print('=-' * 15)
print(jogador)
print('=-' * 15)
for key, valor in jogador.items():
    print(f'O campo {key} tem o valor {valor}')
print('=-' * 15)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')

for partida in range(jogos):
    print(f'   => Na partida {partida}, fez {jogador["gols"][partida]} gols.')
print('=-' * 15)
