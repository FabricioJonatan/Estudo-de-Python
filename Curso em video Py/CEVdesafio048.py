soma = 0
valores = 0

for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
            valores += 1
        
print(f'A soma de todos os \033[33m{valores}\033[m valores solicitados de 1 a 500 deu \033[32m{soma}\033[m')