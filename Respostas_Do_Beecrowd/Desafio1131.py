grenais, vgre, vint, empate = 0, 0, 0, 0

while True:
    inter, gremio = map(int, input().split())
    grenais += 1

    if inter > gremio:
        vint += 1
    elif gremio > inter:
        vgre += 1
    else:
        empate += 1

    print('Novo grenal (1-sim 2-nao)')
    escolha = int(input())

    if escolha == 2:
        break

print('{} grenais'.format(grenais))
print('Inter:{}'.format(vint))
print('Gremio:{}'.format(vgre))
print('Empates:{}'.format(empate))

if vgre > vint:
    print('Gremio venceu mais')
elif vint > vgre:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
