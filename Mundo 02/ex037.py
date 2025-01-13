numero = int(input('Informe um número inteiro: '))
menu = int(input('Escolha a base de conversão:\n1- Binário\n2- Octal\n3- Hexadecimal\nEscolha: '))

match menu:
    case 1:
        print(f'O número {numero} é {bin(numero)} em binário.')
    case 2:
        print(f'O número {numero} é {oct(numero)} em octal.')
    case 3:
        print(f'O número {numero} é {hex(numero)} em hexadecimal.')
    case _:
        print('Opção inválida.')
