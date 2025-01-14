from datetime import datetime
anoNascimento = int(input('Informe o seu ano de nascimento: '))
anoAtual = datetime.date.today().year

print(anoAtual)

if anoAtual - anoNascimento < 18:
    print(f'Faltam {18 - (anoAtual - anoNascimento)} anos para você se alistar.')
elif anoAtual - anoNascimento == 18:
    print(f'Você tem {anoAtual - anoNascimento} anos, está na hora de alistar-se.')
else:
    print(f'Você está atrasado {anoAtual - anoNascimento - 18} ano(s) para o alistamento.')
