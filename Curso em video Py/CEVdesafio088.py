from random import randint
from time import sleep

print('~-~' * 10)
print(f'{"JOGO DA MEGA CENA":^27}')
print('~-~' * 10)

sorteios = int(input('Quantos jogos você deseja que eu sorteie?  '))
jogos = []

print(f'=-=-=-=-=-  SORTEANDO {sorteios} JOGOS  -=-=-=-=-=')

for sorteior in range(sorteios):
    jogo = []
    contador = 1

    while contador <= 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            contador += 1
    jogos.append(jogo)

for i in range(len(jogos)):
    jogos[i] = sorted(jogos[i])
    sleep(1)
    print(f'{i + 1}° Jogo = {jogos[i]}')

print('~=~' * 10)
print(f'{"BOA SORTE!":^27}')
print('~=~' * 10)