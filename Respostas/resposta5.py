contador = 0

senha_cadastro = input('Digite a senah que deseja cadastrar : ')

while contador != 3:
    senha = input('\nDigite a senha cadastrada para entrar : ')

    if senha == senha_cadastro:
        print('====Acesso liberado ao sistema IFCE====')
        break
    else:
        print('Senha inválida!!')

    contador += 1

    if contador == 3:
        print('==== ACESSO NÃO LIBERADO ====')
    