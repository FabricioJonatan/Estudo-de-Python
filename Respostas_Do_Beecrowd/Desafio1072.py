quantidade = int(input())
inn = 0
out = 0

for c in range(1, quantidade + 1):
    numero = int(input())
    if numero in range(10, 21):
        inn += 1
    else:
        out += 1

print('{} in'.format(inn))
print('{} out'.format(out))