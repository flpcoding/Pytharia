contadorMaioresDe18 = 0
contadorHomens = 0
contadorMulheresMenosDe20 = 0

while True:
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu gênero [M/F]: ').strip().lower()

    if idade > 18:
        contadorMaioresDe18 += 1
    if sexo == 'm':
        contadorHomens += 1
    if sexo == 'f' and idade < 20:
        contadorMulheresMenosDe20 += 1
    mais = input('Deseja adicionar mais pessoas [S/N]? ').strip().lower()
    print('\n')
    if mais == 'n':
        break

print(f'''Foram adicionados na lista:
- {contadorMaioresDe18} maiores de 18 anos
- {contadorHomens} homens
- {contadorMulheresMenosDe20} mulheres com menos de 20 anos\n''')
