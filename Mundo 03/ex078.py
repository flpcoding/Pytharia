listaNumeros: list[int] = []
for i in range(0, 5):
    numero = int(input('Informe um número: '))
    listaNumeros.append(numero)

print(f'Os números listados foram: {listaNumeros}')
print(f'O maior número digitado foi {max(listaNumeros)} na {listaNumeros.index(max(listaNumeros)) + 1}ª posição.')
print(f'O menor número digitado foi {min(listaNumeros)} na {listaNumeros.index(min(listaNumeros)) + 1}ª posição.')
