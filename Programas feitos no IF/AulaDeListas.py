#  EXERCICIO DA AULA

letras = ['a', 'n', 'h', 'e', 'i']
vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(3):
    letra = input()
    letras.append(letra)

for letra in letras:
    if letra in vogais:
        print('{} é vogal'.format(letra))
    else:
        print('{} é consoantes'.format(letra))


#  CONTEUDO DA AULA

notas = [9, 3, 4, 5, 2, 10, 11]
notas[3] = 10
soma = 0

print(notas[0])

for c in range(len(notas)):
    nota = int(input())
    notas.append(nota)

for i in range(4):
    print('nota {} = {}'.format(i + 1, notas[i]))
    
for nota in notas:
    print(nota)

#   exemplo / teste
for nota in notas:
    soma += nota
quantidade = len(notas)   
media = soma / quantidade
print('media = {}'.format(media))

pares = []
impares = []

for nota in notas:
    if nota % 2 == 0:
        pares.append(nota)
    else:
        impares.append(nota)

print(40 in notas)

vogais = ['a', 'e', 'i', 'o', 'u']
letra = input()

if letra in vogais:
    print('vogais')
else:
    print('consoantes')