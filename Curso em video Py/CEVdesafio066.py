numero = soma = quantidade = 0

while True:
    numero = int(input(f'Digite o {quantidade + 1}° numero [Digite 999 para encerrar o programa] : '))
    if numero == 999:
        break

    soma += numero
    quantidade += 1

print(f'A soma dos {quantidade} valores foi {soma}!!')