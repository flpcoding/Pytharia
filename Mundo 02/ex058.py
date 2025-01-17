from random import randint

escolhaMaquina = randint(0,10)
escolhaPlayer = int(input('Escolha um número: '))

contadorTentativas = 1

while escolhaPlayer != escolhaMaquina:
    print('\nVocê errou! Tente novamente.')
    escolhaPlayer = int(input('Escolha um número: '))
    contadorTentativas += 1

print(f'\nApós {contadorTentativas} tentativas, você acertou!')
