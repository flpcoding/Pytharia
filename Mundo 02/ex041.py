import datetime

anoNascimento = int(input('Informe o ano de nascimento do atleta: '))
anoAtual = datetime.date.today().year

idade = anoAtual - anoNascimento

if idade <= 9:
    print('Mirim.')
elif idade <= 14:
    print('Infantil.')
elif idade <= 19:
    print('Junior.')
elif idade <= 25:
    print('Sênior.')
else:
    print('Master.')