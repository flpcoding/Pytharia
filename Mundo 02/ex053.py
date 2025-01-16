frase = input('Diga um frase: ')
fraseInvertida =''

for letra in range(len(frase) -1, -1, -1):
    fraseInvertida += frase[letra]

print(f'"{frase}" é Palindromo!' if frase == fraseInvertida else f'"{frase}" não é Palindromo!')
