decimal = int(input('Digite o numero que deseja converter pra Hexadecimal : '))

n1 = decimal % 16
decimal //= 16
n2 = decimal % 16
decimal //= 16
n3 = decimal % 16
n4 = decimal // 16


if n1 == 10:
    n1 = 'A'
if n1 == 11:
    n1 = 'B'
if n1 == 12:
    n1 = 'C'
if n1 == 13:
    n1 = 'D'
if n1 == 14:
    n1 = 'E'
if n1 == 15:
    n1 = 'F'

if n2 == 10:
    n2 = 'A'
if n2 == 11:
    n2 = 'B'
if n2 == 12:
    n2 = 'C'
if n2 == 13:
    n2 = 'D'
if n2 == 14:
    n2 = 'E'
if n2 == 15:
    n2 = 'F'

if n3 == 10:
    n3 = 'A'
if n3 == 11:
    n3 = 'B'
if n3 == 12:
    n3 = 'C'
if n3 == 13:
    n3 = 'D'
if n3 == 14:
    n3 = 'E'
if n3 == 15:
    n3 = 'F'

if n4 == 10:
    n4 = 'A'
if n4 == 11:
    n4 = 'B'
if n4 == 12:
    n4 = 'C'
if n4 == 13:
    n4 = 'D'
if n4 == 14:
    n4 = 'E'
if n4 == 15:
    n4 = 'F'

print('{} {} {} {}'.format(n4, n3, n2, n1))