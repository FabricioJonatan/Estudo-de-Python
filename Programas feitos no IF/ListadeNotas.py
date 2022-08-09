from time import sleep

#                   FUNÇÕES DAS OPÇÕES

alunos = []

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

        aluno = [nome, nota1, nota2, media]
        
        with open('TesteBrabo.txt', 'a') as arquivo:
            for elemento in range(len(aluno)):
                arquivo.write(aluno[elemento])
                arquivo.write('-')
            arquivo.write('\n-')

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
    
    print(f'{"Alunos":<10}{"Nota 1":>5}{"Nota 2":>9}{"média":>11}')
    with open('TesteBrabo.txt', 'r') as arquivo:
        arquivo = arquivo.read()
        arquivo.split('-')
        alunos.append(arquivo)
    print(alunos)

#def apagar():
#    print('~~~~~~~~~~~~~~~~~~~~Apagando . . .\n')
#
#    while len(alunos) > 0:
#        del alunos[0]
#    
#    sleep(1.5)
#    print('Dados apagados!')
#    sleep(1)

def sair():
    print('Programa encerrado, tenha um bom dia!!')

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

#    elif resposta == 3:
#        apagar()

    elif resposta == 4:
        sair()
        break

    else:
        print('Resposta invalida')