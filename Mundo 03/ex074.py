from random import randint

listaNumeros: tuple[int] = (randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(f'Os valores sorteados foram: {listaNumeros}')
print(f'O maior dos valores sorteados foi: {max(listaNumeros)}')
print(f'O menor dos valores sorteados foi: {min(listaNumeros)}')
