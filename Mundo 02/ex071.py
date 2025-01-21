contCedulas50 = 0
contCedulas20 = 0
contCedulas10 = 0
contCedulas1 = 0
valor = float(input('Informe o valor a ser sacado: R$')) 

while valor != 0:
    if valor - 50 >= 0:
        valor -= 50
        contCedulas50 += 1
    elif valor - 20 >= 0:
        valor -= 20
        contCedulas20 += 1
    elif valor - 10 >= 0:
        valor -= 10
        contCedulas10 += 1
    else:
        valor -= 1
        contCedulas1 += 1
print(f'''Você receberá:
{contCedulas50} cédulas de R$50;
{contCedulas20} cédulas de R$20;
{contCedulas10} cédulas de R$10;
{contCedulas1} cédulas de R$1.''')
