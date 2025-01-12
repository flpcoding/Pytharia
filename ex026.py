frase = input('Digite uma frase: ').strip().lower()

print(f'A letra "A" apareceu {frase.count('a')} vezes;')
print(f'Ela apareceu pela primeira vez na {frase.find('a') + 1}° posição;')
print(f'E apareceu por último na {frase.rfind('a') + 1}° posição.')
