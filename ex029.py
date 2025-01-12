velocidade = float(input('Velocidade do carro: '))

if velocidade > 80:
    print(f'Você foi multado!\nMulta: R${(velocidade - 80) * 7 :.2f}')
