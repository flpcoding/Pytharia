palavras: tuple[str] = ('uga', 'buga', 'desu desu', 'nee')

for palavra in palavras:
    print(f'A palavra "{palavra}" tem como vogais as letras:',end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ') 
    print('\n')
