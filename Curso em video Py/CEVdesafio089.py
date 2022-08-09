alunos = []
contador = 0

while True:
    print('--' * 20)
    nome = input('Nome : ').capitalize()
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2 : '))
    media = (nota1 + nota2) / 2
    aluno = [nome, media]
    notas = [nota1, nota2]
    aluno.append(notas)
    alunos.append(aluno)
    print('--' * 20)

    while True:
        resposta = input('Deseja continuar? [S/N] : ').strip().lower()
        if resposta in 'sn': break
        else: print('Resposta inválida!')
    if resposta == 'n': break

print('=~=' * 20)
print(f'{"No.":<5}{"NOME":^10}{"MÉDIA":>15}')

for aluno in range(len(alunos)):
    print(f'{aluno:<5}{alunos[aluno][0]:^10}{alunos[aluno][1]:.>15}')
print('=~=' * 20)

while True:
    posição = int(input('Deseja ver as notas do aluno de qual posição? [digite 999 para encerrar] '))
    if posição == 999:
        break
    else:
        print(f'As nostas do(a) {alunos[posição][0]} são {alunos[posição][2]}')
        print('=~=' * 20)

print('Tenha um bom dia!!')