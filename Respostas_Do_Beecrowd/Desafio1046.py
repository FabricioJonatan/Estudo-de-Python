a, b = map(int, input().split())

if b > a:
    tempo = b - a
else:
    tempo = b + 24 - a

print('O JOGO DUROU {} HORA(S)'.format(tempo))