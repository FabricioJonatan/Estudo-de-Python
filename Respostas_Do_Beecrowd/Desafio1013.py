a, b, c = map(input().split(' '))

maiorAB = (a + b + abs(a - b))/2
maior = (maiorAB + c + abs(maiorAB - c))/2
maior = int(maior)

print('{} eh o maior'.format(maior))