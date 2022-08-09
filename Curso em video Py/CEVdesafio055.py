maior = 0
menor = 0

pessoas = int(input('Gostaria de analisar quantas pessoas? '))

for c in range(1, pessoas + 1):
    peso = float(input(f'Qual o peso da {c}° pessoa : '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior:.2f} KG')
print(f'O menor peso lido foi {menor:.2f} KG')