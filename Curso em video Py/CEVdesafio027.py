nome = input('Digite seu nome completo : ').strip().capitalize()
nome = nome.split(' ')

print('Muito prazer em te conhecer {} !!'.format(nome[0]))
print('Seu primeiro nome é : {}'.format(nome[0]))
print('Seu último nome é : {}'.format(nome[len(nome) - 1]))