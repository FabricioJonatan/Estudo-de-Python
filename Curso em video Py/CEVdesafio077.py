palavras = (input('Digite alguma palavra qualquer : '), input('Digite outra palavra qualquer : '),
input('Digite outra palavra qualquer : '), input('Digite a ultima palavra qualquer : '))

for pala in palavras:
    print(f'\nNa palavra "{pala.capitalize().strip()}" temos ', end = '')

    for vogal in pala:
        if vogal in 'aeiou':
            print(f'{vogal} ', end = '')
