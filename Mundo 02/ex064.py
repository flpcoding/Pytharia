numero = int(input('Número: '))
soma = 0
contador = 0

while numero != 999:
    contador += 1
    soma += numero

    numero = int(input('Número: '))

print(f'Foram escritos {contador} números, e a soma deles é: {soma}')
