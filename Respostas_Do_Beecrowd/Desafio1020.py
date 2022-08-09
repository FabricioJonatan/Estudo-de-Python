d  = int(input())

ano =  d//365
d = d - (ano*365)

mes = d//30
d = d - (mes*30)

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(d))