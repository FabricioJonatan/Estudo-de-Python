pessoas = [['cleiton', 35, 1.50, 70]['junin',20, 1.70, 80]['carlos', 10, 1.00, 40]]

while True:
    print('==' * 20)
    nome = input('Digite o nome da pessoa : ')
    idade = int(input('Digite a idade da pessoa :'))
    altura = float(input('Digite a altura desta pessoa : '))
    peso = float(input('Digite o peso dessa pessoa : '))
    print('==' * 20)

    pessoa = [nome, idade, altura, peso]
    pessoas.append(pessoa)

    continuar = input('Deseja cadastrar mais alguém? [S/N] :').lower()
    if continuar == 'n': break

for i in range(len(pessoas)):
    print(pessoas[i])