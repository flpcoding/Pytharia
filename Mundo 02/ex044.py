preco = float(input('Informe o preço do produto: R$'))
menu = int(input('''Opções de pagamento:
1- À vista cheque/dinheiro (10% de desconto)
2- À vista no cartão (5% de desconto)
3- Duas vezes no cartão
4- Três vezes ou mais no cartão (20% de juros)
Escolha: '''))

match menu:
    case 1:
        print(f'O valor do produto será de: R${preco - (preco * 10 / 100) :.2f}')
    case 2:
        print(f'O valor do produto será de: R${preco - (preco * 5 / 100) :.2f}')
    case 3:
        print(f'O valor do produto será de: R${preco :.2f}')
    case 4:
        print(f'O valor do produto será de: R${preco + (preco * 20 / 100) :.2f}')
    case _:
        print('Opção inválida.')
