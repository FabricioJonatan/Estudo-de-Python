frase = input('Digite um frase qualquer : ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print(f'Você digitou a frase {junto}')

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('\033[35mTemos um palidromo\033[m ')
else:
    print('\033[34mNão temos um palidromo\033[m ')