numero = int(input('Informe um número: '))
x = numero
valorFatorial = 1

while numero > 0:
    valorFatorial *= numero
    numero -= 1
print(f'{x}! = {valorFatorial}')
