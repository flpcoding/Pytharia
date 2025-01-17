primeiroTermo = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.: '))
progressao = primeiroTermo

contador = 0

while contador < 10:
    progressao += razao
    print(f'{progressao}', end=' ')
    contador += 1

print('\n')