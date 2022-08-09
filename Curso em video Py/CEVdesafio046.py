from time import sleep

print('Os fogos de artifício começarão em . . .')
sleep(1)

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('\033[34mKAH\033[32m BUM\033[35m POW\033[36m BUUUM\033[m!!!!')