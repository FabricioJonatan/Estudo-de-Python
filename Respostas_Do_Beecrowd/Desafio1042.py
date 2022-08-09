a, b, c = map(int, input().split(' '))

if a > b and a > c:
    maior1 = a
elif b > a and b > c:
    maior1 = b
else:
    maior1 = c

if a > b and a < c or a < b and a > c:
    maior2 = a
elif b > a and b < c or b < a and b > c:
    maior2 = b
else:
    maior2 = c

if a < b and a < c or a < b and a < c:
    maior3 = a
elif b < a and b < c or b < a and b < c:
    maior3 = b
else:
    maior3 = c

print(maior3)
print(maior2)
print(maior1)
print('')
print(a)
print(b)
print(c)