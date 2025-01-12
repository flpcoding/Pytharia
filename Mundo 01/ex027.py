nome = input('Digite um nome: ').strip()

print(f'Primeiro nome: {nome[:nome.find(' ')]}')
print(f'Último nome: {nome[nome.rfind(' ') + 1:]}')
