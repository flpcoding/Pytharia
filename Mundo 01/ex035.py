reta1 = int(input('Informe o tamanho da primeira reta: '))
reta2 = int(input('Informe o tamanho da segunda reta: '))
reta3 = int(input('Informe o tamanho da terceira reta: '))

if reta1 >= reta2 and reta1 >= reta3:
    if reta2 + reta3 >= reta1:
        print('O conjunto de retas forma um triângulo')
    else:
        print('O conjunto de retas não forma um triângulo')
elif reta2 >= reta1 and reta2 >= reta3:
    if reta1 + reta3 >= reta2:
        print('O conjunto de retas forma um triângulo')
    else:
        print('O conjunto de retas não forma um triângulo')
else:
    if reta2 + reta1 >= reta3:
        print('O conjunto de retas forma um triângulo')
    else:
        print('O conjunto de retas não forma um triângulo')
