from time import sleep

#                   FUNÇÕES DAS OPÇÕES

def cadastrar():
    print('~~~~~~~~~~~~~~~~~~~~CADASTRANDO. . .')
    contador = 1

    while True:
        print(f'\n=====Aluno numero {contador}=====')

        nome = input('Digite o nome do aluno : ').capitalize()
        nota1 = float(input('Digite a primeira nota deste aluno : '))
        nota2 = float(input('Digite a segunda nota deste aluno : '))
        contador += 1
        media = (nota1 + nota2) / 2
        nota1 = str(nota1)
        nota2 = str(nota2)
        media = str(media)

        aluno = {
            'nome' : nome,
            'nota1' : nota1,
            'nota2' : nota2,
            'média' : media
        }
        alunos.append(aluno)
        
        with open('TesteBrabo.txt', 'a') as arquivo:
            for key in aluno.keys():
                arquivo.write(aluno[key])
                arquivo.write(',')
            arquivo.write('\n')

        while True:
            continuar = input('\nDeseja continuar? [S/N] ').strip().lower()
            if continuar == 'n':
                break
            elif continuar == 's':
                break
            else:
                print('Opção inválida, digite novamente. . .')
        if continuar == 'n':
            break

def listar():
    print('~~~~~~~~~~~~~~~~~~~~Listando . . .\n')
    sleep(0.5)
    contador = 1

    if len(alunos) <= 0:
        print('Lista Vazia, adicione coisas a ela em "CADASTRAR".\n')
        sleep(1)
    else:
        print(f'{"Alunos":<10}{"Nota 1":^7}{"Nota 2":^10}{"média":>11}')

        for indice in range(len(alunos)):
            sleep(0.5)
            print(f'{alunos[indice]["nome"]:.<10}{alunos[indice]["nota1"]:.^7}{alunos[indice]["nota2"]:.^10}{alunos[indice]["média"]:>11}')
            contador += 1
    print('')

def apagar():
    print('~~~~~~~~~~~~~~~~~~~~Apagando . . .\n')

    while len(alunos) > 0:
        del alunos[0]
    
    with open('TesteBrabo.txt', 'w') as arquivo:
        arquivo.write('')
    sleep(1.5)
    print('Dados apagados!')
    sleep(1)

def sair():
    print('Programa encerrado, tenha um bom dia!!')

#               VÁRIAVEIS, LEITURA E LISTAS!!!

alunos = []

with open('TesteBrabo.txt', 'r') as arquivo:
    arquivo = arquivo.readlines()
    for c in range(len(arquivo)):
        arquivo[c] = arquivo[c].split(',')
        arquivo[c].pop()
        aluno = {
            'nome' : arquivo[c][0],
            'nota1' : arquivo[c][1],
            'nota2' : arquivo[c][2],
            'média' : arquivo[c][3] 
        }
        alunos.append(aluno)

#                PROGRAMA PRINCIPAL!!!

while True:
    print('==' * 5, 'AGENDA DE NOTAS', '==' * 5)
    print('''
    [ 1 ]  CADASTRAR
    [ 2 ]  LISTAR
    [ 3 ]  APAGAR DADOS
    [ 4 ]  SAIR
    ''')

    resposta = int(input('Sua resposta : '))

    if resposta == 1:
        cadastrar()

    elif resposta == 2:
        listar()

    elif resposta == 3:
        apagar()

    elif resposta == 4:
        sair()
        break

    else:
        print('Resposta invalida')
        