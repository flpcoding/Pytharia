
sexo = input('Digite teu gênero [M/F]: ').lower()

while sexo not in 'mf':
    print('Informação inválida, digite novamente.')
    sexo = input('Digite teu gênero [M/F]: ').lower()
