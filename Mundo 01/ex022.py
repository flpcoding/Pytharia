nome = input('Informe seu nome completo: ').strip()

print(f'{nome.upper()}')
print(f'{nome.lower()}')

nomeDividido = nome.split()

print(f'Seu nome completo tem {len(''.join(nomeDividido))} letras')
print(f'Seu primeiro nome tem {len(nomeDividido[0])} letras')
