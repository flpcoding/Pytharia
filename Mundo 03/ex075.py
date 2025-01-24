n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
n4 = int(input('Quarto número: '))

numeros: tuple[int] = (n1, n2, n3, n4)

print(f'Você digitou os valores: {numeros}')

print(f'O número 9 apareceu {numeros.count(9)} vezes na lista;')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)}ª posição.')
else:
    print('O número 3 não apareceu na lista')

print('Os valores pares digitados foram:', end=' ')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
print('\n')
