num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

menu = int(input('''Opções: 
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
Escolha: 
'''))

while menu != 5:
    match menu:
        case 1:
            print(f'{num1} + {num2} = {num1 + num2}')
        case 2:
            print(f'{num1} x {num2} = {num1 * num2}')
        case 3:
            print(f'{num1} é maior' if num1 >= num2 else f'{num2} é maior\n')
        case 4:
            num1 = int(input('Informe o primeiro número: '))
            num2 = int(input('Informe o segundo número: '))
        case _:
            print('Opção inválida! Tente novamente.\n')    

    menu = int(input('''Opções: 
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
Escolha: '''))
