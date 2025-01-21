while True:
    tabuada = int(input('Quer ver a tabuada de qual número: '))
    if tabuada < 0:
        break
    for fator in range(0, 11):
        print(f'{tabuada} x {fator:>2} = {tabuada * fator}')
    print('-'*10)
