numero = int(input('Informe um número: '))
t1 = 1
t2 = 0
t3 = 0

while t3 <= numero:
    t3 = t1 + t2
    t2 = t1
    t1 = t3

    print(t3, end=' > ')
print('Acabou!\n')
