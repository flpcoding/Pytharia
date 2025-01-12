salario = float(input('Digite o salário: '))

if salario >= 1250:
    print(f'Com um aumento de 10% o seu salário será de: R${salario + salario * 10 / 100}')
else:
    print(f'Com um aumento de 15% o seu salário será de: R${salario + salario * 15 / 100}')
