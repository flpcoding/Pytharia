primeiroTermo = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.: '))

progressao = primeiroTermo
contador = 1

while contador <= 10:
    print(f'{progressao}', end=' > ')
    progressao += razao

    contador += 1 

print('Acabou!\n')
