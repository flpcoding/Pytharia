idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ''
acumuladorIdade = 0
contadorMulherComMenosDe20Anos = 0

for i in range(0, 4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F/NB): ').strip().upper()

    print('-'*20)

    acumuladorIdade += idade

    if sexo == 'M' and idade >= idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome

    if sexo == 'F' and idade < 20:
        contadorMulherComMenosDe20Anos += 1

mediaIdade = acumuladorIdade / 4

print(f'A média de idade do grupo é de {int(mediaIdade)} anos.')
print(f'O homem mais velho tem {idadeHomemMaisVelho} e se chama {nomeHomemMaisVelho}.')
print(f'Dos participantes, {contadorMulherComMenosDe20Anos} mulheres tinham menos de 20 anos.')