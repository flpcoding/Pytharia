ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print('É bissexto!')
elif ano % 400 == 0:
    print('É bissexto!')
else:
    print('Não é bissexto.')
