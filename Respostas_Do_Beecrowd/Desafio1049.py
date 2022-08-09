a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            x = 'aguia'
        else:
            x = 'pomba'
    else:
        if c == 'onivoro':
            x = 'homem'
        else:
            x = 'vaca'

else:
    if b == 'inseto':
        if c == 'hematofago':
            x = 'pulga'
        else:
            x = 'lagarta'
    else:
        if c == 'hematofago':
            x = 'sanguessuga'
        else:
            x = 'minhoca'

print(x)