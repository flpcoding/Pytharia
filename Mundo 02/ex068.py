from random import randint

contadorVitorias = 0

while True:
    escolhaPlayerNum = int(input('Escolha um número: '))
    escolhaPlayerParOuImpar = input('Escolha par ou ímpar [P/I]:').strip().lower()
    escolhaMaquina = randint(0, 10)

    if (escolhaMaquina + escolhaPlayerNum) % 2 == 0 and escolhaPlayerParOuImpar == 'p':
        print(f'A máquina escolheu {escolhaMaquina}, {escolhaPlayerNum} mais {escolhaMaquina} é {escolhaPlayerNum + escolhaMaquina}, que é par.')
        print('Você ganhou!\n')
        contadorVitorias += 1
    elif (escolhaMaquina + escolhaPlayerNum) % 2 != 0 and escolhaPlayerParOuImpar == 'i':
        print(f'A máquina escolheu {escolhaMaquina}, {escolhaPlayerNum} mais {escolhaMaquina} é {escolhaPlayerNum + escolhaMaquina}, que é ímpar.')
        print('Você ganhou!\n')
        contadorVitorias += 1
    else:
        if escolhaPlayerParOuImpar == 'p':
            print(f'A máquina escolheu {escolhaMaquina}, {escolhaPlayerNum} mais {escolhaMaquina} é {escolhaPlayerNum + escolhaMaquina}, que é ímpar.')
        else:
            print(f'A máquina escolheu {escolhaMaquina}, {escolhaPlayerNum} mais {escolhaMaquina} é {escolhaPlayerNum + escolhaMaquina}, que é par.')
        print('Você perdeu!', end=' ')
        break

print(f'Tendo {contadorVitorias} vitórias consecutivas.')
