x,y = map(int,input().split())

n = []
i, k = 0, 0

while i < y-x:
    for c in range(1, x + 1):
        n.append(i + 1)
        n[k] = str(n[k])
        i = i + 1
        k += 1
   
    k = 0
    n = ' '.join(n)
    print(n)
    n = []

for w in range(y - x, y):
    n.append(w + 1)
    n[k] = str(n[k])
    k = k + 1


n = ' '.join(n)
print(n)