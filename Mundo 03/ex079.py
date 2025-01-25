listaNumeros: list[int] = []

while True:
    numero: int = int(input('Informe o número que deseja adicionar: '))
    if numero in listaNumeros:
        print('Número já adicionado.')
        continue
    else:
        listaNumeros.append(numero)
    print('Número adicionado!')
    adicionarMais: str = input('Quer continuar? [S/N]').strip().lower()
    if adicionarMais != 's':
        break
listaNumeros.sort()
print(f'Os números adicionados foram: {listaNumeros}')