soma = 0

for i in range(0, 6):
    numero = int(input('Informe um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
print(f'Resultado das somas é: {soma}')