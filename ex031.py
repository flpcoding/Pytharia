kms = float(input('Diga a distâncida da viagem em quilômetros: '))

if kms <= 200:
    print(f'O preço da passagem será: R${kms * 0.50 :.2f}')
else: 
    print(f'O preço da passagem será: R${kms * 0.45 :.2f}')
