numero = int(input('Informe um número: '))

isPrimo = True

for i in range(1, numero):
    if i != 1 and i != numero and numero % i == 0:
        isPrimo = False

print(f'{numero} é um número primo? {isPrimo}')
