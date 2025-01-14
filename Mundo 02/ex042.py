reta1 = int(input('Informe o tamanho da primeira reta: '))
reta2 = int(input('Informe o tamanho da segunda reta: '))
reta3 = int(input('Informe o tamanho da terceira reta: '))

if reta1 + reta2 >= reta3 and reta3 + reta2 >= reta1 and reta1 + reta3 >= reta2:
    print('Forma um triângulo -', end=' ')
    if reta1 == reta2 == reta3:
        print('Equilátero.')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Isósceles.')
    else:
        print('Escaleno.')
else:
    print('Não forma um triângulo.')
