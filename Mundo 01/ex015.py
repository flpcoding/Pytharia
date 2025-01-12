kmRodados = float(input('Informe a quantidade de quilometros rodados: '))
diasAlugados = int(input('Informe quantos dias o carro ficou alugado: '))
aPagar = kmRodados * 0.15 + diasAlugados * 60
print(f'Você deverá pagar: R${aPagar :.2f}')
