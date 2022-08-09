expressão = input('Digite sua expressão matemática aqui : ')
parenteses = []

for simbolos in expressão:
    if simbolos == '(':
        parenteses.append('(')

    elif simbolos == ')':
        if len(parenteses) > 0:
            parenteses.pop()

        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('Sua expressão é válida!!')
else:
    print('Sua expressão está errada!!')
