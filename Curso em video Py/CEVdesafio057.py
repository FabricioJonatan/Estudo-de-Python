sexo = input('Informe seu Sexo [M/H] : ').strip().upper()[0]

while sexo not in 'HhMm':
    sexo = input('Dados invalidos, informe seu sexo [M/H] : ').strip().upper()[0]

if sexo == 'M':
    print('Você deve ser uma bela MULHER')
else:
    print('Você deve ser um belo HOMEM')