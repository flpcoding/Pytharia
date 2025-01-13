valorCasa = float(input('Informe o valor da casa: R$'))
salarioComprador = float(input('Informe seu salário: R$'))
anosPagando = int(input('Em quantos anos pretende pagar? '))

prestacaoMaxima = salarioComprador * 30 / 100

if valorCasa / (anosPagando * 12) > prestacaoMaxima:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
