from random import choice

opcoes = ['pedra', 'papel', 'tesoura']

escolhaPlayer = input('Opções:\n- Pedra\n- Papel\n- Tesoura\nEscolha: ').strip().lower()
escolhaMaquina = choice(opcoes)

if escolhaPlayer == 'pedra':
    if escolhaMaquina == 'papel':
        print('Escolhi papel, você perdeu!')
    elif escolhaMaquina == 'tesoura':
        print('Escolhi tesoura, você ganhou!')
    else:
        print('Também escolhi pedra, é um empate!')
elif escolhaPlayer == 'papel':
    if escolhaMaquina == 'tesoura':
        print('Escolhi tesoura, você perdeu!')
    elif escolhaMaquina == 'pedra':
        print('Escolhi pedra, você ganhou!')
    else:
        print('Também escolhi papel, é um empate!')
elif escolhaPlayer == 'tesoura':
    if escolhaMaquina == 'pedra':
        print('Escolhi pedra, você perdeu!')
    elif escolhaMaquina == 'papel':
        print('Escolhi papel, você ganhou!')
    else:
        print('Também escolhi tesoura, é um empate!')
else:
    print('Opção inválida.')    
