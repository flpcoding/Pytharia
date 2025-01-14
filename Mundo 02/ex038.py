num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe mais um número inteiro: '))

if num1 > num2:
    print(f'O número {num1} é o maior.')
elif num2 > num1:
    print(f'O número {num2} é o maior.')
else:
    print('Os números são iguais.')