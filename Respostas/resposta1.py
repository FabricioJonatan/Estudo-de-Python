idade = contador = 1
menores = maiores = 0
idades = []

while idade >= 0:
    idade = int(input(f'Digite a {contador}° idade [digite numero negativo para ver o resultado]: '))
    contador += 1

    if idade > 0:
        if idade < 21:
            menores += 1
        if idade > 50:
            maiores += 1
    idades.append(idade)

idades.pop()
print(f'\n\nIdades digitadas : {idades}')
print(f'Total de pessoas menores de 21 : {menores}')
print(f'Total de pessoas maiores de 50 : {maiores}')