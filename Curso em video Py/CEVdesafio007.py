nota1 = float(input('Qual a primeira nota deste aluno : '))
nota2 = float(input('Qual a segunda nota deste aluno : '))
media = (nota1 + nota2) / 2

print('As notas desse aluno foram {} e {}\nLogo a média deste aluno é : {}'.format(nota1, nota2, media))

if media > 8 :
    print('Parabéns!!')