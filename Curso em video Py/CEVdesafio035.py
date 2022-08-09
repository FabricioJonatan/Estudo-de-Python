print('\033[33m=-' * 20)
print('\033[34mAnalisador de triângulos!!')
print('\033[33m=-' * 20)

r1 = float(input('\033[39mPrimeira reta : '))
r2 = float(input('\033[39mSegunda reta : '))
r3 = float(input('\033[39mTerceira reta : '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mAs retas digitadas a cima PODEM formar um triângulo!!')
else:
    print('\033[31mAs retas digitadas a cima NÂO PODEM formar um triângulo!!')