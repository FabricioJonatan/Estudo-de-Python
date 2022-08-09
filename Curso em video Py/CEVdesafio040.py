nota1 = float(input('Qual foi a Primeira nota deste aluno : '))
nota2 = float(input('Qual foi a Segunda nota deste aluno : '))
media = (nota1 + nota2) / 2

print('A média deste aluno baseado nas notas {:.1f} e {:.1f} foi de {:.1f}'.format(nota1, nota2, media))

if media >= 7:
    print('Este aluno foi \033[1;32mAPROVADO!!\033[m Parabéns!')
elif media >= 5:
    print('Este aluno está de \033[1;33mRECUPERAÇÃO!!\033[m Precisa prestar mais atenção!')
else:
    print('Este aluno esá \033[1;31mREPROVADO!!\033[m Precisa estudar mais!!!')