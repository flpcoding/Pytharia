primeiroTermo = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.: '))

progressao = primeiroTermo
contador = 1
total = 0
adicional = 10

while adicional != 0:
    total = total + adicional
    while contador <= total:
        print(f'{progressao}', end=' > ')
        progressao += razao

        contador += 1 

    print('Pausa\n')
    adicional = int(input('Quantos termos você quer mostrar a mais? '))
print('Acabou!')