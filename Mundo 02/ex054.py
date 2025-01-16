import datetime

contador = 0
anoAtual = datetime.date.today().year

for i in range(0, 7):
    anoNascimento = int(input('Informe seu ano de nascimento: '))
    if anoAtual - anoNascimento >= 18:
        contador += 1
    
print(f'Das 7 pessoas listadas, {contador} são maiores de idade.')