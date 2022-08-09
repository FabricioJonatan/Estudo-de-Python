from random import randint
from time import sleep

jogadores = {'jogador1' : 0, 'jogador2' : 0, 'jogador3' : 0, 'jogador4' : 0}

for jogador in jogadores:
    dado = randint(1, 6)
    jogadores[jogador] = dado

for key, valor in jogadores.items():
    sleep(0.7)
    print(f'{key} tirou {valor} no dado.')