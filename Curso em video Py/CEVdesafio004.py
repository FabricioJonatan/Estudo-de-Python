a = input('Digite algo : ')

print('É alfabético? ', a.isalpha())
print('É numérico? ', a.isnumeric())
print('É alfanumérico? ', a.isalnum())
print('Está em minúsculo? ', a.islower())
print('Esta em maiusculo? ', a.isupper())
print('Só tem espaços? ', a.isspace())
print('Qual é o tipo da informação? ', type(a))