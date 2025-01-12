from random import randint

escolhaMaquina = randint(0, 5)
escolhaPlayer = int(input('Digite um número de 0 a 5: '))

print('Você acertou!' if escolhaPlayer == escolhaMaquina else 'Você errou!')
