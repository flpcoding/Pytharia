numero = int(input('Informe um número: '))
maior = numero
menor = numero
soma = numero
contador = 1
flag = input('Deseja continuar [s/n]: ').lower().strip()
print('-'*20)

while flag == 's':
    contador += 1

    numero = int(input('Informe um número: '))
    soma += numero

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    
    flag = input('Deseja continuar [s/n]: ').lower().strip()
    print('-'*25)

media = soma / contador
print(f'Maior: {maior}\nMenor: {menor}\nMedia: {media}')
