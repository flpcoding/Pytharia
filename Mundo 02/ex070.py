totalGastos = 0
contadorMaisDeMil = 0
nomeProdMaisBarato = ''
precoProdMaisBarato = 0

while True:
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: R$'))

    totalGastos += preco

    if preco > 1000:
        contadorMaisDeMil += 1

    if precoProdMaisBarato == 0:
        precoProdMaisBarato = preco
        nomeProdMaisBarato = nome
    else:
        if preco < precoProdMaisBarato:
            precoProdMaisBarato = preco
            nomeProdMaisBarato = nome

    mais = input('Deseja adicionar mais produtos [S/N]? ').strip().lower()
    print('\n')
    if mais == 'n':
        break

print(f'''O total da compra foi de: R${totalGastos:.2f}
- Tendo {contadorMaisDeMil} produtos custando mais de mil reais.
- E de todos os produtos {nomeProdMaisBarato}, foi o mais barato.\n''')