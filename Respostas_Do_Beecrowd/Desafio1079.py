cont = int(input())

for c in range(cont):
    nota1, nota2, nota3 = map(float, input().split())
    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
    print('{:.1f}'.format(media))