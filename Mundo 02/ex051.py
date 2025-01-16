primeiroTermo = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.: '))

progressao = primeiroTermo

for c in range(0, 10):
    progressao += razao
    print(f'{progressao}', end=' ')

print('\n')
